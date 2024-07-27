 



# RDA Client Command Line Interface

## 1\. Installing RDA Command Line Tool

RDA Command Line Interface tool comes as a docker image to make it easy to run RDA commands on any Laptop, Desktop or in a Cloud VM.

To run this tool, following are required:

*   Operating Systems: Linux or MacOS
*   Docker installed on that system
*   At least Python 3.0

#### STEP-1: Download the python script
```
 curl -o rdac.py https://bot-docs.cloudfabrix.io/data/wrappers/rdac.py

```

Make the script an executable:
```
 chmod +x rdac.py

```

#### STEP-2: Download RDA network configuration

From your cfxCloud account, you can download a copy the RDA Network configuration.

Download the RDA Network configuration file and save it under `$HOME/.rda/rda_network_config.json`

![Portal](https://bot-docs.cloudfabrix.io/images/guide/rda_credentials.png)

#### STEP-3: Verify Script

Verify that `rdac.py` is working correctly by using one of the following commands:
```
 python3 rdac.py --help

```

Or
```
 ./rdac.py --help

```

For very first time, above script will validate dependencies such OS, Python version and availability of Docker. If the validation is successful, it will download the docker container image for RDA CLI and run it.

Subsequently, if you want to update the docker container image to latest version, run following command:
```
 ./rdac.py update

```

## 2\. RDA Commands: Cheat Sheet

This section lists few most commonly used RDA Commands.

#### Listing RDA Platform Microservices

RDA Fabric is for each tenant has a set of microservices (pods) deployed as containers either using Kubernetes or as simple docker containers.

Following command lists all active microservices in your RDA Fabric:
```
 python3 rdac.py pods

```

Typical output for `pods` command would look like:

![Portal](https://bot-docs.cloudfabrix.io/images/guide/rdac_pods.png)

Most of RDA Commands support option `--json` which would print output in a JSON format instead of tabular format.
```
 python3 rdac.py pods --json

```

Example rdac pods JSON Output

Partial output of `--json` option:
```
 { 
     "now": "2022-05-20T02:16:31.054287", 
     "started_at": "2022-05-17T22:44:13.602509", 
     "pod_type": "worker", 
     "pod_category": "rda_infra", 
     "pod_id": "ae875728", 
     "hostname": "d1d45ec2d08f", 
     "proc_id": 1, 
     "labels": { 
         "tenant_name": "dev-1-unified", 
         "rda_platform_version": "22.5.13.3", 
         "rda_messenger_version": "22.5.15.1", 
         "rda_pod_version": "22.5.17.1", 
         "rda_license_valid": "no", 
         "rda_license_not_expired": "no", 
         "rda_license_expiration_date": "" 
     }, 
     "build_tag": "daily", 
     "requests": { 
         "auto": "tenants.2dddab0e52544f4eb2de067057aaac31.worker.group.3571581d876b.auto", 
         "direct": "tenants.2dddab0e52544f4eb2de067057aaac31.worker.group.3571581d876b.direct.ae875728" 
     }, 
     "resources": { 
         "cpu_count": 8, 
         "cpu_load1": 2.24, 
         "cpu_load5": 2.43, 
         "cpu_load15": 2.52, 
         "mem_total_gb": 25.3, 
         "mem_available_gb": 9.7, 
         "mem_percent": 61.7, 
         "mem_used_gb": 15.01, 
         "mem_free_gb": 2.93, 
         "mem_active_gb": 11.49, 
         "mem_inactive_gb": 7.64, 
         "pod_usage_active_jobs": 15, 
         "pod_usage_total_jobs": 578 
     }, 
     "pod_leader": false, 
     "objstore_info": { 
         "host": "10.10.10.100:9000", 
         "config_checksum": "8936434b" 
     }, 
     "group": "cfx-lab-122-178", 
     "group_id": "3571581d876b", 
     "site_name": "cfx-lab-122-178", 
     "site_id": "3571581d876b", 
     "public_access": false, 
     "capacity_filter": "cpu_load1 <= 7.0 and mem_percent < 98 and pod_usage_active_jobs < 20", 
     "_local_time": 1653012991.0593688 
 }

```

#### Listing RDA Platform Microservices with Versions
```
 python3 rdac.py pods --versions

```

![Portal](https://bot-docs.cloudfabrix.io/images/guide/rdac_pod_versions.png)

#### Performing a Health Check on RDA Microservices

Following command performs a health check on all microservices and returns status of each health parameter.
```
 python3 rdac.py healthcheck

```

![Portal](https://bot-docs.cloudfabrix.io/images/guide/rdac_healthcheck.png)

#### Listing all Running Pipeline Jobs

Following command lists all active jobs created using Portal, CLI, Scheduler or via Service Blueprints.
```
 python3 rdac.py jobs

```

![Portal](https://bot-docs.cloudfabrix.io/images/guide/rdac_jobs.png)

#### Evicting a Job

Following command can be used to evict a specific Job from RDA Worker. If the job was created by Scheduler or by a Service Blueprint, a new job may be re-created immediately after the job has been evicted.
```
 python3 rdac.py evict --jobid c38025837c284562957f78ab385a0caf

```

This script attempts to evict the job with ID `c38025837c284562957f78ab385a0caf`

#### Observing Pipeline Execution Traces from CLI

Following command can be used watch (observe) all traces from all workers and all the pipelines that are getting executed anywhere in the RDA Fabric.
```
 python3 rdac.py watch-traces

```

![Portal](https://bot-docs.cloudfabrix.io/images/guide/rdac_traces.png)

#### List all datasets currently saved in RDA Fabric
```
 python3 rdac.py dataset-list

```

#### Adding a new dataset to RDA Fabric

Datasets can be added if the data is available as a local file on your system where rdac.py is available or if the data is available via URL. Supported formats are `CSV`, `JSON`, `XLS`, `Parquet`, `ORC` and many compresses formats for `CSV`.

To add a local file as a dataset:
```
 python3 rdac.py dataset-add --name my-dataset --file ./mydata.csv

```

**Note:** rdac.py mounts current directory as /home inside the docker container. You may also place the data in your home directory folder `$HOME/rdac_data/` and access it as `--file /data/mydata.csv`

You may also add a dataset if the data is accessible via http or https URL.


```
python3 rdac.py dataset-add \               --name 'sample-ecommerce-data' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/sample-ecommerce-data.csv'
```

## 3\. List of All RDA CLI Sub Commands

| Sub Command | Description |
| --- | --- |
| [agent-bots](#agent-bots) | List all bots registered by agents for the current tenant |
| [agents](#agents) | List all agents for the current tenant |
| [alert-rules](#alert-rules) | Alert Rule management commands |
| [bots-by-source](#bots-by-source) | List bots available for given sources |
| [check-credentials](#check-credentials) | Perform credential check for one or more sources on a worker pod |
| [checksum](#checksum) | Compute checksums for pipeline contents locally for a given JSON file |
| [content-to-object](#content-to-object) | Convert data from a column into objects |
| [copy-to-objstore](#copy-to-objstore) | Deploy files specified in a ZIP file to the Object Store |
| [dashboard](#dashboard) | User defined dashboard management commands |
| [dataset](#dataset) | Dataset management commands |
| [demo](#demo) | Demo related commands |
| [deployment](#deployment) | Service Blueprints (Deployments) management commands |
| [event-gw-status](#event-gw-status) | List status of all ingestion endpoints at all the event gateways |
| [evict](#evict) | Evict a job from a worker pod |
| [file-ops](#file-ops) | Perform various operations on local files |
| [file-to-object](#file-to-object) | Convert files from a column into objects |
| [fmt-template](#fmt-template) | Formatting Templates management commands |
| [healthcheck](#healthcheck) | Perform healthcheck on each of the Pods |
| [invoke-agent-bot](#invoke-agent-bot) | Invoke a bot published by an agent |
| [jobs](#jobs) | List all jobs for the current tenant |
| [logarchive](#logarchive) | Logarchive management commands |
| [merge-logarchive-files](#merge-logarchive-files) | Merge multiple locally downloaded Log Archive (.gz) filles into a single CSV/Parquet file |
| [object](#object) | RDA Object management commands |
| [output](#output) | Get the output of a Job using jobid. |
| [pipeline](#pipeline) | Pipeline management commands |
| [pods](#pods) | List all pods for the current tenant |
| [pod-logging](#pod-logging) | Commands to set and get logging configuration of pods |
| [pod-logging-handler-set](#pod-logging-handler-set) | To change log levels for any required pod |
| [project](#project) | Project management commands. Projects can be used to link different tenants / projects from this RDA Fabric or a remote RDA Fabric |
| [pstream](#pstream) | Add a new Persistent stream |
| [purge-outputs](#purge-outputs) | Purge outputs of completed jobs |
| [read-stream](#read-stream) | Read messages from an RDA stream |
| [run](#run) | Run a pipeline on a worker pod |
| [run-get-output](#run-get-output) | Run a pipeline on a worker, wait for the completion, get the final output |
| [schedule-add](#schedule-add) | Add a new schedule for pipeline execution |
| [schedule-delete](#schedule-delete) | Delete an existing schedule |
| [schedule-edit](#schedule-edit) | Edit an existing schedule |
| [schedule-info](#schedule-info) | Get details of a schedule |
| [schedule-list](#schedule-list) | List all schedules |
| [schedule-update-status](#schedule-update-status) | Update status of an existing schedule |
| [schema](#schema) | Dataset Model Schema management commands |
| [secret](#secret) | Credentials (Secrets) management commands |
| [set-pod-log-level](#set-pod-log-level) | Update the logging level for a given RDA Pod |
| [site-profile](#site-profile) | Site Profile management commands |
| [site-summary](#site-summary) | Show summary by Site and Overall |
| [stack](#stack) | Application Dependency Mapping (Stack) management commands |
| [staging-area](#staging-area) | Staging Area based data ingestion management commands |
| [subscription](#subscription) | Show current CloudFabrix RDA subscription details |
| [synthetics](#synthetics) | Data synthesizing management commands |
| [verify-pipeline](#verify-pipeline) | Verify the pipeline on a worker pod |
| [viz](#viz) | Visualize data from a file within the console (terminal) |
| [watch](#watch) | Commands to watch various streams such sas trace, logs and change notifications by microservices |
| [worker-obj-info](#worker-obj-info) | List all worker pods with their current Object Store configuration |
| [write-stream](#write-stream) | Write data to the specified stream |

### Sub Command: `agent-bots`

Description: List all bots registered by agents for the current tenant
```
 rdac agent-bots --help

```
```
 usage: rdac [-h] [--json] [--type AGENT_TYPE] [--group AGENT_GROUP] 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --json               Print detailed information in JSON format instead of 
                        tabular format 
   --type AGENT_TYPE    Show only the agents that match the specified agent 
                        type 
   --group AGENT_GROUP  Show only the agents that match the specified agent 
                        group

```

*   Following is the syntax for **agent-bots**
```
 rdac agent-bots --json --type rda-event-gateway --group event_gateway_site01

```

Example Output
```
 [ 
     { 
         "name": "get-status", 
         "description": "List all endpoints configured at this gateway and current status", 
         "query-type": "api-endpoint", 
         "mode": "source-any", 
         "model": {}, 
         "agent_type": "rda-event-gateway", 
         "site_name": "event_gateway_site01", 
         "pod_id": "250951da" 
     } 
 ]

```

### Sub Command: `agents`

Description: List all agents for the current tenant
```
 rdac agents --help

```
```
 Usage: agents  [-h] [--json] [--type AGENT_TYPE] [--group AGENT_GROUP] 
             [--site SITE_NAME] 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --json               Print detailed information in JSON format instead of 
                        tabular format 
   --type AGENT_TYPE    Show only the agents that match the specified agent 
                        type 
   --group AGENT_GROUP  Deprecated. Use --site. Show only the agents that match 
                        the specified site 
   --site SITE_NAME     Show only the agents that match the specified site

```

\* The Following is the syntax for **agents**
```
 rdac agents

```

Example Output
```
 +-------------------+----------------+----------+----------------------+-------------------+--------+--------------+ 
 | Agent-Type        | Host           | ID       | Site                 | Age               |   CPUs |   Memory(GB) | 
 |-------------------+----------------+----------+----------------------+-------------------+--------+--------------| 
 | rda-event-gateway | saaswrk72.qa.e | 250951da | event_gateway_site01 | 28 days, 21:54:20 |      4 |        31.33 | 
 | agent-ml          | 5339ca9ca765   | c4d7b94e | mlagent              | 23:04:10          |      4 |        31.33 | 
 | agent-irm         | aa932951e71e   | 0fbc78ec | irmagent             | 23:03:42          |      4 |        31.33 | 
 +-------------------+----------------+----------+----------------------+-------------------+--------+--------------+

```

### Sub Command: `alert-rules`

**Following are the valid Sub-Commands for the alert-rules**

| Sub Commands | Description |
| --- | --- |
| add | Add or update alert ruleset |
| get | Get YAML data for an alert ruleset |
| delete | Delete an alert ruleset |
| list | List all alert rulesets. |
```
 rdac alert-rules --help

```
```
 Following are valid sub-commands for alert-rules: 
   add                       Add or update alert ruleset 
   get                       Get YAML data for an alert ruleset 
   delete                    Delete an alert ruleset 
   list                      List all alert rulesets.

```

****Sub Command: `add`****

Description: Add or update alert ruleset
```
 Usage: alert-rules-add  [-h] --file INPUT_FILE [--overwrite] 
 
 optional arguments: 
   -h, --help         show this help message and exit 
   --file INPUT_FILE  YAML file containing alert ruleset definition 
   --overwrite        Overwrite even if a ruleset already exists with a name.

```

*   Following is the syntax for **alert-rules add**
```
 cat > alertrulestest1.yml << 'EOF' 
 name: alertruletest 
 description: syslog from filebeat 
 realtime-alerts: 
     -   name: filebeat_syslog_msgs 
         description: VPX Finish task msgs 
         groupBy: host_name 
         condition: severity = 'INFO' 
         severity: CRITICAL 
         suppress-for-minutes: 5 
 saved_time: '2022-02-19T22:34:10.888947' 
 EOF 
 
 rdac alert-rules add --file alertrulestest1.yml

```

Example output
```
 Added ruleset alertruletest with 1 realtime alert rules, 0 aggregate alert rules

```

****Sub Command: `delete`****

Description: Delete an alert ruleset
```
 Usage: alert-rules-delete  [-h] --name RULESET_NAME 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --name RULESET_NAME  Name of the alert ruleset to delete

```

*   Following is the syntax for **alert-rules delete**
```
 rdac alert-rules delete --name alertrulestest1

```

Example Output
```
 Deleted alert ruleset: alertruletest

```

****Sub Command: `get`****

Description: Get YAML data for an alert ruleset
```
 Usage: alert-rules-get  [-h] --name RULESET_NAME 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --name RULESET_NAME  Name of the alert ruleset to display

```

*   Following is the syntax for **alert-rules get**
```
 rdac alert-rules get --name ATest_ZRules

```

Example Output
```
 description: Alert_Rules 
 name: ATest_ZRules 
 aggregate-alerts: 
 - rule_a 
 - rule_b 
 realtime-alerts: 
 - rule_1 
 - rule_2 
 saved_time: '2022-12-20T05:16:41.716023'

```

****Sub Command: `list`****

Description: List all alert rulesets.
```
 Usage: alert-rules-list  [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```

*   Following is the syntax for **alert-rules list**
```
 rdac alert-rules list

```

Example Output
```
     name              description           saved_time                    num_realtime_alert_rules    num_aggr_alert_rules 
 --  ----------------  --------------------  --------------------------  --------------------------  ---------------------- 
  0  alertruletestnew  syslog from filebeat  2023-01-03T05:01:55.361186                           1                       0 
 
 Cleaning up socket for process: 1. Socket file: /tmp/rdf_log_socket_57602b71-8ea5-49c5-acbd-54c9908a0680 
 Exiting out of LogRecordSocketReceiver. pid: 1. Socket file: /tmp/rdf_log_socket_57602b71-8ea5-49c5-acbd-54c9908a0680
 ```

### Sub Command: `bot-package`

**Following are the valid Sub-Commands for the bot-package**

| Sub Commands | Description |
| --- | --- |
| add | Add or update Bot Package |
| get | Get meta data for a Bot Package |
| delete | Delete a Bot Package |
| list | List all Bot Packages |
| build | Build the specified bot package |
| ut  | Run Unit Tests |
| generate | Generate the specified bot package |
| list-runtimes | List available Bot Package runtime environments on each worker |
```
 rdac bot-package --help

```
```
 Following are valid sub-commands for bot-package: 
   add                       Add or update Bot Package 
   get                       Get meta data for a Bot Package 
   delete                    Delete a Bot Package 
   list                      List all Bot Packages 
   build                     Build the specified bot package 
   ut                        Run Unit Tests 
   generate                  Generate the specified bot package 
   list-runtimes             List available Bot Package runtime environments on each worker

```

****Sub Command: `list`****

Description: List all Bot Packages
```
 rdac bot-package list --help

```
```
 usage: bot-package [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```

*   Following is the syntax for **bot-package list**
```
 rdac bot-package list

```

Example Output
```
 Name                       Version    Description                              Has Dist    Publisher    Saved Time 
 -------------------------  ---------  ---------------------------------------  ----------  -----------  -------------------------- 
 botpkg_demo_proactivecase  22.11.9    ProctiveCase API for ServiceNow Tickets  Yes         CloudFabrix  2022-11-14T21:16:30.201550

```

****Sub Command: `get`****

Description: Get meta data for a Bot Package
```
 rdac bot-package get --help

```
```
 optional arguments: 
   -h, --help           show this help message and exit 
   --name PACKAGE_NAME  Name of the Bot Package

```

\* Following is the syntax for **bot-package get**
```
 rdac bot-package get --name botpkg_demo_proactivecase

```

Example Output
```
 extension: 
   namespace: demo 
   type: proactivecase 
   version: 22.11.9 
   description: ProctiveCase API for ServiceNow Tickets 
   default_name: proactivecase 
   publisher: CloudFabrix 
   support_email: mohammed.rahman@cloudfabrix.com 
   config_template: 
     hostname: null 
     port: 443 
     uri_suffix: internal/proactiveCaseAPI/v1.1 
     client_id: null 
     secret: null 
     $secure: 
     - secret 
     $mandatory: 
     - hostname 
     - client_id 
     - secret 
     $labels: 
       hostname: Host 
       port: Port 
       client_id: Client ID 
       secret: Secret Value 
   implementation: 
     code: proactivecase.ProactiveCase 
 bots: 
 - name: get-ticket 
   description: Get ServiceNow Ticket 
   bot_type: source 
   model_type: api 
   model_parameters: 
   - name: ticket_id 
     description: comma separated ticket IDs 
     type: text 
     mandatory: true 
   - name: source 
     description: Source 
     type: text 
     mandatory: true

```

****Sub Command: `generate`****

Description: Generate the specified bot package
```
 rdac bot-package generate --help

```
```
 usage: bot-package [-h] --namespace NAMESPACE --name NAME [--version VERSION] 
                    [--bots NUM_OF_BOTS] --output_dir OUTPUT_DIR 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --namespace NAMESPACE 
                         Namespace for Bot extension 
   --name NAME           Name of the bot extension package 
   --version VERSION     Version for Bot extension 
   --bots NUM_OF_BOTS    Number of Bots to be added to the package 
   --output_dir OUTPUT_DIR 
                         Output directory for creating bot package

```

*   Following is the syntax for **bot-package generate**
```
 rdac bot-package generate --namespace demo --name proactivecasenew --version 23.01.03 --bot 2 --output_dir new11

```

Example Output
```
 Configure : Custom Bot 1 
 
 Name*: get-ticket 
 Bot Type*: source 
 Number of bot input parameters*: 2 
 
 Configure : Bot input parameter 1 
 
 Name*: ticket_id 
 Type: text 
 Is mandatory[yes/no]*: yes 
 
 Configure : Bot input parameter 2 
 
 Name*: source 
 Type: text 
 Is mandatory[yes/no]*: yes 
 
 Configure : Custom Bot 2 
 
 Name*: get-ticket1 
 Bot Type*: source 
 Number of bot input parameters*: 1 
 
 Configure : Bot input parameter 2 1 
 
 Name*: ticket_id1 
 Type: text 
 Is mandatory[yes/no]*: yes 
 Generated: new11/bots.yml

```

****Sub Command: `list-runtimes`****

Description: List available Bot Package runtime environments on each worker
```
 bot-package list-runtimes --help

```
```
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```

*   Following is the syntax for **bot-package list-runtimes**
```
 rdac bot-package list-runtimes

```

Example Output
```
 2022-12-22:09:44:17 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 +--------------+----------+-------------+-------------+-------------+--------------+----------+ 
 | Host         | Pod ID   | Site        | Python3.7   | Python3.9   | Python3.10   | Java11   | 
 |--------------+----------+-------------+-------------+-------------+--------------+----------| 
 | 05969789d903 | b6bb8486 | rda-site-01 | yes         |             |              |          | 
 +--------------+----------+-------------+-------------+-------------+--------------+----------+

```

### Sub Command: `bots-by-source`

Description: List bots available for given sources
```
 rdac bots-by-source --help

```
```
 Usage: bots-by-source  [-h] [--sources SOURCES] [--group WORKER_GROUP] 
             [--site WORKER_SITE] [--lfilter LABEL_FILTER] 
             [--rfilter RESOURCE_FILTER] [--maxwait MAX_WAIT] [--json] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --sources SOURCES     Comma separated list of sources to find bots (in 
                         addition to built-in sources) 
   --group WORKER_GROUP  Deprecated. Use --site option. Specify a worker site 
                         name. If not specified, will use any available worker. 
   --site WORKER_SITE    Specify a worker site name. If not specified, will use 
                         any available worker. 
   --lfilter LABEL_FILTER 
                         CFXQL style query to narrow down workers using their 
                         labels 
   --rfilter RESOURCE_FILTER 
                         CFXQL style query to narrow down workers using their 
                         resources 
   --maxwait MAX_WAIT    Maximum wait time (seconds) for credential check to 
                         complete. 
   --json                Print detailed information in JSON format instead of 
                         tabular format

```

*   Following is the syntax for **bots-by-source**
```
  rdac bots-by-source --group rda-site-01 --maxwait 10
 ```

Example Output
```
 { 
   "status": "started", 
   "reason": "", 
   "results": [], 
   "now": "2023-01-03T06:20:38.129086", 
   "status-subject": "tenants.545590daa4ba44a3b32cb3b33f69df13.worker.group.f4a56ba6388c.direct.2d30eab7", 
   "jobid": "b244f76f663a4033964301e7c3916ddc" 
 } 
 Completed: 
 Bot                                     Type                  Description                                                                                                                                                                                                                                                                Source 
 --------------------------------------  --------------------  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  -------- 
 @c:new-block                            api-endpoint          Start a new block within the pipeline                                                                                                                                                                                                                                      c 
 @c:simple-loop                          api-endpoint          Start a simple looping block using 'loop_var' as list of values                                                                                                                                                                                                            c 
 @c:data-loop                            api-endpoint          Start a looping block using 'dataset' name of the saved dataset, and unique values from 'columns'                                                                                                                                                                          c 
 @c:count-loop                           api-endpoint          Start a looping block that counts from 'start' to 'end' with 'increment' numerical values                                                                                                                                                                                  c 
 @c:timed-loop                           api-endpoint          Start a looping block that waits 'interval' seconds between each iteration

```                               

### Sub Command: `check-credentials`

Description: Perform credential check for one or more sources on a worker pod
```
 Usage: check-credentials  [-h] --config CONFIG [--group WORKER_GROUP] [--site WORKER_SITE] 
             [--maxwait MAX_WAIT] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --config CONFIG       File containing pipeline contents or configuration 
   --group WORKER_GROUP  Deprecated. Use --site. Specify a worker site name. If 
                         not specified, will use any available worker. 
   --site WORKER_SITE    Specify a worker Site name. If not specified, will use 
                         any available worker. 
   --maxwait MAX_WAIT    Maximum wait time (seconds) for credential check to 
                         complete.

```

*   Following is the syntax for **check-credentials**
```
 rdac check-credentials --config aws.json --group cfx-lab --maxwait 30

```

Example Output
```
 Initiating Credential check 
 { 
   "status": "started", 
   "reason": "", 
   "results": [], 
   "now": "2021-07-28T02:12:46.577687", 
   "status-subject": "tenants.2dddab0e52544f4eb2de067057aaac31.worker.group.c640b839efec.direct.255941bb", 
   "jobid": "328ea2d5f0454ed29b64ccdb287c5626" 
 } 
 { 
   "jobid": "328ea2d5f0454ed29b64ccdb287c5626", 
   "status-subject": "tenants.2dddab0e52544f4eb2de067057aaac31.worker.group.c640b839efec.direct.255941bb" 
 } 
 Running:  
 Running:  
 Running:  
 Completed:  
 +---------------+---------------+----------+----------+-----------------+ 
 | Source Name   | Source Type   | Status   | Reason   |   Duration (ms) | 
 |---------------+---------------+----------+----------+-----------------| 
 | aws-dev       | aws           | OK       |          |         1473.79 | 
 | aws-prod      | aws           | OK       |          |         1404.15 | 
 +---------------+---------------+----------+----------+-----------------+

```

### Sub Command: `checksum`

Description: Compute checksums for pipeline contents locally for a given JSON file
```
 Usage: checksum  [-h] --pipeline PIPELINE 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --pipeline PIPELINE  File containing pipeline information in JSON format

```

### Sub Command: `content-to-object`

Description: Convert data from a column into objects
```
 Usage: content-to-object  [-h] --inpcol INPUT_CONTENT_COLUMN --outcol OUTPUT_COLUMN --file 
             INPUT_FILE --outfolder OUTPUT_FOLDER --outfile OUTPUT_FILE 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --inpcol INPUT_CONTENT_COLUMN 
                         Name of the column in input that contains the data 
   --outcol OUTPUT_COLUMN 
                         Column name where object names will be inserted 
   --file INPUT_FILE     Input csv filename 
   --outfolder OUTPUT_FOLDER 
                         Folder name where objects will be stored 
   --outfile OUTPUT_FILE 
                         Name of output csv file that has object location 
                         stored

```

### Sub Command: `copy-to-objstore`

Description: Deploy files specified in a ZIP file to the Object Store
```
 Usage: copy-to-objstore  [-h] --file ZIP_FILENAME [--verify] [--force] 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --file ZIP_FILENAME  ZIP filename (or URL) containing bucket/object entries. 
                        If bucket name is 'default', this tool will use the 
                        target bucket as specified in configuration. 
   --verify             Do not upload files, only verify if the objects in the 
                        ZIP file exists on the target object store 
   --force              Upload the files even if they exist on the target 
                        system with same size

```

### Sub Command: `dashboard`

**Following are the valid Sub-Commands for the dashboard**

| Sub Commands | Description |
| --- | --- |
| add | Add or update dashboard |
| get | Get YAML data for a dashboard |
| list | List all dashboards |
| convert | Convert all dashboards from YAML to JSON |
| delete | Delete a dashboard |
| enable | Change the status of a dashboard to 'enabled' |
| disable | Change the status of a dashboard to 'disabled' |
| verify | Verify the dashboard and any pages inside it for PStreams and columns |
| to-app | Convert a tabbed or sectioned dashboard into multi-paged app |
| live-edit | Supports live edit of dashboards using local editor |
```
 rdac dashboard --help

```
```
 Following are valid sub-commands for dashboard: 
   add                       Add or update dashboard 
   get                       Get YAML data for a dashboard 
   list                      List all dashboards 
   convert                   Convert all dashboards from YAML to JSON 
   delete                    Delete a dashboard 
   enable                    Change the status of a dashboard to 'enabled' 
   disable                   Change the status of a dashboard to 'disabled' 
   verify                    Verify the dashboard and any pages inside it for PStreams and columns 
   to-app                    Convert a tabbed or sectioned dashboard into multi-paged app 
   live-edit                 Supports live edit of dashboards using local editor

```

****Sub Command: `add`****

Description: Add or update dashboard
```
 rdac dashboard add --help

```
```
 optional arguments: 
   -h, --help         show this help message and exit 
   --file INPUT_FILE  YAML file containing dashboard definition 
   --overwrite        Overwrite even if a dashboard already exists with the 
                      specified name.

```

Note

Before running the add cmd ,create a yaml file containing dashboard definition

*   Following is the syntax for **dashboard add**
```
 rdac dashboard add --file dashboard.yml

```

Example Output
```
 2023-01-04:10:24:09 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-04:10:24:09 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-04:10:24:09 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Added dashboard Appdynamics cpu metrics analysis-shaded chartnew

```

****Sub Command: `get`****

Description: Get YAML data for a dashboard
```
 rdac dashboard get --help

```
```
 usage: dashboard [-h] --name DASHBOARD_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name DASHBOARD_NAME 
                         Name of the dashboard

```

*   Following is the syntax for **dashboard get**
```
 rdac dashboard get --name "Appdynamics cpu metrics analysis-shaded chart"

```

Example Output
```
 label: Appdynamics CPU metrics 
 description: Shaded chart for Appdynamics metrics 
 enabled: true 
 dashboard_style: tabbed 
 dashboard_filters: 
   time_filter: true 
   columns_filter: [] 
   group_filters: [] 
 debug: true 
 dashboard_sections: 
 - title: Appdynamics_cpu_metrics 
   show_filter: true 
   widgets: 
   - widget_type: shaded_chart 
     title: Appdynamics-cpumetrics 
     stream: Appdynamics_cpu_metrics 
     ts_column: timestamp 
     baseline_column: baseline 
     anomalies_column: anomalies 
     predicted_column: predicted 
     upperBound_column: upperBound 
     lowerBound_column: lowerBound 
     duration_hours: 5000 
     synchronized-group: 0 
     markers-def: 
     - message: Now 
       color: '#E53935' 
       timestamp: 1647814186 
     - message: Tomorrow 
       color: '#E53935' 
       timestamp: 1648937386 
     - message: Current 
       color: '#E53935' 
       timestamp: 1658355595 
     show-markers: true 
     downsample: true 
     downsample-to-percent: 10 
     downsample-limit-rows: 500 
     widget_id: b0d45ad1 
 saved_time: '2022-12-14T06:07:11.835323'

```

****Sub Command: `list`****

Description: List all dashboards
```
 rdac dashboard list --help

```
```
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```

*   Following is the syntax for **dashboard list**
```
 rdac dashboard list

```

Example Output
```
     name                                                  dashboard_type    label                                                      description                                                                                                                                enabled    saved_time 
 ---  ----------------------------------------------------  ----------------  ---------------------------------------------------------  -----------------------------------------------------------------------------------------------------------------------------------------  ---------  -------------------------- 
   0  rda-mgmt-page-alert-rules                             dashboard         Alert Rules                                                Alert Rules Page                                                                                                                           True       2022-10-06T13:43:06.707246 
   1  rda-mgmt-page-credentials                             dashboard         Credentials                                                Credentials Management Page                                                                                                                True       2022-10-06T13:43:07.346093 
   2  Test_IFRAME                                           dashboard         IFRAME Test                                                ACME Platform Sanity Dash                                                                                                                  False      2022-10-06T13:43:07.367278 
   3  olb-observability-data_page_Incidents                 dashboard         OLB L2/L3 Dashboard, Page: Incidents                       Online Banking App Observability Data for L2/L3 Users, Page: Incidents                                                                     False      2022-11-18T09:24:50.445315 
   4  olb-experience-desk_page_KPIs                         template          Experience Desk Dashboard, Page: KPIs                      Equipped with Events, Alerts and Incidents Information to Maximize Customer Experience and Satisfaction, Page: KPIs                        False      2022-10-06T13:43:07.443675 
   5  ACME_Test_Preview_App                                 template          Test Case Preview                                          Dashboard to preview commits and logs for a test case                                                                                      False      2022-10-06T13:43:07.509264 
   6  l1-service-health                                     template          Service Health - L1 Users                                  L1 Service Health                                                                                                                          False      2022-12-21T05:19:02.332379 
   7  rda-integrations-app                                  app               RDA Integrations                                           Robotic Data Automation Integrations                                                                                                       True       2022-10-06T13:43:07.622712 
   8  l2-l3-dashboard                                       app               L2/L3 Dashboard                                            Dashboard L2/L3 Users                                                                                                                      True       2022-12-21T05:19:02.396260 
   9  rda-dashboard-errors                                  dashboard         Dashboard Errors                                           Query errors in RDA Dashboard widgets                                                                                                      True       2022-10-07T01:49:51.552796 
  10  Appdynamics cpu metrics analysis-shaded chart         dashboard         Appdynamics CPU metrics                                    Shaded chart for Appdynamics metrics                                                                                                       True       2022-12-14T06:07:11.835323
 ```

****Sub Command: `convert`****

Description : Convert all dashboards from YAML to JSON
```
 rdac dashboard convert --help

```
```
 optional arguments: 
   -h, --help  show this help message and exit

```

*   Following is the syntax for **dashboard convert**
```
 rdac dashboard convert

```

Example Output
```
 Migrating to JSON: rda-mgmt-page-alert-rules 
 2023-01-04:05:30:41 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-04:05:30:41 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-04:05:30:41 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Migrating to JSON: rda-mgmt-page-credentials 
 Migrating to JSON: Test_IFRAME 
 Migrating to JSON: olb-observability-data_page_Incidents 
 Migrating to JSON: olb-experience-desk_page_KPIs 
 Migrating to JSON: ACME_Test_Preview_App 
 Migrating to JSON: l1-service-health 
 Migrating to JSON: rda-integrations-app 
 Migrating to JSON: l2-l3-dashboard 
 Migrating to JSON: rda-dashboard-errors 
 Migrating to JSON: Appdynamics cpu metrics analysis-shaded chart 
 Migrating to JSON: metric_anomalies_template 
 Migrating to JSON: olb-engineering-dashboard_page_Metrics 
 Migrating to JSON: olb-observability-data_page_Metrics__with_Anomalies 
 Migrating to JSON: olb-observability-data_page_Metric Analysis

```

****Sub Command: `delete`****

Description: Delete a dashboard
```
 rdac dashboard delete --help

```
```
 usage: dashboard [-h] --name DASHBOARD_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name DASHBOARD_NAME 
                         Name of the dashboard to delete

```

*   Following is the syntax for **dashboard delete**
```
 rdac dashboard delete --name 'Appdynamics cpu metrics analysis-shaded chart 2'

```

Example Output
```
 2023-01-04:09:34:58 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-04:09:34:58 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-04:09:34:58 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Deleted dashboard: Appdynamics cpu metrics analysis-shaded chart 2

```

****Sub Command: `enable`****

Description: Change the status of a dashboard to 'enabled'
```
 rdac dashboard enable --help

```
```
 usage: dashboard [-h] --name DASHBOARD_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name DASHBOARD_NAME 
                         Name of the dashboard

```

*   Following is the syntax for **dashboard enable**
```
 rdac dashboard enable --name 'Appdynamics cpu metrics analysis-shaded chart'

```

Example Output
```
 2023-01-04:05:45:46 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-04:05:45:46 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-04:05:45:46 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Changed status of Appdynamics cpu metrics analysis-shaded chart to enabled

```

****Sub Command: `disable`****

Description: Change the status of a dashboard to 'disabled'
```
 rdac dashboard disable --help

```
```
 usage: dashboard [-h] --name DASHBOARD_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name DASHBOARD_NAME 
                         Name of the dashboard

```

*   Following is the syntax for **dashboard disable**
```
 rdac dashboard disable 'Appdynamics cpu metrics analysis-shaded chart'

```

Example Output
```
 2023-01-04:05:44:47 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-04:05:44:47 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-04:05:44:47 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Changed status of Appdynamics cpu metrics analysis-shaded chart to disabled

```

****Sub Command: `verify`****

Description: Verify the dashboard and any pages inside it for PStreams and columns
```
 rdac dashboard verify --help

```
```
 usage: dashboard [-h] --name DASHBOARD_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name DASHBOARD_NAME 
                         Name of the dashboard to verify

```

*   Following is the syntax for **dashboard verify**
```
 rdac dashboard verify --name 'Appdynamics cpu metrics analysis-shaded chart'

```

Example Output
```
 2023-01-04:06:28:41 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 [ 
   { 
     "dashboard": "Appdynamics cpu metrics analysis-shaded chart", 
     "type": "widget", 
     "widget_type": "shaded_chart", 
     "title": "Appdynamics-cpumetrics", 
     "stream": "Appdynamics_cpu_metrics", 
     "columns": "timestamp", 
     "stream_status": "found", 
     "missing_columns": "" 
   } 
 ]

```

****Sub Command: `to-app`****

Description: Convert a tabbed or sectioned dashboard into multi-paged app
```
 rdac dashboard to-app --help

```
```
 usage: dashboard [-h] --name DASHBOARD_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name DASHBOARD_NAME 
                         Name of the dashboard

```

*   Following is the syntax for **dashboard to-app**
```
 rdac dashboard to-app --name rda-microservice-traces

```

Example Output
```
 Adding new internal dashboard: rda-microservice-traces_page_Traces 
 2023-01-04:06:37:48 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-04:06:37:48 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-04:06:37:48 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Adding new internal dashboard: rda-microservice-traces_page_Healthchecks 
 Updating dashboard {dashboard_name} as app... 
 rdauser@manojp-rda-platform:~$

```

### Sub Command: `dashgroup`

**Following are the valid Sub-Commands for the dashgroup**

| Sub Commands | Description |
| --- | --- |
| add | Add or update dashboard group |
| get | Get JSON data for a dashboard group |
| list | List all dashboard groups |
| delete | Delete a dashboard group |
| enable | Change the status of a dashboard group to 'enabled' |
| disable | Change the status of a dashboard group to 'disabled' |
```
 rdac dashgroup --help

```
```
 Following are valid sub-commands for dashgroup: 
   add                       Add or update dashboard group 
   get                       Get JSON data for a dashboard group 
   list                      List all dashboard groups 
   delete                    Delete a dashboard group 
   enable                    Change the status of a dashboard group to 'enabled' 
   disable                   Change the status of a dashboard group to 'disabled'

```

****Sub Command: `add`****

Description: Add or update dashboard group
```
 rdac dashgroup add --help

```
```
 usage: dashgroup [-h] --file INPUT_FILE [--overwrite] 
 
 optional arguments: 
   -h, --help         show this help message and exit 
   --file INPUT_FILE  JSON file containing dashboard group definition 
   --overwrite        Overwrite even if a dashboard group already exists with 
                      the specified name.

```

Note

Before running the add cmd ,create a JSON file containing dashboard group definition

*   Following is the syntax for **dashgroup add**
```
  rdac dashgroup add --file  dashgroup.json
 ```

Example Output
```
 2023-01-04:11:13:12 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-04:11:13:12 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-04:11:13:12 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Added dashboard group l1-user new

```

****Sub Command: `get`****

Description: Get JSON data for a dashboard group
```
 rdac dashgroup get --help

```
```
 optional arguments: 
   -h, --help            show this help message and exit 
   --name DASHBOARD_GROUP_NAME 
                         Name of the dashboard group

```

*   Following is the syntax for **dashgroup get**
```
  rdac dashgroup get --name l1-users
 ```

Example Output
```
 { 
     "name": "l1-users", 
     "label": "L1 Users", 
     "dashboardList": [ 
         { 
             "id": "user-dashboard-incident-topology", 
             "name": "incident-topology" 
         }, 
         { 
             "id": "user-dashboard-incident-metrics", 
             "name": "incident-metrics" 
         }, 
         { 
             "id": "user-dashboard-incident-collaboration", 
             "name": "incident-collaboration" 
         }, 
         { 
             "id": "user-dashboard-l1-main-app", 
             "name": "l1-main-app" 
         } 
     ], 
     "users": "l1-user@cfx.com", 
     "enabled": true, 
     "description": "Dashboards for L1 Users", 
     "saved_time": "2022-09-28T05:56:11.325672" 
 }

```

****Sub Command: `list`****

Description: List all dashboard groups
```
 rdac dashgroup list --help

```
```
 usage: dashgroup [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```

*   Following is the syntax for **dashgroup list**
```
 rdac dashgroup list

```

Example Output
```
     name                     label                description                               enabled    saved_time 
 --  -----------------------  -------------------  ----------------------------------------  ---------  -------------------------- 
  0  Test                     Admin Group                                                    True       2022-12-21T16:59:47.419691 
  1  l1-users                 L1 Users             Dashboards for L1 Users                   True       2022-09-28T05:56:11.325672 
  2  executives               Executives           Dashboards for Executives                 True       2022-09-29T03:00:33.425663 
  3  Experience Desk          Experience Desk      Dashboards for Experience Desk            True       2022-09-28T05:56:05.969015 
  4  DevOps                   Users                                                          True       2022-09-28T19:21:38.852671 
  5  TestGroup                TestGroup                                                      True       2022-09-28T03:59:14.609687 
  6  Reression Training Test  Admin Group                                                    False      2022-09-28T05:56:07.802828 
  7  Partner                  Admin                All Partner Dashboards                    True       2022-09-28T05:56:06.961122 
  8  Acme                     Acme                                                           True       2022-10-23T22:03:29.461241 
  9  bizops                   Business Operations  Dashboards for Business Operations Users  True       2022-09-29T03:11:06.780365 
 10  l2-users                 L2 Users             Dashboards for L2 Users                   True       2022-09-28T05:56:12.239130 
 11  l1-l3 Dashboard          l1-l3 Dashboard                                                True       2022-12-21T05:28:23.966417 
 12  Biz Command Center       Biz Command Center   Dashboards for Biz Command Center         True       2022-09-28T05:56:03.338590 
 13  Engineering              Engineering Group    Dashboards for Engineering Group          True       2022-09-28T05:56:05.072187
 ```

****Sub Command: `delete`****

Description: Delete a dashboard group
```
 rdac dashgroup delete --help

```
```
 usage: dashgroup [-h] --name DASHBOARD_GROUP_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name DASHBOARD_GROUP_NAME 
                         Name of the dashboard group to delete

```

*   Following is the syntax for **dashgroup delete**
```
  rdac dashgroup delete --name 'synthetics-control'
 ```

Example Output
```
 2023-01-04:12:02:37 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-04:12:02:37 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-04:12:02:37 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Deleted dashboard group: synthetics-control

```

****Sub Command: `enable`****

Description: Change the status of a dashboard group to 'enabled'
```
 rdac dashgroup enable --help

```
```
 usage: dashgroup [-h] --name DASHBOARD_GROUP_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name DASHBOARD_GROUP_NAME 
                         Name of the dashboard group

```

*   Following is the syntax for **dashgroup enable**
```
 rdac dashgroup enable --name l1-users

```

Example Output
```
 2023-01-04:10:54:08 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-04:10:54:08 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-04:10:54:08 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Changed status of l1-users to enabled

```

****Sub Command: `disable`****

Description: Change the status of a dashboard group to 'disabled'
```
 rdac dashgroup disable --help

```
```
 usage: dashgroup [-h] --name DASHBOARD_GROUP_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name DASHBOARD_GROUP_NAME 
                         Name of the dashboard group

```

*   Following is the syntax for **dashgroup disable**
```
 rdac dashgroup disable --name l1-users

```

Example Output
```
 2023-01-04:10:53:16 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-04:10:53:16 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-04:10:53:16 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Changed status of l1-users to disabled

```

### Sub Command: `dataset`

**Following are the valid Sub-Commands for the dataset**

| Sub Commands | Description |
| --- | --- |
| list | List datasets from the object store |
| get | Download a dataset from the object store |
| meta | Download metadata for a dataset from the object store |
| add | Add a new dataset to the object store |
| delete | Delete a dataset from the object store |
| bounded-list | List bounded datasets from the object store |
| bounded-get | Download a bounded dataset from the object store |
| bounded-meta | Download metadata for a bounded dataset from the object store |
| bounded-add | Add a new bounded dataset to the system |
| bounded-import | Import the data for a bounded dataset and store it in the object store |
| bounded-delete | Delete a bounded dataset from the object store |
```
 rdac dataset --help

```
```
 Dataset management commands 
 
 Following are valid sub-commands for dataset: 
   list                      List datasets from the object store 
   get                       Download a dataset from the object store 
   meta                      Download metadata for a dataset from the object store 
   add                       Add a new dataset to the object store 
   delete                    Delete a dataset from the object store 
   bounded-list              List bounded datasets from the object store 
   bounded-get               Download a bounded dataset from the object store 
   bounded-meta              Download metadata for a bounded dataset from the object store 
   bounded-add               Add a new bounded dataset to the system 
   bounded-import            Import the data for a bounded dataset and store it in the object store 
   bounded-delete            Delete a bounded dataset from the object store

```

****Sub Command: `list`****

Description: List datasets from the object store
```
 rdac dataset list --help

```
```
 usage: dataset [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```

*   Following is the syntax for **dataset list**
```
 rdac dataset list

```

Example Output
```
      name                                                    format      mem_size_mb    num_rows    num_columns  saved_time 
 ---  ------------------------------------------------------  --------  -------------  ----------  -------------  -------------------------- 
   0  Appdynamics_cpu_metrics                                 csv               0.092        1000             12  2022-12-14T05:48:07.940815 
   1  Appdynamics_cpu_metrics_new                             csv               0.092        1000             12  2023-01-04T12:00:17.628034 
   2  Balancing_Control_to_Platform_Standardizer              csv               0               1              3  2022-10-19T00:32:51.328289 
   3  DATASET-SERVICEWOW                                      csv               0.015        2000              1  2022-10-13T14:35:08.843641 
   4  Data_Masking_to_hive_load                               csv               0               1              3  2022-10-19T00:32:51.657829 
   5  Data_Parsing_to_Balancing_Control                       csv               0               1              3  2022-10-19T00:32:51.213174 
   6  Feed_Data_Standardizer_to_Data_Masking                  csv               0               1              3  2022-10-19T00:32:51.550645 
   7  Metadata_Validator_to_Preprocessing                     csv               0               1              3  2022-10-19T00:32:50.999017 
   8  Online_Banking_Stack_Metrics                            csv               0.001           6             12  2022-09-29T04:01:45.875869 
   9  Platform_Standardizer_to_Feed_Data_Standardizer         csv               0               1              3  2022-10-19T00:32:51.433995 
  10  Preprocessing_to_Data_Parsing                           csv               0               1              3  2022-10-19T00:32:51.101942 
  11  SS-AWS-event-groups                                     csv               0               3              9  2022-11-08T14:39:47.207992
 ```

****Sub Command: `get`****

Description: Download a dataset from the object store
```
 rdac dataset get --help

```
```
 usage: dataset [-h] --name NAME [--tofile SAVE_TO_FILE] [--json] 
                [--format DATA_FORMAT] [--viz] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Dataset name 
   --tofile SAVE_TO_FILE 
                         Save the data to the specified file (CSV or JSON if 
                         --json is specified) 
   --json                Export data as a JSON formatted rows. ** Deprecated. 
                         Use --format ** 
   --format DATA_FORMAT  Save the downloaded data in the specified format. 
                         Valid values are csv, json, parquet. If format is 
                         'auto', format is determined from extension 
   --viz                 Open Dataframe visualizer to show the data

```

*   Following is the syntax for **dataset get**
```
 rdac dataset get --name Online_Banking_Stack_Metrics --viz

```

Example Output
```
 Downloaded dataset. Number of Rows: 6, Columns: 12 
 [DFViz:1] Rows 6, Cols 12 | View Rows 0-6, Cols: 0-4 | Press 'q' to exit, '?' for help 
           Data Filter:  | Col Filter:  | Data Sort:  | cfxql: 
 +----+-------------+----------+-----------------------+-----------------------------+--------------------------+ 
 |    | component   | count_   | layer                 | metric_name                 | node_id                  | 
 |----+-------------+----------+-----------------------+-----------------------------+--------------------------| 
 |  0 |             |          | Application Component | db_slow_queries             | 10.95.134.103_Database   | 
 |  1 |             |          | Application Component | total_response_time         | 10.95.134.101_Webserver  | 
 |  2 |             |          | Application Component | consumer_lag                | 10.95.134.104_MessageBus | 
 |  3 |             |          | Application Component | under_replicated_partitions | 10.95.134.104_MessageBus | 
 |  4 |             |          | Application Component | db_connections              | 10.95.134.103_Database   | 
 |  5 |             |          | Application Component | transaction_time            | 10.95.134.102_Appserver  | 
 +----+-------------+----------+-----------------------+-----------------------------+--------------------------+

```

****Sub Command: `meta`****

Description: Download metadata for a dataset from the object store
```
 rdac dataset meta --help

```
```
 usage: dataset [-h] --name NAME 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --name NAME  Dataset name

```

*   Following is the syntax for **dataset meta**
```
 rdac dataset meta --name Online_Banking_Stack_Metrics

```

Example Output
```
 { 
   "name": "Online_Banking_Stack_Metrics", 
   "format": "csv", 
   "datafile": "cfxdm-saved-data/Online_Banking_Stack_Metrics-data.csv", 
   "mem_size_mb": 0.001, 
   "num_rows": 6, 
   "num_columns": 12, 
   "saved_time": "2022-09-29T04:01:45.875869", 
   "dtypes": { 
     "component": "float64", 
     "count_": "float64", 
     "layer": "object", 
     "metric_name": "object", 
     "node_id": "object", 
     "node_label": "object", 
     "node_type": "object", 
     "source_tool": "object", 
     "stack_name": "object", 
     "timestamp": "object", 
     "unit": "object", 
     "value": "float64" 
   } 
 }

```

****Sub Command: `add`****

Description: Add a new dataset to the object store
```
 rdac dataset add --help

```
```
 usage: dataset [-h] [--folder FOLDER] --name NAME --file INPUT_FILE 
                [--local_format LOCAL_FORMAT] [--remote_format REMOTE_FORMAT] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --folder FOLDER       Dataset Folder 
   --name NAME           Dataset name 
   --file INPUT_FILE     CSV or parquet formatted file from which dataset will 
                         be added 
   --local_format LOCAL_FORMAT 
                         Local file format (auto or csv or parquet or json). 
                         'auto' means format will be determined from filename 
                         extension 
   --remote_format REMOTE_FORMAT 
                         Remote file format (csv or parquet).

```

*   Following is the syntax for **dataset add**
```
 rdac dataset add --name metricsdata --file metrics.csv --local_format auto

```

Example Output
```
 Loaded dataset from file. Number of Rows: 100000, Columns: 13 
 Dataset 'metricsdata' not found in the object storage. 
 2023-01-05:05:13:37 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-05:05:13:37 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-05:05:13:37 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 
 Added dataset 'metricsdata'

```

****Sub Command: `delete`****

Description: Delete a dataset from the object store
```
 rdac dataset delete --help

```
```
 usage: dataset [-h] --name NAME [--yes] 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --name NAME  Dataset name 
   --yes        Delete without prompting

```

*   Following is the syntax for **dataset delete**
```
 rdac dataset delete --name metricsdata

```

Example Output
```
 Confirm deletion of dataset (y/n)? y 
 2023-01-05:05:21:39 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-05:05:21:39 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-05:05:21:39 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem

```

****Sub Command: `bounded-list`****

Description: List bounded datasets from the object store
```
 rdac dataset bounded-list --help

```
```
 usage: dataset [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```

*   Following is the syntax for **dataset bounded-list**
```
 rdac dataset bounded-list

```

Example Output
```
    drafts      mem_size_mb  name         num_columns    num_rows  saved_time                  schema 
 --  --------  -------------  ---------  -------------  ----------  --------------------------  --------- 
  0  []                    0  Schema-QA              6           0  2023-01-05T04:39:16.255705  Schema-QA 
  1  []                    0  Test                   3           0  2023-01-05T04:39:24.660053  Test
 ```

****Sub Command: `bounded-get`****

Description: Download a bounded dataset from the object store
```
 rdac dataset bounded-get --help

```
```
 usage: dataset [-h] --name NAME [--tofile SAVE_TO_FILE] [--format DATA_FORMAT] 
                [--viz] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Dataset name 
   --tofile SAVE_TO_FILE 
                         Save the data to the specified file (CSV or JSON if 
                         --json is specified) 
   --format DATA_FORMAT  Save the downloaded data in the specified format. 
                         Valid values are csv, json, parquet. If format is 
                         'auto', format is determined from extension 
   --viz                 Open Dataframe visualizer to show the data

```

*   Following is the syntax for **dataset bounded-get**
```
 rdac dataset bounded-get --name Schema-QA --viz

```

Example Output
```
 Downloaded bounded dataset. Number of Rows: 0, Columns: 7 
 [DFViz:1] Rows 0, Cols 7 | View Rows 0-0, Cols: 0-4 | Press 'q' to exit, '?' for help 
           Data Filter:  | Col Filter:  | Data Sort:  | cfxql: 
 +--------+--------+--------+--------------+-------+ 
 | text   | enum   | bool   | enum_array   | int   | 
 |--------+--------+--------+--------------+-------| 
 +--------+--------+--------+--------------+-------+

```

****Sub Command: `bounded-meta`****

Description: Download metadata for a bounded dataset from the object store
```
 rdac dataset bounded-meta --help

```
```
 usage: dataset [-h] --name NAME 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --name NAME  Dataset name

```

\* Following is the syntax for **dataset bounded-meta**
```
 rdac dataset bounded-meta --name Schema-QA

```

Example Output
```
 { 
   "name": "Schema-QA", 
   "mem_size_mb": 0, 
   "num_rows": 0, 
   "drafts": [], 
   "saved_time": "2023-01-05T04:39:16.255705", 
   "schema": "Schema-QA", 
   "num_columns": 6 
 }

```

****Sub Command: `bounded-add`****

Description: Add a new bounded dataset to the system
```
 rdac dataset bounded-add --help

```
```
 usage: dataset [-h] --name NAME --schema SCHEMA_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Dataset name 
   --schema SCHEMA_NAME  Validate data against given schema. When schema is 
                         given, the dataset is added as 'schema bounded 
                         dataset'.

```

*   Following is the syntax for **dataset bounded-add**
```
 rdac dataset bounded-add --name 'Example Schema' --schema 'Example Schema'

```

Example Output
```
 2023-01-05:04:54:02 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-05:04:54:02 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-05:04:54:02 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Successfully added bounded dataset Example Schema

```

****Sub Command: `bounded-delete`****

Description: Delete a bounded dataset from the object store
```
 rdac dataset bounded-delete --help

```
```
 usage: dataset [-h] --name NAME [--yes] 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --name NAME  Dataset name 
   --yes        Delete without prompting

```

\* Following is the syntax for **dataset bounded-delete**
```
 rdac dataset bounded-delete --name 'Example Schema'

```
```
 Confirm deletion of dataset (y/n)? y 
 Successfully deleted all drafts of Example Schema 
 2023-01-05:04:55:43 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-05:04:55:43 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-05:04:55:43 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Successfully deleted bounded data set Example Schema

```

****Sub Command: `bounded-import`****

Description: Import the data for a bounded dataset and store it in the object store
```
 rdac dataset bounded-import --help

```
```
 usage: dataset [-h] --name NAME --file INPUT_FILE 
                [--local_format LOCAL_FORMAT] [--yes] [--json] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Dataset name 
   --file INPUT_FILE     CSV or parquet formatted file from which dataset will 
                         be added 
   --local_format LOCAL_FORMAT 
                         Local file format (auto or csv or parquet or json). 
                         'auto' means format will be determined from filename 
                         extension 
   --yes                 Delete without prompting 
   --json                Print detailed information in JSON format instead of 
                         tabular format

```

*   Following is the syntax for **dataset bounded-import**
```
 rdac dataset bounded-import --name Test --file metrics.csv

```

Example Output
```
 rdac dataset add --name metricsdata --file metrics.csv --local_format auto

```

### Sub Command: `demo`

**Following are the valid Sub-Commands for the demo**

| Sub Commands | Description |
| --- | --- |
| backup | Export dashboards and all related artifact meta data in to a folder |
| setup | Setup a target system for demo |
| diff | Compare two backup directories |
```
 rdac demo--help

```
```
 Demo related commands 
 
 Following are valid sub-commands for demo: 
   backup                    Export dashboards and all related artifact meta data in to a folder 
   setup                     Setup a target system for demo 
   diff                      Compare two backup directories

```

Example
```
 rdac demo backup --to_dir <foldername>

```
```
 tar -cvzf filename.tar.gz <foldername>/

```

Note

To create `demo.tar.gz` file from the output folder use the below mentioned commands
```
 cd demo

```
```
 tar -cvzf /tmp/demo.tar.gz .

```

****Sub Command: `backup`****

Description: Export dashboards and all related artifact meta data in to a folder
```
 rdac demo backup --help

```
```
 usage: demo [-h] --to_dir TO_DIR [--yaml] 
 
 optional arguments: 
   -h, --help       show this help message and exit 
   --to_dir TO_DIR  Output directory 
   --yaml           Export in YAML format (default is JSON)

```

*   Following is the syntax for **demo backup**
```
 rdac demo backup --to_dir demo

```

Example Output
```
 Backing up 109 Dashboards 
 Backing up 16 Dashboard Groups 
 Backing up 52 Published Pipelines 
 Backing up 11 Blueprints 
 Backing up 4 Synthetic Profiles 
 Backing up 4 Stacks used in Synthetic Profiles 
 2023-01-05:06:31:18 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Backing up 16 Endpoints 
 Backing up 9 Mappings 
 Backing up 98 Persistent Streams

```

****Sub Command: `diff`****

Description: Compare two backup directories
```
 rdac demo diff --help

```
```
 usage: demo [-h] --first FIRST --second SECOND [--details] [--side] 
             [--no_ident] [--opts OPTIONS] 
 
 optional arguments: 
   -h, --help       show this help message and exit 
   --first FIRST    First Directory where demo setup artifacts are stored. 
   --second SECOND  Second Directory where demo setup artifacts are stored. 
   --details        Show detailed diffs between files 
   --side           While Showing diffs use side-by-side format 
   --no_ident       Exclude Identical Objects from output 
   --opts OPTIONS   Comma separated list of artifacts names to restrict: stacks 
                    (st), pstreams (ps), dashboards (d), dashboard_groups 
                    (dg),synthetic_profiles (syn)

```

*   Following is the syntax for **demo diff**
```
  rdac demo diff --first demo --second demo2
 ```

Example Output
```
 Dashboard        l1-main-app                                        Identical 
 Dashboard        olb-engineering-dashboard_page_Metric Analysis     Identical 
 Dashboard        rda-mgmt-page-blueprints                           Identical 
 Dashboard        olb-business-command-center                        Identical 
 Dashboard        rda-microservice-traces_page_Healthchecks          Identical 
 Dashboard        rda-mgmt-page-stagingarea                          Identical 
 Dashboard        incident-metrics                                   Identical 
 Dashboard        ss_ch_all_sources                                  Identical 
 Dashboard        alert-incident-summary                             Identical 
 Dashboard        l2-l3-incidents                                    Identical 
 Dashboard        olb-observability-data_page_Metric Analysis        Identical 
 Dashboard        incident-topology                                  Identical 
 Dashboard        olb-bizops-observability_page_Incidents_network    Identical 
 Dashboard        ss_ch_pal_page_Analytics                           Identical 
 Dashboard        olb-bizops-observability                           Identical

```

*   Following is the syntax No.2 for **demo diff**
```
  rdac demo diff --first demo --second demo2 --no_ident
 ```

Example Output No.2
```
 286 Identical, 0 Only In First, 0 Only In Second, 0 Differ

```

****Sub Command: `setup`****

Description: Setup a target system for demo
```
 rdac demo setup --help

```
```
 usage: demo [-h] --dir FOLDER --ip PLATFORM_IP [--port WEBHOOK_PORT] 
             [--protocol  WEBHOOK_PROTO] [--pipelines PIPELINES] 
             [--blueprints BLUEPRINTS] [--verify_only] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --dir FOLDER          Directory where demo setup artifacts are stored. Most 
                         contain a settings.json in that folder 
   --ip PLATFORM_IP      Target platform Public IP Address 
   --port WEBHOOK_PORT   Port for webhook server (Default 7443) 
   --protocol  WEBHOOK_PROTO 
                         Protocol for Webhook server (Default https) 
   --pipelines PIPELINES 
                         Comma seperated list of Pipeline names to deploy them 
                         alone 
   --blueprints BLUEPRINTS 
                         Comma seperated list of Blueprint names to deploy them 
                         alone 
   --verify_only         Verify Only. Do not push changes to target system

```

*   Following is the syntax for **demo setup**
```
 rdac demo setup --dir demo --ip 10.95.122.127

```

Example Output
```
 WARNING: dashboards directory not found, skipping 
 WARNING: dashboard_groups directory not found, skipping 
 WARNING: stacks directory not found, skipping 
 WARNING: synthetic_profiles directory not found, skipping 
 WARNING: persistent_streams directory not found, skipping 
 WARNING: pipelines directory not found, skipping 
 WARNING: blueprints directory not found, skipping 
 WARNING: endpoints directory not found, skipping 
 WARNING: mappings directory not found, skipping 
 Performing Audit ... 
 2023-01-05:06:22:58 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Skipping audit for pstreams 
 Skipping audit for dashboards 
 Skipping audit for Dashboard Groups 
 Skipping audit for Stacks 
 Skipping audit for Synthetic Profiles 
 Skipping audit for Publish Pipelines 
 Skipping audit for Blueprints 
 
 Everyhing configured (Total Checks 2)

```

### Sub Command: `bundle-deploy`
```
 rdac bundle-deploy --help

```
```
 optional arguments: 
   -h, --help          show this help message and exit 
   --file BUNDLE_FILE  Bundle file to be deployed. Must be in .tar.gz format 
   --type TYPE         Deploy only specified types. Comma separated list. (d: 
                       dashboard, b: blueprint, p: pipeline) 
   --compare           Compare bundle vs currently deployed. Do not deploy any 
                       artifact

```

Example
```
 rdac bundle-deploy --file demo.tar.gz --type p

```

Example Output
```
 Deployed following artifacts from this bundle: 
 
     type      name 
 --  --------  --------------------------------------------------- 
  0  pipeline  vmware_vcenter_inventory_pipeline_v1_c1 
  1  pipeline  vmware_vcenter_inventory_topology_pipeline_v1_c2 
  2  pipeline  windows_host_os_system_inventory_and_topology_v1_c1 
  3  pipeline  irm-stream-missing-columns-update 
  4  pipeline  netapp_cmode_storage_arrays_inventory_v1 
  5  pipeline  vmware_vcenter_inventory_pipeline_v1_c2 
  6  pipeline  vmware_vcenter_inventory_topology_pipeline_v1_c1 
  7  pipeline  linux_host_os_system_inventory_and_topology_v1_c2 
  8  pipeline  linux_host_os_system_inventory_and_topology_v1_c3 
  9  pipeline  oia-sources-streams-merge 
 10  pipeline  netapp_storage_array_topology_pipeline_v1 
 11  pipeline  kubernetes_cluster_inventory_pipeline_v1 
 12  pipeline  cisco_ucs_cimc_inventory_v1 
 13  pipeline  linux_host_os_system_inventory_and_topology_v1_c1 
 14  pipeline  windows_host_os_system_inventory_and_topology_v1_c2 
 15  pipeline  kubernetes_cluster_topology_pipeline_v1 
 16  pipeline  cisco-ucsm-infra-topology-pipeline-v1 
 17  pipeline  NetApp_7Mode_inventroy

```

Note

Similar to the pipeline bundle deployment in the example shown above, We can deploy for Dashboards and Service Blueprints

### Sub Command: `deployment`

**Following are the valid Sub-Commands for the deployment**

| Sub Commands | Description |
| --- | --- |
| activity | List recent deployment activities |
| status | Display status of all deployments |
| audit-report | Display Audit report for a given deployment ID |
| add | Add a new Deployment to the repository. Deployment specification must be in valid YML format |
| enable | Enable an existing deployment if it is not already enabled |
| disable | Disable an existing deployment if it is not already disabled |
| delete | Delete an existing deployment from repository |
| dependencies | List all artifact dependencies used by the deployment |
| svcs-status | List current status of all service pipelines in a deployment |
| map | Print service map information in JSON format for the given deployment |
```
 rdac deployment --help

```
```
 Following are valid sub-commands for deployment: 
 
   activity                  List recent deployment activities 
   status                    Display status of all deployments 
   audit-report              Display Audit report for a given deployment ID 
   add                       Add a new Deployment to the repository. Deployment specification must be in valid YML format 
   enable                    Enable an existing deployment if it is not already enabled 
   disable                   Disable an existing deployment if it is not already disabled 
   delete                    Delete an existing deployment from repository 
   dependencies              List all artifact dependencies used by the deployment 
   svcs-status               List current status of all service pipelines in a deployment 
   map                       Print service map information in JSON format for the given deployment

```

****Sub Command: `activity`****

Description: List recent deployment activities
```
 rdac deployment activity --help

```
```
 usage: deployment [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```

*   Following is the syntax for **deployment activity**
```
 rdac deployment activity

```

Example Output
```
     timestamp                   severity    message 
 --  --------------------------  ----------  ---------------------------------------------------------------------------------------------------------------------------------------- 
  0  2022-12-21T09:05:13.943451  WARNING     Re-Created Job: f5cc308e6d014173ac2a7893b1bae564 for Deployment Name: Demo_vmware_service_blueprint, Id: b744c8c2. Restart Count: 213 
  1  2022-12-21T09:05:13.301284  WARNING     Re-Created Job: 19c5ad1f4b5442a6a662bfd0493cc3db for Deployment Name: Service Action schedule pipeline, Id: b744c8c0. Restart Count: 213 
  2  2022-12-21T09:05:12.817716  WARNING     Re-Created Job: 8cc74ba0d633413faea5230aa2590d41 for Deployment Name: Blueprint_18_11_2022, Id: b744c873. Restart Count: 213 
  3  2022-12-21T09:04:02.257588  WARNING     Re-Created Job: 4d2b3770013b462db8cbcc421084a057 for Deployment Name: Demo_vmware_service_blueprint, Id: b744c8c2. Restart Count: 212 
  4  2022-12-21T09:04:01.482574  WARNING     Re-Created Job: e37777adca0a4a3fb6eeb431e0b9acca for Deployment Name: Service Action schedule pipeline, Id: b744c8c0. Restart Count: 212 
  5  2022-12-21T09:04:00.992727  WARNING     Re-Created Job: b792ae4110a6469883abcdf709692dee for Deployment Name: Blueprint_18_11_2022, Id: b744c873. Restart Count: 212 
  6  2022-12-21T09:02:50.307263  WARNING     Re-Created Job: f9e9a10bf1dd46e8a14049d0ac26a87a for Deployment Name: Demo_vmware_service_blueprint, Id: b744c8c2. Restart Count: 211
 ```

****Sub Command: `status`****

Description: Display status of all deployments
```
 rdac deployment status --help

```
```
 usage: deployment [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```

*   Following is the syntax for **deployment status**
```
 rdac deployment status

```

Example Output
```
     id                                      category                                name                                    description                                                                                     enabled      errors    warnings 
 --  --------------------------------------  --------------------------------------  --------------------------------------  ----------------------------------------------------------------------------------------------  ---------  --------  ---------- 
  0  41e33973                                ITSM                                    eBonding                                eBond ServiceNow incidents to PagerDuty, Twilio-SMS, Elasticsearch/Kibana, Slack, Email         no                0           0 
  1  81a1a030                                ITOM                                    ML-Experiments                          ML Experiments                                                                                  yes               0           0 
  2  81a1a2202                               ITOM                                    OIA                                     Ops Intelligence & Analytics                                                                    yes               0           0 
  3  81a1a2203                               ITOM                                    Stacks                                  Stacks                                                                                          yes               0           0 
  4  V2tdZpEs                                Dependency Mapping                      AWS Dependency Mapper                   AWS Dependency mapping with updates every hour                                                  yes               2           0 
  5  b744c873                                Service Action schedule pipeline        Blueprint_18_11_2022                    Service Action schedule pipeline example                                                        yes               0           2 
  6  b744c8c0                                Service Action schedule pipeline        Service Action schedule pipeline        Service Action schedule pipeline example                                                        yes               0           1 
  7  b744c8c1                                Service Action schedule pipeline        Blueprint_16_11_2022                    Service Action schedule pipeline example                                                        no                0           0 
  8  b744c8c2                                vmware schedule pipeline                Demo_vmware_service_blueprint           vmware schedule pipeline                                                                        yes               0           0 
  9  exec_dashboard_kpi_metrics_querystream  exec_dashboard_kpi_metrics_querystream  exec_dashboard_kpi_metrics_querystream  exec_dashboard_kpi_metrics_querystream                                                          yes               0           0 
 10  guide001                                Log Analytics                           Beginner Guide Blueprint                Generate Synthetic Syslogs, Save all logs to Log Archive, send processed logs to a NULL stream  yes               0           0
 ```

****Sub Command: `audit-report`****

Description: Display Audit report for a given deployment ID
```
 rdac deployment audit-report --help

```
```
 usage: deployment [-h] --id DEPLOYMENT_ID [--json] 
 
 optional arguments: 
   -h, --help          show this help message and exit 
   --id DEPLOYMENT_ID  Deployment ID 
   --json              Print detailed information in JSON format instead of 
                       tabular format

```

*   Following is the syntax for **deployment audit-report**
```
 rdac deployment audit-report --id V2tdZpEs

```

Example Output
```
     type                      severity    message 
 --  ------------------------  ----------  ------------------------------------------------------------------------------------------- 
  0  Verify Pipeline           INFO        Pipeline with name 'aws-dependency-mapper' and version '22_02_16_1' loaded 
  1  Verify Pipeline           INFO        Pipeline with name 'aws-dependency-mapper-inner-pipeline' and version '2022_02_16_1' loaded 
  2  Verify Pipeline           ERROR       No published versions found for pipline: aws-dependency-mapper2 
  3  Verify Site               ERROR       No sites matched the regex 'cfx.*' or no active workers found 
  4  Verify Source             INFO        Credential found for Integration: aws, Type: aws_v2 
  5  Verify Persistent Stream  INFO        PStream rda_worker_resource_usage found 
  6  Verify Persistent Stream  INFO        PStream rda_system_worker_trace_summary found 
  7  Verify Persistent Stream  INFO        PStream rda_worker_resource_usage found 
  8  Verify Persistent Stream  INFO        PStream rda_system_worker_trace_summary found 
  9  Verify Persistent Stream  INFO        PStream rda_system_deployment_updates found 
 10  Verify Persistent Stream  INFO        PStream rda_system_gw_endpoint_metrics found
 ```

****Sub Command: `add`****

Description: Add a new Deployment to the repository. Deployment specification must be in valid YML format
```
 rdac deployment add --help

```
```
 usage: deployment [-h] --file INPUT_FILE [--overwrite] 
 
 optional arguments: 
   -h, --help         show this help message and exit 
   --file INPUT_FILE  YAML file containing Deployment specification 
   --overwrite        Overwrite even if a ruleset already exists with a name.

```

*   Following is the syntax for **deployment add**
```
 rdac deployment add --file blueprint.yml

```

*   sample blueprint.yml file
```
 cat > blueprint.yml << 'EOF' 
 name: Blueprint_Example 
 id: b744c873a 
 version: '2022_12_19_01' 
 category: Service Action schedule pipeline 
 comment: Service Action schedule pipeline example 
 enabled: true 
 type: Service 
 auto_deploy: false 
 provider: CloudFabrix Software Inc. 
 attrs: {} 
 service_pipelines: 
     -   name: Service_Pipeline 
         label: Service Pipelines 
         version: '*' 
         site: rda-site-01 
         site_type: regex 
         instances: 1 
         scaling_policy: 
             min_instances: 1 
             max_instances: 1 
 action_pipelines: 
     -   name: Action_Pipeline 
         label: Action Pipelines 
         version: '*' 
         site: rda-site-01 
         site_type: regex 
         instances: 1 
         scaling_policy: 
             min_instances: 1 
             max_instances: 1 
 scheduled_pipelines: 
     -   name: schedule_pipeline 
         label: Scheduled Pipelines 
         version: '*' 
         site: rda-site-01 
         cron_expression: '*/5 * * * *' 
         site_type: regex 
         instances: 1 
         scaling_policy: 
             min_instances: 1 
             max_instances: 1 
 
 EOF

```

Example Output
```
 Added deployment spec with Name: Blueprint_Example, ID: b744c873a

```

****Sub Command: `enable`****

Description: Enable an existing deployment if it is not already enabled
```
 rdac deployment enable --help

```
```
 Usage: deployment-enable  [-h] --id DEP_ID 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --id DEP_ID  Deployment ID

```

*   Following is the syntax for **deployment enable**
```
 rdac deployment disable --id b744c8c1

```

Example Output
```
 Updated deployment with ID ID: b744c8c1

```

****Sub Command: `disable`****

Description: Disable an existing deployment if it is not already disabled
```
 rdac deployment enable --help

```
```
 Usage: deployment-disable  [-h] --id DEP_ID 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --id DEP_ID  Deployment ID

```

*   Following is the syntax for **deployment disable**
```
 rdac deployment disable --id b744c8c1

```

Example Output
```
 Updated deployment with ID ID: b744c8c1

```

****Sub Command: `delete`****

Description: Delete an existing deployment from repository
```
 rdac deployment delete --help

```
```
 usage: deployment [-h] --id DEP_ID 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --id DEP_ID  Deployment ID

```

*   Following is the syntax for **deployment delete**
```
 rdac deployment delete --id 44de62c6

```

Example Delete
```
 2022-12-22:08:49:02 [1] INFO nats_client Creating new SharedPool ... 
 2022-12-22:08:49:02 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2022-12-22:08:49:02 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Deleted deployment with ID ID: 44de62c6

```

****Sub Command: `dependencies`****

Description: List all artifact dependencies used by the deployment
```
 rdac deployment-dependencies --help

```
```
 Usage: deployment-dependencies  [-h] --id DEPLOYMENT_ID [--json] 
 
 optional arguments: 
   -h, --help          show this help message and exit 
   --id DEPLOYMENT_ID  Deployment ID 
   --json              Print detailed information in JSON format instead of 
                       tabular format

```

*   Following is the syntax for **deployment dependencies**
```
 rdac deployment dependencies --id V2tdZpEs

```

Example Output
```
     type      name                                  read    write 
 --  --------  ------------------------------------  ------  ------- 
  0  pipeline  aws-dependency-mapper                 True    False 
  1  pipeline  aws-dependency-mapper-inner-pipeline  True    False 
  2  dataset   cfx-aws-ec2-instances                 True    True 
  3  dataset   cfx-aws-ec2-instance-types            True    True 
  4  dataset   cfx-aws-ec2-volumes                   True    True 
  5  dataset   cfx-aws-ec2-vpcs                      True    True 
  6  dataset   cfx-aws-ec2-efs-filesystems           True    True 
  7  dataset   cfx-aws-ec2-security-groups           True    True 
  8  dataset   cfx-aws-ec2-subnets                   True    True 
  9  dataset   cfx-aws-ec2-internet-gateways         True    True 
 10  dataset   cfx-aws-ec2-security-group-nodes      True    True
 ```

****Sub Command: `svcs-status`****

Description: List current status of all service pipelines in a deployment
```
 rdac deployment svcs-status --help

```
```
 usage: deployment [-h] --id DEPLOYMENT_ID [--json] 
 
 optional arguments: 
   -h, --help          show this help message and exit 
   --id DEPLOYMENT_ID  Deployment ID 
   --json              Print detailed information in JSON format instead of 
                       tabular format

```

*   Following is the syntax for **deployment svcs-status**
```
 deployment svcs-status --id 41e33973

```

Example Output
```
   label                                                         pipeline_name                               version      min_instances    max_instances    instances    num_jobs 
 --  ------------------------------------------------------------  ------------------------------------------  ---------  ---------------  ---------------  -----------  ---------- 
  0  Read incidents from ServiceNow write to stream                ebonding-servicenow-to-stream-v2            *                        1                4            1           0 
  1  Read incidents from stream and write to Elasticsearch/Kibana  ebonding-stream-to-elasticsearch-kibana-v2  *                        0                4            1           0 
  2  Read incidents from stream and write to Twilio-SMS            ebonding-stream-to-twilio-sms-v2            *                        0                4            1           0 
  3  Read incidents from stream and write to PagerDuty             ebonding-stream-to-pagerduty                *                        0                4            1           0 
  4  Read incidents from stream and write to Slack                 ebonding-stream-to-slack                    *                        0                4            1           0 
  5  Read incidents from stream and write to Email                 ebonding-stream-to-email                    *                        0                4            1           0
 ```

****Sub Command: `map`****

Description: Print service map information in JSON format for the given deployment
```
 rdac deployment map --help

```
```
 Usage: deployment-map  [-h] --id DEPLOYMENT_ID 
 
 optional arguments: 
   -h, --help          show this help message and exit 
   --id DEPLOYMENT_ID  Deployment ID

```

*   Following is the syntax for **deployment map**
```
 rdac deployment map --id 41e33973

```

Example Output
```
 { 
   "status": "ok", 
   "reason": "", 
   "data": { 
     "stack": { 
       "name": "eBonding", 
       "description": "Service map for blueprint: eBonding", 
       "nodes": [ 
         { 
           "node_id": "rda-network-stream-ebonding-analytics", 
           "node_type": "rda-network-stream", 
           "layer": "RDA Stream", 
           "iconURL": "Stream", 
           "node_label": "ebonding-analytics" 
         }, 
         { 
           "node_id": "pstream-ebonding-analytics", 
           "node_type": "Persistent Stream", 
           "node_label": "ebonding-analytics", 
           "layer": "Persistent Stream", 
           "iconURL": "Persistent_Stream" 
         }, 
         { 
           "node_id": "rda-network-stream-rda_worker_resource_usage", 
           "node_type": "rda-network-stream", 
           "layer": "RDA Stream", 
           "iconURL": "Stream", 
           "node_label": "rda_worker_resource_usage", 
           "defaultVisibility": "hidden" 
         }, 
         { 
           "node_id": "pstream-rda_worker_resource_usage", 
           "node_type": "Persistent Stream", 
           "node_label": "rda_worker_resource_usage", 
           "layer": "Persistent Stream", 
           "iconURL": "Persistent_Stream", 
           "defaultVisibility": "hidden" 
         }, 
         { 
           "node_id": "rda-network-stream-rda_system_worker_trace_summary", 
           "node_type": "rda-network-stream", 
           "layer": "RDA Stream", 
           "iconURL": "Stream", 
           "node_label": "rda_system_worker_trace_summary", 
           "defaultVisibility": "hidden" 
         }, 
         { 
           "node_id": "pstream-rda_system_worker_trace_summary", 
           "node_type": "Persistent Stream", 
           "node_label": "rda_system_worker_trace_summary", 
           "layer": "Persistent Stream", 
           "iconURL": "Persistent_Stream", 
           "defaultVisibility": "hidden" 
         }, 
         { 
           "node_id": "rda-network-stream-rda_system_deployment_updates", 
           "node_type": "rda-network-stream", 
           "layer": "RDA Stream", 
           "iconURL": "Stream", 
           "node_label": "rda_system_deployment_updates", 
           "defaultVisibility": "hidden" 
         }, 
         { 
           "node_id": "pstream-rda_system_deployment_updates", 
           "node_type": "Persistent Stream", 
           "node_label": "rda_system_deployment_updates", 
           "layer": "Persistent Stream", 
           "iconURL": "Persistent_Stream", 
           "defaultVisibility": "hidden" 
         } 
       ], 
       "relationships": [ 
         { 
           "left_id": "rda-network-stream-ebonding-analytics", 
           "right_id": "pstream-ebonding-analytics", 
           "description": "Stream persistence", 
           "relationship_type": "uses" 
         }, 
         { 
           "left_id": "rda-network-stream-rda_worker_resource_usage", 
           "right_id": "pstream-rda_worker_resource_usage", 
           "description": "Stream persistence", 
           "relationship_type": "uses" 
         }, 
         { 
           "left_id": "rda-network-stream-rda_system_worker_trace_summary", 
           "right_id": "pstream-rda_system_worker_trace_summary", 
           "description": "Stream persistence", 
           "relationship_type": "uses" 
         }, 
         { 
           "left_id": "rda-network-stream-rda_worker_resource_usage", 
           "right_id": "pstream-rda_worker_resource_usage", 
           "description": "Stream persistence", 
           "relationship_type": "uses" 
         }, 
         { 
           "left_id": "rda-network-stream-rda_system_worker_trace_summary", 
           "right_id": "pstream-rda_system_worker_trace_summary", 
           "description": "Stream persistence", 
           "relationship_type": "uses" 
         }, 
         { 
           "left_id": "rda-network-stream-rda_system_deployment_updates", 
           "right_id": "pstream-rda_system_deployment_updates", 
           "description": "Stream persistence", 
           "relationship_type": "uses" 
         } 
       ] 
     } 
   } 
 }

```

### Sub Command: `event-gw-status`

Description: List status of all ingestion endpoints at all the event gateways
```
 rdac event-gw-status --help

```
```
 usage: rdac [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```

\* Following is the syntax for **event-gw-status**
```
 rdac event-gw-status

```

Example Output
```
 No Event gateways found

```

### Sub Command: `evict`

Description: Evict a job from a worker pod
```
 Usage: evict  [-h] --jobid JOBID [--yes] 
 
 optional arguments: 
   -h, --help     show this help message and exit 
   --jobid JOBID  RDA worker jobid. If partial must match only one job. 
   --yes          Do not prompt for confirmation, evict if job is found

```

### Sub Command: `file-ops`

Description: Perform various operations on local files
```
 rdac file-ops --help

```
```
 Usage: file-ops copy                      Copy dataframe from one format to another. Format is inferred from extension. Examples are csv, parquet, json 
   csv-to-parquet            Copy data from CSV to parquet file using chunking 
   test-formats              Run performance test on various formats 
 
 positional arguments: 
   subcommand  File ops sub-command 
 
 optional arguments: 
   -h, --help  show this help message and exit

```

\* Following is the syntax for **file-ops**
```
 rdac file-ops csv-to-parquet --from metrics.csv --to metrics_parquet

```

Example Output
```
 Output File: 
       File Size:       1,687,359 
       Copy time (ms): 585.7

```

### Sub Command: `file-to-object`

Description: Convert files from a column into objects
```
 Usage: file-to-object  [-h] --inpcol INPUT_FILENAME_COLUMN --outcol OUTPUT_COLUMN --file 
             INPUT_FILE --outfolder OUTPUT_FOLDER --outfile OUTPUT_FILE 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --inpcol INPUT_FILENAME_COLUMN 
                         Name of the column in input that contains the 
                         filenames 
   --outcol OUTPUT_COLUMN 
                         Column name where object names will be inserted 
   --file INPUT_FILE     Input csv filename 
   --outfolder OUTPUT_FOLDER 
                         Folder name where objects will be stored 
   --outfile OUTPUT_FILE 
                         Name of output csv file that has object location 
                         stored

```

### Sub Command: `fmt-template-delete`

Description: Delete Formatting Template
```
 Usage: fmt-template-delete  [-h] --name NAME 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --name NAME  Formatting Template Name

```

### Sub Command: `fmt-template-get`

Description: Get Formatting Template
```
 Usage: fmt-template-get  [-h] --name NAME [--tofile SAVE_TO_FILE] [--json] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Formatting Template Name 
   --tofile SAVE_TO_FILE 
                         Save the data to the specified file 
   --json                Export data as a JSON formatted rows. ** Deprecated. 
                         Use --format **

```

### Sub Command: `fmt-template-list`

Description: List Formatting Templates
```
 Usage: fmt-template-list  [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```

### Sub Command: `healthcheck`

Description: Perform healthcheck on each of the Pods
```
 Usage: healthcheck  [-h] [--json] [--type POD_TYPE] [--infra] [--apps] [--simple] 
 
 optional arguments: 
   -h, --help       show this help message and exit 
   --json           Print detailed information in JSON format instead of 
                    tabular format 
   --type POD_TYPE  Show only the pods that match the specified pod type 
   --infra          List only RDA Infra pods. not compatible with --apps option 
   --apps           List only RDA App pods. not compatible with --infra option 
   --simple         When showing in tabular format, show in a easy to read 
                    format.

```

### Sub Command: `invoke-agent-bot`

Description: Invoke a bot published by an agent
```
 Usage: invoke-agent-bot  [-h] --type AGENT_TYPE --group AGENT_GROUP --bot BOT_NAME 
             [--query QUERY] [--input INPUT_FILE] [--output OUTPUT_FILE] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --type AGENT_TYPE     Agent type 
   --group AGENT_GROUP   Agent group 
   --bot BOT_NAME        Bot name 
   --query QUERY         Bot Query (CFXQL) 
   --input INPUT_FILE    Input Dataframe (CSV File) 
   --output OUTPUT_FILE  Output Dataframe (CSV File)

```

### Sub Command: `jobs`

Description: List all jobs for the current tenant
```
 rdac jobs --help

```
```
 usage: rdac [-h] [--json] [--all] [--pipeline_name PIPELINE_NAME] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --json                Print detailed information in JSON format instead of 
                         tabular format 
   --all                 Retrieve all jobs not just active jobs 
   --pipeline_name PIPELINE_NAME 
                         Get all jobs for given pipeline name

```

\* Following is the syntax for **jobs**
```
 rdac jobs --pipeline_name 'oia-new-incidents-to-snowv2'

```

Example Output
```
 2023-01-09:05:58:09 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 worker pipeline name: oia-new-incidents-to-snowv2 
 +--------------+----------+----------------------------------+-------+---------------------+-----------------+-----------------------------+--------------+----------+ 
 | Host         | Pod ID   | Job ID                           |   PID | Created             | Age             | Pipeline                    | Status       | Reason   | 
 |--------------+----------+----------------------------------+-------+---------------------+-----------------+-----------------------------+--------------+----------| 
 | 05969789d903 | 88c26bbe | 5c93dc55cfd84586921aad41b9e7358e |   761 | 2023-01-07T14:00:03 | 1 day, 15:58:06 | oia-new-incidents-to-snowv2 | Initializing |          | 
 | 05969789d903 | 88c26bbe | f0f1d6a240cb45fabf3e65f0c4eb9cfe |  1605 | 2023-01-07T14:35:02 | 1 day, 15:23:07 | oia-new-incidents-to-snowv2 | Initializing |          | 
 | 05969789d903 | 88c26bbe | 384acd9ef4c240aa88c629a75523bc56 |  2352 | 2023-01-07T15:05:02 | 1 day, 14:53:07 | oia-new-incidents-to-snowv2 | Initializing |          | 
 | 05969789d903 | 88c26bbe | 84d8547509c94a4eaf695c57aa139506 | 17718 | 2023-01-08T01:30:02 | 1 day, 4:28:07  | oia-new-incidents-to-snowv2 | Initializing |          | 
 | 05969789d903 | 88c26bbe | 58848c8d5a7e4c54a08e01d25155f22e | 18097 | 2023-01-08T01:45:01 | 1 day, 4:13:08  | oia-new-incidents-to-snowv2 | Initializing |          | 
 | 05969789d903 | 88c26bbe | 32faf9f9ba2445b4b1cc2fb625538f35 | 19080 | 2023-01-08T02:25:02 | 1 day, 3:33:07  | oia-new-incidents-to-snowv2 | Initializing |          | 
 | 05969789d903 | 88c26bbe | b5dc599ce659485f9139242d05c9875e | 23632 | 2023-01-08T05:30:02 | 1 day, 0:28:07  | oia-new-incidents-to-snowv2 | Initializing |          | 
 | 05969789d903 | 88c26bbe | fd361ae94358405cbb9f2ac1d75c142c | 39213 | 2023-01-08T14:20:02 | 15:38:07        | oia-new-incidents-to-snowv2 | Initializing |          | 
 | 05969789d903 | 88c26bbe | 07da31424e18492e976db4451ce82252 | 44773 | 2023-01-08T18:05:02 | 11:53:07        | oia-new-incidents-to-snowv2 | Initializing |          | 
 | 05969789d903 | 88c26bbe | f332d5c0055f43839dffd906c04fb842 | 50985 | 2023-01-08T22:20:01 | 7:38:08         | oia-new-incidents-to-snowv2 | Initializing |          | 
 | 05969789d903 | 88c26bbe | 43b00217d5854d4cb5ab7497929b8369 | 57340 | 2023-01-09T03:30:03 | 2:28:06         | oia-new-incidents-to-snowv2 | Initializing |          | 
 | 05969789d903 | 88c26bbe | 78ab3c2492aa4781820c0be9013cc6d9 | 59707 | 2023-01-09T05:25:02 | 0:33:07         | oia-new-incidents-to-snowv2 | Initializing |          | 
 +--------------+----------+----------------------------------+-------+---------------------+-----------------+-----------------------------+--------------+----------+

```

### Sub Command: `logarchive-add-platform`

Description: Add current platform Minio as logarchive repository
```
 Usage: logarchive-add-platform  [-h] --repo REPO --prefix OBJECT_PREFIX 
             [--retention RETENTION_DAYS] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --repo REPO           Log archive repository name to be created 
   --prefix OBJECT_PREFIX 
                         Object prefix to be used for the archive 
   --retention RETENTION_DAYS 
                         Data retention period in number of days. If not 
                         specified, RDA will not manage the data retention.

```

### Sub Command: `logarchive-data-read`

Description: Read the data from given archive for a specified time interval
```
 Usage: logarchive-data-read  [-h] --repo REPO --name ARCHIVE_NAME [--from TIMESTAMP] 
             [--minutes MINUTES] [--max_rows MAX_ROWS] [--speed SPEED] [--line] 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --repo REPO          Log archive repository name 
   --name ARCHIVE_NAME  Name of the log archive within the repository 
   --from TIMESTAMP     From Date & time in text format (ex: ISO format). 
                        Timezone must be UTC. If not specified, it will use 
                        current time minus specified minutes 
   --minutes MINUTES    Number of minutes from specified date & time. Default 
                        is 15 
   --max_rows MAX_ROWS  If value is specified > 0, stop after reading max_rows 
                        from the archive 
   --speed SPEED        Replay speed. 0 means no delay, 1.0 means closer to 
                        original rate, < 1.0 means slower, > 1.0 means faster 
   --line               Instead of JSON format, print one message per line

```

### Sub Command: `logarchive-data-size`

Description: Show size of data available for given archive for a specified time interval
```
 Usage: logarchive-data-size  [-h] --repo REPO --name ARCHIVE_NAME [--from TIMESTAMP] 
             [--minutes MINUTES] [--json] 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --repo REPO          Log archive repository name 
   --name ARCHIVE_NAME  Name of the log archive within the repository 
   --from TIMESTAMP     From Date & time in text format (ex: ISO format). 
                        Timezone must be UTC. If not specified, it will use 
                        current time minus specified minutes 
   --minutes MINUTES    Number of minutes from specified date & time. Default 
                        is 15 
   --json               Print detailed information in JSON format instead of 
                        tabular format

```

### Sub Command: `logarchive-download`

Description: Download the data from given archive for a specified time interval
```
 Usage: logarchive-download  [-h] --repo REPO --name ARCHIVE_NAME [--from TIMESTAMP] 
             [--minutes MINUTES] --out OUTPUT_DIR [--flatten] 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --repo REPO          Log archive repository name 
   --name ARCHIVE_NAME  Name of the log archive within the repository 
   --from TIMESTAMP     From Date & time in text format (ex: ISO format). 
                        Timezone must be UTC. If not specified, it will use 
                        current time minus specified minutes 
   --minutes MINUTES    Number of minutes from specified date & time. Default 
                        is 15 
   --out OUTPUT_DIR     Output directory where to save the downloaded data 
   --flatten            Flatten directory structure of the files, which 
                        otherwise stores in yyyy/mm/dd/HH/MM/ directory 
                        structure

```

### Sub Command: `logarchive-names`

Description: List archive names in a given repository
```
 Usage: logarchive-names  [-h] --repo REPO [--json] 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --repo REPO  Name of the log archive repository 
   --json       Print detailed information in JSON format instead of tabular 
                format

```

### Sub Command: `logarchive-replay`

Description: Replay the data from given archive for a specified time interval with specified label
```
 Usage: logarchive-replay  [-h] --repo REPO --name ARCHIVE_NAME [--from TIMESTAMP] 
             [--minutes MINUTES] [--max_rows MAX_ROWS] [--speed SPEED] 
             [--batch_size BATCH_SIZE] --stream STREAM [--label LABEL] --site 
             SITE 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --repo REPO           Log archive repository name 
   --name ARCHIVE_NAME   Name of the log archive within the repository 
   --from TIMESTAMP      From Date & time in text format (ex: ISO format). 
                         Timezone must be UTC. If not specified, it will use 
                         current time minus specified minutes 
   --minutes MINUTES     Number of minutes from specified date & time. Default 
                         is 15 
   --max_rows MAX_ROWS   If value is specified > 0, stop after reading max_rows 
                         from the archive 
   --speed SPEED         Replay speed. 0 means no delay, 1.0 means closer to 
                         original rate, < 1.0 means slower, > 1.0 means faster 
   --batch_size BATCH_SIZE 
                         Number of rows to return for each iteration 
   --stream STREAM       Name of the stream to write to 
   --label LABEL         Label for the replay job 
   --site SITE           Site name to run this on a worker

```

### Sub Command: `logarchive-repos`

Description: List of all log archive repositories
```
 rdac logarchive-repos --help

```
```
 Usage: logarchive-repos  [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```

*   Following is the syntax for **logarchive-repos**
```
 rdac logarchive-repos

```

Example Output
```
 +-------------------+--------------------+------------------------------------------+-----------------+ 
 | Repository Name   | Endpoint           | Bucket Name                              | Object Prefix   | 
 |-------------------+--------------------+------------------------------------------+-----------------| 
 | demo_logarchive   | 10.95.122.127:9443 | tenants.ae144f67d2a24034ad6920ace6809763 | demo_logs/      | 
 +-------------------+--------------------+------------------------------------------+-----------------+

```

### Sub Command: `merge-logarchive-files`

Description: Merge multiple locally downloaded Log Archive (.gz) filles into a single CSV/Parquet file
```
 Usage: merge-logarchive-files  [-h] --folder FOLDER --tofile TOFILE [--sample SAMPLE_RATE] 
             [--ts TIMESTAMP] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --folder FOLDER       Path to the folder where locally downloaded .gz files 
                         are available 
   --tofile TOFILE       Save the output to specified file 
   --sample SAMPLE_RATE  Data sample rate must be >0 and <= 1.0 
   --ts TIMESTAMP        Timestamp column, if specified will sort the data 
                         after merge

```

### Sub Command: `object`

Description: RDA Object management commands

**Following are the valid Sub-Commands for the object**

| Sub Commands | Description |
| --- | --- |
| list | List objects from the object store |
| get | Download a object from the object store |
| meta | Download metadata for an object from the object store |
| add | Add a new object to the object store |
| delete | Delete object from the object store |
| to-file | Convert object pointers from a column into file |
| to-content | Convert object pointers from a column into content |
| delete-list | Delete list of objects |
```
 rdac object --help

```
```
 RDA Object management commands 
 
 Following are valid sub-commands for object: 
   list                      List objects from the object store 
   get                       Download a object from the object store 
   meta                      Download metadata for an object from the object store 
   add                       Add a new object to the object store 
   delete                    Delete object from the object store 
   to-file                   Convert object pointers from a column into file 
   to-content                Convert object pointers from a column into content 
   delete-list               Delete list of objects

```

### Sub Command: `object-add`

Description: Add a new object to the object store
```
 rdac object-add --help

```
```
 Usage: object-add  [-h] --name NAME --folder FOLDER --file INPUT_FILE 
             [--descr DESCRIPTION] [--overwrite OVERWRITE] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Object name 
   --folder FOLDER       Folder name on the object storage 
   --file INPUT_FILE     file from which object will be added 
   --descr DESCRIPTION   Description 
   --overwrite OVERWRITE 
                         If file already exists, overwrite without prompting. 
                         Accepted values (yes/no)

```

### Sub Command: `object-delete`
```
 rdac object-delete --help

```

Description: Delete object from the object store
```
 Usage: object-delete  [-h] --name NAME --folder FOLDER 
 
 optional arguments: 
   -h, --help       show this help message and exit 
   --name NAME      Object name 
   --folder FOLDER  Folder name on the object storage

```

*   Following is the syntax for **object-get**
```
 rdac object delete --name testobjectnew --folder testobj-foldernew

```

Example Output
```
 Done deleting objects

```

### Sub Command: `object-delete-list`

Description: Delete list of objects
```
 rdac object-delete-list --help

```
```
 Usage: object-delete-list  [-h] --inpcol INPUT_OBJECT_COLUMN --file INPUT_FILE --outfile 
             OUTPUT_FILE 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --inpcol INPUT_OBJECT_COLUMN 
                         Column with object names 
   --file INPUT_FILE     Input csv filename 
   --outfile OUTPUT_FILE 
                         Name of output csv file that has result for deletion

```

### Sub Command: `object-get`

Description: Download a object from the object store
```
 rdac object-get --help

```
```
 usage: rdac [-h] --name NAME --folder FOLDER [--tofile SAVE_TO_FILE] 
             [--todir SAVE_TO_DIR] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Object name 
   --folder FOLDER       Folder name on the object storage 
   --tofile SAVE_TO_FILE 
                         Save the downloaded object to specified file 
   --todir SAVE_TO_DIR   Save the downloaded object to specified directory

```

*   Following is the syntax for **object-get**
```
 rdac object get --name testobject --folder testobj-folder

```

Example Output
```
 Object saved to /tmp/rda-object-cache/8a2e7e88e5548c33/testobject.csv

```

### Sub Command: `object-list`

Description: List objects from the object store
```
 rdac object-list --help

```
```
 usage: rdac [-h] [--folder FOLDER] [--json] 
 
 optional arguments: 
   -h, --help       show this help message and exit 
   --folder FOLDER  Folder name on the object storage 
   --json           Print detailed information in JSON format instead of 
                    tabular format

```

*   Following is the syntax for **object-list**
```
 rdac object list

```

Example Output
```
 folder             name           description    file_type      file_size  saved_time 
 -----------------  -------------  -------------  -----------  -----------  -------------------------- 
 testobj-folder     testobject     testobjct      csv             15303849  2023-01-09T06:12:03.413276 
 testobj-foldernew  testobjectnew  testobjctnew   csv             15303849  2023-01-09T06:12:55.904404

```

### Sub Command: `object-meta`
```
 rdac object-meta --help

```

Description: Download metadata for an object from the object store
```
 Usage: object-meta  [-h] --name NAME --folder FOLDER 
 
 optional arguments: 
   -h, --help       show this help message and exit 
   --name NAME      Dataset name 
   --folder FOLDER  Folder name on the object storage

```

\* Following is the syntax for **object-meta**
```
 rdac object meta --name testobject --folder testobj-folder

```

Example Output
```
 { 
   "name": "testobject", 
   "folder": "testobj-folder", 
   "description": "testobjct", 
   "saved_time": "2023-01-09T06:12:03.413276", 
   "data_path": "rda-objects/data/testobj-folder/6f44d574-testobject.data", 
   "file_type": "csv", 
   "file_size": 15303849 
 }

```

### Sub Command: `object-to-content`

Description: Convert object pointers from a column into content
```
 rdac object-to-content --help

```
```
 Usage: object-to-content  [-h] --inpcol INPUT_OBJECT_COLUMN --outcol OUTPUT_COLUMN --file 
             INPUT_FILE --outfile OUTPUT_FILE 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --inpcol INPUT_OBJECT_COLUMN 
                         Name of the column in input that contains the object 
                         name 
   --outcol OUTPUT_COLUMN 
                         Column name where content will be inserted 
   --file INPUT_FILE     Input csv file 
   --outfile OUTPUT_FILE 
                         Name of output csv file that has content inserted

```

### Sub Command: `object-to-file`

Description: Convert object pointers from a column into file
```
 rdac object-to-file --help

```
```
 usage: rdac [-h] --inpcol INPUT_OBJECT_COLUMN --outcol OUTPUT_COLUMN --file 
             INPUT_FILE --outfile OUTPUT_FILE 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --inpcol INPUT_OBJECT_COLUMN 
                         Name of the column in input that contains the objects 
   --outcol OUTPUT_COLUMN 
                         Column name where filenames need to be inserted 
   --file INPUT_FILE     Input csv file 
   --outfile OUTPUT_FILE 
                         Name of output csv file that has filename inserted

```

### Sub Command: `output`

Description: Get the output of a Job using jobid.
```
 rdac output --help

```
```
 Usage: output  [-h] --jobid JOBID [--tofile SAVE_TO_FILE] [--format DATA_FORMAT] 
             [--viz] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --jobid JOBID         Job ID (either partial or complete) 
   --tofile SAVE_TO_FILE 
                         Save the data to the specified file (CSV) 
   --format DATA_FORMAT  Format for the saved file. Valid values are auto, csv, 
                         json, parquet. If 'auto' format will be determined 
                         from extension 
   --viz                 Open Dataframe visualizer to show the data

```

### Sub Command: `pipeline`

Description: Pipeline management commands

**Following are the valid Sub-Commands for the Pipeline**

| Sub Commands | Description |
| --- | --- |
| list | List published pipelines |
| get-versions | Get versions for the pipeline |
| get | Get pipeline by name and version |
| delete | Delete pipeline by name and version |
| convert-to-json | Convert all pipelines in folder from yaml to json |
| publish | Publish the pipeline on a worker pod |
| published-run | Run a published pipeline on a worker pod |
```
 rdac pipeline --help

```
```
 Following are valid sub-commands for pipeline: 
   list                      List published pipelines 
   get-versions              Get versions for the pipeline 
   get                       Get pipeline by name and version 
   delete                    Delete pipeline by name and version 
   convert-to-json           Convert all pipelines in folder from yaml to json 
   publish                   Publish the pipeline on a worker pod 
   published-run             Run a published pipeline on a worker pod

```

****Sub Command: `list`****

Description: Get pipeline by name and version
```
 rdac pipeline-list --help

```
```
 usage: rdac [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```

*   Following is the syntax for **pipeline-list**
```
  rdac pipeline list
 ```

Example Output
```
 category                 description    name                                    saved_time                  usecase                                                              version 
 -----------------------  -------------  --------------------------------------  --------------------------  -------------------------------------------------------------------  -------------

```

****Sub Command: `get-versions`****

Description: Get versions for the pipeline
```
 rdac pipeline-get-versions --help

```
```
 Usage: pipeline-get-versions  [-h] --name NAME [--json] 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --name NAME  Get versions of pipeline specified by name 
   --json       Print detailed information in JSON format instead of tabular 
                format

```

*   Following is the syntax for **pipeline-get-versions**
```
 === "Example Output"

```

Versions

* * *

2022\_12\_09\_1

`
```
 <a name='pipeline-list'></a> 
 
 ### Sub Command: `pipeline-list` 
 
 Description: List published pipelines 
 
 ```bash 
 Usage: pipeline-list  [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format`
```

****Sub Command: `get`****

Description: Get pipeline by name and version
```
 rdac pipeline-get --help

```
```
 usage: rdac [-h] --name NAME --version VERSION [--tofile SAVE_TO_FILE] 
             [--json] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Pipeline name 
   --version VERSION     Pipeline version 
   --tofile SAVE_TO_FILE 
                         Save the downloaded pipeline to specified file 
   --json                Print detailed information in JSON format instead of 
                         tabular format

```

*   Following is the syntax for **pipeline-get**
```
 rdac pipeline get --name regression_metrics_data --version 2022_12_09_1

```

Example Output
```
 {'name': 'regression_metrics_data', 'description': 'test pipeline', 'usecase': '', 'category': '1', 'version': '2022_12_09_1', 'sources': {'files': {'name': 'files', 'type': 'file'}, 'cfxml': {'name': 'cfxml', 'type': 'cfxai_regression'}, 'rn': {'name': 'rn', 'type': 'rn'}}, 'data': {'name': 'regression_metrics_data', 'sequence': [{'tag': '@files:loadfile', 'query': "filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-prometheus-timeseries-data.csv'"}, {'tag': '@cfxml:regression', 'query': "value_column = 'value' and\nts_column = 'timestamp' and\nfrequency = '4H' and\nagg_func = 'mean'"}, {'tag': '@dm:change-time-format', 'query': "columns='timestamp' &\nfrom_format='datetimestr' &\nto_format='%Y-%m-%dT%H:%M:%S'", 'comment': 'Changing time format before writing to stream'}, {'tag': '@rn:write-stream', 'query': 'name = "regression_metrics_data"'}]}, 'artifacts': [{'artifact_type': 'rda-network-stream', 'artifact_name': 'regression_metrics_data', 'access': 'write'}], 'html_data': "\n        <style>\n\n        .tooltip {\n            position: relative;\n            display: inline-block;\n            border-bottom: 1px dotted black; /* If you want dots under the hoverable text */\n            }\n\n        /* Tooltip text */\n        .tooltip .tooltiptext {\n            visibility: hidden;\n            width: 120px;\n            background-color: black;\n            color: #fff;\n            text-align: center;\n            padding: 5px 0;\n            border-radius: 6px;\n            \n            /* Position the tooltip text - see examples below! */\n            position: absolute;\n

```   

****Sub Command: `delete`****

Description: Delete pipeline by name and version
```
 rdac pipeline-delete --help

```
```
 Usage: pipeline-delete  [-h] --name NAME --version VERSION 
 
 optional arguments: 
   -h, --help         show this help message and exit 
   --name NAME        Pipeline name 
   --version VERSION  Version for pipeline

```

*   Following is the syntax for **pipeline-delete**
```
  rdac pipeline delete --name nifty50_new --version 2023_01_10
 ```

Example Output
```
 2023-01-10:07:37:49 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-10:07:37:49 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-10:07:37:49 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Done deleting pipeline

```

****Sub Command: `convert-to-json`****

Description: Convert all pipelines in folder from yaml to json
```
 rdac pipeline convert-to-json --help

```
```
 usage: pipeline [-h] --pipetype PIPE_TYPE 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --pipetype PIPE_TYPE  Type of pipelines to convert : Published/Draft. It 
                         converts all pipelines in published/draft folder to 
                         json format.

```

*   Following is the syntax for **pipeline convert-to-json**
```
 rdac pipeline convert-to-json --pipetype Draft

```

Example Output
```
 2023-01-09:11:19:40 [1] INFO nats_client Creating new SharedPool ... 
 2023-01-09:11:19:40 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-01-09:11:19:40 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 
 Converted following pipelines from yaml to json 
 
     pipeline_name                                 version 
 --  ---------------------------------------  ------------ 
  0  all-stacks-join                          2022_09_28_1 
  1  appd_stack                               2022_09_28_1 
  2  appdynamics-enrichment                   2022_09_28_1 
  3  db_alerts_clustering                     2022_09_28_1 
  4  db_alerts_clustering                     2022_11_17_1 
  5  db_alerts_regression                     2022_09_28_1 
  6  db_alerts_regression                     2022_11_17_1 
  7  db_incidents_clustering                  2022_09_28_1 
  8  db_incidents_clustering                  2022_11_17_1 
  9  db_incidents_regression                  2022_09_28_1 
 10  db_incidents_regression                  2022_11_17_1 
 11  file_upload_alerts_clustering            2022_09_28_1 
 12  file_upload_alerts_clustering            2022_11_17_1 
 13  file_upload_incidents_clustering         2022_09_28_1 
 14  file_upload_incidents_clustering         2022_11_17_1 
 15  fileupload_alerts_regression             2022_09_28_1 
 16  fileupload_alerts_regression             2022_11_17_1 
 17  incident_notify_email                    2022_09_28_1 
 18  incident_notify_jenkins                  2022_09_28_1 
 19  incident_notify_msteams                  2022_09_28_1 
 20  incident_stack_asset_attributes_mapping  2022_09_28_1 
 21  incident_stack_generator                 2022_09_28_1

```

****Sub Command: `publish`****

Description: Publish the pipeline on a worker pod
```
 rdac pipeline publish --help

```
```
 usage: rdac [-h] --pipeline PIPELINE --name NAME --version VERSION --category 
             CATEGORY [--usecase USECASE] [--folder FOLDER] 
             [--group WORKER_GROUP] [--site WORKER_SITE] 
             [--lfilter LABEL_FILTER] [--rfilter RESOURCE_FILTER] 
             [--maxwait MAX_WAIT] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --pipeline PIPELINE   File containing pipeline contents 
   --name NAME           Pipeline name 
   --version VERSION     Pipeline version 
   --category CATEGORY   Pipeline category 
   --usecase USECASE     Pipeline usecase 
   --folder FOLDER       Pipeline Folder 
   --group WORKER_GROUP  Deprecated. Use --site option. Specify a worker site 
                         name. If not specified, will use any available worker. 
   --site WORKER_SITE    Specify a worker site name. If not specified, will use 
                         any available worker. 
   --lfilter LABEL_FILTER 
                         CFXQL style query to narrow down workers using their 
                         labels 
   --rfilter RESOURCE_FILTER 
                         CFXQL style query to narrow down workers using their 
                         resources 
   --maxwait MAX_WAIT    Maximum wait time (seconds) for credential check to 
                         complete.

```

*   Following is the syntax for **pipeline publish**
```
 rdac pipeline publish --pipeline testpipelinenew --name nifty_fifty --version 2023_01_10 --category test

```

Example Output
```
 2023-01-10:09:04:06 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 { 
   "status": "started", 
   "reason": "", 
   "results": [], 
   "now": "2023-01-10T09:04:06.130688", 
   "status-subject": "tenants.ae144f67d2a24034ad6920ace6809763.worker.group.f4a56ba6388c.direct.88c26bbe", 
   "jobid": "fa81de86812f4770a0ff8b700749f934" 
 } 
 Waiting: 
 Publishing Pipeline: 
 Completed:

```

****Sub Command: `published-run`****

Description: Run a published pipeline on a worker pod
```
 rdac pipeline published-run --help

```
```
 usage: pipeline [-h] --name NAME --version VERSION [--group WORKER_GROUP] 
                 [--site WORKER_SITE] [--lfilter LABEL_FILTER] 
                 [--rfilter RESOURCE_FILTER] [--maxwait MAX_WAIT] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Pipeline name 
   --version VERSION     Pipeline version 
   --group WORKER_GROUP  Deprecated. Use --site option. Specify a worker site 
                         name. If not specified, will use any available worker. 
   --site WORKER_SITE    Specify a worker site name. If not specified, will use 
                         any available worker. 
   --lfilter LABEL_FILTER 
                         CFXQL style query to narrow down workers using their 
                         labels 
   --rfilter RESOURCE_FILTER 
                         CFXQL style query to narrow down workers using their 
                         resources 
   --maxwait MAX_WAIT    Maximum wait time (seconds) for credential check to 
                         complete.

```

*   Following is the syntax for **pipeline published-run**
```
 rdac pipeline published-run --name nifty_fifty --version 2023_01_10

```

Example Output
```
 2023-01-10:09:05:31 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 { 
   "status": "started", 
   "reason": "", 
   "now": "2023-01-10T09:05:31.126185", 
   "pipeline-name": "nifty_fifty", 
   "status-subject": "tenants.ae144f67d2a24034ad6920ace6809763.worker.group.f4a56ba6388c.direct.88c26bbe", 
   "jobid": "1ec46b3ad80d496380ad1f9eb73482eb", 
   "attributes": { 
     "is_draft": "no" 
   }, 
   "pipeline-checksums": { 
     "nifty_fifty": "785e1b5b" 
   } 
 } 
 Waiting: 
 Initializing: 
 Running: 
 Running: 
 Running: 
 Running: 
 Running: 
 Running: 
 Running: 
 Running: 
 Completed:

```

### Sub Command: `pods`

Description: List all pods for the current tenant
```
 rdac pods --help

```
```
 usage: rdac [-h] [--json] [--type POD_TYPE] [--versions] [--infra] [--apps] 
 
 optional arguments: 
   -h, --help       show this help message and exit 
   --json           Print detailed information in JSON format instead of 
                    tabular format 
   --type POD_TYPE  Show only the pods that match the specified pod type 
   --versions       Show versions for each pod in tabular format, not 
                    compatible with --json option 
   --infra          List only RDA Infra pods. not compatible with --apps option 
   --apps           List only RDA App pods. not compatible with --infra option

```

*   Following is the syntax for **pods**
```
 rdac pods --type worker --json

```

Example Output
```
 2023-01-10:10:37:12 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 [ 
     { 
         "now": "2023-01-10T10:37:12.289225", 
         "started_at": "2023-01-07T13:30:42.380413", 
         "pod_type": "worker", 
         "pod_category": "rda_infra", 
         "pod_id": "88c26bbe", 
         "hostname": "05969789d903", 
         "proc_id": 10, 
         "labels": { 
             "rda_platform_version": "22.12.8.3", 
             "rda_messenger_version": "22.12.19.1", 
             "rda_pod_version": "22.12.14", 
             "rda_license_valid": "no", 
             "rda_license_not_expired": "no", 
             "rda_license_expiration_date": "" 
         }, 
         "build_tag": "daily", 
         "requests": { 
             "auto": "tenants.ae144f67d2a24034ad6920ace6809763.worker.group.f4a56ba6388c.auto", 
             "direct": "tenants.ae144f67d2a24034ad6920ace6809763.worker.group.f4a56ba6388c.direct.88c26bbe" 
         }, 
         "resources": { 
             "cpu_count": 4, 
             "cpu_load1": 6.7, 
             "cpu_load5": 7.08, 
             "cpu_load15": 7.14, 
             "mem_total_gb": 39.16, 
             "mem_available_gb": 15.34, 
             "mem_percent": 60.8,

```\
\
### Sub Command: `pod-logging`\
\
**Following are the valid Sub-Commands for the pod-logging**\
\
| Sub Commands | Description |\
| --- | --- |\
| get | Get logging configuration of given pod |\
| set | Update the logging level of a logging component for a given RDA Pod |\
| handler-set | Update the logging level of a handler for a given RDA Pod |\
| handler-get | Get all logging handlers and handler configuration for a given RDA Pod |\
\
```
 rdac pod-logging --help

```\
\
```
 pod logging commands 
 
 Following are valid sub-commands for pod-logging: 
   get                       Get logging configuration of given pod 
   set                       Update the logging level of a logging component for a given RDA Pod 
   handler-set               Update the logging level of a handler for a given RDA Pod 
   handler-get               Get all logging handlers and handler configuration for a given RDA Pod

```\
\
****Sub Command: `get`****\
\
Description: Get logging configuration of given pod\
\
```
 rdac pod-logging get --help

```\
\
```
 usage: pod-logging [-h] --id POD_ID [--logger LOGGER_NAME] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --id POD_ID           pod_id of the pod for which the logging level need to 
                         be retrieved 
   --logger LOGGER_NAME  Logging Name. By default it sets the root logger.

```\
\
****Sub Command: `set`****\
\
Description: Update the logging level of a logging component for a given RDA Pod\
\
```
 rdac pod-logging set --help

```\
\
```
 usage: pod-logging [-h] --id POD_ID --level LEVEL [--logger LOGGER_NAME] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --id POD_ID           pod_id of the pod for which the logging level need to 
                         be configured 
   --level LEVEL         Logging level. Must be one of DEBUG INFO WARNING ERROR 
                         CRITICAL 
   --logger LOGGER_NAME  Logging Name. By default it sets the root logger.

```\
\
*   Following is the Syntax for **pod-logging set**\
\
```
 rdac set-pod-log-level --id <required pod id> --level <required log level>

```\
\
Example Output\
\
```
 rdac set-pod-log-level --id 07a337e5 --level DEBUG 
 Successfully updated logging level for pod 07a337e5

```\
\
****Sub Command: `handler-set`****\
\
Description: Update the logging level of a handler for a given RDA Pod\
\
```
 rdac pod-logging handler-set --help

```\
\
```
 usage: pod-logging [-h] --id POD_ID --level LEVEL [--handler HANDLER_NAME] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --id POD_ID           pod_id of the pod for which the logging level need to 
                         be configured 
   --level LEVEL         Logging level. Must be one of DEBUG INFO WARNING ERROR 
                         CRITICAL 
   --handler HANDLER_NAME 
                         Logging Handler name. (e.g. console/file_handler) as 
                         specified in logging configuration file. If not 
                         specified, all the handlers will be set to the level 
                         provided.

```\
\
*   Following is the Syntax for **pod-logging handler-set**\
\
```
 rdac pod-logging handler-set --id <required pod id> --level <required log level>

```\
\
Example Output\
\
```
 rdac pod-logging handler-set --id 07a337e5 --level DEBUG 
 Successfully updated logging level for pod 07a337e5

```\
\
****Sub Command: `handler-get`****\
\
Description: Get all logging handlers and handler configuration for a given RDA Pod\
\
```
 rdac pod-logging handler-get --help

```\
\
```
 usage: pod-logging [-h] --id POD_ID 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --id POD_ID  pod_id of the pod for which the logging level need to be 
                retrieved

```\
\
### Sub Command: `pod-logging-handler-set`\
\
Description: To change log levels for any required pod\
\
```
 rdac pod-logging-handler-set --help

```\
\
```
 usage: rdac [-h] --id POD_ID --level LEVEL [--handler HANDLER_NAME] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --id POD_ID           pod_id of the pod for which the logging level need to 
                         be configured 
   --level LEVEL         Logging level. Must be one of DEBUG INFO WARNING ERROR 
                         CRITICAL 
   --handler HANDLER_NAME 
                         Logging Handler name. (e.g. console/file_handler) as 
                         specified in logging configuration file. If not 
                         specified, all the handlers will be set to the level 
                         provided.

```\
\
### Sub Command: `project`\
\
**Following are the valid Sub-Commands for the project**\
\
| Sub Commands | Description |\
| --- | --- |\
| add | Add or update project |\
| get | Get YAML data for a project |\
| list | List all projects |\
| delete | Delete a project |\
| enable | Change the status of a project to 'enabled' |\
| disable | Change the status of a project to 'disabled' |\
\
```
 rdac project --help

```\
\
```
 Project management commands. Projects can be used to link different tenants / projects from this RDA Fabric or a remote RDA Fabric. 
 
 Following are valid sub-commands for project: 
   add                       Add or update project 
   get                       Get YAML data for a project 
   list                      List all projects 
   delete                    Delete a project 
   enable                    Change the status of a project to 'enabled' 
   disable                   Change the status of a project to 'disabled'

```\
\
****Sub Command: `add`****\
\
Description: Add or update project\
\
```
 rdac project add --help

```\
\
```
 usage: project [-h] --file INPUT_FILE [--overwrite] [--rda_config RDA_CONFIG] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --file INPUT_FILE     YAML file containing project definition 
   --overwrite           Overwrite even if a project already exists with the 
                         specified name. 
   --rda_config RDA_CONFIG 
                         JSON file containing RDA Credentials (if the project 
                         belongs to a remote system)

```\
\
*   Following is the syntax for **project add**\
\
```
 rdac project add --file projecttest.yml

```\
\
Example Output\
\
```
 Added project oia-2

```\
\
Note\
\
Create a project YAML file before adding a new project\
\
Sample Project YAML File\
\
```
 name: "oia-2" 
 customerId: "3edd7c702f5d442982dfcd493d2fe7b3" 
 projectId: "3f9ef108-62b8-46d3-bc9e-caee1c53c174" 
 userId: "acme@cfx.com" 
 label: "ACME 2"

```\
\
****Sub Command: `list`****\
\
Description: List all projects\
\
```
 rdac project list --help

```\
\
```
 usage: project [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```\
\
\* Following is the syntax for **project list**\
\
```
 rdac project list

```\
\
Example Output\
\
```
     name    label          enabled    customerId    projectId    tenant_id    nats_url    minio_host    saved_time 
 --  ------  -------------  ---------  ------------  -----------  -----------  ----------  ------------  -------------------------- 
  0  n-bank  National Bank  yes        ae144f**      c2b89a**                                            2022-09-28T05:50:06.285929 
  1  oia-2   ACME 2         no         3edd7c**      3f9ef1**                                            2023-01-23T05:11:28.716514
 ```\
\
****Sub Command: `enable`****\
\
Description: Change the status of a project to 'enabled'\
\
```
 rdac project enable --help

```\
\
```
 usage: project [-h] --name PROJECT_NAME 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --name PROJECT_NAME  Name of the project

```\
\
\* Following is the syntax for **project enable**\
\
```
 rdac project enable --name oia-2

```\
\
Example Output\
\
```
 Changed status of oia-2 to enabled

```\
\
****Sub Command: `disable`****\
\
Description: Change the status of a project to 'disabled'\
\
```
 rdac project disable --help

```\
\
```
 usage: project [-h] --name PROJECT_NAME 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --name PROJECT_NAME  Name of the project

```\
\
\* Following is the syntax for **project disable**\
\
```
 rdac project disable  --name oia-2

```\
\
Example Output\
\
```
 Changed status of oia-2 to disabled

```\
\
****Sub Command: `get`****\
\
Description: Get YAML data for a project\
\
```
 rdac project get --help

```\
\
```
 usage: project [-h] --name PROJECT_NAME 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --name PROJECT_NAME  Name of the project

```\
\
\* Following is the syntax for **project get**\
\
```
 rdac project get --name oia-2

```\
\
Example Output\
\
```
 name: oia-2 
 customerId: 3edd7c702f5d442982dfcd493d2fe7b3 
 projectId: 3f9ef108-62b8-46d3-bc9e-caee1c53c174 
 userId: acme@cfx.com 
 label: ACME 2 
 saved_time: '2023-01-23T05:11:28.716514' 
 enabled: false

```\
\
****Sub Command: `delete`****\
\
Description: Delete a project\
\
```
 rdac project delete --help

```\
\
```
 usage: project [-h] --name PROJECT_NAME 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --name PROJECT_NAME  Name of the project to delete

```\
\
*   Following is the syntax for **project delete**\
\
```
 rdac project delete --name oia-2

```\
\
Example Output\
\
```
 Deleted project: oia-2

```\
\
### Sub Command: `pstream`\
\
**Following are the valid Sub-Commands for the pstream**\
\
| Sub Commands | Description |\
| --- | --- |\
| list | List persistent streams |\
| status | Status of the persistent streams |\
| get | Get information about a persistent stream |\
| metadata | Get metadata information about a persistent stream |\
| add | Add a new persistent stream |\
| delete | Delete a persistent stream |\
| query | Query persistent stream data via collector |\
| delete-by-query | Delete persistent stream data via CFXQL query |\
| update-by-query | Update column(s) in persistent stream data via CFXQL query |\
| add-column | Add column to the persistent stream records that don't have it and set a value via expression |\
| tail | Query a persistent stream and continue to query for incremental data every few seconds |\
| export | Query a persistent stream and export data to CSV or JSON file |\
| export-chunks | Query a persistent stream and export data as minio chunks |\
| migrate | Query a persistent stream and export to another stream with optional type conversion |\
| load | Load data from a CSV file into a persistent stream with optional type conversion |\
| ingest | Ingest data to persistent stream by directly adding data to Opensearch |\
| evict | Evict ingestion Job |\
| evict-export | Evict Export Chunks Job |\
\
```
 rdac pstream --help

```\
\
```
 Persistent Stream management commands 
 
 Following are valid sub-commands for pstream: 
 
   list                      List persistent streams 
   status                    Status of the persistent streams 
   get                       Get information about a persistent stream 
   metadata                  Get metadata information about a persistent stream 
   add                       Add a new Persistent stream 
   delete                    Delete a persistent stream 
   query                     Query persistent stream data via collector 
   delete-by-query           Delete persistent stream data via CFXQL query 
   update-by-query           Update column(s) in persistent stream data via CFXQL query 
   add-column                Add column to the persistent stream records that don't have it and set a value via expression 
   tail                      Query a persistent stream and continue to query for incremental data every few seconds 
   export                    Query a persistent stream and export data to CSV or JSON file 
   export-chunks             Query a persistent stream and export data as minio chunks 
   migrate                   Query a persistent stream and export to another stream with optional type conversion 
   load                      Load data from a CSV file into a persistent stream with optional type conversion 
   ingest                    Ingest data to pstream by directly adding data to Open Search 
   evict                     Evict Ingestion Job 
   evict-export              Evict Export Chunks Job

```\
\
****Sub Command: `list`****\
\
Description : List persistent streams\
\
```
 rdac pstream list --help

```\
\
```
 usage: pstream [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```\
\
*   Following is the syntax for **pstream list**\
\
```
 rdac pstream list

```\
\
Example Output One\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
     name                                       index_name                                                                                  saved_time                  retention_days 
 --  -----------------------------------------  ------------------------------------------------------------------------------------------  --------------------------  ---------------- 
  0  rda_synthetic_metrics                      f92bc678629540f0bcaf7749177acccb-stream-03e632e0-rda_synthetic_metrics                      2022-11-15T04:15:41.692800  31 
  1  oia-incidents-data-coll-stream             f92bc678629540f0bcaf7749177acccb-stream-09c0c9b9-oia-incidents-data-coll-stream             2022-11-14T10:39:14.080246  7 
  2  rdaf_services_logs                         f92bc678629540f0bcaf7749177acccb-stream-rdaf_services_logs                                  2022-11-14T10:29:40.564683  15 
  3  dli-synthetic-logs-processed               f92bc678629540f0bcaf7749177acccb-stream-10fe40a6-dli-synthetic-logs-processed               2022-11-14T15:33:16.490331  31 
  4  test_oia-incident-inserts-pstream          f92bc678629540f0bcaf7749177acccb-stream-1eb8a4d3-test_oia-incident-inserts-pstream          2022-12-05T07:22:48.543676  7 
  5  oia-incidents-collaboration-stream         f92bc678629540f0bcaf7749177acccb-stream-23f2f83a-oia-incidents-collaboration-stream         2022-11-14T10:36:52.070142  7 
  6  dli-log-stats                              f92bc678629540f0bcaf7749177acccb-stream-25235c4a-dli-log-stats                              2022-11-14T15:33:16.356427  90

```\
\
*   Another example syntax for **pstream list**\
\
```
 rdac pstream list --json

```\
\
Example Output Two\
\
```
 { 
     "attrs": { 
       "unique_keys": [ 
         "name" 
       ], 
       "system_defined": "yes" 
     }, 
     "datastore_type": "OS", 
     "index_name": "cf75a3efaa26491b9efea482d2ac981c-stream-01970753-rda_secrets_meta", 
     "name": "rda_secrets_meta", 
     "saved_time": "2023-11-08T07:45:44.541749", 
     "status": "Running" 
   },

```\
\
****Sub Command: `status`****\
\
Description : Status of the persistent streams\
\
```
 rdac pstream status --help

```\
\
```
 usage: pstream [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```\
\
*   Following is the syntax for **pstream status**\
\
```
 rdac pstream status

```\
\
Example Output One\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
     name                                       index_exists      docs_count    size_in_bytes    shards_failed    shards_successful    shards_total  status 
 --  -----------------------------------------  --------------  ------------  ---------------  ---------------  -------------------  --------------  -------- 
  0  rda_synthetic_metrics                      True                  100000         10929315                0                    3               6  OK 
  1  oia-incidents-data-coll-stream             True                       0              690                0                    3               6  OK 
  2  rdaf_services_logs                         True                17733976       8751155216                0                    3               6  OK 
  3  dli-synthetic-logs-processed               True                 4964025        697988506                0                    3               6  OK 
  4  test_oia-incident-inserts-pstream          True                       0              690                0                    3               6  OK 
  5  oia-incidents-collaboration-stream         True                       0              690                0                    3               6  OK 
  6  dli-log-stats                              True                 1028976         77565766                0                    3               6  OK 
  7  regression-aggregated-anomalies            True                    2529           731537                0                    3               6  OK 
  8  oia-incidents-delta-stream                 True                       0              690                0                    3               6  OK 
  9  dli-synthetic-logs-dropped                 True                       0            71681                0                    3               6  OK 
 10  oia-alerts-kpi-stream                      True                      44            26682                0                    3               6  OK

```\
\
*   Another example syntax for **pstream status**\
\
```
 rdac pstream status --json

```\
\
Example Output Two\
\
```
 { 
   "status": "ok", 
   "reason": "", 
   "data": [ 
     { 
       "name": "rda_secrets_meta", 
       "datastore_type": "OS", 
       "index_exists": true, 
       "docs_count": 0, 
       "size_in_bytes": 624, 
       "shards_total": 6, 
       "shards_successful": 3, 
       "shards_failed": 0, 
       "status": "OK" 
     },

```\
\
****Sub Command: `get`****\
\
Description : Get information about a persistent stream\
\
```
 rdac pstream get --help

```\
\
```
 usage: pstream [-h] --name NAME [--json] 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --name NAME  Persistent Stream name 
   --json       Print in JSON format instead of text format

```\
\
*   Following is the syntax for **pstream get**\
\
```
 rdac pstream get --name  test_oia-incident-inserts-pstream

```\
\
Example Output One\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
 Stream Name: test_oia-incident-inserts-pstream 
 Index  Name: f92bc678629540f0bcaf7749177acccb-stream-1eb8a4d3-test_oia-incident-inserts-pstream 
 Saved Time : 2022-12-05T07:22:48.543676 
 Attributes 
   retention_days: 7 
   unique_keys: ['project_id'] 
   timestamp: timestamp

```\
\
*   Another example syntax for **pstream get**\
\
```
 rdac pstream get --name oia-metrics-data --json

```\
\
Example Output Two\
\
```
 { 
   "name": "oia-metrics-data", 
   "datastore_type": "OS", 
   "attrs": { 
     "case_insensitive": true, 
     "unique_keys": [ 
       "asset_id", 
       "metric_id", 
       "metric_source", 
       "metric_timestamp" 
     ], 
     "retention_days": "90" 
   }, 
   "saved_time": "2023-11-08T09:10:06.755111", 
   "index_name": "cf75a3efaa26491b9efea482d2ac981c-stream-08d2fd46-oia-metrics-data", 
   "status": "Running" 
 }

```\
\
****Sub Command: `metadata`****\
\
Description : Get metadata information about a persistent stream\
\
```
 rdac pstream metadata --help

```\
\
```
 usage: pstream [-h] --name NAME [--json] 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --name NAME  Persistent Stream name 
   --json       Print in JSON format instead of text format

```\
\
*   Following is the syntax for **pstream metadata**\
\
```
 rdac pstream metadata --name rda_synthetic_metrics

```\
\
Example Output\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
     columnId             keywordColumn        mappedType    parent       type 
 --  -------------------  -------------------  ------------  -----------  ------- 
  0  component.keyword                         TEXT          component    keyword 
  1  component            component.keyword    TEXT                       text 
  2  count_                                    DOUBLE                     long 
  3  layer.keyword                             TEXT          layer        keyword 
  4  layer                layer.keyword        TEXT                       text 
  5  metric_name.keyword                       TEXT          metric_name  keyword 
  6  metric_name          metric_name.keyword  TEXT                       text 
  7  node_id.keyword                           TEXT          node_id      keyword 
  8  node_id              node_id.keyword      TEXT                       text 
  9  node_label.keyword                        TEXT          node_label   keyword 
 10  node_label           node_label.keyword   TEXT                       text 
 11  node_type.keyword                         TEXT          node_type    keyword 
 12  node_type            node_type.keyword    TEXT                       text 
 13  source_tool.keyword                       TEXT          source_tool  keyword 
 14  source_tool          source_tool.keyword  TEXT                       text 
 15  stack_name.keyword                        TEXT          stack_name   keyword 
 16  stack_name           stack_name.keyword   TEXT                       text 
 17  timestamp                                 DATETIME                   date 
 18  unit.keyword                              TEXT          unit         keyword 
 19  unit                 unit.keyword         TEXT                       text 
 20  value                                     DOUBLE                     float

```\
\
****Sub Command: `add`****\
\
Description : Add a new Persistent stream\
\
```
 rdac pstream add --help

```\
\
```
 usage: pstream [-h] --name NAME [--index INDEX_NAME] 
                [--attr [ATTRS [ATTRS ...]]] [--retention_days RETENTION_DAYS] 
                [--unique_keys UNIQUE_KEYS] [--auto_expand AUTO_EXPAND] 
                [--drop DROP] [--computed COMPUTED] [--timestamp TIMESTAMP] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Persistent Stream name 
   --index INDEX_NAME    OpenSearch index name to store Persistent Stream 
   --attr [ATTRS [ATTRS ...]] 
                         Optional name=value pairs to add to attributes of 
                         persistent stream 
   --retention_days RETENTION_DAYS 
                         Number of days to retain the data 
   --unique_keys UNIQUE_KEYS 
                         Comma separated list of column names to make each row 
                         unique 
   --auto_expand AUTO_EXPAND 
                         Comma separated list of column names that should 
                         parsed as JSON dicts and expanded 
   --drop DROP           Comma separated list of column names that should be 
                         dropped before persisting 
   --computed COMPUTED   JSON fille containing computed column definition 
   --timestamp TIMESTAMP 
                         Timestamp column name

```\
\
*   Following is the syntax for **pstream add**\
\
```
 rdac pstream add --name test_oia-incident-inserts-pstream --retention_days 7 --unique_keys project_id --timestamp timestamp

```\
\
Example Output One\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
 { 
   "retention_days": 7, 
   "unique_keys": [ 
     "project_id" 
   ], 
   "timestamp": "timestamp" 
 } 
 Persistent stream saved.

```\
\
\* Following is the syntax for **pstream add with attr, auto\_expand & Compute**\
\
```
 rdac pstream add --name oia-incidents-stream --attr 'retention_days=1' --auto_expand "resolved_at,created" --computed test.json

```\
\
Example Output Two\
\
```
 { 
   "retention_days": "1", 
   "auto_expand": [ 
     "resolved_at", 
     "created" 
   ], 
   "search_case_insensitive": true, 
   "computed_columns": { 
     "ttr_minutes": { 
       "expr": "(resolved_at - created)/(1000.0*60)", 
       "default": null 
     }, 
     "created_iso": { 
       "expr": "ms_to_isoformat(created)" 
     }, 
     "resolved_at_iso": { 
       "expr": "ms_to_isoformat(resolved_at)" 
     } 
   } 
 } 
 Persistent stream saved.

```\
\
When a pstream is created, the corresponding Index name is automatically generated and created. Please run `rdac pstream list` to see the associated Index name.\
\
Index name has below format.\
\
`<tenant_id>-stream-<random_id>-<pstream-name>`\
\
Below is an example of system generated Index name as part of pstream creation.\
\
`79cc72a1697b487fb2da7b99f0a0cc1a-stream-09c0c9b9-oia-incidents-data-coll-stream`\
\
`pstream add` also supports creating user defined Index name, however, the Index name should always be pre-fixed with tenant-id as shown above.\
\
Organization ID can be found at **RDAF UI portal** --> **Main Menu** --> **Configuration** --> **RDA Admin** --> **Network**\
\
![your-image-description](https://bot-docs.cloudfabrix.io/images/rdaf_fabric_tenant_config.png)\
\
*   Following is the syntax for **pstream add** with user specified Index name.\
\
```
 rdac pstream add --name server_cpu_metrics --retention_days 7 --timestamp timestamp --index 79cc72a1697b487fb2da7b99f0a0cc1a-stream-server_cpu_metrics

```\
\
Warning\
\
Index name always should start with Organization ID. If Organization id is not prefixed as part of user defined index name, the data ingestion into pstream will be failed with permission errors.\
\
****Sub Command: `delete`****\
\
Description : Delete a persistent stream\
\
```
 rdac pstream delete --help

```\
\
```
 usage: pstream [-h] --name NAME [--delete_index] 
 
 optional arguments: 
   -h, --help      show this help message and exit 
   --name NAME     Persistent Stream name 
   --delete_index  Delete all the data and metadata from open search

```\
\
*   Following is the syntax for **pstream delete**\
\
```
 rdac pstream delete --name test_oia-incident-inserts-pstream

```\
\
Example Output\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
 Deleted persistent stream

```\
\
By default, `pstream delete` will not delete the associated Index which contains the data. If associated Index also to be deleted along with the persistent steam, use `--delete_index` option.\
\
Danger\
\
Please be aware that `--delete_index` deletes the persistent stream's index permanently which contains the data.\
\
****Sub Command: `query`****\
\
Description : Query persistent stream data via collector\
\
```
 rdac pstream query --help

```\
\
```
 usage: pstream [-h] --name NAME [--max_rows MAX_ROWS] [--query CFXQL_QUERY] 
                [--aggs AGGS] [--groupby GROUPBY] [--sortby SORT_BY] 
                [--order SORT_ORDER] [--ts TS_COLUMN] [--json] [--no_sort] 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --name NAME          Persistent Stream name 
   --max_rows MAX_ROWS  Max rows in output 
   --query CFXQL_QUERY  CFXQL Query 
   --aggs AGGS          Optional aggs, specified as 'sum:field_name' 
   --groupby GROUPBY    Comma separated list of columns to groupby. Used only 
                        when --aggs is used 
   --sortby SORT_BY     Comma separated list of columns to sort by. Default is 
                        timestamp column. 
   --order SORT_ORDER   Sort oder. Must be one 'asc' or 'desc'. Default is 
                        'desc' 
   --ts TS_COLUMN       Timestamp column for sorting. Default is 'timestamp' 
   --json               Print detailed information in JSON format instead of 
                        tabular format 
   --no_sort            Do not sort by timestamp field

```\
\
*   Following is the syntax for **pstream query**\
\
```
 pstream query --name rda_synthetic_metrics --query "* GET metric_name" --max 5

```\
\
Example Output One\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
     metric_name 
 --  ------------------------------ 
  0  host_cpu_usage 
  1  host_mem_usage 
  2  transaction_time 
  3  shared_svc_total_response_time 
  4  total_response_time

```\
\
Query persistent stream with CFXQL filters, in this example, querying the data and get one of the data record within last 5 mins. Since `@timestamp` has special character, it need to be escaped as shown below.\
\
`
```
 rdac pstream query --name rdaf_services_logs --json --query '"\`@timestamp\`" is after -5min' --max_rows 1`
```\
\
Example Output Two\
\
```
 [ 
   { 
     "_id": "BjhB7oQBXeLk1V97kTCm", 
     "_index": "79cc72a1697b487fb2da7b99f0a0cc1a-stream-rdaf_services_logs", 
     "sort": [ 
       1670444585275, 
       "BjhB7oQBXeLk1V97kTCm" 
     ], 
     "_score": null, 
     "process_name": "systemd-networkd", 
     "log_message": "veth7809965: Gained IPv6LL", 
     "host": "10.95.101.175", 
     "service_category": "rda_infra_svcs", 
     "service_host": "rdaflogstream", 
     "hostname": "rdaflogstream", 
     "received_from": "10.95.101.175", 
     "log": "2022-12-07T20:23:05.275427+00:00 rdaflogstream systemd-networkd[1110]: veth7809965: Gained IPv6LL", 
     "log_severity": "UNKNOWN", 
     "service_name": "rda_os_syslog", 
     "@timestamp": "2022-12-07T20:23:05.275Z", 
     "@version": "1", 
     "fluentbit_timestamp": "2022-12-07T20:23:05.275Z", 
     "process_id": "1110" 
   } 
 ]

```\
\
Below is another example of CFXQL query when the column name `service-category` has a special character.\
\
`
```
 rdac pstream query --name rdaf_services_logs --json --query '"\`@timestamp\`" is after -5min and "\`service-category\`" = "rda_infra_svcs"' --max_rows 1`
```\
\
Tip\
\
When using CFXQL, column names that has special characters such as `@` `-`, need to be escaped as shown in the above examples.\
\
Below is another example of **aggs & groupby** arguments when the column name is `service_name`.\
\
`
```
 rdac pstream query --name rdaf_services_logs --ts @timestamp --query '"\`@timestamp\`" is after -1d and log_severity = 'ERROR' get service_name,log' --aggs value_count:_id --groupby service_name`
```\
\
Example Output Three\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
  Series 
    * Label: _id_value_count 
      Values 
        * Value: 39,918 
 
      Group: rda_nats 
 
    * Label: _id_value_count 
      Values 
        * Value: 5,412 
 
      Group: rda_scheduler 
 
    * Label: _id_value_count 
      Values 
        * Value: 72 
 
      Group: rda_file_browser 
 
    * Label: _id_value_count 
      Values 
        * Value: 48 
 
      Group: rda_resource_manager

```\
\
Below is another example of **sum aggregation** of the column name `duration`.\
\
```
 python3 rdac.py pstream query --name rda_microservice_traces --aggs sum:duration --groupby source --order asc

```\
\
Example Output Four\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
  Series 
    * Label: duration_sum 
      Values 
        * Value: 270,762.0 
 
      Group: scheduler 
 
    * Label: duration_sum 
      Values 
        * Value: 166,608.0 
 
      Group: dataset-caas 
 
    * Label: duration_sum 
      Values 
        * Value: 44,937.0 
 
      Group: api-server 
 
    * Label: duration_sum 
      Values 
        * Value: 81,265.0 
 
      Group: cfxdimensions-app-file-browser

```\
\
Below is another example of **value count** aggregation of the column name `Maths`.\
\
```
 rdac pstream query --name sample-test-scores --aggs 'value_count:Maths' --groupby section

```\
\
Example Output Five\
\
```
 Series 
    * Label: Maths_value_count 
      Values 
        * Value: 5 
 
      Group: A 
 
    * Label: Maths_value_count 
      Values 
        * Value: 5 
 
      Group: B

```\
\
Below is another example of **cardinality** aggregation of the column name `Maths`.\
\
```
 rdac pstream query --name sample-test-scores --aggs 'cardinality:Maths' --groupby section

```\
\
Example Output Six\
\
```
 Series 
    * Label: Maths_cardinality 
      Values 
        * Value: 5 
 
      Group: A 
 
    * Label: Maths_cardinality 
      Values 
        * Value: 4 
 
      Group: B

```\
\
Below is another example of **avg** aggregation of the column name `Maths`.\
\
```
 rdac pstream query --name sample-test-scores --aggs 'avg:Maths' --groupby section

```\
\
Example Output Seven\
\
```
 Series 
    * Label: Maths_avg 
      Values 
        * Value: 57.6 
 
      Group: A 
 
    * Label: Maths_avg 
      Values 
        * Value: 77.8 
 
      Group: B

```\
\
Below is another example of **max** aggregation of the column name `Maths`.\
\
```
 rdac pstream query --name sample-test-scores --aggs 'max:Maths' --groupby section

```\
\
Example Output Eight\
\
```
 Series 
    * Label: Maths_max 
      Values 
        * Value: 87.0 
 
      Group: A 
 
    * Label: Maths_max 
      Values 
        * Value: 90.0 
 
      Group: B

```\
\
****Sub Command: `delete-by-query`****\
\
Description: Delete persistent stream data via CFXQL query\
\
```
 rdac pstream delete-by-query -h

```\
\
```
 usage: pstream [-h] --name NAME --query CFXQL_QUERY [--timeout TIMEOUT] 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --name NAME          Persistent Stream name 
   --query CFXQL_QUERY  CFXQL Query 
   --timeout TIMEOUT    Timeout in seconds to wait for response. Default 60

```\
\
*   Following is the syntax for **pstream delete-by-query**\
\
```
 rdac pstream delete-by-query --name rda_logs_test --query 'artifact_name  is "login_post" and operation = "LOGIN"'

```\
\
Example Output\
\
```
 Deleted all the data that matched the query 
 {'status': 'ok', 'reason': '', 'data': {'took': 14, 'timed_out': False, 'total': 4, 'deleted': 4, 'batches': 1, 'version_conflicts': 0, 'noops': 0, 'retries': {'bulk': 0, 'search': 0}, 'throttled_millis': 0, 'requests_per_second': -1.0, 'throttled_until_millis': 0}, 'now': '2023-11-09T08:23:39.800946'}

```\
\
Warning\
\
`pstream delete-by-query` deletes the records from persistent stream, please make sure the given CFXQL query is appropriate to filter and delete the intended records. As a pre-caution, use `pstream query` with CFXQL filter to validate the query results before running `pstream delete-by-query` command.\
\
****Sub Command: `update-by-query`****\
\
Description: Update column(s) in persistent stream data via CFXQL query\
\
```
 rdac pstream update-by-query -h

```\
\
```
 usage: pstream [-h] --name NAME --query CFXQL_QUERY --columns COLUMNS --values 
                VALUES [--timeout TIMEOUT] 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --name NAME          Persistent Stream name 
   --query CFXQL_QUERY  CFXQL Query 
   --columns COLUMNS    Comma separated list of column names that needs to be 
                        updated for all the records that match the query. 
                        Example: city,state,zipcode 
   --values VALUES      Set the value to specified column or columns (comma 
                        separated). The specified number of columns should 
                        match 'columns' column(s). Example: San Jose,CA,12345 
   --timeout TIMEOUT    Timeout in seconds to wait for response. Default 60

```\
\
*   Following is the syntax for **pstream update-by-query**\
\
```
 rdac pstream update-by-query --name rda_logs_test --query 'artifact_name  is "login_post"' --columns artifact_name --values 'login_test1'

```\
\
Example Output One\
\
```
 Updated all the data that matched the query 
 {'status': 'ok', 'reason': '', 'data': {'took': 578, 'timed_out': False, 'total': 2, 'updated': 2, 'deleted': 0, 'batches': 1, 'version_conflicts': 0, 'noops': 0, 'retries': {'bulk': 0, 'search': 0}, 'throttled_millis': 0, 'requests_per_second': -1.0, 'throttled_until_millis': 0, 'failures': []}, 'now': '2023-11-09T08:38:54.026199'}

```\
\
\* Following is the syntax for **pstream update-by-query with multiple `columns`**\
\
```
 rdac pstream update-by-query --name sample-test-scores --query 'name  is "tej"' --columns "Maths,english" --values "85,54"

```\
\
example Output Two\
\
```
 Updated all the data that matched the query 
 {'status': 'ok', 'reason': '', 'data': {'took': 22, 'timed_out': False, 'total': 1, 'updated': 1, 'deleted': 0, 'batches': 1, 'version_conflicts': 0, 'noops': 0, 'retries': {'bulk': 0, 'search': 0}, 'throttled_millis': 0, 'requests_per_second': -1.0, 'throttled_until_millis': 0, 'failures': []}, 'now': '2023-11-20T05:54:21.625365'}

```\
\
****Sub Command: `add-column`****\
\
Description: Add column to the persistent stream records that don't have it and set a value via expression\
\
```
 rdac pstream add-column -h

```\
\
```
 usage: pstream [-h] --name NAME --column COLUMN --expression EXPRESSION 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Persistent Stream name 
   --column COLUMN       Field name. Example: full_name 
   --expression EXPRESSION 
                         Open Search painless script. Example: 
                         "ctx._source['first_name'] + ' ' + 
                         ctx._source['last_name']"

```\
\
*   Following is the syntax for **pstream add-column**\
\
Run `rdac` command without arguments to enter into **rdac** command shell and followed by `pstream add-column` command as shown below.\
\
```
 rdac

``` \
\
```
 pstream add-column --name rda_logs_test --column artifact add --expression "ctx._source['artifact_type'] + ' ' + ctx._source['artifact_name']"

```\
\
Example Output\
\
```
 Added column 'artifactadd' for all the records that don't have it 
 {'status': 'ok', 'reason': '', 'data': {'took': 111, 'timed_out': False, 'total': 33, 'updated': 33, 'deleted': 0, 'batches': 1, 'version_conflicts': 0, 'noops': 0, 'retries': {'bulk': 0, 'search': 0}, 'throttled_millis': 0, 'requests_per_second': -1.0, 'throttled_until_millis': 0, 'failures': []}, 'now': '2023-11-09T10:59:28.158594'}

```\
\
Note\
\
When adding a new column using the `--expression` option, it uses Opensearch painless scripted language which will have special characters. To prevent issues with these special characters, it is recommended to execute this command within the `rdac` shell.\
\
****Sub Command: `tail`****\
\
Description : Query a persistent stream and continue to query for incremental data every few seconds\
\
```
 rdac pstream tail --help

```\
\
```
 usage: pstream [-h] --name NAME [--max_rows MAX_ROWS] [--query CFXQL_QUERY] 
                [--ts TS_COLUMN] [--format FORMAT] [--out_cols OUTPUT_COLUMNS] 
                [--json] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Persistent Stream name 
   --max_rows MAX_ROWS   Max rows in output for initial query 
   --query CFXQL_QUERY   CFXQL Query 
   --ts TS_COLUMN        Timestamp column for sorting. Default is 'timestamp' 
   --format FORMAT       Format string in {field1:<8} {field2:,.2f} style 
   --out_cols OUTPUT_COLUMNS 
                         Comma separated list of column names to be included in 
                         output. If not specified, all columns will be included 
   --json                Print detailed information in JSON format instead of 
                         tabular format

```\
\
`--query` supports CFXQL query. However it doesn't support `get` columns option.\
\
`--out_cols` use this option to get specific attributes from the pstream as shown in the above example.\
\
`--json` use this option to get the log output in JSON format. However, it doesn't support limiting the selective attributes listed under `--out_cols` option.\
\
*   Following is the syntax for **pstream tail**\
\
```
 rdac pstream tail --name rda_synthetic_metrics

```\
\
Example Output\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
 7 3hSAeYQBuQsspbunzGjR 1 Application Component app_vm_mem_usage 10.95.134.101_Webserver fin-web01 Webserver AppDynamics Online_Banking_Stack 2022-11-15T04:05:13.584582 % 60.48 
 8 3xSAeYQBuQsspbunzGjR 1 Application Component total_response_time 10.95.134.101_Webserver fin-web01 Webserver ThousandEyes Online_Banking_Stack 2022-11-15T04:05:13.584582 ms 65.72 
 9 4BSAeYQBuQsspbunzGjR 1 Application Component app_vm_cpu_usage 10.95.134.101_Webserver fin-web01 Webserver AppDynamics Online_Banking_Stack 2022-11-15T04:05:13.584582 % 69.24 
 4 2xSAeYQBuQsspbunzGjR 1 Application Component total_response_time 10.95.134.101_Webserver fin-web01 Webserver ThousandEyes Online_Banking_Stack 2022-11-15T04:05:13.921674 ms 29.11 
 5 3BSAeYQBuQsspbunzGjR 1 Application Component app_vm_cpu_usage 10.95.134.101_Webserver fin-web01 Webserver AppDynamics Online_Banking_Stack 2022-11-15T04:05:13.921674 % 69.28 
 6 3RSAeYQBuQsspbunzGjR 1 Application Component app_vm_mem_usage 10.95.134.101_Webserver fin-web01 Webserver AppDynamics Online_Banking_Stack 2022-11-15T04:05:13.921674 % 60.75 
 3 2hSAeYQBuQsspbunzGjR 1 Shared Service shared_svc_total_response_time app.okta.com app.okta.com IdentityProvider ThousandEyes Online_Banking_Stack 2022-11-15T04:05:16.339953 ms 50.31 
 2 2RSAeYQBuQsspbunzGjR 1 Application Component transaction_time 10.95.134.102_Appserver fin-app01 Appserver AppDynamics Online_Banking_Stack 2022-11-15T04:05:18.318154 ms 4.35 
 0 1xSAeYQBuQsspbunzGjR 1 Host host_cpu_usage 10.95.158.194_esxi esxi-server-04 EsxiHost VROps Online_Banking_Stack 2022-11-15T04:05:23.190271 % 78.13 
 1 2BSAeYQBuQsspbunzGjR 1 Host host_mem_usage 10.95.158.194_esxi esxi-server-04 EsxiHost VROps Online_Banking_Stack 2022-11-15T04:05:23.190271 % 69.05

```\
\
*   Below is an example of `pstream tail` with CFXQL query to filter and tail selected output column(s) specified with `--out_cols`\
\
```
 rdac pstream tail --name rdaf_services_logs --ts @timestamp --query "service_name = 'rda_registry'" --out_cols 'log'

```\
\
Example Output\
\
```
 2022-12-07:20:50:53 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 2022-12-07 20:50:51,245 [PID=9:TID=Thread-9:cfx.rda_messaging.nats_client:cb:1021] INFO - Sending request-reply to _INBOX.RZtDMglua05ndrDR200bGx.RZtDMglua05ndrDR200bJ8 
 
 2022-12-07 20:50:51,274 [PID=9:TID=Thread-10:cfx.rda_registry.registry_main:registry_requests:501] INFO - received registry request on subject tenants.79cc72a1697b487fb2da7b99f0a0cc1a.registry.auto: get-pods 
 
 2022-12-07 20:50:51,274 [PID=9:TID=Thread-10:cfx.rda_registry.registry_main:registry_requests:546] INFO - Returning 1 pods 
 
 2022-12-07 20:50:51,275 [PID=9:TID=Thread-10:cfx.rda_messaging.nats_client:cb:1021] INFO - Sending request-reply to _INBOX.AeVKdrtKiJGJtMSKQEfui2.AeVKdrtKiJGJtMSKQEfukt 
 ... 
 ...

```\
\
Tip\
\
When using CFXQL, column names that has special characters such as `@` `-`, need to be escaped. Please refer `pstream query` section for reference examples.\
\
****Sub Command: `export`****\
\
Description : Query a persistent stream and export data to CSV or JSON file\
\
```
 rdac pstream export --help

```\
\
```
 usage: pstream [-h] --name NAME [--max_rows MAX_ROWS] [--limit LIMIT] 
                [--query CFXQL_QUERY] [--ts TS_COLUMN] --to_file TO_FILE 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --name NAME          Persistent Stream name 
   --max_rows MAX_ROWS  Max rows in each batch 
   --limit LIMIT        Total limit on downloaded rows 
   --query CFXQL_QUERY  CFXQL Query 
   --ts TS_COLUMN       Timestamp column for sorting. Default is 'timestamp' 
   --to_file TO_FILE    Output filename (CSV or JSON)

```\
\
*   Following is the syntax for **pstream export**\
\
```
 rdac pstream export --name oia-alerts-stream --max_rows 100 --limit 100 --query "a_status is ACTIVE" --to_file ./test.csv

```\
\
Example Output\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
 Fetching offset 0, totalResults=?, limit=100 
 Completed download of 100 rows

```\
\
****Sub Command: `export-chunks`****\
\
Description: Query a persistent stream and export data as minio chunks\
\
```
 rdac pstream export-chunks --help

```\
\
```
 usage: pstream [-h] --name NAME [--query CFXQL_QUERY] [--limit LIMIT] 
                [--ts TS_COLUMN] 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --name NAME          Persistent Stream name 
   --query CFXQL_QUERY  CFXQL Query 
   --limit LIMIT        Total limit exported rows 
   --ts TS_COLUMN       Timestamp column for sorting. Default is 'timestamp'

```\
\
\* Following is the syntax for **pstream export-chunks**\
\
```
 rdac pstream export-chunks --name "rda_logs_test" --q

``` \
\
Example Output\
\
```
 "timestamp is after -2 days" 
 Check 'rda_system_collector_export_job_status' stream for updates for export job: rda_logs_test-6ebeeb88 
 Exiting out of LogRecordSocketReceiver. pid: 1. Socket file: /tmp/rdf_log_socket_2bef0dfa-8c71-466a-a592-25d33326b8c7

```\
\
****Sub Command: `migrate`****\
\
Description : Query a persistent stream and export to another stream with optional type conversion\
\
```
 rdac pstream migrate --help

```\
\
```
 usage: pstream [-h] --name NAME [--max_rows MAX_ROWS] [--limit LIMIT] 
                [--query CFXQL_QUERY] [--ts TS_COLUMN] --dest_stream 
                DEST_STREAM [--to_int TO_INT] [--to_float TO_FLOAT] 
                [--to_text TO_TEXT] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Persistent Stream name 
   --max_rows MAX_ROWS   Max rows in each batch 
   --limit LIMIT         Total limit on downloaded rows 
   --query CFXQL_QUERY   CFXQL Query 
   --ts TS_COLUMN        Timestamp column for sorting. Default is 'timestamp' 
   --dest_stream DEST_STREAM 
                         Output PStream name 
   --to_int TO_INT       Comma separated list of columns to be converted to int 
   --to_float TO_FLOAT   Comma separated list of columns to be converted to 
                         float 
   --to_text TO_TEXT     Comma separated list of columns to be converted to

```\
\
*   Following is the syntax for **pstream migrate**\
\
```
 rdac pstream migrate --name oia-incidents-stream --max_rows 100 --limit 100 --dest_stream test_pstream --to_int i_ttr_millis

```\
\
Example Output\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
 Fetching offset 0, totalResults=?, limit=100 
 Completed migration of 100 rows, with 0 mapping errors

```\
\
****Sub Command: `load`****\
\
Description : Load data from a CSV file into a persistent stream with optional type conversion\
\
```
 rdac pstream load --help

```\
\
```
 usage: pstream [-h] --name NAME --data DATA_FILE [--limit LIMIT] 
                [--filter CFXQL_QUERY] [--to_ts TO_TS] [--timestamp TIMESTAMP] 
                [--to_int TO_INT] [--to_float TO_FLOAT] [--to_text TO_TEXT] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Destination Persistent Stream name 
   --data DATA_FILE      Input data file (CSV) 
   --limit LIMIT         Total limit on published rows 
   --filter CFXQL_QUERY  CFXQL Query to apply on loaded dataframe before 
                         publishing 
   --to_ts TO_TS         Comma separated list of timestamp columns (ISO format) 
   --timestamp TIMESTAMP 
                         Create Timestamp column from a an existing column 
   --to_int TO_INT       Comma separated list of columns to be converted to int 
   --to_float TO_FLOAT   Comma separated list of columns to be converted to 
                         float 
   --to_text TO_TEXT     Comma separated list of columns to be converted to 
                         text

```\
\
*   Following is the syntax for **pstream load**\
\
```
 rdac pstream load --name rda_synthetic_metrics --data time_series_data_test.csv

```\
\
Example Output\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
 Reading input data file... 
 Input data file has 12 Rows and 9 Columns 
 Publishing 12 rows.. 
 Completed loading of 12 rows into stream rda_synthetic_metrics in 0.3 seconds

```\
\
****Sub Command: `ingest`****\
\
Description : Ingest data to pstream by directly adding data to Open Search\
\
```
 rdac pstream ingest --help

```\
\
```
 usage: pstream [-h] --name NAME [--minio_object_prefix MINIO_OBJECT_PREFIX] 
                [--local_directory LOCAL_DIRECTORY] 
                [--filename_pattern FILENAME_PATTERN] [--dataset DATASET] 
                [--num_rows NUM_ROWS] [--replace] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Destination Persistent Stream name 
   --minio_object_prefix MINIO_OBJECT_PREFIX 
                         Platform's minio object prefix. Example: /data/ 
   --local_directory LOCAL_DIRECTORY 
                         Local directory of input file. 
   --filename_pattern FILENAME_PATTERN 
                         File criteria in regex format. Only files with csv 
                         extension (or csv file compressesd as .gz file) are 
                         supported. Applicable if 'minio_object_prefix' or 
                         'local_directory' is provided 
   --dataset DATASET     Dataset name 
   --num_rows NUM_ROWS   Number of rows to fetch in each chunk 
   --replace             Delete any existing data in the index and load new 
                         data

```\
\
*   Following is the syntax for **pstream ingest**\
\
```
 rdac pstream ingest --name test_pstream --filename_pattern csv --dataset time_series_data_test --num_rows 100 --replace

```\
\
Example Output One\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
 Check 'rda_system_collector_ingestion_job_status' stream for updates for ingestion job: test_pstream-2115d970

```\
\
*   Following is the syntax for **pstream ingest --minio\_object\_prefix**\
\
```
 rdac pstream ingest --name demo-test --filename_pattern csv --dataset sample-test-scores --minio_object_prefix cfxdm-saved-data

```\
\
\=== Example Output Two\
\
```
 Check 'rda_system_collector_ingestion_job_status' stream for updates for ingestion job: demo-test-3824eb70

```\
\
****Sub Command: `evict`****\
\
Description : Evict Ingestion Job\
\
```
 usage: pstream [-h] --name NAME 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --name NAME  Ingestion Job name

```\
\
Note\
\
`evict` command will work only when the ingest job status is **Ingesting**. Ingestion job status is captured in **rda\_system\_collector\_ingestion\_job\_status** persistent stream.\
\
*   Following is the syntax to check **pstream ingestion status**\
\
```
 rdac.py pstream query --name <ingestion status pstream name>

```\
\
Example Syntax\
\
```
 rdac pstream query --name rda_system_collector_ingestion_job_status

```\
\
Example Output\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
       count_  dataset                ingest_job_name                   row_count  status     stream                 timestamp 
 --  --------  ---------------------  ------------------------------  -----------  ---------  ---------------------  -------------------------- 
  0         1  rda_synthetic_metrics  test_pstream-9721ebd0                 78900  Ingesting  test_pstream           2022-12-07T05:45:18.348868 
  1         1  rda_synthetic_metrics  test_pstream-618b8063                100000  Done       test_pstream           2022-12-07T05:06:56.391054 
  2         1  rda_synthetic_metrics  test_pstream-becb20a7                100000  Done       test_pstream           2022-12-06T15:03:04.692909 
  3         1  rda_synthetic_metrics  test_pstream-60b98c94                100000  Done       test_pstream           2022-12-06T14:32:52.728035

```\
\
Note\
\
To evict the pstream ingestion job (when the status is **Ingesting** ) run the `evict` command to terminate the ingestion job\
\
*   Following is the syntax for **pstream evict**\
\
```
 rdac pstream evict --name <ingest job name>

```\
\
Example Syntax\
\
```
 rdac.py pstream evict --name test_pstream-9721ebd0

```\
\
Example Output\
\
```
 Detected OS Name: Linux 
 Detected docker version: 20.10.12 
 Job Evicted Successfully

```\
\
****Sub Command: `evict-export`****\
\
Description: Evict Export Chunks Job\
\
```
 rdac pstream evict-export --help

```\
\
```
 optional arguments: 
   -h, --help   show this help message and exit 
   --name NAME  Export Chunk Job name

```\
\
*   Following is the syntax for **pstream evict-export**\
\
```
 rdac pstream evict-export --name epss_test_logs-bb1c56ea

```\
\
Example Output\
\
```
 Job Evicted Successfully

```\
\
### Sub Command: `purge-outputs`\
\
Description: Purge outputs of completed jobs\
\
```
 Usage: purge-outputs  [-h] --hours OLDER_THAN_HOURS 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --hours OLDER_THAN_HOURS 
                         Purge jobs older than specified number of hours. Must 
                         be >= 1

```\
\
### Sub Command: `read-stream`\
\
Description: Read messages from an RDA stream\
\
```
 Usage: read-stream  [-h] --name STREAM_NAME [--group GROUP] [--delay DELAY] 
             [--show_rate] 
 
 optional arguments: 
   -h, --help          show this help message and exit 
   --name STREAM_NAME  Stream name to read from 
   --group GROUP       Message consumer group name 
   --delay DELAY       Simulate processing delay between each read message 
   --show_rate         Do not print messages, just show rate per minute and 
                       counts

```\
\
### Sub Command: `run`\
\
Description: Run a pipeline on a worker pod\
\
```
 Usage: run  [-h] --pipeline PIPELINE [--nowait] [--log LOGLEVEL] 
             [--group WORKER_GROUP] [--site WORKER_SITE] 
             [--lfilter LABEL_FILTER] [--rfilter RESOURCE_FILTER] [--dryrun] 
             [--save_jobid SAVE_JOBID] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --pipeline PIPELINE   File containing pipeline information in JSON format 
   --nowait              If specified, command does not wait for the completion 
                         of the pipeline 
   --log LOGLEVEL        Specify logging level as none, 
                         DEBUG,INFO,WARNING,ERROR,CRITICAL 
   --group WORKER_GROUP  Deprecated. Use --site option. Specify a worker site 
                         name. If not specified, will use any available worker. 
   --site WORKER_SITE    Specify a worker site name. If not specified, will use 
                         any available worker. 
   --lfilter LABEL_FILTER 
                         CFXQL style query to narrow down workers using their 
                         labels 
   --rfilter RESOURCE_FILTER 
                         CFXQL style query to narrow down workers using their 
                         resources 
   --dryrun              Do not run pipeline but show which worker nodes would 
                         have been selected for run 
   --save_jobid SAVE_JOBID 
                         Save the jobid to a specified file

```\
\
### Sub Command: `run-get-output`\
\
Description: Run a pipeline on a worker, wait for the completion, get the final output\
\
```
 Usage: run-get-output  [-h] [--config CONFIG] [--site SITE] [--pipeline PIPELINE] 
             [--max_rows MAX_ROWS] [--md] [--onerow] [--vault] [--tocsv TO_CSV] 
 
 optional arguments: 
   -h, --help           show this help message and exit 
   --config CONFIG      Additional configurations defined in a YAML or JSON 
                        file 
   --site SITE          Site name regex 
   --pipeline PIPELINE  Plain text Pipeline filename. If not specified, will 
                        read from STDIN. 
   --max_rows MAX_ROWS  Max rows to print on screen. 
   --md                 Print in markdown format on screen instead of text 
                        table format 
   --onerow             Print fist row in a vertical format (in addition to 
                        table) 
   --vault              Use RDA Vault for credentials if not specified locally 
                        in a JSON file 
   --tocsv TO_CSV       Save the output to CSV formatted file

```\
\
### Sub Command: `schedule-add`\
\
Description: Add a new schedule for pipeline execution\
\
```
 Usage: schedule-add  [-h] --pipeline PIPELINE [--log LOGLEVEL] --name SCHEDULENAME 
             --type SCHEDULE_TYPE [--startdate STARTDATE] 
             [--starttime STARTTIME] [--enddate ENDDATE] [--weekdays WEEKDAYS] 
             [--freq FREQUENCY] [--tz TIMEZONE] --group GROUP 
             [--retries RETRIES] [--retry-intervals RETRYINTERVALS] 
             [--parallel-instances PARALLELINSTANCES] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --pipeline PIPELINE   File containing pipeline contents 
   --log LOGLEVEL        Specify logging level as none, 
                         DEBUG,INFO,WARNING,ERROR,CRITICAL 
   --name SCHEDULENAME   Schedule name to use 
   --type SCHEDULE_TYPE  Schedule Type (Once, Minutes, Hourly, Daily, Weekly, 
                         Always) 
   --startdate STARTDATE 
                         Start date for schedule in YYYY-MM-DD format 
   --starttime STARTTIME 
                         Start time for schedule in HH:MM format 
   --enddate ENDDATE     End date for schedule in YYYY-MM-DD format 
   --weekdays WEEKDAYS   Comma separated Day(s) of the week. Mandatory weekly 
                         schedule type. Possible values:'MON', 
                         'TUE','WED','THU','FRI','SAT','SUN' 
   --freq FREQUENCY      Default 1 except for minutes, where it is 15 minutes 
   --tz TIMEZONE         Timezone name 
   --group GROUP         Worker group name 
   --retries RETRIES     Maximum Retries 
   --retry-intervals RETRYINTERVALS 
                         Retry intervals. Example 5,10,15. Delay time interval 
                         in minutes between each retry 
   --parallel-instances PARALLELINSTANCES 
                         Parallel instances number should range in between 
                         1-10. Example 1,2,3

```\
\
### Sub Command: `schedule-delete`\
\
Description: Delete an existing schedule\
\
```
 Usage: schedule-delete  [-h] --scheduleId SCHEDULEID 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --scheduleId SCHEDULEID 
                         Schedule ID

```\
\
### Sub Command: `schedule-edit`\
\
Description: Edit an existing schedule\
\
```
 Usage: schedule-edit  [-h] --scheduleId SCHEDULEID --type SCHEDULE_TYPE 
             [--startdate STARTDATE] [--starttime STARTTIME] 
             [--enddate ENDDATE] [--weekdays WEEKDAYS] [--freq FREQUENCY] 
             [--tz TIMEZONE] [--group GROUP] [--retries RETRIES] 
             [--retry-intervals RETRYINTERVALS] 
             [--parallel-instances PARALLELINSTANCES] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --scheduleId SCHEDULEID 
                         Schedule ID 
   --type SCHEDULE_TYPE  Schedule Type (Once, Minutes, Hourly, Daily, Weekly, 
                         Always) 
   --startdate STARTDATE 
                         Start date for schedule in YYYY-MM-DD format 
   --starttime STARTTIME 
                         Start time for schedule in HH:MM format 
   --enddate ENDDATE     End Date for schedule in YYYY-MM-DD format 
   --weekdays WEEKDAYS   Comma separated Day(s) of the week. Mandatory weekly 
                         schedule type. Possible values:'MON', 
                         'TUE','WED','THU','FRI','SAT','SUN' 
   --freq FREQUENCY      Default 1 except for minutes, where it is 15 minutes 
   --tz TIMEZONE         Timezone name 
   --group GROUP         Worker group name 
   --retries RETRIES     Maximum Retries 
   --retry-intervals RETRYINTERVALS 
                         Retry intervals 
   --parallel-instances PARALLELINSTANCES 
                         Parallel instances number should range in between 1-10

```\
\
### Sub Command: `schedule-info`\
\
Description: Get details of a schedule\
\
```
 Usage: schedule-info  [-h] --scheduleId SCHEDULEID [--json] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --scheduleId SCHEDULEID 
                         Schedule ID 
   --json                Print detailed information in JSON format instead of 
                         tabular format

```\
\
### Sub Command: `schedule-list`\
\
Description: List all schedules\
\
```
 Usage: schedule-list  [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```\
\
### Sub Command: `schedule-update-status`\
\
Description: Update status of an existing schedule\
\
```
 Usage: schedule-update-status  [-h] --scheduleId SCHEDULEID --status STATUS 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --scheduleId SCHEDULEID 
                         Schedule ID 
   --status STATUS       Status

```\
\
### Sub Command: `schema`\
\
**Following are the valid Sub-Commands for the schema**\
\
| Sub Commands | Description |\
| --- | --- |\
| list | List schemas from the object store |\
| get | Download a schema from the object store |\
| add | Add a new schema to the object store |\
| delete | Delete a schema from the object store |\
\
```
 rdac schema --help

```\
\
```
 Dataset Model Schema management commands 
 
 Following are valid sub-commands for schema: 
   list                      List schemas from the object store 
   get                       Download a schema from the object store 
   add                       Add a new schema to the object store 
   delete                    Delete a schema from the object store

```\
\
****Sub Command: `list`****\
\
Description: List schemas from the object store\
\
```
 Usage: schema-list  [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```\
\
*   Following is the syntax for **schema-list**\
\
```
 rdac schema list --help

```\
\
Example Output\
\
```
    name              num_columns  saved_time                  title 
 --  --------------  -------------  --------------------------  ----------------------------- 
  0  Example Schema              5  2023-01-05T04:52:38.182396  Example Schema 
  1  Schema-QA                   6  2023-01-05T04:38:41.935552  QA Schema 
  2  Test                        3  2023-01-05T04:39:03.106297  Pager Duty Urgency Enrichment
 ```\
\
****Sub Command: `get`****\
\
Description: Download a schema from the object store\
\
```
 rdac schema get --help

```\
\
```
 Usage: schema-get  [-h] --name NAME 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --name NAME  Schema name

```\
\
*   Following is the syntax for **schema-get**\
\
```
  rdac schema get --name Test
 ```\
\
Example Output\
\
```
 { 
   "title": "Pager Duty Urgency Enrichment", 
   "properties": { 
     "rule": { 
       "type": "string" 
     }, 
     "rule_id": { 
       "type": "string" 
     }, 
     "urgency_id": { 
       "type": "string", 
       "default": "low", 
       "enum": [ 
         "low", 
         "medium", 
         "high", 
         "critical", 
         "emergency" 
       ] 
     } 
   }, 
   "required": [ 
     "rule", 
     "rule_id" 
   ], 
   "name": "Test", 
   "date": "2023-01-05T04:39:03.106297" 
 }

```\
\
****Sub Command: `add`****\
\
Description: Add a new schema to the object store\
\
```
 rdac schema add --help

```\
\
```
 Usage: schema-add  [-h] --name NAME --file INPUT_FILE 
 
 optional arguments: 
   -h, --help         show this help message and exit 
   --name NAME        Schema name 
   --file INPUT_FILE  File (or URL) containing the json schema as per 
                      (https://json-schema.org/specification.html)

```\
\
*   Following is the syntax for **schema-add**\
\
```
 rdac schema add --name Schematest --file schematest.json

```\
\
Example Output 1\
\
```
 Successfully loaded schema Schematest and validated. 
 Unknown schema Schematest 
 
 Added/modified schema Schematest

```\
\
Note\
\
Before adding the schema, create a JSON input\_file containing the json schema.\
\
Example output 2\
\
```
 { 
   "title": "New Pager Duty Urgency Enrichment", 
   "properties": { 
     "rule": { 
       "type": "string" 
     }, 
     "rule_id": { 
       "type": "string" 
     }, 
     "urgency_id": { 
       "type": "string", 
       "default": "low", 
       "enum": [ 
         "low", 
         "medium", 
         "high", 
         "critical", 
         "emergency" 
       ] 
     } 
   }, 
   "required": [ 
     "rule", 
     "rule_id" 
   ], 
   "name": "Test", 
   "date": "2023-01-24T04:39:03.106297" 
 }

```\
\
****Sub Command: `delete`****\
\
Description: Delete a schema from the object store\
\
rdac schema delete --help\
\
```
 Usage: schema-delete  [-h] --name NAME [--yes] 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --name NAME  Schema name 
   --yes        Delete without prompting

```\
\
*   Following is the syntax for **schema-delete**\
\
```
 rdac schema delete --name Schematest

```\
\
Example Output\
\
```
 Confirm deletion of schema (y/n)? y 
 Schema deleted.

```\
\
### Sub Command: `secret`\
\
Description: Credentials (Secrets) management commands\
\
**Following are the valid Sub-Commands for the secret**\
\
| Sub Commands | Description |\
| --- | --- |\
| types | List of all available secret types |\
| add | Add a new secret to the vault |\
| delete | Delete a secret from the vault |\
| list | List names and types of all secrets in vault |\
\
```
 rdac secret

```\
\
```
 Credentials (Secrets) management commands 
 
 Following are valid sub-commands for secret: 
   types                     List of all available secret types 
   add                       Add a new secret to the vault 
   delete                    Delete a secret from the vault 
   list                      List names and types of all secrets in vault

```\
\
****Sub Command: `types`****\
\
Description: List of all available secret types\
\
```
 rdac secret-types --help

```\
\
```
 Usage: secret-types  [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```\
\
\* Following is the syntax for **secret-types**\
\
```
 rdac secret-types

```\
\
Example Output\
\
```
 +-----------------------+-----------------------------------------------------------------------------------------------------------------+ 
 | Type                  | Description                                                                                                     | 
 |-----------------------+-----------------------------------------------------------------------------------------------------------------| 
 | aiaexpress            | CloudFabrix AIA Express                                                                                         | 
 | ansible               | Ansible - Run Ansible playbook defined in the input dataset                                                     | 
 | appdynamics           | AppDynamics - Inventory and Metrics collection from AppDynamics                                                 | 
 | arcsight              | ArcSight - Get event details from ArcSight                                                                      | 
 | arista-bigswitch      | Arista Bigswitch Fabric Inventory Collection                                                                    | 
 | aws                   | AWS EC2                                                                                                         | 
 | aws-cloudwatch        | AWS CloudWatch - Logs and Metric collection from AWS Cloudwatch                                                 | 
 | aws-cloudwatch-v2     | AWS CloudWatch - Logs and Metric collection from AWS Cloudwatch                                                 | 
 | aws-kinesis           | AWS Kinesis - Read and Write data on AWS Kinesis streams                                                        | 
 | aws-sqs               | AWS SQS - Read and Write data to SQS stream                                                                     | 
 | aws_v2                | AWS EC2 - Collect inventory details from EC2 instances                                                          | 
 | azure                 | Microsoft Azure - Collect inventory details from Microsoft Azure                                                | 
 | azure-insights        | Microsoft Azure Insights - Collect metrics and logs from Azure                                                  | 
 | blob_aws              | Pull/Push blobs from AWS Cloud object stores                                                                    | 
 | blob_azure            | Pull/Push blobs from Azure Cloud object stores                                                                  | 
 | blob_gcp              | Pull/Push blobs from GCP Cloud object stores                                                                    | 
 | cfxai_classification  | CloudFabrix ML - Classification                                                                                 | 
 +-----------------------+-----------------------------------------------------------------------------------------------------------------+

```\
\
****Sub Command: `add`****\
\
### Sub Command: `secret-add`\
\
Description: Add a new secret to the vault\
\
```
 Usage: secret-add  [-h] --type SECRET_TYPE 
 
 optional arguments: 
   -h, --help          show this help message and exit 
   --type SECRET_TYPE  Secret type (use secret-list command to see available 
                       secret types)

```\
\
****Sub Command: `list`****\
\
Description: List names and types of all secrets in vault\
\
```
 Usage: secret-list  [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```\
\
\* Following is the syntax for **secret-list**\
\
```
 rdac secret-list

```\
\
Example Output\
\
```
     name    type              saved_time                  checksum 
 --  ------  ----------------  --------------------------  -------------------------------- 
  0  cfxml   cfxai_regression  2023-01-12T05:49:39.325308  def3259af30655a412beb39a8a99e53a
 ```\
\
### Sub command: `set-pod-log-level`\
\
Description: Update the logging level for a given RDA Pod\
\
```
 usage: rdac [-h] --id POD_ID --level LEVEL [--logger LOGGER_NAME] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --id POD_ID           pod_id of the pod for which the logging level need to 
                         be configured 
   --level LEVEL         Logging level. Must be one of DEBUG INFO WARNING ERROR 
                         CRITICAL 
   --logger LOGGER_NAME  Logging Name. By default it sets the root logger.

```\
\
Note\
\
This command is deprecated. It is recommended to use `pod-logging` instead\
\
### Sub Command: `site-profile`\
\
Description: Site Profile management commands\
\
**Following are the valid Sub-Commands for the site-profile**\
\
| Sub Commands | Description |\
| --- | --- |\
| Following are valid sub-commands for site-profile: |     |\
| add | Add a new site profile |\
| edit | Update a site profile |\
| get | Get a site profile data |\
| delete | Delete a site profile |\
| list | List all site profiles |\
\
```
 rdac site-profile --help

```\
\
```
 Site Profile management commands 
 
 Following are valid sub-commands for site-profile: 
   add                       Add a new site profile 
   edit                      Update a site profile 
   get                       Get a site profile data 
   delete                    Delete a site profile 
   list                      List all site profiles

```\
\
### Sub Command: `site-profile-add`\
\
Description: Add a new site profile\
\
```
 Usage: site-profile-add  [-h] --name NAME --site SITE [--description DESCRIPTION] 
             [--sources SOURCES] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Name of Site Profile 
   --site SITE           Site name or a regular expression 
   --description DESCRIPTION 
                         Description of Site Profile 
   --sources SOURCES     Comma separated list of sources

```\
\
### Sub Command: `site-profile-delete`\
\
Description: Delete a site profile\
\
```
 Usage: site-profile-delete  [-h] --name NAME 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --name NAME  Name of the site profile to delete

```\
\
### Sub Command: `site-profile-edit`\
\
Description: Update a site profile\
\
```
 Usage: site-profile-edit  [-h] --name NAME [--site SITE] [--description DESCRIPTION] 
             [--sources SOURCES] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name NAME           Name of Site Profile 
   --site SITE           Site name or a regular expression 
   --description DESCRIPTION 
                         Description of Site Profile 
   --sources SOURCES     Comma separated list of sources

```\
\
### Sub Command: `site-profile-get`\
\
Description: Get a site profile data\
\
```
 Usage: site-profile-get  [-h] --name NAME 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --name NAME  Name of the site profile to display

```\
\
### Sub Command: `site-profile-list`\
\
Description: List all site profiles.\
\
```
 rdac site-profile-list --help

```\
\
```
 Usage: site-profile-list  [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```\
\
\* Following is the syntax for **site-profile-list**\
\
```
 rdac site-profile-list

```\
\
Example Output\
\
```
     name     description           site    sources    saved_time 
 --  -------  --------------------  ------  ---------  -------------------------- 
  0  default  Default Site Profile  .*      cfxml      2023-01-12T05:49:39.425974
 ```\
\
### Sub Command: `site-summary`\
\
Description: Show summary by Site and Overall\
\
```
 rdac site-summary --help

```\
\
```
 usage: rdac [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```\
\
\* Following is the syntax for **site-summary**\
\
```
 rdac site-summary

```\
\
Example Output\
\
```
 Summary 
     Overall 
        Infra Pod Count: 25 
        Worker Count: 1 
        Worker Group Count: 4 
        Site Count: 4 
        Cpu Cores: 4 
        Memory Gb: 31.3 
        Active Jobs: 3 
        Total Jobs: 10 
        Agent Count: 3 
        Site Names: collabagent, mlagent, irmagent, rda-site-01 
 
     By Site 
       * Name: collabagent 
         Worker Count: 0 
         Cpu Cores: 0 
         Memory Gb: 0 
         Active Jobs: 0 
         Total Jobs: 0 
         Agent Count: 1 
         Agent Names: agent-collab 
 
       * Name: irmagent 
         Worker Count: 0 
         Cpu Cores: 0 
         Memory Gb: 0 
         Active Jobs: 0 
         Total Jobs: 0 
         Agent Count: 1 
         Agent Names: agent-irm

```\
\
### Sub Command: `stack`\
\
**Following are valid sub-commands for stack:**\
\
| Sub Commands | Description |\
| --- | --- |\
| cache-list | List cached stack entries from asset-dependency service |\
| search | Search in a stack using asset-dependency service |\
| search-json | Search in a stack using asset-dependency service, load search criteria from a JSON file |\
| impact-distance | Find the impact distances in a stack using asset-dependency service, load search criteria from a JSON file |\
\
****Sub Command: `cache-list`****\
\
Description: List cached stack entries from asset-dependency service\
\
```
 rdac stack cache-list --help

```\
\
```
 usage: stack [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print results in JSON format

```\
\
*   Following is the syntax for **stack cache-list**\
\
```
 rdac stack cache-list --json

```\
\
Example Output\
\
{ "status": "ok", "data": \[\], "now": "2023-01-23T07:04:25.597835" }\
\
****Sub Command: `impact-distance`****\
\
Description: Find the impact distances in a stack using asset-dependency service, load search criteria from a JSON file\
\
```
 rdac stack impact-distance --help

```\
\
```
 usage: stack [-h] --name STACK_NAME --search_file SEARCH_FILE [--json] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name STACK_NAME     Stack name 
   --search_file SEARCH_FILE 
                         Filename with JSON based search criteria 
   --json                Print results in JSON format

```\
\
\* Following is the syntax for **stack impact-distance**\
\
```
 rdac stack-impact-distance  --name vcenter_topology_stacks --search_file /tmp/search.json

```\
\
Example Output\
\
```
  node_id                   node_label              layer      node_type   distance via 
 -- ------------------------------------------ ----------------------------------- -------------- ----------- ---------- ------------------------------------------ 
  0 423306a6-f91e-ed00-c1dc-d5b3a004659a    debian8.engr.cloudfabrix.com     Virtualization VM          -1 10.95.158.200 
  1 42330bd2-019b-3f22-c629-29824bc07ab7    AIA-Hari-PF80.engr.cloudfabrix.com  Virtualization VM          -1 10.95.158.200 
  2 42331120-6a91-ce70-f8f2-3bfe6620c4f1    macaw0vf1.0.0-Ch           Virtualization VM          -1 10.95.158.200 
  3 42333b86-240a-eddd-0b33-fadc6e242c25    MacawOVFPlatformPOC-v1.0.0      Virtualization VM          -1 10.95.158.200 
  4 42336507-674d-0d86-d8a2-508518fdf9f8    SNMPSimulator-macaw-219       Virtualization VM          -1 10.95.158.200 
  5 4233a553-8746-5ee6-02d8-87423d388ba1    oialatserv1.qa.engr.cloudfabrix.com Virtualization VM          -1 10.95.158.200 
  6 4233ab94-559d-892d-7130-b0ec1d237d11    windows2008r2enterprise       Virtualization VM          -1 10.95.158.200 
  7 4233ee33-5cd3-2a90-0a11-65e2db7ce9dc    platform-60.qa.engr.cloudfabrix.com Virtualization VM          -1 10.95.158.200 
  8 4233f1eb-3ddc-7464-08f9-d536844c10e9    SNMPSimulator-238          Virtualization VM          -1 10.95.158.200 
  9 4233f62f-7f59-fb80-31d3-a89ab6108df1    oialatpf.qa.engr.cloudfabrix.com   Virtualization VM          -1 10.95.158.200 
 10 4233f6a4-5870-48f4-9d61-af0a0f455593    Promotheus_windows_vm_testing    Virtualization VM          -1 10.95.158.200 
 11 4233ffd3-2061-59fd-fe2c-832097ccc1f6    oialatclam1.qa.engr.cloudfabrix.com Virtualization VM          -1 10.95.158.200 
 12 564d3503-5fe7-d5a0-70b8-e1adf218ffaa    pf150.qa.engr.cloudfabrix.com    Virtualization VM          -1 10.95.158.200 
 13 564d3c15-d2a9-e904-0c21-bf53301960f7    hari_elk7.4.engr.cloudfabrix.com   Virtualization VM          -1 10.95.158.200 
 14 564d4711-398f-34f1-7f3f-919d3b4eadcd    SNMPSimulator-macaw-214       Virtualization VM          -1 10.95.158.200
 ```\
\
### Sub Command: `stack-search`\
\
Description: Search in a stack using asset-dependency service\
\
```
 Usage: stack-search  [-h] --name STACK_NAME --values VALUES --attrs ATTRS --types TYPES 
             [--exclude EXCLUDE] [--depth DEPTH] 
 
 optional arguments: 
   -h, --help         show this help message and exit 
   --name STACK_NAME  Stack name 
   --values VALUES    Attribute values to search for. Multiple values may be 
                      specified separated by a comma 
   --attrs ATTRS      Comma separated list of node attribute names 
   --types TYPES      Comma separated list of node types to search 
   --exclude EXCLUDE  Comma separated list of node types to exclude in search 
   --depth DEPTH      Max depth

```\
\
### Sub Command: `stack-search-json`\
\
Description: Search in a stack using asset-dependency service, load search criteria from a JSON file\
\
```
 Usage: stack-search-json  [-h] --name STACK_NAME --search_file SEARCH_FILE 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name STACK_NAME     Stack name 
   --search_file SEARCH_FILE 
                         Filename with JSON based search criteria

```\
\
### Sub Command: `staging-area-add`\
\
Description: Add or update staging area\
\
```
 Usage: staging-area-add  [-h] --file INPUT_FILE [--overwrite] 
 
 optional arguments: 
   -h, --help         show this help message and exit 
   --file INPUT_FILE  YAML file containing staging area definition 
   --overwrite        Overwrite even if a staging area already exists with a 
                      name.

```\
\
### Sub Command: `staging-area-delete`\
\
Description: Delete a staging area\
\
```
 Usage: staging-area-delete  [-h] --name STAGING_AREA_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name STAGING_AREA_NAME 
                         Name of the staging area to delete

```\
\
### Sub Command: `staging-area-get`\
\
Description: Get YAML data for a staging area\
\
```
 Usage: staging-area-get  [-h] --name STAGING_AREA_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name STAGING_AREA_NAME 
                         Name of the staging area

```\
\
### Sub Command: `staging-area-list`\
\
Description: List all staging areas.\
\
```
 Usage: staging-area-list  [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```\
\
### Sub Command: `subscription`\
\
Description: Show current CloudFabrix RDA subscription details\
\
```
 Usage: subscription  [-h] [--json] [--details] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format 
   --details   Show full details when showing plain text format

```\
\
### Sub Command: `synthetics`\
\
Description: Data synthesizing management commands\
\
**Following are the valid Sub-Commands for the synthetics**\
\
| Sub Commands | Description |\
| --- | --- |\
| add | Add or update Synthetic Profile |\
| get | Get JSON data for a Synthetic Profile |\
| list | List all Synthetic Profiles |\
| delete | Delete a Synthetic Profile |\
| enable | Change the status of a Synthetic Profile to 'enabled' |\
| disable | Change the status of a Synthetic Profile to 'disabled' |\
| status | List status of all active synthetic profiles |\
| reset | Reset all active situations in a single synthetic profile |\
| situation | Activate a specific situtation in a given synthetic profile |\
| webhooks-list | List all Webhook Targets for Synthesizer |\
| webhooks-update | Update Webhook Targets for Synthesizer |\
| generate-ml-dataset | Generate ML dataset from input alerts & incidents stream and write to an output stream |\
\
```
 rdac synthetics --help

```\
\
```
 Data synthesizing management commands 
 
 Following are valid sub-commands for synthetics: 
   add                       Add or update Synthetic Profile 
   get                       Get JSON data for a Synthetic Profile 
   list                      List all Synthetic Profiles 
   delete                    Delete a Synthetic Profile 
   enable                    Change the status of a Synthetic Profile to 'enabled' 
   disable                   Change the status of a Synthetic Profile to 'disabled' 
   status                    List status of all active synthetic profiles 
   reset                     Reset all active situations in a single synthetic profile 
   situation                 Activate a specific situtation in a given synthetic profile 
   webhooks-list             List all Webhook Targets for Synthesizer 
   webhooks-update           Update Webhook Targets for Synthesizer 
   generate-ml-dataset       Generate ML dataset from input alerts & incidents stream and write to an output stream

```\
\
****Sub Command: `get`****\
\
Description: Get JSON data for a Synthetic Profile\
\
```
 rdac synthetics get --help

```\
\
```
 usage: synthetics [-h] --name SYNTHETIC_PROFILE_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name SYNTHETIC_PROFILE_NAME 
                         Name of the synthetic_profile

```\
\
\* Following is the syntax for **synthetics get**\
\
```
 rdac synthetics get --name Online_Banking_App_Profile

```\
\
Example Output\
\
```
 { 
     "name": "Online_Banking_App_Profile", 
     "label": "Online Banking App Synthetics", 
     "enabled": true, 
     "version": "22.8.22.1", 
     "stack": "Online_Banking_Stack", 
     "metric_stream": "rda_synthetic_metrics", 
     "alert_stream": "rda_synthetic_alerts", 
     "diagnostics": [ 
         { 
             "id": "db_storage", 
             "label": "Check Database Storage", 
             "rules": { 
                 "tlog": { 
                     "name": "Transaction Log Free Disk Space", 
                     "check": "Ensure 100GB of free disk space", 
                     "status": { 
                         "NORMAL": "Available Disk space is 100GB oe more", 
                         "WARNING": "Available disk space is between 75GB to 100GB", 
                         "CRITICAL": "Available disk space is less than 50GB" 
                     } 
                 }, 
                 "backup": { 
                     "name": "Backup Volume Free Disk Space", 
                     "check": "Ensure 500GB of free disk space", 
                     "status": {

```\
\
****Sub Command: `list`****\
\
Description: List all Synthetic Profiles\
\
```
 rdac synthetics list --help

```\
\
```
 usage: synthetics [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```\
\
*   Following is the syntax for **synthetics list**\
\
```
 rdac synthetics list

```\
\
Example Output\
\
```
 name                        label                          enabled    saved_time 
 --  --------------------------  -----------------------------  ---------  -------------------------- 
  0  Pet_Clinic_App_Profile1     Pet Clinic App Synthetics1     no         2022-10-04T23:01:52.860735 
  1  log-profile-example-1       ACME Log Synthetics            yes        2023-01-23T22:13:48.183910 
  2  Pet_Clinic_App_Profile      Pet Clinic App Synthetics      no         2022-09-28T05:51:51.861521 
  3  Online_Banking_App_Profile  Online Banking App Synthetics  yes        2023-01-10T01:51:32.625109

```\
\
****Sub Command: `status`****\
\
Description: List status of all active synthetic profiles\
\
```
 rdac synthetics status --help

```\
\
```
 usage: synthetics [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```\
\
*   Following is the syntax for **synthetics status**\
\
```
 rdac synthetics status --json

```\
\
Example Output\
\
```
 2023-02-10:09:59:38 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 { 
     "status": "ok", 
     "data": [ 
         { 
             "metrics": 0, 
             "alerts": 0, 
             "profile_name": "log-profile-example-1", 
             "stack": "Enterprise_Data_and_Analytics_Stack", 
             "active_situations": "" 
         }, 
         { 
             "metrics": 26, 
             "alerts": 1, 
             "profile_name": "Online_Banking_App_Profile", 
             "stack": "Online_Banking_Stack", 
             "active_situations": "" 
         } 
     ], 
     "now": "2023-02-10T09:59:38.147686" 
 }

```\
\
****Sub Command: `enable`****\
\
Description: Change the status of a Synthetic Profile to 'enabled'\
\
```
 rdac synthetics enable --help

```\
\
```
 usage: synthetics [-h] --name SYNTHETIC_PROFILE_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name SYNTHETIC_PROFILE_NAME 
                         Name of the synthetic profile

```\
\
*   Following is the syntax for **synthetics enable**\
\
```
 rdac synthetics enable  Pet_Clinic_App_Profile1

```\
\
Example Output\
\
```
 2023-02-10:09:58:02 [1] INFO nats_client Creating new SharedPool ... 
 2023-02-10:09:58:02 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-02-10:09:58:02 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Changed status of Pet_Clinic_App_Profile1 to enabled

```\
\
****Sub Command: `disable`****\
\
Description: Change the status of a Synthetic Profile to 'disabled'\
\
```
 rdac synthetics disable --help

```\
\
```
 usage: synthetics [-h] --name SYNTHETIC_PROFILE_NAME 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --name SYNTHETIC_PROFILE_NAME 
                         Name of the synthetic profile

```\
\
*   Following is the syntax for **synthetics disable**\
\
```
  rdac synthetics disable  --name  Pet_Clinic_App_Profile1
 ```\
\
Example Output\
\
```
 2023-02-10:09:58:45 [1] INFO nats_client Creating new SharedPool ... 
 2023-02-10:09:58:45 [1] INFO nats_client Initiallzing PubMgr for pid=1 
 2023-02-10:09:58:45 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 Changed status of Pet_Clinic_App_Profile1 to disabled

```\
\
### Sub Command: `verify-pipeline`\
\
Description: Verify the pipeline on a worker pod\
\
```
 Usage: verify-pipeline  [-h] --pipeline PIPELINE [--group WORKER_GROUP] 
             [--site WORKER_SITE] [--lfilter LABEL_FILTER] 
             [--rfilter RESOURCE_FILTER] [--maxwait MAX_WAIT] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --pipeline PIPELINE   File containing pipeline contents 
   --group WORKER_GROUP  Deprecated. Use --site option. Specify a worker site 
                         name. If not specified, will use any available worker. 
   --site WORKER_SITE    Specify a worker site name. If not specified, will use 
                         any available worker. 
   --lfilter LABEL_FILTER 
                         CFXQL style query to narrow down workers using their 
                         labels 
   --rfilter RESOURCE_FILTER 
                         CFXQL style query to narrow down workers using their 
                         resources 
   --maxwait MAX_WAIT    Maximum wait time (seconds) for credential check to 
                         complete.

```\
\
*   Following is the syntax for **verify-pipeline**\
\
```
 rdac verify-pipeline --pipeline jira.json --group aws-qa-102-200 --rfilter "cpu_count = 8" --lfilter "rda_messenger_version = '21.7.29.3'"

```\
\
Example Output\
\
```
 Initiating verify pipeline 
 { 
   "status": "started", 
   "reason": "", 
   "results": [], 
   "now": "2021-08-06T15:35:11.078751", 
   "status-subject": "tenants.d6152687e007482e99ed210bca1fbe9e.worker.group.f17ce69d60d8.direct.9729ad1e", 
   "jobid": "39e2cf7970b144fe911ec51f7a9f5a35" 
 } 
 Initializing: 
 Initializing: 
 Initializing: 
 Initializing: 
 Completed:

```\
\
### Sub Command: `viz`\
\
Description: Visualize data from a file within the console (terminal)\
\
```
 Usage: viz  [-h] --file INPUT_FILE [--format FILE_FORMAT] 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --file INPUT_FILE     CSV or parquet or JSON formatted file which will be 
                         visualized 
   --format FILE_FORMAT  Input file format (csv or parquet or json). 'auto' 
                         means format will be derived from file extension

```\
\
### Sub Command: `watch`\
\
**Following are the valid Sub-Commands for the watch**\
\
| Sub Commands | Description |\
| --- | --- |\
| registry | Start watching updates published by the RDA pod registry |\
| logs | Start watching logs produced by the pipelines |\
| traces | Start watching traces produced by the pipelines |\
\
```
 rdac watch --help

```\
\
```
 Commands to watch various streams such sas trace, logs and change notifications by microservices 
 
 Following are valid sub-commands for watch: 
   registry                  Start watching updates published by the RDA pod registry 
   logs                      Start watching logs produced by the pipelines 
   traces                    Start watching traces produced by the pipelines

```\
\
****Sub Command: `registry`****\
\
Description: Start watching updates published by the RDA pod registry\
\
```
 rdac watch registry --help

```\
\
```
 usage: watch [-h] [--json] 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --json      Print detailed information in JSON format instead of tabular 
               format

```\
\
*   Following is the syntax for **watch registry**\
\
```
 rdac watch registry

```\
\
Example Output\
\
```
  Update Type  Pod Type     Pod ID       Host         Pod Started At 
 2023-02-01:13:39:54 [1] INFO nats_client Creating new SharedPool ... 
 2023-02-01:13:39:54 [1] INFO nats_client Initiallzing SubMgr for pid=1 
 2023-02-01:13:39:54 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 2023-02-01:13:39:54 [1] INFO nats_client Creating thread-pool of size: 4, PID=1
 ```\
\
****Sub Command: `logs`****\
\
Description: Start watching logs produced by the pipelines\
\
```
 rdac watch logs --help

```\
\
```
 usage: watch [-h] [--json] [--attr ATTR] 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --json       Print detailed information in JSON format instead of tabular 
                format 
   --attr ATTR  Filter for a specific attribute. Example: --attr 
                debug=MyDebugging1

```\
\
*   Following is the syntax for **watch logs**\
\
```
 rdac watch logs

```\
\
Example Output\
\
```
 2023-02-01:13:40:37 [1] INFO nats_client Creating new SharedPool ... 
 2023-02-01:13:40:37 [1] INFO nats_client Initiallzing SubMgr for pid=1 
 2023-02-01:13:40:37 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 2023-02-01:13:40:37 [1] INFO nats_client Creating thread-pool of size: 4, PID=1 
  13:40:37.316 da9d9b28 INFO     executor.py:599:send_to_stream                [Job da9d9b28a0954327a19c941302ce7947] Status update pipeline=reg-predict-parent-pipeline, type=in-progress 
  13:40:37.337 da9d9b28 INFO     executor.py:599:send_to_stream                [Job da9d9b28a0954327a19c941302ce7947] Status update pipeline=reg-predict-parent-pipeline, type=in-progress 
  13:40:37.355 da9d9b28 INFO     executor.py:599:send_to_stream                [Job da9d9b28a0954327a19c941302ce7947] Status update pipeline=reg-predict-parent-pipeline, type=in-progress 
  13:40:38.376 da9d9b28 INFO     executor.py:599:send_to_stream                [Job da9d9b28a0954327a19c941302ce7947] Status update pipeline=reg-predict-parent-pipeline, type=in-progress 
  13:40:38.406 da9d9b28 INFO     exec_source.py:277:update_data                Executing inner pipeline 'reg-predict-child-pipeline', previous_pipelines = ['reg-predict-parent-pipeline'] 
  13:40:38.407 da9d9b28 INFO     plumbing_pipeline.py:627:execute_sequence     Executing pipeline reg-predict-child-pipeline 
  13:40:38.408 da9d9b28 INFO     plumbing_pipeline.py:661:execute_sequence     Executing block reg-predict-child-pipelineb0 
  13:40:38.408 da9d9b28 INFO     executor.py:599:send_to_stream                [Job da9d9b28a0954327a19c941302ce7947] Status update pipeline=reg-predict-parent-pipeline, type=in-progress 
  13:40:38.429 da9d9b28 INFO     executor.py:599:send_to_stream                [Job da9d9b28a0954327a19c941302ce7947] Status update pipeline=reg-predict-parent-pipeline, type=in-progress

```\
\
****Sub Command: `traces`****\
\
Description: Start watching traces produced by the pipelines\
\
```
 rdac watch traces --help

```\
\
```
 usage: watch [-h] [--json] [--ts] [--attr ATTR] 
 
 optional arguments: 
   -h, --help   show this help message and exit 
   --json       Print detailed information in JSON format instead of tabular 
                format 
   --ts         Show timestamp when printing traces in plain text format 
   --attr ATTR  Filter for a specific attribute. Example: --attr 
                debug=MyDebugging1

```\
\
\* Following is the syntax for **watch traces**\
\
```
 rdac watch traces

```\
\
Example Output 1\
\
```
 Host         Pipeline                       JobID    Seq Status      Bot                       Dataframe  Error Message 
 2023-02-01:13:41:38 [1] INFO nats_client Creating new SharedPool ... 
 2023-02-01:13:41:38 [1] INFO nats_client Initiallzing SubMgr for pid=1 
 2023-02-01:13:41:38 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 2023-02-01:13:41:38 [1] INFO nats_client Creating thread-pool of size: 4, PID=1 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:enrich                0x12 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:add-missing-columns   0x12 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:eval                  0x14 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:eval                  0x15 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:eval                  0x16 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:eval                  0x17 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:eval                  0x18 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:change-time-format    0x18 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @rn:write-stream          0x18 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:empty                 0x0 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:addrow                0x0 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress #dm:query-persistent-stre 1x2 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:save                  0x0 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:recall                0x0 
  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress *dm:filter                10x12

```\
\
\* Following is the syntax for **watch traces**\
\
```
 rdac watch traces --json

```\
\
Example Output 2\
\
```
 2023-02-10:07:51:23 [1] INFO nats_client Creating new SharedPool ... 
 2023-02-10:07:51:23 [1] INFO nats_client Initiallzing SubMgr for pid=1 
 2023-02-10:07:51:23 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 2023-02-10:07:51:24 [1] INFO nats_client Creating thread-pool of size: 4, PID=1 
 { 
   "msg_version": "rda:1", 
   "proc_id": "57", 
   "proc_info": { 
     "hostname": "05969789d903", 
     "cpu_percent": 0.0, 
     "memory_percent": 1.21, 
     "mem_mb": 486.3, 
     "create_time": 1675792948.18, 
     "cpu_time_user": 111524.55, 
     "cpu_time_system": 10933.69, 
     "system_cpu_percents": [ 
       100.0, 
       33.3, 
       66.7, 
       66.7 
     ] 
   }, 
   "tenant_id": "ae144f67d2a24034ad6920ace6809763", 
   "pod_id": "d08072c8", 
   "pod_group": "rda-site-01", 
   "group_id": "f4a56ba6388c",

```\
\
### Sub Command: `worker-obj-info`\
\
Description: List all worker pods with their current Object Store configuration\
\
```
 rdac worker-obj-info --help

```\
\
```
 Usage: worker-obj-info  [-h] 
 
 optional arguments: 
   -h, --help  show this help message and exit

```\
\
*   Following is the syntax for **worker-obj-info**\
\
```
 rdac worker-obj-info

```\
\
Example Output\
\
```
 Client is configured with following object store 
      Host          : 10.95.122.127:9443 
      Config Cheksum: b469ce79 
 
 2023-02-01:08:49:34 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem 
 +--------------+----------+-------------+--------------------+--------------------------------+ 
 | Host         | ID       | Group       | Object Store       | Object Store Config Checksum   | 
 |--------------+----------+-------------+--------------------+--------------------------------| 
 | 05969789d903 | a92cd27b | rda-site-01 | 10.95.122.127:9443 | b469ce79                       | 
 +--------------+----------+-------------+--------------------+--------------------------------+

```\
\
### Sub Command: `write-stream`\
\
Description: Write data to the specified stream\
\
```
 Usage: write-stream  [-h] --name STREAM_NAME --data DATA [--delay DELAY] [--compress] 
 
 optional arguments: 
   -h, --help          show this help message and exit 
   --name STREAM_NAME  Stream name to write to 
   --data DATA         File containing either single JSON dict or a list 
   --delay DELAY       Delay between each publish message 
   --compress          Enable compression of the data

```\
\
Was this page helpful?\
\
Thanks for your feedback!\
\
Thanks for your feedback!