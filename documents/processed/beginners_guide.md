 



# Beginner's Guide to Building Pipelines and Service Blueprints in RDA Fabric

This document captures step-by-step instructions to build few simple RDA Pipelines and create a Service Blueprint in Robotic Data Automation Fabric (RDAF).

  

#### 1\. Introduction (Pre-requisites)

Before you proceed, make sure you have access to following

*    **RDA Studio:** A Jupyter notebook based User Interface for developing, testing RDA Pipelines.
*    **RDA Portal:** Provides a Cloud based User Interface to run pipelines in cfxCloud or in your on-premises RDA environment

Free RDA Studio and Portal can be accessed in cfxCloud by simply [signing up](https://cloudfabrix.io/start)
 with an email address.

As a first step, login to RDA Studio. It would show an App Launcher:

[![Studio Launcher](https://bot-docs.cloudfabrix.io/images/guide/studio_launcher.png)](/images/guide/studio_launcher.png)

Click on **RDA Python 3** Notebook icon to open a new notebook.

Once the notebook is open, in an empty notebook cell, type `studio()` and then press Shift+Enter

[![Studio Cell](https://bot-docs.cloudfabrix.io/images/guide/studio_cell.png)](/images/guide/studio_cell.png)

  

#### 2\. Starting with a sample dataset

In this example, we will use one of the [Example Datasets](https://bot-docs.cloudfabrix.io/#explore-example-datasets)
. We will specifically use [synthetic\_syslogs\_dataset](https://bot-docs.cloudfabrix.io/Datasets/#synthetic_syslogs_dataset)

In the Studio, Select Task: "Pipelines: Add a New Pipeline" and start with following simple pipeline with just one bot


```
@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/synthetic_syslogs_dataset.csv'
```

It should look like this in your Studio:

[![Studio Step](https://bot-docs.cloudfabrix.io/images/guide/studio_step1.png)](/images/guide/studio_step1.png)

Now, Click on **Execute** to run this very simple pipeline. Pipeline execution should be successful and look like this

[![Studio Step](https://bot-docs.cloudfabrix.io/images/guide/studio_step1b.png)](/images/guide/studio_step1b.png)

Now select the **Inspect** tab, which should show the following output:

[![Studio Step](https://bot-docs.cloudfabrix.io/images/guide/studio_step1c.png)](/images/guide/studio_step1c.png)

  
So far we have used the [@files:loadfile](https://bot-docs.cloudfabrix.io/Bots/file/#loadfile)
. As you can see in the Bot documentation, it is a Source Bot. Which implies that bot produces data to be consumed by other Sink bots. In this case, loadfile bot is downloading the data from a URL and returning dataframe for further processing by other bots.

  

#### 3\. Sending the data to a Sink Bot

The pipeline we have produced 10,000 Rows and 2 Columns. Let us use [@dm:sample](https://bot-docs.cloudfabrix.io/Bots/cfxdm/#sample)
 Bot to randomly select 1% of the rows (100 rows)


```
@files:loadfile            filename = 'https://bot-docs.cloudfabrix.io/data/datasets/synthetic_syslogs_dataset.csv'     --> @dm:sample            n = 0.01
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=bguide_1)

If we examine the final Output of this pipeline now, you should see randomly selected 100 rows. Each time you run the pipeline, it would produce 100 rows from the same original 10,000 Rows.

You will also see that output dataframe has just two columns: Device and Message. Let us add _timestamp_ column using [@dm:eval](https://bot-docs.cloudfabrix.io/Bots/cfxdm/#eval)
 Sink Bot. This bot adds a new column using expressions for each row.


```
@files:loadfile            filename = 'https://bot-docs.cloudfabrix.io/data/datasets/synthetic_syslogs_dataset.csv'     --> @dm:sample            n = 0.01     --> @dm:eval            timestamp = "utcnow().isoformat()"
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=bguide_2)

We have now added new column _timestamp_ in the output:

[![Studio Step](https://bot-docs.cloudfabrix.io/images/guide/studio_step2a.png)](/images/guide/studio_step2a.png)

[@dm:eval](https://bot-docs.cloudfabrix.io/Bots/cfxdm/#eval)
 Bot can also be used to add multiple columns in a single statement.

  

#### 4\. Sending data to a destination

So far we have generated randomly sampled data, but we have not send the data to any destination.

In RDA data can be sent to many destinations. Some of the typical data destinations are:

*   **RDA Datasets:** RDA Stores datasets on Object storage like Minio or S3 or any compatible storage systems. cfxCloud uses built-in object storage by default. See bots [@dm:save](https://bot-docs.cloudfabrix.io/Bots/cfxdm/#save)
     and [@dm:recall](https://bot-docs.cloudfabrix.io/Bots/cfxdm/#recall)
    .
*   Many ITSM/ ITOM / Log Management Systems. Most common destinations for logs are [Splunk](https://bot-docs.cloudfabrix.io/Extensions/extensions_O_S/#extension-splunk_v2)
     and [Elasticsearch / Opensearch](https://bot-docs.cloudfabrix.io/Extensions/extensions_D_E/#extension-elasticsearch_v2)
    
*   **RDA Streams:** RDA provides powerful and flexible way to move the data between different systems and pipelines using Streaming mechanism. More on this topic later.

  
Below is sample pipeline to save the logs to RDA Dataset:

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
 | `@files:loadfile            filename = 'https://bot-docs.cloudfabrix.io/data/datasets/synthetic_syslogs_dataset.csv'     --> @dm:sample            n = 0.01     --> @dm:eval            timestamp = "utcnow().isoformat()"     --> @dm:save            name = "my-generated-logs"` |

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=bguide_3)

Above pipeline saves 100 randomly selected rows to the dataset with name `my-generated-logs`. By using the parameter `append = "yes"`, dataset can be used as a continuously appended dataset. If the dataset name begins with `temp-` prefix, then dataset is only saved in-memory and is deleted once the pipeline execution completes.

For our usecase, let us focus on sending data to RDA Stream.

  

#### 5\. Sending data to RDA Stream

RDA Streams use [NATS](https://nats.io)
 publish-subscribe to exchange data between different pipelines, possibly running in different cloud environments. In addition to NATS, RDA also supports streaming using other similar technologies like [Kafka](https://bot-docs.cloudfabrix.io/Bots/kafka/)
, [MQTT](https://bot-docs.cloudfabrix.io/Extensions/extensions_L_N/#extension-mqtt)
, [AWS Kinesis](https://bot-docs.cloudfabrix.io/Bots/aws-kinesis/)
 and many more.

Data can be written to an RDA Stream by simply using the sink bot [@rn:write-stream](https://bot-docs.cloudfabrix.io/Bots/rn/#write-stream)
:


```
--> @rn:write-stream            name = "synthetic-logs-raw"
```

This pipeline segment converts each row of dataframe as a JSON object, and sends it as a message. RDA Stream name is essentially agreed name between publisher and subscriber.

So the updated pipeline with RDA Streaming would look like this:

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
 | `@files:loadfile            filename = 'https://bot-docs.cloudfabrix.io/data/datasets/synthetic_syslogs_dataset.csv'     --> @dm:sample            n = 0.01     --> @dm:eval            timestamp = "utcnow().isoformat()"     --> @rn:write-stream            name = "synthetic-logs-raw"` |

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=bguide_4)

We will look into how to read / consume the data from an RDA Stream in [section-9](#subsect9)
.

  

#### 6\. Implementing loops

So far the pipeline generates 100 randomly selected log messages and writes to a stream. But, it does only one time. We can use [control](https://bot-docs.cloudfabrix.io/Bots/control/)
 bots to bring looping to the pipelines.

In this case, it might make more sense to generate logs on a periodic basis. So we will use [@c:timed-loop](https://bot-docs.cloudfabrix.io/Bots/control/#timed-loop)
 accomplish this:

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
 | `@c:timed-loop            interval = 60     --> @files:loadfile            filename = 'https://bot-docs.cloudfabrix.io/data/datasets/synthetic_syslogs_dataset.csv'     --> @dm:sample            n = 0.01     --> @dm:eval            timestamp = "utcnow().isoformat()"     --> @rn:write-stream            name = "synthetic-logs-raw"` |

The bot [@c:timed-loop](https://bot-docs.cloudfabrix.io/Bots/control/#timed-loop)
 uses parameter `interval` which is number of seconds between each loop iteration.

Let us take a look at how Studio Inspect shows the looped data:

[![Studio Loop](https://bot-docs.cloudfabrix.io/images/guide/studio_loop1.png)](/images/guide/studio_loop1.png)

> NOTE: [control](https://bot-docs.cloudfabrix.io/Bots/control/)
>  bots do not appear in the Inspect as they do not have any data to show.

  

#### 7\. Using in-memory datasets to cache data

The pipeline is now looping every minute to download a dataset from a URL, do random sampling, add a timestamp column and then write the data to stream. In this case the example dataset has 10,000 rows. What if the dataset is very large, potentially with millions of rows? Downloading it every minute is not optimal use of network resources.

One of the options is to load the data from a URL and keep it in the memory as a `temp-` dataset.


```
@files:loadfile            filename = 'https://bot-docs.cloudfabrix.io/data/datasets/synthetic_syslogs_dataset.csv'     --> @dm:save             name = "temp-syslogs-dataset"
```

Now let us update the whole pipeline:

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
 | `@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/synthetic_syslogs_dataset.csv'     --> @dm:save             name = "temp-syslogs-dataset" --> @c:timed-loop         interval = 60     --> @dm:recall             name = "temp-syslogs-dataset"     --> @dm:sample             n = 0.01     --> @dm:eval             timestamp = "utcnow().isoformat()"     --> @rn:write-stream             name = "synthetic-logs-raw"` |

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=bguide_5)

The updated pipeline now contains two **blocks**. First block downloads the data from a URL and saves it as in-memory dataset `temp-syslogs-dataset`

Second block implements a timed loop. During each iteration, it recalls the in-memory dataset.

We have traded for higher continuous memory usage for reducing number of downloads.

For the sake of future reference, let us save the pipeline with name `guide-example-produce-logs` in RDA Studio

  

#### 8\. Running pipeline from RDA Portal

RDA Studio is a Jupyter notebook based environment for developing, debugging pipelines. Not meant for running pipelines in production RDA Fabric.

All pipelines saved RDA Studio are only meant to run in that Studio. In order to run any pipeline in RDAF, pipelines need to be **Published**.

There are two ways to **publish** a pipeline:

1.  Use RDA Studio action Pipelines: Publish a Pipeline
2.  Copy-paste the pipeline in RDA Portal.

For this exercise, we will use 2nd approach.

Assuming you have already created a free workspace in RDA Portal in Step-1, login into your workspace. You should see following menu on the left side:

![Main Navigation Menu](https://bot-docs.cloudfabrix.io/images/guide/main_navigation_menu2.png)

Click on **Home Menu** -> **Configuration** -> **RDA Administration** which would show:

[![Portal](https://bot-docs.cloudfabrix.io/images/guide/portal_artifacts1.png)](/images/guide/portal_artifacts1.png)

Click on **Pipelines** -> **Draft Pipelines**

[![Portal Draft Pipelines](https://bot-docs.cloudfabrix.io/images/guide/portal_draft_pipelines1.png)](/images/guide/portal_draft_pipelines1.png)

Select **Draft Pipelines** and Click on **Add with Text** action to add the pipeline.

Specify `guide-example-produce-logs` as Pipeline name. Version should be in `YYYY_MM_DD_n` format. Copy paste following contents into the 'Content' section and click 'Save'.

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
 | `@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/synthetic_syslogs_dataset.csv'     --> @dm:save             name = "temp-syslogs-dataset" --> @c:timed-loop         interval = 60     --> @dm:recall             name = "temp-syslogs-dataset"     --> @dm:sample             n = 0.01     --> @dm:eval             timestamp = "utcnow().isoformat()"     --> @rn:write-stream             name = "synthetic-logs-raw"` |

Pipeline table should show following pipeline and Pop-up actions:

[![Portal Pipelines](https://bot-docs.cloudfabrix.io/images/guide/portal_pipeline_2.png)](/images/guide/portal_pipeline_2.png)

Click **Run** from the pop-up actions for that pipeline. RDAF would start running the pipeline on one of the RDA Worker nodes.

You can view most recent **traces** for each bot that is getting executed in this pipeline using **View Traces** popup action.

Example Traces Report would show:

[![Portal Pipelines Traces](https://bot-docs.cloudfabrix.io/images/guide/portal_traces_2.png)](/images/guide/portal_traces_2.png)

  

#### 9\. Reading data from an RDA Stream

Earlier pipeline has been writing randomly selected messages to an RDA Stream. Let us see how we can consume it.

If you have installed [RDA CLI Client](https://bot-docs.cloudfabrix.io/beginners_guide/rdac/)
 in any of the supported environments and if you are already connected your RDAF, you can use following command to verify that messages are being published to the desired stream:
```
 rdac.py read-stream --name "synthetic-logs-raw"

```

It would show output similar to the following:

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
 | `[   {     "device": "10.10.131.55",     "message": "%VSHD-5-VSHD_SYSLOG_CONFIG_I: Configured from vty by admin on 10.10.121.121@pts/1",     "timestamp": "2022-04-14T21:32:43.497033"   },   {     "device": "10.10.131.56",     "message": "%ETHPORT-5-SPEED: Interface Ethernet1/21, operational speed changed to 10 Gbps",     "timestamp": "2022-04-14T21:32:43.497288"   },   {     "device": "10.10.131.55",     "message": "%VSHD-5-VSHD_SYSLOG_CONFIG_I: Configured from vty by admin on 10.10.121.121@pts/1",     "timestamp": "2022-04-14T21:32:43.497536"   },   ... ]` |

Note

`rdac.py read-stream` command can be terminated using Ctrl+C (If you ran the command inside Jupyter notebook, you would need to restart the Kernel to stop the command)

  

#### 10\. Building stream consumer pipeline

For this exercise let us start creating a new pipeline `guide-example-consume-logs`.


```
@rn:read-stream             name = "synthetic-logs-raw"  &             group = "example"
```

The bot [@rn:read-stream](https://bot-docs.cloudfabrix.io/Bots/rn/#read-stream)
 is Source bot. It reads set of messages from the the stream and sends it to next bot (if any).

Note that all bots that read stream are **forever looping bots**. They don't need to be placed inside a loop like write-stream bots.

This bot has two parameters:

*   `name = "synthetic-logs-raw"`: This stream name should match the name used in our producer pipeline.
*   `group = "example"`: This parameter specifies how the data is replicated between different consumers. If two different consumers use same group name, only one of them will receive any specific message posted on that stream. If they use different group names, each consumer will receive copy of every message posted to that stream.

Normally, we would do following tasks in a log / event consumer pipeline (in that order):

1.  Save the raw / unfiltered logs to Log Archive.
2.  Do some filtering and remove some noise / events deemed un-necessary.
3.  Send filtered data to a destination.

For now, we will skip step #1 and come back to this later in this guide.

In real world, we will use more advanced techniques for filtering, but for the sake of this guide, we will use only basic filtering. Most simple way to filter out some data is to use [\*dm:filter](https://bot-docs.cloudfabrix.io/Bots/cfxdm/#bot-dmfilter)
 Bot.

So the pipeline now looks like this:


```
@rn:read-stream             name = "synthetic-logs-raw"  &             group = "example"      --> *dm:filter              device is not in [ "10.10.131.56" ]
```

In the above pipeline we are asking to include any data that matches the specified filter criteria. In this case \*dm:filter bot will filter out any rows where column `device` has value `10.10.131.56`. This bot accepts [CFXQL](https://bot-docs.cloudfabrix.io/reference_guides/cfxql/)
 and refer to the link for full syntax.

Now that we have filtered out some data, let us send remaining data (if any) to a destination. Normally it would be an ITSM or ITOM or Log Management Tool. For simplicity, let us send this to a `NULL` stream.


```
@rn:read-stream             name = "synthetic-logs-raw"  &             group = "example"      --> *dm:filter              device is not in [ "10.10.131.56" ]      --> @rn:write-stream             name = "NULL"
```

In RDAF, `NULL` streams are special purpose streams which simply discard the data.

  

#### 11\. Sending data to Log Archive

RDAF uses AWS S3 or any compatible storages to archive any data using the ingestion timestamp and indexes the data using MINUTE part the timestamp. For example, if the event had been ingested at the timestamp `2022-03-28 15:03:45` it would be saved under the folder `2022/03/28/15/03/` in object storage.

Normally, you would provide storage details for archiving your logs in RDA Portal using menu Data → Log Archives → Add

For the sake of simplicity, we will use RDAF Built-in object storage. The bot [@dm:create-logarchive-repo](/Bots/cfxdm/#bot-dmcreate-logarchive-repo)
 will create a named Log Archive repo in that built-in storage.

Following pipeline would create the archive (if does not exist already):


```
@dm:create-logarchive-repo                  repo = "demo_logarchive" &              prefix = "demo_logs/" &              retention = 31
```

The above bot is using 3 parameters:

*   `repo = "demo_logarchive"`: Name of the log archive repository to be created in object storage
*   `prefix = "demo_logs/"`: Object path prefix inside the object storage bucket.
*   `retention = 31`: How long to retain the data in the archive. In this case keeps minimum of 31 days.

We will use [@dm:logarchive-save](/Bots/cfxdm/#bot-dmlogarchive-save)
 bot to actually save the data in the above archive repository.

Let us take a look at the pipeline that combines reading of data from a stream along with archiving.

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
 | `@dm:create-logarchive-repo                  repo = "demo_logarchive" &              prefix = "demo_logs/" &              retention = 31   --> @c:new-block       --> @rn:read-stream             name = "synthetic-logs-raw"  &             group = "example"       -->  @dm:logarchive-save             repo = "demo_logarchive" &              archive = "exammple_guide_syslogs"      --> *dm:filter              device is not in [ "10.10.131.56" ]      --> @rn:write-stream             name = "NULL"` |

We have created a two **block** pipeline. Once we create the Log Archive in first bot, we need to start reading the data from RDA Stream using `@rn:read-stream` bot. However, `@rn:read-stream` is a Source bot. It can only be used at the beginning of any Block in RDA pipeline. [@c:new-block](/Bots/control/#bot-cnew-block)
 can be used anytime we need to insert simple block.

Within one Log Archive, we can have any number of named Archives. In this case we are saving the data under archive `exammple_guide_syslogs`.

Save the pipeline data in RDA Pipeline using [Section-8 Instructions](#8-running-pipeline-from-rda-portal)
 with name `guide-example-consume-logs`.

  

#### 12\. Stopping the pipelines

**In RDA Studio:**

*   Pipelines can be stopped by restarting the Kernel where the pipelines are currently running

**Using RDA CLI Client**

*   List of active jobs can be queried using `rdac.py jobs`
*   Any specific job can be evicted using `rdac.py evict`

`rdac.py evict` command accepts following parameters:

    `--jobid JOBID  RDA worker jobid. If partial must match only one job.     --yes          Do not prompt for confirmation, evict if job is found`

  

#### 13\. Introducing service blueprints

So far we have seen:

*   How to build a simple pipeline in Studio, Run it, Inspect data
*   How to publish pipelines using RDA Portal and run them in RDAF
*   How to create loops
*   How to read and write to streams
*   How to archive data in object storage.

In this simple example, we have created two pipelines:

*   `guide-example-produce-logs`
*   `guide-example-consume-logs`

These two pipelines can be considered as single **service** as they work together to address a specific need.

In this section we will learn about **RDA Service Blueprints** which will help to:

*   Manage lifecycle of a service in RDA
*   Manage scalability
*   Manage dependencies between pipelines, other artifacts like Credentials
*   Create and Manage Service specific dashboards

Each RDA Service Blueprint is typically a single YAML file. Let us take a look at our first blueprint:

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
 | `name: Beginner Guide Blueprint id: guide001 version: '2022_04_15_1' category: Log Analytics comment: Generate Synthetic Syslogs, Save all logs to Log Archive, send processed logs to a NULL stream enabled: true type: Service provider: Beginner's Guide Developer service_pipelines:     -   name: guide-example-produce-logs         label: Produce Synthetic Syslogs         version: '*'         site: cfx.*         site_type: regex         instances: 1         scaling_policy:             min_instances: 1             max_instances: 1     -   name: guide-example-consume-logs         label: Consume synthetic logs, Archive and then Filter         version: '*'         site: cfx.*         site_type: regex         instances: 1         scaling_policy:             min_instances: 1             max_instances: 1 artifact-dependency-validation:     credentials:         verify: false         exclude: demo_logarchive` |

Following are the parameters we used in the Service Blueprint:

*   `name`: Name of the Blueprint. This is visible in the Services.
*   `id`: Unique ID for the service. Each Service Blueprint ID in an RDA Fabric should be unique.
*   `version`: Version of the blueprint in `YYYY_MM_DD_n` format.
*   `category`: Optional label for the blueprint category. Example categories are ITSM, ITOM, AIOPS, Log Analytics. _Optional_.
*   `comment`: A descriptive text explaining the blueprint purpose. _Optional_
*   `enabled`: Boolean value. If set to `false`, blueprint will be disabled and pipelines will not be scheduled for execution.
*   `type`: Must be set to 'Service'.
*   `provider`: Name of the company or contact information creator of the blueprint. _Optional_.
*   `service_pipelines`: List. Zero or more objects listing pipelines that are part of the **Service**. See below for more details.
*   `artifact-dependency-validation`: Section to control the pre-validation of a blueprint. See below for more details.

**Service Pipelines Section (`service_pipelines`)**

In RDA Service Blueprints, the term **Service Pipeline** implies that pipeline must be in always running mode. These pipelines are typically infinite looping pipelines or pipelines reading from a stream. RDAF monitors the status of each Service Pipeline continuously. If any of the Service Pipeline exits or fails, it will restart.

Let us take a look at the first Service Pipeline in our blueprint above:


```
-   name: 'guide-example-produce-logs'         label: 'Produce Synthetic Syslogs'         version: '*'         site: 'cfx.*'         site_type: regex         instances: 1         scaling_policy:             min_instances: 1             max_instances: 1
```

Service Pipeline parameters:

*   `name`: Name of the Pipeline
*   `label`: Label for the Pipeline
*   `version`: Version of the pipeline to use. `*` implies any latest version of the pipeline.
*   `site_type`: Valid values are `regex` or `name`. If set to `regex`, the **site** parameter is interpreted as a regular expression. If set to `name`, the **site** parameter is interpreted as an exact name of the site. Default is `regex`
*   `site`: Either name of pattern identifying the Site for the RDA Worker(s). RDAF uses prefix `cfx-` for all workers hosted in cfxCloud.
*   `instances`: Number of instances to start for this Service Pipeline. Default is 1. If set to 0, no instances would be scheduled. User can configure this value from RDA Portal.
*   `scaling_policy`: Defines manual scaling policy for this service pipeline.
    
    > *   `min_instances`: Minimum number of instances user is allowed to configure for this service pipeline.
    > *   `max_instances`: Maximum number of instances user is allowed to configure for this service pipeline.
    

**Artifact Validation Section (`artifact-dependency-validation`)**

RDAF performs **audit** of all aspects of a service blueprint on a periodic basis. This audit typically checks for following:

*   Ensure specified pipelines & versions are found in the system
*   Ensure that all artifacts such as Credentials, Datasets and Log Archives are properly created.
*   Ensures that specified sites have at least one RDA Worker deployed.

Warning

If the audit fails, RDAF will not schedule the pipelines.

In this example consumer pipeline, we are creating the log archive repository using bot. So inform the RDAF Audit function to skip this specific validation:


```
artifact-dependency-validation:     credentials:         verify: false         exclude: demo_logarchive
```

  

#### 14\. Deploying service blueprint in RDA Portal

First, let us verify that following two pipelines have been published using RDA Portal:

*   `guide-example-produce-logs`
*   `guide-example-consume-logs`

Login to RDA Portal. click on **Configuration** -> **Rda Administration** -> **Pipelines** -> **Published Pipelines**

Search for `guide` using quick search. If the report looks something like this, we have the necessary pipelines:

[![Portal Pipelines Search](https://bot-docs.cloudfabrix.io/images/guide/portal_guide1_pipelines1.png)](/images/guide/portal_guide1_pipelines1.png)

If you do not see the necessary pipelines, follow the instructions at [Section-8 Instructions](#8-running-pipeline-from-rda-portal)
 and publish the pipelines.

click on **Home Menu** -> **Configuration** -> **Rda Administration** -> **Service Blueprints**

[![Service Blueprints](https://bot-docs.cloudfabrix.io/images/guide/service_blueprints.png)](/images/guide/service_blueprints.png)

Use **Add** action to copy paste following blueprint:

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
 | `name: Beginner Guide Blueprint id: guide001 version: '2022_04_15_1' category: Log Analytics comment: Generate Synthetic Syslogs, Save all logs to Log Archive, send processed     logs to a NULL stream enabled: true type: Service provider: Beginner's Guide Developer service_pipelines:     -   name: guide-example-produce-logs         label: Produce Synthetic Syslogs         version: '*'         site: rda.*         site_type: regex         instances: 1         scaling_policy:             min_instances: 1             max_instances: 1     -   name: guide-example-consume-logs         label: Consume synthetic logs, Archive and then Filter         version: '*'         site: rda.*         site_type: regex         instances: 1         scaling_policy:             min_instances: 1             max_instances: 1 artifact-dependency-validation:     credentials:         verify: false         exclude: demo_logarchive` |

It may take few seconds for the Blueprint to be imported. Click Refresh on the on the report and search for `guide` to look for our blueprint.

[![Service Blueprint](https://bot-docs.cloudfabrix.io/images/guide/import_blueprint.png)](/images/guide/import_blueprint.png)

If the **Audit Errors** and **Audit Warnings** show zeros, it means we have successfully imported.

  

#### 15\. Understanding service blueprint details dashboard

When you **Click** on the example `Beginner Guide Blueprint`, it would look something like this:

**1**. **STATUS**

[![Blueprint Details](https://bot-docs.cloudfabrix.io/images/guide/portal_bp_details1.png)](/images/guide/portal_bp_details1.png)

*   **Summary Report**: This report shows current status of the blueprint and number of audit errors/ warnings. You can see YAML text of the blueprint by clicking 'View'. Blueprint can be Enabled / Disabled from this report.
    
*   **Audit Report**: Shows list of audit checks performed and their status. If there were any errors or warnings, they can be remediated by clicking on the pop-up action for each row.
    
*   **Artifact Dependencies**: Show list of various artifacts consumed / produced by this blueprint.
    

**2**. **SERVICE MAP**

RDAF automatically analyzes the blueprint and all related artifacts, and creates a visual map of the Service and possible interaction between various pipelines, data sources and destinations.

For our example service, the service map would look like this:

[![Service Map](https://bot-docs.cloudfabrix.io/images/guide/portal_bp_servicemap1.png)](/images/guide/portal_bp_servicemap1.png)

By selecting a pipeline or any other artifact, you can view additional details:

[![Service Map](https://bot-docs.cloudfabrix.io/images/guide/portal_bp_servicemap2.png)](/images/guide/portal_bp_servicemap2.png)

**3**. **SERVICES**:

This tab shows current status of all Service Pipelines in the blueprint. Screenshot below shows typical status for our example blueprint:

[![Service Map](https://bot-docs.cloudfabrix.io/images/guide/portal_bp_services_tab1.png)](/images/guide/portal_bp_services_tab1.png)

  

#### 16\. Creating and Deploying the Bundle

**Steps to Take Backup**

**1**. Login to RDA Platform

*   Open your terminal or SSH client.
    
*   Login to the platform using your credentials.
    

**2**. Create a Backup Directory
```
 mkdir <folder_name> 
 
 cd <folder_name>

```

**3**. Backup Command

*   Execute the following command to take a backup
```
 rdac demo backup --to

```

**4**. Compress the Backup

*   Create a compressed tar file
```
 tar -cvzf <new_folder_name>.tar.gz

```

Note

SFTP this .tar.gz to the machine where the user can upload to target RDA environment.

**Steps to Upload and Deploy the Tar File**

**1**. Navigate to the RDA Administration

*   Open the platform UI.
    
*   Go to the **Menu** → **Configuration** → **RDA Administration** → **Bundles**.
    

[![Hamburger Menu](https://bot-docs.cloudfabrix.io/images/guide/hamburger_menu.png)](/images/guide/hamburger_menu.png)

![Configurtion](https://bot-docs.cloudfabrix.io/images/guide/configuration.png)

**2**. Import the Tar File

*   Click on the **Import** button.
    
*   Select the file .tar.gz and upload it. As shown in the below screenshot
    

[![Import Bundles](https://bot-docs.cloudfabrix.io/images/guide/import_bundles.png)](/images/guide/import_bundles.png)

**3**. Deploy the Bundle

*   Once the file is imported, click on the row action corresponding to the uploaded file.

[![Deploy Bundle](https://bot-docs.cloudfabrix.io/images/guide/deploy_bundle.png)](/images/guide/deploy_bundle.png)

*   Select 'Deploy' to deploy the bundle. As shown in the above screenshot
    
*   Optionally, User can check the files being deployed by clicking on the 'Compare' row action.
    

[![Compare](https://bot-docs.cloudfabrix.io/images/guide/compare.png)](/images/guide/compare.png)

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!