# mongodb-sc demos

Repositories in [mongodb-sc](https://github.com/mongodb-sc) and the HTTP endpoints their [Drone](https://drone.corp.mongodb.com/) deploys publish.

Refresh this file with `python3 refresh.py`. The GitHub CLI token has to be authorized for the mongodb-sc single sign-on organization, and `DRONE_TOKEN` comes from the [Drone account page](https://drone.corp.mongodb.com/account). `DRONE_SERVER` defaults to `https://drone.corp.mongodb.com`.

An endpoint is the application URL from the latest successful deploy step of each Drone pipeline, in the newest 25 builds. Helm notes that only print a port-forward are ignored. When a successful deploy prints no URL, hosts are read from that pipeline's values files. Drone's chart notes use `http`; the links below use `https`.

Refreshed 2026-11-13. 108 repositories, 21 published endpoints.

## Published endpoints

| Endpoint | Repository | Description |
| --- | --- | --- |
| [https://atlas-demo-wl.sa-demo.staging.corp.mongodb.com/](https://atlas-demo-wl.sa-demo.staging.corp.mongodb.com/) | [AtlasDemoWL](https://github.com/mongodb-sc/AtlasDemoWL) | Runs slow queries against Atlas sample data so Query Insights and Performance Advisor have something to show before a demo. |
| [https://catalyst.sa-demo.staging.corp.mongodb.com/](https://catalyst.sa-demo.staging.corp.mongodb.com/) | [catalyst](https://github.com/mongodb-sc/catalyst) | From discovery context to a ready-to-present MongoDB proof — then close the gap with live evidence. MongoDB SAs: discovery context in, a guided live proof out, feasibility gap closed. |
| [https://champion-builder.sa.staging.corp.mongodb.com/](https://champion-builder.sa.staging.corp.mongodb.com/) | [champion-tracker-v3](https://github.com/mongodb-sc/champion-tracker-v3) | Multi-tenant champion tracking app. Each team gets their own isolated data in MongoDB Atlas, secured with Clerk authentication. |
| [https://discobuddy.sa-demo.staging.corp.mongodb.com/](https://discobuddy.sa-demo.staging.corp.mongodb.com/) | [discobuddy](https://github.com/mongodb-sc/discobuddy) | A local discovery co-pilot for Solutions Architects: live call transcription and context-aware next-question suggestions powered by Gemini. |
| [https://rdbms-comparator.sa-demo.staging.corp.mongodb.com/](https://rdbms-comparator.sa-demo.staging.corp.mongodb.com/) | [rdbms-comparator](https://github.com/mongodb-sc/rdbms-comparator) | Demo tool highlighting benefits of MongoDB over Postgres |
| [https://sa-blueprint-client-intent.sa-demo.staging.corp.mongodb.com/](https://sa-blueprint-client-intent.sa-demo.staging.corp.mongodb.com/) | [sa-blueprint-client-intent](https://github.com/mongodb-sc/sa-blueprint-client-intent) | This demo helps an implementation manager reuse an existing pharmacy plan design for a client. |
| [https://sa-blueprint-client-intent.sa-demo.staging.corp.mongodb.com/api/](https://sa-blueprint-client-intent.sa-demo.staging.corp.mongodb.com/api/) | [sa-blueprint-client-intent](https://github.com/mongodb-sc/sa-blueprint-client-intent) | This demo helps an implementation manager reuse an existing pharmacy plan design for a client. |
| [https://sa-blueprint-continuous-authorization.sa-demo.staging.corp.mongodb.com/](https://sa-blueprint-continuous-authorization.sa-demo.staging.corp.mongodb.com/) | [sa-blueprint-continuous-authorization](https://github.com/mongodb-sc/sa-blueprint-continuous-authorization) | This MongoDB blueprint is a runnable, agentic demo of continuous prior authorization. |
| [https://sa-blueprint-continuous-authorization.sa-demo.staging.corp.mongodb.com/api/](https://sa-blueprint-continuous-authorization.sa-demo.staging.corp.mongodb.com/api/) | [sa-blueprint-continuous-authorization](https://github.com/mongodb-sc/sa-blueprint-continuous-authorization) | This MongoDB blueprint is a runnable, agentic demo of continuous prior authorization. |
| [https://sa-blueprint-marketing-personalization.sa-demo.staging.corp.mongodb.com/](https://sa-blueprint-marketing-personalization.sa-demo.staging.corp.mongodb.com/) | [sa-blueprint-marketing-personalization](https://github.com/mongodb-sc/sa-blueprint-marketing-personalization) | Marketing Personalization |
| [https://sa-blueprint-marketing-personalization.sa-demo.staging.corp.mongodb.com/api/](https://sa-blueprint-marketing-personalization.sa-demo.staging.corp.mongodb.com/api/) | [sa-blueprint-marketing-personalization](https://github.com/mongodb-sc/sa-blueprint-marketing-personalization) | Marketing Personalization |
| [https://sa-blueprint-mdm.sa-demo.staging.corp.mongodb.com/](https://sa-blueprint-mdm.sa-demo.staging.corp.mongodb.com/) | [sa-blueprint-mdm](https://github.com/mongodb-sc/sa-blueprint-mdm) | MDM Demo |
| [https://sa-blueprint-mdm.sa-demo.staging.corp.mongodb.com/api/](https://sa-blueprint-mdm.sa-demo.staging.corp.mongodb.com/api/) | [sa-blueprint-mdm](https://github.com/mongodb-sc/sa-blueprint-mdm) | MDM Demo |
| [https://sa-blueprint-rule-configurator.sa-demo.staging.corp.mongodb.com/](https://sa-blueprint-rule-configurator.sa-demo.staging.corp.mongodb.com/) | [sa-blueprint-rule-configurator](https://github.com/mongodb-sc/sa-blueprint-rule-configurator) | The Configurable Rules Workstation shows how a health plan or PBM clinical team can build, govern, and measure outreach rules on MongoDB Atlas. |
| [https://sa-blueprint-rule-configurator.sa-demo.staging.corp.mongodb.com/api/](https://sa-blueprint-rule-configurator.sa-demo.staging.corp.mongodb.com/api/) | [sa-blueprint-rule-configurator](https://github.com/mongodb-sc/sa-blueprint-rule-configurator) | The Configurable Rules Workstation shows how a health plan or PBM clinical team can build, govern, and measure outreach rules on MongoDB Atlas. |
| [https://sharedmind.sa-demo.prod.corp.mongodb.com/](https://sharedmind.sa-demo.prod.corp.mongodb.com/) | [sharedmind-bot](https://github.com/mongodb-sc/sharedmind-bot) | A place to work on, communicate, and plan for the customer journey, from meetings, to champions, to services |
| [https://sharedmind.sa-demo.staging.corp.mongodb.com/](https://sharedmind.sa-demo.staging.corp.mongodb.com/) | [sharedmind-bot](https://github.com/mongodb-sc/sharedmind-bot) | A place to work on, communicate, and plan for the customer journey, from meetings, to champions, to services |
| [https://solutionstudio.sa.staging.corp.mongodb.com/](https://solutionstudio.sa.staging.corp.mongodb.com/) | [solutionstudio](https://github.com/mongodb-sc/solutionstudio) | Repo for the 2026 Hackathon |
| [https://video-search-demo.sa.staging.corp.mongodb.com/](https://video-search-demo.sa.staging.corp.mongodb.com/) | [voyage-video-search](https://github.com/mongodb-sc/voyage-video-search) | Web page titled Video Search Demo, with a Python vsearch package and kanopy deploy files. |
| [https://yafc.sa-demo.prod.corp.mongodb.com/](https://yafc.sa-demo.prod.corp.mongodb.com/) | [yafc](https://github.com/mongodb-sc/yafc) | Yet Another Forecast Calculator |
| [https://yafc.sa-demo.staging.corp.mongodb.com/](https://yafc.sa-demo.staging.corp.mongodb.com/) | [yafc](https://github.com/mongodb-sc/yafc) | Yet Another Forecast Calculator |

Active Drone repos whose latest successful deploy has no public URL: [sa-blueprint-mcp](https://github.com/mongodb-sc/sa-blueprint-mcp).

## SA Demo Toolkits

Hand-maintained from the [SA Demo Toolkits wiki](https://wiki.corp.mongodb.com/spaces/10GEN/pages/96680506/SA+Demo+Toolkits).

| Demo | Description |
| --- | --- |
| [mSIDE demo app](https://mside-rqcve.mongodbstitch.com/), [Github repo](https://github.com/10gen/presales-mside), [tutorial video](https://drive.google.com/file/d/1Ni3qN-n0-uXpV-iKipl49dHWyk1zvk9F/view) | The mSIDE demo app + Github repo + example tutorial video (slack channel: solution-consulting-mside). |
| The Standard Remote Demos [Guide](https://docs.google.com/document/d/1wi5X1lSvt8ILXzIPac5FE68TZ0BEyOXs3Ug16J1n6J0/) + [Folder](https://drive.google.com/drive/u/1/folders/1Ygyzb0Nrx8U_-S5tw_pZP5jPvyMFol7s) | The Standard Remote Demos Guide + Folder. |
| [Specialists microsite with demos, jupyter notebooks, emulators, and more](https://specialists.sa.prod.corp.mongodb.com/) | Specialists microsite with demos, jupyter notebooks, emulators, and more. |
| [PoV Proof Items GitHub](https://github.com/10gen/pov-proof-exercises/) (receive 404? see [here](https://wiki.corp.mongodb.com/spaces/10GEN/pages/91004619/Presales+GitHub+Repository+Access)) | PoV Proof Items GitHub (receive 404? see here). |
| [Google Cloud + MongoDB Atlas PoV Proof Items GitHub](https://github.com/10gen/atlas-google-pov) (receive 404? see [here](https://wiki.corp.mongodb.com/spaces/10GEN/pages/91004619/Presales+GitHub+Repository+Access)) | Google Cloud + MongoDB Atlas PoV Proof Items GitHub (receive 404? see here). |
| [Github Repository Search](http://repo-search.sa.staging.corp.mongodb.com/) | Github Repository Search. |
| [AUTO-HA Laptop Demo](https://github.com/pkdone/MongoDB-AUTO-HA) + [Video](https://drive.google.com/file/d/1qTxEb569CpIw2-6Yf61Cr66Q6dMZS-CL/) | AUTO-HA Laptop Demo + Video (Paul Done). |
| [Change Streams Stock Ticker](https://github.com/pkdone/PyMongoStockTicker) | Change Streams Stock Ticker (Paul Done). |
| [MongoDB Security Playpen](https://github.com/pkdone/MongoSecurityPlaypen) | MongoDB Security Playpen (Paul Done). |
| [Client Side Field Level Encryption](https://github.com/felixreichenbach/jupyter/tree/master/field_level_encryption) | Client Side Field Level Encryption (Felix Reichenbach). |
| [Change Streams IoT](https://github.com/snarvaez/changestreams) | Change Streams IoT (Sig Narváez). |
| [Distributed Transactions + Subset Schema Design Pattern using IMDB data set](https://github.com/snarvaez/mdb-distributedtx-subset) | Distributed Transactions + Subset Schema Design Pattern using IMDB data set (Sig Narváez). |
| [Distributed Transactions Demo Toolkit](https://docs.google.com/document/d/1LTpRFE915u671CGm5z3XSzlPQha2wQUWCys8XntfOYQ/edit) | Distributed Transactions Demo Toolkit (Fuat Sungur). |
| [Application which enforces Field / Record Level Access Control](https://github.com/mcinteerj/mdb-field-record-access-control) | Application which enforces Field / Record Level Access Control (Jake McInteer). |
| [Geofencing example using the zip codes of the state of Colorado, USA as geofences](https://github.com/snarvaez/ColoradoScooters) + [video](https://youtu.be/QzrtElHwvVs) | Geofencing example using the zip codes of the state of Colorado, USA as geofences + video (Sig Narváez). |
| [Java based Client-Side Field Level Encryption](https://github.com/blainemincey/clientfle.git) | Java based Client-Side Field Level Encryption (Blaine Mincey). |
| [MongoDB Rust Driver to create a REST API example](https://github.com/pkdone/rust-groceries-mongo-api) | MongoDB Rust Driver to create a REST API example (Paul Done). |
| [Consistency and Isolation using Transactions in Python](https://github.com/mcinteerj/pymongo-txns) | Consistency and Isolation using Transactions in Python (Jake McInteer). |
| [Proportional Reader to demo WT Cache impact](https://github.com/mcinteerj/mdb-proportional-reader) + [Slides](https://docs.google.com/presentation/d/1JE_xHJMOleofJVXvaB-37w-yHR4ZGSirn2BUnzFnQg8/edit#slide=id.g6dafc75f0b_2_314) | Proportional Reader to demo WT Cache impact + Slides (Jake McInteer). |
| [Custom Aggregation Expressions](https://wiki.corp.mongodb.com/display/ENGCOMMS/Custom+Aggregation+Expressions+-+%24function+Operator) | Custom Aggregation Expressions (Event Content team). |
| [MongoDB Data Masking Aggregation Examples](https://github.com/pkdone/mongo-data-masking) | MongoDB Data Masking Aggregation Examples (Paul Done). |
| [Currency Analysis with MongoDB Time-Series Collection](https://github.com/afsungur/mongodb-currency-analysis) \| [Live Demo](https://cryptocurrencyanalysis-mqfhc.mongodbstitch.com/currency) | Currency Analysis with MongoDB Time-Series Collection \| Live Demo (Fuat Sungur). |
| [RTO Framework](https://drive.google.com/drive/folders/1DhFUDu5Y8gtSbbGICxpsHNwp162_mvtY?usp=sharing) | RTO Framework (Eugene Bogaart). |
| [Atlas Management using API](https://github.com/mdg-2018/atlas-api-workshop) | Atlas Management using API (Matt Grogan). |
| [Slow queries script for Profiler & Performance Advisor](https://github.com/robbertkauffman/mdb-slow-running-queries) | Slow queries script for Profiler & Performance Advisor (Robbert Kauffman). |
| [VNet Peering with Azure](https://docs.google.com/document/d/1HPCfTmo3npjIj7cISPVnca4aO1sjAq5vDBvT9jjMzTk/edit?usp=sharing) | VNet Peering with Azure (Abdelkrim Lahlou). |
| [Postman Collection for Atlas APIs](https://github.com/gamepop/AtlasApiPostmanCollection) | Postman Collection for Atlas APIs (Prashant Gupta). |
| [Atlas Performance Advisor - Index Suggestions](https://wiki.corp.mongodb.com/display/ENGCOMMS/Atlas+Performance+Advisor+-+Index+suggestions?src=contextnavpagetreemode) | Atlas Performance Advisor - Index Suggestions (Event Content team). |
| [mongocli script](https://github.com/jayrunkel/deployAtlasProjects) for deploying 1 or many Atlas users, projects, and clusters | mongocli script for deploying 1 or many Atlas users, projects, and clusters (Jay Runkel). |
| [Manage Atlas Dev-clusters \[pause, resume, terminate\] by using Realm triggers](https://github.com/phil2211/ManageMongoDBAtlasDevClusters) | Manage Atlas Dev-clusters [pause, resume, terminate] by using Realm triggers (Philip Eschenbacher). |
| [Integrating Atlas with Prometheus](https://docs.google.com/document/d/1R5eq5-tx8LUsgKOmihB0r7-c4uxwhHLiw8dUKDB9nCQ/edit) | Integrating Atlas with Prometheus (Dawoud Ibrahim). |
| [X509 Authentication Example](https://docs.google.com/document/d/1nuGWYftSdzHvmom3npV9VrTZ91sYQ_iHRsaOA8ezneg/edit?usp=sharing) | X509 Authentication Example (Fuat Sungur). |
| [Google Cloud Global Shared VPC + Atlas Peering](https://drive.google.com/open?id=1A56ILhc-E4U6RtBitauYRIJvvtVHpyah) (recording) | Google Cloud Global Shared VPC + Atlas Peering (recording) (Sig Narváez). |
| [ODS+EDW - Realtime Sync between Atlas + BigQuery + Google AutoML](https://drive.google.com/file/d/1cUp77Posr7YLiNaY2lqch1H96XBmsab-/view?usp=sharing) (recording) | ODS+EDW - Realtime Sync between Atlas + BigQuery + Google AutoML (recording) (Sig Narváez). |
| [Google G4 MFOL PoC (GCP, Atlas, Informatica/DB2, Java/Spring Data, Swagger, GAE)](https://drive.google.com/file/d/1gLesLFYU7JKukBg8vk2yIiS5akFKnB6a/view) (recording) | Google G4 MFOL PoC (GCP, Atlas, Informatica/DB2, Java/Spring Data, Swagger, GAE) (recording) (Sig Narváez). |
| [To-Do list reference application in browser emulators (Specialists)](https://specialists.sa.prod.corp.mongodb.com/Mobile/Demo) | To-Do list reference application in browser emulators (Specialists). |
| [Get a cloud-based workstation for Realm development (Specialists)](https://specialists.sa.prod.corp.mongodb.com/Mobile/Workstation) | Get a cloud-based workstation for Realm development (Specialists). |
| [Introduction to Stitch - QuickStart - Developer Hands-on Lab](https://github.com/mongodb-university/customer-labs/tree/master/introduction-to-stitch) | Introduction to Stitch - QuickStart - Developer Hands-on Lab (LaRoche,Grabosky,Reichenbach, Leonard,Kalan,RVZ,Osgood,Mincey). |
| [Stitch Blog - Developer Hands-on Lab](https://drive.google.com/drive/folders/1y1ngLIzGMI_zTvCAbI8aR76pMx_XcPlo?usp=sharing) (+ [video](https://mongodb.zoom.us/recording/play/Q5HTmzYKdX2L1Q3mCAUXbJQCrFoHAmw1MM0Jq_leISifjQq0WeuXjRBqX3m3zfVT?continueMode=true)) | Stitch Blog - Developer Hands-on Lab (+ video) (Britton LaRoche). |
| [HR Application Example - Developer Hands-on Lab](https://github.com/brittonlaroche/MongoDB-Demos/blob/master/Stitch/employee/README.md) | HR Application Example - Developer Hands-on Lab (Britton LaRoche). |
| [Shipping Prototype - Developer Hands-on Lab](https://github.com/brittonlaroche/MongoDB-Demos/blob/master/Applications/Shipping/README.MD) | Shipping Prototype - Developer Hands-on Lab (Britton LaRoche). |
| [Customer MDM Single View Application - Developer Hands-on Lab](https://github.com/brittonlaroche/MongoDB-Demos/blob/master/Applications/Customer-MDM/README.md) ([SA Video](https://mongodb.zoom.us/recording/play/Bg75TbROUDyjXKrexNVjtEx01SlM0D5bguZulFFeJMMRsEoHzrzAcjGvKnorV20i?continueMode=true), [Customer Video](https://mongodb.zoom.us/recording/play/Ek9IHNSMbkuJZxvw7Y6FzN0Nf1monqg-TkY2cPcYpnsQTm2PtIze_EXp3eJqZDlK?continueMode=true), [MDB Live 2020 Video](https://www.youtube.com/watch?v=KNrt5FaYpQQ))([Overview Doc with Links](https://docs.google.com/document/d/1QRZhGOQctd5mlWNbR3z6So9DDFphzULTZa4xJ1Nhczc/edit)) | Customer MDM Single View Application - Developer Hands-on Lab (Britton LaRoche, Andre Spiegel) (SA Video, Customer Video, MDB Live 2020 Video)(Overview Doc with Links). |
| [Custom JWT Auth with Keycloak/Red Hat SSO](https://github.com/blainemincey/stitch-jwt-auth) | Custom JWT Auth with Keycloak/Red Hat SSO (Blaine Mincey). |
| [GraphQL](https://docs.google.com/document/d/1IONwn5fY9ShkYug_rblIQKsSJrw7NjdQsVDOjDJCS5I/edit?usp=sharing) | GraphQL (Brian Leonard). |
| [Realm & Atlas Inventory Demo](https://docs.google.com/document/d/1tyZGPoPT1A6UzL3GcdUgCgmLABYhSJ1VOlSo76Ixvkk/edit?usp=sharing) (+ [Ted Talk VIDEO](https://drive.google.com/file/d/1LDbKQvF3s53Euvc5IEsIYisYr1jvZ1FV/view?usp=sharing))( [+ 7 Minute PG Video](https://www.youtube.com/watch?v=S2KmEDq8-CI)) | Realm & Atlas Inventory Demo (+ Ted Talk VIDEO)( + 7 Minute PG Video) (Britton LaRoche). |
| [GraphQL Keynote demo](https://wiki.corp.mongodb.com/display/ENGCOMMS/GraphQL+Demo+2019) | GraphQL Keynote demo (Event Content team). |
| [WildAid Realm Mobile Sync MDBW 2020 Keynote](https://wiki.corp.mongodb.com/display/ENGCOMMS/Realm+Mobile+Sync) | WildAid Realm Mobile Sync MDBW 2020 Keynote (Event Content team). |
| [Running Realm on Xcode Playground](https://ankurraina.medium.com/mongodb-realm-on-xcode-playground-installation-af03df782bf6) | Running Realm on Xcode Playground (Ankur Raina). |
| [Atlas Alerts to AWS CloudWatch using Realm Webhooks](https://ankurraina.medium.com/feeding-mongodb-atlas-alerts-to-aws-cloudwatch-686470cde2e0) | Atlas Alerts to AWS CloudWatch using Realm Webhooks (Ankur Raina). |
| [Event-driven web UI with Atlas App Services and Angular](https://github.com/mjwo321/event-driven-web-ui) | Event-driven web UI with Atlas App Services and Angular (Jan-Willem Oltmann). |
| [Grid application to demo App Services combined with Search](https://github.com/phil2211/MDBMasterclassTutorialApp) | Grid application to demo App Services combined with Search (Philip Eschenbacher). |
| [Sales Analytics in Charts](https://docs.google.com/document/d/1rKpgckHFUxZkNQJ9-oJyb2GwXBuFDzQb6KE0IzxQUt0) | Sales Analytics in Charts (Guillaume Meister). |
| [Geo charts demo script and deck](https://docs.google.com/document/d/1fxKPo_7jdEyzeWba8Q4CjSKmRPFB8tv9h4g7LtEnUO0) | Geo charts demo script and deck (Guillaume Meister). |
| [Billing Dashboard blog](https://www.mongodb.com/blog/post/building-a-mongodb-billing-dashboard--part-1) | Billing Dashboard blog (Ronan Bohan). |
| Charts Embedding - [Resources](https://drive.google.com/drive/folders/1xuTZOYC2TYB-Mh4KrinTkA4FVCTq6WCE) and [Recording](https://mongodb.zoom.us/recording/play/cSsrbcdAip4pGHuUPzCE7V-Z_oyWEB8QAU5Ezqwu4X7Rvb7B0_B8kKWhLnFYK6lP?continueMode=true) | Charts Embedding - Resources and Recording (Sander De Vos). |
| [Personalized Charts MDBW 2019 Keynote](https://wiki.corp.mongodb.com/display/ENGCOMMS/Charts+Demo+2019) | Personalized Charts MDBW 2019 Keynote (Event Content team). |
| [MDBW17 GitHub repo](https://github.com/rbohan/mongodbworld2017) ([video1](https://drive.google.com/file/d/0By3g-d0d4OgebW5Nek9oUDd4SlE/view?usp=sharing&resourcekey=0-vxnF1hLbgTIA6W9aUbC73g), [video2](https://drive.google.com/file/d/0By3g-d0d4OgednlramlHN1g3Qlk/view?usp=sharing&resourcekey=0-_bjyjig5S1sT5EX5SRs-Vw), [video3](https://drive.google.com/file/d/0By3g-d0d4OgeeFcxU2RIYjd1VGs/view?usp=sharing&resourcekey=0-WnG3GafdPbbLDjvtfKVU0w)) | MDBW17 GitHub repo (video1, video2, video3) (Ronan Bohan). |
| [OM Quick Launch (Specialists)](https://specialists.sa.prod.corp.mongodb.com/Tools/DeployOM) | OM Quick Launch (Specialists). |
| [CM Quick Launch (Specialists)](https://specialists.sa.prod.corp.mongodb.com/Tools/DeployCM) | CM Quick Launch (Specialists). |
| [MongoDB Enterprise K8s Operator - end-to-end Demo](https://github.com/tluck/OpsMgr-in-Kubernetes-and-Docker) | MongoDB Enterprise K8s Operator - end-to-end Demo (by Tom Luckenbach). |
| [Ops Manager VM](https://docs.google.com/document/d/1VPdPq_jDrEaRXiUz7sp2oG46113gQQaswEHR3kKU_3s/) | Ops Manager VM (Paul Done). |
| [Ops Manager Kubernetes VMs](https://drive.google.com/open?id=1rOld6xrHLm3GxnvISYIw5Y8SGbcKYOX0w5-7yKzhk3o) | Ops Manager Kubernetes VMs (Paul Done). |
| [OpsManager and Google Kubernetes](https://docs.google.com/document/d/1Kc3NfCM_64Fu6FvB0OvQYN5WJ6LrDsvYJ2XASxhybz8/edit?usp=sharing) | OpsManager and Google Kubernetes (Marc Martin). |
| [Ops Manager in Docker](https://github.com/janosj/mongodb-opsmgr/tree/main/opsmgr-docker) - works with Apple Silicon | Ops Manager in Docker - works with Apple Silicon (Jonathan Janos). |
| [Create an Atlas Data Lake](https://docs.google.com/document/d/1dsY72Wq_AeyOiEotF0iuVlvRb9ld_3LT4LUcMOzjjSw/edit#heading=h.tlccm5s2wobn) | Create an Atlas Data Lake (Dawoud Ibrahim). |
| [S3 Datalake EMEA Demo environments Quick Reference](https://docs.google.com/document/d/1XGz_VLTIjdZcbk9-Zp2ARkZEhx7ZopHn2xKkAEno770) | S3 Datalake EMEA Demo environments Quick Reference (Guillaume Meister). |
| [Archive data from Atlas to AWS S3 for Data Lake](https://github.com/robbertkauffman/mdb-stitch-archive-atlas-to-s3) | Archive data from Atlas to AWS S3 for Data Lake (Robbert Kauffman). |
| [Atlas Data Lake MDBW 2019 Keynote](https://wiki.corp.mongodb.com/pages/viewpage.action?pageId=126650502) | Atlas Data Lake MDBW 2019 Keynote (Event Content team). |
| [Federated Queries MDBW 2020 Keynote](https://wiki.corp.mongodb.com/display/ENGCOMMS/Atlas+Data+Lake+-+Federated+Query) | Federated Queries MDBW 2020 Keynote (Event Content team). |
| [Online Archive MDBW 2020 Keynote](https://wiki.corp.mongodb.com/display/ENGCOMMS/Atlas+Data+Lake+-+Online+Archive) | Online Archive MDBW 2020 Keynote (Event Content Team). |
| [Lucene token analyzer (Specialists)](https://specialists.sa.prod.corp.mongodb.com/Search/Analyzer) | Lucene token analyzer (Specialists). |
| [Jupyter Python Notebooks (autocomplete, compound, explain, facets, MLT, multi-collection, scoring, synonyms, sorting, etc) (Specialists)](https://specialists.sa.prod.corp.mongodb.com/Search/Notebooks) | Jupyter Python Notebooks (autocomplete, compound, explain, facets, MLT, multi-collection, scoring, synonyms, sorting, etc) (Specialists). |
| [Query Tuning (writing and tuning queries and indexes) (Specialists)](https://specialists.sa.prod.corp.mongodb.com/Search/Tuning) | Query Tuning (writing and tuning queries and indexes) (Specialists). |
| [Query Inspector (see why Search isn't returning results you expect) (Specialists)](https://specialists.sa.prod.corp.mongodb.com/Search/QueryInspector) | Query Inspector (see why Search isn't returning results you expect) (Specialists). |
| [Rapid Application Development - Evolving a Search UI - .Local 2023](https://searchdemomovie.sa.prod.corp.mongodb.com/) ([video](https://www.youtube.com/watch?v=Xu_AZlBp07U)) | Rapid Application Development - Evolving a Search UI - .Local 2023 (Chris Grabosky) (video). |
| [Search Proofs](https://github.com/10gen/search-proofs) | Search Proofs (Ethan Steininger). |
| [Full-Text Search Demo MDBW 2019 Keynote](https://docs.google.com/presentation/d/14kSQnz98EOCORveEE1PYfxa5JMV32Z9LRxOSP9fFppA) | Full-Text Search Demo MDBW 2019 Keynote (Karen Huaulmé). |
| [Full-Text Search GitHub repo](https://github.com/esteininger/mongodb-full-text-search-app) demo using Python/Flask | Full-Text Search GitHub repo demo using Python/Flask (Ethan Steininger). |
| [Atlas Search Demo MDBW 2020 2020 Keynote](https://wiki.corp.mongodb.com/display/ENGCOMMS/Atlas+Search+Demo+2020) | Atlas Search Demo MDBW 2020 2020 Keynote (Event Content team). |
| [Detailed Full-Text Search Demo including Geospatial queries](https://github.com/afsungur/mongodb-atlas-fts) | Detailed Full-Text Search Demo including Geospatial queries (Fuat Sungur). |
| [Atlas Search Patterns Repository](https://github.com/esteininger/atlas-search-patterns) | Atlas Search Patterns Repository (Ethan Steininger). |
| [Atlas Search Index Update Latency Test](https://github.com/afsungur/mongodb-atlas-fts-latency-test) | Atlas Search Index Update Latency Test (Fuat Sungur). |
| [MSide Airbnb Demo](https://www.mside.tech/) | MSide Airbnb Demo. |
| [Restaurant Demo](https://www.atlassearchrestaurants.com/) | Restaurant Demo (DevRel). |
| [MongoRX Clinical Trials Demo](https://mongodb.highspot.com/items/61de564f9567a2c5656aa3a8) | MongoRX Clinical Trials Demo (Roy Kiesler). |
| Atlas Vector Search [Q&A](https://github.com/wbleonard/atlas-vector-search-qa), [PDFs](https://github.com/wbleonard/atlas-vector-search-pdf), [Videos](https://github.com/wbleonard/atlas-vector-search-video), [Movie Recommendations](https://github.com/wbleonard/movie_recommendations) | Atlas Vector Search Q&A, PDFs, Videos, Movie Recommendations (Brian Leonard). |
| [Searchable Video Contents](https://github.com/philipp-weyer/video-searcher) | Searchable Video Contents (Philipp Weyer). |
| [Leafy Hospital](https://mongodb-hospital.com/) | Leafy Hospital (Industry Solutions). |
| [Jupyter Python Notebooks (Vector Search, RAG, etc) (Specialists)](https://specialists.sa.prod.corp.mongodb.com/Search/Notebooks) | Jupyter Python Notebooks (Vector Search, RAG, etc) (Specialists). |
| [Vectorizor REST API (Specialists)](https://specialists.sa.prod.corp.mongodb.com/Vector/Vectorizor) | Vectorizor REST API (Specialists). |
| [RAGTAG (chatbot) (Specialists)](https://specialists.sa.prod.corp.mongodb.com/SpecRAG/why%20is%20atlas%20vector%20search%20better%20than%20pinecone) | RAGTAG (chatbot) (Specialists). |
| [Atlas Vector Search (Images) on Fashion Products](https://github.com/afsungur/mongodb-atlas-vector-search-fashion-products) | Atlas Vector Search (Images) on Fashion Products (Fuat Sungur). |
| [Candlestick Data Analysis with Vector Search](https://github.com/afsungur/mongodb-vector-search-candlestick-pattern-analysis) | Candlestick Data Analysis with Vector Search (Fuat Sungur). |
| [Face Image Similarity Search](https://github.com/afsungur/mongodb-vector-search-human-face-similarity) | Face Image Similarity Search (Fuat Sungur). |
| [Chat with PDFs](https://github.com/afsungur/mongodb-vector-search-chat-with-pdfs) | Chat with PDFs (Fuat Sungur). |
| [Kafka Technical Exploration](https://drive.google.com/drive/folders/1Qwn_26lVDREe0yEalYO_FhRDtjqfl_gA?usp=sharing) | Kafka Technical Exploration (Gabriel Paranthoen). |
| [Kafka Demo](https://docs.google.com/document/d/1qkZW8c_mVwikAklSg_BhztiSQFa93ffMEyuM_CZ44g8/edit?usp=sharing) | Kafka Demo (Gabriel Paranthoen). |
| [SinkConnector Customization Starter Kit](https://github.com/felixreichenbach/KafkaSinkConnectorCustomizations) | SinkConnector Customization Starter Kit (Felix Reichenbach / Marco Sabotinski). |
| [Kafka Connector Demo - Linking Oracle via Kafka to MongoDB](https://github.com/PhilippW94/Kafka_POV) | Kafka Connector Demo - Linking Oracle via Kafka to MongoDB (Michael Gerstenberg / Timo Lackmann / Philipp Waffler). |
| [Sharded Cluster with Docker & Compose on Laptop](https://github.com/pkdone/sharded-mongodb-docker) | Sharded Cluster with Docker & Compose on Laptop (Paul Done). |
| [GraphQL with Apollo Server using native MongoDB Node.js Driver](https://github.com/blainemincey/gql-mongodb) | GraphQL with Apollo Server using native MongoDB Node.js Driver (Blaine Mincey). |
| [E2E Demos Highspot Home](https://mongodb.highspot.com/items/60ef1e58f7794d23222c7814) | E2E Demos Highspot Home. |
| [Liberate Data (Relational Migrator, Schema Patterns, Search, Mobile & GraphQL)](https://github.com/mongodb-developer/liberate-data) | Liberate Data (Relational Migrator, Schema Patterns, Search, Mobile & GraphQL) (Mark Franklin, Sig Narváez). |
| [Rocket Analytics (Time Series, Data Federation, Atlas SQL & Charts)](https://github.com/mongodb-developer/rocket-analytics) | Rocket Analytics (Time Series, Data Federation, Atlas SQL & Charts) (Jay Runkel, Fabian Valle, Ralph Capasso, Sig Narváez). |
| [Real-Time Personalized Game Offers (Unity, Realm, App Services, Triggers, Google ML)](https://github.com/mongodb-developer/e2e-game-offers) | Real-Time Personalized Game Offers (Unity, Realm, App Services, Triggers, Google ML) (Nic Raboy, Roy Kiesler, Andrew Chaffin, Beau Peck, Charles Van Parys, Sig Narváez). |
| [Mainframe Offloading, Single View, Legacy Modernization for Insurance](https://github.com/ckurze/mdb-modernization-single-view-demo) [slides](https://drive.google.com/drive/u/0/folders/14wl8GJjdhcJy04o3yofh-c9pGDahkdzF), [video](https://mongodb.zoom.us/recording/play/4JYDhe_tu8Y_vOp0VGm_qRPimFYOfauGEETKl8g6KVNRwzcsmsdNiYudgMNUgEmB) | Mainframe Offloading, Single View, Legacy Modernization for Insurance (Christian Kurze, Sergi Vives, Felix Reichenbach) (slides link, video). |
| [Full stack Vue.js/Webpack/Nginx/REST/Gunicorn/Flask/Python/MongoDB application](https://github.com/pkdone/books-vue-flask-pymongo) | Full stack Vue.js/Webpack/Nginx/REST/Gunicorn/Flask/Python/MongoDB application (Paul Done). |
| [FHIR/HL7 Interoperability for Healthcare](https://github.com/blainemincey/fhir-webservice) | FHIR/HL7 Interoperability for Healthcare (Blaine Mincey). |
| [Full-Stack React.JS/Flask/Python/MongoDB Currency Analysis](https://github.com/afsungur/mongodb-currency-analysis) | Full-Stack React.JS/Flask/Python/MongoDB Currency Analysis (Fuat Sungur). |
| [IoT Use Case with MongoDB Atlas, Kinesis Data firehose, MongoDB Charts and Atlas Datalake](https://docs.google.com/document/d/1Es4AB5J2D7XQRlA4ATdgjrLrUSFr6NqduzvT882j0vU/edit#heading=h.d18qghftjv26) | IoT Use Case with MongoDB Atlas, Kinesis Data firehose, MongoDB Charts and Atlas Datalake (Paresh Saraf, Venkatesh Shanbhag). |
| [Customer 360 Single View Use Case (Pentaho/Different Sources:JSON Tweets/MySQL/Oracle)](https://docs.google.com/document/d/1rqUuByfUAUNpfOrwCWqEh_KOEcN5cECyWf8EWB3kgFc/edit?usp=sharing) | Customer 360 Single View Use Case (Pentaho/Different Sources:JSON Tweets/MySQL/Oracle) (Fuat Sungur). |
| [Backup/Restore Database or collection from Query-able continuous backup](https://docs.google.com/document/d/1iBwccTODUXwTlpxJ7IiKp2PI-DpvPynGxA1twikq_Vo/edit) | Backup/Restore Database or collection from Query-able continuous backup (Dawoud Ibrahim). |
| [Setup Demo OpsManager for PIT Restore and Queryable Backup](https://docs.google.com/document/d/1e56J7mwDwF6g1rhR0_2hOLSrtoJRFc6VYytxy8bz9Ns/edit?usp=sharing) | Setup Demo OpsManager for PIT Restore and Queryable Backup (Marc Martin). |
| 2025 - [Deploy OpsManager and MongoDB on a GKE cluster using the Enterprise K8s Operator](https://github.com/kamloiic/ent-mongodb-opertor) | 2025 - Deploy OpsManager and MongoDB on a GKE cluster using the Enterprise K8s Operator (Loic Kameni, Ramon Nascimento). |
| 2023 - [end-to-end K8s Operator Demo](https://github.com/tluck/OpsMgr-in-Kubernetes-and-Docker) | 2023 - end-to-end K8s Operator Demo (Tom Luckenbach). |
| [Demo Hands-on Lab](https://docs.google.com/document/d/14GtQff5BcN51ym7W6NDHXfaAlaHbfMAI5cPE7ysdT_I/edit?usp=sharing) + [Deck](https://docs.google.com/presentation/d/1-SeG-srqlOH1XJF3oaefUEJqwfL0-7ufl1N4RdEY8To/edit?usp=sharing) using [minishift](https://www.okd.io/minishift/) | Demo Hands-on Lab + Deck using minishift (Ronan Bohan and Matthew Aylard). |
| [Open Service Broker](https://github.com/felixreichenbach/mdbscripts/tree/master/OpenServiceBroker) | Open Service Broker (Felix Reichenbach). |
| [MongoDB K8S Operator Scripts](https://github.com/blainemincey/mongodb-k8s) | MongoDB K8S Operator Scripts (Blaine Mincey). |
| [Deploy a MongoDB cluster and Ops Manager on K8S leveraging Minikube, MongoDB Kubernetes Operator and Helm](https://github.com/Natural0rder/mongodb-k8s) | Deploy a MongoDB cluster and Ops Manager on K8S leveraging Minikube, MongoDB Kubernetes Operator and Helm (Nicolas Benhamou). |
| [String to Date Conversions](http://pauldone.blogspot.com/2020/05/aggregation-convert-nasty-date-strings.html) | String to Date Conversions (Paul Done). |
| [R - Mongolite - CRUD & Visualization in Shiny](https://github.com/JSdotPY/MongoDB_and_R-shiny-mongolite) | R - Mongolite - CRUD & Visualization in Shiny - (Julian Storz). |
| [Machine Learning with MongoDB (PyMongo) and Tensorflow (Keras)](https://github.com/JSdotPY/Machine_Learning_With_MongoDB_And_Tensorflow_Keras) | Machine Learning with MongoDB (PyMongo) and Tensorflow (Keras) - (Julian Storz). |
| [Customer Name Matching Based on Similarity Score](https://github.com/afsungur/mdm-name-matcher) | Customer Name Matching Based on Similarity Score - (Fuat Sungur). |
| [Movie Recommendation with Databricks Spark & MongoDB](https://github.com/afsungur/mongodb-spark-movie-recommendation) | Movie Recommendation with Databricks Spark & MongoDB (Fuat Sungur). |
| [Atlas Online Archive Demo Guide](https://docs.google.com/document/d/1tn2dI-_WDiqPA3cXYNXcdCBnR9LuwyC7F6GV-xM_DSw/edit?usp=sharing) | Atlas Online Archive Demo Guide. |
| [Terraform Multi Region with Private Link on Azure](https://github.com/eugenebogaart/Atlas-MultiRegion-Azure-Link) | Terraform Multi Region with Private Link on Azure (Eugene Bogaart). |
| [Terraform Private Link with Azure](https://github.com/eugenebogaart/Atlas-Azure-Link) | Terraform Private Link with Azure (Eugene Bogaart). |
| [Terraform Private Endpoint with AWS](https://github.com/eugenebogaart/Atlas-AWS-Link) | Terraform Private Endpoint with AWS (Eugene Bogaart). |
| [Terraform Multi Private Endpoints to the same Atlas Cluster](https://github.com/afsungur/mongodb-atlas-terraform-private-link-2vpcendpoints-in-2vpcs) | Terraform Multi Private Endpoints to the same Atlas Cluster (Fuat Sungur). |
| [Vault example - DB Secrets (both Self-Managed & Atlas)](https://github.com/pkdone/pymongo-vault-test) | Vault example - DB Secrets (both Self-Managed & Atlas) (Paul Done). |
| [Vault example - Atlas API Key creation](https://gist.github.com/pkdone/0c3a2181864d789138948be254644c38) | Vault example - Atlas API Key creation (Paul Done). |
| [Vault example - Encryption-at-Rest using KMIP](https://gist.github.com/pkdone/8c37c217ce67247e8a7770884231ec7c) | Vault example - Encryption-at-Rest using KMIP (Paul Done). |
| [Vault example - CSFLE using KMIP](https://gist.github.com/pkdone/084c91e0f99b46aae23919182284bfd5) | Vault example - CSFLE using KMIP (Paul Done). |
| [Dynatrace Integration Demo](https://wiki.corp.mongodb.com/spaces/10GEN/pages/189466801/Dynatrace+Integration+Demo) | Dynatrace Integration Demo. |
| [TFW Micro-Demos GitHub](https://github.com/10gen/tfw-micro-demos) (receive 404? see [here](https://wiki.corp.mongodb.com/spaces/10GEN/pages/91004619/Presales+GitHub+Repository+Access)) | TFW Micro-Demos GitHub (receive 404? see here). |
| [Full DevRel demo list](https://docs.google.com/spreadsheets/d/1_J-JQhVeJzmali95UChvYwgzAFWeilSZnkTW_ZT7t6w) | Full DevRel demo list. |
| [C# .NET Driver Demos](https://github.com/jdrumgoole/MongoDB-CSharp-Workshop) | C# .NET Driver Demos. |
| [Back to basics course (from 2018)](https://github.com/jdrumgoole/mongodb-back-to-basics-2018) | Back to basics course (from 2018). |
| [Python API for MongoDB Atlas](https://github.com/jdrumgoole/MongoDB-Atlas-API) | Python API for MongoDB Atlas. |
| [Event Sourcing Microservices with Python](https://github.com/jdrumgoole/micro-services-exemplar) | Event Sourcing Microservices with Python. |
| [Keynote demos](https://wiki.corp.mongodb.com/pages/viewpage.action?pageId=116559476) | Keynote demos. |

## Repositories

| Repository | Visibility | Language | Description |
| --- | --- | --- | --- |
| [.github](https://github.com/mongodb-sc/.github) | Private |  | Special repository to allow for creation of the public facing README |
| [.github-private](https://github.com/mongodb-sc/.github-private) | Private |  | Org level README repo |
| [aegon-v](https://github.com/mongodb-sc/aegon-v) | Internal | HTML | Automatic discovery assistant tool |
| [agent-engine-demo](https://github.com/mongodb-sc/agent-engine-demo) | Private | Python | Atlas Agent Engine demo: home-search agents with context layers, guardrails, and token visibility |
| [agent-skills-okf](https://github.com/mongodb-sc/agent-skills-okf) | Internal | TypeScript | Enable OpenCode with skills and extensions to manage data in Google Open Knowledge Format. |
| [agent-test](https://github.com/mongodb-sc/agent-test) | Private |  | testing an AI agent |
| [agenticmemories](https://github.com/mongodb-sc/agenticmemories) | Internal | Python | A FastAPI-based demo and benchmark harness that shows how layered, MongoDB-backed agent memory reduces how much traffic reaches the LLM — while keeping (or improving) answer quality. |
| [AlexSTest](https://github.com/mongodb-sc/AlexSTest) | Private |  | Test Repo |
| [alpha](https://github.com/mongodb-sc/alpha) | Private archive |  | This is a test repo to confirm permissions |
| [atlas-search-guide](https://github.com/mongodb-sc/atlas-search-guide) | Public archive | Jupyter Notebook | Reference of foundations and common patterns in Atlas Search. |
| [AtlasDemoWL](https://github.com/mongodb-sc/AtlasDemoWL) | Internal | Python | Runs slow queries against Atlas sample data so Query Insights and Performance Advisor have something to show before a demo. |
| [autodesk-FusionBOM](https://github.com/mongodb-sc/autodesk-FusionBOM) | Internal | Python | MongoDB Atlas Technical Framework Workshop for Autodesk Fusion BoM caching solution |
| [bn-agentic-memory-demo](https://github.com/mongodb-sc/bn-agentic-memory-demo) | Private | Python | A LangGraph agent demonstration showcasing MongoDB Vector Search with persistent AI memory, document processing, and intelligent reasoning. |
| [books-vue-flask-pymongo](https://github.com/mongodb-sc/books-vue-flask-pymongo) | Public archive | Vue | An example full stack Vue.js/Webpack/Nginx/REST/Gunicorn/Flask/MongoDB application, showing how a developer can focus on programming in Python |
| [bulk-lofter](https://github.com/mongodb-sc/bulk-lofter) | Internal | TypeScript | A local web app for bulk-editing Salesloft calendar meetings — meeting type and SA prep time — without opening each event one-by-one in Satellite. |
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
| [e2e-game-offers](https://github.com/mongodb-sc/e2e-game-offers) | Public archive | JavaScript | Today, gaming companies compete fiercely in red ocean spaces with free-2-play (F2P) games, where microtransactions bring revenue. |
| [easy-cloud-k8s-cluster](https://github.com/mongodb-sc/easy-cloud-k8s-cluster) | Private | HCL | Provision a Kubernetes cluster on AWS or GCP using Terraform for infrastructure and Ansible + kubeadm for cluster bootstrap |
| [fhir-webservice](https://github.com/mongodb-sc/fhir-webservice) | Public archive | Java | End-to-end demonstration of a FHIR Server utilizing MongoDB and Confluent for Kafka |
| [hackathon-cluster-copilot](https://github.com/mongodb-sc/hackathon-cluster-copilot) | Private | Python | An AI-driven MongoDB Atlas cluster metrics exploratory and analytical tool built for the Sales team. |
| [henry-test-auto-approve](https://github.com/mongodb-sc/henry-test-auto-approve) | Private archive |  | testing auto approval of creations for this org |
| [honeybadgers-sa-hackathon](https://github.com/mongodb-sc/honeybadgers-sa-hackathon) | Private | TypeScript | Global AI Hackathon 2026 - Team Honeybadgers (Nordics+Benelux) |
| [industry-explorer](https://github.com/mongodb-sc/industry-explorer) | Internal | JavaScript | A static enablement tool for MongoDB Solutions Architects to browse a deep, industry-correct taxonomy and understand business structure, typical systems, vendor-neutral database guidance, and MongoDB fit overlay. |
| [intelligence-layer-en](https://github.com/mongodb-sc/intelligence-layer-en) | Internal | Python | Teams shipping AI features usually end up with the "intelligence" of the system scattered everywhere except the database: prompts hardcoded in the app, the model name in an env var, a separate vector store for embeddings, a cache in yet another service, and agent memory nowhere at all. |
| [JG-demo](https://github.com/mongodb-sc/JG-demo) | Internal | TypeScript | A complete starter template for building MongoDB demos with Cursor or Claude. |
| [leafy-farm](https://github.com/mongodb-sc/leafy-farm) | Private | Python | Demo of IOT data and Atlas Stream processing using a simulated farm activity |
| [legacy-bank-modern-csharp](https://github.com/mongodb-sc/legacy-bank-modern-csharp) | Private | ASP.NET | AMP chained-workflow engagement: legacy-bank csharp → .NET + MongoDB |
| [legacy-bank-mods](https://github.com/mongodb-sc/legacy-bank-mods) | Internal |  | For various experiments of converting legacy-bank-app |
| [legacy-bank-speckit](https://github.com/mongodb-sc/legacy-bank-speckit) | Internal | Shell | Modernized version of Legacy Bank using GH Speckit for spec-driven dev |
| [local-mdb-cm-backup](https://github.com/mongodb-sc/local-mdb-cm-backup) | Internal | Shell | Default local MDB sandbox |
| [magenta-examples](https://github.com/mongodb-sc/magenta-examples) | Internal | Python | standalone example applications built on top of magenta-client-libraries |
| [magenta-learning](https://github.com/mongodb-sc/magenta-learning) | Internal |  | Resources for building on MongoDB's Agentic AI Platform ("Magenta"). |
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
| [monica-graph-poc](https://github.com/mongodb-sc/monica-graph-poc) | Private | JavaScript | A focused MongoDB Atlas demonstration for exploring the upstream and downstream impact of enterprise service failures. |
| [morgana-ae-agent](https://github.com/mongodb-sc/morgana-ae-agent) | Internal | Python | Morgana Atlas Agent Engine for the Morgana extension. Build for SA hackaton by Uroboros team |
| [morgana-api](https://github.com/mongodb-sc/morgana-api) | Internal | Python | API to receive payloads from the morgana-extension. Built for SA Hackaton by Uroboros team |
| [morgana-extension](https://github.com/mongodb-sc/morgana-extension) | Internal | JavaScript | Google Chrome Extension to scrape content out of Merlin. Built for SA-Hackaton by Uroboros team |
| [morgana-worker](https://github.com/mongodb-sc/morgana-worker) | Internal | Python | Morgana worker lambda function. Created for SA hackaton by uroboros team |
| [movie-search-agent](https://github.com/mongodb-sc/movie-search-agent) | Public | Python | Movie agent search |
| [movie_recommendations](https://github.com/mongodb-sc/movie_recommendations) | Public archive | Python | A simple vector search client for the MongoDB Atlas movies sample data. |
| [odl-agentic-ai](https://github.com/mongodb-sc/odl-agentic-ai) | Public | Python | A real-time AI agent built on a MongoDB Operational Data Layer (ODL) using LangGraph. |
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
| [sa-blueprint-client-intent](https://github.com/mongodb-sc/sa-blueprint-client-intent) | Internal | Python | This demo helps an implementation manager reuse an existing pharmacy plan design for a client. |
| [sa-blueprint-configurable-workstation](https://github.com/mongodb-sc/sa-blueprint-configurable-workstation) | Internal archive |  | Empty archived repository with no files, named for a configurable workstation blueprint. |
| [sa-blueprint-continuous-authorization](https://github.com/mongodb-sc/sa-blueprint-continuous-authorization) | Internal | Python | This MongoDB blueprint is a runnable, agentic demo of continuous prior authorization. |
| [sa-blueprint-marketing-personalization](https://github.com/mongodb-sc/sa-blueprint-marketing-personalization) | Internal | TypeScript | Marketing Personalization |
| [sa-blueprint-mcp](https://github.com/mongodb-sc/sa-blueprint-mcp) | Internal | Python | SA Blueprint MCP |
| [sa-blueprint-mdm](https://github.com/mongodb-sc/sa-blueprint-mdm) | Internal | TypeScript | MDM Demo |
| [sa-blueprint-notification-service](https://github.com/mongodb-sc/sa-blueprint-notification-service) | Internal | Python | Docs and a Python backend for a notification service demo on MongoDB Atlas, following the EMH design. |
| [sa-blueprint-rule-configurator](https://github.com/mongodb-sc/sa-blueprint-rule-configurator) | Internal | Python | The Configurable Rules Workstation shows how a health plan or PBM clinical team can build, govern, and measure outreach rules on MongoDB Atlas. |
| [sa-blueprint-skills](https://github.com/mongodb-sc/sa-blueprint-skills) | Internal | Go Template | SA Blueprint Skills |
| [sa-hackathon-sourcessey](https://github.com/mongodb-sc/sa-hackathon-sourcessey) | Private | Python | A governed, stateful LangGraph orchestrator for MongoDB Solution Architects. |
| [sa-harness-baseline](https://github.com/mongodb-sc/sa-harness-baseline) | Private | Python | The source of truth for how the SA department's AI harnesses are configured. |
| [sa-transcript-library](https://github.com/mongodb-sc/sa-transcript-library) | Internal | TypeScript | Searchable knowledge library for Solutions Architects, washed from call transcripts into MongoDB Atlas. Verbatim atoms + derived rollups, hybrid $rankFusion search, and the extraction logic as a portable Claude skill. Code only — no corpus. |
| [sample-data](https://github.com/mongodb-sc/sample-data) | Private |  | Collection of scripts to generate sample data for various purposes |
| [se-pov-proofs](https://github.com/mongodb-sc/se-pov-proofs) | Internal | TypeScript | A guided, presenter-friendly front end for MongoDB’s proven PoV proof exercises. |
| [search-proofs](https://github.com/mongodb-sc/search-proofs) | Private archive | Jupyter Notebook | Atlas Search PoV Proofs of RCs and Design Patterns |
| [seismic-semi-search](https://github.com/mongodb-sc/seismic-semi-search) | Private | HTML | HTML page titled Learning Search that filters content by tags. |
| [sharedmind-bot](https://github.com/mongodb-sc/sharedmind-bot) | Internal | Python | A place to work on, communicate, and plan for the customer journey, from meetings, to champions, to services |
| [solutionstudio](https://github.com/mongodb-sc/solutionstudio) | Internal | Python | Repo for the 2026 Hackathon |
| [sourcessey-v2](https://github.com/mongodb-sc/sourcessey-v2) | Internal | Python | Thin external web UI client for the Sourceyssey agent (Glean Agents / MongoDB Agentic Platform). |
| [structured-vector-examples](https://github.com/mongodb-sc/structured-vector-examples) | Private | Python | Example using the sample-mflix data of how to conduct similarity searches against structured data, including feedback loop functionality |
| [thd-cpp-poc](https://github.com/mongodb-sc/thd-cpp-poc) | Internal | JavaScript | Customer Purchase Platform POC |
| [timeseries-benchmark](https://github.com/mongodb-sc/timeseries-benchmark) | Public | TypeScript | Compare MongoDB 8.3.7 (native time-series vs custom bucketing), VictoriaMetrics, TimescaleDB, and InfluxDB 1.x using the mongodb-forks/tsbs workload generator. |
| [timeseriesDemo](https://github.com/mongodb-sc/timeseriesDemo) | Internal | TypeScript | Solutions Architect demo for MongoDB Atlas Time Series: live data generation, real-time charts, advanced time-series aggregations, cluster load testing, and an Atlas Vector Search RAG chatbot. |
| [underwriting-agent-demo](https://github.com/mongodb-sc/underwriting-agent-demo) | Internal | Python | Demo app of using an agentic approach to credit underwriting |
| [video-searcher](https://github.com/mongodb-sc/video-searcher) | Public archive | JavaScript | Tool that demonstrates the capabilities of MongoDB by making the contents of uploaded videos searchable |
| [Voice-to-RAG](https://github.com/mongodb-sc/Voice-to-RAG) | Private | Python | RAG demo using voice data |
| [voyage-video-search](https://github.com/mongodb-sc/voyage-video-search) | Private | HTML | Web page titled Video Search Demo, with a Python vsearch package and kanopy deploy files. |
| [yafc](https://github.com/mongodb-sc/yafc) | Internal | TypeScript | Yet Another Forecast Calculator |
