 



# Data at Rest in RDA Fabric

Robotic Data Automation Fabric (RDAF) provides several types of ways to store metadata and data within the Fabric itself. In most common use cases, RDAF pulls data from various sources or ingests data via streaming and eventually sends to another destination outside the Fabric. In these scenarios, only limited data is saved in RDAF.

| Artifact Type | Description |
| --- | --- |
| [Datasets](#datasets) | Tabular data. Could be input to many pipelines or output from pipelines. |
| [Log Archives](#log_archives) | Time based storage of data in object storage optimized for long term retention and cost reduction |
| [Application Dependency Mappings](#stacks) | Application dependency mappings, typically consumed by AIOps or ITSM applications.  <br>Also known as Stacks in RDAF. |
| [RDA Objects](#rda_objects) | Any arbitrary data including binary data such as Images, Videos, Pickled Objects. |
| [Job Outputs](#job_outputs) | Output of recently executed pipelines. |
| [Persistent Streams](#pstreams) | Automated persistence for any streamed data . |

* * *

## 1\. Datasets

In RDA, the term Dataset refers to tabular data and typically stored within RDA fabric.

Supported formats for RDAF datasets are CSV and [Parquet](https://parquet.apache.org)
.

**Storage Location**

*   Both Dataset Metadata and Data are stored in RDAF Object Storage.

**Related Bots**

*   [@dm:savedlist](/Bots/cfxdm/#bot-dmsavedlist)
    
*   [@dm:save](/Bots/cfxdm/#bot-dmsave)
    
*   [@dm:recall](/Bots/cfxdm/#bot-dmrecall)
    
*   [@dm:enrich](/Bots/cfxdm/#bot-dmenrich)
    
*   [@dm:enrich-using-rule-dict](/Bots/cfxdm/#bot-dmenrich-using-rule-dict)
    

**Related RDA Client CLI Commands**
```
    dataset-add               Add a new dataset to the object store 
    dataset-delete            Delete a dataset from the object store 
    dataset-get               Download a dataset from the object store 
    dataset-list              List datasets from the object store 
    dataset-meta              Download metadata for a dataset from the object store 
    dataset-query             Query dataset from the object store
 ```

[See RDA CLI Guide for installation instructions](/beginners_guide/rdac/)

**Managing through RDA Portal**

*   Go to **Home Menu** -> Click **Configuration** -> **Rda Administration** -> **Datasets** -> Click **Datasets**

**Managing through RDA Studio**

*   Studio only supports viewing/ exploring of datasets
*   In Studio, Select Task: "Explore Datasets"

[![Studio Datasets](https://bot-docs.cloudfabrix.io/images/guide/studio_datasets.png)](/images/guide/studio_datasets.png)

*   Since Studio is a Jupyter notebook, dataset can be accessed using `get_dataset` function. List of all dataset management functions available in notebook:
    
    a. `add_dataset(data_or_file, name)`: Add a dataset using `data_or_file` with dataset name `name`
    
    b. `add_dataframe(df, name)`: Adds dataframe `df` as a dataset with name `name`
    
    c. `get_dataset(name)`: Download specified dataset and return pandas DataFrame.
    
    d. `list_datasets()`:
    

[![Studio Cell Dataset](https://bot-docs.cloudfabrix.io/images/guide/studio_cell_dataset.png)](/images/guide/studio_cell_dataset.png)

**Examples**

*   [Example Datasets](/#explore-example-datasets)
    
*   Example Dataset Metadata
    
    |     |     |
    | --- | --- |
    | 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
 | `{             "name": "my-dataset",             "format": "csv",             "mem_size_mb": 0.0,             "num_rows": 4,             "num_columns": 8,             "saved_time": "2022-02-22T10:05:28.847550",             "dtypes": {                     "sysContact": "object",                     "sysDescr": "object",                     "sysLocation": "object",                     "sysName": "object",                     "sysObjectID": "object",                     "sysServices": "int64",                     "sysUpTime": "int64",                     "target": "object"             }         }` |
    

* * *

## 2\. Bounded Datasets

Bounded Datasets are always bound to a specific data model defined using [JSON Schema](https://json-schema.org/understanding-json-schema/)
. Bounded datasets can also be edited in RDA Portal.

This is a new feature introduced in May 2022

**Example JSON Schema for Bounded Datasets**

| Example Schema.json |     |
| --- | --- |
| 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
 | `{       "title": "Example Schema",       "properties": {             "text": {                   "type": "string",                   "title": "Simple Text"             },             "enum": {                   "type": "string",                   "default": "low",                   "enum": [                         "low",                         "medium",                         "high",                         "critical",                         "emergency"                   ],                   "title": "Scalar Enum"             },             "bool": {                   "type": "boolean",                   "title": "Simple Boolean"             },             "enum_array": {                   "type": "array",                   "title": "Array Enum",                   "items": {                         "type": "string",                         "enum": [                               "enum1",                               "enum2",                               "enum3",                               "enum4"                         ]                   }             },             "int": {                   "type": "integer",                   "title": "Integer",                   "description": "Integer with < 80 and > 20",                   "exclusiveMaximum": 80,                   "exclusiveMinimum": 20             }       },       "required": [             "text",             "enum"       ],       "name": "sample" }` |

**Storage Location**

*   Both Bounded Dataset Data and Schema are stored in RDAF Object Storage.

**Managing through RDA Portal**

*   Go to **Home Menu** -> Click **Configuration** -> **Rda Administration** -> **Datasets** -> Click **Schemas**

## 3\. Log Archives

Log Archives are time based storage of data in object storage, optimized for long term retention and cost reduction. Log Archives store streaming log data in S3 like storage. Each Log Archive Repository may contain one or more named archives, each with data stored in a compressed format at minute level granularity.

Log Archives are stored in a user provided object storage in following format:
```
     Object_Prefix/ 
         ARCHIVE_NAME/ 
             YEAR (4 digits)/ 
                 MONTH (2 digits)/ 
                     DAY (2 digits)/ 
                         HOUR (2 digits, 24 hr clock)/ 
                             MINUTE (2 digits)/ 
                                 UUID.gz
 ```

Each file under the MINUTE folder is typically a UUID based name to uniquely identify the ingestor or pipeline saving the data. Contents of the file are one line per each row of data, encoded in JSON format. Files are stored in GZIP compressed format.

Example contents of the file look like this:


```
{"device":"milesxi-dr-03.acme.internal","message":"Vpxa: verbose vpxa[B203B70] [Originator@6876 sub=vpxaMoService opID=3c62fb43-d2] Adding querySpec. Had=33, has=33","rda_gw_timestamp":"2022-04-16T00:00:01.289885","timestamp":"2022-04-16T00:00:01.289885"} {"device":"milesxi-dr-05.acme.internal","message":"Rhttpproxy: verbose rhttpproxy[468CB70] [Originator@6876 sub=Proxy Req 75640] Resolved endpoint : [N7Vmacore4Http16LocalServiceSpecE:0x0420c070] _serverNamespace = \/vpxa action = Allow _port = 8089","rda_gw_timestamp":"2022-04-16T00:00:01.290207","timestamp":"2022-04-16T00:00:01.290207"} ...
```

**Storage Location**

*   Typically, Log Archives are stored in one or more S3 compatible storages like Minio, AWS S3, Google Cloud Object Storage, Azure Blob.
    
*   For demonstration and experimentation purposes, RDAF built-in object storage may also be used.
    

**Related Bots**

*   [@dm:create-logarchive-repo](/Bots/cfxdm/#bot-dmcreate-logarchive-repo)
    
*   [@dm:logarchive-replay](/Bots/cfxdm/#bot-dmlogarchive-replay)
    
*   [@dm:logarchive-save](/Bots/cfxdm/#bot-dmlogarchive-save)
    

**Related RDA Client CLI Commands**
```
     logarchive-add-platform   Add current platform Minio as logarchive repository 
     logarchive-data-read      Read the data from given archive for a specified time interval 
     logarchive-data-size      Show size of data available for given archive for a specified  
                               time interval 
     logarchive-download       Download the data from given archive for a specified time interval 
     logarchive-names          List archive names in a given repository 
     logarchive-replay         Replay the data from given archive for a specified time  
                               interval with specified label 
     logarchive-repos          List of all log archive repositories 
     merge-logarchive-files    Merge multiple locally downloaded Log Archive (.gz) files  
                               into a single CSV/Parquet file
 ```

**Managing through RDA Portal**

*   Go to **Home Menu** -> Click **Configuration** -> **Rda Integrations** -> **Log Archives**

**Managing through RDA Studio**

*   Studio does not have any user interface for managing Log Archives.

## 4\. Application Dependency Mappings (Stacks)

Application Dependency mappings are typically consumed by AIOps or ITSM applications.

Application Dependency Mappings capture relationships among various application components and infrastructure components. Dependency Mappings are produced by RDA Pipelines with data retrieved from one or more sources.

See [Application Dependency Mapping](https://bot-docs.cloudfabrix.io/beginners_guide/adm/)
 for more details on how to create Stacks using RDA Bots.

**Storage Location**

*   RDA Fabric Object Storage

**Related Bots**

*   [@dm:stack-create](/Bots/cfxdm/#bot-dmstack-create)
    
*   [@dm:stack-connected-nodes](/Bots/cfxdm/#bot-dmstack-connected-nodes)
    
*   [@dm:stack-filter](/Bots/cfxdm/#bot-dmstack-filter)
    
*   [@dm:stack-find-impact-distances](/Bots/cfxdm/#bot-dmstack-find-impact-distances)
    
*   [@dm:stack-join](/Bots/cfxdm/#bot-dmstack-join)
    
*   [@dm:stack-list](/Bots/cfxdm/#bot-dmstack-list)
    
*   [@dm:stack-load](/Bots/cfxdm/#bot-dmstack-load)
    
*   [@dm:stack-save](/Bots/cfxdm/#bot-dmstack-save)
    
*   [@dm:stack-search](/Bots/cfxdm/#bot-dmstack-search)
    
*   [@dm:stack-select-nodes](/Bots/cfxdm/#bot-dmstack-select-nodes)
    
*   [@dm:stack-unselect-nodes](/Bots/cfxdm/#bot-dmstack-unselect-nodes)
    

**Related RDA Client CLI Commands**
```
     stack-cache-list          List cached stack entries from asset-dependency service 
     stack-impact-distance     Find the impact distances in a stack using asset-dependency service, 
                               load search criteria from a JSON file 
     stack-search              Search in a stack using asset-dependency service 
     stack-search-json         Search in a stack using asset-dependency service,  
                               load searchcriteria from a JSON file
 ```

[See RDA CLI Guide for installation instructions](/beginners_guide/rdac/)

**Managing through RDA Portal**

*   In RDA Portal, Click on left menu **Data**
*   Click on **View Details** next to **Dependency Mappings**

[![Portal](https://bot-docs.cloudfabrix.io/images/guide/portal_stack.png)](/images/guide/portal_stack.png)

**Managing through RDA Studio** \* Both RDA Studio & RDA Fabric share this artifact \* In RDA Studio, Select Task **Explore: Stacks**

[![Studio](https://bot-docs.cloudfabrix.io/images/guide/studio_stacks.png)](/images/guide/studio_stacks.png)

* * *

## 5\. RDA Objects

RDA Objects can be any arbitrary data including binary data such as Images, Videos, Pickled Objects.

**Storage Location** \* RDA Fabric Object Storage

**Related Bots** \* [@dm:object-add](/Bots/cfxdm/#bot-dmobject-add)
 \* [@dm:object-delete](/Bots/cfxdm/#bot-dmobject-delete)
 \* [@dm:object-delete-list](/Bots/cfxdm/#bot-dmobject-delete-list)
 \* [@dm:object-get](/Bots/cfxdm/#bot-dmobject-get)
 \* [@dm:object-list](/Bots/cfxdm/#bot-dmobject-list)
 \* [@dm:object-to-inline-img](/Bots/cfxdm/#bot-dmobject-to-inline-img)
 \* [@dm:object-to-file](/Bots/cfxdm/#bot-dmobject-to-file)
 \* [@dm:object-to-content](/Bots/cfxdm/#bot-dmobject-to-content)

**Related RDA Client CLI Commands**
```
     content-to-object         Convert data from a column into objects 
     file-to-object            Convert files from a column into objects 
     object-add                Add a new object to the object store 
     object-delete             Delete object from the object store 
     object-delete-list        Delete list of objects 
     object-get                Download a object from the object store 
     object-list               List objects from the object store 
     object-meta               Download metadata for an object from the object store 
     object-to-content         Convert object pointers from a column into content 
     object-to-file            Convert object pointers from a column into file 
     object-to-inline-img      Convert object pointers from a column into inline HTML img tags
 ```

[See RDA CLI Guide for installation instructions](/beginners_guide/rdac/)

**Managing through RDA Portal**

*   RDA Objects are only managed by RDA Pipelines & CLI

**Managing through RDA Studio** \* RDA Objects are only managed by RDA Pipelines & CLI

* * *

## 6\. Job Outputs

Output of recently executed pipelines. RDAF retains Job Outputs for 4 hours after completion of a pipeline execution job.

If the pipeline developer does not want to save the final output, it is recommended that final bot of the pipeline be [@dm:empty](/Bots/cfxdm/#bot-dmempty)

**Storage Location** \* RDA Fabric Object Storage

**Related RDA Client CLI Commands**
```
     output                    Get the output of a Job using jobid. 
     purge-outputs             Purge outputs of completed jobs
 ```

* * *

## 7\. Persistent Streams

[RDA Streams](#streams)
 allow streaming of data from Edge to Cloud and between pipelines. Persistent Streams allow automatic persistence of data into Opensearch (OS) / Elasticsearch (ES).

Persisting continuously streamed data into OS/ES, allows it to be indexed and can be queried.

**List of Automatically Persisted Streams**

| Stream Name | Retention  <br>(Days) | Description |
| --- | --- | --- |
| rda\_system\_feature\_usage | 31  | RDA Portal and Studio capture all usage metrics by feature.  <br>This report is accessible via left side menu **Analytics** |
| rda\_system\_deployment\_updates | 31  | Audit trail of changes to Service Blueprints |
| rda\_system\_gw\_endpoint\_metrics | 31  | RDA Event Gateway data ingestion metrics by ingestion endpoint |
| rda\_system\_worker\_trace\_summary | 31  | Pipeline execution statistics by Site, Bots etc. |
| rda\_worker\_resource\_usage | 31  | Resource usage metrics published by RDA Workers |
| rda\_system\_gw\_log\_archival\_updates | 31  | Log Archive metrics by RDA Event Gateway |
| rda\_system\_log\_replays | 31  | Audit trail of Log Archive replays |
| rda\_system\_worker\_traces | 1   | Detailed execution traces for each pipeline, published by RDA Workers |

**Storage Location** \* Metadata: RDA Fabric Object Storage \* Data: In RDA Fabric Opensearch or Customer provided OS/ES (See [Data Plane Policy](#dataplane)
)

**Related Bots** \* [@dm:create-persistent-stream](/Bots/cfxdm/#bot-dmcreate-persistent-stream)

**Related RDA Client CLI Commands**
```
     pstream-add               Add a new Persistent stream 
     pstream-delete            Delete a persistent stream 
     pstream-get               Get information about a persistent stream 
     pstream-list              List persistent streams 
     pstream-query             Query persistent stream data via collector 
     pstream-tail              Query a persistent stream and continue to query for incremental data every few seconds
 ```

Deleting Persistent Streams

Deleting a persistent stream only deletes metadata about persistent stream. It will stop persisting any new data.

Does not delete already persisted data from underlying OS/ES.

**Managing through RDA Portal**

In RDA Portal, Click on left menu Data

*   In RDA Portal, Click on left menu **Data**
*   Click on 'View Details' next to **Persistent Streams**

[![Portal](https://bot-docs.cloudfabrix.io/images/guide/portal_pstreams.png)](/images/guide/portal_pstreams.png)

**Configuring Data Plane Policy**

RDA Fabric available at [cfxCloud](https://www.cloudfabrix.com/signup/)
 provides a built-in Opensearch for storing usage data and many operational metrics for RDA Fabric itself.

It can also be used to store data ingested by the Fabric on an experimental basis. To route & store large amount of data, users may provide their own Cloud Hosted Opensearch/ Elasticsearch.

Following is an example how the policy can be configured either for cfxCloud or on-premises or customer's own cloud deployments:

Example Policy JSON

|     |     |
| --- | --- |
| 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br> 
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
 | `{     "pstream-mappings": [         {             "pattern": "app-logs.*",             "es_name": "es1"         },         {             "pattern": "infra-logs.*",             "es_name": "es2"         },         {             "pattern": "rda.*",             "es_name": "default"         },         {             "pattern": ".*",             "es_name": "default"         }     ],     "credentials": {         "es": {             "es1": {                 "hosts": [ "my-opensearch-host" ],                 "port":"9200",                 "user":"**********",                 "password":"**********",                 "scheme" : "https"             },             "es2": {                 "hosts": [ "my-elasticsearch-host" ],                 "port":"9200",                 "user":"**********",                 "password":"**********",                 "scheme" : "https"             }         }     } }` |

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!