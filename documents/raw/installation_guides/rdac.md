 



RDA Client Command Line Interface
=================================

1\. Installing RDA Command Line Tool
------------------------------------

RDA Command Line Interface tool comes as a docker image to make it easy to run RDA commands on any Laptop, Desktop or in a Cloud VM.

To run this tool, following are required:

*   Operating Systems: Linux or MacOS
*   Docker installed on that system
*   At least Python 3.0

#### STEP-1: Download the python script

`[](#__codelineno-0-1) curl -o rdac.py https://bot-docs.cloudfabrix.io/data/wrappers/rdac.py`

Make the script an executable:

`[](#__codelineno-1-1) chmod +x rdac.py`

#### STEP-2: Download RDA network configuration

From your cfxCloud account, you can download a copy the RDA Network configuration.

Download the RDA Network configuration file and save it under `$HOME/.rda/rda_network_config.json`

![Portal](https://bot-docs.cloudfabrix.io/images/guide/rda_credentials.png)

#### STEP-3: Verify Script

Verify that `rdac.py` is working correctly by using one of the following commands:

`[](#__codelineno-2-1) python3 rdac.py --help`

Or

`[](#__codelineno-3-1) ./rdac.py --help`

For very first time, above script will validate dependencies such OS, Python version and availability of Docker. If the validation is successful, it will download the docker container image for RDA CLI and run it.

Subsequently, if you want to update the docker container image to latest version, run following command:

`[](#__codelineno-4-1) ./rdac.py update`

2\. RDA Commands: Cheat Sheet
-----------------------------

This section lists few most commonly used RDA Commands.

#### Listing RDA Platform Microservices

RDA Fabric is for each tenant has a set of microservices (pods) deployed as containers either using Kubernetes or as simple docker containers.

Following command lists all active microservices in your RDA Fabric:

`[](#__codelineno-5-1) python3 rdac.py pods`

Typical output for `pods` command would look like:

![Portal](https://bot-docs.cloudfabrix.io/images/guide/rdac_pods.png)

Most of RDA Commands support option `--json` which would print output in a JSON format instead of tabular format.

`[](#__codelineno-6-1) python3 rdac.py pods --json`

Example rdac pods JSON Output

Partial output of `--json` option:

`[](#__codelineno-7-1) { [](#__codelineno-7-2)     "now": "2022-05-20T02:16:31.054287", [](#__codelineno-7-3)     "started_at": "2022-05-17T22:44:13.602509", [](#__codelineno-7-4)     "pod_type": "worker", [](#__codelineno-7-5)     "pod_category": "rda_infra", [](#__codelineno-7-6)     "pod_id": "ae875728", [](#__codelineno-7-7)     "hostname": "d1d45ec2d08f", [](#__codelineno-7-8)     "proc_id": 1, [](#__codelineno-7-9)     "labels": { [](#__codelineno-7-10)         "tenant_name": "dev-1-unified", [](#__codelineno-7-11)         "rda_platform_version": "22.5.13.3", [](#__codelineno-7-12)         "rda_messenger_version": "22.5.15.1", [](#__codelineno-7-13)         "rda_pod_version": "22.5.17.1", [](#__codelineno-7-14)         "rda_license_valid": "no", [](#__codelineno-7-15)         "rda_license_not_expired": "no", [](#__codelineno-7-16)         "rda_license_expiration_date": "" [](#__codelineno-7-17)     }, [](#__codelineno-7-18)     "build_tag": "daily", [](#__codelineno-7-19)     "requests": { [](#__codelineno-7-20)         "auto": "tenants.2dddab0e52544f4eb2de067057aaac31.worker.group.3571581d876b.auto", [](#__codelineno-7-21)         "direct": "tenants.2dddab0e52544f4eb2de067057aaac31.worker.group.3571581d876b.direct.ae875728" [](#__codelineno-7-22)     }, [](#__codelineno-7-23)     "resources": { [](#__codelineno-7-24)         "cpu_count": 8, [](#__codelineno-7-25)         "cpu_load1": 2.24, [](#__codelineno-7-26)         "cpu_load5": 2.43, [](#__codelineno-7-27)         "cpu_load15": 2.52, [](#__codelineno-7-28)         "mem_total_gb": 25.3, [](#__codelineno-7-29)         "mem_available_gb": 9.7, [](#__codelineno-7-30)         "mem_percent": 61.7, [](#__codelineno-7-31)         "mem_used_gb": 15.01, [](#__codelineno-7-32)         "mem_free_gb": 2.93, [](#__codelineno-7-33)         "mem_active_gb": 11.49, [](#__codelineno-7-34)         "mem_inactive_gb": 7.64, [](#__codelineno-7-35)         "pod_usage_active_jobs": 15, [](#__codelineno-7-36)         "pod_usage_total_jobs": 578 [](#__codelineno-7-37)     }, [](#__codelineno-7-38)     "pod_leader": false, [](#__codelineno-7-39)     "objstore_info": { [](#__codelineno-7-40)         "host": "10.10.10.100:9000", [](#__codelineno-7-41)         "config_checksum": "8936434b" [](#__codelineno-7-42)     }, [](#__codelineno-7-43)     "group": "cfx-lab-122-178", [](#__codelineno-7-44)     "group_id": "3571581d876b", [](#__codelineno-7-45)     "site_name": "cfx-lab-122-178", [](#__codelineno-7-46)     "site_id": "3571581d876b", [](#__codelineno-7-47)     "public_access": false, [](#__codelineno-7-48)     "capacity_filter": "cpu_load1 <= 7.0 and mem_percent < 98 and pod_usage_active_jobs < 20", [](#__codelineno-7-49)     "_local_time": 1653012991.0593688 [](#__codelineno-7-50) }`

#### Listing RDA Platform Microservices with Versions

`[](#__codelineno-8-1) python3 rdac.py pods --versions`

![Portal](https://bot-docs.cloudfabrix.io/images/guide/rdac_pod_versions.png)

#### Performing a Health Check on RDA Microservices

Following command performs a health check on all microservices and returns status of each health parameter.

`[](#__codelineno-9-1) python3 rdac.py healthcheck`

![Portal](https://bot-docs.cloudfabrix.io/images/guide/rdac_healthcheck.png)

#### Listing all Running Pipeline Jobs

Following command lists all active jobs created using Portal, CLI, Scheduler or via Service Blueprints.

`[](#__codelineno-10-1) python3 rdac.py jobs`

![Portal](https://bot-docs.cloudfabrix.io/images/guide/rdac_jobs.png)

#### Evicting a Job

Following command can be used to evict a specific Job from RDA Worker. If the job was created by Scheduler or by a Service Blueprint, a new job may be re-created immediately after the job has been evicted.

`[](#__codelineno-11-1) python3 rdac.py evict --jobid c38025837c284562957f78ab385a0caf`

This script attempts to evict the job with ID `c38025837c284562957f78ab385a0caf`

#### Observing Pipeline Execution Traces from CLI

Following command can be used watch (observe) all traces from all workers and all the pipelines that are getting executed anywhere in the RDA Fabric.

`[](#__codelineno-12-1) python3 rdac.py watch-traces`

![Portal](https://bot-docs.cloudfabrix.io/images/guide/rdac_traces.png)

#### List all datasets currently saved in RDA Fabric

`[](#__codelineno-13-1) python3 rdac.py dataset-list`

#### Adding a new dataset to RDA Fabric

Datasets can be added if the data is available as a local file on your system where rdac.py is available or if the data is available via URL. Supported formats are `CSV`, `JSON`, `XLS`, `Parquet`, `ORC` and many compresses formats for `CSV`.

To add a local file as a dataset:

`[](#__codelineno-14-1) python3 rdac.py dataset-add --name my-dataset --file ./mydata.csv`

**Note:** rdac.py mounts current directory as /home inside the docker container. You may also place the data in your home directory folder `$HOME/rdac_data/` and access it as `--file /data/mydata.csv`

You may also add a dataset if the data is accessible via http or https URL.

|     |     |
| --- | --- |
| [1](#__codelineno-15-1)<br>[2](#__codelineno-15-2)<br>[3](#__codelineno-15-3) | `python3 rdac.py dataset-add \               --name 'sample-ecommerce-data' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/sample-ecommerce-data.csv'` |

3\. List of All RDA CLI Sub Commands
------------------------------------

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

`[](#__codelineno-16-1) rdac agent-bots --help`

`[](#__codelineno-17-1) usage: rdac [-h] [--json] [--type AGENT_TYPE] [--group AGENT_GROUP] [](#__codelineno-17-2) [](#__codelineno-17-3) optional arguments: [](#__codelineno-17-4)   -h, --help           show this help message and exit [](#__codelineno-17-5)   --json               Print detailed information in JSON format instead of [](#__codelineno-17-6)                        tabular format [](#__codelineno-17-7)   --type AGENT_TYPE    Show only the agents that match the specified agent [](#__codelineno-17-8)                        type [](#__codelineno-17-9)   --group AGENT_GROUP  Show only the agents that match the specified agent [](#__codelineno-17-10)                        group`

*   Following is the syntax for **agent-bots**

`[](#__codelineno-18-1) rdac agent-bots --json --type rda-event-gateway --group event_gateway_site01`

Example Output

`[](#__codelineno-19-1) [ [](#__codelineno-19-2)     { [](#__codelineno-19-3)         "name": "get-status", [](#__codelineno-19-4)         "description": "List all endpoints configured at this gateway and current status", [](#__codelineno-19-5)         "query-type": "api-endpoint", [](#__codelineno-19-6)         "mode": "source-any", [](#__codelineno-19-7)         "model": {}, [](#__codelineno-19-8)         "agent_type": "rda-event-gateway", [](#__codelineno-19-9)         "site_name": "event_gateway_site01", [](#__codelineno-19-10)         "pod_id": "250951da" [](#__codelineno-19-11)     } [](#__codelineno-19-12) ]`

### Sub Command: `agents`

Description: List all agents for the current tenant

`[](#__codelineno-20-1) rdac agents --help`

`[](#__codelineno-21-1) Usage: agents  [-h] [--json] [--type AGENT_TYPE] [--group AGENT_GROUP] [](#__codelineno-21-2)             [--site SITE_NAME] [](#__codelineno-21-3) [](#__codelineno-21-4) optional arguments: [](#__codelineno-21-5)   -h, --help           show this help message and exit [](#__codelineno-21-6)   --json               Print detailed information in JSON format instead of [](#__codelineno-21-7)                        tabular format [](#__codelineno-21-8)   --type AGENT_TYPE    Show only the agents that match the specified agent [](#__codelineno-21-9)                        type [](#__codelineno-21-10)   --group AGENT_GROUP  Deprecated. Use --site. Show only the agents that match [](#__codelineno-21-11)                        the specified site [](#__codelineno-21-12)   --site SITE_NAME     Show only the agents that match the specified site`

\* The Following is the syntax for **agents**

`[](#__codelineno-22-1) rdac agents`

Example Output

`[](#__codelineno-23-1) +-------------------+----------------+----------+----------------------+-------------------+--------+--------------+ [](#__codelineno-23-2) | Agent-Type        | Host           | ID       | Site                 | Age               |   CPUs |   Memory(GB) | [](#__codelineno-23-3) |-------------------+----------------+----------+----------------------+-------------------+--------+--------------| [](#__codelineno-23-4) | rda-event-gateway | saaswrk72.qa.e | 250951da | event_gateway_site01 | 28 days, 21:54:20 |      4 |        31.33 | [](#__codelineno-23-5) | agent-ml          | 5339ca9ca765   | c4d7b94e | mlagent              | 23:04:10          |      4 |        31.33 | [](#__codelineno-23-6) | agent-irm         | aa932951e71e   | 0fbc78ec | irmagent             | 23:03:42          |      4 |        31.33 | [](#__codelineno-23-7) +-------------------+----------------+----------+----------------------+-------------------+--------+--------------+`

### Sub Command: `alert-rules`

**Following are the valid Sub-Commands for the alert-rules**

| Sub Commands | Description |
| --- | --- |
| add | Add or update alert ruleset |
| get | Get YAML data for an alert ruleset |
| delete | Delete an alert ruleset |
| list | List all alert rulesets. |

`[](#__codelineno-24-1) rdac alert-rules --help`

`[](#__codelineno-25-1) Following are valid sub-commands for alert-rules: [](#__codelineno-25-2)   add                       Add or update alert ruleset [](#__codelineno-25-3)   get                       Get YAML data for an alert ruleset [](#__codelineno-25-4)   delete                    Delete an alert ruleset [](#__codelineno-25-5)   list                      List all alert rulesets.`

****Sub Command: `add`****

Description: Add or update alert ruleset

`[](#__codelineno-26-1) Usage: alert-rules-add  [-h] --file INPUT_FILE [--overwrite] [](#__codelineno-26-2) [](#__codelineno-26-3) optional arguments: [](#__codelineno-26-4)   -h, --help         show this help message and exit [](#__codelineno-26-5)   --file INPUT_FILE  YAML file containing alert ruleset definition [](#__codelineno-26-6)   --overwrite        Overwrite even if a ruleset already exists with a name.`

*   Following is the syntax for **alert-rules add**

`[](#__codelineno-27-1) cat > alertrulestest1.yml << 'EOF' [](#__codelineno-27-2) name: alertruletest [](#__codelineno-27-3) description: syslog from filebeat [](#__codelineno-27-4) realtime-alerts: [](#__codelineno-27-5)     -   name: filebeat_syslog_msgs [](#__codelineno-27-6)         description: VPX Finish task msgs [](#__codelineno-27-7)         groupBy: host_name [](#__codelineno-27-8)         condition: severity = 'INFO' [](#__codelineno-27-9)         severity: CRITICAL [](#__codelineno-27-10)         suppress-for-minutes: 5 [](#__codelineno-27-11) saved_time: '2022-02-19T22:34:10.888947' [](#__codelineno-27-12) EOF [](#__codelineno-27-13) [](#__codelineno-27-14) rdac alert-rules add --file alertrulestest1.yml`

Example output

`[](#__codelineno-28-1) Added ruleset alertruletest with 1 realtime alert rules, 0 aggregate alert rules`

****Sub Command: `delete`****

Description: Delete an alert ruleset

`[](#__codelineno-29-1) Usage: alert-rules-delete  [-h] --name RULESET_NAME [](#__codelineno-29-2) [](#__codelineno-29-3) optional arguments: [](#__codelineno-29-4)   -h, --help           show this help message and exit [](#__codelineno-29-5)   --name RULESET_NAME  Name of the alert ruleset to delete`

*   Following is the syntax for **alert-rules delete**

`[](#__codelineno-30-1) rdac alert-rules delete --name alertrulestest1`

Example Output

`[](#__codelineno-31-1) Deleted alert ruleset: alertruletest`

****Sub Command: `get`****

Description: Get YAML data for an alert ruleset

`[](#__codelineno-32-1) Usage: alert-rules-get  [-h] --name RULESET_NAME [](#__codelineno-32-2) [](#__codelineno-32-3) optional arguments: [](#__codelineno-32-4)   -h, --help           show this help message and exit [](#__codelineno-32-5)   --name RULESET_NAME  Name of the alert ruleset to display`

*   Following is the syntax for **alert-rules get**

`[](#__codelineno-33-1) rdac alert-rules get --name ATest_ZRules`

Example Output

`[](#__codelineno-34-1) description: Alert_Rules [](#__codelineno-34-2) name: ATest_ZRules [](#__codelineno-34-3) aggregate-alerts: [](#__codelineno-34-4) - rule_a [](#__codelineno-34-5) - rule_b [](#__codelineno-34-6) realtime-alerts: [](#__codelineno-34-7) - rule_1 [](#__codelineno-34-8) - rule_2 [](#__codelineno-34-9) saved_time: '2022-12-20T05:16:41.716023'`

****Sub Command: `list`****

Description: List all alert rulesets.

`[](#__codelineno-35-1) Usage: alert-rules-list  [-h] [--json] [](#__codelineno-35-2) [](#__codelineno-35-3) optional arguments: [](#__codelineno-35-4)   -h, --help  show this help message and exit [](#__codelineno-35-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-35-6)               format`

*   Following is the syntax for **alert-rules list**

`[](#__codelineno-36-1) rdac alert-rules list`

Example Output

    `[](#__codelineno-37-1)     name              description           saved_time                    num_realtime_alert_rules    num_aggr_alert_rules [](#__codelineno-37-2) --  ----------------  --------------------  --------------------------  --------------------------  ---------------------- [](#__codelineno-37-3)  0  alertruletestnew  syslog from filebeat  2023-01-03T05:01:55.361186                           1                       0 [](#__codelineno-37-4) [](#__codelineno-37-5) Cleaning up socket for process: 1. Socket file: /tmp/rdf_log_socket_57602b71-8ea5-49c5-acbd-54c9908a0680 [](#__codelineno-37-6) Exiting out of LogRecordSocketReceiver. pid: 1. Socket file: /tmp/rdf_log_socket_57602b71-8ea5-49c5-acbd-54c9908a0680`

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

`[](#__codelineno-38-1) rdac bot-package --help`

`[](#__codelineno-39-1) Following are valid sub-commands for bot-package: [](#__codelineno-39-2)   add                       Add or update Bot Package [](#__codelineno-39-3)   get                       Get meta data for a Bot Package [](#__codelineno-39-4)   delete                    Delete a Bot Package [](#__codelineno-39-5)   list                      List all Bot Packages [](#__codelineno-39-6)   build                     Build the specified bot package [](#__codelineno-39-7)   ut                        Run Unit Tests [](#__codelineno-39-8)   generate                  Generate the specified bot package [](#__codelineno-39-9)   list-runtimes             List available Bot Package runtime environments on each worker`

****Sub Command: `list`****

Description: List all Bot Packages

`[](#__codelineno-40-1) rdac bot-package list --help`

`[](#__codelineno-41-1) usage: bot-package [-h] [--json] [](#__codelineno-41-2) [](#__codelineno-41-3) optional arguments: [](#__codelineno-41-4)   -h, --help  show this help message and exit [](#__codelineno-41-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-41-6)               format`

*   Following is the syntax for **bot-package list**

`[](#__codelineno-42-1) rdac bot-package list`

Example Output

`[](#__codelineno-43-1) Name                       Version    Description                              Has Dist    Publisher    Saved Time [](#__codelineno-43-2) -------------------------  ---------  ---------------------------------------  ----------  -----------  -------------------------- [](#__codelineno-43-3) botpkg_demo_proactivecase  22.11.9    ProctiveCase API for ServiceNow Tickets  Yes         CloudFabrix  2022-11-14T21:16:30.201550`

****Sub Command: `get`****

Description: Get meta data for a Bot Package

`[](#__codelineno-44-1) rdac bot-package get --help`

`[](#__codelineno-45-1) optional arguments: [](#__codelineno-45-2)   -h, --help           show this help message and exit [](#__codelineno-45-3)   --name PACKAGE_NAME  Name of the Bot Package`

\* Following is the syntax for **bot-package get**

`[](#__codelineno-46-1) rdac bot-package get --name botpkg_demo_proactivecase`

Example Output

`[](#__codelineno-47-1) extension: [](#__codelineno-47-2)   namespace: demo [](#__codelineno-47-3)   type: proactivecase [](#__codelineno-47-4)   version: 22.11.9 [](#__codelineno-47-5)   description: ProctiveCase API for ServiceNow Tickets [](#__codelineno-47-6)   default_name: proactivecase [](#__codelineno-47-7)   publisher: CloudFabrix [](#__codelineno-47-8)   support_email: mohammed.rahman@cloudfabrix.com [](#__codelineno-47-9)   config_template: [](#__codelineno-47-10)     hostname: null [](#__codelineno-47-11)     port: 443 [](#__codelineno-47-12)     uri_suffix: internal/proactiveCaseAPI/v1.1 [](#__codelineno-47-13)     client_id: null [](#__codelineno-47-14)     secret: null [](#__codelineno-47-15)     $secure: [](#__codelineno-47-16)     - secret [](#__codelineno-47-17)     $mandatory: [](#__codelineno-47-18)     - hostname [](#__codelineno-47-19)     - client_id [](#__codelineno-47-20)     - secret [](#__codelineno-47-21)     $labels: [](#__codelineno-47-22)       hostname: Host [](#__codelineno-47-23)       port: Port [](#__codelineno-47-24)       client_id: Client ID [](#__codelineno-47-25)       secret: Secret Value [](#__codelineno-47-26)   implementation: [](#__codelineno-47-27)     code: proactivecase.ProactiveCase [](#__codelineno-47-28) bots: [](#__codelineno-47-29) - name: get-ticket [](#__codelineno-47-30)   description: Get ServiceNow Ticket [](#__codelineno-47-31)   bot_type: source [](#__codelineno-47-32)   model_type: api [](#__codelineno-47-33)   model_parameters: [](#__codelineno-47-34)   - name: ticket_id [](#__codelineno-47-35)     description: comma separated ticket IDs [](#__codelineno-47-36)     type: text [](#__codelineno-47-37)     mandatory: true [](#__codelineno-47-38)   - name: source [](#__codelineno-47-39)     description: Source [](#__codelineno-47-40)     type: text [](#__codelineno-47-41)     mandatory: true`

****Sub Command: `generate`****

Description: Generate the specified bot package

`[](#__codelineno-48-1) rdac bot-package generate --help`

`[](#__codelineno-49-1) usage: bot-package [-h] --namespace NAMESPACE --name NAME [--version VERSION] [](#__codelineno-49-2)                    [--bots NUM_OF_BOTS] --output_dir OUTPUT_DIR [](#__codelineno-49-3) [](#__codelineno-49-4) optional arguments: [](#__codelineno-49-5)   -h, --help            show this help message and exit [](#__codelineno-49-6)   --namespace NAMESPACE [](#__codelineno-49-7)                         Namespace for Bot extension [](#__codelineno-49-8)   --name NAME           Name of the bot extension package [](#__codelineno-49-9)   --version VERSION     Version for Bot extension [](#__codelineno-49-10)   --bots NUM_OF_BOTS    Number of Bots to be added to the package [](#__codelineno-49-11)   --output_dir OUTPUT_DIR [](#__codelineno-49-12)                         Output directory for creating bot package`

*   Following is the syntax for **bot-package generate**

`[](#__codelineno-50-1) rdac bot-package generate --namespace demo --name proactivecasenew --version 23.01.03 --bot 2 --output_dir new11`

Example Output

`[](#__codelineno-51-1) Configure : Custom Bot 1 [](#__codelineno-51-2) [](#__codelineno-51-3) Name*: get-ticket [](#__codelineno-51-4) Bot Type*: source [](#__codelineno-51-5) Number of bot input parameters*: 2 [](#__codelineno-51-6) [](#__codelineno-51-7) Configure : Bot input parameter 1 [](#__codelineno-51-8) [](#__codelineno-51-9) Name*: ticket_id [](#__codelineno-51-10) Type: text [](#__codelineno-51-11) Is mandatory[yes/no]*: yes [](#__codelineno-51-12) [](#__codelineno-51-13) Configure : Bot input parameter 2 [](#__codelineno-51-14) [](#__codelineno-51-15) Name*: source [](#__codelineno-51-16) Type: text [](#__codelineno-51-17) Is mandatory[yes/no]*: yes [](#__codelineno-51-18) [](#__codelineno-51-19) Configure : Custom Bot 2 [](#__codelineno-51-20) [](#__codelineno-51-21) Name*: get-ticket1 [](#__codelineno-51-22) Bot Type*: source [](#__codelineno-51-23) Number of bot input parameters*: 1 [](#__codelineno-51-24) [](#__codelineno-51-25) Configure : Bot input parameter 2 1 [](#__codelineno-51-26) [](#__codelineno-51-27) Name*: ticket_id1 [](#__codelineno-51-28) Type: text [](#__codelineno-51-29) Is mandatory[yes/no]*: yes [](#__codelineno-51-30) Generated: new11/bots.yml`

****Sub Command: `list-runtimes`****

Description: List available Bot Package runtime environments on each worker

`[](#__codelineno-52-1) bot-package list-runtimes --help`

`[](#__codelineno-53-1) optional arguments: [](#__codelineno-53-2)   -h, --help  show this help message and exit [](#__codelineno-53-3)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-53-4)               format`

*   Following is the syntax for **bot-package list-runtimes**

`[](#__codelineno-54-1) rdac bot-package list-runtimes`

Example Output

`[](#__codelineno-55-1) 2022-12-22:09:44:17 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-55-2) +--------------+----------+-------------+-------------+-------------+--------------+----------+ [](#__codelineno-55-3) | Host         | Pod ID   | Site        | Python3.7   | Python3.9   | Python3.10   | Java11   | [](#__codelineno-55-4) |--------------+----------+-------------+-------------+-------------+--------------+----------| [](#__codelineno-55-5) | 05969789d903 | b6bb8486 | rda-site-01 | yes         |             |              |          | [](#__codelineno-55-6) +--------------+----------+-------------+-------------+-------------+--------------+----------+`

### Sub Command: `bots-by-source`

Description: List bots available for given sources

`[](#__codelineno-56-1) rdac bots-by-source --help`

`[](#__codelineno-57-1) Usage: bots-by-source  [-h] [--sources SOURCES] [--group WORKER_GROUP] [](#__codelineno-57-2)             [--site WORKER_SITE] [--lfilter LABEL_FILTER] [](#__codelineno-57-3)             [--rfilter RESOURCE_FILTER] [--maxwait MAX_WAIT] [--json] [](#__codelineno-57-4) [](#__codelineno-57-5) optional arguments: [](#__codelineno-57-6)   -h, --help            show this help message and exit [](#__codelineno-57-7)   --sources SOURCES     Comma separated list of sources to find bots (in [](#__codelineno-57-8)                         addition to built-in sources) [](#__codelineno-57-9)   --group WORKER_GROUP  Deprecated. Use --site option. Specify a worker site [](#__codelineno-57-10)                         name. If not specified, will use any available worker. [](#__codelineno-57-11)   --site WORKER_SITE    Specify a worker site name. If not specified, will use [](#__codelineno-57-12)                         any available worker. [](#__codelineno-57-13)   --lfilter LABEL_FILTER [](#__codelineno-57-14)                         CFXQL style query to narrow down workers using their [](#__codelineno-57-15)                         labels [](#__codelineno-57-16)   --rfilter RESOURCE_FILTER [](#__codelineno-57-17)                         CFXQL style query to narrow down workers using their [](#__codelineno-57-18)                         resources [](#__codelineno-57-19)   --maxwait MAX_WAIT    Maximum wait time (seconds) for credential check to [](#__codelineno-57-20)                         complete. [](#__codelineno-57-21)   --json                Print detailed information in JSON format instead of [](#__codelineno-57-22)                         tabular format`

*   Following is the syntax for **bots-by-source**

 `[](#__codelineno-58-1)  rdac bots-by-source --group rda-site-01 --maxwait 10`

Example Output

`[](#__codelineno-59-1) { [](#__codelineno-59-2)   "status": "started", [](#__codelineno-59-3)   "reason": "", [](#__codelineno-59-4)   "results": [], [](#__codelineno-59-5)   "now": "2023-01-03T06:20:38.129086", [](#__codelineno-59-6)   "status-subject": "tenants.545590daa4ba44a3b32cb3b33f69df13.worker.group.f4a56ba6388c.direct.2d30eab7", [](#__codelineno-59-7)   "jobid": "b244f76f663a4033964301e7c3916ddc" [](#__codelineno-59-8) } [](#__codelineno-59-9) Completed: [](#__codelineno-59-10) Bot                                     Type                  Description                                                                                                                                                                                                                                                                Source [](#__codelineno-59-11) --------------------------------------  --------------------  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  -------- [](#__codelineno-59-12) @c:new-block                            api-endpoint          Start a new block within the pipeline                                                                                                                                                                                                                                      c [](#__codelineno-59-13) @c:simple-loop                          api-endpoint          Start a simple looping block using 'loop_var' as list of values                                                                                                                                                                                                            c [](#__codelineno-59-14) @c:data-loop                            api-endpoint          Start a looping block using 'dataset' name of the saved dataset, and unique values from 'columns'                                                                                                                                                                          c [](#__codelineno-59-15) @c:count-loop                           api-endpoint          Start a looping block that counts from 'start' to 'end' with 'increment' numerical values                                                                                                                                                                                  c [](#__codelineno-59-16) @c:timed-loop                           api-endpoint          Start a looping block that waits 'interval' seconds between each iteration`                               

### Sub Command: `check-credentials`

Description: Perform credential check for one or more sources on a worker pod

`[](#__codelineno-60-1) Usage: check-credentials  [-h] --config CONFIG [--group WORKER_GROUP] [--site WORKER_SITE] [](#__codelineno-60-2)             [--maxwait MAX_WAIT] [](#__codelineno-60-3) [](#__codelineno-60-4) optional arguments: [](#__codelineno-60-5)   -h, --help            show this help message and exit [](#__codelineno-60-6)   --config CONFIG       File containing pipeline contents or configuration [](#__codelineno-60-7)   --group WORKER_GROUP  Deprecated. Use --site. Specify a worker site name. If [](#__codelineno-60-8)                         not specified, will use any available worker. [](#__codelineno-60-9)   --site WORKER_SITE    Specify a worker Site name. If not specified, will use [](#__codelineno-60-10)                         any available worker. [](#__codelineno-60-11)   --maxwait MAX_WAIT    Maximum wait time (seconds) for credential check to [](#__codelineno-60-12)                         complete.`

*   Following is the syntax for **check-credentials**

`[](#__codelineno-61-1) rdac check-credentials --config aws.json --group cfx-lab --maxwait 30`

Example Output

`[](#__codelineno-62-1) Initiating Credential check [](#__codelineno-62-2) { [](#__codelineno-62-3)   "status": "started", [](#__codelineno-62-4)   "reason": "", [](#__codelineno-62-5)   "results": [], [](#__codelineno-62-6)   "now": "2021-07-28T02:12:46.577687", [](#__codelineno-62-7)   "status-subject": "tenants.2dddab0e52544f4eb2de067057aaac31.worker.group.c640b839efec.direct.255941bb", [](#__codelineno-62-8)   "jobid": "328ea2d5f0454ed29b64ccdb287c5626" [](#__codelineno-62-9) } [](#__codelineno-62-10) { [](#__codelineno-62-11)   "jobid": "328ea2d5f0454ed29b64ccdb287c5626", [](#__codelineno-62-12)   "status-subject": "tenants.2dddab0e52544f4eb2de067057aaac31.worker.group.c640b839efec.direct.255941bb" [](#__codelineno-62-13) } [](#__codelineno-62-14) Running:  [](#__codelineno-62-15) Running:  [](#__codelineno-62-16) Running:  [](#__codelineno-62-17) Completed:  [](#__codelineno-62-18) +---------------+---------------+----------+----------+-----------------+ [](#__codelineno-62-19) | Source Name   | Source Type   | Status   | Reason   |   Duration (ms) | [](#__codelineno-62-20) |---------------+---------------+----------+----------+-----------------| [](#__codelineno-62-21) | aws-dev       | aws           | OK       |          |         1473.79 | [](#__codelineno-62-22) | aws-prod      | aws           | OK       |          |         1404.15 | [](#__codelineno-62-23) +---------------+---------------+----------+----------+-----------------+`

### Sub Command: `checksum`

Description: Compute checksums for pipeline contents locally for a given JSON file

`[](#__codelineno-63-1) Usage: checksum  [-h] --pipeline PIPELINE [](#__codelineno-63-2) [](#__codelineno-63-3) optional arguments: [](#__codelineno-63-4)   -h, --help           show this help message and exit [](#__codelineno-63-5)   --pipeline PIPELINE  File containing pipeline information in JSON format`

### Sub Command: `content-to-object`

Description: Convert data from a column into objects

`[](#__codelineno-64-1) Usage: content-to-object  [-h] --inpcol INPUT_CONTENT_COLUMN --outcol OUTPUT_COLUMN --file [](#__codelineno-64-2)             INPUT_FILE --outfolder OUTPUT_FOLDER --outfile OUTPUT_FILE [](#__codelineno-64-3) [](#__codelineno-64-4) optional arguments: [](#__codelineno-64-5)   -h, --help            show this help message and exit [](#__codelineno-64-6)   --inpcol INPUT_CONTENT_COLUMN [](#__codelineno-64-7)                         Name of the column in input that contains the data [](#__codelineno-64-8)   --outcol OUTPUT_COLUMN [](#__codelineno-64-9)                         Column name where object names will be inserted [](#__codelineno-64-10)   --file INPUT_FILE     Input csv filename [](#__codelineno-64-11)   --outfolder OUTPUT_FOLDER [](#__codelineno-64-12)                         Folder name where objects will be stored [](#__codelineno-64-13)   --outfile OUTPUT_FILE [](#__codelineno-64-14)                         Name of output csv file that has object location [](#__codelineno-64-15)                         stored`

### Sub Command: `copy-to-objstore`

Description: Deploy files specified in a ZIP file to the Object Store

`[](#__codelineno-65-1) Usage: copy-to-objstore  [-h] --file ZIP_FILENAME [--verify] [--force] [](#__codelineno-65-2) [](#__codelineno-65-3) optional arguments: [](#__codelineno-65-4)   -h, --help           show this help message and exit [](#__codelineno-65-5)   --file ZIP_FILENAME  ZIP filename (or URL) containing bucket/object entries. [](#__codelineno-65-6)                        If bucket name is 'default', this tool will use the [](#__codelineno-65-7)                        target bucket as specified in configuration. [](#__codelineno-65-8)   --verify             Do not upload files, only verify if the objects in the [](#__codelineno-65-9)                        ZIP file exists on the target object store [](#__codelineno-65-10)   --force              Upload the files even if they exist on the target [](#__codelineno-65-11)                        system with same size`

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

`[](#__codelineno-66-1) rdac dashboard --help`

`[](#__codelineno-67-1) Following are valid sub-commands for dashboard: [](#__codelineno-67-2)   add                       Add or update dashboard [](#__codelineno-67-3)   get                       Get YAML data for a dashboard [](#__codelineno-67-4)   list                      List all dashboards [](#__codelineno-67-5)   convert                   Convert all dashboards from YAML to JSON [](#__codelineno-67-6)   delete                    Delete a dashboard [](#__codelineno-67-7)   enable                    Change the status of a dashboard to 'enabled' [](#__codelineno-67-8)   disable                   Change the status of a dashboard to 'disabled' [](#__codelineno-67-9)   verify                    Verify the dashboard and any pages inside it for PStreams and columns [](#__codelineno-67-10)   to-app                    Convert a tabbed or sectioned dashboard into multi-paged app [](#__codelineno-67-11)   live-edit                 Supports live edit of dashboards using local editor`

****Sub Command: `add`****

Description: Add or update dashboard

`[](#__codelineno-68-1) rdac dashboard add --help`

`[](#__codelineno-69-1) optional arguments: [](#__codelineno-69-2)   -h, --help         show this help message and exit [](#__codelineno-69-3)   --file INPUT_FILE  YAML file containing dashboard definition [](#__codelineno-69-4)   --overwrite        Overwrite even if a dashboard already exists with the [](#__codelineno-69-5)                      specified name.`

Note

Before running the add cmd ,create a yaml file containing dashboard definition

*   Following is the syntax for **dashboard add**

`[](#__codelineno-70-1) rdac dashboard add --file dashboard.yml`

Example Output

`[](#__codelineno-71-1) 2023-01-04:10:24:09 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-71-2) 2023-01-04:10:24:09 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-71-3) 2023-01-04:10:24:09 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-71-4) Added dashboard Appdynamics cpu metrics analysis-shaded chartnew`

****Sub Command: `get`****

Description: Get YAML data for a dashboard

`[](#__codelineno-72-1) rdac dashboard get --help`

`[](#__codelineno-73-1) usage: dashboard [-h] --name DASHBOARD_NAME [](#__codelineno-73-2) [](#__codelineno-73-3) optional arguments: [](#__codelineno-73-4)   -h, --help            show this help message and exit [](#__codelineno-73-5)   --name DASHBOARD_NAME [](#__codelineno-73-6)                         Name of the dashboard`

*   Following is the syntax for **dashboard get**

`[](#__codelineno-74-1) rdac dashboard get --name "Appdynamics cpu metrics analysis-shaded chart"`

Example Output

`[](#__codelineno-75-1) label: Appdynamics CPU metrics [](#__codelineno-75-2) description: Shaded chart for Appdynamics metrics [](#__codelineno-75-3) enabled: true [](#__codelineno-75-4) dashboard_style: tabbed [](#__codelineno-75-5) dashboard_filters: [](#__codelineno-75-6)   time_filter: true [](#__codelineno-75-7)   columns_filter: [] [](#__codelineno-75-8)   group_filters: [] [](#__codelineno-75-9) debug: true [](#__codelineno-75-10) dashboard_sections: [](#__codelineno-75-11) - title: Appdynamics_cpu_metrics [](#__codelineno-75-12)   show_filter: true [](#__codelineno-75-13)   widgets: [](#__codelineno-75-14)   - widget_type: shaded_chart [](#__codelineno-75-15)     title: Appdynamics-cpumetrics [](#__codelineno-75-16)     stream: Appdynamics_cpu_metrics [](#__codelineno-75-17)     ts_column: timestamp [](#__codelineno-75-18)     baseline_column: baseline [](#__codelineno-75-19)     anomalies_column: anomalies [](#__codelineno-75-20)     predicted_column: predicted [](#__codelineno-75-21)     upperBound_column: upperBound [](#__codelineno-75-22)     lowerBound_column: lowerBound [](#__codelineno-75-23)     duration_hours: 5000 [](#__codelineno-75-24)     synchronized-group: 0 [](#__codelineno-75-25)     markers-def: [](#__codelineno-75-26)     - message: Now [](#__codelineno-75-27)       color: '#E53935' [](#__codelineno-75-28)       timestamp: 1647814186 [](#__codelineno-75-29)     - message: Tomorrow [](#__codelineno-75-30)       color: '#E53935' [](#__codelineno-75-31)       timestamp: 1648937386 [](#__codelineno-75-32)     - message: Current [](#__codelineno-75-33)       color: '#E53935' [](#__codelineno-75-34)       timestamp: 1658355595 [](#__codelineno-75-35)     show-markers: true [](#__codelineno-75-36)     downsample: true [](#__codelineno-75-37)     downsample-to-percent: 10 [](#__codelineno-75-38)     downsample-limit-rows: 500 [](#__codelineno-75-39)     widget_id: b0d45ad1 [](#__codelineno-75-40) saved_time: '2022-12-14T06:07:11.835323'`

****Sub Command: `list`****

Description: List all dashboards

`[](#__codelineno-76-1) rdac dashboard list --help`

`[](#__codelineno-77-1) optional arguments: [](#__codelineno-77-2)   -h, --help  show this help message and exit [](#__codelineno-77-3)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-77-4)               format`

*   Following is the syntax for **dashboard list**

`[](#__codelineno-78-1) rdac dashboard list`

Example Output

    `[](#__codelineno-79-1)     name                                                  dashboard_type    label                                                      description                                                                                                                                enabled    saved_time [](#__codelineno-79-2) ---  ----------------------------------------------------  ----------------  ---------------------------------------------------------  -----------------------------------------------------------------------------------------------------------------------------------------  ---------  -------------------------- [](#__codelineno-79-3)   0  rda-mgmt-page-alert-rules                             dashboard         Alert Rules                                                Alert Rules Page                                                                                                                           True       2022-10-06T13:43:06.707246 [](#__codelineno-79-4)   1  rda-mgmt-page-credentials                             dashboard         Credentials                                                Credentials Management Page                                                                                                                True       2022-10-06T13:43:07.346093 [](#__codelineno-79-5)   2  Test_IFRAME                                           dashboard         IFRAME Test                                                ACME Platform Sanity Dash                                                                                                                  False      2022-10-06T13:43:07.367278 [](#__codelineno-79-6)   3  olb-observability-data_page_Incidents                 dashboard         OLB L2/L3 Dashboard, Page: Incidents                       Online Banking App Observability Data for L2/L3 Users, Page: Incidents                                                                     False      2022-11-18T09:24:50.445315 [](#__codelineno-79-7)   4  olb-experience-desk_page_KPIs                         template          Experience Desk Dashboard, Page: KPIs                      Equipped with Events, Alerts and Incidents Information to Maximize Customer Experience and Satisfaction, Page: KPIs                        False      2022-10-06T13:43:07.443675 [](#__codelineno-79-8)   5  ACME_Test_Preview_App                                 template          Test Case Preview                                          Dashboard to preview commits and logs for a test case                                                                                      False      2022-10-06T13:43:07.509264 [](#__codelineno-79-9)   6  l1-service-health                                     template          Service Health - L1 Users                                  L1 Service Health                                                                                                                          False      2022-12-21T05:19:02.332379 [](#__codelineno-79-10)   7  rda-integrations-app                                  app               RDA Integrations                                           Robotic Data Automation Integrations                                                                                                       True       2022-10-06T13:43:07.622712 [](#__codelineno-79-11)   8  l2-l3-dashboard                                       app               L2/L3 Dashboard                                            Dashboard L2/L3 Users                                                                                                                      True       2022-12-21T05:19:02.396260 [](#__codelineno-79-12)   9  rda-dashboard-errors                                  dashboard         Dashboard Errors                                           Query errors in RDA Dashboard widgets                                                                                                      True       2022-10-07T01:49:51.552796 [](#__codelineno-79-13)  10  Appdynamics cpu metrics analysis-shaded chart         dashboard         Appdynamics CPU metrics                                    Shaded chart for Appdynamics metrics                                                                                                       True       2022-12-14T06:07:11.835323`

****Sub Command: `convert`****

Description : Convert all dashboards from YAML to JSON

`[](#__codelineno-80-1) rdac dashboard convert --help`

`[](#__codelineno-81-1) optional arguments: [](#__codelineno-81-2)   -h, --help  show this help message and exit`

*   Following is the syntax for **dashboard convert**

`[](#__codelineno-82-1) rdac dashboard convert`

Example Output

`[](#__codelineno-83-1) Migrating to JSON: rda-mgmt-page-alert-rules [](#__codelineno-83-2) 2023-01-04:05:30:41 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-83-3) 2023-01-04:05:30:41 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-83-4) 2023-01-04:05:30:41 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-83-5) Migrating to JSON: rda-mgmt-page-credentials [](#__codelineno-83-6) Migrating to JSON: Test_IFRAME [](#__codelineno-83-7) Migrating to JSON: olb-observability-data_page_Incidents [](#__codelineno-83-8) Migrating to JSON: olb-experience-desk_page_KPIs [](#__codelineno-83-9) Migrating to JSON: ACME_Test_Preview_App [](#__codelineno-83-10) Migrating to JSON: l1-service-health [](#__codelineno-83-11) Migrating to JSON: rda-integrations-app [](#__codelineno-83-12) Migrating to JSON: l2-l3-dashboard [](#__codelineno-83-13) Migrating to JSON: rda-dashboard-errors [](#__codelineno-83-14) Migrating to JSON: Appdynamics cpu metrics analysis-shaded chart [](#__codelineno-83-15) Migrating to JSON: metric_anomalies_template [](#__codelineno-83-16) Migrating to JSON: olb-engineering-dashboard_page_Metrics [](#__codelineno-83-17) Migrating to JSON: olb-observability-data_page_Metrics__with_Anomalies [](#__codelineno-83-18) Migrating to JSON: olb-observability-data_page_Metric Analysis`

****Sub Command: `delete`****

Description: Delete a dashboard

`[](#__codelineno-84-1) rdac dashboard delete --help`

`[](#__codelineno-85-1) usage: dashboard [-h] --name DASHBOARD_NAME [](#__codelineno-85-2) [](#__codelineno-85-3) optional arguments: [](#__codelineno-85-4)   -h, --help            show this help message and exit [](#__codelineno-85-5)   --name DASHBOARD_NAME [](#__codelineno-85-6)                         Name of the dashboard to delete`

*   Following is the syntax for **dashboard delete**

`[](#__codelineno-86-1) rdac dashboard delete --name 'Appdynamics cpu metrics analysis-shaded chart 2'`

Example Output

`[](#__codelineno-87-1) 2023-01-04:09:34:58 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-87-2) 2023-01-04:09:34:58 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-87-3) 2023-01-04:09:34:58 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-87-4) Deleted dashboard: Appdynamics cpu metrics analysis-shaded chart 2`

****Sub Command: `enable`****

Description: Change the status of a dashboard to 'enabled'

`[](#__codelineno-88-1) rdac dashboard enable --help`

`[](#__codelineno-89-1) usage: dashboard [-h] --name DASHBOARD_NAME [](#__codelineno-89-2) [](#__codelineno-89-3) optional arguments: [](#__codelineno-89-4)   -h, --help            show this help message and exit [](#__codelineno-89-5)   --name DASHBOARD_NAME [](#__codelineno-89-6)                         Name of the dashboard`

*   Following is the syntax for **dashboard enable**

`[](#__codelineno-90-1) rdac dashboard enable --name 'Appdynamics cpu metrics analysis-shaded chart'`

Example Output

`[](#__codelineno-91-1) 2023-01-04:05:45:46 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-91-2) 2023-01-04:05:45:46 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-91-3) 2023-01-04:05:45:46 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-91-4) Changed status of Appdynamics cpu metrics analysis-shaded chart to enabled`

****Sub Command: `disable`****

Description: Change the status of a dashboard to 'disabled'

`[](#__codelineno-92-1) rdac dashboard disable --help`

`[](#__codelineno-93-1) usage: dashboard [-h] --name DASHBOARD_NAME [](#__codelineno-93-2) [](#__codelineno-93-3) optional arguments: [](#__codelineno-93-4)   -h, --help            show this help message and exit [](#__codelineno-93-5)   --name DASHBOARD_NAME [](#__codelineno-93-6)                         Name of the dashboard`

*   Following is the syntax for **dashboard disable**

`[](#__codelineno-94-1) rdac dashboard disable 'Appdynamics cpu metrics analysis-shaded chart'`

Example Output

`[](#__codelineno-95-1) 2023-01-04:05:44:47 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-95-2) 2023-01-04:05:44:47 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-95-3) 2023-01-04:05:44:47 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-95-4) Changed status of Appdynamics cpu metrics analysis-shaded chart to disabled`

****Sub Command: `verify`****

Description: Verify the dashboard and any pages inside it for PStreams and columns

`[](#__codelineno-96-1) rdac dashboard verify --help`

`[](#__codelineno-97-1) usage: dashboard [-h] --name DASHBOARD_NAME [](#__codelineno-97-2) [](#__codelineno-97-3) optional arguments: [](#__codelineno-97-4)   -h, --help            show this help message and exit [](#__codelineno-97-5)   --name DASHBOARD_NAME [](#__codelineno-97-6)                         Name of the dashboard to verify`

*   Following is the syntax for **dashboard verify**

`[](#__codelineno-98-1) rdac dashboard verify --name 'Appdynamics cpu metrics analysis-shaded chart'`

Example Output

`[](#__codelineno-99-1) 2023-01-04:06:28:41 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-99-2) [ [](#__codelineno-99-3)   { [](#__codelineno-99-4)     "dashboard": "Appdynamics cpu metrics analysis-shaded chart", [](#__codelineno-99-5)     "type": "widget", [](#__codelineno-99-6)     "widget_type": "shaded_chart", [](#__codelineno-99-7)     "title": "Appdynamics-cpumetrics", [](#__codelineno-99-8)     "stream": "Appdynamics_cpu_metrics", [](#__codelineno-99-9)     "columns": "timestamp", [](#__codelineno-99-10)     "stream_status": "found", [](#__codelineno-99-11)     "missing_columns": "" [](#__codelineno-99-12)   } [](#__codelineno-99-13) ]`

****Sub Command: `to-app`****

Description: Convert a tabbed or sectioned dashboard into multi-paged app

`[](#__codelineno-100-1) rdac dashboard to-app --help`

`[](#__codelineno-101-1) usage: dashboard [-h] --name DASHBOARD_NAME [](#__codelineno-101-2) [](#__codelineno-101-3) optional arguments: [](#__codelineno-101-4)   -h, --help            show this help message and exit [](#__codelineno-101-5)   --name DASHBOARD_NAME [](#__codelineno-101-6)                         Name of the dashboard`

*   Following is the syntax for **dashboard to-app**

`[](#__codelineno-102-1) rdac dashboard to-app --name rda-microservice-traces`

Example Output

`[](#__codelineno-103-1) Adding new internal dashboard: rda-microservice-traces_page_Traces [](#__codelineno-103-2) 2023-01-04:06:37:48 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-103-3) 2023-01-04:06:37:48 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-103-4) 2023-01-04:06:37:48 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-103-5) Adding new internal dashboard: rda-microservice-traces_page_Healthchecks [](#__codelineno-103-6) Updating dashboard {dashboard_name} as app... [](#__codelineno-103-7) rdauser@manojp-rda-platform:~$`

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

`[](#__codelineno-104-1) rdac dashgroup --help`

`[](#__codelineno-105-1) Following are valid sub-commands for dashgroup: [](#__codelineno-105-2)   add                       Add or update dashboard group [](#__codelineno-105-3)   get                       Get JSON data for a dashboard group [](#__codelineno-105-4)   list                      List all dashboard groups [](#__codelineno-105-5)   delete                    Delete a dashboard group [](#__codelineno-105-6)   enable                    Change the status of a dashboard group to 'enabled' [](#__codelineno-105-7)   disable                   Change the status of a dashboard group to 'disabled'`

****Sub Command: `add`****

Description: Add or update dashboard group

`[](#__codelineno-106-1) rdac dashgroup add --help`

`[](#__codelineno-107-1) usage: dashgroup [-h] --file INPUT_FILE [--overwrite] [](#__codelineno-107-2) [](#__codelineno-107-3) optional arguments: [](#__codelineno-107-4)   -h, --help         show this help message and exit [](#__codelineno-107-5)   --file INPUT_FILE  JSON file containing dashboard group definition [](#__codelineno-107-6)   --overwrite        Overwrite even if a dashboard group already exists with [](#__codelineno-107-7)                      the specified name.`

Note

Before running the add cmd ,create a JSON file containing dashboard group definition

*   Following is the syntax for **dashgroup add**

 `[](#__codelineno-108-1)  rdac dashgroup add --file  dashgroup.json`

Example Output

`[](#__codelineno-109-1) 2023-01-04:11:13:12 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-109-2) 2023-01-04:11:13:12 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-109-3) 2023-01-04:11:13:12 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-109-4) Added dashboard group l1-user new`

****Sub Command: `get`****

Description: Get JSON data for a dashboard group

`[](#__codelineno-110-1) rdac dashgroup get --help`

`[](#__codelineno-111-1) optional arguments: [](#__codelineno-111-2)   -h, --help            show this help message and exit [](#__codelineno-111-3)   --name DASHBOARD_GROUP_NAME [](#__codelineno-111-4)                         Name of the dashboard group`

*   Following is the syntax for **dashgroup get**

 `[](#__codelineno-112-1)  rdac dashgroup get --name l1-users`

Example Output

`[](#__codelineno-113-1) { [](#__codelineno-113-2)     "name": "l1-users", [](#__codelineno-113-3)     "label": "L1 Users", [](#__codelineno-113-4)     "dashboardList": [ [](#__codelineno-113-5)         { [](#__codelineno-113-6)             "id": "user-dashboard-incident-topology", [](#__codelineno-113-7)             "name": "incident-topology" [](#__codelineno-113-8)         }, [](#__codelineno-113-9)         { [](#__codelineno-113-10)             "id": "user-dashboard-incident-metrics", [](#__codelineno-113-11)             "name": "incident-metrics" [](#__codelineno-113-12)         }, [](#__codelineno-113-13)         { [](#__codelineno-113-14)             "id": "user-dashboard-incident-collaboration", [](#__codelineno-113-15)             "name": "incident-collaboration" [](#__codelineno-113-16)         }, [](#__codelineno-113-17)         { [](#__codelineno-113-18)             "id": "user-dashboard-l1-main-app", [](#__codelineno-113-19)             "name": "l1-main-app" [](#__codelineno-113-20)         } [](#__codelineno-113-21)     ], [](#__codelineno-113-22)     "users": "l1-user@cfx.com", [](#__codelineno-113-23)     "enabled": true, [](#__codelineno-113-24)     "description": "Dashboards for L1 Users", [](#__codelineno-113-25)     "saved_time": "2022-09-28T05:56:11.325672" [](#__codelineno-113-26) }`

****Sub Command: `list`****

Description: List all dashboard groups

`[](#__codelineno-114-1) rdac dashgroup list --help`

`[](#__codelineno-115-1) usage: dashgroup [-h] [--json] [](#__codelineno-115-2) [](#__codelineno-115-3) optional arguments: [](#__codelineno-115-4)   -h, --help  show this help message and exit [](#__codelineno-115-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-115-6)               format`

*   Following is the syntax for **dashgroup list**

`[](#__codelineno-116-1) rdac dashgroup list`

Example Output

    `[](#__codelineno-117-1)     name                     label                description                               enabled    saved_time [](#__codelineno-117-2) --  -----------------------  -------------------  ----------------------------------------  ---------  -------------------------- [](#__codelineno-117-3)  0  Test                     Admin Group                                                    True       2022-12-21T16:59:47.419691 [](#__codelineno-117-4)  1  l1-users                 L1 Users             Dashboards for L1 Users                   True       2022-09-28T05:56:11.325672 [](#__codelineno-117-5)  2  executives               Executives           Dashboards for Executives                 True       2022-09-29T03:00:33.425663 [](#__codelineno-117-6)  3  Experience Desk          Experience Desk      Dashboards for Experience Desk            True       2022-09-28T05:56:05.969015 [](#__codelineno-117-7)  4  DevOps                   Users                                                          True       2022-09-28T19:21:38.852671 [](#__codelineno-117-8)  5  TestGroup                TestGroup                                                      True       2022-09-28T03:59:14.609687 [](#__codelineno-117-9)  6  Reression Training Test  Admin Group                                                    False      2022-09-28T05:56:07.802828 [](#__codelineno-117-10)  7  Partner                  Admin                All Partner Dashboards                    True       2022-09-28T05:56:06.961122 [](#__codelineno-117-11)  8  Acme                     Acme                                                           True       2022-10-23T22:03:29.461241 [](#__codelineno-117-12)  9  bizops                   Business Operations  Dashboards for Business Operations Users  True       2022-09-29T03:11:06.780365 [](#__codelineno-117-13) 10  l2-users                 L2 Users             Dashboards for L2 Users                   True       2022-09-28T05:56:12.239130 [](#__codelineno-117-14) 11  l1-l3 Dashboard          l1-l3 Dashboard                                                True       2022-12-21T05:28:23.966417 [](#__codelineno-117-15) 12  Biz Command Center       Biz Command Center   Dashboards for Biz Command Center         True       2022-09-28T05:56:03.338590 [](#__codelineno-117-16) 13  Engineering              Engineering Group    Dashboards for Engineering Group          True       2022-09-28T05:56:05.072187`

****Sub Command: `delete`****

Description: Delete a dashboard group

`[](#__codelineno-118-1) rdac dashgroup delete --help`

`[](#__codelineno-119-1) usage: dashgroup [-h] --name DASHBOARD_GROUP_NAME [](#__codelineno-119-2) [](#__codelineno-119-3) optional arguments: [](#__codelineno-119-4)   -h, --help            show this help message and exit [](#__codelineno-119-5)   --name DASHBOARD_GROUP_NAME [](#__codelineno-119-6)                         Name of the dashboard group to delete`

*   Following is the syntax for **dashgroup delete**

 `[](#__codelineno-120-1)  rdac dashgroup delete --name 'synthetics-control'`

Example Output

`[](#__codelineno-121-1) 2023-01-04:12:02:37 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-121-2) 2023-01-04:12:02:37 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-121-3) 2023-01-04:12:02:37 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-121-4) Deleted dashboard group: synthetics-control`

****Sub Command: `enable`****

Description: Change the status of a dashboard group to 'enabled'

`[](#__codelineno-122-1) rdac dashgroup enable --help`

`[](#__codelineno-123-1) usage: dashgroup [-h] --name DASHBOARD_GROUP_NAME [](#__codelineno-123-2) [](#__codelineno-123-3) optional arguments: [](#__codelineno-123-4)   -h, --help            show this help message and exit [](#__codelineno-123-5)   --name DASHBOARD_GROUP_NAME [](#__codelineno-123-6)                         Name of the dashboard group`

*   Following is the syntax for **dashgroup enable**

`[](#__codelineno-124-1) rdac dashgroup enable --name l1-users`

Example Output

`[](#__codelineno-125-1) 2023-01-04:10:54:08 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-125-2) 2023-01-04:10:54:08 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-125-3) 2023-01-04:10:54:08 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-125-4) Changed status of l1-users to enabled`

****Sub Command: `disable`****

Description: Change the status of a dashboard group to 'disabled'

`[](#__codelineno-126-1) rdac dashgroup disable --help`

`[](#__codelineno-127-1) usage: dashgroup [-h] --name DASHBOARD_GROUP_NAME [](#__codelineno-127-2) [](#__codelineno-127-3) optional arguments: [](#__codelineno-127-4)   -h, --help            show this help message and exit [](#__codelineno-127-5)   --name DASHBOARD_GROUP_NAME [](#__codelineno-127-6)                         Name of the dashboard group`

*   Following is the syntax for **dashgroup disable**

`[](#__codelineno-128-1) rdac dashgroup disable --name l1-users`

Example Output

`[](#__codelineno-129-1) 2023-01-04:10:53:16 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-129-2) 2023-01-04:10:53:16 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-129-3) 2023-01-04:10:53:16 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-129-4) Changed status of l1-users to disabled`

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

`[](#__codelineno-130-1) rdac dataset --help`

`[](#__codelineno-131-1) Dataset management commands [](#__codelineno-131-2) [](#__codelineno-131-3) Following are valid sub-commands for dataset: [](#__codelineno-131-4)   list                      List datasets from the object store [](#__codelineno-131-5)   get                       Download a dataset from the object store [](#__codelineno-131-6)   meta                      Download metadata for a dataset from the object store [](#__codelineno-131-7)   add                       Add a new dataset to the object store [](#__codelineno-131-8)   delete                    Delete a dataset from the object store [](#__codelineno-131-9)   bounded-list              List bounded datasets from the object store [](#__codelineno-131-10)   bounded-get               Download a bounded dataset from the object store [](#__codelineno-131-11)   bounded-meta              Download metadata for a bounded dataset from the object store [](#__codelineno-131-12)   bounded-add               Add a new bounded dataset to the system [](#__codelineno-131-13)   bounded-import            Import the data for a bounded dataset and store it in the object store [](#__codelineno-131-14)   bounded-delete            Delete a bounded dataset from the object store`

****Sub Command: `list`****

Description: List datasets from the object store

`[](#__codelineno-132-1) rdac dataset list --help`

`[](#__codelineno-133-1) usage: dataset [-h] [--json] [](#__codelineno-133-2) [](#__codelineno-133-3) optional arguments: [](#__codelineno-133-4)   -h, --help  show this help message and exit [](#__codelineno-133-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-133-6)               format`

*   Following is the syntax for **dataset list**

`[](#__codelineno-134-1) rdac dataset list`

Example Output

     `[](#__codelineno-135-1)      name                                                    format      mem_size_mb    num_rows    num_columns  saved_time [](#__codelineno-135-2) ---  ------------------------------------------------------  --------  -------------  ----------  -------------  -------------------------- [](#__codelineno-135-3)   0  Appdynamics_cpu_metrics                                 csv               0.092        1000             12  2022-12-14T05:48:07.940815 [](#__codelineno-135-4)   1  Appdynamics_cpu_metrics_new                             csv               0.092        1000             12  2023-01-04T12:00:17.628034 [](#__codelineno-135-5)   2  Balancing_Control_to_Platform_Standardizer              csv               0               1              3  2022-10-19T00:32:51.328289 [](#__codelineno-135-6)   3  DATASET-SERVICEWOW                                      csv               0.015        2000              1  2022-10-13T14:35:08.843641 [](#__codelineno-135-7)   4  Data_Masking_to_hive_load                               csv               0               1              3  2022-10-19T00:32:51.657829 [](#__codelineno-135-8)   5  Data_Parsing_to_Balancing_Control                       csv               0               1              3  2022-10-19T00:32:51.213174 [](#__codelineno-135-9)   6  Feed_Data_Standardizer_to_Data_Masking                  csv               0               1              3  2022-10-19T00:32:51.550645 [](#__codelineno-135-10)   7  Metadata_Validator_to_Preprocessing                     csv               0               1              3  2022-10-19T00:32:50.999017 [](#__codelineno-135-11)   8  Online_Banking_Stack_Metrics                            csv               0.001           6             12  2022-09-29T04:01:45.875869 [](#__codelineno-135-12)   9  Platform_Standardizer_to_Feed_Data_Standardizer         csv               0               1              3  2022-10-19T00:32:51.433995 [](#__codelineno-135-13)  10  Preprocessing_to_Data_Parsing                           csv               0               1              3  2022-10-19T00:32:51.101942 [](#__codelineno-135-14)  11  SS-AWS-event-groups                                     csv               0               3              9  2022-11-08T14:39:47.207992`

****Sub Command: `get`****

Description: Download a dataset from the object store

`[](#__codelineno-136-1) rdac dataset get --help`

`[](#__codelineno-137-1) usage: dataset [-h] --name NAME [--tofile SAVE_TO_FILE] [--json] [](#__codelineno-137-2)                [--format DATA_FORMAT] [--viz] [](#__codelineno-137-3) [](#__codelineno-137-4) optional arguments: [](#__codelineno-137-5)   -h, --help            show this help message and exit [](#__codelineno-137-6)   --name NAME           Dataset name [](#__codelineno-137-7)   --tofile SAVE_TO_FILE [](#__codelineno-137-8)                         Save the data to the specified file (CSV or JSON if [](#__codelineno-137-9)                         --json is specified) [](#__codelineno-137-10)   --json                Export data as a JSON formatted rows. ** Deprecated. [](#__codelineno-137-11)                         Use --format ** [](#__codelineno-137-12)   --format DATA_FORMAT  Save the downloaded data in the specified format. [](#__codelineno-137-13)                         Valid values are csv, json, parquet. If format is [](#__codelineno-137-14)                         'auto', format is determined from extension [](#__codelineno-137-15)   --viz                 Open Dataframe visualizer to show the data`

*   Following is the syntax for **dataset get**

`[](#__codelineno-138-1) rdac dataset get --name Online_Banking_Stack_Metrics --viz`

Example Output

`[](#__codelineno-139-1) Downloaded dataset. Number of Rows: 6, Columns: 12 [](#__codelineno-139-2) [DFViz:1] Rows 6, Cols 12 | View Rows 0-6, Cols: 0-4 | Press 'q' to exit, '?' for help [](#__codelineno-139-3)           Data Filter:  | Col Filter:  | Data Sort:  | cfxql: [](#__codelineno-139-4) +----+-------------+----------+-----------------------+-----------------------------+--------------------------+ [](#__codelineno-139-5) |    | component   | count_   | layer                 | metric_name                 | node_id                  | [](#__codelineno-139-6) |----+-------------+----------+-----------------------+-----------------------------+--------------------------| [](#__codelineno-139-7) |  0 |             |          | Application Component | db_slow_queries             | 10.95.134.103_Database   | [](#__codelineno-139-8) |  1 |             |          | Application Component | total_response_time         | 10.95.134.101_Webserver  | [](#__codelineno-139-9) |  2 |             |          | Application Component | consumer_lag                | 10.95.134.104_MessageBus | [](#__codelineno-139-10) |  3 |             |          | Application Component | under_replicated_partitions | 10.95.134.104_MessageBus | [](#__codelineno-139-11) |  4 |             |          | Application Component | db_connections              | 10.95.134.103_Database   | [](#__codelineno-139-12) |  5 |             |          | Application Component | transaction_time            | 10.95.134.102_Appserver  | [](#__codelineno-139-13) +----+-------------+----------+-----------------------+-----------------------------+--------------------------+`

****Sub Command: `meta`****

Description: Download metadata for a dataset from the object store

`[](#__codelineno-140-1) rdac dataset meta --help`

`[](#__codelineno-141-1) usage: dataset [-h] --name NAME [](#__codelineno-141-2) [](#__codelineno-141-3) optional arguments: [](#__codelineno-141-4)   -h, --help   show this help message and exit [](#__codelineno-141-5)   --name NAME  Dataset name`

*   Following is the syntax for **dataset meta**

`[](#__codelineno-142-1) rdac dataset meta --name Online_Banking_Stack_Metrics`

Example Output

`[](#__codelineno-143-1) { [](#__codelineno-143-2)   "name": "Online_Banking_Stack_Metrics", [](#__codelineno-143-3)   "format": "csv", [](#__codelineno-143-4)   "datafile": "cfxdm-saved-data/Online_Banking_Stack_Metrics-data.csv", [](#__codelineno-143-5)   "mem_size_mb": 0.001, [](#__codelineno-143-6)   "num_rows": 6, [](#__codelineno-143-7)   "num_columns": 12, [](#__codelineno-143-8)   "saved_time": "2022-09-29T04:01:45.875869", [](#__codelineno-143-9)   "dtypes": { [](#__codelineno-143-10)     "component": "float64", [](#__codelineno-143-11)     "count_": "float64", [](#__codelineno-143-12)     "layer": "object", [](#__codelineno-143-13)     "metric_name": "object", [](#__codelineno-143-14)     "node_id": "object", [](#__codelineno-143-15)     "node_label": "object", [](#__codelineno-143-16)     "node_type": "object", [](#__codelineno-143-17)     "source_tool": "object", [](#__codelineno-143-18)     "stack_name": "object", [](#__codelineno-143-19)     "timestamp": "object", [](#__codelineno-143-20)     "unit": "object", [](#__codelineno-143-21)     "value": "float64" [](#__codelineno-143-22)   } [](#__codelineno-143-23) }`

****Sub Command: `add`****

Description: Add a new dataset to the object store

`[](#__codelineno-144-1) rdac dataset add --help`

`[](#__codelineno-145-1) usage: dataset [-h] [--folder FOLDER] --name NAME --file INPUT_FILE [](#__codelineno-145-2)                [--local_format LOCAL_FORMAT] [--remote_format REMOTE_FORMAT] [](#__codelineno-145-3) [](#__codelineno-145-4) optional arguments: [](#__codelineno-145-5)   -h, --help            show this help message and exit [](#__codelineno-145-6)   --folder FOLDER       Dataset Folder [](#__codelineno-145-7)   --name NAME           Dataset name [](#__codelineno-145-8)   --file INPUT_FILE     CSV or parquet formatted file from which dataset will [](#__codelineno-145-9)                         be added [](#__codelineno-145-10)   --local_format LOCAL_FORMAT [](#__codelineno-145-11)                         Local file format (auto or csv or parquet or json). [](#__codelineno-145-12)                         'auto' means format will be determined from filename [](#__codelineno-145-13)                         extension [](#__codelineno-145-14)   --remote_format REMOTE_FORMAT [](#__codelineno-145-15)                         Remote file format (csv or parquet).`

*   Following is the syntax for **dataset add**

`[](#__codelineno-146-1) rdac dataset add --name metricsdata --file metrics.csv --local_format auto`

Example Output

`[](#__codelineno-147-1) Loaded dataset from file. Number of Rows: 100000, Columns: 13 [](#__codelineno-147-2) Dataset 'metricsdata' not found in the object storage. [](#__codelineno-147-3) 2023-01-05:05:13:37 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-147-4) 2023-01-05:05:13:37 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-147-5) 2023-01-05:05:13:37 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-147-6) [](#__codelineno-147-7) Added dataset 'metricsdata'`

****Sub Command: `delete`****

Description: Delete a dataset from the object store

`[](#__codelineno-148-1) rdac dataset delete --help`

`[](#__codelineno-149-1) usage: dataset [-h] --name NAME [--yes] [](#__codelineno-149-2) [](#__codelineno-149-3) optional arguments: [](#__codelineno-149-4)   -h, --help   show this help message and exit [](#__codelineno-149-5)   --name NAME  Dataset name [](#__codelineno-149-6)   --yes        Delete without prompting`

*   Following is the syntax for **dataset delete**

`[](#__codelineno-150-1) rdac dataset delete --name metricsdata`

Example Output

`[](#__codelineno-151-1) Confirm deletion of dataset (y/n)? y [](#__codelineno-151-2) 2023-01-05:05:21:39 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-151-3) 2023-01-05:05:21:39 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-151-4) 2023-01-05:05:21:39 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem`

****Sub Command: `bounded-list`****

Description: List bounded datasets from the object store

`[](#__codelineno-152-1) rdac dataset bounded-list --help`

`[](#__codelineno-153-1) usage: dataset [-h] [--json] [](#__codelineno-153-2) [](#__codelineno-153-3) optional arguments: [](#__codelineno-153-4)   -h, --help  show this help message and exit [](#__codelineno-153-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-153-6)               format`

*   Following is the syntax for **dataset bounded-list**

`[](#__codelineno-154-1) rdac dataset bounded-list`

Example Output

   `[](#__codelineno-155-1)    drafts      mem_size_mb  name         num_columns    num_rows  saved_time                  schema [](#__codelineno-155-2) --  --------  -------------  ---------  -------------  ----------  --------------------------  --------- [](#__codelineno-155-3)  0  []                    0  Schema-QA              6           0  2023-01-05T04:39:16.255705  Schema-QA [](#__codelineno-155-4)  1  []                    0  Test                   3           0  2023-01-05T04:39:24.660053  Test`

****Sub Command: `bounded-get`****

Description: Download a bounded dataset from the object store

`[](#__codelineno-156-1) rdac dataset bounded-get --help`

`[](#__codelineno-157-1) usage: dataset [-h] --name NAME [--tofile SAVE_TO_FILE] [--format DATA_FORMAT] [](#__codelineno-157-2)                [--viz] [](#__codelineno-157-3) [](#__codelineno-157-4) optional arguments: [](#__codelineno-157-5)   -h, --help            show this help message and exit [](#__codelineno-157-6)   --name NAME           Dataset name [](#__codelineno-157-7)   --tofile SAVE_TO_FILE [](#__codelineno-157-8)                         Save the data to the specified file (CSV or JSON if [](#__codelineno-157-9)                         --json is specified) [](#__codelineno-157-10)   --format DATA_FORMAT  Save the downloaded data in the specified format. [](#__codelineno-157-11)                         Valid values are csv, json, parquet. If format is [](#__codelineno-157-12)                         'auto', format is determined from extension [](#__codelineno-157-13)   --viz                 Open Dataframe visualizer to show the data`

*   Following is the syntax for **dataset bounded-get**

`[](#__codelineno-158-1) rdac dataset bounded-get --name Schema-QA --viz`

Example Output

`[](#__codelineno-159-1) Downloaded bounded dataset. Number of Rows: 0, Columns: 7 [](#__codelineno-159-2) [DFViz:1] Rows 0, Cols 7 | View Rows 0-0, Cols: 0-4 | Press 'q' to exit, '?' for help [](#__codelineno-159-3)           Data Filter:  | Col Filter:  | Data Sort:  | cfxql: [](#__codelineno-159-4) +--------+--------+--------+--------------+-------+ [](#__codelineno-159-5) | text   | enum   | bool   | enum_array   | int   | [](#__codelineno-159-6) |--------+--------+--------+--------------+-------| [](#__codelineno-159-7) +--------+--------+--------+--------------+-------+`

****Sub Command: `bounded-meta`****

Description: Download metadata for a bounded dataset from the object store

`[](#__codelineno-160-1) rdac dataset bounded-meta --help`

`[](#__codelineno-161-1) usage: dataset [-h] --name NAME [](#__codelineno-161-2) [](#__codelineno-161-3) optional arguments: [](#__codelineno-161-4)   -h, --help   show this help message and exit [](#__codelineno-161-5)   --name NAME  Dataset name`

\* Following is the syntax for **dataset bounded-meta**

`[](#__codelineno-162-1) rdac dataset bounded-meta --name Schema-QA`

Example Output

`[](#__codelineno-163-1) { [](#__codelineno-163-2)   "name": "Schema-QA", [](#__codelineno-163-3)   "mem_size_mb": 0, [](#__codelineno-163-4)   "num_rows": 0, [](#__codelineno-163-5)   "drafts": [], [](#__codelineno-163-6)   "saved_time": "2023-01-05T04:39:16.255705", [](#__codelineno-163-7)   "schema": "Schema-QA", [](#__codelineno-163-8)   "num_columns": 6 [](#__codelineno-163-9) }`

****Sub Command: `bounded-add`****

Description: Add a new bounded dataset to the system

`[](#__codelineno-164-1) rdac dataset bounded-add --help`

`[](#__codelineno-165-1) usage: dataset [-h] --name NAME --schema SCHEMA_NAME [](#__codelineno-165-2) [](#__codelineno-165-3) optional arguments: [](#__codelineno-165-4)   -h, --help            show this help message and exit [](#__codelineno-165-5)   --name NAME           Dataset name [](#__codelineno-165-6)   --schema SCHEMA_NAME  Validate data against given schema. When schema is [](#__codelineno-165-7)                         given, the dataset is added as 'schema bounded [](#__codelineno-165-8)                         dataset'.`

*   Following is the syntax for **dataset bounded-add**

`[](#__codelineno-166-1) rdac dataset bounded-add --name 'Example Schema' --schema 'Example Schema'`

Example Output

`[](#__codelineno-167-1) 2023-01-05:04:54:02 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-167-2) 2023-01-05:04:54:02 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-167-3) 2023-01-05:04:54:02 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-167-4) Successfully added bounded dataset Example Schema`

****Sub Command: `bounded-delete`****

Description: Delete a bounded dataset from the object store

`[](#__codelineno-168-1) rdac dataset bounded-delete --help`

`[](#__codelineno-169-1) usage: dataset [-h] --name NAME [--yes] [](#__codelineno-169-2) [](#__codelineno-169-3) optional arguments: [](#__codelineno-169-4)   -h, --help   show this help message and exit [](#__codelineno-169-5)   --name NAME  Dataset name [](#__codelineno-169-6)   --yes        Delete without prompting`

\* Following is the syntax for **dataset bounded-delete**

`[](#__codelineno-170-1) rdac dataset bounded-delete --name 'Example Schema'`

`[](#__codelineno-171-1) Confirm deletion of dataset (y/n)? y [](#__codelineno-171-2) Successfully deleted all drafts of Example Schema [](#__codelineno-171-3) 2023-01-05:04:55:43 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-171-4) 2023-01-05:04:55:43 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-171-5) 2023-01-05:04:55:43 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-171-6) Successfully deleted bounded data set Example Schema`

****Sub Command: `bounded-import`****

Description: Import the data for a bounded dataset and store it in the object store

`[](#__codelineno-172-1) rdac dataset bounded-import --help`

`[](#__codelineno-173-1) usage: dataset [-h] --name NAME --file INPUT_FILE [](#__codelineno-173-2)                [--local_format LOCAL_FORMAT] [--yes] [--json] [](#__codelineno-173-3) [](#__codelineno-173-4) optional arguments: [](#__codelineno-173-5)   -h, --help            show this help message and exit [](#__codelineno-173-6)   --name NAME           Dataset name [](#__codelineno-173-7)   --file INPUT_FILE     CSV or parquet formatted file from which dataset will [](#__codelineno-173-8)                         be added [](#__codelineno-173-9)   --local_format LOCAL_FORMAT [](#__codelineno-173-10)                         Local file format (auto or csv or parquet or json). [](#__codelineno-173-11)                         'auto' means format will be determined from filename [](#__codelineno-173-12)                         extension [](#__codelineno-173-13)   --yes                 Delete without prompting [](#__codelineno-173-14)   --json                Print detailed information in JSON format instead of [](#__codelineno-173-15)                         tabular format`

*   Following is the syntax for **dataset bounded-import**

`[](#__codelineno-174-1) rdac dataset bounded-import --name Test --file metrics.csv`

Example Output

`[](#__codelineno-175-1) rdac dataset add --name metricsdata --file metrics.csv --local_format auto`

### Sub Command: `demo`

**Following are the valid Sub-Commands for the demo**

| Sub Commands | Description |
| --- | --- |
| backup | Export dashboards and all related artifact meta data in to a folder |
| setup | Setup a target system for demo |
| diff | Compare two backup directories |

`[](#__codelineno-176-1) rdac demo--help`

`[](#__codelineno-177-1) Demo related commands [](#__codelineno-177-2) [](#__codelineno-177-3) Following are valid sub-commands for demo: [](#__codelineno-177-4)   backup                    Export dashboards and all related artifact meta data in to a folder [](#__codelineno-177-5)   setup                     Setup a target system for demo [](#__codelineno-177-6)   diff                      Compare two backup directories`

Example

`[](#__codelineno-178-1) rdac demo backup --to_dir <foldername>`

`[](#__codelineno-179-1) tar -cvzf filename.tar.gz <foldername>/`

Note

To create `demo.tar.gz` file from the output folder use the below mentioned commands

`[](#__codelineno-180-1) cd demo`

`[](#__codelineno-181-1) tar -cvzf /tmp/demo.tar.gz .`

****Sub Command: `backup`****

Description: Export dashboards and all related artifact meta data in to a folder

`[](#__codelineno-182-1) rdac demo backup --help`

`[](#__codelineno-183-1) usage: demo [-h] --to_dir TO_DIR [--yaml] [](#__codelineno-183-2) [](#__codelineno-183-3) optional arguments: [](#__codelineno-183-4)   -h, --help       show this help message and exit [](#__codelineno-183-5)   --to_dir TO_DIR  Output directory [](#__codelineno-183-6)   --yaml           Export in YAML format (default is JSON)`

*   Following is the syntax for **demo backup**

`[](#__codelineno-184-1) rdac demo backup --to_dir demo`

Example Output

`[](#__codelineno-185-1) Backing up 109 Dashboards [](#__codelineno-185-2) Backing up 16 Dashboard Groups [](#__codelineno-185-3) Backing up 52 Published Pipelines [](#__codelineno-185-4) Backing up 11 Blueprints [](#__codelineno-185-5) Backing up 4 Synthetic Profiles [](#__codelineno-185-6) Backing up 4 Stacks used in Synthetic Profiles [](#__codelineno-185-7) 2023-01-05:06:31:18 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-185-8) Backing up 16 Endpoints [](#__codelineno-185-9) Backing up 9 Mappings [](#__codelineno-185-10) Backing up 98 Persistent Streams`

****Sub Command: `diff`****

Description: Compare two backup directories

`[](#__codelineno-186-1) rdac demo diff --help`

`[](#__codelineno-187-1) usage: demo [-h] --first FIRST --second SECOND [--details] [--side] [](#__codelineno-187-2)             [--no_ident] [--opts OPTIONS] [](#__codelineno-187-3) [](#__codelineno-187-4) optional arguments: [](#__codelineno-187-5)   -h, --help       show this help message and exit [](#__codelineno-187-6)   --first FIRST    First Directory where demo setup artifacts are stored. [](#__codelineno-187-7)   --second SECOND  Second Directory where demo setup artifacts are stored. [](#__codelineno-187-8)   --details        Show detailed diffs between files [](#__codelineno-187-9)   --side           While Showing diffs use side-by-side format [](#__codelineno-187-10)   --no_ident       Exclude Identical Objects from output [](#__codelineno-187-11)   --opts OPTIONS   Comma separated list of artifacts names to restrict: stacks [](#__codelineno-187-12)                    (st), pstreams (ps), dashboards (d), dashboard_groups [](#__codelineno-187-13)                    (dg),synthetic_profiles (syn)`

*   Following is the syntax for **demo diff**

 `[](#__codelineno-188-1)  rdac demo diff --first demo --second demo2`

Example Output

`[](#__codelineno-189-1) Dashboard        l1-main-app                                        Identical [](#__codelineno-189-2) Dashboard        olb-engineering-dashboard_page_Metric Analysis     Identical [](#__codelineno-189-3) Dashboard        rda-mgmt-page-blueprints                           Identical [](#__codelineno-189-4) Dashboard        olb-business-command-center                        Identical [](#__codelineno-189-5) Dashboard        rda-microservice-traces_page_Healthchecks          Identical [](#__codelineno-189-6) Dashboard        rda-mgmt-page-stagingarea                          Identical [](#__codelineno-189-7) Dashboard        incident-metrics                                   Identical [](#__codelineno-189-8) Dashboard        ss_ch_all_sources                                  Identical [](#__codelineno-189-9) Dashboard        alert-incident-summary                             Identical [](#__codelineno-189-10) Dashboard        l2-l3-incidents                                    Identical [](#__codelineno-189-11) Dashboard        olb-observability-data_page_Metric Analysis        Identical [](#__codelineno-189-12) Dashboard        incident-topology                                  Identical [](#__codelineno-189-13) Dashboard        olb-bizops-observability_page_Incidents_network    Identical [](#__codelineno-189-14) Dashboard        ss_ch_pal_page_Analytics                           Identical [](#__codelineno-189-15) Dashboard        olb-bizops-observability                           Identical`

*   Following is the syntax No.2 for **demo diff**

 `[](#__codelineno-190-1)  rdac demo diff --first demo --second demo2 --no_ident`

Example Output No.2

`[](#__codelineno-191-1) 286 Identical, 0 Only In First, 0 Only In Second, 0 Differ`

****Sub Command: `setup`****

Description: Setup a target system for demo

`[](#__codelineno-192-1) rdac demo setup --help`

`[](#__codelineno-193-1) usage: demo [-h] --dir FOLDER --ip PLATFORM_IP [--port WEBHOOK_PORT] [](#__codelineno-193-2)             [--protocol  WEBHOOK_PROTO] [--pipelines PIPELINES] [](#__codelineno-193-3)             [--blueprints BLUEPRINTS] [--verify_only] [](#__codelineno-193-4) [](#__codelineno-193-5) optional arguments: [](#__codelineno-193-6)   -h, --help            show this help message and exit [](#__codelineno-193-7)   --dir FOLDER          Directory where demo setup artifacts are stored. Most [](#__codelineno-193-8)                         contain a settings.json in that folder [](#__codelineno-193-9)   --ip PLATFORM_IP      Target platform Public IP Address [](#__codelineno-193-10)   --port WEBHOOK_PORT   Port for webhook server (Default 7443) [](#__codelineno-193-11)   --protocol  WEBHOOK_PROTO [](#__codelineno-193-12)                         Protocol for Webhook server (Default https) [](#__codelineno-193-13)   --pipelines PIPELINES [](#__codelineno-193-14)                         Comma seperated list of Pipeline names to deploy them [](#__codelineno-193-15)                         alone [](#__codelineno-193-16)   --blueprints BLUEPRINTS [](#__codelineno-193-17)                         Comma seperated list of Blueprint names to deploy them [](#__codelineno-193-18)                         alone [](#__codelineno-193-19)   --verify_only         Verify Only. Do not push changes to target system`

*   Following is the syntax for **demo setup**

`[](#__codelineno-194-1) rdac demo setup --dir demo --ip 10.95.122.127`

Example Output

`[](#__codelineno-195-1) WARNING: dashboards directory not found, skipping [](#__codelineno-195-2) WARNING: dashboard_groups directory not found, skipping [](#__codelineno-195-3) WARNING: stacks directory not found, skipping [](#__codelineno-195-4) WARNING: synthetic_profiles directory not found, skipping [](#__codelineno-195-5) WARNING: persistent_streams directory not found, skipping [](#__codelineno-195-6) WARNING: pipelines directory not found, skipping [](#__codelineno-195-7) WARNING: blueprints directory not found, skipping [](#__codelineno-195-8) WARNING: endpoints directory not found, skipping [](#__codelineno-195-9) WARNING: mappings directory not found, skipping [](#__codelineno-195-10) Performing Audit ... [](#__codelineno-195-11) 2023-01-05:06:22:58 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-195-12) Skipping audit for pstreams [](#__codelineno-195-13) Skipping audit for dashboards [](#__codelineno-195-14) Skipping audit for Dashboard Groups [](#__codelineno-195-15) Skipping audit for Stacks [](#__codelineno-195-16) Skipping audit for Synthetic Profiles [](#__codelineno-195-17) Skipping audit for Publish Pipelines [](#__codelineno-195-18) Skipping audit for Blueprints [](#__codelineno-195-19) [](#__codelineno-195-20) Everyhing configured (Total Checks 2)`

### Sub Command: `bundle-deploy`

`[](#__codelineno-196-1) rdac bundle-deploy --help`

`[](#__codelineno-197-1) optional arguments: [](#__codelineno-197-2)   -h, --help          show this help message and exit [](#__codelineno-197-3)   --file BUNDLE_FILE  Bundle file to be deployed. Must be in .tar.gz format [](#__codelineno-197-4)   --type TYPE         Deploy only specified types. Comma separated list. (d: [](#__codelineno-197-5)                       dashboard, b: blueprint, p: pipeline) [](#__codelineno-197-6)   --compare           Compare bundle vs currently deployed. Do not deploy any [](#__codelineno-197-7)                       artifact`

Example

`[](#__codelineno-198-1) rdac bundle-deploy --file demo.tar.gz --type p`

Example Output

`[](#__codelineno-199-1) Deployed following artifacts from this bundle: [](#__codelineno-199-2) [](#__codelineno-199-3)     type      name [](#__codelineno-199-4) --  --------  --------------------------------------------------- [](#__codelineno-199-5)  0  pipeline  vmware_vcenter_inventory_pipeline_v1_c1 [](#__codelineno-199-6)  1  pipeline  vmware_vcenter_inventory_topology_pipeline_v1_c2 [](#__codelineno-199-7)  2  pipeline  windows_host_os_system_inventory_and_topology_v1_c1 [](#__codelineno-199-8)  3  pipeline  irm-stream-missing-columns-update [](#__codelineno-199-9)  4  pipeline  netapp_cmode_storage_arrays_inventory_v1 [](#__codelineno-199-10)  5  pipeline  vmware_vcenter_inventory_pipeline_v1_c2 [](#__codelineno-199-11)  6  pipeline  vmware_vcenter_inventory_topology_pipeline_v1_c1 [](#__codelineno-199-12)  7  pipeline  linux_host_os_system_inventory_and_topology_v1_c2 [](#__codelineno-199-13)  8  pipeline  linux_host_os_system_inventory_and_topology_v1_c3 [](#__codelineno-199-14)  9  pipeline  oia-sources-streams-merge [](#__codelineno-199-15) 10  pipeline  netapp_storage_array_topology_pipeline_v1 [](#__codelineno-199-16) 11  pipeline  kubernetes_cluster_inventory_pipeline_v1 [](#__codelineno-199-17) 12  pipeline  cisco_ucs_cimc_inventory_v1 [](#__codelineno-199-18) 13  pipeline  linux_host_os_system_inventory_and_topology_v1_c1 [](#__codelineno-199-19) 14  pipeline  windows_host_os_system_inventory_and_topology_v1_c2 [](#__codelineno-199-20) 15  pipeline  kubernetes_cluster_topology_pipeline_v1 [](#__codelineno-199-21) 16  pipeline  cisco-ucsm-infra-topology-pipeline-v1 [](#__codelineno-199-22) 17  pipeline  NetApp_7Mode_inventroy`

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

`[](#__codelineno-200-1) rdac deployment --help`

`[](#__codelineno-201-1) Following are valid sub-commands for deployment: [](#__codelineno-201-2) [](#__codelineno-201-3)   activity                  List recent deployment activities [](#__codelineno-201-4)   status                    Display status of all deployments [](#__codelineno-201-5)   audit-report              Display Audit report for a given deployment ID [](#__codelineno-201-6)   add                       Add a new Deployment to the repository. Deployment specification must be in valid YML format [](#__codelineno-201-7)   enable                    Enable an existing deployment if it is not already enabled [](#__codelineno-201-8)   disable                   Disable an existing deployment if it is not already disabled [](#__codelineno-201-9)   delete                    Delete an existing deployment from repository [](#__codelineno-201-10)   dependencies              List all artifact dependencies used by the deployment [](#__codelineno-201-11)   svcs-status               List current status of all service pipelines in a deployment [](#__codelineno-201-12)   map                       Print service map information in JSON format for the given deployment`

****Sub Command: `activity`****

Description: List recent deployment activities

`[](#__codelineno-202-1) rdac deployment activity --help`

`[](#__codelineno-203-1) usage: deployment [-h] [--json] [](#__codelineno-203-2) [](#__codelineno-203-3) optional arguments: [](#__codelineno-203-4)   -h, --help  show this help message and exit [](#__codelineno-203-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-203-6)               format`

*   Following is the syntax for **deployment activity**

`[](#__codelineno-204-1) rdac deployment activity`

Example Output

    `[](#__codelineno-205-1)     timestamp                   severity    message [](#__codelineno-205-2) --  --------------------------  ----------  ---------------------------------------------------------------------------------------------------------------------------------------- [](#__codelineno-205-3)  0  2022-12-21T09:05:13.943451  WARNING     Re-Created Job: f5cc308e6d014173ac2a7893b1bae564 for Deployment Name: Demo_vmware_service_blueprint, Id: b744c8c2. Restart Count: 213 [](#__codelineno-205-4)  1  2022-12-21T09:05:13.301284  WARNING     Re-Created Job: 19c5ad1f4b5442a6a662bfd0493cc3db for Deployment Name: Service Action schedule pipeline, Id: b744c8c0. Restart Count: 213 [](#__codelineno-205-5)  2  2022-12-21T09:05:12.817716  WARNING     Re-Created Job: 8cc74ba0d633413faea5230aa2590d41 for Deployment Name: Blueprint_18_11_2022, Id: b744c873. Restart Count: 213 [](#__codelineno-205-6)  3  2022-12-21T09:04:02.257588  WARNING     Re-Created Job: 4d2b3770013b462db8cbcc421084a057 for Deployment Name: Demo_vmware_service_blueprint, Id: b744c8c2. Restart Count: 212 [](#__codelineno-205-7)  4  2022-12-21T09:04:01.482574  WARNING     Re-Created Job: e37777adca0a4a3fb6eeb431e0b9acca for Deployment Name: Service Action schedule pipeline, Id: b744c8c0. Restart Count: 212 [](#__codelineno-205-8)  5  2022-12-21T09:04:00.992727  WARNING     Re-Created Job: b792ae4110a6469883abcdf709692dee for Deployment Name: Blueprint_18_11_2022, Id: b744c873. Restart Count: 212 [](#__codelineno-205-9)  6  2022-12-21T09:02:50.307263  WARNING     Re-Created Job: f9e9a10bf1dd46e8a14049d0ac26a87a for Deployment Name: Demo_vmware_service_blueprint, Id: b744c8c2. Restart Count: 211`

****Sub Command: `status`****

Description: Display status of all deployments

`[](#__codelineno-206-1) rdac deployment status --help`

`[](#__codelineno-207-1) usage: deployment [-h] [--json] [](#__codelineno-207-2) [](#__codelineno-207-3) optional arguments: [](#__codelineno-207-4)   -h, --help  show this help message and exit [](#__codelineno-207-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-207-6)               format`

*   Following is the syntax for **deployment status**

`[](#__codelineno-208-1) rdac deployment status`

Example Output

    `[](#__codelineno-209-1)     id                                      category                                name                                    description                                                                                     enabled      errors    warnings [](#__codelineno-209-2) --  --------------------------------------  --------------------------------------  --------------------------------------  ----------------------------------------------------------------------------------------------  ---------  --------  ---------- [](#__codelineno-209-3)  0  41e33973                                ITSM                                    eBonding                                eBond ServiceNow incidents to PagerDuty, Twilio-SMS, Elasticsearch/Kibana, Slack, Email         no                0           0 [](#__codelineno-209-4)  1  81a1a030                                ITOM                                    ML-Experiments                          ML Experiments                                                                                  yes               0           0 [](#__codelineno-209-5)  2  81a1a2202                               ITOM                                    OIA                                     Ops Intelligence & Analytics                                                                    yes               0           0 [](#__codelineno-209-6)  3  81a1a2203                               ITOM                                    Stacks                                  Stacks                                                                                          yes               0           0 [](#__codelineno-209-7)  4  V2tdZpEs                                Dependency Mapping                      AWS Dependency Mapper                   AWS Dependency mapping with updates every hour                                                  yes               2           0 [](#__codelineno-209-8)  5  b744c873                                Service Action schedule pipeline        Blueprint_18_11_2022                    Service Action schedule pipeline example                                                        yes               0           2 [](#__codelineno-209-9)  6  b744c8c0                                Service Action schedule pipeline        Service Action schedule pipeline        Service Action schedule pipeline example                                                        yes               0           1 [](#__codelineno-209-10)  7  b744c8c1                                Service Action schedule pipeline        Blueprint_16_11_2022                    Service Action schedule pipeline example                                                        no                0           0 [](#__codelineno-209-11)  8  b744c8c2                                vmware schedule pipeline                Demo_vmware_service_blueprint           vmware schedule pipeline                                                                        yes               0           0 [](#__codelineno-209-12)  9  exec_dashboard_kpi_metrics_querystream  exec_dashboard_kpi_metrics_querystream  exec_dashboard_kpi_metrics_querystream  exec_dashboard_kpi_metrics_querystream                                                          yes               0           0 [](#__codelineno-209-13) 10  guide001                                Log Analytics                           Beginner Guide Blueprint                Generate Synthetic Syslogs, Save all logs to Log Archive, send processed logs to a NULL stream  yes               0           0`

****Sub Command: `audit-report`****

Description: Display Audit report for a given deployment ID

`[](#__codelineno-210-1) rdac deployment audit-report --help`

`[](#__codelineno-211-1) usage: deployment [-h] --id DEPLOYMENT_ID [--json] [](#__codelineno-211-2) [](#__codelineno-211-3) optional arguments: [](#__codelineno-211-4)   -h, --help          show this help message and exit [](#__codelineno-211-5)   --id DEPLOYMENT_ID  Deployment ID [](#__codelineno-211-6)   --json              Print detailed information in JSON format instead of [](#__codelineno-211-7)                       tabular format`

*   Following is the syntax for **deployment audit-report**

`[](#__codelineno-212-1) rdac deployment audit-report --id V2tdZpEs`

Example Output

    `[](#__codelineno-213-1)     type                      severity    message [](#__codelineno-213-2) --  ------------------------  ----------  ------------------------------------------------------------------------------------------- [](#__codelineno-213-3)  0  Verify Pipeline           INFO        Pipeline with name 'aws-dependency-mapper' and version '22_02_16_1' loaded [](#__codelineno-213-4)  1  Verify Pipeline           INFO        Pipeline with name 'aws-dependency-mapper-inner-pipeline' and version '2022_02_16_1' loaded [](#__codelineno-213-5)  2  Verify Pipeline           ERROR       No published versions found for pipline: aws-dependency-mapper2 [](#__codelineno-213-6)  3  Verify Site               ERROR       No sites matched the regex 'cfx.*' or no active workers found [](#__codelineno-213-7)  4  Verify Source             INFO        Credential found for Integration: aws, Type: aws_v2 [](#__codelineno-213-8)  5  Verify Persistent Stream  INFO        PStream rda_worker_resource_usage found [](#__codelineno-213-9)  6  Verify Persistent Stream  INFO        PStream rda_system_worker_trace_summary found [](#__codelineno-213-10)  7  Verify Persistent Stream  INFO        PStream rda_worker_resource_usage found [](#__codelineno-213-11)  8  Verify Persistent Stream  INFO        PStream rda_system_worker_trace_summary found [](#__codelineno-213-12)  9  Verify Persistent Stream  INFO        PStream rda_system_deployment_updates found [](#__codelineno-213-13) 10  Verify Persistent Stream  INFO        PStream rda_system_gw_endpoint_metrics found`

****Sub Command: `add`****

Description: Add a new Deployment to the repository. Deployment specification must be in valid YML format

`[](#__codelineno-214-1) rdac deployment add --help`

`[](#__codelineno-215-1) usage: deployment [-h] --file INPUT_FILE [--overwrite] [](#__codelineno-215-2) [](#__codelineno-215-3) optional arguments: [](#__codelineno-215-4)   -h, --help         show this help message and exit [](#__codelineno-215-5)   --file INPUT_FILE  YAML file containing Deployment specification [](#__codelineno-215-6)   --overwrite        Overwrite even if a ruleset already exists with a name.`

*   Following is the syntax for **deployment add**

`[](#__codelineno-216-1) rdac deployment add --file blueprint.yml`

*   sample blueprint.yml file

`[](#__codelineno-217-1) cat > blueprint.yml << 'EOF' [](#__codelineno-217-2) name: Blueprint_Example [](#__codelineno-217-3) id: b744c873a [](#__codelineno-217-4) version: '2022_12_19_01' [](#__codelineno-217-5) category: Service Action schedule pipeline [](#__codelineno-217-6) comment: Service Action schedule pipeline example [](#__codelineno-217-7) enabled: true [](#__codelineno-217-8) type: Service [](#__codelineno-217-9) auto_deploy: false [](#__codelineno-217-10) provider: CloudFabrix Software Inc. [](#__codelineno-217-11) attrs: {} [](#__codelineno-217-12) service_pipelines: [](#__codelineno-217-13)     -   name: Service_Pipeline [](#__codelineno-217-14)         label: Service Pipelines [](#__codelineno-217-15)         version: '*' [](#__codelineno-217-16)         site: rda-site-01 [](#__codelineno-217-17)         site_type: regex [](#__codelineno-217-18)         instances: 1 [](#__codelineno-217-19)         scaling_policy: [](#__codelineno-217-20)             min_instances: 1 [](#__codelineno-217-21)             max_instances: 1 [](#__codelineno-217-22) action_pipelines: [](#__codelineno-217-23)     -   name: Action_Pipeline [](#__codelineno-217-24)         label: Action Pipelines [](#__codelineno-217-25)         version: '*' [](#__codelineno-217-26)         site: rda-site-01 [](#__codelineno-217-27)         site_type: regex [](#__codelineno-217-28)         instances: 1 [](#__codelineno-217-29)         scaling_policy: [](#__codelineno-217-30)             min_instances: 1 [](#__codelineno-217-31)             max_instances: 1 [](#__codelineno-217-32) scheduled_pipelines: [](#__codelineno-217-33)     -   name: schedule_pipeline [](#__codelineno-217-34)         label: Scheduled Pipelines [](#__codelineno-217-35)         version: '*' [](#__codelineno-217-36)         site: rda-site-01 [](#__codelineno-217-37)         cron_expression: '*/5 * * * *' [](#__codelineno-217-38)         site_type: regex [](#__codelineno-217-39)         instances: 1 [](#__codelineno-217-40)         scaling_policy: [](#__codelineno-217-41)             min_instances: 1 [](#__codelineno-217-42)             max_instances: 1 [](#__codelineno-217-43) [](#__codelineno-217-44) EOF`

Example Output

`[](#__codelineno-218-1) Added deployment spec with Name: Blueprint_Example, ID: b744c873a`

****Sub Command: `enable`****

Description: Enable an existing deployment if it is not already enabled

`[](#__codelineno-219-1) rdac deployment enable --help`

`[](#__codelineno-220-1) Usage: deployment-enable  [-h] --id DEP_ID [](#__codelineno-220-2) [](#__codelineno-220-3) optional arguments: [](#__codelineno-220-4)   -h, --help   show this help message and exit [](#__codelineno-220-5)   --id DEP_ID  Deployment ID`

*   Following is the syntax for **deployment enable**

`[](#__codelineno-221-1) rdac deployment disable --id b744c8c1`

Example Output

`[](#__codelineno-222-1) Updated deployment with ID ID: b744c8c1`

****Sub Command: `disable`****

Description: Disable an existing deployment if it is not already disabled

`[](#__codelineno-223-1) rdac deployment enable --help`

`[](#__codelineno-224-1) Usage: deployment-disable  [-h] --id DEP_ID [](#__codelineno-224-2) [](#__codelineno-224-3) optional arguments: [](#__codelineno-224-4)   -h, --help   show this help message and exit [](#__codelineno-224-5)   --id DEP_ID  Deployment ID`

*   Following is the syntax for **deployment disable**

`[](#__codelineno-225-1) rdac deployment disable --id b744c8c1`

Example Output

`[](#__codelineno-226-1) Updated deployment with ID ID: b744c8c1`

****Sub Command: `delete`****

Description: Delete an existing deployment from repository

`[](#__codelineno-227-1) rdac deployment delete --help`

`[](#__codelineno-228-1) usage: deployment [-h] --id DEP_ID [](#__codelineno-228-2) [](#__codelineno-228-3) optional arguments: [](#__codelineno-228-4)   -h, --help   show this help message and exit [](#__codelineno-228-5)   --id DEP_ID  Deployment ID`

*   Following is the syntax for **deployment delete**

`[](#__codelineno-229-1) rdac deployment delete --id 44de62c6`

Example Delete

`[](#__codelineno-230-1) 2022-12-22:08:49:02 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-230-2) 2022-12-22:08:49:02 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-230-3) 2022-12-22:08:49:02 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-230-4) Deleted deployment with ID ID: 44de62c6`

****Sub Command: `dependencies`****

Description: List all artifact dependencies used by the deployment

`[](#__codelineno-231-1) rdac deployment-dependencies --help`

`[](#__codelineno-232-1) Usage: deployment-dependencies  [-h] --id DEPLOYMENT_ID [--json] [](#__codelineno-232-2) [](#__codelineno-232-3) optional arguments: [](#__codelineno-232-4)   -h, --help          show this help message and exit [](#__codelineno-232-5)   --id DEPLOYMENT_ID  Deployment ID [](#__codelineno-232-6)   --json              Print detailed information in JSON format instead of [](#__codelineno-232-7)                       tabular format`

*   Following is the syntax for **deployment dependencies**

`[](#__codelineno-233-1) rdac deployment dependencies --id V2tdZpEs`

Example Output

    `[](#__codelineno-234-1)     type      name                                  read    write [](#__codelineno-234-2) --  --------  ------------------------------------  ------  ------- [](#__codelineno-234-3)  0  pipeline  aws-dependency-mapper                 True    False [](#__codelineno-234-4)  1  pipeline  aws-dependency-mapper-inner-pipeline  True    False [](#__codelineno-234-5)  2  dataset   cfx-aws-ec2-instances                 True    True [](#__codelineno-234-6)  3  dataset   cfx-aws-ec2-instance-types            True    True [](#__codelineno-234-7)  4  dataset   cfx-aws-ec2-volumes                   True    True [](#__codelineno-234-8)  5  dataset   cfx-aws-ec2-vpcs                      True    True [](#__codelineno-234-9)  6  dataset   cfx-aws-ec2-efs-filesystems           True    True [](#__codelineno-234-10)  7  dataset   cfx-aws-ec2-security-groups           True    True [](#__codelineno-234-11)  8  dataset   cfx-aws-ec2-subnets                   True    True [](#__codelineno-234-12)  9  dataset   cfx-aws-ec2-internet-gateways         True    True [](#__codelineno-234-13) 10  dataset   cfx-aws-ec2-security-group-nodes      True    True`

****Sub Command: `svcs-status`****

Description: List current status of all service pipelines in a deployment

`[](#__codelineno-235-1) rdac deployment svcs-status --help`

`[](#__codelineno-236-1) usage: deployment [-h] --id DEPLOYMENT_ID [--json] [](#__codelineno-236-2) [](#__codelineno-236-3) optional arguments: [](#__codelineno-236-4)   -h, --help          show this help message and exit [](#__codelineno-236-5)   --id DEPLOYMENT_ID  Deployment ID [](#__codelineno-236-6)   --json              Print detailed information in JSON format instead of [](#__codelineno-236-7)                       tabular format`

*   Following is the syntax for **deployment svcs-status**

`[](#__codelineno-237-1) deployment svcs-status --id 41e33973`

Example Output

  `[](#__codelineno-238-1)   label                                                         pipeline_name                               version      min_instances    max_instances    instances    num_jobs [](#__codelineno-238-2) --  ------------------------------------------------------------  ------------------------------------------  ---------  ---------------  ---------------  -----------  ---------- [](#__codelineno-238-3)  0  Read incidents from ServiceNow write to stream                ebonding-servicenow-to-stream-v2            *                        1                4            1           0 [](#__codelineno-238-4)  1  Read incidents from stream and write to Elasticsearch/Kibana  ebonding-stream-to-elasticsearch-kibana-v2  *                        0                4            1           0 [](#__codelineno-238-5)  2  Read incidents from stream and write to Twilio-SMS            ebonding-stream-to-twilio-sms-v2            *                        0                4            1           0 [](#__codelineno-238-6)  3  Read incidents from stream and write to PagerDuty             ebonding-stream-to-pagerduty                *                        0                4            1           0 [](#__codelineno-238-7)  4  Read incidents from stream and write to Slack                 ebonding-stream-to-slack                    *                        0                4            1           0 [](#__codelineno-238-8)  5  Read incidents from stream and write to Email                 ebonding-stream-to-email                    *                        0                4            1           0`

****Sub Command: `map`****

Description: Print service map information in JSON format for the given deployment

`[](#__codelineno-239-1) rdac deployment map --help`

`[](#__codelineno-240-1) Usage: deployment-map  [-h] --id DEPLOYMENT_ID [](#__codelineno-240-2) [](#__codelineno-240-3) optional arguments: [](#__codelineno-240-4)   -h, --help          show this help message and exit [](#__codelineno-240-5)   --id DEPLOYMENT_ID  Deployment ID`

*   Following is the syntax for **deployment map**

`[](#__codelineno-241-1) rdac deployment map --id 41e33973`

Example Output

`[](#__codelineno-242-1) { [](#__codelineno-242-2)   "status": "ok", [](#__codelineno-242-3)   "reason": "", [](#__codelineno-242-4)   "data": { [](#__codelineno-242-5)     "stack": { [](#__codelineno-242-6)       "name": "eBonding", [](#__codelineno-242-7)       "description": "Service map for blueprint: eBonding", [](#__codelineno-242-8)       "nodes": [ [](#__codelineno-242-9)         { [](#__codelineno-242-10)           "node_id": "rda-network-stream-ebonding-analytics", [](#__codelineno-242-11)           "node_type": "rda-network-stream", [](#__codelineno-242-12)           "layer": "RDA Stream", [](#__codelineno-242-13)           "iconURL": "Stream", [](#__codelineno-242-14)           "node_label": "ebonding-analytics" [](#__codelineno-242-15)         }, [](#__codelineno-242-16)         { [](#__codelineno-242-17)           "node_id": "pstream-ebonding-analytics", [](#__codelineno-242-18)           "node_type": "Persistent Stream", [](#__codelineno-242-19)           "node_label": "ebonding-analytics", [](#__codelineno-242-20)           "layer": "Persistent Stream", [](#__codelineno-242-21)           "iconURL": "Persistent_Stream" [](#__codelineno-242-22)         }, [](#__codelineno-242-23)         { [](#__codelineno-242-24)           "node_id": "rda-network-stream-rda_worker_resource_usage", [](#__codelineno-242-25)           "node_type": "rda-network-stream", [](#__codelineno-242-26)           "layer": "RDA Stream", [](#__codelineno-242-27)           "iconURL": "Stream", [](#__codelineno-242-28)           "node_label": "rda_worker_resource_usage", [](#__codelineno-242-29)           "defaultVisibility": "hidden" [](#__codelineno-242-30)         }, [](#__codelineno-242-31)         { [](#__codelineno-242-32)           "node_id": "pstream-rda_worker_resource_usage", [](#__codelineno-242-33)           "node_type": "Persistent Stream", [](#__codelineno-242-34)           "node_label": "rda_worker_resource_usage", [](#__codelineno-242-35)           "layer": "Persistent Stream", [](#__codelineno-242-36)           "iconURL": "Persistent_Stream", [](#__codelineno-242-37)           "defaultVisibility": "hidden" [](#__codelineno-242-38)         }, [](#__codelineno-242-39)         { [](#__codelineno-242-40)           "node_id": "rda-network-stream-rda_system_worker_trace_summary", [](#__codelineno-242-41)           "node_type": "rda-network-stream", [](#__codelineno-242-42)           "layer": "RDA Stream", [](#__codelineno-242-43)           "iconURL": "Stream", [](#__codelineno-242-44)           "node_label": "rda_system_worker_trace_summary", [](#__codelineno-242-45)           "defaultVisibility": "hidden" [](#__codelineno-242-46)         }, [](#__codelineno-242-47)         { [](#__codelineno-242-48)           "node_id": "pstream-rda_system_worker_trace_summary", [](#__codelineno-242-49)           "node_type": "Persistent Stream", [](#__codelineno-242-50)           "node_label": "rda_system_worker_trace_summary", [](#__codelineno-242-51)           "layer": "Persistent Stream", [](#__codelineno-242-52)           "iconURL": "Persistent_Stream", [](#__codelineno-242-53)           "defaultVisibility": "hidden" [](#__codelineno-242-54)         }, [](#__codelineno-242-55)         { [](#__codelineno-242-56)           "node_id": "rda-network-stream-rda_system_deployment_updates", [](#__codelineno-242-57)           "node_type": "rda-network-stream", [](#__codelineno-242-58)           "layer": "RDA Stream", [](#__codelineno-242-59)           "iconURL": "Stream", [](#__codelineno-242-60)           "node_label": "rda_system_deployment_updates", [](#__codelineno-242-61)           "defaultVisibility": "hidden" [](#__codelineno-242-62)         }, [](#__codelineno-242-63)         { [](#__codelineno-242-64)           "node_id": "pstream-rda_system_deployment_updates", [](#__codelineno-242-65)           "node_type": "Persistent Stream", [](#__codelineno-242-66)           "node_label": "rda_system_deployment_updates", [](#__codelineno-242-67)           "layer": "Persistent Stream", [](#__codelineno-242-68)           "iconURL": "Persistent_Stream", [](#__codelineno-242-69)           "defaultVisibility": "hidden" [](#__codelineno-242-70)         } [](#__codelineno-242-71)       ], [](#__codelineno-242-72)       "relationships": [ [](#__codelineno-242-73)         { [](#__codelineno-242-74)           "left_id": "rda-network-stream-ebonding-analytics", [](#__codelineno-242-75)           "right_id": "pstream-ebonding-analytics", [](#__codelineno-242-76)           "description": "Stream persistence", [](#__codelineno-242-77)           "relationship_type": "uses" [](#__codelineno-242-78)         }, [](#__codelineno-242-79)         { [](#__codelineno-242-80)           "left_id": "rda-network-stream-rda_worker_resource_usage", [](#__codelineno-242-81)           "right_id": "pstream-rda_worker_resource_usage", [](#__codelineno-242-82)           "description": "Stream persistence", [](#__codelineno-242-83)           "relationship_type": "uses" [](#__codelineno-242-84)         }, [](#__codelineno-242-85)         { [](#__codelineno-242-86)           "left_id": "rda-network-stream-rda_system_worker_trace_summary", [](#__codelineno-242-87)           "right_id": "pstream-rda_system_worker_trace_summary", [](#__codelineno-242-88)           "description": "Stream persistence", [](#__codelineno-242-89)           "relationship_type": "uses" [](#__codelineno-242-90)         }, [](#__codelineno-242-91)         { [](#__codelineno-242-92)           "left_id": "rda-network-stream-rda_worker_resource_usage", [](#__codelineno-242-93)           "right_id": "pstream-rda_worker_resource_usage", [](#__codelineno-242-94)           "description": "Stream persistence", [](#__codelineno-242-95)           "relationship_type": "uses" [](#__codelineno-242-96)         }, [](#__codelineno-242-97)         { [](#__codelineno-242-98)           "left_id": "rda-network-stream-rda_system_worker_trace_summary", [](#__codelineno-242-99)           "right_id": "pstream-rda_system_worker_trace_summary", [](#__codelineno-242-100)           "description": "Stream persistence", [](#__codelineno-242-101)           "relationship_type": "uses" [](#__codelineno-242-102)         }, [](#__codelineno-242-103)         { [](#__codelineno-242-104)           "left_id": "rda-network-stream-rda_system_deployment_updates", [](#__codelineno-242-105)           "right_id": "pstream-rda_system_deployment_updates", [](#__codelineno-242-106)           "description": "Stream persistence", [](#__codelineno-242-107)           "relationship_type": "uses" [](#__codelineno-242-108)         } [](#__codelineno-242-109)       ] [](#__codelineno-242-110)     } [](#__codelineno-242-111)   } [](#__codelineno-242-112) }`

### Sub Command: `event-gw-status`

Description: List status of all ingestion endpoints at all the event gateways

`[](#__codelineno-243-1) rdac event-gw-status --help`

`[](#__codelineno-244-1) usage: rdac [-h] [--json] [](#__codelineno-244-2) [](#__codelineno-244-3) optional arguments: [](#__codelineno-244-4)   -h, --help  show this help message and exit [](#__codelineno-244-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-244-6)               format`

\* Following is the syntax for **event-gw-status**

`[](#__codelineno-245-1) rdac event-gw-status`

Example Output

`[](#__codelineno-246-1) No Event gateways found`

### Sub Command: `evict`

Description: Evict a job from a worker pod

`[](#__codelineno-247-1) Usage: evict  [-h] --jobid JOBID [--yes] [](#__codelineno-247-2) [](#__codelineno-247-3) optional arguments: [](#__codelineno-247-4)   -h, --help     show this help message and exit [](#__codelineno-247-5)   --jobid JOBID  RDA worker jobid. If partial must match only one job. [](#__codelineno-247-6)   --yes          Do not prompt for confirmation, evict if job is found`

### Sub Command: `file-ops`

Description: Perform various operations on local files

`[](#__codelineno-248-1) rdac file-ops --help`

`[](#__codelineno-249-1) Usage: file-ops copy                      Copy dataframe from one format to another. Format is inferred from extension. Examples are csv, parquet, json [](#__codelineno-249-2)   csv-to-parquet            Copy data from CSV to parquet file using chunking [](#__codelineno-249-3)   test-formats              Run performance test on various formats [](#__codelineno-249-4) [](#__codelineno-249-5) positional arguments: [](#__codelineno-249-6)   subcommand  File ops sub-command [](#__codelineno-249-7) [](#__codelineno-249-8) optional arguments: [](#__codelineno-249-9)   -h, --help  show this help message and exit`

\* Following is the syntax for **file-ops**

`[](#__codelineno-250-1) rdac file-ops csv-to-parquet --from metrics.csv --to metrics_parquet`

Example Output

`[](#__codelineno-251-1) Output File: [](#__codelineno-251-2)       File Size:       1,687,359 [](#__codelineno-251-3)       Copy time (ms): 585.7`

### Sub Command: `file-to-object`

Description: Convert files from a column into objects

`[](#__codelineno-252-1) Usage: file-to-object  [-h] --inpcol INPUT_FILENAME_COLUMN --outcol OUTPUT_COLUMN --file [](#__codelineno-252-2)             INPUT_FILE --outfolder OUTPUT_FOLDER --outfile OUTPUT_FILE [](#__codelineno-252-3) [](#__codelineno-252-4) optional arguments: [](#__codelineno-252-5)   -h, --help            show this help message and exit [](#__codelineno-252-6)   --inpcol INPUT_FILENAME_COLUMN [](#__codelineno-252-7)                         Name of the column in input that contains the [](#__codelineno-252-8)                         filenames [](#__codelineno-252-9)   --outcol OUTPUT_COLUMN [](#__codelineno-252-10)                         Column name where object names will be inserted [](#__codelineno-252-11)   --file INPUT_FILE     Input csv filename [](#__codelineno-252-12)   --outfolder OUTPUT_FOLDER [](#__codelineno-252-13)                         Folder name where objects will be stored [](#__codelineno-252-14)   --outfile OUTPUT_FILE [](#__codelineno-252-15)                         Name of output csv file that has object location [](#__codelineno-252-16)                         stored`

### Sub Command: `fmt-template-delete`

Description: Delete Formatting Template

`[](#__codelineno-253-1) Usage: fmt-template-delete  [-h] --name NAME [](#__codelineno-253-2) [](#__codelineno-253-3) optional arguments: [](#__codelineno-253-4)   -h, --help   show this help message and exit [](#__codelineno-253-5)   --name NAME  Formatting Template Name`

### Sub Command: `fmt-template-get`

Description: Get Formatting Template

`[](#__codelineno-254-1) Usage: fmt-template-get  [-h] --name NAME [--tofile SAVE_TO_FILE] [--json] [](#__codelineno-254-2) [](#__codelineno-254-3) optional arguments: [](#__codelineno-254-4)   -h, --help            show this help message and exit [](#__codelineno-254-5)   --name NAME           Formatting Template Name [](#__codelineno-254-6)   --tofile SAVE_TO_FILE [](#__codelineno-254-7)                         Save the data to the specified file [](#__codelineno-254-8)   --json                Export data as a JSON formatted rows. ** Deprecated. [](#__codelineno-254-9)                         Use --format **`

### Sub Command: `fmt-template-list`

Description: List Formatting Templates

`[](#__codelineno-255-1) Usage: fmt-template-list  [-h] [--json] [](#__codelineno-255-2) [](#__codelineno-255-3) optional arguments: [](#__codelineno-255-4)   -h, --help  show this help message and exit [](#__codelineno-255-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-255-6)               format`

### Sub Command: `healthcheck`

Description: Perform healthcheck on each of the Pods

`[](#__codelineno-256-1) Usage: healthcheck  [-h] [--json] [--type POD_TYPE] [--infra] [--apps] [--simple] [](#__codelineno-256-2) [](#__codelineno-256-3) optional arguments: [](#__codelineno-256-4)   -h, --help       show this help message and exit [](#__codelineno-256-5)   --json           Print detailed information in JSON format instead of [](#__codelineno-256-6)                    tabular format [](#__codelineno-256-7)   --type POD_TYPE  Show only the pods that match the specified pod type [](#__codelineno-256-8)   --infra          List only RDA Infra pods. not compatible with --apps option [](#__codelineno-256-9)   --apps           List only RDA App pods. not compatible with --infra option [](#__codelineno-256-10)   --simple         When showing in tabular format, show in a easy to read [](#__codelineno-256-11)                    format.`

### Sub Command: `invoke-agent-bot`

Description: Invoke a bot published by an agent

`[](#__codelineno-257-1) Usage: invoke-agent-bot  [-h] --type AGENT_TYPE --group AGENT_GROUP --bot BOT_NAME [](#__codelineno-257-2)             [--query QUERY] [--input INPUT_FILE] [--output OUTPUT_FILE] [](#__codelineno-257-3) [](#__codelineno-257-4) optional arguments: [](#__codelineno-257-5)   -h, --help            show this help message and exit [](#__codelineno-257-6)   --type AGENT_TYPE     Agent type [](#__codelineno-257-7)   --group AGENT_GROUP   Agent group [](#__codelineno-257-8)   --bot BOT_NAME        Bot name [](#__codelineno-257-9)   --query QUERY         Bot Query (CFXQL) [](#__codelineno-257-10)   --input INPUT_FILE    Input Dataframe (CSV File) [](#__codelineno-257-11)   --output OUTPUT_FILE  Output Dataframe (CSV File)`

### Sub Command: `jobs`

Description: List all jobs for the current tenant

`[](#__codelineno-258-1) rdac jobs --help`

`[](#__codelineno-259-1) usage: rdac [-h] [--json] [--all] [--pipeline_name PIPELINE_NAME] [](#__codelineno-259-2) [](#__codelineno-259-3) optional arguments: [](#__codelineno-259-4)   -h, --help            show this help message and exit [](#__codelineno-259-5)   --json                Print detailed information in JSON format instead of [](#__codelineno-259-6)                         tabular format [](#__codelineno-259-7)   --all                 Retrieve all jobs not just active jobs [](#__codelineno-259-8)   --pipeline_name PIPELINE_NAME [](#__codelineno-259-9)                         Get all jobs for given pipeline name`

\* Following is the syntax for **jobs**

`[](#__codelineno-260-1) rdac jobs --pipeline_name 'oia-new-incidents-to-snowv2'`

Example Output

`[](#__codelineno-261-1) 2023-01-09:05:58:09 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-261-2) worker pipeline name: oia-new-incidents-to-snowv2 [](#__codelineno-261-3) +--------------+----------+----------------------------------+-------+---------------------+-----------------+-----------------------------+--------------+----------+ [](#__codelineno-261-4) | Host         | Pod ID   | Job ID                           |   PID | Created             | Age             | Pipeline                    | Status       | Reason   | [](#__codelineno-261-5) |--------------+----------+----------------------------------+-------+---------------------+-----------------+-----------------------------+--------------+----------| [](#__codelineno-261-6) | 05969789d903 | 88c26bbe | 5c93dc55cfd84586921aad41b9e7358e |   761 | 2023-01-07T14:00:03 | 1 day, 15:58:06 | oia-new-incidents-to-snowv2 | Initializing |          | [](#__codelineno-261-7) | 05969789d903 | 88c26bbe | f0f1d6a240cb45fabf3e65f0c4eb9cfe |  1605 | 2023-01-07T14:35:02 | 1 day, 15:23:07 | oia-new-incidents-to-snowv2 | Initializing |          | [](#__codelineno-261-8) | 05969789d903 | 88c26bbe | 384acd9ef4c240aa88c629a75523bc56 |  2352 | 2023-01-07T15:05:02 | 1 day, 14:53:07 | oia-new-incidents-to-snowv2 | Initializing |          | [](#__codelineno-261-9) | 05969789d903 | 88c26bbe | 84d8547509c94a4eaf695c57aa139506 | 17718 | 2023-01-08T01:30:02 | 1 day, 4:28:07  | oia-new-incidents-to-snowv2 | Initializing |          | [](#__codelineno-261-10) | 05969789d903 | 88c26bbe | 58848c8d5a7e4c54a08e01d25155f22e | 18097 | 2023-01-08T01:45:01 | 1 day, 4:13:08  | oia-new-incidents-to-snowv2 | Initializing |          | [](#__codelineno-261-11) | 05969789d903 | 88c26bbe | 32faf9f9ba2445b4b1cc2fb625538f35 | 19080 | 2023-01-08T02:25:02 | 1 day, 3:33:07  | oia-new-incidents-to-snowv2 | Initializing |          | [](#__codelineno-261-12) | 05969789d903 | 88c26bbe | b5dc599ce659485f9139242d05c9875e | 23632 | 2023-01-08T05:30:02 | 1 day, 0:28:07  | oia-new-incidents-to-snowv2 | Initializing |          | [](#__codelineno-261-13) | 05969789d903 | 88c26bbe | fd361ae94358405cbb9f2ac1d75c142c | 39213 | 2023-01-08T14:20:02 | 15:38:07        | oia-new-incidents-to-snowv2 | Initializing |          | [](#__codelineno-261-14) | 05969789d903 | 88c26bbe | 07da31424e18492e976db4451ce82252 | 44773 | 2023-01-08T18:05:02 | 11:53:07        | oia-new-incidents-to-snowv2 | Initializing |          | [](#__codelineno-261-15) | 05969789d903 | 88c26bbe | f332d5c0055f43839dffd906c04fb842 | 50985 | 2023-01-08T22:20:01 | 7:38:08         | oia-new-incidents-to-snowv2 | Initializing |          | [](#__codelineno-261-16) | 05969789d903 | 88c26bbe | 43b00217d5854d4cb5ab7497929b8369 | 57340 | 2023-01-09T03:30:03 | 2:28:06         | oia-new-incidents-to-snowv2 | Initializing |          | [](#__codelineno-261-17) | 05969789d903 | 88c26bbe | 78ab3c2492aa4781820c0be9013cc6d9 | 59707 | 2023-01-09T05:25:02 | 0:33:07         | oia-new-incidents-to-snowv2 | Initializing |          | [](#__codelineno-261-18) +--------------+----------+----------------------------------+-------+---------------------+-----------------+-----------------------------+--------------+----------+`

### Sub Command: `logarchive-add-platform`

Description: Add current platform Minio as logarchive repository

`[](#__codelineno-262-1) Usage: logarchive-add-platform  [-h] --repo REPO --prefix OBJECT_PREFIX [](#__codelineno-262-2)             [--retention RETENTION_DAYS] [](#__codelineno-262-3) [](#__codelineno-262-4) optional arguments: [](#__codelineno-262-5)   -h, --help            show this help message and exit [](#__codelineno-262-6)   --repo REPO           Log archive repository name to be created [](#__codelineno-262-7)   --prefix OBJECT_PREFIX [](#__codelineno-262-8)                         Object prefix to be used for the archive [](#__codelineno-262-9)   --retention RETENTION_DAYS [](#__codelineno-262-10)                         Data retention period in number of days. If not [](#__codelineno-262-11)                         specified, RDA will not manage the data retention.`

### Sub Command: `logarchive-data-read`

Description: Read the data from given archive for a specified time interval

`[](#__codelineno-263-1) Usage: logarchive-data-read  [-h] --repo REPO --name ARCHIVE_NAME [--from TIMESTAMP] [](#__codelineno-263-2)             [--minutes MINUTES] [--max_rows MAX_ROWS] [--speed SPEED] [--line] [](#__codelineno-263-3) [](#__codelineno-263-4) optional arguments: [](#__codelineno-263-5)   -h, --help           show this help message and exit [](#__codelineno-263-6)   --repo REPO          Log archive repository name [](#__codelineno-263-7)   --name ARCHIVE_NAME  Name of the log archive within the repository [](#__codelineno-263-8)   --from TIMESTAMP     From Date & time in text format (ex: ISO format). [](#__codelineno-263-9)                        Timezone must be UTC. If not specified, it will use [](#__codelineno-263-10)                        current time minus specified minutes [](#__codelineno-263-11)   --minutes MINUTES    Number of minutes from specified date & time. Default [](#__codelineno-263-12)                        is 15 [](#__codelineno-263-13)   --max_rows MAX_ROWS  If value is specified > 0, stop after reading max_rows [](#__codelineno-263-14)                        from the archive [](#__codelineno-263-15)   --speed SPEED        Replay speed. 0 means no delay, 1.0 means closer to [](#__codelineno-263-16)                        original rate, < 1.0 means slower, > 1.0 means faster [](#__codelineno-263-17)   --line               Instead of JSON format, print one message per line`

### Sub Command: `logarchive-data-size`

Description: Show size of data available for given archive for a specified time interval

`[](#__codelineno-264-1) Usage: logarchive-data-size  [-h] --repo REPO --name ARCHIVE_NAME [--from TIMESTAMP] [](#__codelineno-264-2)             [--minutes MINUTES] [--json] [](#__codelineno-264-3) [](#__codelineno-264-4) optional arguments: [](#__codelineno-264-5)   -h, --help           show this help message and exit [](#__codelineno-264-6)   --repo REPO          Log archive repository name [](#__codelineno-264-7)   --name ARCHIVE_NAME  Name of the log archive within the repository [](#__codelineno-264-8)   --from TIMESTAMP     From Date & time in text format (ex: ISO format). [](#__codelineno-264-9)                        Timezone must be UTC. If not specified, it will use [](#__codelineno-264-10)                        current time minus specified minutes [](#__codelineno-264-11)   --minutes MINUTES    Number of minutes from specified date & time. Default [](#__codelineno-264-12)                        is 15 [](#__codelineno-264-13)   --json               Print detailed information in JSON format instead of [](#__codelineno-264-14)                        tabular format`

### Sub Command: `logarchive-download`

Description: Download the data from given archive for a specified time interval

`[](#__codelineno-265-1) Usage: logarchive-download  [-h] --repo REPO --name ARCHIVE_NAME [--from TIMESTAMP] [](#__codelineno-265-2)             [--minutes MINUTES] --out OUTPUT_DIR [--flatten] [](#__codelineno-265-3) [](#__codelineno-265-4) optional arguments: [](#__codelineno-265-5)   -h, --help           show this help message and exit [](#__codelineno-265-6)   --repo REPO          Log archive repository name [](#__codelineno-265-7)   --name ARCHIVE_NAME  Name of the log archive within the repository [](#__codelineno-265-8)   --from TIMESTAMP     From Date & time in text format (ex: ISO format). [](#__codelineno-265-9)                        Timezone must be UTC. If not specified, it will use [](#__codelineno-265-10)                        current time minus specified minutes [](#__codelineno-265-11)   --minutes MINUTES    Number of minutes from specified date & time. Default [](#__codelineno-265-12)                        is 15 [](#__codelineno-265-13)   --out OUTPUT_DIR     Output directory where to save the downloaded data [](#__codelineno-265-14)   --flatten            Flatten directory structure of the files, which [](#__codelineno-265-15)                        otherwise stores in yyyy/mm/dd/HH/MM/ directory [](#__codelineno-265-16)                        structure`

### Sub Command: `logarchive-names`

Description: List archive names in a given repository

`[](#__codelineno-266-1) Usage: logarchive-names  [-h] --repo REPO [--json] [](#__codelineno-266-2) [](#__codelineno-266-3) optional arguments: [](#__codelineno-266-4)   -h, --help   show this help message and exit [](#__codelineno-266-5)   --repo REPO  Name of the log archive repository [](#__codelineno-266-6)   --json       Print detailed information in JSON format instead of tabular [](#__codelineno-266-7)                format`

### Sub Command: `logarchive-replay`

Description: Replay the data from given archive for a specified time interval with specified label

`[](#__codelineno-267-1) Usage: logarchive-replay  [-h] --repo REPO --name ARCHIVE_NAME [--from TIMESTAMP] [](#__codelineno-267-2)             [--minutes MINUTES] [--max_rows MAX_ROWS] [--speed SPEED] [](#__codelineno-267-3)             [--batch_size BATCH_SIZE] --stream STREAM [--label LABEL] --site [](#__codelineno-267-4)             SITE [](#__codelineno-267-5) [](#__codelineno-267-6) optional arguments: [](#__codelineno-267-7)   -h, --help            show this help message and exit [](#__codelineno-267-8)   --repo REPO           Log archive repository name [](#__codelineno-267-9)   --name ARCHIVE_NAME   Name of the log archive within the repository [](#__codelineno-267-10)   --from TIMESTAMP      From Date & time in text format (ex: ISO format). [](#__codelineno-267-11)                         Timezone must be UTC. If not specified, it will use [](#__codelineno-267-12)                         current time minus specified minutes [](#__codelineno-267-13)   --minutes MINUTES     Number of minutes from specified date & time. Default [](#__codelineno-267-14)                         is 15 [](#__codelineno-267-15)   --max_rows MAX_ROWS   If value is specified > 0, stop after reading max_rows [](#__codelineno-267-16)                         from the archive [](#__codelineno-267-17)   --speed SPEED         Replay speed. 0 means no delay, 1.0 means closer to [](#__codelineno-267-18)                         original rate, < 1.0 means slower, > 1.0 means faster [](#__codelineno-267-19)   --batch_size BATCH_SIZE [](#__codelineno-267-20)                         Number of rows to return for each iteration [](#__codelineno-267-21)   --stream STREAM       Name of the stream to write to [](#__codelineno-267-22)   --label LABEL         Label for the replay job [](#__codelineno-267-23)   --site SITE           Site name to run this on a worker`

### Sub Command: `logarchive-repos`

Description: List of all log archive repositories

`[](#__codelineno-268-1) rdac logarchive-repos --help`

`[](#__codelineno-269-1) Usage: logarchive-repos  [-h] [--json] [](#__codelineno-269-2) [](#__codelineno-269-3) optional arguments: [](#__codelineno-269-4)   -h, --help  show this help message and exit [](#__codelineno-269-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-269-6)               format`

*   Following is the syntax for **logarchive-repos**

`[](#__codelineno-270-1) rdac logarchive-repos`

Example Output

`[](#__codelineno-271-1) +-------------------+--------------------+------------------------------------------+-----------------+ [](#__codelineno-271-2) | Repository Name   | Endpoint           | Bucket Name                              | Object Prefix   | [](#__codelineno-271-3) |-------------------+--------------------+------------------------------------------+-----------------| [](#__codelineno-271-4) | demo_logarchive   | 10.95.122.127:9443 | tenants.ae144f67d2a24034ad6920ace6809763 | demo_logs/      | [](#__codelineno-271-5) +-------------------+--------------------+------------------------------------------+-----------------+`

### Sub Command: `merge-logarchive-files`

Description: Merge multiple locally downloaded Log Archive (.gz) filles into a single CSV/Parquet file

`[](#__codelineno-272-1) Usage: merge-logarchive-files  [-h] --folder FOLDER --tofile TOFILE [--sample SAMPLE_RATE] [](#__codelineno-272-2)             [--ts TIMESTAMP] [](#__codelineno-272-3) [](#__codelineno-272-4) optional arguments: [](#__codelineno-272-5)   -h, --help            show this help message and exit [](#__codelineno-272-6)   --folder FOLDER       Path to the folder where locally downloaded .gz files [](#__codelineno-272-7)                         are available [](#__codelineno-272-8)   --tofile TOFILE       Save the output to specified file [](#__codelineno-272-9)   --sample SAMPLE_RATE  Data sample rate must be >0 and <= 1.0 [](#__codelineno-272-10)   --ts TIMESTAMP        Timestamp column, if specified will sort the data [](#__codelineno-272-11)                         after merge`

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

`[](#__codelineno-273-1) rdac object --help`

`[](#__codelineno-274-1) RDA Object management commands [](#__codelineno-274-2) [](#__codelineno-274-3) Following are valid sub-commands for object: [](#__codelineno-274-4)   list                      List objects from the object store [](#__codelineno-274-5)   get                       Download a object from the object store [](#__codelineno-274-6)   meta                      Download metadata for an object from the object store [](#__codelineno-274-7)   add                       Add a new object to the object store [](#__codelineno-274-8)   delete                    Delete object from the object store [](#__codelineno-274-9)   to-file                   Convert object pointers from a column into file [](#__codelineno-274-10)   to-content                Convert object pointers from a column into content [](#__codelineno-274-11)   delete-list               Delete list of objects`

### Sub Command: `object-add`

Description: Add a new object to the object store

`[](#__codelineno-275-1) rdac object-add --help`

`[](#__codelineno-276-1) Usage: object-add  [-h] --name NAME --folder FOLDER --file INPUT_FILE [](#__codelineno-276-2)             [--descr DESCRIPTION] [--overwrite OVERWRITE] [](#__codelineno-276-3) [](#__codelineno-276-4) optional arguments: [](#__codelineno-276-5)   -h, --help            show this help message and exit [](#__codelineno-276-6)   --name NAME           Object name [](#__codelineno-276-7)   --folder FOLDER       Folder name on the object storage [](#__codelineno-276-8)   --file INPUT_FILE     file from which object will be added [](#__codelineno-276-9)   --descr DESCRIPTION   Description [](#__codelineno-276-10)   --overwrite OVERWRITE [](#__codelineno-276-11)                         If file already exists, overwrite without prompting. [](#__codelineno-276-12)                         Accepted values (yes/no)`

### Sub Command: `object-delete`

`[](#__codelineno-277-1) rdac object-delete --help`

Description: Delete object from the object store

`[](#__codelineno-278-1) Usage: object-delete  [-h] --name NAME --folder FOLDER [](#__codelineno-278-2) [](#__codelineno-278-3) optional arguments: [](#__codelineno-278-4)   -h, --help       show this help message and exit [](#__codelineno-278-5)   --name NAME      Object name [](#__codelineno-278-6)   --folder FOLDER  Folder name on the object storage`

*   Following is the syntax for **object-get**

`[](#__codelineno-279-1) rdac object delete --name testobjectnew --folder testobj-foldernew`

Example Output

`[](#__codelineno-280-1) Done deleting objects`

### Sub Command: `object-delete-list`

Description: Delete list of objects

`[](#__codelineno-281-1) rdac object-delete-list --help`

`[](#__codelineno-282-1) Usage: object-delete-list  [-h] --inpcol INPUT_OBJECT_COLUMN --file INPUT_FILE --outfile [](#__codelineno-282-2)             OUTPUT_FILE [](#__codelineno-282-3) [](#__codelineno-282-4) optional arguments: [](#__codelineno-282-5)   -h, --help            show this help message and exit [](#__codelineno-282-6)   --inpcol INPUT_OBJECT_COLUMN [](#__codelineno-282-7)                         Column with object names [](#__codelineno-282-8)   --file INPUT_FILE     Input csv filename [](#__codelineno-282-9)   --outfile OUTPUT_FILE [](#__codelineno-282-10)                         Name of output csv file that has result for deletion`

### Sub Command: `object-get`

Description: Download a object from the object store

`[](#__codelineno-283-1) rdac object-get --help`

`[](#__codelineno-284-1) usage: rdac [-h] --name NAME --folder FOLDER [--tofile SAVE_TO_FILE] [](#__codelineno-284-2)             [--todir SAVE_TO_DIR] [](#__codelineno-284-3) [](#__codelineno-284-4) optional arguments: [](#__codelineno-284-5)   -h, --help            show this help message and exit [](#__codelineno-284-6)   --name NAME           Object name [](#__codelineno-284-7)   --folder FOLDER       Folder name on the object storage [](#__codelineno-284-8)   --tofile SAVE_TO_FILE [](#__codelineno-284-9)                         Save the downloaded object to specified file [](#__codelineno-284-10)   --todir SAVE_TO_DIR   Save the downloaded object to specified directory`

*   Following is the syntax for **object-get**

`[](#__codelineno-285-1) rdac object get --name testobject --folder testobj-folder`

Example Output

`[](#__codelineno-286-1) Object saved to /tmp/rda-object-cache/8a2e7e88e5548c33/testobject.csv`

### Sub Command: `object-list`

Description: List objects from the object store

`[](#__codelineno-287-1) rdac object-list --help`

`[](#__codelineno-288-1) usage: rdac [-h] [--folder FOLDER] [--json] [](#__codelineno-288-2) [](#__codelineno-288-3) optional arguments: [](#__codelineno-288-4)   -h, --help       show this help message and exit [](#__codelineno-288-5)   --folder FOLDER  Folder name on the object storage [](#__codelineno-288-6)   --json           Print detailed information in JSON format instead of [](#__codelineno-288-7)                    tabular format`

*   Following is the syntax for **object-list**

`[](#__codelineno-289-1) rdac object list`

Example Output

`[](#__codelineno-290-1) folder             name           description    file_type      file_size  saved_time [](#__codelineno-290-2) -----------------  -------------  -------------  -----------  -----------  -------------------------- [](#__codelineno-290-3) testobj-folder     testobject     testobjct      csv             15303849  2023-01-09T06:12:03.413276 [](#__codelineno-290-4) testobj-foldernew  testobjectnew  testobjctnew   csv             15303849  2023-01-09T06:12:55.904404`

### Sub Command: `object-meta`

`[](#__codelineno-291-1) rdac object-meta --help`

Description: Download metadata for an object from the object store

`[](#__codelineno-292-1) Usage: object-meta  [-h] --name NAME --folder FOLDER [](#__codelineno-292-2) [](#__codelineno-292-3) optional arguments: [](#__codelineno-292-4)   -h, --help       show this help message and exit [](#__codelineno-292-5)   --name NAME      Dataset name [](#__codelineno-292-6)   --folder FOLDER  Folder name on the object storage`

\* Following is the syntax for **object-meta**

`[](#__codelineno-293-1) rdac object meta --name testobject --folder testobj-folder`

Example Output

`[](#__codelineno-294-1) { [](#__codelineno-294-2)   "name": "testobject", [](#__codelineno-294-3)   "folder": "testobj-folder", [](#__codelineno-294-4)   "description": "testobjct", [](#__codelineno-294-5)   "saved_time": "2023-01-09T06:12:03.413276", [](#__codelineno-294-6)   "data_path": "rda-objects/data/testobj-folder/6f44d574-testobject.data", [](#__codelineno-294-7)   "file_type": "csv", [](#__codelineno-294-8)   "file_size": 15303849 [](#__codelineno-294-9) }`

### Sub Command: `object-to-content`

Description: Convert object pointers from a column into content

`[](#__codelineno-295-1) rdac object-to-content --help`

`[](#__codelineno-296-1) Usage: object-to-content  [-h] --inpcol INPUT_OBJECT_COLUMN --outcol OUTPUT_COLUMN --file [](#__codelineno-296-2)             INPUT_FILE --outfile OUTPUT_FILE [](#__codelineno-296-3) [](#__codelineno-296-4) optional arguments: [](#__codelineno-296-5)   -h, --help            show this help message and exit [](#__codelineno-296-6)   --inpcol INPUT_OBJECT_COLUMN [](#__codelineno-296-7)                         Name of the column in input that contains the object [](#__codelineno-296-8)                         name [](#__codelineno-296-9)   --outcol OUTPUT_COLUMN [](#__codelineno-296-10)                         Column name where content will be inserted [](#__codelineno-296-11)   --file INPUT_FILE     Input csv file [](#__codelineno-296-12)   --outfile OUTPUT_FILE [](#__codelineno-296-13)                         Name of output csv file that has content inserted`

### Sub Command: `object-to-file`

Description: Convert object pointers from a column into file

`[](#__codelineno-297-1) rdac object-to-file --help`

`[](#__codelineno-298-1) usage: rdac [-h] --inpcol INPUT_OBJECT_COLUMN --outcol OUTPUT_COLUMN --file [](#__codelineno-298-2)             INPUT_FILE --outfile OUTPUT_FILE [](#__codelineno-298-3) [](#__codelineno-298-4) optional arguments: [](#__codelineno-298-5)   -h, --help            show this help message and exit [](#__codelineno-298-6)   --inpcol INPUT_OBJECT_COLUMN [](#__codelineno-298-7)                         Name of the column in input that contains the objects [](#__codelineno-298-8)   --outcol OUTPUT_COLUMN [](#__codelineno-298-9)                         Column name where filenames need to be inserted [](#__codelineno-298-10)   --file INPUT_FILE     Input csv file [](#__codelineno-298-11)   --outfile OUTPUT_FILE [](#__codelineno-298-12)                         Name of output csv file that has filename inserted`

### Sub Command: `output`

Description: Get the output of a Job using jobid.

`[](#__codelineno-299-1) rdac output --help`

`[](#__codelineno-300-1) Usage: output  [-h] --jobid JOBID [--tofile SAVE_TO_FILE] [--format DATA_FORMAT] [](#__codelineno-300-2)             [--viz] [](#__codelineno-300-3) [](#__codelineno-300-4) optional arguments: [](#__codelineno-300-5)   -h, --help            show this help message and exit [](#__codelineno-300-6)   --jobid JOBID         Job ID (either partial or complete) [](#__codelineno-300-7)   --tofile SAVE_TO_FILE [](#__codelineno-300-8)                         Save the data to the specified file (CSV) [](#__codelineno-300-9)   --format DATA_FORMAT  Format for the saved file. Valid values are auto, csv, [](#__codelineno-300-10)                         json, parquet. If 'auto' format will be determined [](#__codelineno-300-11)                         from extension [](#__codelineno-300-12)   --viz                 Open Dataframe visualizer to show the data`

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

`[](#__codelineno-301-1) rdac pipeline --help`

`[](#__codelineno-302-1) Following are valid sub-commands for pipeline: [](#__codelineno-302-2)   list                      List published pipelines [](#__codelineno-302-3)   get-versions              Get versions for the pipeline [](#__codelineno-302-4)   get                       Get pipeline by name and version [](#__codelineno-302-5)   delete                    Delete pipeline by name and version [](#__codelineno-302-6)   convert-to-json           Convert all pipelines in folder from yaml to json [](#__codelineno-302-7)   publish                   Publish the pipeline on a worker pod [](#__codelineno-302-8)   published-run             Run a published pipeline on a worker pod`

****Sub Command: `list`****

Description: Get pipeline by name and version

`[](#__codelineno-303-1) rdac pipeline-list --help`

`[](#__codelineno-304-1) usage: rdac [-h] [--json] [](#__codelineno-304-2) [](#__codelineno-304-3) optional arguments: [](#__codelineno-304-4)   -h, --help  show this help message and exit [](#__codelineno-304-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-304-6)               format`

*   Following is the syntax for **pipeline-list**

 `[](#__codelineno-305-1)  rdac pipeline list`

Example Output

`[](#__codelineno-306-1) category                 description    name                                    saved_time                  usecase                                                              version [](#__codelineno-306-2) -----------------------  -------------  --------------------------------------  --------------------------  -------------------------------------------------------------------  -------------`

****Sub Command: `get-versions`****

Description: Get versions for the pipeline

`[](#__codelineno-307-1) rdac pipeline-get-versions --help`

`[](#__codelineno-308-1) Usage: pipeline-get-versions  [-h] --name NAME [--json] [](#__codelineno-308-2) [](#__codelineno-308-3) optional arguments: [](#__codelineno-308-4)   -h, --help   show this help message and exit [](#__codelineno-308-5)   --name NAME  Get versions of pipeline specified by name [](#__codelineno-308-6)   --json       Print detailed information in JSON format instead of tabular [](#__codelineno-308-7)                format`

*   Following is the syntax for **pipeline-get-versions**

`[](#__codelineno-309-1) === "Example Output"`

Versions

* * *

2022\_12\_09\_1

``[](#__codelineno-310-1) <a name='pipeline-list'></a> [](#__codelineno-310-2) [](#__codelineno-310-3) ### Sub Command: `pipeline-list` [](#__codelineno-310-4) [](#__codelineno-310-5) Description: List published pipelines [](#__codelineno-310-6) [](#__codelineno-310-7) ```bash [](#__codelineno-310-8) Usage: pipeline-list  [-h] [--json] [](#__codelineno-310-9) [](#__codelineno-310-10) optional arguments: [](#__codelineno-310-11)   -h, --help  show this help message and exit [](#__codelineno-310-12)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-310-13)               format``

****Sub Command: `get`****

Description: Get pipeline by name and version

`[](#__codelineno-311-1) rdac pipeline-get --help`

`[](#__codelineno-312-1) usage: rdac [-h] --name NAME --version VERSION [--tofile SAVE_TO_FILE] [](#__codelineno-312-2)             [--json] [](#__codelineno-312-3) [](#__codelineno-312-4) optional arguments: [](#__codelineno-312-5)   -h, --help            show this help message and exit [](#__codelineno-312-6)   --name NAME           Pipeline name [](#__codelineno-312-7)   --version VERSION     Pipeline version [](#__codelineno-312-8)   --tofile SAVE_TO_FILE [](#__codelineno-312-9)                         Save the downloaded pipeline to specified file [](#__codelineno-312-10)   --json                Print detailed information in JSON format instead of [](#__codelineno-312-11)                         tabular format`

*   Following is the syntax for **pipeline-get**

`[](#__codelineno-313-1) rdac pipeline get --name regression_metrics_data --version 2022_12_09_1`

Example Output

`[](#__codelineno-314-1) {'name': 'regression_metrics_data', 'description': 'test pipeline', 'usecase': '', 'category': '1', 'version': '2022_12_09_1', 'sources': {'files': {'name': 'files', 'type': 'file'}, 'cfxml': {'name': 'cfxml', 'type': 'cfxai_regression'}, 'rn': {'name': 'rn', 'type': 'rn'}}, 'data': {'name': 'regression_metrics_data', 'sequence': [{'tag': '@files:loadfile', 'query': "filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-prometheus-timeseries-data.csv'"}, {'tag': '@cfxml:regression', 'query': "value_column = 'value' and\nts_column = 'timestamp' and\nfrequency = '4H' and\nagg_func = 'mean'"}, {'tag': '@dm:change-time-format', 'query': "columns='timestamp' &\nfrom_format='datetimestr' &\nto_format='%Y-%m-%dT%H:%M:%S'", 'comment': 'Changing time format before writing to stream'}, {'tag': '@rn:write-stream', 'query': 'name = "regression_metrics_data"'}]}, 'artifacts': [{'artifact_type': 'rda-network-stream', 'artifact_name': 'regression_metrics_data', 'access': 'write'}], 'html_data': "\n        <style>\n\n        .tooltip {\n            position: relative;\n            display: inline-block;\n            border-bottom: 1px dotted black; /* If you want dots under the hoverable text */\n            }\n\n        /* Tooltip text */\n        .tooltip .tooltiptext {\n            visibility: hidden;\n            width: 120px;\n            background-color: black;\n            color: #fff;\n            text-align: center;\n            padding: 5px 0;\n            border-radius: 6px;\n            \n            /* Position the tooltip text - see examples below! */\n            position: absolute;\n`   

****Sub Command: `delete`****

Description: Delete pipeline by name and version

`[](#__codelineno-315-1) rdac pipeline-delete --help`

`[](#__codelineno-316-1) Usage: pipeline-delete  [-h] --name NAME --version VERSION [](#__codelineno-316-2) [](#__codelineno-316-3) optional arguments: [](#__codelineno-316-4)   -h, --help         show this help message and exit [](#__codelineno-316-5)   --name NAME        Pipeline name [](#__codelineno-316-6)   --version VERSION  Version for pipeline`

*   Following is the syntax for **pipeline-delete**

 `[](#__codelineno-317-1)  rdac pipeline delete --name nifty50_new --version 2023_01_10`

Example Output

`[](#__codelineno-318-1) 2023-01-10:07:37:49 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-318-2) 2023-01-10:07:37:49 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-318-3) 2023-01-10:07:37:49 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-318-4) Done deleting pipeline`

****Sub Command: `convert-to-json`****

Description: Convert all pipelines in folder from yaml to json

`[](#__codelineno-319-1) rdac pipeline convert-to-json --help`

`[](#__codelineno-320-1) usage: pipeline [-h] --pipetype PIPE_TYPE [](#__codelineno-320-2) [](#__codelineno-320-3) optional arguments: [](#__codelineno-320-4)   -h, --help            show this help message and exit [](#__codelineno-320-5)   --pipetype PIPE_TYPE  Type of pipelines to convert : Published/Draft. It [](#__codelineno-320-6)                         converts all pipelines in published/draft folder to [](#__codelineno-320-7)                         json format.`

*   Following is the syntax for **pipeline convert-to-json**

`[](#__codelineno-321-1) rdac pipeline convert-to-json --pipetype Draft`

Example Output

`[](#__codelineno-322-1) 2023-01-09:11:19:40 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-322-2) 2023-01-09:11:19:40 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-322-3) 2023-01-09:11:19:40 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-322-4) [](#__codelineno-322-5) Converted following pipelines from yaml to json [](#__codelineno-322-6) [](#__codelineno-322-7)     pipeline_name                                 version [](#__codelineno-322-8) --  ---------------------------------------  ------------ [](#__codelineno-322-9)  0  all-stacks-join                          2022_09_28_1 [](#__codelineno-322-10)  1  appd_stack                               2022_09_28_1 [](#__codelineno-322-11)  2  appdynamics-enrichment                   2022_09_28_1 [](#__codelineno-322-12)  3  db_alerts_clustering                     2022_09_28_1 [](#__codelineno-322-13)  4  db_alerts_clustering                     2022_11_17_1 [](#__codelineno-322-14)  5  db_alerts_regression                     2022_09_28_1 [](#__codelineno-322-15)  6  db_alerts_regression                     2022_11_17_1 [](#__codelineno-322-16)  7  db_incidents_clustering                  2022_09_28_1 [](#__codelineno-322-17)  8  db_incidents_clustering                  2022_11_17_1 [](#__codelineno-322-18)  9  db_incidents_regression                  2022_09_28_1 [](#__codelineno-322-19) 10  db_incidents_regression                  2022_11_17_1 [](#__codelineno-322-20) 11  file_upload_alerts_clustering            2022_09_28_1 [](#__codelineno-322-21) 12  file_upload_alerts_clustering            2022_11_17_1 [](#__codelineno-322-22) 13  file_upload_incidents_clustering         2022_09_28_1 [](#__codelineno-322-23) 14  file_upload_incidents_clustering         2022_11_17_1 [](#__codelineno-322-24) 15  fileupload_alerts_regression             2022_09_28_1 [](#__codelineno-322-25) 16  fileupload_alerts_regression             2022_11_17_1 [](#__codelineno-322-26) 17  incident_notify_email                    2022_09_28_1 [](#__codelineno-322-27) 18  incident_notify_jenkins                  2022_09_28_1 [](#__codelineno-322-28) 19  incident_notify_msteams                  2022_09_28_1 [](#__codelineno-322-29) 20  incident_stack_asset_attributes_mapping  2022_09_28_1 [](#__codelineno-322-30) 21  incident_stack_generator                 2022_09_28_1`

****Sub Command: `publish`****

Description: Publish the pipeline on a worker pod

`[](#__codelineno-323-1) rdac pipeline publish --help`

`[](#__codelineno-324-1) usage: rdac [-h] --pipeline PIPELINE --name NAME --version VERSION --category [](#__codelineno-324-2)             CATEGORY [--usecase USECASE] [--folder FOLDER] [](#__codelineno-324-3)             [--group WORKER_GROUP] [--site WORKER_SITE] [](#__codelineno-324-4)             [--lfilter LABEL_FILTER] [--rfilter RESOURCE_FILTER] [](#__codelineno-324-5)             [--maxwait MAX_WAIT] [](#__codelineno-324-6) [](#__codelineno-324-7) optional arguments: [](#__codelineno-324-8)   -h, --help            show this help message and exit [](#__codelineno-324-9)   --pipeline PIPELINE   File containing pipeline contents [](#__codelineno-324-10)   --name NAME           Pipeline name [](#__codelineno-324-11)   --version VERSION     Pipeline version [](#__codelineno-324-12)   --category CATEGORY   Pipeline category [](#__codelineno-324-13)   --usecase USECASE     Pipeline usecase [](#__codelineno-324-14)   --folder FOLDER       Pipeline Folder [](#__codelineno-324-15)   --group WORKER_GROUP  Deprecated. Use --site option. Specify a worker site [](#__codelineno-324-16)                         name. If not specified, will use any available worker. [](#__codelineno-324-17)   --site WORKER_SITE    Specify a worker site name. If not specified, will use [](#__codelineno-324-18)                         any available worker. [](#__codelineno-324-19)   --lfilter LABEL_FILTER [](#__codelineno-324-20)                         CFXQL style query to narrow down workers using their [](#__codelineno-324-21)                         labels [](#__codelineno-324-22)   --rfilter RESOURCE_FILTER [](#__codelineno-324-23)                         CFXQL style query to narrow down workers using their [](#__codelineno-324-24)                         resources [](#__codelineno-324-25)   --maxwait MAX_WAIT    Maximum wait time (seconds) for credential check to [](#__codelineno-324-26)                         complete.`

*   Following is the syntax for **pipeline publish**

`[](#__codelineno-325-1) rdac pipeline publish --pipeline testpipelinenew --name nifty_fifty --version 2023_01_10 --category test`

Example Output

`[](#__codelineno-326-1) 2023-01-10:09:04:06 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-326-2) { [](#__codelineno-326-3)   "status": "started", [](#__codelineno-326-4)   "reason": "", [](#__codelineno-326-5)   "results": [], [](#__codelineno-326-6)   "now": "2023-01-10T09:04:06.130688", [](#__codelineno-326-7)   "status-subject": "tenants.ae144f67d2a24034ad6920ace6809763.worker.group.f4a56ba6388c.direct.88c26bbe", [](#__codelineno-326-8)   "jobid": "fa81de86812f4770a0ff8b700749f934" [](#__codelineno-326-9) } [](#__codelineno-326-10) Waiting: [](#__codelineno-326-11) Publishing Pipeline: [](#__codelineno-326-12) Completed:`

****Sub Command: `published-run`****

Description: Run a published pipeline on a worker pod

`[](#__codelineno-327-1) rdac pipeline published-run --help`

`[](#__codelineno-328-1) usage: pipeline [-h] --name NAME --version VERSION [--group WORKER_GROUP] [](#__codelineno-328-2)                 [--site WORKER_SITE] [--lfilter LABEL_FILTER] [](#__codelineno-328-3)                 [--rfilter RESOURCE_FILTER] [--maxwait MAX_WAIT] [](#__codelineno-328-4) [](#__codelineno-328-5) optional arguments: [](#__codelineno-328-6)   -h, --help            show this help message and exit [](#__codelineno-328-7)   --name NAME           Pipeline name [](#__codelineno-328-8)   --version VERSION     Pipeline version [](#__codelineno-328-9)   --group WORKER_GROUP  Deprecated. Use --site option. Specify a worker site [](#__codelineno-328-10)                         name. If not specified, will use any available worker. [](#__codelineno-328-11)   --site WORKER_SITE    Specify a worker site name. If not specified, will use [](#__codelineno-328-12)                         any available worker. [](#__codelineno-328-13)   --lfilter LABEL_FILTER [](#__codelineno-328-14)                         CFXQL style query to narrow down workers using their [](#__codelineno-328-15)                         labels [](#__codelineno-328-16)   --rfilter RESOURCE_FILTER [](#__codelineno-328-17)                         CFXQL style query to narrow down workers using their [](#__codelineno-328-18)                         resources [](#__codelineno-328-19)   --maxwait MAX_WAIT    Maximum wait time (seconds) for credential check to [](#__codelineno-328-20)                         complete.`

*   Following is the syntax for **pipeline published-run**

`[](#__codelineno-329-1) rdac pipeline published-run --name nifty_fifty --version 2023_01_10`

Example Output

`[](#__codelineno-330-1) 2023-01-10:09:05:31 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-330-2) { [](#__codelineno-330-3)   "status": "started", [](#__codelineno-330-4)   "reason": "", [](#__codelineno-330-5)   "now": "2023-01-10T09:05:31.126185", [](#__codelineno-330-6)   "pipeline-name": "nifty_fifty", [](#__codelineno-330-7)   "status-subject": "tenants.ae144f67d2a24034ad6920ace6809763.worker.group.f4a56ba6388c.direct.88c26bbe", [](#__codelineno-330-8)   "jobid": "1ec46b3ad80d496380ad1f9eb73482eb", [](#__codelineno-330-9)   "attributes": { [](#__codelineno-330-10)     "is_draft": "no" [](#__codelineno-330-11)   }, [](#__codelineno-330-12)   "pipeline-checksums": { [](#__codelineno-330-13)     "nifty_fifty": "785e1b5b" [](#__codelineno-330-14)   } [](#__codelineno-330-15) } [](#__codelineno-330-16) Waiting: [](#__codelineno-330-17) Initializing: [](#__codelineno-330-18) Running: [](#__codelineno-330-19) Running: [](#__codelineno-330-20) Running: [](#__codelineno-330-21) Running: [](#__codelineno-330-22) Running: [](#__codelineno-330-23) Running: [](#__codelineno-330-24) Running: [](#__codelineno-330-25) Running: [](#__codelineno-330-26) Completed:`

### Sub Command: `pods`

Description: List all pods for the current tenant

`[](#__codelineno-331-1) rdac pods --help`

`[](#__codelineno-332-1) usage: rdac [-h] [--json] [--type POD_TYPE] [--versions] [--infra] [--apps] [](#__codelineno-332-2) [](#__codelineno-332-3) optional arguments: [](#__codelineno-332-4)   -h, --help       show this help message and exit [](#__codelineno-332-5)   --json           Print detailed information in JSON format instead of [](#__codelineno-332-6)                    tabular format [](#__codelineno-332-7)   --type POD_TYPE  Show only the pods that match the specified pod type [](#__codelineno-332-8)   --versions       Show versions for each pod in tabular format, not [](#__codelineno-332-9)                    compatible with --json option [](#__codelineno-332-10)   --infra          List only RDA Infra pods. not compatible with --apps option [](#__codelineno-332-11)   --apps           List only RDA App pods. not compatible with --infra option`

*   Following is the syntax for **pods**

`[](#__codelineno-333-1) rdac pods --type worker --json`

Example Output

`[](#__codelineno-334-1) 2023-01-10:10:37:12 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-334-2) [ [](#__codelineno-334-3)     { [](#__codelineno-334-4)         "now": "2023-01-10T10:37:12.289225", [](#__codelineno-334-5)         "started_at": "2023-01-07T13:30:42.380413", [](#__codelineno-334-6)         "pod_type": "worker", [](#__codelineno-334-7)         "pod_category": "rda_infra", [](#__codelineno-334-8)         "pod_id": "88c26bbe", [](#__codelineno-334-9)         "hostname": "05969789d903", [](#__codelineno-334-10)         "proc_id": 10, [](#__codelineno-334-11)         "labels": { [](#__codelineno-334-12)             "rda_platform_version": "22.12.8.3", [](#__codelineno-334-13)             "rda_messenger_version": "22.12.19.1", [](#__codelineno-334-14)             "rda_pod_version": "22.12.14", [](#__codelineno-334-15)             "rda_license_valid": "no", [](#__codelineno-334-16)             "rda_license_not_expired": "no", [](#__codelineno-334-17)             "rda_license_expiration_date": "" [](#__codelineno-334-18)         }, [](#__codelineno-334-19)         "build_tag": "daily", [](#__codelineno-334-20)         "requests": { [](#__codelineno-334-21)             "auto": "tenants.ae144f67d2a24034ad6920ace6809763.worker.group.f4a56ba6388c.auto", [](#__codelineno-334-22)             "direct": "tenants.ae144f67d2a24034ad6920ace6809763.worker.group.f4a56ba6388c.direct.88c26bbe" [](#__codelineno-334-23)         }, [](#__codelineno-334-24)         "resources": { [](#__codelineno-334-25)             "cpu_count": 4, [](#__codelineno-334-26)             "cpu_load1": 6.7, [](#__codelineno-334-27)             "cpu_load5": 7.08, [](#__codelineno-334-28)             "cpu_load15": 7.14, [](#__codelineno-334-29)             "mem_total_gb": 39.16, [](#__codelineno-334-30)             "mem_available_gb": 15.34, [](#__codelineno-334-31)             "mem_percent": 60.8,`\
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
`[](#__codelineno-335-1) rdac pod-logging --help`\
\
`[](#__codelineno-336-1) pod logging commands [](#__codelineno-336-2) [](#__codelineno-336-3) Following are valid sub-commands for pod-logging: [](#__codelineno-336-4)   get                       Get logging configuration of given pod [](#__codelineno-336-5)   set                       Update the logging level of a logging component for a given RDA Pod [](#__codelineno-336-6)   handler-set               Update the logging level of a handler for a given RDA Pod [](#__codelineno-336-7)   handler-get               Get all logging handlers and handler configuration for a given RDA Pod`\
\
****Sub Command: `get`****\
\
Description: Get logging configuration of given pod\
\
`[](#__codelineno-337-1) rdac pod-logging get --help`\
\
`[](#__codelineno-338-1) usage: pod-logging [-h] --id POD_ID [--logger LOGGER_NAME] [](#__codelineno-338-2) [](#__codelineno-338-3) optional arguments: [](#__codelineno-338-4)   -h, --help            show this help message and exit [](#__codelineno-338-5)   --id POD_ID           pod_id of the pod for which the logging level need to [](#__codelineno-338-6)                         be retrieved [](#__codelineno-338-7)   --logger LOGGER_NAME  Logging Name. By default it sets the root logger.`\
\
****Sub Command: `set`****\
\
Description: Update the logging level of a logging component for a given RDA Pod\
\
`[](#__codelineno-339-1) rdac pod-logging set --help`\
\
`[](#__codelineno-340-1) usage: pod-logging [-h] --id POD_ID --level LEVEL [--logger LOGGER_NAME] [](#__codelineno-340-2) [](#__codelineno-340-3) optional arguments: [](#__codelineno-340-4)   -h, --help            show this help message and exit [](#__codelineno-340-5)   --id POD_ID           pod_id of the pod for which the logging level need to [](#__codelineno-340-6)                         be configured [](#__codelineno-340-7)   --level LEVEL         Logging level. Must be one of DEBUG INFO WARNING ERROR [](#__codelineno-340-8)                         CRITICAL [](#__codelineno-340-9)   --logger LOGGER_NAME  Logging Name. By default it sets the root logger.`\
\
*   Following is the Syntax for **pod-logging set**\
\
`[](#__codelineno-341-1) rdac set-pod-log-level --id <required pod id> --level <required log level>`\
\
Example Output\
\
`[](#__codelineno-342-1) rdac set-pod-log-level --id 07a337e5 --level DEBUG [](#__codelineno-342-2) Successfully updated logging level for pod 07a337e5`\
\
****Sub Command: `handler-set`****\
\
Description: Update the logging level of a handler for a given RDA Pod\
\
`[](#__codelineno-343-1) rdac pod-logging handler-set --help`\
\
`[](#__codelineno-344-1) usage: pod-logging [-h] --id POD_ID --level LEVEL [--handler HANDLER_NAME] [](#__codelineno-344-2) [](#__codelineno-344-3) optional arguments: [](#__codelineno-344-4)   -h, --help            show this help message and exit [](#__codelineno-344-5)   --id POD_ID           pod_id of the pod for which the logging level need to [](#__codelineno-344-6)                         be configured [](#__codelineno-344-7)   --level LEVEL         Logging level. Must be one of DEBUG INFO WARNING ERROR [](#__codelineno-344-8)                         CRITICAL [](#__codelineno-344-9)   --handler HANDLER_NAME [](#__codelineno-344-10)                         Logging Handler name. (e.g. console/file_handler) as [](#__codelineno-344-11)                         specified in logging configuration file. If not [](#__codelineno-344-12)                         specified, all the handlers will be set to the level [](#__codelineno-344-13)                         provided.`\
\
*   Following is the Syntax for **pod-logging handler-set**\
\
`[](#__codelineno-345-1) rdac pod-logging handler-set --id <required pod id> --level <required log level>`\
\
Example Output\
\
`[](#__codelineno-346-1) rdac pod-logging handler-set --id 07a337e5 --level DEBUG [](#__codelineno-346-2) Successfully updated logging level for pod 07a337e5`\
\
****Sub Command: `handler-get`****\
\
Description: Get all logging handlers and handler configuration for a given RDA Pod\
\
`[](#__codelineno-347-1) rdac pod-logging handler-get --help`\
\
`[](#__codelineno-348-1) usage: pod-logging [-h] --id POD_ID [](#__codelineno-348-2) [](#__codelineno-348-3) optional arguments: [](#__codelineno-348-4)   -h, --help   show this help message and exit [](#__codelineno-348-5)   --id POD_ID  pod_id of the pod for which the logging level need to be [](#__codelineno-348-6)                retrieved`\
\
### Sub Command: `pod-logging-handler-set`\
\
Description: To change log levels for any required pod\
\
`[](#__codelineno-349-1) rdac pod-logging-handler-set --help`\
\
`[](#__codelineno-350-1) usage: rdac [-h] --id POD_ID --level LEVEL [--handler HANDLER_NAME] [](#__codelineno-350-2) [](#__codelineno-350-3) optional arguments: [](#__codelineno-350-4)   -h, --help            show this help message and exit [](#__codelineno-350-5)   --id POD_ID           pod_id of the pod for which the logging level need to [](#__codelineno-350-6)                         be configured [](#__codelineno-350-7)   --level LEVEL         Logging level. Must be one of DEBUG INFO WARNING ERROR [](#__codelineno-350-8)                         CRITICAL [](#__codelineno-350-9)   --handler HANDLER_NAME [](#__codelineno-350-10)                         Logging Handler name. (e.g. console/file_handler) as [](#__codelineno-350-11)                         specified in logging configuration file. If not [](#__codelineno-350-12)                         specified, all the handlers will be set to the level [](#__codelineno-350-13)                         provided.`\
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
`[](#__codelineno-351-1) rdac project --help`\
\
`[](#__codelineno-352-1) Project management commands. Projects can be used to link different tenants / projects from this RDA Fabric or a remote RDA Fabric. [](#__codelineno-352-2) [](#__codelineno-352-3) Following are valid sub-commands for project: [](#__codelineno-352-4)   add                       Add or update project [](#__codelineno-352-5)   get                       Get YAML data for a project [](#__codelineno-352-6)   list                      List all projects [](#__codelineno-352-7)   delete                    Delete a project [](#__codelineno-352-8)   enable                    Change the status of a project to 'enabled' [](#__codelineno-352-9)   disable                   Change the status of a project to 'disabled'`\
\
****Sub Command: `add`****\
\
Description: Add or update project\
\
`[](#__codelineno-353-1) rdac project add --help`\
\
`[](#__codelineno-354-1) usage: project [-h] --file INPUT_FILE [--overwrite] [--rda_config RDA_CONFIG] [](#__codelineno-354-2) [](#__codelineno-354-3) optional arguments: [](#__codelineno-354-4)   -h, --help            show this help message and exit [](#__codelineno-354-5)   --file INPUT_FILE     YAML file containing project definition [](#__codelineno-354-6)   --overwrite           Overwrite even if a project already exists with the [](#__codelineno-354-7)                         specified name. [](#__codelineno-354-8)   --rda_config RDA_CONFIG [](#__codelineno-354-9)                         JSON file containing RDA Credentials (if the project [](#__codelineno-354-10)                         belongs to a remote system)`\
\
*   Following is the syntax for **project add**\
\
`[](#__codelineno-355-1) rdac project add --file projecttest.yml`\
\
Example Output\
\
`[](#__codelineno-356-1) Added project oia-2`\
\
Note\
\
Create a project YAML file before adding a new project\
\
Sample Project YAML File\
\
`[](#__codelineno-357-1) name: "oia-2" [](#__codelineno-357-2) customerId: "3edd7c702f5d442982dfcd493d2fe7b3" [](#__codelineno-357-3) projectId: "3f9ef108-62b8-46d3-bc9e-caee1c53c174" [](#__codelineno-357-4) userId: "acme@cfx.com" [](#__codelineno-357-5) label: "ACME 2"`\
\
****Sub Command: `list`****\
\
Description: List all projects\
\
`[](#__codelineno-358-1) rdac project list --help`\
\
`[](#__codelineno-359-1) usage: project [-h] [--json] [](#__codelineno-359-2) [](#__codelineno-359-3) optional arguments: [](#__codelineno-359-4)   -h, --help  show this help message and exit [](#__codelineno-359-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-359-6)               format`\
\
\* Following is the syntax for **project list**\
\
`[](#__codelineno-360-1) rdac project list`\
\
Example Output\
\
    `[](#__codelineno-361-1)     name    label          enabled    customerId    projectId    tenant_id    nats_url    minio_host    saved_time [](#__codelineno-361-2) --  ------  -------------  ---------  ------------  -----------  -----------  ----------  ------------  -------------------------- [](#__codelineno-361-3)  0  n-bank  National Bank  yes        ae144f**      c2b89a**                                            2022-09-28T05:50:06.285929 [](#__codelineno-361-4)  1  oia-2   ACME 2         no         3edd7c**      3f9ef1**                                            2023-01-23T05:11:28.716514`\
\
****Sub Command: `enable`****\
\
Description: Change the status of a project to 'enabled'\
\
`[](#__codelineno-362-1) rdac project enable --help`\
\
`[](#__codelineno-363-1) usage: project [-h] --name PROJECT_NAME [](#__codelineno-363-2) [](#__codelineno-363-3) optional arguments: [](#__codelineno-363-4)   -h, --help           show this help message and exit [](#__codelineno-363-5)   --name PROJECT_NAME  Name of the project`\
\
\* Following is the syntax for **project enable**\
\
`[](#__codelineno-364-1) rdac project enable --name oia-2`\
\
Example Output\
\
`[](#__codelineno-365-1) Changed status of oia-2 to enabled`\
\
****Sub Command: `disable`****\
\
Description: Change the status of a project to 'disabled'\
\
`[](#__codelineno-366-1) rdac project disable --help`\
\
`[](#__codelineno-367-1) usage: project [-h] --name PROJECT_NAME [](#__codelineno-367-2) [](#__codelineno-367-3) optional arguments: [](#__codelineno-367-4)   -h, --help           show this help message and exit [](#__codelineno-367-5)   --name PROJECT_NAME  Name of the project`\
\
\* Following is the syntax for **project disable**\
\
`[](#__codelineno-368-1) rdac project disable  --name oia-2`\
\
Example Output\
\
`[](#__codelineno-369-1) Changed status of oia-2 to disabled`\
\
****Sub Command: `get`****\
\
Description: Get YAML data for a project\
\
`[](#__codelineno-370-1) rdac project get --help`\
\
`[](#__codelineno-371-1) usage: project [-h] --name PROJECT_NAME [](#__codelineno-371-2) [](#__codelineno-371-3) optional arguments: [](#__codelineno-371-4)   -h, --help           show this help message and exit [](#__codelineno-371-5)   --name PROJECT_NAME  Name of the project`\
\
\* Following is the syntax for **project get**\
\
`[](#__codelineno-372-1) rdac project get --name oia-2`\
\
Example Output\
\
`[](#__codelineno-373-1) name: oia-2 [](#__codelineno-373-2) customerId: 3edd7c702f5d442982dfcd493d2fe7b3 [](#__codelineno-373-3) projectId: 3f9ef108-62b8-46d3-bc9e-caee1c53c174 [](#__codelineno-373-4) userId: acme@cfx.com [](#__codelineno-373-5) label: ACME 2 [](#__codelineno-373-6) saved_time: '2023-01-23T05:11:28.716514' [](#__codelineno-373-7) enabled: false`\
\
****Sub Command: `delete`****\
\
Description: Delete a project\
\
`[](#__codelineno-374-1) rdac project delete --help`\
\
`[](#__codelineno-375-1) usage: project [-h] --name PROJECT_NAME [](#__codelineno-375-2) [](#__codelineno-375-3) optional arguments: [](#__codelineno-375-4)   -h, --help           show this help message and exit [](#__codelineno-375-5)   --name PROJECT_NAME  Name of the project to delete`\
\
*   Following is the syntax for **project delete**\
\
`[](#__codelineno-376-1) rdac project delete --name oia-2`\
\
Example Output\
\
`[](#__codelineno-377-1) Deleted project: oia-2`\
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
`[](#__codelineno-378-1) rdac pstream --help`\
\
`[](#__codelineno-379-1) Persistent Stream management commands [](#__codelineno-379-2) [](#__codelineno-379-3) Following are valid sub-commands for pstream: [](#__codelineno-379-4) [](#__codelineno-379-5)   list                      List persistent streams [](#__codelineno-379-6)   status                    Status of the persistent streams [](#__codelineno-379-7)   get                       Get information about a persistent stream [](#__codelineno-379-8)   metadata                  Get metadata information about a persistent stream [](#__codelineno-379-9)   add                       Add a new Persistent stream [](#__codelineno-379-10)   delete                    Delete a persistent stream [](#__codelineno-379-11)   query                     Query persistent stream data via collector [](#__codelineno-379-12)   delete-by-query           Delete persistent stream data via CFXQL query [](#__codelineno-379-13)   update-by-query           Update column(s) in persistent stream data via CFXQL query [](#__codelineno-379-14)   add-column                Add column to the persistent stream records that don't have it and set a value via expression [](#__codelineno-379-15)   tail                      Query a persistent stream and continue to query for incremental data every few seconds [](#__codelineno-379-16)   export                    Query a persistent stream and export data to CSV or JSON file [](#__codelineno-379-17)   export-chunks             Query a persistent stream and export data as minio chunks [](#__codelineno-379-18)   migrate                   Query a persistent stream and export to another stream with optional type conversion [](#__codelineno-379-19)   load                      Load data from a CSV file into a persistent stream with optional type conversion [](#__codelineno-379-20)   ingest                    Ingest data to pstream by directly adding data to Open Search [](#__codelineno-379-21)   evict                     Evict Ingestion Job [](#__codelineno-379-22)   evict-export              Evict Export Chunks Job`\
\
****Sub Command: `list`****\
\
Description : List persistent streams\
\
`[](#__codelineno-380-1) rdac pstream list --help`\
\
`[](#__codelineno-381-1) usage: pstream [-h] [--json] [](#__codelineno-381-2) [](#__codelineno-381-3) optional arguments: [](#__codelineno-381-4)   -h, --help  show this help message and exit [](#__codelineno-381-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-381-6)               format`\
\
*   Following is the syntax for **pstream list**\
\
`[](#__codelineno-382-1) rdac pstream list`\
\
Example Output One\
\
`[](#__codelineno-383-1) Detected OS Name: Linux [](#__codelineno-383-2) Detected docker version: 20.10.12 [](#__codelineno-383-3)     name                                       index_name                                                                                  saved_time                  retention_days [](#__codelineno-383-4) --  -----------------------------------------  ------------------------------------------------------------------------------------------  --------------------------  ---------------- [](#__codelineno-383-5)  0  rda_synthetic_metrics                      f92bc678629540f0bcaf7749177acccb-stream-03e632e0-rda_synthetic_metrics                      2022-11-15T04:15:41.692800  31 [](#__codelineno-383-6)  1  oia-incidents-data-coll-stream             f92bc678629540f0bcaf7749177acccb-stream-09c0c9b9-oia-incidents-data-coll-stream             2022-11-14T10:39:14.080246  7 [](#__codelineno-383-7)  2  rdaf_services_logs                         f92bc678629540f0bcaf7749177acccb-stream-rdaf_services_logs                                  2022-11-14T10:29:40.564683  15 [](#__codelineno-383-8)  3  dli-synthetic-logs-processed               f92bc678629540f0bcaf7749177acccb-stream-10fe40a6-dli-synthetic-logs-processed               2022-11-14T15:33:16.490331  31 [](#__codelineno-383-9)  4  test_oia-incident-inserts-pstream          f92bc678629540f0bcaf7749177acccb-stream-1eb8a4d3-test_oia-incident-inserts-pstream          2022-12-05T07:22:48.543676  7 [](#__codelineno-383-10)  5  oia-incidents-collaboration-stream         f92bc678629540f0bcaf7749177acccb-stream-23f2f83a-oia-incidents-collaboration-stream         2022-11-14T10:36:52.070142  7 [](#__codelineno-383-11)  6  dli-log-stats                              f92bc678629540f0bcaf7749177acccb-stream-25235c4a-dli-log-stats                              2022-11-14T15:33:16.356427  90`\
\
*   Another example syntax for **pstream list**\
\
`[](#__codelineno-384-1) rdac pstream list --json`\
\
Example Output Two\
\
`[](#__codelineno-385-1) { [](#__codelineno-385-2)     "attrs": { [](#__codelineno-385-3)       "unique_keys": [ [](#__codelineno-385-4)         "name" [](#__codelineno-385-5)       ], [](#__codelineno-385-6)       "system_defined": "yes" [](#__codelineno-385-7)     }, [](#__codelineno-385-8)     "datastore_type": "OS", [](#__codelineno-385-9)     "index_name": "cf75a3efaa26491b9efea482d2ac981c-stream-01970753-rda_secrets_meta", [](#__codelineno-385-10)     "name": "rda_secrets_meta", [](#__codelineno-385-11)     "saved_time": "2023-11-08T07:45:44.541749", [](#__codelineno-385-12)     "status": "Running" [](#__codelineno-385-13)   },`\
\
****Sub Command: `status`****\
\
Description : Status of the persistent streams\
\
`[](#__codelineno-386-1) rdac pstream status --help`\
\
`[](#__codelineno-387-1) usage: pstream [-h] [--json] [](#__codelineno-387-2) [](#__codelineno-387-3) optional arguments: [](#__codelineno-387-4)   -h, --help  show this help message and exit [](#__codelineno-387-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-387-6)               format`\
\
*   Following is the syntax for **pstream status**\
\
`[](#__codelineno-388-1) rdac pstream status`\
\
Example Output One\
\
`[](#__codelineno-389-1) Detected OS Name: Linux [](#__codelineno-389-2) Detected docker version: 20.10.12 [](#__codelineno-389-3)     name                                       index_exists      docs_count    size_in_bytes    shards_failed    shards_successful    shards_total  status [](#__codelineno-389-4) --  -----------------------------------------  --------------  ------------  ---------------  ---------------  -------------------  --------------  -------- [](#__codelineno-389-5)  0  rda_synthetic_metrics                      True                  100000         10929315                0                    3               6  OK [](#__codelineno-389-6)  1  oia-incidents-data-coll-stream             True                       0              690                0                    3               6  OK [](#__codelineno-389-7)  2  rdaf_services_logs                         True                17733976       8751155216                0                    3               6  OK [](#__codelineno-389-8)  3  dli-synthetic-logs-processed               True                 4964025        697988506                0                    3               6  OK [](#__codelineno-389-9)  4  test_oia-incident-inserts-pstream          True                       0              690                0                    3               6  OK [](#__codelineno-389-10)  5  oia-incidents-collaboration-stream         True                       0              690                0                    3               6  OK [](#__codelineno-389-11)  6  dli-log-stats                              True                 1028976         77565766                0                    3               6  OK [](#__codelineno-389-12)  7  regression-aggregated-anomalies            True                    2529           731537                0                    3               6  OK [](#__codelineno-389-13)  8  oia-incidents-delta-stream                 True                       0              690                0                    3               6  OK [](#__codelineno-389-14)  9  dli-synthetic-logs-dropped                 True                       0            71681                0                    3               6  OK [](#__codelineno-389-15) 10  oia-alerts-kpi-stream                      True                      44            26682                0                    3               6  OK`\
\
*   Another example syntax for **pstream status**\
\
`[](#__codelineno-390-1) rdac pstream status --json`\
\
Example Output Two\
\
`[](#__codelineno-391-1) { [](#__codelineno-391-2)   "status": "ok", [](#__codelineno-391-3)   "reason": "", [](#__codelineno-391-4)   "data": [ [](#__codelineno-391-5)     { [](#__codelineno-391-6)       "name": "rda_secrets_meta", [](#__codelineno-391-7)       "datastore_type": "OS", [](#__codelineno-391-8)       "index_exists": true, [](#__codelineno-391-9)       "docs_count": 0, [](#__codelineno-391-10)       "size_in_bytes": 624, [](#__codelineno-391-11)       "shards_total": 6, [](#__codelineno-391-12)       "shards_successful": 3, [](#__codelineno-391-13)       "shards_failed": 0, [](#__codelineno-391-14)       "status": "OK" [](#__codelineno-391-15)     },`\
\
****Sub Command: `get`****\
\
Description : Get information about a persistent stream\
\
`[](#__codelineno-392-1) rdac pstream get --help`\
\
`[](#__codelineno-393-1) usage: pstream [-h] --name NAME [--json] [](#__codelineno-393-2) [](#__codelineno-393-3) optional arguments: [](#__codelineno-393-4)   -h, --help   show this help message and exit [](#__codelineno-393-5)   --name NAME  Persistent Stream name [](#__codelineno-393-6)   --json       Print in JSON format instead of text format`\
\
*   Following is the syntax for **pstream get**\
\
`[](#__codelineno-394-1) rdac pstream get --name  test_oia-incident-inserts-pstream`\
\
Example Output One\
\
`[](#__codelineno-395-1) Detected OS Name: Linux [](#__codelineno-395-2) Detected docker version: 20.10.12 [](#__codelineno-395-3) Stream Name: test_oia-incident-inserts-pstream [](#__codelineno-395-4) Index  Name: f92bc678629540f0bcaf7749177acccb-stream-1eb8a4d3-test_oia-incident-inserts-pstream [](#__codelineno-395-5) Saved Time : 2022-12-05T07:22:48.543676 [](#__codelineno-395-6) Attributes [](#__codelineno-395-7)   retention_days: 7 [](#__codelineno-395-8)   unique_keys: ['project_id'] [](#__codelineno-395-9)   timestamp: timestamp`\
\
*   Another example syntax for **pstream get**\
\
`[](#__codelineno-396-1) rdac pstream get --name oia-metrics-data --json`\
\
Example Output Two\
\
`[](#__codelineno-397-1) { [](#__codelineno-397-2)   "name": "oia-metrics-data", [](#__codelineno-397-3)   "datastore_type": "OS", [](#__codelineno-397-4)   "attrs": { [](#__codelineno-397-5)     "case_insensitive": true, [](#__codelineno-397-6)     "unique_keys": [ [](#__codelineno-397-7)       "asset_id", [](#__codelineno-397-8)       "metric_id", [](#__codelineno-397-9)       "metric_source", [](#__codelineno-397-10)       "metric_timestamp" [](#__codelineno-397-11)     ], [](#__codelineno-397-12)     "retention_days": "90" [](#__codelineno-397-13)   }, [](#__codelineno-397-14)   "saved_time": "2023-11-08T09:10:06.755111", [](#__codelineno-397-15)   "index_name": "cf75a3efaa26491b9efea482d2ac981c-stream-08d2fd46-oia-metrics-data", [](#__codelineno-397-16)   "status": "Running" [](#__codelineno-397-17) }`\
\
****Sub Command: `metadata`****\
\
Description : Get metadata information about a persistent stream\
\
`[](#__codelineno-398-1) rdac pstream metadata --help`\
\
`[](#__codelineno-399-1) usage: pstream [-h] --name NAME [--json] [](#__codelineno-399-2) [](#__codelineno-399-3) optional arguments: [](#__codelineno-399-4)   -h, --help   show this help message and exit [](#__codelineno-399-5)   --name NAME  Persistent Stream name [](#__codelineno-399-6)   --json       Print in JSON format instead of text format`\
\
*   Following is the syntax for **pstream metadata**\
\
`[](#__codelineno-400-1) rdac pstream metadata --name rda_synthetic_metrics`\
\
Example Output\
\
`[](#__codelineno-401-1) Detected OS Name: Linux [](#__codelineno-401-2) Detected docker version: 20.10.12 [](#__codelineno-401-3)     columnId             keywordColumn        mappedType    parent       type [](#__codelineno-401-4) --  -------------------  -------------------  ------------  -----------  ------- [](#__codelineno-401-5)  0  component.keyword                         TEXT          component    keyword [](#__codelineno-401-6)  1  component            component.keyword    TEXT                       text [](#__codelineno-401-7)  2  count_                                    DOUBLE                     long [](#__codelineno-401-8)  3  layer.keyword                             TEXT          layer        keyword [](#__codelineno-401-9)  4  layer                layer.keyword        TEXT                       text [](#__codelineno-401-10)  5  metric_name.keyword                       TEXT          metric_name  keyword [](#__codelineno-401-11)  6  metric_name          metric_name.keyword  TEXT                       text [](#__codelineno-401-12)  7  node_id.keyword                           TEXT          node_id      keyword [](#__codelineno-401-13)  8  node_id              node_id.keyword      TEXT                       text [](#__codelineno-401-14)  9  node_label.keyword                        TEXT          node_label   keyword [](#__codelineno-401-15) 10  node_label           node_label.keyword   TEXT                       text [](#__codelineno-401-16) 11  node_type.keyword                         TEXT          node_type    keyword [](#__codelineno-401-17) 12  node_type            node_type.keyword    TEXT                       text [](#__codelineno-401-18) 13  source_tool.keyword                       TEXT          source_tool  keyword [](#__codelineno-401-19) 14  source_tool          source_tool.keyword  TEXT                       text [](#__codelineno-401-20) 15  stack_name.keyword                        TEXT          stack_name   keyword [](#__codelineno-401-21) 16  stack_name           stack_name.keyword   TEXT                       text [](#__codelineno-401-22) 17  timestamp                                 DATETIME                   date [](#__codelineno-401-23) 18  unit.keyword                              TEXT          unit         keyword [](#__codelineno-401-24) 19  unit                 unit.keyword         TEXT                       text [](#__codelineno-401-25) 20  value                                     DOUBLE                     float`\
\
****Sub Command: `add`****\
\
Description : Add a new Persistent stream\
\
`[](#__codelineno-402-1) rdac pstream add --help`\
\
`[](#__codelineno-403-1) usage: pstream [-h] --name NAME [--index INDEX_NAME] [](#__codelineno-403-2)                [--attr [ATTRS [ATTRS ...]]] [--retention_days RETENTION_DAYS] [](#__codelineno-403-3)                [--unique_keys UNIQUE_KEYS] [--auto_expand AUTO_EXPAND] [](#__codelineno-403-4)                [--drop DROP] [--computed COMPUTED] [--timestamp TIMESTAMP] [](#__codelineno-403-5) [](#__codelineno-403-6) optional arguments: [](#__codelineno-403-7)   -h, --help            show this help message and exit [](#__codelineno-403-8)   --name NAME           Persistent Stream name [](#__codelineno-403-9)   --index INDEX_NAME    OpenSearch index name to store Persistent Stream [](#__codelineno-403-10)   --attr [ATTRS [ATTRS ...]] [](#__codelineno-403-11)                         Optional name=value pairs to add to attributes of [](#__codelineno-403-12)                         persistent stream [](#__codelineno-403-13)   --retention_days RETENTION_DAYS [](#__codelineno-403-14)                         Number of days to retain the data [](#__codelineno-403-15)   --unique_keys UNIQUE_KEYS [](#__codelineno-403-16)                         Comma separated list of column names to make each row [](#__codelineno-403-17)                         unique [](#__codelineno-403-18)   --auto_expand AUTO_EXPAND [](#__codelineno-403-19)                         Comma separated list of column names that should [](#__codelineno-403-20)                         parsed as JSON dicts and expanded [](#__codelineno-403-21)   --drop DROP           Comma separated list of column names that should be [](#__codelineno-403-22)                         dropped before persisting [](#__codelineno-403-23)   --computed COMPUTED   JSON fille containing computed column definition [](#__codelineno-403-24)   --timestamp TIMESTAMP [](#__codelineno-403-25)                         Timestamp column name`\
\
*   Following is the syntax for **pstream add**\
\
`[](#__codelineno-404-1) rdac pstream add --name test_oia-incident-inserts-pstream --retention_days 7 --unique_keys project_id --timestamp timestamp`\
\
Example Output One\
\
`[](#__codelineno-405-1) Detected OS Name: Linux [](#__codelineno-405-2) Detected docker version: 20.10.12 [](#__codelineno-405-3) { [](#__codelineno-405-4)   "retention_days": 7, [](#__codelineno-405-5)   "unique_keys": [ [](#__codelineno-405-6)     "project_id" [](#__codelineno-405-7)   ], [](#__codelineno-405-8)   "timestamp": "timestamp" [](#__codelineno-405-9) } [](#__codelineno-405-10) Persistent stream saved.`\
\
\* Following is the syntax for **pstream add with attr, auto\_expand & Compute**\
\
`[](#__codelineno-406-1) rdac pstream add --name oia-incidents-stream --attr 'retention_days=1' --auto_expand "resolved_at,created" --computed test.json`\
\
Example Output Two\
\
`[](#__codelineno-407-1) { [](#__codelineno-407-2)   "retention_days": "1", [](#__codelineno-407-3)   "auto_expand": [ [](#__codelineno-407-4)     "resolved_at", [](#__codelineno-407-5)     "created" [](#__codelineno-407-6)   ], [](#__codelineno-407-7)   "search_case_insensitive": true, [](#__codelineno-407-8)   "computed_columns": { [](#__codelineno-407-9)     "ttr_minutes": { [](#__codelineno-407-10)       "expr": "(resolved_at - created)/(1000.0*60)", [](#__codelineno-407-11)       "default": null [](#__codelineno-407-12)     }, [](#__codelineno-407-13)     "created_iso": { [](#__codelineno-407-14)       "expr": "ms_to_isoformat(created)" [](#__codelineno-407-15)     }, [](#__codelineno-407-16)     "resolved_at_iso": { [](#__codelineno-407-17)       "expr": "ms_to_isoformat(resolved_at)" [](#__codelineno-407-18)     } [](#__codelineno-407-19)   } [](#__codelineno-407-20) } [](#__codelineno-407-21) Persistent stream saved.`\
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
`[](#__codelineno-408-1) rdac pstream add --name server_cpu_metrics --retention_days 7 --timestamp timestamp --index 79cc72a1697b487fb2da7b99f0a0cc1a-stream-server_cpu_metrics`\
\
Warning\
\
Index name always should start with Organization ID. If Organization id is not prefixed as part of user defined index name, the data ingestion into pstream will be failed with permission errors.\
\
****Sub Command: `delete`****\
\
Description : Delete a persistent stream\
\
`[](#__codelineno-409-1) rdac pstream delete --help`\
\
`[](#__codelineno-410-1) usage: pstream [-h] --name NAME [--delete_index] [](#__codelineno-410-2) [](#__codelineno-410-3) optional arguments: [](#__codelineno-410-4)   -h, --help      show this help message and exit [](#__codelineno-410-5)   --name NAME     Persistent Stream name [](#__codelineno-410-6)   --delete_index  Delete all the data and metadata from open search`\
\
*   Following is the syntax for **pstream delete**\
\
`[](#__codelineno-411-1) rdac pstream delete --name test_oia-incident-inserts-pstream`\
\
Example Output\
\
`[](#__codelineno-412-1) Detected OS Name: Linux [](#__codelineno-412-2) Detected docker version: 20.10.12 [](#__codelineno-412-3) Deleted persistent stream`\
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
`[](#__codelineno-413-1) rdac pstream query --help`\
\
`[](#__codelineno-414-1) usage: pstream [-h] --name NAME [--max_rows MAX_ROWS] [--query CFXQL_QUERY] [](#__codelineno-414-2)                [--aggs AGGS] [--groupby GROUPBY] [--sortby SORT_BY] [](#__codelineno-414-3)                [--order SORT_ORDER] [--ts TS_COLUMN] [--json] [--no_sort] [](#__codelineno-414-4) [](#__codelineno-414-5) optional arguments: [](#__codelineno-414-6)   -h, --help           show this help message and exit [](#__codelineno-414-7)   --name NAME          Persistent Stream name [](#__codelineno-414-8)   --max_rows MAX_ROWS  Max rows in output [](#__codelineno-414-9)   --query CFXQL_QUERY  CFXQL Query [](#__codelineno-414-10)   --aggs AGGS          Optional aggs, specified as 'sum:field_name' [](#__codelineno-414-11)   --groupby GROUPBY    Comma separated list of columns to groupby. Used only [](#__codelineno-414-12)                        when --aggs is used [](#__codelineno-414-13)   --sortby SORT_BY     Comma separated list of columns to sort by. Default is [](#__codelineno-414-14)                        timestamp column. [](#__codelineno-414-15)   --order SORT_ORDER   Sort oder. Must be one 'asc' or 'desc'. Default is [](#__codelineno-414-16)                        'desc' [](#__codelineno-414-17)   --ts TS_COLUMN       Timestamp column for sorting. Default is 'timestamp' [](#__codelineno-414-18)   --json               Print detailed information in JSON format instead of [](#__codelineno-414-19)                        tabular format [](#__codelineno-414-20)   --no_sort            Do not sort by timestamp field`\
\
*   Following is the syntax for **pstream query**\
\
`[](#__codelineno-415-1) pstream query --name rda_synthetic_metrics --query "* GET metric_name" --max 5`\
\
Example Output One\
\
`[](#__codelineno-416-1) Detected OS Name: Linux [](#__codelineno-416-2) Detected docker version: 20.10.12 [](#__codelineno-416-3)     metric_name [](#__codelineno-416-4) --  ------------------------------ [](#__codelineno-416-5)  0  host_cpu_usage [](#__codelineno-416-6)  1  host_mem_usage [](#__codelineno-416-7)  2  transaction_time [](#__codelineno-416-8)  3  shared_svc_total_response_time [](#__codelineno-416-9)  4  total_response_time`\
\
Query persistent stream with CFXQL filters, in this example, querying the data and get one of the data record within last 5 mins. Since `@timestamp` has special character, it need to be escaped as shown below.\
\
``[](#__codelineno-417-1) rdac pstream query --name rdaf_services_logs --json --query '"\`@timestamp\`" is after -5min' --max_rows 1``\
\
Example Output Two\
\
`[](#__codelineno-418-1) [ [](#__codelineno-418-2)   { [](#__codelineno-418-3)     "_id": "BjhB7oQBXeLk1V97kTCm", [](#__codelineno-418-4)     "_index": "79cc72a1697b487fb2da7b99f0a0cc1a-stream-rdaf_services_logs", [](#__codelineno-418-5)     "sort": [ [](#__codelineno-418-6)       1670444585275, [](#__codelineno-418-7)       "BjhB7oQBXeLk1V97kTCm" [](#__codelineno-418-8)     ], [](#__codelineno-418-9)     "_score": null, [](#__codelineno-418-10)     "process_name": "systemd-networkd", [](#__codelineno-418-11)     "log_message": "veth7809965: Gained IPv6LL", [](#__codelineno-418-12)     "host": "10.95.101.175", [](#__codelineno-418-13)     "service_category": "rda_infra_svcs", [](#__codelineno-418-14)     "service_host": "rdaflogstream", [](#__codelineno-418-15)     "hostname": "rdaflogstream", [](#__codelineno-418-16)     "received_from": "10.95.101.175", [](#__codelineno-418-17)     "log": "2022-12-07T20:23:05.275427+00:00 rdaflogstream systemd-networkd[1110]: veth7809965: Gained IPv6LL", [](#__codelineno-418-18)     "log_severity": "UNKNOWN", [](#__codelineno-418-19)     "service_name": "rda_os_syslog", [](#__codelineno-418-20)     "@timestamp": "2022-12-07T20:23:05.275Z", [](#__codelineno-418-21)     "@version": "1", [](#__codelineno-418-22)     "fluentbit_timestamp": "2022-12-07T20:23:05.275Z", [](#__codelineno-418-23)     "process_id": "1110" [](#__codelineno-418-24)   } [](#__codelineno-418-25) ]`\
\
Below is another example of CFXQL query when the column name `service-category` has a special character.\
\
``[](#__codelineno-419-1) rdac pstream query --name rdaf_services_logs --json --query '"\`@timestamp\`" is after -5min and "\`service-category\`" = "rda_infra_svcs"' --max_rows 1``\
\
Tip\
\
When using CFXQL, column names that has special characters such as `@` `-`, need to be escaped as shown in the above examples.\
\
Below is another example of **aggs & groupby** arguments when the column name is `service_name`.\
\
``[](#__codelineno-420-1) rdac pstream query --name rdaf_services_logs --ts @timestamp --query '"\`@timestamp\`" is after -1d and log_severity = 'ERROR' get service_name,log' --aggs value_count:_id --groupby service_name``\
\
Example Output Three\
\
`[](#__codelineno-421-1) Detected OS Name: Linux [](#__codelineno-421-2) Detected docker version: 20.10.12 [](#__codelineno-421-3)  Series [](#__codelineno-421-4)    * Label: _id_value_count [](#__codelineno-421-5)      Values [](#__codelineno-421-6)        * Value: 39,918 [](#__codelineno-421-7) [](#__codelineno-421-8)      Group: rda_nats [](#__codelineno-421-9) [](#__codelineno-421-10)    * Label: _id_value_count [](#__codelineno-421-11)      Values [](#__codelineno-421-12)        * Value: 5,412 [](#__codelineno-421-13) [](#__codelineno-421-14)      Group: rda_scheduler [](#__codelineno-421-15) [](#__codelineno-421-16)    * Label: _id_value_count [](#__codelineno-421-17)      Values [](#__codelineno-421-18)        * Value: 72 [](#__codelineno-421-19) [](#__codelineno-421-20)      Group: rda_file_browser [](#__codelineno-421-21) [](#__codelineno-421-22)    * Label: _id_value_count [](#__codelineno-421-23)      Values [](#__codelineno-421-24)        * Value: 48 [](#__codelineno-421-25) [](#__codelineno-421-26)      Group: rda_resource_manager`\
\
Below is another example of **sum aggregation** of the column name `duration`.\
\
`[](#__codelineno-422-1) python3 rdac.py pstream query --name rda_microservice_traces --aggs sum:duration --groupby source --order asc`\
\
Example Output Four\
\
`[](#__codelineno-423-1) Detected OS Name: Linux [](#__codelineno-423-2) Detected docker version: 20.10.12 [](#__codelineno-423-3)  Series [](#__codelineno-423-4)    * Label: duration_sum [](#__codelineno-423-5)      Values [](#__codelineno-423-6)        * Value: 270,762.0 [](#__codelineno-423-7) [](#__codelineno-423-8)      Group: scheduler [](#__codelineno-423-9) [](#__codelineno-423-10)    * Label: duration_sum [](#__codelineno-423-11)      Values [](#__codelineno-423-12)        * Value: 166,608.0 [](#__codelineno-423-13) [](#__codelineno-423-14)      Group: dataset-caas [](#__codelineno-423-15) [](#__codelineno-423-16)    * Label: duration_sum [](#__codelineno-423-17)      Values [](#__codelineno-423-18)        * Value: 44,937.0 [](#__codelineno-423-19) [](#__codelineno-423-20)      Group: api-server [](#__codelineno-423-21) [](#__codelineno-423-22)    * Label: duration_sum [](#__codelineno-423-23)      Values [](#__codelineno-423-24)        * Value: 81,265.0 [](#__codelineno-423-25) [](#__codelineno-423-26)      Group: cfxdimensions-app-file-browser`\
\
Below is another example of **value count** aggregation of the column name `Maths`.\
\
`[](#__codelineno-424-1) rdac pstream query --name sample-test-scores --aggs 'value_count:Maths' --groupby section`\
\
Example Output Five\
\
`[](#__codelineno-425-1) Series [](#__codelineno-425-2)    * Label: Maths_value_count [](#__codelineno-425-3)      Values [](#__codelineno-425-4)        * Value: 5 [](#__codelineno-425-5) [](#__codelineno-425-6)      Group: A [](#__codelineno-425-7) [](#__codelineno-425-8)    * Label: Maths_value_count [](#__codelineno-425-9)      Values [](#__codelineno-425-10)        * Value: 5 [](#__codelineno-425-11) [](#__codelineno-425-12)      Group: B`\
\
Below is another example of **cardinality** aggregation of the column name `Maths`.\
\
`[](#__codelineno-426-1) rdac pstream query --name sample-test-scores --aggs 'cardinality:Maths' --groupby section`\
\
Example Output Six\
\
`[](#__codelineno-427-1) Series [](#__codelineno-427-2)    * Label: Maths_cardinality [](#__codelineno-427-3)      Values [](#__codelineno-427-4)        * Value: 5 [](#__codelineno-427-5) [](#__codelineno-427-6)      Group: A [](#__codelineno-427-7) [](#__codelineno-427-8)    * Label: Maths_cardinality [](#__codelineno-427-9)      Values [](#__codelineno-427-10)        * Value: 4 [](#__codelineno-427-11) [](#__codelineno-427-12)      Group: B`\
\
Below is another example of **avg** aggregation of the column name `Maths`.\
\
`[](#__codelineno-428-1) rdac pstream query --name sample-test-scores --aggs 'avg:Maths' --groupby section`\
\
Example Output Seven\
\
`[](#__codelineno-429-1) Series [](#__codelineno-429-2)    * Label: Maths_avg [](#__codelineno-429-3)      Values [](#__codelineno-429-4)        * Value: 57.6 [](#__codelineno-429-5) [](#__codelineno-429-6)      Group: A [](#__codelineno-429-7) [](#__codelineno-429-8)    * Label: Maths_avg [](#__codelineno-429-9)      Values [](#__codelineno-429-10)        * Value: 77.8 [](#__codelineno-429-11) [](#__codelineno-429-12)      Group: B`\
\
Below is another example of **max** aggregation of the column name `Maths`.\
\
`[](#__codelineno-430-1) rdac pstream query --name sample-test-scores --aggs 'max:Maths' --groupby section`\
\
Example Output Eight\
\
`[](#__codelineno-431-1) Series [](#__codelineno-431-2)    * Label: Maths_max [](#__codelineno-431-3)      Values [](#__codelineno-431-4)        * Value: 87.0 [](#__codelineno-431-5) [](#__codelineno-431-6)      Group: A [](#__codelineno-431-7) [](#__codelineno-431-8)    * Label: Maths_max [](#__codelineno-431-9)      Values [](#__codelineno-431-10)        * Value: 90.0 [](#__codelineno-431-11) [](#__codelineno-431-12)      Group: B`\
\
****Sub Command: `delete-by-query`****\
\
Description: Delete persistent stream data via CFXQL query\
\
`[](#__codelineno-432-1) rdac pstream delete-by-query -h`\
\
`[](#__codelineno-433-1) usage: pstream [-h] --name NAME --query CFXQL_QUERY [--timeout TIMEOUT] [](#__codelineno-433-2) [](#__codelineno-433-3) optional arguments: [](#__codelineno-433-4)   -h, --help           show this help message and exit [](#__codelineno-433-5)   --name NAME          Persistent Stream name [](#__codelineno-433-6)   --query CFXQL_QUERY  CFXQL Query [](#__codelineno-433-7)   --timeout TIMEOUT    Timeout in seconds to wait for response. Default 60`\
\
*   Following is the syntax for **pstream delete-by-query**\
\
`[](#__codelineno-434-1) rdac pstream delete-by-query --name rda_logs_test --query 'artifact_name  is "login_post" and operation = "LOGIN"'`\
\
Example Output\
\
`[](#__codelineno-435-1) Deleted all the data that matched the query [](#__codelineno-435-2) {'status': 'ok', 'reason': '', 'data': {'took': 14, 'timed_out': False, 'total': 4, 'deleted': 4, 'batches': 1, 'version_conflicts': 0, 'noops': 0, 'retries': {'bulk': 0, 'search': 0}, 'throttled_millis': 0, 'requests_per_second': -1.0, 'throttled_until_millis': 0}, 'now': '2023-11-09T08:23:39.800946'}`\
\
Warning\
\
`pstream delete-by-query` deletes the records from persistent stream, please make sure the given CFXQL query is appropriate to filter and delete the intended records. As a pre-caution, use `pstream query` with CFXQL filter to validate the query results before running `pstream delete-by-query` command.\
\
****Sub Command: `update-by-query`****\
\
Description: Update column(s) in persistent stream data via CFXQL query\
\
`[](#__codelineno-436-1) rdac pstream update-by-query -h`\
\
`[](#__codelineno-437-1) usage: pstream [-h] --name NAME --query CFXQL_QUERY --columns COLUMNS --values [](#__codelineno-437-2)                VALUES [--timeout TIMEOUT] [](#__codelineno-437-3) [](#__codelineno-437-4) optional arguments: [](#__codelineno-437-5)   -h, --help           show this help message and exit [](#__codelineno-437-6)   --name NAME          Persistent Stream name [](#__codelineno-437-7)   --query CFXQL_QUERY  CFXQL Query [](#__codelineno-437-8)   --columns COLUMNS    Comma separated list of column names that needs to be [](#__codelineno-437-9)                        updated for all the records that match the query. [](#__codelineno-437-10)                        Example: city,state,zipcode [](#__codelineno-437-11)   --values VALUES      Set the value to specified column or columns (comma [](#__codelineno-437-12)                        separated). The specified number of columns should [](#__codelineno-437-13)                        match 'columns' column(s). Example: San Jose,CA,12345 [](#__codelineno-437-14)   --timeout TIMEOUT    Timeout in seconds to wait for response. Default 60`\
\
*   Following is the syntax for **pstream update-by-query**\
\
`[](#__codelineno-438-1) rdac pstream update-by-query --name rda_logs_test --query 'artifact_name  is "login_post"' --columns artifact_name --values 'login_test1'`\
\
Example Output One\
\
`[](#__codelineno-439-1) Updated all the data that matched the query [](#__codelineno-439-2) {'status': 'ok', 'reason': '', 'data': {'took': 578, 'timed_out': False, 'total': 2, 'updated': 2, 'deleted': 0, 'batches': 1, 'version_conflicts': 0, 'noops': 0, 'retries': {'bulk': 0, 'search': 0}, 'throttled_millis': 0, 'requests_per_second': -1.0, 'throttled_until_millis': 0, 'failures': []}, 'now': '2023-11-09T08:38:54.026199'}`\
\
\* Following is the syntax for **pstream update-by-query with multiple `columns`**\
\
`[](#__codelineno-440-1) rdac pstream update-by-query --name sample-test-scores --query 'name  is "tej"' --columns "Maths,english" --values "85,54"`\
\
example Output Two\
\
`[](#__codelineno-441-1) Updated all the data that matched the query [](#__codelineno-441-2) {'status': 'ok', 'reason': '', 'data': {'took': 22, 'timed_out': False, 'total': 1, 'updated': 1, 'deleted': 0, 'batches': 1, 'version_conflicts': 0, 'noops': 0, 'retries': {'bulk': 0, 'search': 0}, 'throttled_millis': 0, 'requests_per_second': -1.0, 'throttled_until_millis': 0, 'failures': []}, 'now': '2023-11-20T05:54:21.625365'}`\
\
****Sub Command: `add-column`****\
\
Description: Add column to the persistent stream records that don't have it and set a value via expression\
\
`[](#__codelineno-442-1) rdac pstream add-column -h`\
\
`[](#__codelineno-443-1) usage: pstream [-h] --name NAME --column COLUMN --expression EXPRESSION [](#__codelineno-443-2) [](#__codelineno-443-3) optional arguments: [](#__codelineno-443-4)   -h, --help            show this help message and exit [](#__codelineno-443-5)   --name NAME           Persistent Stream name [](#__codelineno-443-6)   --column COLUMN       Field name. Example: full_name [](#__codelineno-443-7)   --expression EXPRESSION [](#__codelineno-443-8)                         Open Search painless script. Example: [](#__codelineno-443-9)                         "ctx._source['first_name'] + ' ' + [](#__codelineno-443-10)                         ctx._source['last_name']"`\
\
*   Following is the syntax for **pstream add-column**\
\
Run `rdac` command without arguments to enter into **rdac** command shell and followed by `pstream add-column` command as shown below.\
\
`[](#__codelineno-444-1) rdac` \
\
`[](#__codelineno-445-1) pstream add-column --name rda_logs_test --column artifact add --expression "ctx._source['artifact_type'] + ' ' + ctx._source['artifact_name']"`\
\
Example Output\
\
`[](#__codelineno-446-1) Added column 'artifactadd' for all the records that don't have it [](#__codelineno-446-2) {'status': 'ok', 'reason': '', 'data': {'took': 111, 'timed_out': False, 'total': 33, 'updated': 33, 'deleted': 0, 'batches': 1, 'version_conflicts': 0, 'noops': 0, 'retries': {'bulk': 0, 'search': 0}, 'throttled_millis': 0, 'requests_per_second': -1.0, 'throttled_until_millis': 0, 'failures': []}, 'now': '2023-11-09T10:59:28.158594'}`\
\
Note\
\
When adding a new column using the `--expression` option, it uses Opensearch painless scripted language which will have special characters. To prevent issues with these special characters, it is recommended to execute this command within the `rdac` shell.\
\
****Sub Command: `tail`****\
\
Description : Query a persistent stream and continue to query for incremental data every few seconds\
\
`[](#__codelineno-447-1) rdac pstream tail --help`\
\
`[](#__codelineno-448-1) usage: pstream [-h] --name NAME [--max_rows MAX_ROWS] [--query CFXQL_QUERY] [](#__codelineno-448-2)                [--ts TS_COLUMN] [--format FORMAT] [--out_cols OUTPUT_COLUMNS] [](#__codelineno-448-3)                [--json] [](#__codelineno-448-4) [](#__codelineno-448-5) optional arguments: [](#__codelineno-448-6)   -h, --help            show this help message and exit [](#__codelineno-448-7)   --name NAME           Persistent Stream name [](#__codelineno-448-8)   --max_rows MAX_ROWS   Max rows in output for initial query [](#__codelineno-448-9)   --query CFXQL_QUERY   CFXQL Query [](#__codelineno-448-10)   --ts TS_COLUMN        Timestamp column for sorting. Default is 'timestamp' [](#__codelineno-448-11)   --format FORMAT       Format string in {field1:<8} {field2:,.2f} style [](#__codelineno-448-12)   --out_cols OUTPUT_COLUMNS [](#__codelineno-448-13)                         Comma separated list of column names to be included in [](#__codelineno-448-14)                         output. If not specified, all columns will be included [](#__codelineno-448-15)   --json                Print detailed information in JSON format instead of [](#__codelineno-448-16)                         tabular format`\
\
`--query` supports CFXQL query. However it doesn't support `get` columns option.\
\
`--out_cols` use this option to get specific attributes from the pstream as shown in the above example.\
\
`--json` use this option to get the log output in JSON format. However, it doesn't support limiting the selective attributes listed under `--out_cols` option.\
\
*   Following is the syntax for **pstream tail**\
\
`[](#__codelineno-449-1) rdac pstream tail --name rda_synthetic_metrics`\
\
Example Output\
\
`[](#__codelineno-450-1) Detected OS Name: Linux [](#__codelineno-450-2) Detected docker version: 20.10.12 [](#__codelineno-450-3) 7 3hSAeYQBuQsspbunzGjR 1 Application Component app_vm_mem_usage 10.95.134.101_Webserver fin-web01 Webserver AppDynamics Online_Banking_Stack 2022-11-15T04:05:13.584582 % 60.48 [](#__codelineno-450-4) 8 3xSAeYQBuQsspbunzGjR 1 Application Component total_response_time 10.95.134.101_Webserver fin-web01 Webserver ThousandEyes Online_Banking_Stack 2022-11-15T04:05:13.584582 ms 65.72 [](#__codelineno-450-5) 9 4BSAeYQBuQsspbunzGjR 1 Application Component app_vm_cpu_usage 10.95.134.101_Webserver fin-web01 Webserver AppDynamics Online_Banking_Stack 2022-11-15T04:05:13.584582 % 69.24 [](#__codelineno-450-6) 4 2xSAeYQBuQsspbunzGjR 1 Application Component total_response_time 10.95.134.101_Webserver fin-web01 Webserver ThousandEyes Online_Banking_Stack 2022-11-15T04:05:13.921674 ms 29.11 [](#__codelineno-450-7) 5 3BSAeYQBuQsspbunzGjR 1 Application Component app_vm_cpu_usage 10.95.134.101_Webserver fin-web01 Webserver AppDynamics Online_Banking_Stack 2022-11-15T04:05:13.921674 % 69.28 [](#__codelineno-450-8) 6 3RSAeYQBuQsspbunzGjR 1 Application Component app_vm_mem_usage 10.95.134.101_Webserver fin-web01 Webserver AppDynamics Online_Banking_Stack 2022-11-15T04:05:13.921674 % 60.75 [](#__codelineno-450-9) 3 2hSAeYQBuQsspbunzGjR 1 Shared Service shared_svc_total_response_time app.okta.com app.okta.com IdentityProvider ThousandEyes Online_Banking_Stack 2022-11-15T04:05:16.339953 ms 50.31 [](#__codelineno-450-10) 2 2RSAeYQBuQsspbunzGjR 1 Application Component transaction_time 10.95.134.102_Appserver fin-app01 Appserver AppDynamics Online_Banking_Stack 2022-11-15T04:05:18.318154 ms 4.35 [](#__codelineno-450-11) 0 1xSAeYQBuQsspbunzGjR 1 Host host_cpu_usage 10.95.158.194_esxi esxi-server-04 EsxiHost VROps Online_Banking_Stack 2022-11-15T04:05:23.190271 % 78.13 [](#__codelineno-450-12) 1 2BSAeYQBuQsspbunzGjR 1 Host host_mem_usage 10.95.158.194_esxi esxi-server-04 EsxiHost VROps Online_Banking_Stack 2022-11-15T04:05:23.190271 % 69.05`\
\
*   Below is an example of `pstream tail` with CFXQL query to filter and tail selected output column(s) specified with `--out_cols`\
\
`[](#__codelineno-451-1) rdac pstream tail --name rdaf_services_logs --ts @timestamp --query "service_name = 'rda_registry'" --out_cols 'log'`\
\
Example Output\
\
`[](#__codelineno-452-1) 2022-12-07:20:50:53 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-452-2) 2022-12-07 20:50:51,245 [PID=9:TID=Thread-9:cfx.rda_messaging.nats_client:cb:1021] INFO - Sending request-reply to _INBOX.RZtDMglua05ndrDR200bGx.RZtDMglua05ndrDR200bJ8 [](#__codelineno-452-3) [](#__codelineno-452-4) 2022-12-07 20:50:51,274 [PID=9:TID=Thread-10:cfx.rda_registry.registry_main:registry_requests:501] INFO - received registry request on subject tenants.79cc72a1697b487fb2da7b99f0a0cc1a.registry.auto: get-pods [](#__codelineno-452-5) [](#__codelineno-452-6) 2022-12-07 20:50:51,274 [PID=9:TID=Thread-10:cfx.rda_registry.registry_main:registry_requests:546] INFO - Returning 1 pods [](#__codelineno-452-7) [](#__codelineno-452-8) 2022-12-07 20:50:51,275 [PID=9:TID=Thread-10:cfx.rda_messaging.nats_client:cb:1021] INFO - Sending request-reply to _INBOX.AeVKdrtKiJGJtMSKQEfui2.AeVKdrtKiJGJtMSKQEfukt [](#__codelineno-452-9) ... [](#__codelineno-452-10) ...`\
\
Tip\
\
When using CFXQL, column names that has special characters such as `@` `-`, need to be escaped. Please refer `pstream query` section for reference examples.\
\
****Sub Command: `export`****\
\
Description : Query a persistent stream and export data to CSV or JSON file\
\
`[](#__codelineno-453-1) rdac pstream export --help`\
\
`[](#__codelineno-454-1) usage: pstream [-h] --name NAME [--max_rows MAX_ROWS] [--limit LIMIT] [](#__codelineno-454-2)                [--query CFXQL_QUERY] [--ts TS_COLUMN] --to_file TO_FILE [](#__codelineno-454-3) [](#__codelineno-454-4) optional arguments: [](#__codelineno-454-5)   -h, --help           show this help message and exit [](#__codelineno-454-6)   --name NAME          Persistent Stream name [](#__codelineno-454-7)   --max_rows MAX_ROWS  Max rows in each batch [](#__codelineno-454-8)   --limit LIMIT        Total limit on downloaded rows [](#__codelineno-454-9)   --query CFXQL_QUERY  CFXQL Query [](#__codelineno-454-10)   --ts TS_COLUMN       Timestamp column for sorting. Default is 'timestamp' [](#__codelineno-454-11)   --to_file TO_FILE    Output filename (CSV or JSON)`\
\
*   Following is the syntax for **pstream export**\
\
`[](#__codelineno-455-1) rdac pstream export --name oia-alerts-stream --max_rows 100 --limit 100 --query "a_status is ACTIVE" --to_file ./test.csv`\
\
Example Output\
\
`[](#__codelineno-456-1) Detected OS Name: Linux [](#__codelineno-456-2) Detected docker version: 20.10.12 [](#__codelineno-456-3) Fetching offset 0, totalResults=?, limit=100 [](#__codelineno-456-4) Completed download of 100 rows`\
\
****Sub Command: `export-chunks`****\
\
Description: Query a persistent stream and export data as minio chunks\
\
`[](#__codelineno-457-1) rdac pstream export-chunks --help`\
\
`[](#__codelineno-458-1) usage: pstream [-h] --name NAME [--query CFXQL_QUERY] [--limit LIMIT] [](#__codelineno-458-2)                [--ts TS_COLUMN] [](#__codelineno-458-3) [](#__codelineno-458-4) optional arguments: [](#__codelineno-458-5)   -h, --help           show this help message and exit [](#__codelineno-458-6)   --name NAME          Persistent Stream name [](#__codelineno-458-7)   --query CFXQL_QUERY  CFXQL Query [](#__codelineno-458-8)   --limit LIMIT        Total limit exported rows [](#__codelineno-458-9)   --ts TS_COLUMN       Timestamp column for sorting. Default is 'timestamp'`\
\
\* Following is the syntax for **pstream export-chunks**\
\
`[](#__codelineno-459-1) rdac pstream export-chunks --name "rda_logs_test" --q` \
\
Example Output\
\
`[](#__codelineno-460-1) "timestamp is after -2 days" [](#__codelineno-460-2) Check 'rda_system_collector_export_job_status' stream for updates for export job: rda_logs_test-6ebeeb88 [](#__codelineno-460-3) Exiting out of LogRecordSocketReceiver. pid: 1. Socket file: /tmp/rdf_log_socket_2bef0dfa-8c71-466a-a592-25d33326b8c7`\
\
****Sub Command: `migrate`****\
\
Description : Query a persistent stream and export to another stream with optional type conversion\
\
`[](#__codelineno-461-1) rdac pstream migrate --help`\
\
`[](#__codelineno-462-1) usage: pstream [-h] --name NAME [--max_rows MAX_ROWS] [--limit LIMIT] [](#__codelineno-462-2)                [--query CFXQL_QUERY] [--ts TS_COLUMN] --dest_stream [](#__codelineno-462-3)                DEST_STREAM [--to_int TO_INT] [--to_float TO_FLOAT] [](#__codelineno-462-4)                [--to_text TO_TEXT] [](#__codelineno-462-5) [](#__codelineno-462-6) optional arguments: [](#__codelineno-462-7)   -h, --help            show this help message and exit [](#__codelineno-462-8)   --name NAME           Persistent Stream name [](#__codelineno-462-9)   --max_rows MAX_ROWS   Max rows in each batch [](#__codelineno-462-10)   --limit LIMIT         Total limit on downloaded rows [](#__codelineno-462-11)   --query CFXQL_QUERY   CFXQL Query [](#__codelineno-462-12)   --ts TS_COLUMN        Timestamp column for sorting. Default is 'timestamp' [](#__codelineno-462-13)   --dest_stream DEST_STREAM [](#__codelineno-462-14)                         Output PStream name [](#__codelineno-462-15)   --to_int TO_INT       Comma separated list of columns to be converted to int [](#__codelineno-462-16)   --to_float TO_FLOAT   Comma separated list of columns to be converted to [](#__codelineno-462-17)                         float [](#__codelineno-462-18)   --to_text TO_TEXT     Comma separated list of columns to be converted to`\
\
*   Following is the syntax for **pstream migrate**\
\
`[](#__codelineno-463-1) rdac pstream migrate --name oia-incidents-stream --max_rows 100 --limit 100 --dest_stream test_pstream --to_int i_ttr_millis`\
\
Example Output\
\
`[](#__codelineno-464-1) Detected OS Name: Linux [](#__codelineno-464-2) Detected docker version: 20.10.12 [](#__codelineno-464-3) Fetching offset 0, totalResults=?, limit=100 [](#__codelineno-464-4) Completed migration of 100 rows, with 0 mapping errors`\
\
****Sub Command: `load`****\
\
Description : Load data from a CSV file into a persistent stream with optional type conversion\
\
`[](#__codelineno-465-1) rdac pstream load --help`\
\
`[](#__codelineno-466-1) usage: pstream [-h] --name NAME --data DATA_FILE [--limit LIMIT] [](#__codelineno-466-2)                [--filter CFXQL_QUERY] [--to_ts TO_TS] [--timestamp TIMESTAMP] [](#__codelineno-466-3)                [--to_int TO_INT] [--to_float TO_FLOAT] [--to_text TO_TEXT] [](#__codelineno-466-4) [](#__codelineno-466-5) optional arguments: [](#__codelineno-466-6)   -h, --help            show this help message and exit [](#__codelineno-466-7)   --name NAME           Destination Persistent Stream name [](#__codelineno-466-8)   --data DATA_FILE      Input data file (CSV) [](#__codelineno-466-9)   --limit LIMIT         Total limit on published rows [](#__codelineno-466-10)   --filter CFXQL_QUERY  CFXQL Query to apply on loaded dataframe before [](#__codelineno-466-11)                         publishing [](#__codelineno-466-12)   --to_ts TO_TS         Comma separated list of timestamp columns (ISO format) [](#__codelineno-466-13)   --timestamp TIMESTAMP [](#__codelineno-466-14)                         Create Timestamp column from a an existing column [](#__codelineno-466-15)   --to_int TO_INT       Comma separated list of columns to be converted to int [](#__codelineno-466-16)   --to_float TO_FLOAT   Comma separated list of columns to be converted to [](#__codelineno-466-17)                         float [](#__codelineno-466-18)   --to_text TO_TEXT     Comma separated list of columns to be converted to [](#__codelineno-466-19)                         text`\
\
*   Following is the syntax for **pstream load**\
\
`[](#__codelineno-467-1) rdac pstream load --name rda_synthetic_metrics --data time_series_data_test.csv`\
\
Example Output\
\
`[](#__codelineno-468-1) Detected OS Name: Linux [](#__codelineno-468-2) Detected docker version: 20.10.12 [](#__codelineno-468-3) Reading input data file... [](#__codelineno-468-4) Input data file has 12 Rows and 9 Columns [](#__codelineno-468-5) Publishing 12 rows.. [](#__codelineno-468-6) Completed loading of 12 rows into stream rda_synthetic_metrics in 0.3 seconds`\
\
****Sub Command: `ingest`****\
\
Description : Ingest data to pstream by directly adding data to Open Search\
\
`[](#__codelineno-469-1) rdac pstream ingest --help`\
\
`[](#__codelineno-470-1) usage: pstream [-h] --name NAME [--minio_object_prefix MINIO_OBJECT_PREFIX] [](#__codelineno-470-2)                [--local_directory LOCAL_DIRECTORY] [](#__codelineno-470-3)                [--filename_pattern FILENAME_PATTERN] [--dataset DATASET] [](#__codelineno-470-4)                [--num_rows NUM_ROWS] [--replace] [](#__codelineno-470-5) [](#__codelineno-470-6) optional arguments: [](#__codelineno-470-7)   -h, --help            show this help message and exit [](#__codelineno-470-8)   --name NAME           Destination Persistent Stream name [](#__codelineno-470-9)   --minio_object_prefix MINIO_OBJECT_PREFIX [](#__codelineno-470-10)                         Platform's minio object prefix. Example: /data/ [](#__codelineno-470-11)   --local_directory LOCAL_DIRECTORY [](#__codelineno-470-12)                         Local directory of input file. [](#__codelineno-470-13)   --filename_pattern FILENAME_PATTERN [](#__codelineno-470-14)                         File criteria in regex format. Only files with csv [](#__codelineno-470-15)                         extension (or csv file compressesd as .gz file) are [](#__codelineno-470-16)                         supported. Applicable if 'minio_object_prefix' or [](#__codelineno-470-17)                         'local_directory' is provided [](#__codelineno-470-18)   --dataset DATASET     Dataset name [](#__codelineno-470-19)   --num_rows NUM_ROWS   Number of rows to fetch in each chunk [](#__codelineno-470-20)   --replace             Delete any existing data in the index and load new [](#__codelineno-470-21)                         data`\
\
*   Following is the syntax for **pstream ingest**\
\
`[](#__codelineno-471-1) rdac pstream ingest --name test_pstream --filename_pattern csv --dataset time_series_data_test --num_rows 100 --replace`\
\
Example Output One\
\
`[](#__codelineno-472-1) Detected OS Name: Linux [](#__codelineno-472-2) Detected docker version: 20.10.12 [](#__codelineno-472-3) Check 'rda_system_collector_ingestion_job_status' stream for updates for ingestion job: test_pstream-2115d970`\
\
*   Following is the syntax for **pstream ingest --minio\_object\_prefix**\
\
`[](#__codelineno-473-1) rdac pstream ingest --name demo-test --filename_pattern csv --dataset sample-test-scores --minio_object_prefix cfxdm-saved-data`\
\
\=== Example Output Two\
\
`[](#__codelineno-474-1) Check 'rda_system_collector_ingestion_job_status' stream for updates for ingestion job: demo-test-3824eb70`\
\
****Sub Command: `evict`****\
\
Description : Evict Ingestion Job\
\
`[](#__codelineno-475-1) usage: pstream [-h] --name NAME [](#__codelineno-475-2) [](#__codelineno-475-3) optional arguments: [](#__codelineno-475-4)   -h, --help   show this help message and exit [](#__codelineno-475-5)   --name NAME  Ingestion Job name`\
\
Note\
\
`evict` command will work only when the ingest job status is **Ingesting**. Ingestion job status is captured in **rda\_system\_collector\_ingestion\_job\_status** persistent stream.\
\
*   Following is the syntax to check **pstream ingestion status**\
\
`[](#__codelineno-476-1) rdac.py pstream query --name <ingestion status pstream name>`\
\
Example Syntax\
\
`[](#__codelineno-477-1) rdac pstream query --name rda_system_collector_ingestion_job_status`\
\
Example Output\
\
`[](#__codelineno-478-1) Detected OS Name: Linux [](#__codelineno-478-2) Detected docker version: 20.10.12 [](#__codelineno-478-3)       count_  dataset                ingest_job_name                   row_count  status     stream                 timestamp [](#__codelineno-478-4) --  --------  ---------------------  ------------------------------  -----------  ---------  ---------------------  -------------------------- [](#__codelineno-478-5)  0         1  rda_synthetic_metrics  test_pstream-9721ebd0                 78900  Ingesting  test_pstream           2022-12-07T05:45:18.348868 [](#__codelineno-478-6)  1         1  rda_synthetic_metrics  test_pstream-618b8063                100000  Done       test_pstream           2022-12-07T05:06:56.391054 [](#__codelineno-478-7)  2         1  rda_synthetic_metrics  test_pstream-becb20a7                100000  Done       test_pstream           2022-12-06T15:03:04.692909 [](#__codelineno-478-8)  3         1  rda_synthetic_metrics  test_pstream-60b98c94                100000  Done       test_pstream           2022-12-06T14:32:52.728035`\
\
Note\
\
To evict the pstream ingestion job (when the status is **Ingesting** ) run the `evict` command to terminate the ingestion job\
\
*   Following is the syntax for **pstream evict**\
\
`[](#__codelineno-479-1) rdac pstream evict --name <ingest job name>`\
\
Example Syntax\
\
`[](#__codelineno-480-1) rdac.py pstream evict --name test_pstream-9721ebd0`\
\
Example Output\
\
`[](#__codelineno-481-1) Detected OS Name: Linux [](#__codelineno-481-2) Detected docker version: 20.10.12 [](#__codelineno-481-3) Job Evicted Successfully`\
\
****Sub Command: `evict-export`****\
\
Description: Evict Export Chunks Job\
\
`[](#__codelineno-482-1) rdac pstream evict-export --help`\
\
`[](#__codelineno-483-1) optional arguments: [](#__codelineno-483-2)   -h, --help   show this help message and exit [](#__codelineno-483-3)   --name NAME  Export Chunk Job name`\
\
*   Following is the syntax for **pstream evict-export**\
\
`[](#__codelineno-484-1) rdac pstream evict-export --name epss_test_logs-bb1c56ea`\
\
Example Output\
\
`[](#__codelineno-485-1) Job Evicted Successfully`\
\
### Sub Command: `purge-outputs`\
\
Description: Purge outputs of completed jobs\
\
`[](#__codelineno-486-1) Usage: purge-outputs  [-h] --hours OLDER_THAN_HOURS [](#__codelineno-486-2) [](#__codelineno-486-3) optional arguments: [](#__codelineno-486-4)   -h, --help            show this help message and exit [](#__codelineno-486-5)   --hours OLDER_THAN_HOURS [](#__codelineno-486-6)                         Purge jobs older than specified number of hours. Must [](#__codelineno-486-7)                         be >= 1`\
\
### Sub Command: `read-stream`\
\
Description: Read messages from an RDA stream\
\
`[](#__codelineno-487-1) Usage: read-stream  [-h] --name STREAM_NAME [--group GROUP] [--delay DELAY] [](#__codelineno-487-2)             [--show_rate] [](#__codelineno-487-3) [](#__codelineno-487-4) optional arguments: [](#__codelineno-487-5)   -h, --help          show this help message and exit [](#__codelineno-487-6)   --name STREAM_NAME  Stream name to read from [](#__codelineno-487-7)   --group GROUP       Message consumer group name [](#__codelineno-487-8)   --delay DELAY       Simulate processing delay between each read message [](#__codelineno-487-9)   --show_rate         Do not print messages, just show rate per minute and [](#__codelineno-487-10)                       counts`\
\
### Sub Command: `run`\
\
Description: Run a pipeline on a worker pod\
\
`[](#__codelineno-488-1) Usage: run  [-h] --pipeline PIPELINE [--nowait] [--log LOGLEVEL] [](#__codelineno-488-2)             [--group WORKER_GROUP] [--site WORKER_SITE] [](#__codelineno-488-3)             [--lfilter LABEL_FILTER] [--rfilter RESOURCE_FILTER] [--dryrun] [](#__codelineno-488-4)             [--save_jobid SAVE_JOBID] [](#__codelineno-488-5) [](#__codelineno-488-6) optional arguments: [](#__codelineno-488-7)   -h, --help            show this help message and exit [](#__codelineno-488-8)   --pipeline PIPELINE   File containing pipeline information in JSON format [](#__codelineno-488-9)   --nowait              If specified, command does not wait for the completion [](#__codelineno-488-10)                         of the pipeline [](#__codelineno-488-11)   --log LOGLEVEL        Specify logging level as none, [](#__codelineno-488-12)                         DEBUG,INFO,WARNING,ERROR,CRITICAL [](#__codelineno-488-13)   --group WORKER_GROUP  Deprecated. Use --site option. Specify a worker site [](#__codelineno-488-14)                         name. If not specified, will use any available worker. [](#__codelineno-488-15)   --site WORKER_SITE    Specify a worker site name. If not specified, will use [](#__codelineno-488-16)                         any available worker. [](#__codelineno-488-17)   --lfilter LABEL_FILTER [](#__codelineno-488-18)                         CFXQL style query to narrow down workers using their [](#__codelineno-488-19)                         labels [](#__codelineno-488-20)   --rfilter RESOURCE_FILTER [](#__codelineno-488-21)                         CFXQL style query to narrow down workers using their [](#__codelineno-488-22)                         resources [](#__codelineno-488-23)   --dryrun              Do not run pipeline but show which worker nodes would [](#__codelineno-488-24)                         have been selected for run [](#__codelineno-488-25)   --save_jobid SAVE_JOBID [](#__codelineno-488-26)                         Save the jobid to a specified file`\
\
### Sub Command: `run-get-output`\
\
Description: Run a pipeline on a worker, wait for the completion, get the final output\
\
`[](#__codelineno-489-1) Usage: run-get-output  [-h] [--config CONFIG] [--site SITE] [--pipeline PIPELINE] [](#__codelineno-489-2)             [--max_rows MAX_ROWS] [--md] [--onerow] [--vault] [--tocsv TO_CSV] [](#__codelineno-489-3) [](#__codelineno-489-4) optional arguments: [](#__codelineno-489-5)   -h, --help           show this help message and exit [](#__codelineno-489-6)   --config CONFIG      Additional configurations defined in a YAML or JSON [](#__codelineno-489-7)                        file [](#__codelineno-489-8)   --site SITE          Site name regex [](#__codelineno-489-9)   --pipeline PIPELINE  Plain text Pipeline filename. If not specified, will [](#__codelineno-489-10)                        read from STDIN. [](#__codelineno-489-11)   --max_rows MAX_ROWS  Max rows to print on screen. [](#__codelineno-489-12)   --md                 Print in markdown format on screen instead of text [](#__codelineno-489-13)                        table format [](#__codelineno-489-14)   --onerow             Print fist row in a vertical format (in addition to [](#__codelineno-489-15)                        table) [](#__codelineno-489-16)   --vault              Use RDA Vault for credentials if not specified locally [](#__codelineno-489-17)                        in a JSON file [](#__codelineno-489-18)   --tocsv TO_CSV       Save the output to CSV formatted file`\
\
### Sub Command: `schedule-add`\
\
Description: Add a new schedule for pipeline execution\
\
`[](#__codelineno-490-1) Usage: schedule-add  [-h] --pipeline PIPELINE [--log LOGLEVEL] --name SCHEDULENAME [](#__codelineno-490-2)             --type SCHEDULE_TYPE [--startdate STARTDATE] [](#__codelineno-490-3)             [--starttime STARTTIME] [--enddate ENDDATE] [--weekdays WEEKDAYS] [](#__codelineno-490-4)             [--freq FREQUENCY] [--tz TIMEZONE] --group GROUP [](#__codelineno-490-5)             [--retries RETRIES] [--retry-intervals RETRYINTERVALS] [](#__codelineno-490-6)             [--parallel-instances PARALLELINSTANCES] [](#__codelineno-490-7) [](#__codelineno-490-8) optional arguments: [](#__codelineno-490-9)   -h, --help            show this help message and exit [](#__codelineno-490-10)   --pipeline PIPELINE   File containing pipeline contents [](#__codelineno-490-11)   --log LOGLEVEL        Specify logging level as none, [](#__codelineno-490-12)                         DEBUG,INFO,WARNING,ERROR,CRITICAL [](#__codelineno-490-13)   --name SCHEDULENAME   Schedule name to use [](#__codelineno-490-14)   --type SCHEDULE_TYPE  Schedule Type (Once, Minutes, Hourly, Daily, Weekly, [](#__codelineno-490-15)                         Always) [](#__codelineno-490-16)   --startdate STARTDATE [](#__codelineno-490-17)                         Start date for schedule in YYYY-MM-DD format [](#__codelineno-490-18)   --starttime STARTTIME [](#__codelineno-490-19)                         Start time for schedule in HH:MM format [](#__codelineno-490-20)   --enddate ENDDATE     End date for schedule in YYYY-MM-DD format [](#__codelineno-490-21)   --weekdays WEEKDAYS   Comma separated Day(s) of the week. Mandatory weekly [](#__codelineno-490-22)                         schedule type. Possible values:'MON', [](#__codelineno-490-23)                         'TUE','WED','THU','FRI','SAT','SUN' [](#__codelineno-490-24)   --freq FREQUENCY      Default 1 except for minutes, where it is 15 minutes [](#__codelineno-490-25)   --tz TIMEZONE         Timezone name [](#__codelineno-490-26)   --group GROUP         Worker group name [](#__codelineno-490-27)   --retries RETRIES     Maximum Retries [](#__codelineno-490-28)   --retry-intervals RETRYINTERVALS [](#__codelineno-490-29)                         Retry intervals. Example 5,10,15. Delay time interval [](#__codelineno-490-30)                         in minutes between each retry [](#__codelineno-490-31)   --parallel-instances PARALLELINSTANCES [](#__codelineno-490-32)                         Parallel instances number should range in between [](#__codelineno-490-33)                         1-10. Example 1,2,3`\
\
### Sub Command: `schedule-delete`\
\
Description: Delete an existing schedule\
\
`[](#__codelineno-491-1) Usage: schedule-delete  [-h] --scheduleId SCHEDULEID [](#__codelineno-491-2) [](#__codelineno-491-3) optional arguments: [](#__codelineno-491-4)   -h, --help            show this help message and exit [](#__codelineno-491-5)   --scheduleId SCHEDULEID [](#__codelineno-491-6)                         Schedule ID`\
\
### Sub Command: `schedule-edit`\
\
Description: Edit an existing schedule\
\
`[](#__codelineno-492-1) Usage: schedule-edit  [-h] --scheduleId SCHEDULEID --type SCHEDULE_TYPE [](#__codelineno-492-2)             [--startdate STARTDATE] [--starttime STARTTIME] [](#__codelineno-492-3)             [--enddate ENDDATE] [--weekdays WEEKDAYS] [--freq FREQUENCY] [](#__codelineno-492-4)             [--tz TIMEZONE] [--group GROUP] [--retries RETRIES] [](#__codelineno-492-5)             [--retry-intervals RETRYINTERVALS] [](#__codelineno-492-6)             [--parallel-instances PARALLELINSTANCES] [](#__codelineno-492-7) [](#__codelineno-492-8) optional arguments: [](#__codelineno-492-9)   -h, --help            show this help message and exit [](#__codelineno-492-10)   --scheduleId SCHEDULEID [](#__codelineno-492-11)                         Schedule ID [](#__codelineno-492-12)   --type SCHEDULE_TYPE  Schedule Type (Once, Minutes, Hourly, Daily, Weekly, [](#__codelineno-492-13)                         Always) [](#__codelineno-492-14)   --startdate STARTDATE [](#__codelineno-492-15)                         Start date for schedule in YYYY-MM-DD format [](#__codelineno-492-16)   --starttime STARTTIME [](#__codelineno-492-17)                         Start time for schedule in HH:MM format [](#__codelineno-492-18)   --enddate ENDDATE     End Date for schedule in YYYY-MM-DD format [](#__codelineno-492-19)   --weekdays WEEKDAYS   Comma separated Day(s) of the week. Mandatory weekly [](#__codelineno-492-20)                         schedule type. Possible values:'MON', [](#__codelineno-492-21)                         'TUE','WED','THU','FRI','SAT','SUN' [](#__codelineno-492-22)   --freq FREQUENCY      Default 1 except for minutes, where it is 15 minutes [](#__codelineno-492-23)   --tz TIMEZONE         Timezone name [](#__codelineno-492-24)   --group GROUP         Worker group name [](#__codelineno-492-25)   --retries RETRIES     Maximum Retries [](#__codelineno-492-26)   --retry-intervals RETRYINTERVALS [](#__codelineno-492-27)                         Retry intervals [](#__codelineno-492-28)   --parallel-instances PARALLELINSTANCES [](#__codelineno-492-29)                         Parallel instances number should range in between 1-10`\
\
### Sub Command: `schedule-info`\
\
Description: Get details of a schedule\
\
`[](#__codelineno-493-1) Usage: schedule-info  [-h] --scheduleId SCHEDULEID [--json] [](#__codelineno-493-2) [](#__codelineno-493-3) optional arguments: [](#__codelineno-493-4)   -h, --help            show this help message and exit [](#__codelineno-493-5)   --scheduleId SCHEDULEID [](#__codelineno-493-6)                         Schedule ID [](#__codelineno-493-7)   --json                Print detailed information in JSON format instead of [](#__codelineno-493-8)                         tabular format`\
\
### Sub Command: `schedule-list`\
\
Description: List all schedules\
\
`[](#__codelineno-494-1) Usage: schedule-list  [-h] [--json] [](#__codelineno-494-2) [](#__codelineno-494-3) optional arguments: [](#__codelineno-494-4)   -h, --help  show this help message and exit [](#__codelineno-494-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-494-6)               format`\
\
### Sub Command: `schedule-update-status`\
\
Description: Update status of an existing schedule\
\
`[](#__codelineno-495-1) Usage: schedule-update-status  [-h] --scheduleId SCHEDULEID --status STATUS [](#__codelineno-495-2) [](#__codelineno-495-3) optional arguments: [](#__codelineno-495-4)   -h, --help            show this help message and exit [](#__codelineno-495-5)   --scheduleId SCHEDULEID [](#__codelineno-495-6)                         Schedule ID [](#__codelineno-495-7)   --status STATUS       Status`\
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
`[](#__codelineno-496-1) rdac schema --help`\
\
`[](#__codelineno-497-1) Dataset Model Schema management commands [](#__codelineno-497-2) [](#__codelineno-497-3) Following are valid sub-commands for schema: [](#__codelineno-497-4)   list                      List schemas from the object store [](#__codelineno-497-5)   get                       Download a schema from the object store [](#__codelineno-497-6)   add                       Add a new schema to the object store [](#__codelineno-497-7)   delete                    Delete a schema from the object store`\
\
****Sub Command: `list`****\
\
Description: List schemas from the object store\
\
`[](#__codelineno-498-1) Usage: schema-list  [-h] [--json] [](#__codelineno-498-2) [](#__codelineno-498-3) optional arguments: [](#__codelineno-498-4)   -h, --help  show this help message and exit [](#__codelineno-498-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-498-6)               format`\
\
*   Following is the syntax for **schema-list**\
\
`[](#__codelineno-499-1) rdac schema list --help`\
\
Example Output\
\
   `[](#__codelineno-500-1)    name              num_columns  saved_time                  title [](#__codelineno-500-2) --  --------------  -------------  --------------------------  ----------------------------- [](#__codelineno-500-3)  0  Example Schema              5  2023-01-05T04:52:38.182396  Example Schema [](#__codelineno-500-4)  1  Schema-QA                   6  2023-01-05T04:38:41.935552  QA Schema [](#__codelineno-500-5)  2  Test                        3  2023-01-05T04:39:03.106297  Pager Duty Urgency Enrichment`\
\
****Sub Command: `get`****\
\
Description: Download a schema from the object store\
\
`[](#__codelineno-501-1) rdac schema get --help`\
\
`[](#__codelineno-502-1) Usage: schema-get  [-h] --name NAME [](#__codelineno-502-2) [](#__codelineno-502-3) optional arguments: [](#__codelineno-502-4)   -h, --help   show this help message and exit [](#__codelineno-502-5)   --name NAME  Schema name`\
\
*   Following is the syntax for **schema-get**\
\
 `[](#__codelineno-503-1)  rdac schema get --name Test`\
\
Example Output\
\
`[](#__codelineno-504-1) { [](#__codelineno-504-2)   "title": "Pager Duty Urgency Enrichment", [](#__codelineno-504-3)   "properties": { [](#__codelineno-504-4)     "rule": { [](#__codelineno-504-5)       "type": "string" [](#__codelineno-504-6)     }, [](#__codelineno-504-7)     "rule_id": { [](#__codelineno-504-8)       "type": "string" [](#__codelineno-504-9)     }, [](#__codelineno-504-10)     "urgency_id": { [](#__codelineno-504-11)       "type": "string", [](#__codelineno-504-12)       "default": "low", [](#__codelineno-504-13)       "enum": [ [](#__codelineno-504-14)         "low", [](#__codelineno-504-15)         "medium", [](#__codelineno-504-16)         "high", [](#__codelineno-504-17)         "critical", [](#__codelineno-504-18)         "emergency" [](#__codelineno-504-19)       ] [](#__codelineno-504-20)     } [](#__codelineno-504-21)   }, [](#__codelineno-504-22)   "required": [ [](#__codelineno-504-23)     "rule", [](#__codelineno-504-24)     "rule_id" [](#__codelineno-504-25)   ], [](#__codelineno-504-26)   "name": "Test", [](#__codelineno-504-27)   "date": "2023-01-05T04:39:03.106297" [](#__codelineno-504-28) }`\
\
****Sub Command: `add`****\
\
Description: Add a new schema to the object store\
\
`[](#__codelineno-505-1) rdac schema add --help`\
\
`[](#__codelineno-506-1) Usage: schema-add  [-h] --name NAME --file INPUT_FILE [](#__codelineno-506-2) [](#__codelineno-506-3) optional arguments: [](#__codelineno-506-4)   -h, --help         show this help message and exit [](#__codelineno-506-5)   --name NAME        Schema name [](#__codelineno-506-6)   --file INPUT_FILE  File (or URL) containing the json schema as per [](#__codelineno-506-7)                      (https://json-schema.org/specification.html)`\
\
*   Following is the syntax for **schema-add**\
\
`[](#__codelineno-507-1) rdac schema add --name Schematest --file schematest.json`\
\
Example Output 1\
\
`[](#__codelineno-508-1) Successfully loaded schema Schematest and validated. [](#__codelineno-508-2) Unknown schema Schematest [](#__codelineno-508-3) [](#__codelineno-508-4) Added/modified schema Schematest`\
\
Note\
\
Before adding the schema, create a JSON input\_file containing the json schema.\
\
Example output 2\
\
`[](#__codelineno-509-1) { [](#__codelineno-509-2)   "title": "New Pager Duty Urgency Enrichment", [](#__codelineno-509-3)   "properties": { [](#__codelineno-509-4)     "rule": { [](#__codelineno-509-5)       "type": "string" [](#__codelineno-509-6)     }, [](#__codelineno-509-7)     "rule_id": { [](#__codelineno-509-8)       "type": "string" [](#__codelineno-509-9)     }, [](#__codelineno-509-10)     "urgency_id": { [](#__codelineno-509-11)       "type": "string", [](#__codelineno-509-12)       "default": "low", [](#__codelineno-509-13)       "enum": [ [](#__codelineno-509-14)         "low", [](#__codelineno-509-15)         "medium", [](#__codelineno-509-16)         "high", [](#__codelineno-509-17)         "critical", [](#__codelineno-509-18)         "emergency" [](#__codelineno-509-19)       ] [](#__codelineno-509-20)     } [](#__codelineno-509-21)   }, [](#__codelineno-509-22)   "required": [ [](#__codelineno-509-23)     "rule", [](#__codelineno-509-24)     "rule_id" [](#__codelineno-509-25)   ], [](#__codelineno-509-26)   "name": "Test", [](#__codelineno-509-27)   "date": "2023-01-24T04:39:03.106297" [](#__codelineno-509-28) }`\
\
****Sub Command: `delete`****\
\
Description: Delete a schema from the object store\
\
rdac schema delete --help\
\
`[](#__codelineno-510-1) Usage: schema-delete  [-h] --name NAME [--yes] [](#__codelineno-510-2) [](#__codelineno-510-3) optional arguments: [](#__codelineno-510-4)   -h, --help   show this help message and exit [](#__codelineno-510-5)   --name NAME  Schema name [](#__codelineno-510-6)   --yes        Delete without prompting`\
\
*   Following is the syntax for **schema-delete**\
\
`[](#__codelineno-511-1) rdac schema delete --name Schematest`\
\
Example Output\
\
`[](#__codelineno-512-1) Confirm deletion of schema (y/n)? y [](#__codelineno-512-2) Schema deleted.`\
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
`[](#__codelineno-513-1) rdac secret`\
\
`[](#__codelineno-514-1) Credentials (Secrets) management commands [](#__codelineno-514-2) [](#__codelineno-514-3) Following are valid sub-commands for secret: [](#__codelineno-514-4)   types                     List of all available secret types [](#__codelineno-514-5)   add                       Add a new secret to the vault [](#__codelineno-514-6)   delete                    Delete a secret from the vault [](#__codelineno-514-7)   list                      List names and types of all secrets in vault`\
\
****Sub Command: `types`****\
\
Description: List of all available secret types\
\
`[](#__codelineno-515-1) rdac secret-types --help`\
\
`[](#__codelineno-516-1) Usage: secret-types  [-h] [--json] [](#__codelineno-516-2) [](#__codelineno-516-3) optional arguments: [](#__codelineno-516-4)   -h, --help  show this help message and exit [](#__codelineno-516-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-516-6)               format`\
\
\* Following is the syntax for **secret-types**\
\
`[](#__codelineno-517-1) rdac secret-types`\
\
Example Output\
\
`[](#__codelineno-518-1) +-----------------------+-----------------------------------------------------------------------------------------------------------------+ [](#__codelineno-518-2) | Type                  | Description                                                                                                     | [](#__codelineno-518-3) |-----------------------+-----------------------------------------------------------------------------------------------------------------| [](#__codelineno-518-4) | aiaexpress            | CloudFabrix AIA Express                                                                                         | [](#__codelineno-518-5) | ansible               | Ansible - Run Ansible playbook defined in the input dataset                                                     | [](#__codelineno-518-6) | appdynamics           | AppDynamics - Inventory and Metrics collection from AppDynamics                                                 | [](#__codelineno-518-7) | arcsight              | ArcSight - Get event details from ArcSight                                                                      | [](#__codelineno-518-8) | arista-bigswitch      | Arista Bigswitch Fabric Inventory Collection                                                                    | [](#__codelineno-518-9) | aws                   | AWS EC2                                                                                                         | [](#__codelineno-518-10) | aws-cloudwatch        | AWS CloudWatch - Logs and Metric collection from AWS Cloudwatch                                                 | [](#__codelineno-518-11) | aws-cloudwatch-v2     | AWS CloudWatch - Logs and Metric collection from AWS Cloudwatch                                                 | [](#__codelineno-518-12) | aws-kinesis           | AWS Kinesis - Read and Write data on AWS Kinesis streams                                                        | [](#__codelineno-518-13) | aws-sqs               | AWS SQS - Read and Write data to SQS stream                                                                     | [](#__codelineno-518-14) | aws_v2                | AWS EC2 - Collect inventory details from EC2 instances                                                          | [](#__codelineno-518-15) | azure                 | Microsoft Azure - Collect inventory details from Microsoft Azure                                                | [](#__codelineno-518-16) | azure-insights        | Microsoft Azure Insights - Collect metrics and logs from Azure                                                  | [](#__codelineno-518-17) | blob_aws              | Pull/Push blobs from AWS Cloud object stores                                                                    | [](#__codelineno-518-18) | blob_azure            | Pull/Push blobs from Azure Cloud object stores                                                                  | [](#__codelineno-518-19) | blob_gcp              | Pull/Push blobs from GCP Cloud object stores                                                                    | [](#__codelineno-518-20) | cfxai_classification  | CloudFabrix ML - Classification                                                                                 | [](#__codelineno-518-21) +-----------------------+-----------------------------------------------------------------------------------------------------------------+`\
\
****Sub Command: `add`****\
\
### Sub Command: `secret-add`\
\
Description: Add a new secret to the vault\
\
`[](#__codelineno-519-1) Usage: secret-add  [-h] --type SECRET_TYPE [](#__codelineno-519-2) [](#__codelineno-519-3) optional arguments: [](#__codelineno-519-4)   -h, --help          show this help message and exit [](#__codelineno-519-5)   --type SECRET_TYPE  Secret type (use secret-list command to see available [](#__codelineno-519-6)                       secret types)`\
\
****Sub Command: `list`****\
\
Description: List names and types of all secrets in vault\
\
`[](#__codelineno-520-1) Usage: secret-list  [-h] [--json] [](#__codelineno-520-2) [](#__codelineno-520-3) optional arguments: [](#__codelineno-520-4)   -h, --help  show this help message and exit [](#__codelineno-520-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-520-6)               format`\
\
\* Following is the syntax for **secret-list**\
\
`[](#__codelineno-521-1) rdac secret-list`\
\
Example Output\
\
    `[](#__codelineno-522-1)     name    type              saved_time                  checksum [](#__codelineno-522-2) --  ------  ----------------  --------------------------  -------------------------------- [](#__codelineno-522-3)  0  cfxml   cfxai_regression  2023-01-12T05:49:39.325308  def3259af30655a412beb39a8a99e53a`\
\
### Sub command: `set-pod-log-level`\
\
Description: Update the logging level for a given RDA Pod\
\
`[](#__codelineno-523-1) usage: rdac [-h] --id POD_ID --level LEVEL [--logger LOGGER_NAME] [](#__codelineno-523-2) [](#__codelineno-523-3) optional arguments: [](#__codelineno-523-4)   -h, --help            show this help message and exit [](#__codelineno-523-5)   --id POD_ID           pod_id of the pod for which the logging level need to [](#__codelineno-523-6)                         be configured [](#__codelineno-523-7)   --level LEVEL         Logging level. Must be one of DEBUG INFO WARNING ERROR [](#__codelineno-523-8)                         CRITICAL [](#__codelineno-523-9)   --logger LOGGER_NAME  Logging Name. By default it sets the root logger.`\
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
`[](#__codelineno-524-1) rdac site-profile --help`\
\
`[](#__codelineno-525-1) Site Profile management commands [](#__codelineno-525-2) [](#__codelineno-525-3) Following are valid sub-commands for site-profile: [](#__codelineno-525-4)   add                       Add a new site profile [](#__codelineno-525-5)   edit                      Update a site profile [](#__codelineno-525-6)   get                       Get a site profile data [](#__codelineno-525-7)   delete                    Delete a site profile [](#__codelineno-525-8)   list                      List all site profiles`\
\
### Sub Command: `site-profile-add`\
\
Description: Add a new site profile\
\
`[](#__codelineno-526-1) Usage: site-profile-add  [-h] --name NAME --site SITE [--description DESCRIPTION] [](#__codelineno-526-2)             [--sources SOURCES] [](#__codelineno-526-3) [](#__codelineno-526-4) optional arguments: [](#__codelineno-526-5)   -h, --help            show this help message and exit [](#__codelineno-526-6)   --name NAME           Name of Site Profile [](#__codelineno-526-7)   --site SITE           Site name or a regular expression [](#__codelineno-526-8)   --description DESCRIPTION [](#__codelineno-526-9)                         Description of Site Profile [](#__codelineno-526-10)   --sources SOURCES     Comma separated list of sources`\
\
### Sub Command: `site-profile-delete`\
\
Description: Delete a site profile\
\
`[](#__codelineno-527-1) Usage: site-profile-delete  [-h] --name NAME [](#__codelineno-527-2) [](#__codelineno-527-3) optional arguments: [](#__codelineno-527-4)   -h, --help   show this help message and exit [](#__codelineno-527-5)   --name NAME  Name of the site profile to delete`\
\
### Sub Command: `site-profile-edit`\
\
Description: Update a site profile\
\
`[](#__codelineno-528-1) Usage: site-profile-edit  [-h] --name NAME [--site SITE] [--description DESCRIPTION] [](#__codelineno-528-2)             [--sources SOURCES] [](#__codelineno-528-3) [](#__codelineno-528-4) optional arguments: [](#__codelineno-528-5)   -h, --help            show this help message and exit [](#__codelineno-528-6)   --name NAME           Name of Site Profile [](#__codelineno-528-7)   --site SITE           Site name or a regular expression [](#__codelineno-528-8)   --description DESCRIPTION [](#__codelineno-528-9)                         Description of Site Profile [](#__codelineno-528-10)   --sources SOURCES     Comma separated list of sources`\
\
### Sub Command: `site-profile-get`\
\
Description: Get a site profile data\
\
`[](#__codelineno-529-1) Usage: site-profile-get  [-h] --name NAME [](#__codelineno-529-2) [](#__codelineno-529-3) optional arguments: [](#__codelineno-529-4)   -h, --help   show this help message and exit [](#__codelineno-529-5)   --name NAME  Name of the site profile to display`\
\
### Sub Command: `site-profile-list`\
\
Description: List all site profiles.\
\
`[](#__codelineno-530-1) rdac site-profile-list --help`\
\
`[](#__codelineno-531-1) Usage: site-profile-list  [-h] [--json] [](#__codelineno-531-2) [](#__codelineno-531-3) optional arguments: [](#__codelineno-531-4)   -h, --help  show this help message and exit [](#__codelineno-531-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-531-6)               format`\
\
\* Following is the syntax for **site-profile-list**\
\
`[](#__codelineno-532-1) rdac site-profile-list`\
\
Example Output\
\
    `[](#__codelineno-533-1)     name     description           site    sources    saved_time [](#__codelineno-533-2) --  -------  --------------------  ------  ---------  -------------------------- [](#__codelineno-533-3)  0  default  Default Site Profile  .*      cfxml      2023-01-12T05:49:39.425974`\
\
### Sub Command: `site-summary`\
\
Description: Show summary by Site and Overall\
\
`[](#__codelineno-534-1) rdac site-summary --help`\
\
`[](#__codelineno-535-1) usage: rdac [-h] [--json] [](#__codelineno-535-2) [](#__codelineno-535-3) optional arguments: [](#__codelineno-535-4)   -h, --help  show this help message and exit [](#__codelineno-535-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-535-6)               format`\
\
\* Following is the syntax for **site-summary**\
\
`[](#__codelineno-536-1) rdac site-summary`\
\
Example Output\
\
`[](#__codelineno-537-1) Summary [](#__codelineno-537-2)     Overall [](#__codelineno-537-3)        Infra Pod Count: 25 [](#__codelineno-537-4)        Worker Count: 1 [](#__codelineno-537-5)        Worker Group Count: 4 [](#__codelineno-537-6)        Site Count: 4 [](#__codelineno-537-7)        Cpu Cores: 4 [](#__codelineno-537-8)        Memory Gb: 31.3 [](#__codelineno-537-9)        Active Jobs: 3 [](#__codelineno-537-10)        Total Jobs: 10 [](#__codelineno-537-11)        Agent Count: 3 [](#__codelineno-537-12)        Site Names: collabagent, mlagent, irmagent, rda-site-01 [](#__codelineno-537-13) [](#__codelineno-537-14)     By Site [](#__codelineno-537-15)       * Name: collabagent [](#__codelineno-537-16)         Worker Count: 0 [](#__codelineno-537-17)         Cpu Cores: 0 [](#__codelineno-537-18)         Memory Gb: 0 [](#__codelineno-537-19)         Active Jobs: 0 [](#__codelineno-537-20)         Total Jobs: 0 [](#__codelineno-537-21)         Agent Count: 1 [](#__codelineno-537-22)         Agent Names: agent-collab [](#__codelineno-537-23) [](#__codelineno-537-24)       * Name: irmagent [](#__codelineno-537-25)         Worker Count: 0 [](#__codelineno-537-26)         Cpu Cores: 0 [](#__codelineno-537-27)         Memory Gb: 0 [](#__codelineno-537-28)         Active Jobs: 0 [](#__codelineno-537-29)         Total Jobs: 0 [](#__codelineno-537-30)         Agent Count: 1 [](#__codelineno-537-31)         Agent Names: agent-irm`\
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
`[](#__codelineno-538-1) rdac stack cache-list --help`\
\
`[](#__codelineno-539-1) usage: stack [-h] [--json] [](#__codelineno-539-2) [](#__codelineno-539-3) optional arguments: [](#__codelineno-539-4)   -h, --help  show this help message and exit [](#__codelineno-539-5)   --json      Print results in JSON format`\
\
*   Following is the syntax for **stack cache-list**\
\
`[](#__codelineno-540-1) rdac stack cache-list --json`\
\
Example Output\
\
{ "status": "ok", "data": \[\], "now": "2023-01-23T07:04:25.597835" }\
\
****Sub Command: `impact-distance`****\
\
Description: Find the impact distances in a stack using asset-dependency service, load search criteria from a JSON file\
\
`[](#__codelineno-541-1) rdac stack impact-distance --help`\
\
`[](#__codelineno-542-1) usage: stack [-h] --name STACK_NAME --search_file SEARCH_FILE [--json] [](#__codelineno-542-2) [](#__codelineno-542-3) optional arguments: [](#__codelineno-542-4)   -h, --help            show this help message and exit [](#__codelineno-542-5)   --name STACK_NAME     Stack name [](#__codelineno-542-6)   --search_file SEARCH_FILE [](#__codelineno-542-7)                         Filename with JSON based search criteria [](#__codelineno-542-8)   --json                Print results in JSON format`\
\
\* Following is the syntax for **stack impact-distance**\
\
`[](#__codelineno-543-1) rdac stack-impact-distance  --name vcenter_topology_stacks --search_file /tmp/search.json`\
\
Example Output\
\
 `[](#__codelineno-544-1)  node_id                   node_label              layer      node_type   distance via [](#__codelineno-544-2) -- ------------------------------------------ ----------------------------------- -------------- ----------- ---------- ------------------------------------------ [](#__codelineno-544-3)  0 423306a6-f91e-ed00-c1dc-d5b3a004659a    debian8.engr.cloudfabrix.com     Virtualization VM          -1 10.95.158.200 [](#__codelineno-544-4)  1 42330bd2-019b-3f22-c629-29824bc07ab7    AIA-Hari-PF80.engr.cloudfabrix.com  Virtualization VM          -1 10.95.158.200 [](#__codelineno-544-5)  2 42331120-6a91-ce70-f8f2-3bfe6620c4f1    macaw0vf1.0.0-Ch           Virtualization VM          -1 10.95.158.200 [](#__codelineno-544-6)  3 42333b86-240a-eddd-0b33-fadc6e242c25    MacawOVFPlatformPOC-v1.0.0      Virtualization VM          -1 10.95.158.200 [](#__codelineno-544-7)  4 42336507-674d-0d86-d8a2-508518fdf9f8    SNMPSimulator-macaw-219       Virtualization VM          -1 10.95.158.200 [](#__codelineno-544-8)  5 4233a553-8746-5ee6-02d8-87423d388ba1    oialatserv1.qa.engr.cloudfabrix.com Virtualization VM          -1 10.95.158.200 [](#__codelineno-544-9)  6 4233ab94-559d-892d-7130-b0ec1d237d11    windows2008r2enterprise       Virtualization VM          -1 10.95.158.200 [](#__codelineno-544-10)  7 4233ee33-5cd3-2a90-0a11-65e2db7ce9dc    platform-60.qa.engr.cloudfabrix.com Virtualization VM          -1 10.95.158.200 [](#__codelineno-544-11)  8 4233f1eb-3ddc-7464-08f9-d536844c10e9    SNMPSimulator-238          Virtualization VM          -1 10.95.158.200 [](#__codelineno-544-12)  9 4233f62f-7f59-fb80-31d3-a89ab6108df1    oialatpf.qa.engr.cloudfabrix.com   Virtualization VM          -1 10.95.158.200 [](#__codelineno-544-13) 10 4233f6a4-5870-48f4-9d61-af0a0f455593    Promotheus_windows_vm_testing    Virtualization VM          -1 10.95.158.200 [](#__codelineno-544-14) 11 4233ffd3-2061-59fd-fe2c-832097ccc1f6    oialatclam1.qa.engr.cloudfabrix.com Virtualization VM          -1 10.95.158.200 [](#__codelineno-544-15) 12 564d3503-5fe7-d5a0-70b8-e1adf218ffaa    pf150.qa.engr.cloudfabrix.com    Virtualization VM          -1 10.95.158.200 [](#__codelineno-544-16) 13 564d3c15-d2a9-e904-0c21-bf53301960f7    hari_elk7.4.engr.cloudfabrix.com   Virtualization VM          -1 10.95.158.200 [](#__codelineno-544-17) 14 564d4711-398f-34f1-7f3f-919d3b4eadcd    SNMPSimulator-macaw-214       Virtualization VM          -1 10.95.158.200`\
\
### Sub Command: `stack-search`\
\
Description: Search in a stack using asset-dependency service\
\
`[](#__codelineno-545-1) Usage: stack-search  [-h] --name STACK_NAME --values VALUES --attrs ATTRS --types TYPES [](#__codelineno-545-2)             [--exclude EXCLUDE] [--depth DEPTH] [](#__codelineno-545-3) [](#__codelineno-545-4) optional arguments: [](#__codelineno-545-5)   -h, --help         show this help message and exit [](#__codelineno-545-6)   --name STACK_NAME  Stack name [](#__codelineno-545-7)   --values VALUES    Attribute values to search for. Multiple values may be [](#__codelineno-545-8)                      specified separated by a comma [](#__codelineno-545-9)   --attrs ATTRS      Comma separated list of node attribute names [](#__codelineno-545-10)   --types TYPES      Comma separated list of node types to search [](#__codelineno-545-11)   --exclude EXCLUDE  Comma separated list of node types to exclude in search [](#__codelineno-545-12)   --depth DEPTH      Max depth`\
\
### Sub Command: `stack-search-json`\
\
Description: Search in a stack using asset-dependency service, load search criteria from a JSON file\
\
`[](#__codelineno-546-1) Usage: stack-search-json  [-h] --name STACK_NAME --search_file SEARCH_FILE [](#__codelineno-546-2) [](#__codelineno-546-3) optional arguments: [](#__codelineno-546-4)   -h, --help            show this help message and exit [](#__codelineno-546-5)   --name STACK_NAME     Stack name [](#__codelineno-546-6)   --search_file SEARCH_FILE [](#__codelineno-546-7)                         Filename with JSON based search criteria`\
\
### Sub Command: `staging-area-add`\
\
Description: Add or update staging area\
\
`[](#__codelineno-547-1) Usage: staging-area-add  [-h] --file INPUT_FILE [--overwrite] [](#__codelineno-547-2) [](#__codelineno-547-3) optional arguments: [](#__codelineno-547-4)   -h, --help         show this help message and exit [](#__codelineno-547-5)   --file INPUT_FILE  YAML file containing staging area definition [](#__codelineno-547-6)   --overwrite        Overwrite even if a staging area already exists with a [](#__codelineno-547-7)                      name.`\
\
### Sub Command: `staging-area-delete`\
\
Description: Delete a staging area\
\
`[](#__codelineno-548-1) Usage: staging-area-delete  [-h] --name STAGING_AREA_NAME [](#__codelineno-548-2) [](#__codelineno-548-3) optional arguments: [](#__codelineno-548-4)   -h, --help            show this help message and exit [](#__codelineno-548-5)   --name STAGING_AREA_NAME [](#__codelineno-548-6)                         Name of the staging area to delete`\
\
### Sub Command: `staging-area-get`\
\
Description: Get YAML data for a staging area\
\
`[](#__codelineno-549-1) Usage: staging-area-get  [-h] --name STAGING_AREA_NAME [](#__codelineno-549-2) [](#__codelineno-549-3) optional arguments: [](#__codelineno-549-4)   -h, --help            show this help message and exit [](#__codelineno-549-5)   --name STAGING_AREA_NAME [](#__codelineno-549-6)                         Name of the staging area`\
\
### Sub Command: `staging-area-list`\
\
Description: List all staging areas.\
\
`[](#__codelineno-550-1) Usage: staging-area-list  [-h] [--json] [](#__codelineno-550-2) [](#__codelineno-550-3) optional arguments: [](#__codelineno-550-4)   -h, --help  show this help message and exit [](#__codelineno-550-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-550-6)               format`\
\
### Sub Command: `subscription`\
\
Description: Show current CloudFabrix RDA subscription details\
\
`[](#__codelineno-551-1) Usage: subscription  [-h] [--json] [--details] [](#__codelineno-551-2) [](#__codelineno-551-3) optional arguments: [](#__codelineno-551-4)   -h, --help  show this help message and exit [](#__codelineno-551-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-551-6)               format [](#__codelineno-551-7)   --details   Show full details when showing plain text format`\
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
`[](#__codelineno-552-1) rdac synthetics --help`\
\
`[](#__codelineno-553-1) Data synthesizing management commands [](#__codelineno-553-2) [](#__codelineno-553-3) Following are valid sub-commands for synthetics: [](#__codelineno-553-4)   add                       Add or update Synthetic Profile [](#__codelineno-553-5)   get                       Get JSON data for a Synthetic Profile [](#__codelineno-553-6)   list                      List all Synthetic Profiles [](#__codelineno-553-7)   delete                    Delete a Synthetic Profile [](#__codelineno-553-8)   enable                    Change the status of a Synthetic Profile to 'enabled' [](#__codelineno-553-9)   disable                   Change the status of a Synthetic Profile to 'disabled' [](#__codelineno-553-10)   status                    List status of all active synthetic profiles [](#__codelineno-553-11)   reset                     Reset all active situations in a single synthetic profile [](#__codelineno-553-12)   situation                 Activate a specific situtation in a given synthetic profile [](#__codelineno-553-13)   webhooks-list             List all Webhook Targets for Synthesizer [](#__codelineno-553-14)   webhooks-update           Update Webhook Targets for Synthesizer [](#__codelineno-553-15)   generate-ml-dataset       Generate ML dataset from input alerts & incidents stream and write to an output stream`\
\
****Sub Command: `get`****\
\
Description: Get JSON data for a Synthetic Profile\
\
`[](#__codelineno-554-1) rdac synthetics get --help`\
\
`[](#__codelineno-555-1) usage: synthetics [-h] --name SYNTHETIC_PROFILE_NAME [](#__codelineno-555-2) [](#__codelineno-555-3) optional arguments: [](#__codelineno-555-4)   -h, --help            show this help message and exit [](#__codelineno-555-5)   --name SYNTHETIC_PROFILE_NAME [](#__codelineno-555-6)                         Name of the synthetic_profile`\
\
\* Following is the syntax for **synthetics get**\
\
`[](#__codelineno-556-1) rdac synthetics get --name Online_Banking_App_Profile`\
\
Example Output\
\
`[](#__codelineno-557-1) { [](#__codelineno-557-2)     "name": "Online_Banking_App_Profile", [](#__codelineno-557-3)     "label": "Online Banking App Synthetics", [](#__codelineno-557-4)     "enabled": true, [](#__codelineno-557-5)     "version": "22.8.22.1", [](#__codelineno-557-6)     "stack": "Online_Banking_Stack", [](#__codelineno-557-7)     "metric_stream": "rda_synthetic_metrics", [](#__codelineno-557-8)     "alert_stream": "rda_synthetic_alerts", [](#__codelineno-557-9)     "diagnostics": [ [](#__codelineno-557-10)         { [](#__codelineno-557-11)             "id": "db_storage", [](#__codelineno-557-12)             "label": "Check Database Storage", [](#__codelineno-557-13)             "rules": { [](#__codelineno-557-14)                 "tlog": { [](#__codelineno-557-15)                     "name": "Transaction Log Free Disk Space", [](#__codelineno-557-16)                     "check": "Ensure 100GB of free disk space", [](#__codelineno-557-17)                     "status": { [](#__codelineno-557-18)                         "NORMAL": "Available Disk space is 100GB oe more", [](#__codelineno-557-19)                         "WARNING": "Available disk space is between 75GB to 100GB", [](#__codelineno-557-20)                         "CRITICAL": "Available disk space is less than 50GB" [](#__codelineno-557-21)                     } [](#__codelineno-557-22)                 }, [](#__codelineno-557-23)                 "backup": { [](#__codelineno-557-24)                     "name": "Backup Volume Free Disk Space", [](#__codelineno-557-25)                     "check": "Ensure 500GB of free disk space", [](#__codelineno-557-26)                     "status": {`\
\
****Sub Command: `list`****\
\
Description: List all Synthetic Profiles\
\
`[](#__codelineno-558-1) rdac synthetics list --help`\
\
`[](#__codelineno-559-1) usage: synthetics [-h] [--json] [](#__codelineno-559-2) [](#__codelineno-559-3) optional arguments: [](#__codelineno-559-4)   -h, --help  show this help message and exit [](#__codelineno-559-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-559-6)               format`\
\
*   Following is the syntax for **synthetics list**\
\
`[](#__codelineno-560-1) rdac synthetics list`\
\
Example Output\
\
`[](#__codelineno-561-1) name                        label                          enabled    saved_time [](#__codelineno-561-2) --  --------------------------  -----------------------------  ---------  -------------------------- [](#__codelineno-561-3)  0  Pet_Clinic_App_Profile1     Pet Clinic App Synthetics1     no         2022-10-04T23:01:52.860735 [](#__codelineno-561-4)  1  log-profile-example-1       ACME Log Synthetics            yes        2023-01-23T22:13:48.183910 [](#__codelineno-561-5)  2  Pet_Clinic_App_Profile      Pet Clinic App Synthetics      no         2022-09-28T05:51:51.861521 [](#__codelineno-561-6)  3  Online_Banking_App_Profile  Online Banking App Synthetics  yes        2023-01-10T01:51:32.625109`\
\
****Sub Command: `status`****\
\
Description: List status of all active synthetic profiles\
\
`[](#__codelineno-562-1) rdac synthetics status --help`\
\
`[](#__codelineno-563-1) usage: synthetics [-h] [--json] [](#__codelineno-563-2) [](#__codelineno-563-3) optional arguments: [](#__codelineno-563-4)   -h, --help  show this help message and exit [](#__codelineno-563-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-563-6)               format`\
\
*   Following is the syntax for **synthetics status**\
\
`[](#__codelineno-564-1) rdac synthetics status --json`\
\
Example Output\
\
`[](#__codelineno-565-1) 2023-02-10:09:59:38 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-565-2) { [](#__codelineno-565-3)     "status": "ok", [](#__codelineno-565-4)     "data": [ [](#__codelineno-565-5)         { [](#__codelineno-565-6)             "metrics": 0, [](#__codelineno-565-7)             "alerts": 0, [](#__codelineno-565-8)             "profile_name": "log-profile-example-1", [](#__codelineno-565-9)             "stack": "Enterprise_Data_and_Analytics_Stack", [](#__codelineno-565-10)             "active_situations": "" [](#__codelineno-565-11)         }, [](#__codelineno-565-12)         { [](#__codelineno-565-13)             "metrics": 26, [](#__codelineno-565-14)             "alerts": 1, [](#__codelineno-565-15)             "profile_name": "Online_Banking_App_Profile", [](#__codelineno-565-16)             "stack": "Online_Banking_Stack", [](#__codelineno-565-17)             "active_situations": "" [](#__codelineno-565-18)         } [](#__codelineno-565-19)     ], [](#__codelineno-565-20)     "now": "2023-02-10T09:59:38.147686" [](#__codelineno-565-21) }`\
\
****Sub Command: `enable`****\
\
Description: Change the status of a Synthetic Profile to 'enabled'\
\
`[](#__codelineno-566-1) rdac synthetics enable --help`\
\
`[](#__codelineno-567-1) usage: synthetics [-h] --name SYNTHETIC_PROFILE_NAME [](#__codelineno-567-2) [](#__codelineno-567-3) optional arguments: [](#__codelineno-567-4)   -h, --help            show this help message and exit [](#__codelineno-567-5)   --name SYNTHETIC_PROFILE_NAME [](#__codelineno-567-6)                         Name of the synthetic profile`\
\
*   Following is the syntax for **synthetics enable**\
\
`[](#__codelineno-568-1) rdac synthetics enable  Pet_Clinic_App_Profile1`\
\
Example Output\
\
`[](#__codelineno-569-1) 2023-02-10:09:58:02 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-569-2) 2023-02-10:09:58:02 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-569-3) 2023-02-10:09:58:02 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-569-4) Changed status of Pet_Clinic_App_Profile1 to enabled`\
\
****Sub Command: `disable`****\
\
Description: Change the status of a Synthetic Profile to 'disabled'\
\
`[](#__codelineno-570-1) rdac synthetics disable --help`\
\
`[](#__codelineno-571-1) usage: synthetics [-h] --name SYNTHETIC_PROFILE_NAME [](#__codelineno-571-2) [](#__codelineno-571-3) optional arguments: [](#__codelineno-571-4)   -h, --help            show this help message and exit [](#__codelineno-571-5)   --name SYNTHETIC_PROFILE_NAME [](#__codelineno-571-6)                         Name of the synthetic profile`\
\
*   Following is the syntax for **synthetics disable**\
\
 `[](#__codelineno-572-1)  rdac synthetics disable  --name  Pet_Clinic_App_Profile1`\
\
Example Output\
\
`[](#__codelineno-573-1) 2023-02-10:09:58:45 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-573-2) 2023-02-10:09:58:45 [1] INFO nats_client Initiallzing PubMgr for pid=1 [](#__codelineno-573-3) 2023-02-10:09:58:45 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-573-4) Changed status of Pet_Clinic_App_Profile1 to disabled`\
\
### Sub Command: `verify-pipeline`\
\
Description: Verify the pipeline on a worker pod\
\
`[](#__codelineno-574-1) Usage: verify-pipeline  [-h] --pipeline PIPELINE [--group WORKER_GROUP] [](#__codelineno-574-2)             [--site WORKER_SITE] [--lfilter LABEL_FILTER] [](#__codelineno-574-3)             [--rfilter RESOURCE_FILTER] [--maxwait MAX_WAIT] [](#__codelineno-574-4) [](#__codelineno-574-5) optional arguments: [](#__codelineno-574-6)   -h, --help            show this help message and exit [](#__codelineno-574-7)   --pipeline PIPELINE   File containing pipeline contents [](#__codelineno-574-8)   --group WORKER_GROUP  Deprecated. Use --site option. Specify a worker site [](#__codelineno-574-9)                         name. If not specified, will use any available worker. [](#__codelineno-574-10)   --site WORKER_SITE    Specify a worker site name. If not specified, will use [](#__codelineno-574-11)                         any available worker. [](#__codelineno-574-12)   --lfilter LABEL_FILTER [](#__codelineno-574-13)                         CFXQL style query to narrow down workers using their [](#__codelineno-574-14)                         labels [](#__codelineno-574-15)   --rfilter RESOURCE_FILTER [](#__codelineno-574-16)                         CFXQL style query to narrow down workers using their [](#__codelineno-574-17)                         resources [](#__codelineno-574-18)   --maxwait MAX_WAIT    Maximum wait time (seconds) for credential check to [](#__codelineno-574-19)                         complete.`\
\
*   Following is the syntax for **verify-pipeline**\
\
`[](#__codelineno-575-1) rdac verify-pipeline --pipeline jira.json --group aws-qa-102-200 --rfilter "cpu_count = 8" --lfilter "rda_messenger_version = '21.7.29.3'"`\
\
Example Output\
\
`[](#__codelineno-576-1) Initiating verify pipeline [](#__codelineno-576-2) { [](#__codelineno-576-3)   "status": "started", [](#__codelineno-576-4)   "reason": "", [](#__codelineno-576-5)   "results": [], [](#__codelineno-576-6)   "now": "2021-08-06T15:35:11.078751", [](#__codelineno-576-7)   "status-subject": "tenants.d6152687e007482e99ed210bca1fbe9e.worker.group.f17ce69d60d8.direct.9729ad1e", [](#__codelineno-576-8)   "jobid": "39e2cf7970b144fe911ec51f7a9f5a35" [](#__codelineno-576-9) } [](#__codelineno-576-10) Initializing: [](#__codelineno-576-11) Initializing: [](#__codelineno-576-12) Initializing: [](#__codelineno-576-13) Initializing: [](#__codelineno-576-14) Completed:`\
\
### Sub Command: `viz`\
\
Description: Visualize data from a file within the console (terminal)\
\
`[](#__codelineno-577-1) Usage: viz  [-h] --file INPUT_FILE [--format FILE_FORMAT] [](#__codelineno-577-2) [](#__codelineno-577-3) optional arguments: [](#__codelineno-577-4)   -h, --help            show this help message and exit [](#__codelineno-577-5)   --file INPUT_FILE     CSV or parquet or JSON formatted file which will be [](#__codelineno-577-6)                         visualized [](#__codelineno-577-7)   --format FILE_FORMAT  Input file format (csv or parquet or json). 'auto' [](#__codelineno-577-8)                         means format will be derived from file extension`\
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
`[](#__codelineno-578-1) rdac watch --help`\
\
`[](#__codelineno-579-1) Commands to watch various streams such sas trace, logs and change notifications by microservices [](#__codelineno-579-2) [](#__codelineno-579-3) Following are valid sub-commands for watch: [](#__codelineno-579-4)   registry                  Start watching updates published by the RDA pod registry [](#__codelineno-579-5)   logs                      Start watching logs produced by the pipelines [](#__codelineno-579-6)   traces                    Start watching traces produced by the pipelines`\
\
****Sub Command: `registry`****\
\
Description: Start watching updates published by the RDA pod registry\
\
`[](#__codelineno-580-1) rdac watch registry --help`\
\
`[](#__codelineno-581-1) usage: watch [-h] [--json] [](#__codelineno-581-2) [](#__codelineno-581-3) optional arguments: [](#__codelineno-581-4)   -h, --help  show this help message and exit [](#__codelineno-581-5)   --json      Print detailed information in JSON format instead of tabular [](#__codelineno-581-6)               format`\
\
*   Following is the syntax for **watch registry**\
\
`[](#__codelineno-582-1) rdac watch registry`\
\
Example Output\
\
 `[](#__codelineno-583-1)  Update Type  Pod Type     Pod ID       Host         Pod Started At [](#__codelineno-583-2) 2023-02-01:13:39:54 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-583-3) 2023-02-01:13:39:54 [1] INFO nats_client Initiallzing SubMgr for pid=1 [](#__codelineno-583-4) 2023-02-01:13:39:54 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-583-5) 2023-02-01:13:39:54 [1] INFO nats_client Creating thread-pool of size: 4, PID=1`\
\
****Sub Command: `logs`****\
\
Description: Start watching logs produced by the pipelines\
\
`[](#__codelineno-584-1) rdac watch logs --help`\
\
`[](#__codelineno-585-1) usage: watch [-h] [--json] [--attr ATTR] [](#__codelineno-585-2) [](#__codelineno-585-3) optional arguments: [](#__codelineno-585-4)   -h, --help   show this help message and exit [](#__codelineno-585-5)   --json       Print detailed information in JSON format instead of tabular [](#__codelineno-585-6)                format [](#__codelineno-585-7)   --attr ATTR  Filter for a specific attribute. Example: --attr [](#__codelineno-585-8)                debug=MyDebugging1`\
\
*   Following is the syntax for **watch logs**\
\
`[](#__codelineno-586-1) rdac watch logs`\
\
Example Output\
\
`[](#__codelineno-587-1) 2023-02-01:13:40:37 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-587-2) 2023-02-01:13:40:37 [1] INFO nats_client Initiallzing SubMgr for pid=1 [](#__codelineno-587-3) 2023-02-01:13:40:37 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-587-4) 2023-02-01:13:40:37 [1] INFO nats_client Creating thread-pool of size: 4, PID=1 [](#__codelineno-587-5)  13:40:37.316 da9d9b28 INFO     executor.py:599:send_to_stream                [Job da9d9b28a0954327a19c941302ce7947] Status update pipeline=reg-predict-parent-pipeline, type=in-progress [](#__codelineno-587-6)  13:40:37.337 da9d9b28 INFO     executor.py:599:send_to_stream                [Job da9d9b28a0954327a19c941302ce7947] Status update pipeline=reg-predict-parent-pipeline, type=in-progress [](#__codelineno-587-7)  13:40:37.355 da9d9b28 INFO     executor.py:599:send_to_stream                [Job da9d9b28a0954327a19c941302ce7947] Status update pipeline=reg-predict-parent-pipeline, type=in-progress [](#__codelineno-587-8)  13:40:38.376 da9d9b28 INFO     executor.py:599:send_to_stream                [Job da9d9b28a0954327a19c941302ce7947] Status update pipeline=reg-predict-parent-pipeline, type=in-progress [](#__codelineno-587-9)  13:40:38.406 da9d9b28 INFO     exec_source.py:277:update_data                Executing inner pipeline 'reg-predict-child-pipeline', previous_pipelines = ['reg-predict-parent-pipeline'] [](#__codelineno-587-10)  13:40:38.407 da9d9b28 INFO     plumbing_pipeline.py:627:execute_sequence     Executing pipeline reg-predict-child-pipeline [](#__codelineno-587-11)  13:40:38.408 da9d9b28 INFO     plumbing_pipeline.py:661:execute_sequence     Executing block reg-predict-child-pipelineb0 [](#__codelineno-587-12)  13:40:38.408 da9d9b28 INFO     executor.py:599:send_to_stream                [Job da9d9b28a0954327a19c941302ce7947] Status update pipeline=reg-predict-parent-pipeline, type=in-progress [](#__codelineno-587-13)  13:40:38.429 da9d9b28 INFO     executor.py:599:send_to_stream                [Job da9d9b28a0954327a19c941302ce7947] Status update pipeline=reg-predict-parent-pipeline, type=in-progress`\
\
****Sub Command: `traces`****\
\
Description: Start watching traces produced by the pipelines\
\
`[](#__codelineno-588-1) rdac watch traces --help`\
\
`[](#__codelineno-589-1) usage: watch [-h] [--json] [--ts] [--attr ATTR] [](#__codelineno-589-2) [](#__codelineno-589-3) optional arguments: [](#__codelineno-589-4)   -h, --help   show this help message and exit [](#__codelineno-589-5)   --json       Print detailed information in JSON format instead of tabular [](#__codelineno-589-6)                format [](#__codelineno-589-7)   --ts         Show timestamp when printing traces in plain text format [](#__codelineno-589-8)   --attr ATTR  Filter for a specific attribute. Example: --attr [](#__codelineno-589-9)                debug=MyDebugging1`\
\
\* Following is the syntax for **watch traces**\
\
`[](#__codelineno-590-1) rdac watch traces`\
\
Example Output 1\
\
`[](#__codelineno-591-1) Host         Pipeline                       JobID    Seq Status      Bot                       Dataframe  Error Message [](#__codelineno-591-2) 2023-02-01:13:41:38 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-591-3) 2023-02-01:13:41:38 [1] INFO nats_client Initiallzing SubMgr for pid=1 [](#__codelineno-591-4) 2023-02-01:13:41:38 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-591-5) 2023-02-01:13:41:38 [1] INFO nats_client Creating thread-pool of size: 4, PID=1 [](#__codelineno-591-6)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:enrich                0x12 [](#__codelineno-591-7)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:add-missing-columns   0x12 [](#__codelineno-591-8)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:eval                  0x14 [](#__codelineno-591-9)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:eval                  0x15 [](#__codelineno-591-10)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:eval                  0x16 [](#__codelineno-591-11)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:eval                  0x17 [](#__codelineno-591-12)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:eval                  0x18 [](#__codelineno-591-13)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:change-time-format    0x18 [](#__codelineno-591-14)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @rn:write-stream          0x18 [](#__codelineno-591-15)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:empty                 0x0 [](#__codelineno-591-16)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:addrow                0x0 [](#__codelineno-591-17)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress #dm:query-persistent-stre 1x2 [](#__codelineno-591-18)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:save                  0x0 [](#__codelineno-591-19)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress @dm:recall                0x0 [](#__codelineno-591-20)  05969789d903 reg-predict-child-pipeline     da9d9b28 605 in-progress *dm:filter                10x12`\
\
\* Following is the syntax for **watch traces**\
\
`[](#__codelineno-592-1) rdac watch traces --json`\
\
Example Output 2\
\
`[](#__codelineno-593-1) 2023-02-10:07:51:23 [1] INFO nats_client Creating new SharedPool ... [](#__codelineno-593-2) 2023-02-10:07:51:23 [1] INFO nats_client Initiallzing SubMgr for pid=1 [](#__codelineno-593-3) 2023-02-10:07:51:23 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-593-4) 2023-02-10:07:51:24 [1] INFO nats_client Creating thread-pool of size: 4, PID=1 [](#__codelineno-593-5) { [](#__codelineno-593-6)   "msg_version": "rda:1", [](#__codelineno-593-7)   "proc_id": "57", [](#__codelineno-593-8)   "proc_info": { [](#__codelineno-593-9)     "hostname": "05969789d903", [](#__codelineno-593-10)     "cpu_percent": 0.0, [](#__codelineno-593-11)     "memory_percent": 1.21, [](#__codelineno-593-12)     "mem_mb": 486.3, [](#__codelineno-593-13)     "create_time": 1675792948.18, [](#__codelineno-593-14)     "cpu_time_user": 111524.55, [](#__codelineno-593-15)     "cpu_time_system": 10933.69, [](#__codelineno-593-16)     "system_cpu_percents": [ [](#__codelineno-593-17)       100.0, [](#__codelineno-593-18)       33.3, [](#__codelineno-593-19)       66.7, [](#__codelineno-593-20)       66.7 [](#__codelineno-593-21)     ] [](#__codelineno-593-22)   }, [](#__codelineno-593-23)   "tenant_id": "ae144f67d2a24034ad6920ace6809763", [](#__codelineno-593-24)   "pod_id": "d08072c8", [](#__codelineno-593-25)   "pod_group": "rda-site-01", [](#__codelineno-593-26)   "group_id": "f4a56ba6388c",`\
\
### Sub Command: `worker-obj-info`\
\
Description: List all worker pods with their current Object Store configuration\
\
`[](#__codelineno-594-1) rdac worker-obj-info --help`\
\
`[](#__codelineno-595-1) Usage: worker-obj-info  [-h] [](#__codelineno-595-2) [](#__codelineno-595-3) optional arguments: [](#__codelineno-595-4)   -h, --help  show this help message and exit`\
\
*   Following is the syntax for **worker-obj-info**\
\
`[](#__codelineno-596-1) rdac worker-obj-info`\
\
Example Output\
\
`[](#__codelineno-597-1) Client is configured with following object store [](#__codelineno-597-2)      Host          : 10.95.122.127:9443 [](#__codelineno-597-3)      Config Cheksum: b469ce79 [](#__codelineno-597-4) [](#__codelineno-597-5) 2023-02-01:08:49:34 [1] INFO nats_client Saving NATS certificate to file: /tmp/nats_cert_custom_461dedd908ef2d75e509377dfe35be02_1.pem [](#__codelineno-597-6) +--------------+----------+-------------+--------------------+--------------------------------+ [](#__codelineno-597-7) | Host         | ID       | Group       | Object Store       | Object Store Config Checksum   | [](#__codelineno-597-8) |--------------+----------+-------------+--------------------+--------------------------------| [](#__codelineno-597-9) | 05969789d903 | a92cd27b | rda-site-01 | 10.95.122.127:9443 | b469ce79                       | [](#__codelineno-597-10) +--------------+----------+-------------+--------------------+--------------------------------+`\
\
### Sub Command: `write-stream`\
\
Description: Write data to the specified stream\
\
`[](#__codelineno-598-1) Usage: write-stream  [-h] --name STREAM_NAME --data DATA [--delay DELAY] [--compress] [](#__codelineno-598-2) [](#__codelineno-598-3) optional arguments: [](#__codelineno-598-4)   -h, --help          show this help message and exit [](#__codelineno-598-5)   --name STREAM_NAME  Stream name to write to [](#__codelineno-598-6)   --data DATA         File containing either single JSON dict or a list [](#__codelineno-598-7)   --delay DELAY       Delay between each publish message [](#__codelineno-598-8)   --compress          Enable compression of the data`\
\
Was this page helpful?\
\
Thanks for your feedback!\
\
Thanks for your feedback!