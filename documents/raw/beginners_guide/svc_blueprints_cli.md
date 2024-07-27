 



Managing Service Blueprints using RDA CLI
=========================================

1\. Prerequisites
-----------------

User must have following :

1.  Access the rdac cli
2.  Worker Site name/Label
3.  Required bot source credentials if any
4.  Published pipeline name and version

2\. Steps to follow to deploy service blueprint using RDAC CLI
--------------------------------------------------------------

Run below command to verify necessary microservices are running:

`[](#__codelineno-0-1) rdac.py pods --v`

Output should be similar to:

[Example Output](#__tabbed_1_1)

`[](#__codelineno-1-1) Detected OS Name: Linux [](#__codelineno-1-2) Detected docker version: 20.10.12 [](#__codelineno-1-3) +-------+---------------------+--------------+----------+---------------+----------------+---------------+---------------------+--------------------+-------------+ [](#__codelineno-1-4) | Cat   | Pod-Type            | Host         | ID       | Site          | Age            | Pod Version   | Messenger Version   | Platform Version   | Build Tag   | [](#__codelineno-1-5) |-------+---------------------+--------------+----------+---------------+----------------+---------------+---------------------+--------------------+-------------| [](#__codelineno-1-6) | App   | alert-state-manager | 667de09aa8e8 | 80334eea |               | 1 day, 5:46:40 |               | 22.6.21.1           |                    | daily       | [](#__codelineno-1-7) | Infra | collector           | b4ca2fae6c5b | ec9da6b4 |               | 1 day, 5:52:41 | 22.5.20.1     | 22.6.21.1           |                    | daily       | [](#__codelineno-1-8) | Infra | registry            | 2839102b0fe8 | 31acab9f |               | 1 day, 5:52:42 | 22.6.8.1      | 22.6.21.1           |                    | daily       | [](#__codelineno-1-9) | Infra | scheduler           | eddb1a147f5f | e4ac4817 | *leader*      | 1 day, 5:52:42 | 22.6.20.1     | 22.6.21.1           |                    | daily       | [](#__codelineno-1-10) | Infra | schedulerAdmin      | e73e42ec5cbe | 59558b8f |               | 1 day, 5:52:42 | 22.6.20.1     | 22.6.21.1           |                    | daily       | [](#__codelineno-1-11) | Infra | worker              | a1079bec23ce | 2401cc8c | rda-worker-01 | 0:14:57        | 22.6.17.3     | 22.6.21.1           | 22.6.22.1          | daily       | [](#__codelineno-1-12) +-------+---------------------+--------------+----------+---------------+----------------+---------------+---------------------+--------------------+-------------+`

**`rda-worker-01`** is the site label here .

### 2.2 Service blueprint template

Template are defined in YAML format. Following is a simple example file. Going forward this file will be referred to as `service-blueprint.yml`

| service-blueprint.yml |     |
| --- | --- |
| [1](#__codelineno-2-1)<br> [2](#__codelineno-2-2)<br> [3](#__codelineno-2-3)<br> [4](#__codelineno-2-4)<br> [5](#__codelineno-2-5)<br> [6](#__codelineno-2-6)<br> [7](#__codelineno-2-7)<br> [8](#__codelineno-2-8)<br> [9](#__codelineno-2-9)<br>[10](#__codelineno-2-10)<br>[11](#__codelineno-2-11)<br>[12](#__codelineno-2-12)<br>[13](#__codelineno-2-13)<br>[14](#__codelineno-2-14)<br>[15](#__codelineno-2-15)<br>[16](#__codelineno-2-16)<br>[17](#__codelineno-2-17)<br>[18](#__codelineno-2-18)<br>[19](#__codelineno-2-19) | `name: bookmark-test id: bookmarktest2022_06_22_01 version: '2022_06_22_01' category: bookmark-tests comment: bookmark-tests enabled: true type: Service provider: RDA CloudFabrix service_pipelines:     -   name: bookmark-tests         label: bookmark-tests         version: '*'         site: rda-worker-01         site_type: regex         instances: 1         scaling_policy:             min_instances: 1             max_instances: 1` |

**`service-blueprint.yml`** file needs to update by the user sections: `service_pipelines` and `deployment details`.

Following are the parameters we used in the Service Blueprint:

`name`: Name of the Blueprint. This is visible in the Services.

`id`: Unique ID for the service. Each Service Blueprint ID in an RDA Fabric should be unique.

`version`: Version of the blueprint in YYYY\_MM\_DD\_n format.

`category`: Optional label for the blueprint category. Example categories are ITSM, ITOM, AIOPS, Log Analytics. Optional.

`comment`: A descriptive text explaining the blueprint purpose. Optional

`enabled`: Boolean value. If set to false, blueprint will be disabled and pipelines will not be scheduled for execution.

`type`: Must be set to 'Service'.

`provider`: Name of the company or contact information creator of the blueprint. Optional.

`service_pipelines`: List. Zero or more objects listing pipelines that are part of the Service. See below for more details.

### 2.3 Service Pipelines Section (`service_pipelines`)

In RDA Service Blueprints, the term Service Pipeline implies that pipeline must be in always running mode. These pipelines are typically infinite looping pipelines or pipelines reading from a stream. RDAF monitors the status of each Service Pipeline continuously. If any of the Service Pipeline exits or fails, it will restart.

Let us take a look at the first Service Pipeline in our blueprint above:

`[](#__codelineno-3-1) service_pipelines: [](#__codelineno-3-2)     -   name: bookmark-tests [](#__codelineno-3-3)         label: bookmark-tests [](#__codelineno-3-4)         version: '*' [](#__codelineno-3-5)         site: rda-worker-01 [](#__codelineno-3-6)         site_type: regex [](#__codelineno-3-7)         instances: 1 [](#__codelineno-3-8)         scaling_policy: [](#__codelineno-3-9)             min_instances: 1 [](#__codelineno-3-10)             max_instances: 1`

Service Pipeline parameters:

`name`: Name of the Pipeline

`label`: Label for the Pipeline

`version`: Version of the pipeline to use. \* implies any latest version of the pipeline.

`site_type`: Valid values are regex or name. If set to regex, the site parameter is interpreted as a regular expression. If set to name, the site parameter is interpreted as an exact name of the site. Default is regex

`site`: Either name of pattern identifying the Site for the RDA Worker(s). RDAF uses prefix cfx- for all workers hosted in cfxCloud.

`instances`: Number of instances to start for this Service Pipeline. Default is 1. If set to 0, no instances would be scheduled. User can configure this value from RDA Portal.

`scaling_policy`: Defines manual scaling policy for this service pipeline.

`min_instances`: Minimum number of instances user is allowed to configure for this service pipeline.

`max_instances`: Maximum number of instances user is allowed to configure for this service pipeline.

After updated the all details save the file name as **`service-blueprint.yml`**

3\. Finding the bot sources and type from the published pipeline
----------------------------------------------------------------

Run below command to list published pipelines

`[](#__codelineno-4-1) rdac.py  pipeline list`

[Example Output](#__tabbed_2_1)

`[](#__codelineno-5-1) Detected OS Name: Linux [](#__codelineno-5-2) Detected docker version: 20.10.12 [](#__codelineno-5-3) category                                         description    name                        saved_time                  usecase                                                 version [](#__codelineno-5-4) -----------------------------------------------  -------------  --------------------------  --------------------------  -----------------------------------------------  -------------- [](#__codelineno-5-5)                                                  test pipeline  basic-test                  2022-04-26T17:40:55.243861                                                    2022_04_26_01 [](#__codelineno-5-6) bookmark-test                                    test pipeline  bookmark-test               2022-06-22T21:53:09.233161  bookmark-test                                    2022_06_22_02 [](#__codelineno-5-7) bookmark-tests                                   test pipeline  bookmark-tests              2022-06-22T22:18:21.281638  bookmark-tests                                    2022_06_22_02 [](#__codelineno-5-8) Consume synthetic logs, Archive and then Filter  test pipeline  guide-example-consume-logs  2022-06-22T17:43:31.559167  Consume synthetic logs, Archive and then Filter   2022_06_21_01 [](#__codelineno-5-9) Produce Synthetic Syslog                         test pipeline  guide-example-produce-logs  2022-06-22T17:42:29.147322  Produce Synthetic Syslog                          2022_06_21_01`

Command to get published pipeline details

`[](#__codelineno-6-1) rdac.py  pipeline get --name <pipeline_name> --version <version>`

Example :

`[](#__codelineno-7-1) rdac.py  pipeline get --name bookmark-tests --version 2022_06_22_02`

[Example Output](#__tabbed_3_1)

`[](#__codelineno-8-1) Detected OS Name: Linux [](#__codelineno-8-2) Detected docker version: 20.10.12 [](#__codelineno-8-3) name: bookmark-tests [](#__codelineno-8-4) description: test pipeline [](#__codelineno-8-5) usecase: bookmark-tests [](#__codelineno-8-6) category: bookmark-tests [](#__codelineno-8-7) version: '2022_06_22_02' [](#__codelineno-8-8) sources: [](#__codelineno-8-9)   snowv2: [](#__codelineno-8-10)     name: snowv2 [](#__codelineno-8-11)     type: servicenow_v2 [](#__codelineno-8-12)   rn: [](#__codelineno-8-13)     name: rn [](#__codelineno-8-14)     type: rn [](#__codelineno-8-15) data: [](#__codelineno-8-16)   name: bookmark-tests [](#__codelineno-8-17)   sequence: [](#__codelineno-8-18)   - tag: '@c:bookmark-loop' [](#__codelineno-8-19)     query: 'bookmark = ''ebonding-snow-incidents'' [](#__codelineno-8-20) [](#__codelineno-8-21)       & initial_value = ''-1 hour'' [](#__codelineno-8-22) [](#__codelineno-8-23)       & offset_reset = "latest"' [](#__codelineno-8-24)     comment: Create a bookmark for streaming data. [](#__codelineno-8-25)   - tag: '@dm:empty' [](#__codelineno-8-26)   - tag: '@dm:addrow' [](#__codelineno-8-27)     query: 'table="incident" & [](#__codelineno-8-28) [](#__codelineno-8-29)       limit=0' [](#__codelineno-8-30)   - tag: '#snowv2:query-table' [](#__codelineno-8-31)     query: sys_created_on is after '${bookmark}' [](#__codelineno-8-32)   - tag: '@rn:write-stream' [](#__codelineno-8-33)     query: name = "snow-incidents" [](#__codelineno-8-34)     comment: write incident to the stream [](#__codelineno-8-35)   - tag: '@dm:save_bookmark' [](#__codelineno-8-36)     query: 'name = ''ebonding-snow-incidents'' & [](#__codelineno-8-37) [](#__codelineno-8-38)       value_column = ''sys_created_on'' & [](#__codelineno-8-39) [](#__codelineno-8-40)       value_type = ''timestamp'' & [](#__codelineno-8-41) [](#__codelineno-8-42)       value_func = ''max''' [](#__codelineno-8-43)     comment: update bookmark [](#__codelineno-8-44)   - tag: '@rn:write-stats-to-stream' [](#__codelineno-8-45)     query: 'name = "ebonding-analytics" & [](#__codelineno-8-46) [](#__codelineno-8-47)       groupby = "category,priority,severity,company" & [](#__codelineno-8-48) [](#__codelineno-8-49)       type = "ServiceNow" & [](#__codelineno-8-50) [](#__codelineno-8-51)       mode = "input"' [](#__codelineno-8-52)     comment: update stats [](#__codelineno-8-53) artifacts: [](#__codelineno-8-54) - artifact_type: rda-network-stream [](#__codelineno-8-55)   artifact_name: snow-incidents [](#__codelineno-8-56)   access: write [](#__codelineno-8-57) - artifact_type: bookmark [](#__codelineno-8-58)   artifact_name: ebonding-snow-incidents [](#__codelineno-8-59)   access: write [](#__codelineno-8-60) - artifact_type: rda-network-stream [](#__codelineno-8-61)   artifact_name: ebonding-analytics [](#__codelineno-8-62)   access: write`

Let us take a look at the sections: `sources` from above:

`[](#__codelineno-9-1) sources: [](#__codelineno-9-2)   snowv2: [](#__codelineno-9-3)     name: snowv2 [](#__codelineno-9-4)     type: servicenow_v2`

user need to add secrets for listed bot source

### 3.3 Adding secrets credentials using RDAC CLI

Adding bot source with name: `snowv2` and type: `servicenow_v2`

`[](#__codelineno-10-1) rdac.py secret-add --type servicenow_v2` 

[Example Inputs](#__tabbed_4_1)

`[](#__codelineno-11-1) Detected OS Name: Linux [](#__codelineno-11-2) Detected docker version: 20.10.12 [](#__codelineno-11-3) Configure : ServiceNow - Read, Write and Update ServiceNow tables [](#__codelineno-11-4) [](#__codelineno-11-5) Name*: snowv2 [](#__codelineno-11-6) Instance ID: dev96995 [](#__codelineno-11-7) Hostname:  [](#__codelineno-11-8) Username*: admin [](#__codelineno-11-9) Password*:  [](#__codelineno-11-10) Add to Default Site Profile: yes`

Similarly we need to add other secrets / credentials, if we list in sections: `sources` from above:

4\. Deploying Service blueprints
--------------------------------

Command to deploy blueprints

`[](#__codelineno-12-1) rdac.py deployment add --file <serviceblueprintfilename.yaml>`

Example :

`[](#__codelineno-13-1) rdac.py deployment add --file service-blueprint2.yaml`

Output should be similar to:

[Example Output](#__tabbed_5_1)

`[](#__codelineno-14-1) Detected OS Name: Linux [](#__codelineno-14-2) Detected docker version: 20.10.12 [](#__codelineno-14-3) Added deployment spec with Name: Beginner Guide Blueprint, ID: rdaccli2022062201`

**`ID`** is the deployment\_id .

Command to check audit-reports

`[](#__codelineno-15-1) rdac.py deployment audit-report --id <deployment_id>`

Example :

`[](#__codelineno-16-1) rdac.py deployment audit-report --id bookmarktest2022_06_22_01`

Output should be similar to:

[Example Output](#__tabbed_6_1)

`[](#__codelineno-17-1) Detected OS Name: Linux [](#__codelineno-17-2) Detected docker version: 20.10.12 [](#__codelineno-17-3)     type             severity    message [](#__codelineno-17-4) --  ---------------  ----------  ---------------------------------------------------------------------- [](#__codelineno-17-5)  0  Verify Pipeline  INFO        Pipeline with name 'bookmark-tests' and version '2022_06_22_01' loaded [](#__codelineno-17-6)  1  Verify Site      INFO        Site rda-worker-01 has 1 active workers(s) [](#__codelineno-17-7)  2  Verify Source    INFO        Credential found for Integration: snowv2, Type: servicenow_v2`

If we see any ERROR in **`severity`** user need to fix based on the message.

Command to check service status

`[](#__codelineno-18-1) rdac.py deployment svcs-status --id <deployment_id>`

Example :

`[](#__codelineno-19-1) rdac.py deployment svcs-status --id bookmarktest2022_06_22_01`

Output should be similar to:

[Example Output](#__tabbed_7_1)

`[](#__codelineno-20-1) Detected OS Name: Linux [](#__codelineno-20-2) Detected docker version: 20.10.12 [](#__codelineno-20-3)     label           pipeline_name    version      min_instances    max_instances    instances    num_jobs [](#__codelineno-20-4) --  --------------  ---------------  ---------  ---------------  ---------------  -----------  ---------- [](#__codelineno-20-5)  0  bookmark-tests  bookmark-tests   *                        1                1            1           1`

Command to check watch traces

`[](#__codelineno-21-1) rdac.py watch traces --attr deployment_id=<deployment_id>`

Example :

`[](#__codelineno-22-1) rdac.py watch traces --attr deployment_id=bookmarktest2022_06_22_01`

Output should be similar to:

[Example Output](#__tabbed_8_1)

`[](#__codelineno-23-1) Detected OS Name: Linux [](#__codelineno-23-2) Detected docker version: 20.10.12 [](#__codelineno-23-3)  Host         Pipeline                       JobID    Seq Status      Bot                       Dataframe  Error Message  [](#__codelineno-23-4)  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @rn:write-stream          0x0          [](#__codelineno-23-5)  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @dm:save_bookmark         0x0          [](#__codelineno-23-6)  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @rn:write-stats-to-stream 0x0          [](#__codelineno-23-7)  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @dm:empty                 0x0          [](#__codelineno-23-8)  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @dm:addrow                0x0          [](#__codelineno-23-9)  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress #snowv2:query-table       1x2          [](#__codelineno-23-10)  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @rn:write-stream          0x0          [](#__codelineno-23-11)  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @dm:save_bookmark         0x0          [](#__codelineno-23-12)  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @rn:write-stats-to-stream 0x0`       

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!