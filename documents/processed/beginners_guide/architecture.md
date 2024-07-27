 



# RDA Fabric Architecture

Robotic Data Automation Fabric designed to manage data in a multi-cloud and multi-site environments at scale. One of the primary design principles of RDAF is to perform data operations close to data source. It provides flexibility in choosing the right data operations model based on use case.

![Architecture](https://bot-docs.cloudfabrix.io/images/guide/rda_arch_1.png)

RDAF can be started of as docker container(s) and can be scaled up to a multi-cloud or multi-site deployment.

## 1\. Deployment Models

### 1.1 Comparison of Deployment Models

| Deployment Model | [Starter](#12-deployment-model-starter) | Standard (cfxCloud) | Distributed |
| --- | --- | --- | --- |
| **Microservices** |     |     |     |
| RDA Studio | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| registry | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| worker | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| scheduler |     | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| collector |     | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| api-server |     | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| **Data Infrastructure** |     |     |     |
| NATS | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| Minio | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| MariaDB |     | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| Opensearch |     | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| **Features** |     |     |     |
| Pipeline Development | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| Pipeline Publishing | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| ML Bots | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| Streams Support | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| Persistent Streams |     | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| Event Gateway based Ingestion |     | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| Staging Area based Ingestion |     | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| Service Blueprints |     | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |
| Multi-Site Workers |     |     | ![✅](https://twemoji.maxcdn.com/v/latest/svg/2705.svg ":white_check_mark:") |

### 1.2 Deployment Model: Starter

This deployment is suitable to get started with RDA Fabric.

*   Intended for pipeline development and validation.
*   Can be deployed on laptops or desktops
*   Should not be used for production

![Architecture](https://bot-docs.cloudfabrix.io/images/guide/rda_arch_starter.png)

### 1.3 Deployment Model: Standard

This deployment is suitable for many production deployments:

*   Intended for pipeline development and validation.
*   Should be deployed on Private Cloud or Public Cloud
*   Managed Kubernetes environments are recommended but docker can also be used.
*   cfxCloud uses this model for all tenants

![Architecture](https://bot-docs.cloudfabrix.io/images/guide/rda_arch_standard.png)

### 1.4 Deployment Model: Distributed

Distributed deployment is used when data needs to be processed closer to data sources or edge locations.

![Architecture](https://bot-docs.cloudfabrix.io/images/guide/rda_arch_distributed.png)

RDA provides event gateway which can be used to [ingest](/beginners_guide/data_ingestion/)
 many types of streaming data into RDA Fabric.

![Architecture](https://bot-docs.cloudfabrix.io/images/guide/rda_arch_distributed_gw.png)

## 2\. Fabric Components

This section provides details on various RDA Fabric components.

### 2.1 RDA Studio

RDA Studio is a Jupyter notebook based environment to develop and test RDA Pipelines. Jupyter notebook can be deployed anywhere as long as it can access `NATS` and `Minio` from it's location.

RDA Studio is optional component for production environments.

### 2.2 Worker

RDA Worker is a microservice which is essential to the functioning of RDA Fabric. RDA Worker runs all pipelines (except when Pipelines are run in Studio). RDA Worker capacity is measured by number of cores available and amount of Memory (GB) available.

Any number of workers can be deployed to achieve greater scale. Each worker must specify a `site` name. Any given site may contain one or more workers in it.

### 2.3 Registry

RDA registry manages a dynamic registry of all RDA Microservices. For High Availability (HA), at least two instances of Registry should be deployed on two different nodes.

### 2.4 Scheduler

RDA Scheduler is a microservice `scheduler` that manages life cycle and state of all schedules within RDA Fabric. This service requires access to Maria DB (MySQL) to manage life cycle and state of all schedules.

Scheduler also manages Staging Area based ingestion and Service Blueprints.

For HA, at least two instances of Scheduler services should be deployed. `scheduler` microservice uses leader election protocol to select a primary instance.

### 2.5 Collector

RDA Collector manages RDA Fabric telemetry and all [Persistent Streams](/beginners_guide/data_at_rest/#6-persistent-streams)
. RDA Collector requires access to one ore more Opensearch (Elasticsearch) instances.

RDA Fabric Telemetry includes:

*   Traces for all pipelines executed by any worker at any site
*   Resource usage data for all workers
*   Ingestion data metrics for Event Gateway and Staging Area
*   Log Archiving data metrics for all workers
*   Any additional metrics and audit logs produced by various Service Blueprints

For HA, at least two instances of Collector services should be deployed. All instances of collector services will be in Active-Active mode.

### 2.6 API Server

RDA API Server acts as a gateway between User Interface and all NATS based microservices. It provides HTTPS & REST like APIs for any client that need to interact with RDA Fabric.

### 2.7 Event Gateway

RDA Event Gateway allows [ingestion of streaming data](/beginners_guide/data_ingestion/)
 from an edge or datacenter into RDA Fabric.

Event Gateway can ingest following types of events from local devices or event aggregators such as [fluentd](https://www.fluentd.org)
, [fluentbit](https://fluentbit.io/)
, [rsyslog](https://www.rsyslog.com)
 and [filebeat](https://www.elastic.co/beats/filebeat)

Some of the supported ingestion types are:

*   Syslog UDP
*   Syslog TCP (with or without SSL)
*   TCP JSON (with or without SSL)
*   HTTP(S)
*   Filebeat (supports both filebeat and winlogbeat log shipping agents)
*   SNMP Traps

Event Gateway can also be configured to directly [archive](/beginners_guide/data_at_rest/#2-log-archives)
 any ingested data into cheaper object storage such as AWS S3 or Minio or any compatible object storages.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!