 



Guide to Data Ingestion in RDA Fabric
=====================================

1\. Ingesting Data into RDAF Using Event Gateway
------------------------------------------------

[RDA Event Gateway](https://docs.cloudfabrix.io/rda/installation/event-gateway)
 is a RDA Fabric component that can be deployed in Cloud or on-premises / edge locations to ingest data from various sources.

**RDA Event Gateway supports following endpoints types:**

| Endpoint Type | Protocols | Description |
| --- | --- | --- |
| syslog\_tcp | TCP/SSL | Syslog or Syslog like event ingestion via TCP or SSL |
| syslog\_udp | UDP | Syslog or Syslog like event ingestion via UDP |
| http | HTTP/HTTPS | JSON or Plain Text formatted events via Webhook. Supports HTTP operations POST & PUT |
| tcp\_json | TCP/SSL | JSON encoded messages with one message per line |
| filebeat | HTTP/HTTPS | Elasticsearch Filebeat / Winlogbeat based ingestion of data |
| file |     | Ingestion of data from one or more file(s) or folder(s) |

RDA Event Gateway Endpoint configuration example for Webhook:

|     |     |
| --- | --- |
| [1](#__codelineno-0-1)<br> [2](#__codelineno-0-2)<br> [3](#__codelineno-0-3)<br> [4](#__codelineno-0-4)<br> [5](#__codelineno-0-5)<br> [6](#__codelineno-0-6)<br> [7](#__codelineno-0-7)<br> [8](#__codelineno-0-8)<br> [9](#__codelineno-0-9)<br>[10](#__codelineno-0-10) | `endpoints:   - name: http_events     enabled: true     type: http     secure: true     content_type: auto     port: 516     stream: my-webhook-data     attrs:         site_code: cfx_dc` |

Explanation of configuration fields:

*   `name`: Name of the endpoint. Must be unique
*   `enabled`: If set to `false`, Event Gateway will shutdown the endpoint
*   `type`: Type of Endpoint. For this example `http`
*   `secure`: If `true` runs the endpoint in HTTPS mode
*   `content_type`: Type of content to expect in incoming payload. Possible values are 'auto', 'json', 'text'. If set to auto, endpoint will detect the content using Content-Type HTTP header.
*   `port`: TCP port to listen for data
*   `stream`: Name of the RDA Stream where the data will be published for further consumption by RDA [Pipelines](#pipelines)
     or [Persistent Streams](#pstreams)
    
*   `attrs`: Optional dictionary of attributes that will be added to each message's payload. Event Gateway automatically inserts attributes:
*   Following attributes are automatically inserted into each message:
    
    > *   `rda_gw_ep_type`: Endpoint Type (in this example: 'http')
    > *   `rda_gw_ep_name`: Endpoint Name
    > *   `rda_gw_timestamp`: Ingested timestamp in ISO format
    > *   `rda_content_type`: HTTP Content-Type header value
    > *   `rda_url`: HTTP URL
    > *   `rda_path`: Path part of HTTP URL
    > *   `rda_gw_client_ip`: IP Address of the client that posted the data
    > *   `rda_user_agent`: User-Agent of the client
    > *   `rda_stream`: RDA Stream where this message is being forwarded to
    

**Automatic Archival of Data from Event Gateway:**

RDA Event Gateway can be configured to automatically archive using [RDA Log Archive](#log_archives)
 feature.

Following is an example snippet for main.yml configuration file:

|     |     |
| --- | --- |
| [1](#__codelineno-1-1)<br> [2](#__codelineno-1-2)<br> [3](#__codelineno-1-3)<br> [4](#__codelineno-1-4)<br> [5](#__codelineno-1-5)<br> [6](#__codelineno-1-6)<br> [7](#__codelineno-1-7)<br> [8](#__codelineno-1-8)<br> [9](#__codelineno-1-9)<br>[10](#__codelineno-1-10)<br>[11](#__codelineno-1-11)<br>[12](#__codelineno-1-12)<br>[13](#__codelineno-1-13)<br>[14](#__codelineno-1-14)<br>[15](#__codelineno-1-15)<br>[16](#__codelineno-1-16)<br>[17](#__codelineno-1-17)<br>[18](#__codelineno-1-18)<br>[19](#__codelineno-1-19)<br>[20](#__codelineno-1-20)<br>[21](#__codelineno-1-21)<br>[22](#__codelineno-1-22)<br>[23](#__codelineno-1-23) | `# This is the main configuration for Event Gateway. # Changes to this file only take affect after Gateway container is restarted # # Name of the site at which Event gateway is deployed # If not specified, uses ENV variable RDA_SITE_NAME. This will override  # env variable value site_name: SITE_NAME archival:     enabled: true     # local directory where log files (JSONs and then .gz files) will be saved     local_dir: /tmp/log_archive/     # Name of the archival. Must be only letters and digits and optionally _-     name: example_archive     # Local .gz files are deleted immediately after copying to destination (minio or s3)     # If not able to push to minio, how long to keep in local directory     local_retain_max_hours: 24     # Archival destination. If not specified, archival will be disabled     destination_repository: demo_logarchive` |

Note

Log Archive repository (`demo_logarchive`) must be pre-created using CLI or RDA Portal.

* * *

2\. Ingesting Data into RDAF Using Message Queues
-------------------------------------------------

RDA Pipelines can continuously ingest data from many types of message queues. Some of the most commonly used approaches are:

*   [RDA Streams Using NATS](/Bots/rn/)
    
*   [Kafka](/Bots/kafka/)
     and [RDA Streams using Kafka](/Bots/datanetwork/)
    
*   [MQTT](/Bots/mqtt/)
    
*   [AWS SQS](/Bots/aws-sqs/)
    
*   [AWS Kinesis](/Bots/aws-kinesis/)
    

See above pages for list of bots available for ingesting data from different types of queues.

3\. Ingesting Data into RDAF Using Purpose Built Bots
-----------------------------------------------------

RDA Provides extensive set of bots to retrieve data from various sources. Following are some of the integrations available:

*   **APM**
    
    *   [AppDynamics](/Bots/appdynamics/)
        
    *   [Dynatrace](/Bots/dynatrace/)
        
*   **Cloud Infrastructure**
    
    *   [AWS](/Bots/aws_v2/)
        
    *   [AWS Cloudwatch](/Bots/aws-cloudwatch/)
        
    *   [Azure](/Bots/azure/)
        
    *   [Azure Insights](/Bots/azure-insights/)
        
    *   [Google Cloud](/Bots/gcp/)
        
*   **Databases**
    
    *   [Elasticsearch / Opensearch](/Bots/elasticsearch_v2/)
        
    *   [MySQL / MariaDB](/Bots/mysql_v2)
        
    *   [SQLite](/Bots/sqlite)
        
*   **File & Object Storages**
    
    *   [Files & URLs](/Bots/file/)
        : Supports many formats like CSV, ZIP, GZIP, Parquet
    *   [Minio/ S3](/Bots/minio/)
        
*   **Generic APIs**
    
    *   [REST Client](/Bots/restclient/)
        
    *   [SSH](/Bots/ssh/)
        
*   **Container Infrastructure**
    
    *   [Istio](/Bots/istio/)
        
    *   [Kubernetes](/Bots/kubernetes-inventory/)
        
*   **ITOM & Observability**
    
    *   [Datadog](/Bots/datadog/)
        
    *   [ManageEngine OpManager](/Bots/me-opmanager/)
        
    *   [Motadata](/Bots/motadata/)
        
    *   [Nagios](/Bots/nagios/)
        
    *   [Prometheus](/Bots/prometheus/)
        
    *   [PRTG](/Bots/prtg/)
        
    *   [Splunk](/Bots/splunk_v2/)
        
    *   [VMware vROps](/Bots/vrops/)
        
    *   [Zabbix](/Bots/zabbix/)
        
*   **ITSM**
    
    *   [Service Desk Plus CMDB](/Bots/cmdbservicedeskplus/)
        
    *   [Infoblox NetMRI](/Bots/infoblox-netmri/)
        
    *   [Jira](/Bots/jira/)
        
    *   [ManageEngine AppManager](/Bots/me-appmanager/)
        
    *   [PagerDuty](/Bots/pagerduty/)
        
    *   [Service Desk Plus](/Bots/servicedeskplus/)
        
    *   [Servicenow](/Bots/servicenow_v2/)
        
*   **Infrastructure**
    
    *   [Arista Bigswitch](/Bots/arista-bigswitch/)
        
    *   [Cisco ACI](/Bots/cisco-aci-apic/)
        
    *   [Cisco Intersight](/Bots/cisco-intersight/)
        
    *   [Cisco IoS](/Bots/cisco-ios/)
        
    *   [Cisco Meraki](/Bots/cisco-meraki/)
        
    *   [Cisco NXOS](/Bots/cisco-nxos/)
        
    *   [Cisco Support](/Bots/cisco-support/)
        
    *   [Cisco UCS CIMC](/Bots/cisco-ucs-cimc/)
        
    *   [Cisco UCS Manager](/Bots/cisco-ucs-manager/)
        
    *   [Cisco Unified Call Manager](/Bots/cisco_ucm/)
        
    *   [EMC Isilon](/Bots/emc-isilon/)
        
    *   [EMC Unity](/Bots/emc-unity/)
        
    *   [EMC XtremIO](/Bots/emc-xtremio/)
        
    *   [HPE 3Par](/Bots/hpe-3par/)
        
    *   [IBM AIX](/Bots/ibm-aix/)
        
    *   [Linux & Docker](/Bots/linux-inventory/)
        
    *   [NetApp ONTAP 7-Mode](/Bots/netapp-ontap-7mode/)
        
    *   [NetApp ONTAP C-Mode](/Bots/netapp-ontap-cmode/)
        
    *   [Openstack](/Bots/openstack/)
        
    *   [Pure Storage](/Bots/purestorage/)
        
    *   [Redfish](/Bots/redfish/)
        
    *   [VMware vCenter](/Bots/vmware-vcenter/)
        
    *   [Windows](/Bots/windows-inventory/)
        

4\. Ingesting Data Using Staging Area
-------------------------------------

RDA Pipelines can continuously ingest data from staging area (for example S3 or minio). Data can be ingested directly from files in a specified bucket and a folder path (or prefix).

Staging area definition specifies where data files are stored so that the data in the files can be ingested into RDA Fabric.

**Storage Location**

*   Storage area definitions are stored in RDAF Object Storage.
*   The staging area data can be in RDAF Object Storage or any external storage (S3 or minio). For external staging area, the user needs to create [credential](#credentials)
     of type `stagingarea-ingest` for RDA platform to access the bucket.

**Related Bots**

*   [@dm:staging-read](/Bots/cfxdm/#bot-dmstaging-read)
    

**Related RDA Client CLI Commands**

    `[](#__codelineno-2-1)     staging-area-add          Add or update staging area [](#__codelineno-2-2)     staging-area-delete       Delete a staging area [](#__codelineno-2-3)     staging-area-get          Get YAML data for a staging area [](#__codelineno-2-4)     staging-area-list         List all staging areas.`

[See RDA CLI Guide for installation instructions](/beginners_guide/rdac/)

Sample YAML: For staging area in RDA platform

|     |     |
| --- | --- |
| [1](#__codelineno-3-1)<br> [2](#__codelineno-3-2)<br> [3](#__codelineno-3-3)<br> [4](#__codelineno-3-4)<br> [5](#__codelineno-3-5)<br> [6](#__codelineno-3-6)<br> [7](#__codelineno-3-7)<br> [8](#__codelineno-3-8)<br> [9](#__codelineno-3-9)<br>[10](#__codelineno-3-10)<br>[11](#__codelineno-3-11) | `name: staging-area-platform-sample description: staging area data in RDAF Object Storage # platform_config field is used when staging area is in RDAF Object Storage platform_config:  object_prefix: /data/ # file criteria in regex format  filename_pattern: .* # Optional. Delete data from staging area after ingestion (y/n). Default: n delete_after_ingestion: n # Optional. If you set the date, it will only ingest the files that are newer than provided 'ingest_after' datetime. The fields needs to be in UTC Time Zone and ISO Date Time Format. Default is null ingest_after: "2022-05-10T23:12:03.223067"` |
Sample YAML: For staging area that is external (S3 or minio)

|     |     |
| --- | --- |
| [1](#__codelineno-4-1)<br>[2](#__codelineno-4-2)<br>[3](#__codelineno-4-3)<br>[4](#__codelineno-4-4)<br>[5](#__codelineno-4-5)<br>[6](#__codelineno-4-6) | `name: staging-area-external-sample description: staging area data in external S3 or minio # Name of the predefined credential for the external S3 or minio external_storage_credential_name: "s3-sa" # file criteria in regex format  filename_pattern: sample.json` |

**Managing through RDA Portal**

*   In RDA Portal, Click on left menu **Data**
*   Click on 'View Details' next to **Data Staging Area**

**Managing through RDA Studio**

*   Studio does not have any user interface for managing the staging area.

5\. Ingesting Data once from location
-------------------------------------

RDA Pipelines can also ingest data once from a given location (S3 or minio). Data can be ingested directly from files in a specified bucket and a folder path (or prefix).

For external location, the user needs to create [credential](#credentials)
 of type `stagingarea-ingest` for RDA platform to access the bucket.

**Related Bots**

*   [@dm:ingest-from-location](/Bots/cfxdm/#bot-dmingest-from-location)
    

6\. Ingesting Data from Kafka
-----------------------------

Data can be ingested into persistent streams via Kafka.

You can provide Kafka as the messaging platform to read data from and then write to Open Search the following way when you are creating the persistent stream in the attributes section of the UI:

On the Left Side Menu Bar Click on the **Configuration** → **RDA Administration** → **Persistent Streams** → **Add** → **Attributes** (please add the below code) → **Save**

`[](#__codelineno-5-1) { [](#__codelineno-5-2)   "messaging_platform_settings": { [](#__codelineno-5-3)     "platform": "kafka", [](#__codelineno-5-4)     "credential_name": "mykafka", [](#__codelineno-5-5)     "kafka-params": { [](#__codelineno-5-6)       "topics": [ [](#__codelineno-5-7)         "kafka_topic1", [](#__codelineno-5-8)         "kafka_topic2" [](#__codelineno-5-9)       ], [](#__codelineno-5-10)       "auto.offset.reset": "latest", [](#__codelineno-5-11)       "consumer_poll_timeout": 1.0 [](#__codelineno-5-12)     } [](#__codelineno-5-13)   } [](#__codelineno-5-14) }`

To add [kafka-v2](https://bot-docs.cloudfabrix.io/Extensions/extensions_F_K/?h=kafka+v2#extension-kafka-v2 "kafka-v2")
 Credentials from the UI: Click on **Configuration** → **RDA Integrations** → **Credentials** → **Add** → **Save**

| Parameter Name | Description |
| --- | --- |
| credential\_name | Name of the credential of type kafka-v2 |
| topics | One or more kafka topics to receive data from |
| auto.offset.reset | “earliest” or “latest”, Default: “latest” |
| consumer\_poll\_timeout | Milliseconds spent waiting in the poll if data is not available in the buffer. Default is 1. |

Related RDA Client CLI Commands:

`[](#__codelineno-6-1) pstream-add             Add a new Persistent stream [](#__codelineno-6-2) Sub-option              --messaging_platform_settings [](#__codelineno-6-3)                         JSON file containing Messaging platform settings to [](#__codelineno-6-4)                         read data from (Ex KAFKA) and write to Open Search. If [](#__codelineno-6-5)                         not provided, default platform NATS is used.`

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!