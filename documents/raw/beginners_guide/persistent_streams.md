 



Persistent Streams
==================

**1\. RDAF Platform's persistent streams**
------------------------------------------

RDAF supports ingesting, processing, consuming data at scale for different use cases such as AIOps, Asset Intelligence, Log Intelligence solutions. Additionally, it deliver the processed data to numerous destinations such as **Data lakes, Data Warehousing, ITSM, CMDB, Collaboration, Log management tools** and more.

It supports streaming the data such as **Metrics, Logs, Events, Traces & Asset Inventory** which is processed through RDAF's **NATs** or **Kafka** messaging service. By default, the streaming data is ingested, processed and consumed through NATs messaging service which holds the data in-memory during the transit, however, if the data need to be protected against system crashes or restarts, RDAF supports writing the streamed data to disk through persistent stream feature. If the in-transit data also need to be protected, Kafka based persistent stream can be used.

Streamed data is persisted in index store (database) which is consumed by many features or usecases. Below are some of the features or usecases (not limited to) which leverages the persistent streams.

*   Alerts / Incidents / Ticketing
*   Data Enrichment
*   Change Events from ITSM
*   Metrics, Logs, Events (Timeseries)
*   Asset Inventory and Topology
*   Regression, Anomaly Detection & Dynamic Thresholds
*   Analytics (Dashboards)
*   Others (Custom Usecases)

![Pstream_Data_Flow](https://bot-docs.cloudfabrix.io/images/persistent_streams/persistent_streams_data_flow.png)

Persistent streams can be managed through `rdac` CLI or through **RDAF UI portal**. By default, RDAF's applications such as **OIA (AIOps: Operations Intelligence and Analytics) and AIA (Asset Intelligence and Analytics)** comes with pre-created persistent streams.

Additional to system provided persistent streams, users can create new persistent streams to ingest any data for analytics or for any user's specific custom use cases.

Warning

Please do not **modify or delete** system provided persistent streams. Contact CloudFabrix technical support for any assistance (support@cloudfabrix.com) around system provided ones.

**2 Manage persistent stream**
------------------------------

Persistent streams can be managed through RDAF UI portal or using `rdac` CLI.

### **2.1 Add**

**Add persistent stream through UI**

Login into RDAF UI portal and go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Persistent Streams**

Click on **Add** button to create a new **persistent stream**

Select **Datastore** type and Enter **persistent stream** name.

Tip

When specifying a **name** for a **persistent stream**, please use alphanumeric characters. If necessary special characters such as **\-** (dash) or **\_** (underscore) can be used.

**Datastore Types:**

*   **OpenSearch:** Opensearch Index store database (support both read and write operations)
*   **SQL:** MariaDB database (support only read operations)

**Adding OpenSearch based Persistent Stream:**

![Add Pstream](https://bot-docs.cloudfabrix.io/images/persistent_streams/add_pstream1.png)

**Attributes** are settings for persistent streams (optional) and the supported format is in **JSON**

Below are supported **attributes** for **OpenSearch** based persistent streams.

| Attribute Name | Mandatory | Description |
| --- | --- | --- |
| `retention_days` | no  | Specify the data retention time in days (e.g., 7, 10, 15, etc.). When specified, data older than the specified number of days will be permanently deleted. Older data is determined by the `timestamp` field. Default `timestamp` field of a persistent stream can be overridden by mapping to another valid **timestamp** (ISO datetime format) field from the ingested data. |
| `retention_purge_extra_filter` | no  | Specify the CFXQL filter that will be applied to filter the data while deleting older data, based on the `retention_days` parameter setting. |
| `timestamp` | no  | Map a valid **timestamp** (in ISO datetime format) field (e.g., created\_time, alert\_time etc.) from the ingested data to override the default `timestamp` field. By default, every persistent stream will have a `timestamp` (in UTC) field that represents the time when the data was ingested. This setting is primarily used for **timestamp** filter when visualizing the data in Dashboards and for deleting the older data when `retention_days` is set. |
| `unique_keys` | no  | Specify array of field names (e.g., \["name", "age", "location"\] etc.) from the ingested data which will be used to identify uniqueness of each record. Use this option to configure the **persistent stream** in **update** mode. By default, **persistent stream** is configured in **append** mode. |
| `search_case_insensitive` | no  | This option is used when searching data within the persistent stream. Please specify **true** or **false**. When enabled (set to **true**), the specified text in the filter is searched without case-sensitivity. By default, it is set to `true` |
| `default_values` | no  | Specify a list of fields for which a default value (e.g., 'Not Available' or 'Not Applicable,' etc.) should be set when their value is empty for some of the records before ingesting into the persistent stream. |
| `messaging_platform_settings` | no  | This setting is only applicable, if you need to use the **Kafka** messaging service. Configure this setting to specify one or more topics (of RDA Fabric platform or from an external Kafka system) from which to read and ingest the data. By default, persistent streams use the **NATs** messaging service to read and ingest the data. (**Note:** When **external Kafka** system to be used, please configure `credential_name` parameter to specify the credential name which was created under **Configuration** --> **RDA Integrations**) |
| `auto_expand` | no  | Specify array of field names (e.g., \["names", "locations"\] etc.) from the ingested data when their value is in JSON format. Extract, flatten and add them as new fields. |
| `drop_columns` | no  | Specify array of field names (e.g., \["tags", "type"\] etc.) from the ingested data which need to be dropped before ingesting the data into a persistent stream. |
| `_settings` | no  | Specify index level settings such as `number_of_shards`, `number_of_replicas`, `refresh_interval` etc. Please note that, these settings will be applied only during persistent stream creation time. |
| `_mappings` | no  | Specify index level field mappings to define data types for each field (e.g., **double, long, boolean, text, keyword, ip, date** etc.). By default, each field's data type is automatically determined based on the data presented in the first record from the ingested data. If the field's data type is not determined, it will be treated as a Text (String). Please note that, these settings will be applied only during persistent stream creation time. |

Below is an example for persistent stream configuration settings when all of the above mentioned options are used.

Tip

Please note that all of the below listed configuration settings are **NOT** applicable for every persistent stream. Please configure only the applicable settings based on persistent stream use case requirement.

`[](#__codelineno-0-1) { [](#__codelineno-0-2)     "retention_days": 30, [](#__codelineno-0-3)     "retention_purge_extra_filter": "asset_status = 'Purge'", [](#__codelineno-0-4)     "search_case_insensitive": true, [](#__codelineno-0-5)     "timestamp": "collection_timestamp", [](#__codelineno-0-6)     "unique_keys": [ [](#__codelineno-0-7)         "a_id" [](#__codelineno-0-8)     ], [](#__codelineno-0-9)     "drop_columns": [ [](#__codelineno-0-10)         "correlationparent" [](#__codelineno-0-11)     ], [](#__codelineno-0-12)     "default_values": { [](#__codelineno-0-13)         "a_source_systemname": "Not Available", [](#__codelineno-0-14)         "a_status": "Not Available", [](#__codelineno-0-15)         "a_severity": "Not Available" [](#__codelineno-0-16)     }, [](#__codelineno-0-17)     "auto_expand": [ [](#__codelineno-0-18)         "payload" [](#__codelineno-0-19)     ], [](#__codelineno-0-20)     "messaging_platform_settings": { [](#__codelineno-0-21)         "platform": "kafka", [](#__codelineno-0-22)         "kafka-params": { [](#__codelineno-0-23)             "topics": [ [](#__codelineno-0-24)                 "ab12ern1a94mq.ingested-alerts" [](#__codelineno-0-25)             ], [](#__codelineno-0-26)             "auto.offset.reset": "latest", [](#__codelineno-0-27)             "consumer_poll_timeout": 1.0, [](#__codelineno-0-28)             "batch_max_size": 100, [](#__codelineno-0-29)             "batch_max_time_seconds": 2 [](#__codelineno-0-30)         } [](#__codelineno-0-31)     }, [](#__codelineno-0-32)     "_settings": { [](#__codelineno-0-33)         "number_of_shards": 3, [](#__codelineno-0-34)         "number_of_replicas": 1, [](#__codelineno-0-35)         "refresh_interval": "1s" [](#__codelineno-0-36)     }, [](#__codelineno-0-37)     "_mappings": { [](#__codelineno-0-38)         "properties": { [](#__codelineno-0-39)             "value": { [](#__codelineno-0-40)                 "type": "double" [](#__codelineno-0-41)             }, [](#__codelineno-0-42)             "employee_name": { [](#__codelineno-0-43)                 "type": "text", [](#__codelineno-0-44)                 "fields": { [](#__codelineno-0-45)                   "keyword": { [](#__codelineno-0-46)                     "type": "keyword" [](#__codelineno-0-47)                   } [](#__codelineno-0-48)                 } [](#__codelineno-0-49)             } [](#__codelineno-0-50)         } [](#__codelineno-0-51)     } [](#__codelineno-0-52) }`

**Adding SQL based Persistent Stream:**

Note

Currently, **SQL** based persistent streams are supported only using RDA Fabric platform's mariadb database. It supports **read-only** operations querying the data from the configured database and table. For any assistance around this feature, please contact CloudFabrix technical support (support@cloudfabrix.com)

While adding the SQL based persistent stream, please configure the below.

*   **Datastore Type:** Select **SQL**
*   **Database Name:** Enter database name from the RDAF platform's database (**Note:** Only databases that have the tenant id as pre-fix in their name are supported)
*   **Table Name:** Enter database table name or view name.

![Pstream_UI_Add](https://bot-docs.cloudfabrix.io/images/persistent_streams/pstream_ui_add_sql.png)

**Attributes** are settings for persistent streams (optional) and the supported format is in **JSON**

Below are supported **attributes** for **SQL** based persistent streams.

| Attribute Name | Mandatory | Description |
| --- | --- | --- |
| `timestamp` | no  | Map a valid **timestamp** (in ISO datetime format) field (e.g., created\_time, alert\_time etc.) from the database table. This setting is primarily used for **timestamp** filter when visualizing the data in Dashboards. |

#### **2.1.1 Append vs Update**

When a persistent stream is created with **OpenSearch** as a **Datastore Type**, it operates in either of the below two modes.

*   **Append:** Keep appending every data row as a new record (e.g., Timeseries). This is a default mode.
*   **Update:** Updates the existing data row using the list of filed(s) (as primary key(s)) configured under `unique_keys` setting.

[Example](#__tabbed_1_1)

`[](#__codelineno-1-1) { [](#__codelineno-1-2)   "retention_days": 30, [](#__codelineno-1-3)   "search_case_insensitive": true, [](#__codelineno-1-4)   "timestamp": "collection_timestamp", [](#__codelineno-1-5)   "unique_keys": [ [](#__codelineno-1-6)       "field_name_1", [](#__codelineno-1-7)       "field_name_2" [](#__codelineno-1-8)   ] [](#__codelineno-1-9) }`

#### **2.1.2 Default value for Field(s)**

If a field or fields do not exist in the ingested data record, you can add the default value for the field by configuring the `default_values` parameter.

In the example below, if the **person\_name** and **person\_age** fields do not exist in the ingested data record, default values of **Not Available** and **0** will be set for them, respectively.

[Example](#__tabbed_2_1)

`[](#__codelineno-2-1) { [](#__codelineno-2-2)   "retention_days": 30, [](#__codelineno-2-3)   "search_case_insensitive": true, [](#__codelineno-2-4)   "timestamp": "collection_timestamp", [](#__codelineno-2-5)   "default_values": { [](#__codelineno-2-6)     "person_name": "Not Available", [](#__codelineno-2-7)     "person_age": 0 [](#__codelineno-2-8)   } [](#__codelineno-2-9) }`

#### **2.1.3 Computed Field(s)**

While ingesting the data, if there's a need to create a new field based on the values of existing fields, the `ingest_pipelines` setting can be used.

In the following example, the **perc\_profit** and **profit** fields will be automatically computed and created using the values of the existing **sold\_price** and **purchase\_price** fields, and they will be added to the ingested data record.

For each field, namely **perc\_profit** and **profit**, configure the \`script\`\` configuration block with the parameters below.

*   **description:** Specify the purpose of this new field
*   **lang:** Set it as **painless**
*   **source:** Specify the computed formula used to derive the value based on the existing field's value.
*   **ignore\_failure:** Set it as **true**

[Example](#__tabbed_3_1)

`[](#__codelineno-3-1) { [](#__codelineno-3-2)   "retention_days": 30, [](#__codelineno-3-3)   "search_case_insensitive": true, [](#__codelineno-3-4)   "timestamp": "collection_timestamp", [](#__codelineno-3-5)   "ingest_pipeline": { [](#__codelineno-3-6)       "processors": [ [](#__codelineno-3-7)           { [](#__codelineno-3-8)               "script": { [](#__codelineno-3-9)                   "description": "Profit Calculator", [](#__codelineno-3-10)                   "lang": "painless", [](#__codelineno-3-11)                   "source": "ctx['perc_profit'] = (ctx['sold_price'] - ctx['purchase_price'])*100/(ctx['purchase_price'])", [](#__codelineno-3-12)                   "ignore_failure": true [](#__codelineno-3-13)               } [](#__codelineno-3-14)           }, [](#__codelineno-3-15)           { [](#__codelineno-3-16)               "script": { [](#__codelineno-3-17)                   "description": "Profit", [](#__codelineno-3-18)                   "lang": "painless", [](#__codelineno-3-19)                   "source": "ctx['profit'] = ctx['sold_price'] - ctx['purchase_price']", [](#__codelineno-3-20)                   "ignore_failure": true [](#__codelineno-3-21)               } [](#__codelineno-3-22)           } [](#__codelineno-3-23)       ] [](#__codelineno-3-24)   } [](#__codelineno-3-25) }`

Tip

The `ingest_pipelines` setting leverages the native capability of the OpenSearch service. It's important to note that, for arithmetic computations, the field's data type should be either `long` or `double`.

#### **2.1.4 Multiple Indices Rollover**

When managing time series data such as **logs or metrics**, it's not feasible to write to a single index indefinitely. To ensure good search performance and manage resource usage effectively, data need to be written to an index until it reaches a specified threshold. At that point, a new index is created, and writing continues to the new index.

The following demonstrates how to create a **persistent stream** with support for automatic rollover across multiple indices. In this example, the rollover occurs when the current write index meets one or more of the following conditions.

*   **The current write index was created 7 or more days ago**
    
*   **The current write index contains 1,000,000 or more documents**
    
*   **The current write index’s size is 100mb or larger**
    

Given the potential for many indices associated with the persistent stream, default behavior is to retrieve field mappings (metadata) from the last 10 indices. If you require information from more indices, you can provide the metadata option as demonstrated below.

`[](#__codelineno-4-1) { [](#__codelineno-4-2)   "retention_days": 30, [](#__codelineno-4-3)   "search_case_insensitive": true, [](#__codelineno-4-4)   "timestamp": "metric_timestamp", [](#__codelineno-4-5)   "multi_indices_rollover": { [](#__codelineno-4-6)     "conditions": { [](#__codelineno-4-7)       "max_age": "7d", [](#__codelineno-4-8)       "max_docs": 1000000, [](#__codelineno-4-9)       "max_size": "100mb" [](#__codelineno-4-10)     }, [](#__codelineno-4-11)     "metadata": { [](#__codelineno-4-12)       "max_indices": 100 [](#__codelineno-4-13)     } [](#__codelineno-4-14)   } [](#__codelineno-4-15) }`

#### **2.1.5 Bounded Dataset**

With this feature, the **Pstream** will be in **sync** with the selected dataset, i.e., any changes to the data in the dataset automatically get synced to the data in the Pstream. This Pstream is treated as a **read-only** stream, which means it cannot be written to in any other way.

*   Syncing the data from the dataset to the Pstream will make it easier to use for reporting and other purposes, such as when customers upload their device lists and other information as datasets.
    
*   This feature also allows multiple Pstreams to be associated with the same dataset, as each Pstream can have additional attributes such as computed columns and enriched information that could differentiate them.
    
*   If the associated dataset is deleted, the data in the Pstream is not deleted. But if the dataset with the same name is created again, it will automatically sync up with associated Pstreams.
    

Go to **Home** -> **Configuration** -> **RDA Administration** -> **Datasets** -> Copy the Dataset Name

*   Navigate to Dataset and copy the name of the dataset you wish to map to the Pstream. In this case, **customer\_summary** is used as an example.

[![Dataset Customer](https://bot-docs.cloudfabrix.io/images/ps_ui/dataset_customer.png)](/images/ps_ui/dataset_customer.png)

*   Create a new Pstream associating it to a dataset.

Go to **Home** -> **Configuration** -> **RDA Administration** -> **Persistent Streams** -> **Add**

[![Add Pstream](https://bot-docs.cloudfabrix.io/images/ps_ui/add_pstream.png)](/images/ps_ui/add_pstream.png)

*   When adding the Pstream, specify the attribute `source_dataset` as shown below.

`[](#__codelineno-5-1) { [](#__codelineno-5-2)   "source_dataset": "<give the name of the dataset>" [](#__codelineno-5-3) }`

Warning

The addition of the **source\_dataset** attribute to an already created Pstream is not supported..

Tip

By default, Pstreams are created in **append** mode unless the `unique_keys` attribute is defined, which causes the Pstream to write the data in **update** mode. In the example below, **customerName** is defined as the **unique\_key**, which uses it as a primary key to maintain a unique record for each customer.

`[](#__codelineno-6-1) { [](#__codelineno-6-2)   "unique_keys": [ [](#__codelineno-6-3)     "customerName" [](#__codelineno-6-4)   ], [](#__codelineno-6-5)   "source_dataset": "<give the name of the dataset>" [](#__codelineno-6-6) }`

[![Add Dataset](https://bot-docs.cloudfabrix.io/images/ps_ui/add_dataset.png)](/images/ps_ui/add_dataset.png)

The user can see the Added Pstream that is bound to the Dataset in the below screenshot

[![Add Dataset](https://bot-docs.cloudfabrix.io/images/ps_ui/dataone.png)](/images/ps_ui/dataone.png)

The data in the dataset is also visible in the Pstream, as shown below.

[![Output](https://bot-docs.cloudfabrix.io/images/ps_ui/output.png)](/images/ps_ui/output.png)

#### **2.1.6 Using Kafka Topics**

By default, the persistent stream uses streams created out of the NATS messaging service. The RDA Fabric platform also provides Kafka messaging service, which can be used to protect in-transit data against application service outages on the consumption end. During a brief application service outage, Kafka retains unprocessed data on disk (subject to the retention time setting). Once the application service is restored and functional again, the retained data will be processed without any data loss.

In addition to the Kafka messaging service provided by the RDA Fabric platform, external Kafka messaging service is also supported. It can be used within the persistent stream configuration.

**Using RDAF Platform's Kafka:**

RDAF Platform's Kafka is used by `@dn` bots (also known as **Data Network**) to publish and receive events within the platform. However, It can also be used to receive events from external tools.

In the example below, a persistent stream is configured to use a Kafka topic, **itsm\_snow\_incoming\_updates**, created using the `@dn:write-stream` bot.

`[](#__codelineno-7-1) { [](#__codelineno-7-2)     "retention_days": 30, [](#__codelineno-7-3)     "search_case_insensitive": true, [](#__codelineno-7-4)     "timestamp": "collection_timestamp", [](#__codelineno-7-5)     "messaging_platform_settings": { [](#__codelineno-7-6)         "platform": "kafka", [](#__codelineno-7-7)         "kafka-params": { [](#__codelineno-7-8)             "topics": [ [](#__codelineno-7-9)                 "itsm_snow_incoming_updates" [](#__codelineno-7-10)             ], [](#__codelineno-7-11)             "auto.offset.reset": "latest", [](#__codelineno-7-12)             "consumer_poll_timeout": 1.0, [](#__codelineno-7-13)             "batch_max_size": 100, [](#__codelineno-7-14)             "batch_max_time_seconds": 2 [](#__codelineno-7-15)         } [](#__codelineno-7-16)     } [](#__codelineno-7-17) }`

Tip

In the above example, **platform** parameter is set to `kafka` i.e. it uses **Data Network** feature of the platform to consume the events from the given Kafka topic. (**Note:** When using the **Data Network**, the internal naming format for Kafka topics is `tenant_id.datanetwork.topic_name` (e.g., `032a23f3e54444f4b4e3ae69e7a3f5fb.datanetwork.itsm_snow_incoming_updates`))

**Using RDAF platform's Kafka topic created for external tools:**

In the example below, a persistent stream is configured to utilize a Kafka topic named **production\_application\_events**, created by an external tool using the RDAF platform's Kafka credentials for external tools.

*   Configure the Persistent Stream with the below settings.

`[](#__codelineno-8-1) { [](#__codelineno-8-2)     "retention_days": 30, [](#__codelineno-8-3)     "search_case_insensitive": true, [](#__codelineno-8-4)     "timestamp": "collection_timestamp", [](#__codelineno-8-5)     "messaging_platform_settings": { [](#__codelineno-8-6)         "platform": "kafka-external", [](#__codelineno-8-7)         "kafka-params": { [](#__codelineno-8-8)             "topics": [ [](#__codelineno-8-9)                 "production_application_events" [](#__codelineno-8-10)             ], [](#__codelineno-8-11)             "auto.offset.reset": "latest", [](#__codelineno-8-12)             "consumer_poll_timeout": 1.0, [](#__codelineno-8-13)             "batch_max_size": 100, [](#__codelineno-8-14)             "batch_max_time_seconds": 2 [](#__codelineno-8-15)         } [](#__codelineno-8-16)     } [](#__codelineno-8-17) }`

Tip

In the above example, **platform** parameter is set to `kafka-external` and when it is set, the internal naming format for Kafka external topics is `tenant_id.external.topic_name` (e.g., `032a23f3e54444f4b4e3ae69e7a3f5fb.external.production_application_events`)

To publish the events from External tools into RDAF platform, the credentials for RDAF Platform's Kafka, can be found in the **/opt/rdaf/rdaf.cfg** configuration file. This file is located on the VM where the **RDAF deployment CLI** was executed to set up and configure the RDAF platform.

`[](#__codelineno-9-1) [kafka] [](#__codelineno-9-2) datadir = 192.168.125.45/kafka-logs [](#__codelineno-9-3) host = 192.168.125.45 [](#__codelineno-9-4) external_user = 032a23f3e54444f4b4e3ae69e7a3f5fb.external [](#__codelineno-9-5) external_password = elJRdWpLVGU2ag==`

The `externl_password` is in **base64** encoded format and it need to be decoded to see the actual password using the command `echo <external_password> | base64 -d`

The Kafka topic for external tools will be automatically created (if it doesn't exist) when the external tool starts publishing events, subject to authentication validation.

Below is the sample configuration settings for external tools to publish the events to RDAF Platform's Kafka.

*   **Bootstrap Servers:** RDAF Platform's Kafka node(s) IPs (comma separated values) with Kafka port 9093 (e.g., 192.168.10.10:9093 or 192.168.10.10:9093,192.168.10.11:9093,192.168.10.12:9093)
*   **Security Protocol:** Set the value as `SASL_SSL`
*   **SASL Mechanism:** Set the value as `SCRAM-SHA-256`
*   **SASL Username:** Enter SASL username created for external tools
*   **SASL Password:** Enter SASL password created for external tools
*   **SSL CA Certificate:** CA certificate from RDAF Platform, **ca.pem** file can be found under **/opt/rdaf/cert/ca/** directory
*   **Topic name:** Kafka topic name. The format should be `tenant_id.external.topic_name` (e.g., `032a23f3e54444f4b4e3ae69e7a3f5fb.external.production_application_events`) (**Note:** For tenant id, please go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Network** --> **For Organization: \[tenant\_id\]**)

**Using External Kafka Cluster:**

As a pre-requisite, external Kafka cluster's credentials need to be added under **Main Menu** --> **Configuration** --> **RDA Integrations** --> **Credentials** --> Click on **Add**, Select **Secret-Type** as **kafka-v2** and enter the external Kafka cluster settings.

![Pstream_UI_Kafka_External](https://bot-docs.cloudfabrix.io/images/persistent_streams/pstream_ui_kaka_external.png)

In the example below, a persistent stream is configured to use a external Kafka cluster's topic, **metrics\_data\_lake**

Tip

Configure `credential_name` setting with the **credential name** of the **external Kafka cluster** which was created as part of the above pre-requisite step.

`[](#__codelineno-10-1) { [](#__codelineno-10-2)     "retention_days": 30, [](#__codelineno-10-3)     "search_case_insensitive": true, [](#__codelineno-10-4)     "timestamp": "collection_timestamp", [](#__codelineno-10-5)     "messaging_platform_settings": { [](#__codelineno-10-6)         "platform": "kafka", [](#__codelineno-10-7)         "credential_name": "kafka-cluster-ext", [](#__codelineno-10-8)         "kafka-params": { [](#__codelineno-10-9)             "topics": [ [](#__codelineno-10-10)                 "metrics_data_lake" [](#__codelineno-10-11)             ], [](#__codelineno-10-12)             "auto.offset.reset": "latest", [](#__codelineno-10-13)             "consumer_poll_timeout": 1.0, [](#__codelineno-10-14)             "batch_max_size": 100, [](#__codelineno-10-15)             "batch_max_time_seconds": 2 [](#__codelineno-10-16)         } [](#__codelineno-10-17)     } [](#__codelineno-10-18) }`

### **2.2 Dashboard**

**View persistent stream through UI**

Login into RDAF UI portal and go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Persistent Streams** --> Click on the **Persistent Stream** Here in the below screenshot **rda\_microservice\_traces** Persistent Stream is selected to view the data.

[![Stream Details](https://bot-docs.cloudfabrix.io/images/persistent_streams/stream_details.png)](/images/persistent_streams/stream_details.png)

**Data Preview:** In this view, it presents all the ingested data into the persistent stream. It provides a filter bar along with a quick time filter highlighted in the top right side using which data can be filtered to validate the ingested data.

[![pstream ui view data preview](https://bot-docs.cloudfabrix.io/images/persistent_streams/pstream_ui_view_data_preview_new.png)](/images/persistent_streams/pstream_ui_view_data_preview_new.png)

**Stats:** It provides details about the configuration, usage, and health statistics of the persistent stream, including but not limited to the following:

*   status
*   docs\_count
*   index\_name
*   size\_in\_bytes
*   shards\_total
*   shards\_successful

![Pstream_UI_View_Stats](https://bot-docs.cloudfabrix.io/images/persistent_streams/pstream_ui_view_stats.png)

**Metadata:** It provides details about the schema of the persistent stream.

![Pstream_UI_View_Metadata](https://bot-docs.cloudfabrix.io/images/persistent_streams/pstream_ui_view_metadata.png)

### **2.3 Edit**

**Edit persistent stream through UI**

Login into RDAF UI portal and go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Persistent Streams** --> Select the **Edit** Action as shown in the screenshot below

Edit operation will allow to add / modify the settings of the persistent stream.

[![Edit Pstream](https://bot-docs.cloudfabrix.io/images/persistent_streams/edit_pstream.png)](/images/persistent_streams/edit_pstream.png)

![Pstream UI Edit](https://bot-docs.cloudfabrix.io/images/persistent_streams/pstream_ui_edit.png)

Note

Please note that, some of the settings are applied only during persistent stream creation time. Please refer **attribute settings** table for more information.

### **2.4 Delete**

**Delete persistent stream through UI**

Login into RDAF UI portal and go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Persistent Streams** --> From persistent stream menu, select **Delete** option.

When the persistent stream is deleted without selecting **Delete all the data as well** option, it will delete only the persistent stream configuration object and it will not delete the index from back-end OpenSearch.

If a new persistent stream is re-created with the same name as before, it will re-use the same index that was not deleted.

To delete the persistent stream along with it's data stored in the Opensearch index, select **Delete all the data as well** option.

![Pstream_UI_Delete](https://bot-docs.cloudfabrix.io/images/persistent_streams/pstream_ui_delete.png)

Danger

Deleting a persistent stream with **Delete all the data as well** option is a non-reversible operation as it will delete the data permanently.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!