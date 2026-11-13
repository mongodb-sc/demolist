#!/usr/bin/env python3
"""Rebuild README.md from the mongodb-sc GitHub org and Drone deploy logs.

Requires the GitHub CLI, with its token authorized for mongodb-sc SSO, and
DRONE_TOKEN from https://drone.corp.mongodb.com/account.
"""

from __future__ import annotations

import base64
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import TypedDict

DRONE_SERVER = os.environ.get("DRONE_SERVER", "https://drone.corp.mongodb.com").rstrip("/")
ORG = "mongodb-sc"
# shortcut: a successful deploy older than this window is missed, raise it if a pipeline's last success falls off the list.
BUILD_WINDOW = 25
HOST_RE = re.compile(
    r"(?:https?://)?([a-z0-9][a-z0-9.-]*\.corp\.mongodb\.com)(/[^\s\"'<>),]*)?",
    re.IGNORECASE,
)
SKIP_HOSTS = {
    "api.staging.corp.mongodb.com",
    "api.prod.corp.mongodb.com",
    "drone.corp.mongodb.com",
}
LOGIN_HOSTS = {
    "login.corp.mongodb.com",
    "login.staging.corp.mongodb.com",
}
HOSTS_KEY_RE = re.compile(r"(?:^|\s)hosts\s*:")
BARE_HOST_RE = re.compile(
    r"^\s*-\s+([a-z0-9][a-z0-9.-]*\.corp\.mongodb\.com)\s*$",
    re.IGNORECASE,
)


class Repo(TypedDict):
    name: str
    visibility: str
    language: str
    description: str


class Endpoint(TypedDict):
    url: str
    repo: str
    description: str


def main() -> None:
    if "--self-check" in sys.argv:
        self_check()
        print("self-check ok")
        return
    token = os.environ.get("DRONE_TOKEN", "")
    if not token:
        raise SystemExit("Set DRONE_TOKEN from https://drone.corp.mongodb.com/account")
    repos = github_repos()
    by_name = {repo["name"]: repo for repo in repos}
    endpoints, quiet = drone_endpoints(token, by_name)
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(render(repos, endpoints, quiet, generated))
    print(f"wrote {path}: {len(repos)} repositories, {len(endpoints)} endpoints")


def github_repos() -> list[Repo]:
    raw = gh_api(f"orgs/{ORG}/repos?per_page=100&type=all")
    repos: list[Repo] = []
    for item in raw:
        visibility = str(item.get("visibility") or "public")
        label = visibility[:1].upper() + visibility[1:]
        if item.get("archived"):
            label += " archive"
        language = item.get("language") or ""
        repos.append(
            {
                "name": str(item["name"]),
                "visibility": label,
                "language": str(language),
                "description": str(item.get("description") or "").strip(),
            }
        )
    repos.sort(key=lambda repo: repo["name"].casefold())
    return repos


def drone_endpoints(token: str, by_name: dict[str, Repo]) -> tuple[list[Endpoint], list[str]]:
    listed = drone_json(token, "/api/user/repos")
    if not isinstance(listed, list):
        raise SystemExit("Drone /api/user/repos did not return a list")
    active = [
        repo
        for repo in listed
        if repo.get("namespace") == ORG and repo.get("active") and int(repo.get("counter") or 0) > 0
    ]
    found: list[Endpoint] = []
    quiet: list[str] = []
    for repo in sorted(active, key=lambda item: str(item["name"]).casefold()):
        name = str(repo["name"])
        description = by_name.get(name, {}).get("description", "")
        urls = urls_for_repo(token, repo)
        if not urls:
            quiet.append(name)
            continue
        for url in urls:
            found.append({"url": url, "repo": name, "description": description})
    found.sort(key=lambda item: item["url"])
    return found, quiet


def urls_for_repo(token: str, repo: dict[str, object]) -> list[str]:
    name = str(repo["name"])
    quoted = urllib.parse.quote(name, safe="")
    builds = drone_json(token, f"/api/repos/{ORG}/{quoted}/builds?per_page={BUILD_WINDOW}")
    if not isinstance(builds, list):
        return []
    seen: dict[str, list[str]] = {}
    for summary in builds:
        number = summary.get("number")
        if not isinstance(number, int):
            continue
        build = drone_json(token, f"/api/repos/{ORG}/{quoted}/builds/{number}")
        if not isinstance(build, dict):
            continue
        for stage in build.get("stages") or []:
            stage_name = str(stage.get("name") or "")
            if not stage_name or stage_name in seen:
                continue
            steps = [
                step
                for step in stage.get("steps") or []
                if "deploy" in str(step.get("name") or "").lower() and step.get("status") == "success"
            ]
            if not steps:
                continue
            urls: list[str] = []
            for step in steps:
                log = drone_text(
                    token,
                    f"/api/repos/{ORG}/{quoted}/builds/{number}/logs/{stage.get('number')}/{step.get('number')}",
                )
                urls.extend(public_urls(log))
            seen[stage_name] = dedupe(urls)
    if not seen:
        return []
    fill_from_config(repo, seen)
    return dedupe(url for urls in seen.values() for url in urls)


def fill_from_config(repo: dict[str, object], seen: dict[str, list[str]]) -> None:
    if all(seen.values()):
        return
    name = str(repo["name"])
    branch = str(repo.get("default_branch") or "main")
    config_path = str(repo.get("config_path") or ".drone.yml")
    try:
        yml = github_file(name, config_path, branch)
    except SystemExit:
        return
    blocks = re.split(r"(?=^kind:\s*pipeline\b)", yml, flags=re.MULTILINE)
    by_pipeline: dict[str, str] = {}
    for block in blocks:
        match = re.search(r"^name:\s*(\S+)\s*$", block, re.MULTILINE)
        if match:
            by_pipeline[match.group(1)] = block
    for stage_name, urls in seen.items():
        if urls:
            continue
        block = by_pipeline.get(stage_name, "")
        hosts = ingress_urls(block)
        for path in re.findall(r"[A-Za-z0-9_./-]+\.(?:yaml|yml)", block):
            if path == config_path:
                continue
            try:
                hosts.extend(ingress_urls(github_file(name, path, branch)))
            except SystemExit:
                continue
        seen[stage_name] = dedupe(hosts)


def github_file(repo: str, path: str, ref: str) -> str:
    quoted_repo = urllib.parse.quote(repo, safe="")
    quoted_path = urllib.parse.quote(path, safe="/")
    payload = gh_api_one(
        f"repos/{ORG}/{quoted_repo}/contents/{quoted_path}?ref={urllib.parse.quote(ref, safe='')}"
    )
    if not isinstance(payload, dict) or "content" not in payload:
        raise SystemExit(f"no content for {repo}/{path}")
    return base64.b64decode(str(payload["content"])).decode("utf-8", errors="replace")


def public_urls(text: str) -> list[str]:
    body = log_text(text)
    found: list[str] = []
    for match in HOST_RE.finditer(body):
        host = match.group(1).lower()
        if host in SKIP_HOSTS:
            continue
        path = (match.group(2) or "/").rstrip(").,;\"'")
        if not path.startswith("/"):
            path = "/" + path
        found.append(f"https://{host}{path}")
    return dedupe(found)


def ingress_urls(text: str) -> list[str]:
    """Ingress hosts from a Drone pipeline or Helm values file.

    Deploy logs stay on public_urls. Values files mention OAuth, JWKS, and
    callbacks that are not the published application.
    """
    lines = text.splitlines()
    found: list[str] = []
    for index, raw in enumerate(lines):
        line = raw.split("#", 1)[0]
        cursor = index - 1
        while cursor >= 0 and not lines[cursor].strip():
            cursor -= 1
        previous = lines[cursor].split("#", 1)[0] if cursor >= 0 else ""
        ingress = marks_ingress(line) or marks_ingress(previous)
        if not ingress and BARE_HOST_RE.match(line) is None:
            continue
        for match in HOST_RE.finditer(line):
            host = match.group(1).lower()
            path = (match.group(2) or "/").rstrip(").,;\"'")
            if host in SKIP_HOSTS or host in LOGIN_HOSTS or path not in ("", "/"):
                continue
            found.append(f"https://{host}/")
    return dedupe(found)


def marks_ingress(line: str) -> bool:
    return "ingress.hosts" in line.lower() or HOSTS_KEY_RE.search(line) is not None


def log_text(payload: str) -> str:
    stripped = payload.strip()
    if not stripped.startswith("["):
        return payload
    try:
        data = json.loads(stripped)
    except json.JSONDecodeError:
        return payload
    if not isinstance(data, list):
        return payload
    return "".join(str(item.get("out") or "") for item in data if isinstance(item, dict))


def dedupe(urls: object) -> list[str]:
    seen: list[str] = []
    for url in urls:
        if url and url not in seen:
            seen.append(str(url))
    return seen


def render(repos: list[Repo], endpoints: list[Endpoint], quiet: list[str], generated: str) -> str:
    repos = sorted(repos, key=lambda repo: repo["name"].casefold())
    endpoints = sorted(endpoints, key=lambda endpoint: endpoint["url"])
    quiet = sorted(quiet, key=str.casefold)
    lines = [
        "# mongodb-sc demos",
        "",
        "Repositories in [mongodb-sc](https://github.com/mongodb-sc) and the HTTP endpoints their [Drone](https://drone.corp.mongodb.com/) deploys publish.",
        "",
        "Refresh this file with `python3 refresh.py`. The GitHub CLI token has to be authorized for the mongodb-sc single sign-on organization, and `DRONE_TOKEN` comes from the [Drone account page](https://drone.corp.mongodb.com/account). `DRONE_SERVER` defaults to `https://drone.corp.mongodb.com`.",
        "",
        "An endpoint is the application URL from the latest successful deploy step of each Drone pipeline, in the newest "
        f"{BUILD_WINDOW} builds. Helm notes that only print a port-forward are ignored. When a successful deploy prints no URL, hosts are read from that pipeline's values files. Drone's chart notes use `http`; the links below use `https`.",
        "",
        f"Refreshed {generated}. {len(repos)} repositories, {len(endpoints)} published endpoints.",
        "",
        "## Published endpoints",
        "",
        "| Endpoint | Repository | Description |",
        "| --- | --- | --- |",
    ]
    for endpoint in endpoints:
        repo = endpoint["repo"]
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(endpoint["url"], link=endpoint["url"]),
                    cell(repo, link=f"https://github.com/{ORG}/{repo}"),
                    cell(endpoint["description"]),
                ]
            )
            + " |"
        )
    if quiet:
        names = ", ".join(f"[{cell(name)}](https://github.com/{ORG}/{name})" for name in quiet)
        lines.extend(["", f"Active Drone repos whose latest successful deploy has no public URL: {names}."])
    lines.extend(
        [
            "",
            "## Repositories",
            "",
            "| Repository | Visibility | Language | Description |",
            "| --- | --- | --- | --- |",
        ]
    )
    for repo in repos:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(repo["name"], link=f"https://github.com/{ORG}/{repo['name']}"),
                    cell(repo["visibility"]),
                    cell(repo["language"]),
                    cell(repo["description"]),
                ]
            )
            + " |"
        )
    lines.append("")
    return "\n".join(lines)


def cell(value: str, link: str = "") -> str:
    text = value.replace("\n", " ").replace("|", "\\|").strip()
    if not link:
        return text
    return f"[{text}]({link})"


def gh_api(path: str) -> list[dict[str, object]]:
    result = subprocess.run(
        ["gh", "api", "--paginate", path],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip() or "gh api failed"
        raise SystemExit(message)
    return parse_json_pages(result.stdout)


def gh_api_one(path: str) -> object:
    result = subprocess.run(
        ["gh", "api", path],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or "gh api failed"
        raise SystemExit(message)
    return json.loads(result.stdout)


def parse_json_pages(raw: str) -> list[dict[str, object]]:
    decoder = json.JSONDecoder()
    items: list[dict[str, object]] = []
    index = 0
    text = raw.strip()
    while index < len(text):
        while index < len(text) and text[index].isspace():
            index += 1
        if index >= len(text):
            break
        obj, end = decoder.raw_decode(text, index)
        index = end
        pages = obj if isinstance(obj, list) else [obj]
        if pages and isinstance(pages[0], list):
            for page in pages:
                items.extend(entry for entry in page if isinstance(entry, dict))
        else:
            items.extend(entry for entry in pages if isinstance(entry, dict))
    return items


def drone_json(token: str, path: str) -> object:
    return json.loads(drone_text(token, path))


def drone_text(token: str, path: str) -> str:
    request = urllib.request.Request(
        DRONE_SERVER + path,
        headers={"Authorization": f"Bearer {token}"},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Drone {path} returned {exc.code}: {body[:300]}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"Drone {path} failed: {exc.reason}") from exc


def self_check() -> None:
    sample = (
        '[{"out":"Access the application at:\\n"},'
        '{"out":"  http://rdbms-comparator.sa-demo.staging.corp.mongodb.com/\\n"},'
        '{"out":"Visit http://127.0.0.1:8080\\n"},'
        '{"out":"GET:https://api.staging.corp.mongodb.com/api\\n"},'
        '{"out":"http://sa-blueprint-mdm.sa-demo.staging.corp.mongodb.com/api/\\n"}]'
    )
    assert public_urls(sample) == [
        "https://rdbms-comparator.sa-demo.staging.corp.mongodb.com/",
        "https://sa-blueprint-mdm.sa-demo.staging.corp.mongodb.com/api/",
    ]
    pages = parse_json_pages('[{"name":"a"}]\n[{"name":"b"}]')
    assert [item["name"] for item in pages] == ["a", "b"]
    yml = """
kind: pipeline
name: web
steps:
- name: deploy
  settings:
    values_files: [web/staging.yaml]
---
kind: pipeline
name: gateway
steps:
- name: deploy-gateway
  settings:
    values_files: [gateway/staging.yaml]
"""
    blocks = re.split(r"(?=^kind:\s*pipeline\b)", yml, flags=re.MULTILINE)
    names = []
    for block in blocks:
        match = re.search(r"^name:\s*(\S+)\s*$", block, re.MULTILINE)
        if match:
            names.append(match.group(1))
    assert names == ["web", "gateway"]
    assert public_urls("hosts:\n  - solutionstudio.sa.staging.corp.mongodb.com\n") == [
        "https://solutionstudio.sa.staging.corp.mongodb.com/"
    ]
    values = """ingress:
  hosts:
    - solutionstudio.sa.staging.corp.mongodb.com
OAUTH_ISSUER: https://login.corp.mongodb.com/
JWKS: https://login.corp.mongodb.com/.well-known/jwks.json
callback: https://solutionstudio.sa.staging.corp.mongodb.com/input-aggregator/api/me/glean/callback
trino: https://trino-jwt-gateway.dataplatform.prod.corp.mongodb.com/
"""
    assert ingress_urls(values) == ["https://solutionstudio.sa.staging.corp.mongodb.com/"]


if __name__ == "__main__":
    main()
