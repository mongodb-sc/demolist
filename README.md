# mongodb-sc demos

Repositories in [mongodb-sc](https://github.com/mongodb-sc) and the HTTP endpoints their [Drone](https://drone.corp.mongodb.com/) deploys publish.

Refresh this file with `python3 refresh.py`. The GitHub CLI token has to be authorized for the mongodb-sc single sign-on organization, and `DRONE_TOKEN` comes from the [Drone account page](https://drone.corp.mongodb.com/account). `DRONE_SERVER` defaults to `https://drone.corp.mongodb.com`.

An endpoint is the application URL from the latest successful deploy step of each Drone pipeline, in the newest 25 builds. Helm notes that only print a port-forward are ignored. When a successful deploy prints no URL, hosts are read from that pipeline's values files. Drone's chart notes use `http`; the links below use `https`.

Refreshed 2026-11-13. 108 repositories, 21 published endpoints.

## Published endpoints

| Endpoint | Repository | Description |
| --- | --- | --- |
| [https://atlas-demo-wl.sa-demo.staging.corp.mongodb.com/](https://atlas-demo-wl.sa-demo.staging.corp.mongodb.com/) | [AtlasDemoWL](https://github.com/mongodb-sc/AtlasDemoWL) |  |
| [https://catalyst.sa-demo.staging.corp.mongodb.com/](https://catalyst.sa-demo.staging.corp.mongodb.com/) | [catalyst](https://github.com/mongodb-sc/catalyst) | From discovery context to a ready-to-present MongoDB proof — then close the gap with live evidence. MongoDB SAs: discovery context in, a guided live proof out, feasibility gap closed. |
| [https://champion-builder.sa.staging.corp.mongodb.com/](https://champion-builder.sa.staging.corp.mongodb.com/) | [champion-tracker-v3](https://github.com/mongodb-sc/champion-tracker-v3) | Multi-tenant champion tracking app. Each team gets their own isolated data in MongoDB Atlas, secured with Clerk authentication. |
| [https://discobuddy.sa-demo.staging.corp.mongodb.com/](https://discobuddy.sa-demo.staging.corp.mongodb.com/) | [discobuddy](https://github.com/mongodb-sc/discobuddy) | A local discovery co-pilot for Solutions Architects: live call transcription and context-aware next-question suggestions powered by Gemini. |
| [https://rdbms-comparator.sa-demo.staging.corp.mongodb.com/](https://rdbms-comparator.sa-demo.staging.corp.mongodb.com/) | [rdbms-comparator](https://github.com/mongodb-sc/rdbms-comparator) | Demo tool highlighting benefits of MongoDB over Postgres |
| [https://sa-blueprint-client-intent.sa-demo.staging.corp.mongodb.com/](https://sa-blueprint-client-intent.sa-demo.staging.corp.mongodb.com/) | [sa-blueprint-client-intent](https://github.com/mongodb-sc/sa-blueprint-client-intent) |  |
| [https://sa-blueprint-client-intent.sa-demo.staging.corp.mongodb.com/api/](https://sa-blueprint-client-intent.sa-demo.staging.corp.mongodb.com/api/) | [sa-blueprint-client-intent](https://github.com/mongodb-sc/sa-blueprint-client-intent) |  |
| [https://sa-blueprint-continuous-authorization.sa-demo.staging.corp.mongodb.com/](https://sa-blueprint-continuous-authorization.sa-demo.staging.corp.mongodb.com/) | [sa-blueprint-continuous-authorization](https://github.com/mongodb-sc/sa-blueprint-continuous-authorization) |  |
| [https://sa-blueprint-continuous-authorization.sa-demo.staging.corp.mongodb.com/api/](https://sa-blueprint-continuous-authorization.sa-demo.staging.corp.mongodb.com/api/) | [sa-blueprint-continuous-authorization](https://github.com/mongodb-sc/sa-blueprint-continuous-authorization) |  |
| [https://sa-blueprint-marketing-personalization.sa-demo.staging.corp.mongodb.com/](https://sa-blueprint-marketing-personalization.sa-demo.staging.corp.mongodb.com/) | [sa-blueprint-marketing-personalization](https://github.com/mongodb-sc/sa-blueprint-marketing-personalization) | Marketing Personalization |
| [https://sa-blueprint-marketing-personalization.sa-demo.staging.corp.mongodb.com/api/](https://sa-blueprint-marketing-personalization.sa-demo.staging.corp.mongodb.com/api/) | [sa-blueprint-marketing-personalization](https://github.com/mongodb-sc/sa-blueprint-marketing-personalization) | Marketing Personalization |
| [https://sa-blueprint-mdm.sa-demo.staging.corp.mongodb.com/](https://sa-blueprint-mdm.sa-demo.staging.corp.mongodb.com/) | [sa-blueprint-mdm](https://github.com/mongodb-sc/sa-blueprint-mdm) | MDM Demo |
| [https://sa-blueprint-mdm.sa-demo.staging.corp.mongodb.com/api/](https://sa-blueprint-mdm.sa-demo.staging.corp.mongodb.com/api/) | [sa-blueprint-mdm](https://github.com/mongodb-sc/sa-blueprint-mdm) | MDM Demo |
| [https://sa-blueprint-rule-configurator.sa-demo.staging.corp.mongodb.com/](https://sa-blueprint-rule-configurator.sa-demo.staging.corp.mongodb.com/) | [sa-blueprint-rule-configurator](https://github.com/mongodb-sc/sa-blueprint-rule-configurator) |  |
| [https://sa-blueprint-rule-configurator.sa-demo.staging.corp.mongodb.com/api/](https://sa-blueprint-rule-configurator.sa-demo.staging.corp.mongodb.com/api/) | [sa-blueprint-rule-configurator](https://github.com/mongodb-sc/sa-blueprint-rule-configurator) |  |
| [https://sharedmind.sa-demo.prod.corp.mongodb.com/](https://sharedmind.sa-demo.prod.corp.mongodb.com/) | [sharedmind-bot](https://github.com/mongodb-sc/sharedmind-bot) | A place to work on, communicate, and plan for the customer journey, from meetings, to champions, to services |
| [https://sharedmind.sa-demo.staging.corp.mongodb.com/](https://sharedmind.sa-demo.staging.corp.mongodb.com/) | [sharedmind-bot](https://github.com/mongodb-sc/sharedmind-bot) | A place to work on, communicate, and plan for the customer journey, from meetings, to champions, to services |
| [https://solutionstudio.sa.staging.corp.mongodb.com/](https://solutionstudio.sa.staging.corp.mongodb.com/) | [solutionstudio](https://github.com/mongodb-sc/solutionstudio) | Repo for the 2026 Hackathon |
| [https://video-search-demo.sa.staging.corp.mongodb.com/](https://video-search-demo.sa.staging.corp.mongodb.com/) | [voyage-video-search](https://github.com/mongodb-sc/voyage-video-search) |  |
| [https://yafc.sa-demo.prod.corp.mongodb.com/](https://yafc.sa-demo.prod.corp.mongodb.com/) | [yafc](https://github.com/mongodb-sc/yafc) | Yet Another Forecast Calculator |
| [https://yafc.sa-demo.staging.corp.mongodb.com/](https://yafc.sa-demo.staging.corp.mongodb.com/) | [yafc](https://github.com/mongodb-sc/yafc) | Yet Another Forecast Calculator |

Active Drone repos whose latest successful deploy has no public URL: [sa-blueprint-mcp](https://github.com/mongodb-sc/sa-blueprint-mcp).

## Repositories

| Repository | Visibility | Language | Description |
| --- | --- | --- | --- |
| [.github](https://github.com/mongodb-sc/.github) | Private |  | Special repository to allow for creation of the public facing README |
| [.github-private](https://github.com/mongodb-sc/.github-private) | Private |  | Org level README repo |
| [aegon-v](https://github.com/mongodb-sc/aegon-v) | Internal | HTML | Automatic discovery assistant tool |
| [agent-engine-demo](https://github.com/mongodb-sc/agent-engine-demo) | Private | Python | Atlas Agent Engine demo: home-search agents with context layers, guardrails, and token visibility |
| [agent-skills-okf](https://github.com/mongodb-sc/agent-skills-okf) | Internal | TypeScript | Enable OpenCode with skills and extensions to manage data in Google Open Knowledge Format. |
| [agent-test](https://github.com/mongodb-sc/agent-test) | Private |  | testing an AI agent |
| [agenticmemories](https://github.com/mongodb-sc/agenticmemories) | Internal | Python |  |
| [AlexSTest](https://github.com/mongodb-sc/AlexSTest) | Private |  | Test Repo |
| [alpha](https://github.com/mongodb-sc/alpha) | Private archive |  | This is a test repo to confirm permissions |
| [atlas-search-guide](https://github.com/mongodb-sc/atlas-search-guide) | Public archive | Jupyter Notebook | Reference of foundations and common patterns in Atlas Search. |
| [AtlasDemoWL](https://github.com/mongodb-sc/AtlasDemoWL) | Internal | Python |  |
| [autodesk-FusionBOM](https://github.com/mongodb-sc/autodesk-FusionBOM) | Internal | Python | MongoDB Atlas Technical Framework Workshop for Autodesk Fusion BoM caching solution |
| [bn-agentic-memory-demo](https://github.com/mongodb-sc/bn-agentic-memory-demo) | Private | Python | A LangGraph agent demonstration showcasing MongoDB Vector Search with persistent AI memory, document processing, and intelligent reasoning. |
| [books-vue-flask-pymongo](https://github.com/mongodb-sc/books-vue-flask-pymongo) | Public archive | Vue | An example full stack Vue.js/Webpack/Nginx/REST/Gunicorn/Flask/MongoDB application, showing how a developer can focus on programming in Python |
| [bulk-lofter](https://github.com/mongodb-sc/bulk-lofter) | Internal | TypeScript |  |
| [calendar-hygiene-agent](https://github.com/mongodb-sc/calendar-hygiene-agent) | Private |  | calendar hygiene |
| [can-demo-template](https://github.com/mongodb-sc/can-demo-template) | Internal | TypeScript | A Framework with batteries included to help SAs build out vibe coded demos. |
| [catalyst](https://github.com/mongodb-sc/catalyst) | Internal | TypeScript | From discovery context to a ready-to-present MongoDB proof — then close the gap with live evidence. MongoDB SAs: discovery context in, a guided live proof out, feasibility gap closed. |
| [cerebro-chrome-extension](https://github.com/mongodb-sc/cerebro-chrome-extension) | Internal | JavaScript | Cerebro is a productivity-focused Chrome Extension built for MongoDB internal use. It serves as a bridge between internal administrative dashboards (Customer Hub and Merlin) and AI-assisted workflows (Glean) for automating account plan creation. |
| [champion-tracker-v2](https://github.com/mongodb-sc/champion-tracker-v2) | Internal | JavaScript | Multi-tenant champion tracking app. Each team gets their own isolated data in MongoDB Atlas, secured with Clerk authentication. |
| [champion-tracker-v3](https://github.com/mongodb-sc/champion-tracker-v3) | Internal | JavaScript | Multi-tenant champion tracking app. Each team gets their own isolated data in MongoDB Atlas, secured with Clerk authentication. |
| [cmvr_ais_search](https://github.com/mongodb-sc/cmvr_ais_search) | Public | Jupyter Notebook | Get the context rich and evidence backed regulatory search |
| [cosmosdb-nosql-kafka-migrator](https://github.com/mongodb-sc/cosmosdb-nosql-kafka-migrator) | Internal | Python | Kafka Connect + Ansible toolkit for zero-downtime, one-way migration from Azure Cosmos DB to MongoDB, preserving deletes via a two-phase change-feed strategy. |
| [demo-platform](https://github.com/mongodb-sc/demo-platform) | Private | Python | A baseline demo repo for multiple demos that have been presented and shared with my clients that you all can clone/PR and enhance. |
| [demolist](https://github.com/mongodb-sc/demolist) | Public |  | This repo is to host a list of endpoints of demos |
| [devops-samples](https://github.com/mongodb-sc/devops-samples) | Private | Python | Sample scripts for devops actions |
| [discobuddy](https://github.com/mongodb-sc/discobuddy) | Internal | JavaScript | A local discovery co-pilot for Solutions Architects: live call transcription and context-aware next-question suggestions powered by Gemini. |
| [e2e-game-offers](https://github.com/mongodb-sc/e2e-game-offers) | Public archive | JavaScript |  |
| [easy-cloud-k8s-cluster](https://github.com/mongodb-sc/easy-cloud-k8s-cluster) | Private | HCL | Provision a Kubernetes cluster on AWS or GCP using Terraform for infrastructure and Ansible + kubeadm for cluster bootstrap |
| [fhir-webservice](https://github.com/mongodb-sc/fhir-webservice) | Public archive | Java | End-to-end demonstration of a FHIR Server utilizing MongoDB and Confluent for Kafka |
| [hackathon-cluster-copilot](https://github.com/mongodb-sc/hackathon-cluster-copilot) | Private | Python | An AI-driven MongoDB Atlas cluster metrics exploratory and analytical tool built for the Sales team. |
| [henry-test-auto-approve](https://github.com/mongodb-sc/henry-test-auto-approve) | Private archive |  | testing auto approval of creations for this org |
| [honeybadgers-sa-hackathon](https://github.com/mongodb-sc/honeybadgers-sa-hackathon) | Private | TypeScript | Global AI Hackathon 2026 - Team Honeybadgers (Nordics+Benelux) |
| [industry-explorer](https://github.com/mongodb-sc/industry-explorer) | Internal | JavaScript |  |
| [intelligence-layer-en](https://github.com/mongodb-sc/intelligence-layer-en) | Internal | Python |  |
| [JG-demo](https://github.com/mongodb-sc/JG-demo) | Internal | TypeScript |  |
| [leafy-farm](https://github.com/mongodb-sc/leafy-farm) | Private | Python | Demo of IOT data and Atlas Stream processing using a simulated farm activity |
| [legacy-bank-modern-csharp](https://github.com/mongodb-sc/legacy-bank-modern-csharp) | Private | ASP.NET | AMP chained-workflow engagement: legacy-bank csharp → .NET + MongoDB |
| [legacy-bank-mods](https://github.com/mongodb-sc/legacy-bank-mods) | Internal |  | For various experiments of converting legacy-bank-app |
| [legacy-bank-speckit](https://github.com/mongodb-sc/legacy-bank-speckit) | Internal | Shell | Modernized version of Legacy Bank using GH Speckit for spec-driven dev |
| [local-mdb-cm-backup](https://github.com/mongodb-sc/local-mdb-cm-backup) | Internal | Shell | Default local MDB sandbox |
| [magenta-examples](https://github.com/mongodb-sc/magenta-examples) | Internal | Python | standalone example applications built on top of magenta-client-libraries |
| [magenta-learning](https://github.com/mongodb-sc/magenta-learning) | Internal |  |  |
| [mck-om-dedicated-search-modes](https://github.com/mongodb-sc/mck-om-dedicated-search-modes) | Public | Shell | Deploy OpsManager and MongoDB locally with Kubernetes. Configure dedicated search nodes k8n |
| [mdb-ai-agent-memory](https://github.com/mongodb-sc/mdb-ai-agent-memory) | Internal | Python | MongoDB Memory for AI applications Lab |
| [mdb-modernization-single-view-demo](https://github.com/mongodb-sc/mdb-modernization-single-view-demo) | Public archive | JavaScript | MongoDB Demo for Legacy Modernization, Mainframe Offloading and Single View |
| [mDuel](https://github.com/mongodb-sc/mDuel) | Private | Shell | mLens is a side-by-side comparison tool designed to showcase the strengths of the MongoDB Atlas Developer Data Platform against other database technologies like PostgreSQL (RDS), DynamoDB, and Couchbase (Capella). |
| [mongo-bank](https://github.com/mongodb-sc/mongo-bank) | Internal | Java | Example banking app with MongoDB |
| [mongodb-ai-arena](https://github.com/mongodb-sc/mongodb-ai-arena) | Public | JavaScript | MongoDB AI Arena |
| [mongodb-atlas-fts](https://github.com/mongodb-sc/mongodb-atlas-fts) | Public archive | HTML | Atlas Full-Text Search Demo |
| [mongodb-atlas-fts-latency-test](https://github.com/mongodb-sc/mongodb-atlas-fts-latency-test) | Public archive | JavaScript | MongoDB Atlas - Lucene Index Update Latency Test |
| [mongodb-atlas-vector-search-fashion-products](https://github.com/mongodb-sc/mongodb-atlas-vector-search-fashion-products) | Public archive | HTML | MongoDB Atlas Vector Search (Images) on Fashion Products |
| [mongodb-currency-analysis](https://github.com/mongodb-sc/mongodb-currency-analysis) | Public archive | JavaScript | MongoDB 5.0 Time Series - Crypto Currency Analysis |
| [mongodb-design-review](https://github.com/mongodb-sc/mongodb-design-review) | Internal |  | Use MongoDB Agent-Skills to assist in MongoDB Design Reviews |
| [mongodb-explainer-deck](https://github.com/mongodb-sc/mongodb-explainer-deck) | Internal | HTML | Single-file interactive explainer deck for MongoDB, for live customer meetings. |
| [mongodb-full-text-search-app](https://github.com/mongodb-sc/mongodb-full-text-search-app) | Public archive | HTML | Demonstration of MongoDB's Full Text Search capability within a Flask web application |
| [mongodb-gameday](https://github.com/mongodb-sc/mongodb-gameday) | Internal | TypeScript | purpose-built platform that turns traditional training and enablement sessions into an engaging, gamified environment. |
| [mongodb-vector-search-candlestick-pattern-analysis](https://github.com/mongodb-sc/mongodb-vector-search-candlestick-pattern-analysis) | Public archive | Jupyter Notebook | Candlestick Pattern Analysis with MongoDB Vector Search |
| [mongodb-vector-search-chat-with-pdfs](https://github.com/mongodb-sc/mongodb-vector-search-chat-with-pdfs) | Public archive | HTML | Chatting with your PDFs via MongoDB Vector Search |
| [mongodb-vector-search-human-face-similarity](https://github.com/mongodb-sc/mongodb-vector-search-human-face-similarity) | Public archive | HTML | A MongoDB Vector Search App to find similar faces from the repository by given face photo |
| [monica-graph-poc](https://github.com/mongodb-sc/monica-graph-poc) | Private | JavaScript |  |
| [morgana-ae-agent](https://github.com/mongodb-sc/morgana-ae-agent) | Internal | Python | Morgana Atlas Agent Engine for the Morgana extension. Build for SA hackaton by Uroboros team |
| [morgana-api](https://github.com/mongodb-sc/morgana-api) | Internal | Python | API to receive payloads from the morgana-extension. Built for SA Hackaton by Uroboros team |
| [morgana-extension](https://github.com/mongodb-sc/morgana-extension) | Internal | JavaScript | Google Chrome Extension to scrape content out of Merlin. Built for SA-Hackaton by Uroboros team |
| [morgana-worker](https://github.com/mongodb-sc/morgana-worker) | Internal | Python | Morgana worker lambda function. Created for SA hackaton by uroboros team |
| [movie-search-agent](https://github.com/mongodb-sc/movie-search-agent) | Public | Python | Movie agent search |
| [movie_recommendations](https://github.com/mongodb-sc/movie_recommendations) | Public archive | Python | A simple vector search client for the MongoDB Atlas movies sample data. |
| [odl-agentic-ai](https://github.com/mongodb-sc/odl-agentic-ai) | Public | Python |  |
| [pattern-rules](https://github.com/mongodb-sc/pattern-rules) | Private |  | Create a referenceable pattern for business rules and configurations that can be materialized via ASP. |
| [pensive](https://github.com/mongodb-sc/pensive) | Internal | Python | Demonstration of Agentic Memory leveraging LangChain/LangGraph and MongoDB Vector Search. |
| [pilot-tr-roch](https://github.com/mongodb-sc/pilot-tr-roch) | Private | Java | A place to share code with Thomson Reuters |
| [post-trade-demo](https://github.com/mongodb-sc/post-trade-demo) | Private | Python | Demo of post-trade analysis agent |
| [proof-of-vibe](https://github.com/mongodb-sc/proof-of-vibe) | Private | TypeScript | This interactive web application is a multi-use-case workshop framework for self-paced and instructor-led MongoDB learning. |
| [qe-perf-benchmark](https://github.com/mongodb-sc/qe-perf-benchmark) | Private | Python | Code to create a perf benchmark of the QE product |
| [rag-error-assistant](https://github.com/mongodb-sc/rag-error-assistant) | Internal | Python | RAG Error Assistant — end-to-end hybrid RAG reference library on MongoDB Atlas. $rankFusion, Voyage auto-embedding, cross-encoder reranking, Atlas Stream Processing. |
| [RAGsToRiches](https://github.com/mongodb-sc/RAGsToRiches) | Public | Python | This site is a MongoDB Atlas interactive demo showcasing AI architecture for a retail bank. It demonstrates Atlas Vector Search, RAG with citations, LangGraph agent memory, $graphLookup knowledge graphs, and role-based governance with PII redaction and audit tracking. |
| [rdbms-comparator](https://github.com/mongodb-sc/rdbms-comparator) | Public | Java | Demo tool highlighting benefits of MongoDB over Postgres |
| [retail-inventory-stream-processing](https://github.com/mongodb-sc/retail-inventory-stream-processing) | Private | JavaScript | Demo of using stream processing to summarize inventory updates for retail orgs. |
| [rocket-analytics](https://github.com/mongodb-sc/rocket-analytics) | Public archive | JavaScript | Learn how the various components of MongoDB's Developer Data Platform (DDP) can support app-driven and traditional analytics in real-time without duplicating data to other data stores. This demo was created for AWS re:Invent 2022 and presented at the MongoDB booth area at the Venetian expo hall. |
| [sa-ai-foundry](https://github.com/mongodb-sc/sa-ai-foundry) | Internal | Python | The SA AI Foundry is an internal learning program that enables the Solution Architect team on all things AI and agents. The end goal is to make every SA fluent enough in the finer details of agent development that they can credibly help customers build agents on MongoDB, spot architectural problems early, and speak from hands-on experience |
| [sa-blueprint-client-intent](https://github.com/mongodb-sc/sa-blueprint-client-intent) | Internal | Python |  |
| [sa-blueprint-configurable-workstation](https://github.com/mongodb-sc/sa-blueprint-configurable-workstation) | Internal archive |  |  |
| [sa-blueprint-continuous-authorization](https://github.com/mongodb-sc/sa-blueprint-continuous-authorization) | Internal | Python |  |
| [sa-blueprint-marketing-personalization](https://github.com/mongodb-sc/sa-blueprint-marketing-personalization) | Internal | TypeScript | Marketing Personalization |
| [sa-blueprint-mcp](https://github.com/mongodb-sc/sa-blueprint-mcp) | Internal | Python | SA Blueprint MCP |
| [sa-blueprint-mdm](https://github.com/mongodb-sc/sa-blueprint-mdm) | Internal | TypeScript | MDM Demo |
| [sa-blueprint-notification-service](https://github.com/mongodb-sc/sa-blueprint-notification-service) | Internal | Python |  |
| [sa-blueprint-rule-configurator](https://github.com/mongodb-sc/sa-blueprint-rule-configurator) | Internal | Python |  |
| [sa-blueprint-skills](https://github.com/mongodb-sc/sa-blueprint-skills) | Internal | Go Template | SA Blueprint Skills |
| [sa-hackathon-sourcessey](https://github.com/mongodb-sc/sa-hackathon-sourcessey) | Private | Python |  |
| [sa-harness-baseline](https://github.com/mongodb-sc/sa-harness-baseline) | Private | Python |  |
| [sa-transcript-library](https://github.com/mongodb-sc/sa-transcript-library) | Internal | TypeScript | Searchable knowledge library for Solutions Architects, washed from call transcripts into MongoDB Atlas. Verbatim atoms + derived rollups, hybrid $rankFusion search, and the extraction logic as a portable Claude skill. Code only — no corpus. |
| [sample-data](https://github.com/mongodb-sc/sample-data) | Private |  | Collection of scripts to generate sample data for various purposes |
| [se-pov-proofs](https://github.com/mongodb-sc/se-pov-proofs) | Internal | TypeScript | A guided, presenter-friendly front end for MongoDB’s proven PoV proof exercises. |
| [search-proofs](https://github.com/mongodb-sc/search-proofs) | Private archive | Jupyter Notebook | Atlas Search PoV Proofs of RCs and Design Patterns |
| [seismic-semi-search](https://github.com/mongodb-sc/seismic-semi-search) | Private | HTML |  |
| [sharedmind-bot](https://github.com/mongodb-sc/sharedmind-bot) | Internal | Python | A place to work on, communicate, and plan for the customer journey, from meetings, to champions, to services |
| [solutionstudio](https://github.com/mongodb-sc/solutionstudio) | Internal | Python | Repo for the 2026 Hackathon |
| [sourcessey-v2](https://github.com/mongodb-sc/sourcessey-v2) | Internal | Python |  |
| [structured-vector-examples](https://github.com/mongodb-sc/structured-vector-examples) | Private | Python | Example using the sample-mflix data of how to conduct similarity searches against structured data, including feedback loop functionality |
| [thd-cpp-poc](https://github.com/mongodb-sc/thd-cpp-poc) | Internal | JavaScript | Customer Purchase Platform POC |
| [timeseries-benchmark](https://github.com/mongodb-sc/timeseries-benchmark) | Public | TypeScript |  |
| [timeseriesDemo](https://github.com/mongodb-sc/timeseriesDemo) | Internal | TypeScript | Solutions Architect demo for MongoDB Atlas Time Series: live data generation, real-time charts, advanced time-series aggregations, cluster load testing, and an Atlas Vector Search RAG chatbot. |
| [underwriting-agent-demo](https://github.com/mongodb-sc/underwriting-agent-demo) | Internal | Python | Demo app of using an agentic approach to credit underwriting |
| [video-searcher](https://github.com/mongodb-sc/video-searcher) | Public archive | JavaScript | Tool that demonstrates the capabilities of MongoDB by making the contents of uploaded videos searchable |
| [Voice-to-RAG](https://github.com/mongodb-sc/Voice-to-RAG) | Private | Python | RAG demo using voice data |
| [voyage-video-search](https://github.com/mongodb-sc/voyage-video-search) | Private | HTML |  |
| [yafc](https://github.com/mongodb-sc/yafc) | Internal | TypeScript | Yet Another Forecast Calculator |
