 



# Managing Service Blueprints using RDA CLI

## 1\. Prerequisites

User must have following :

1.  Access the rdac cli
2.  Worker Site name/Label
3.  Required bot source credentials if any
4.  Published pipeline name and version

## 2\. Steps to follow to deploy service blueprint using RDAC CLI

Run below command to verify necessary microservices are running:
```
 rdac.py pods --v

```

Output should be similar to:

[Example Output](#__tabbed_1_1)
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
 +-------+---------------------+--------------+----------+---------------+----------------+---------------+---------------------+--------------------+-------------+ 
 | Cat   | Pod-Type            | Host         | ID       | Site          | Age            | Pod Version   | Messenger Version   | Platform Version   | Build Tag   | 
 |-------+---------------------+--------------+----------+---------------+----------------+---------------+---------------------+--------------------+-------------| 
 | App   | alert-state-manager | 667de09aa8e8 | 80334eea |               | 1 day, 5:46:40 |               | 22.6.21.1           |                    | daily       | 
 | Infra | collector           | b4ca2fae6c5b | ec9da6b4 |               | 1 day, 5:52:41 | 22.5.20.1     | 22.6.21.1           |                    | daily       | 
 | Infra | registry            | 2839102b0fe8 | 31acab9f |               | 1 day, 5:52:42 | 22.6.8.1      | 22.6.21.1           |                    | daily       | 
 | Infra | scheduler           | eddb1a147f5f | e4ac4817 | *leader*      | 1 day, 5:52:42 | 22.6.20.1     | 22.6.21.1           |                    | daily       | 
 | Infra | schedulerAdmin      | e73e42ec5cbe | 59558b8f |               | 1 day, 5:52:42 | 22.6.20.1     | 22.6.21.1           |                    | daily       | 
 | Infra | worker              | a1079bec23ce | 2401cc8c | rda-worker-01 | 0:14:57        | 22.6.17.3     | 22.6.21.1           | 22.6.22.1          | daily       | 
 +-------+---------------------+--------------+----------+---------------+----------------+---------------+---------------------+--------------------+-------------+

```

**`rda-worker-01`** is the site label here .

### 2.2 Service blueprint template

Template are defined in YAML format. Following is a simple example file. Going forward this file will be referred to as `service-blueprint.yml`

| service-blueprint.yml |     |
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
 | `name: bookmark-test id: bookmarktest2022_06_22_01 version: '2022_06_22_01' category: bookmark-tests comment: bookmark-tests enabled: true type: Service provider: RDA CloudFabrix service_pipelines:     -   name: bookmark-tests         label: bookmark-tests         version: '*'         site: rda-worker-01         site_type: regex         instances: 1         scaling_policy:             min_instances: 1             max_instances: 1` |

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
```
 service_pipelines: 
     -   name: bookmark-tests 
         label: bookmark-tests 
         version: '*' 
         site: rda-worker-01 
         site_type: regex 
         instances: 1 
         scaling_policy: 
             min_instances: 1 
             max_instances: 1

```

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

## 3\. Finding the bot sources and type from the published pipeline

Run below command to list published pipelines
```
 rdac.py  pipeline list

```

[Example Output](#__tabbed_2_1)
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
 category                                         description    name                        saved_time                  usecase                                                 version 
 -----------------------------------------------  -------------  --------------------------  --------------------------  -----------------------------------------------  -------------- 
                                                  test pipeline  basic-test                  2022-04-26T17:40:55.243861                                                    2022_04_26_01 
 bookmark-test                                    test pipeline  bookmark-test               2022-06-22T21:53:09.233161  bookmark-test                                    2022_06_22_02 
 bookmark-tests                                   test pipeline  bookmark-tests              2022-06-22T22:18:21.281638  bookmark-tests                                    2022_06_22_02 
 Consume synthetic logs, Archive and then Filter  test pipeline  guide-example-consume-logs  2022-06-22T17:43:31.559167  Consume synthetic logs, Archive and then Filter   2022_06_21_01 
 Produce Synthetic Syslog                         test pipeline  guide-example-produce-logs  2022-06-22T17:42:29.147322  Produce Synthetic Syslog                          2022_06_21_01

```

Command to get published pipeline details
```
 rdac.py  pipeline get --name <pipeline_name> --version <version>

```

Example :
```
 rdac.py  pipeline get --name bookmark-tests --version 2022_06_22_02

```

[Example Output](#__tabbed_3_1)
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
 name: bookmark-tests 
 description: test pipeline 
 usecase: bookmark-tests 
 category: bookmark-tests 
 version: '2022_06_22_02' 
 sources: 
   snowv2: 
     name: snowv2 
     type: servicenow_v2 
   rn: 
     name: rn 
     type: rn 
 data: 
   name: bookmark-tests 
   sequence: 
   - tag: '@c:bookmark-loop' 
     query: 'bookmark = ''ebonding-snow-incidents'' 
 
       & initial_value = ''-1 hour'' 
 
       & offset_reset = "latest"' 
     comment: Create a bookmark for streaming data. 
   - tag: '@dm:empty' 
   - tag: '@dm:addrow' 
     query: 'table="incident" & 
 
       limit=0' 
   - tag: '#snowv2:query-table' 
     query: sys_created_on is after '${bookmark}' 
   - tag: '@rn:write-stream' 
     query: name = "snow-incidents" 
     comment: write incident to the stream 
   - tag: '@dm:save_bookmark' 
     query: 'name = ''ebonding-snow-incidents'' & 
 
       value_column = ''sys_created_on'' & 
 
       value_type = ''timestamp'' & 
 
       value_func = ''max''' 
     comment: update bookmark 
   - tag: '@rn:write-stats-to-stream' 
     query: 'name = "ebonding-analytics" & 
 
       groupby = "category,priority,severity,company" & 
 
       type = "ServiceNow" & 
 
       mode = "input"' 
     comment: update stats 
 artifacts: 
 - artifact_type: rda-network-stream 
   artifact_name: snow-incidents 
   access: write 
 - artifact_type: bookmark 
   artifact_name: ebonding-snow-incidents 
   access: write 
 - artifact_type: rda-network-stream 
   artifact_name: ebonding-analytics 
   access: write

```

Let us take a look at the sections: `sources` from above:
```
 sources: 
   snowv2: 
     name: snowv2 
     type: servicenow_v2

```

user need to add secrets for listed bot source

### 3.3 Adding secrets credentials using RDAC CLI

Adding bot source with name: `snowv2` and type: `servicenow_v2`
```
 rdac.py secret-add --type servicenow_v2

``` 

[Example Inputs](#__tabbed_4_1)
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
 Configure : ServiceNow - Read, Write and Update ServiceNow tables 
 
 Name*: snowv2 
 Instance ID: dev96995 
 Hostname:  
 Username*: admin 
 Password*:  
 Add to Default Site Profile: yes

```

Similarly we need to add other secrets / credentials, if we list in sections: `sources` from above:

## 4\. Deploying Service blueprints

Command to deploy blueprints
```
 rdac.py deployment add --file <serviceblueprintfilename.yaml>

```

Example :
```
 rdac.py deployment add --file service-blueprint2.yaml

```

Output should be similar to:

[Example Output](#__tabbed_5_1)
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
 Added deployment spec with Name: Beginner Guide Blueprint, ID: rdaccli2022062201

```

**`ID`** is the deployment\_id .

Command to check audit-reports
```
 rdac.py deployment audit-report --id <deployment_id>

```

Example :
```
 rdac.py deployment audit-report --id bookmarktest2022_06_22_01

```

Output should be similar to:

[Example Output](#__tabbed_6_1)
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
     type             severity    message 
 --  ---------------  ----------  ---------------------------------------------------------------------- 
  0  Verify Pipeline  INFO        Pipeline with name 'bookmark-tests' and version '2022_06_22_01' loaded 
  1  Verify Site      INFO        Site rda-worker-01 has 1 active workers(s) 
  2  Verify Source    INFO        Credential found for Integration: snowv2, Type: servicenow_v2

```

If we see any ERROR in **`severity`** user need to fix based on the message.

Command to check service status
```
 rdac.py deployment svcs-status --id <deployment_id>

```

Example :
```
 rdac.py deployment svcs-status --id bookmarktest2022_06_22_01

```

Output should be similar to:

[Example Output](#__tabbed_7_1)
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
     label           pipeline_name    version      min_instances    max_instances    instances    num_jobs 
 --  --------------  ---------------  ---------  ---------------  ---------------  -----------  ---------- 
  0  bookmark-tests  bookmark-tests   *                        1                1            1           1

```

Command to check watch traces
```
 rdac.py watch traces --attr deployment_id=<deployment_id>

```

Example :
```
 rdac.py watch traces --attr deployment_id=bookmarktest2022_06_22_01

```

Output should be similar to:

[Example Output](#__tabbed_8_1)
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
  Host         Pipeline                       JobID    Seq Status      Bot                       Dataframe  Error Message  
  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @rn:write-stream          0x0          
  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @dm:save_bookmark         0x0          
  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @rn:write-stats-to-stream 0x0          
  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @dm:empty                 0x0          
  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @dm:addrow                0x0          
  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress #snowv2:query-table       1x2          
  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @rn:write-stream          0x0          
  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @dm:save_bookmark         0x0          
  a1079bec23ce bookmark-tests                 88182d7f 109 in-progress @rn:write-stats-to-stream 0x0

```       

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!