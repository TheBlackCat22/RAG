 



Guide to Install and Configure RDA Fabric Edge Services
=======================================================

**1\. Install RDA Fabric Edge Services**
----------------------------------------

**RDA Worker:**

RDA worker nodes are stateless data processing entities that can be installed closed to the source of data generation (ex: on-prem/enterprise/edge sites etc.). Worker nodes execute bots and pipelines and communicate with the RDAF platform that is responsible for scheduling and orchestrating jobs (pipelines) across various worker nodes.

Using worker nodes you can ingest and process/transform data locally without having to send all the data to centralized locations like an analytics platform or data warehouse. Two or more worker nodes in one environment can work as a group for load balancing and scale. RDAF platform can orchestrate data sharing or routing among worker nodes in distributed environments (ex: Worker nodes in edge location exchange data with workers in DC or workers in cloud).

Workers are essentially containerized service nodes and can be installed using Docker-compose or in a Kubernetes environment. Workers are typically installed on VMs that are located on-premises / cloud / edge environments.

**RDA Event Gateway:**

RDA Event Gateway is a type of **RDA Agent** that can send streaming data to the RDA Fabric platform. If user wants to send logs/events in real-time to the RDAF platform, users can install Event Gateway in their local environment and configure event sources to send data to Event Gateway.

Similar to RDA worker nodes, event gateways are also containerized services and can be installed using Docker-compose or in a Kubernetes environment. RDA event gateways are typically installed on VMs that are located on-premises / cloud / edge environments.

*   **Log Sources:** For instance, to send syslogs from your Linux servers to the RDA platform, you can install Event Gateway and configure rsyslog on your Linux servers to send data to Event Gateway, which in turn can send data to the RDAF platform.
    
*   **Existing Log Shippers:** Users can also use existing log shippers like **Splunk Universal Forwarder**, **Elasticsearch beats**, **Fluentd**, **rsyslog**, **syslog-ng**, etc. to route / send data to Event Gateway.
    
*   **Endpoints:** Event Gateway supports endpoints and each endpoint is configured to send data to a stream on RDAF platform. For example, you can configure an endpoint with a port and protocol/type (ex: TCP/syslog) and all syslog sources can send data to that endpoint.
    

**RDA Edge Collector :**

RDA Edge Collector is a type of RDA agent that can discover and collect IT asset data in an agentless manner and send the collected data to the RDA Fabric platform. Edge Collector agent is primarily used to discover the IT assets (i.e. Servers, Switches, Routers, Firewall, Load Balancers, Storage Arrays etc.) that provide inventory data over SNMP and SSH protocols.

Similar to RDA worker & event gateway, edge collectors are also containerized services and can be installed using Docker-compose or in a Kubernetes environment. RDA edge collectors are typically installed on VMs that are located on-premises / cloud / edge environments.

### **1.1 RDA Worker Installation**

**Prerequisites:**

*   Linux OS
*   Memory - 8GB
*   Disk - 50GB
*   Python 3.7.4 or above
*   Docker container runtime environment (18.09.2 or above)
*   Docker-compose utility (1.27.x or above)

**Installation Steps:**

**Step-1:**

The RDA worker node registers and communicates with the RDAF platform using a configuration file that contains your tenant ID, data fabric access tokens, and object storage credentials.

Download RDA Fabric Configuration from the portal by going to `Configuration --> RDA Administration --> Network` and copy it to the local filesystem where the worker node is going to be installed.

*   Save the file as `rda_network_config.json`

![RDAFNetworkConfig](https://bot-docs.cloudfabrix.io/images/rda-network-config.png)

*   Create the below directory structure

``[](#__codelineno-0-1) sudo mkdir -p /opt/rdaf/network_config [](#__codelineno-0-2) sudo mkdir -p /opt/rdaf/worker/config [](#__codelineno-0-3) sudo mkdir -p /opt/rdaf/worker/logs [](#__codelineno-0-4) sudo chown -R `id -u`:`id -g` /opt/rdaf``

*   Copy the downloaded RDA Fabric configuration file as shown below.

`[](#__codelineno-1-1) cp rda_network_config.json /opt/rdaf/network_config/rda_network_config.json`

*   Create **common.yml** file for RDA Worker to configure logger settings as shown below.

`[](#__codelineno-2-1) cd /opt/rdaf/worker/config [](#__codelineno-2-2) [](#__codelineno-2-3) cat > common.yml << 'EOF' [](#__codelineno-2-4) version: 1 [](#__codelineno-2-5) disable_existing_loggers: false [](#__codelineno-2-6) formatters: [](#__codelineno-2-7)   standard: [](#__codelineno-2-8)     format: "%(asctime)s %(levelname)s %(module)s - PID=%(process)s %(message)s" [](#__codelineno-2-9) handlers: [](#__codelineno-2-10)   console: [](#__codelineno-2-11)     class: logging.StreamHandler [](#__codelineno-2-12)     level: INFO [](#__codelineno-2-13)     formatter: standard [](#__codelineno-2-14)     stream: ext://sys.stdout [](#__codelineno-2-15)   file_handler: [](#__codelineno-2-16)     class: logging.handlers.RotatingFileHandler [](#__codelineno-2-17)     level: INFO [](#__codelineno-2-18)     formatter: standard [](#__codelineno-2-19)     filename: /logs/${pod_type}-${pod_id}.log [](#__codelineno-2-20)     maxBytes: 10485760 # 10MB [](#__codelineno-2-21)     backupCount: 5 [](#__codelineno-2-22)     encoding: utf8 [](#__codelineno-2-23) root: [](#__codelineno-2-24)   level: INFO [](#__codelineno-2-25)   handlers: [console, file_handler] [](#__codelineno-2-26)   propogate: yes [](#__codelineno-2-27) [](#__codelineno-2-28) EOF`

**Step-2:** **Docker Login**

Run the below command to create and save the docker login session into CloudFabrix's secure docker repository.

`[](#__codelineno-3-1) docker login -u='readonly' -p='readonly' cfxregistry.cloudfabrix.io`

**Step-3:** **Create Docker Compose File**

Create docker compose configuration file for RDA Worker as shown below.

Tip

**Note-1:** Optionally change the worker group name (also known as **Site**) in the docker-compose file by updating the WORKER\_GROUP value. In this example, the worker group name is specified as rda\_worker\_group01

**Note-2:** Adjust **mem\_limit** and **memswap\_limit** as per the workload requirements. In the below configuration, these parameters are set to **16GB**

`[](#__codelineno-4-1) cd /opt/rdaf/worker [](#__codelineno-4-2) [](#__codelineno-4-3) cat > rda-worker-docker-compose.yml <<EOF [](#__codelineno-4-4) version: '3.1' [](#__codelineno-4-5) services: [](#__codelineno-4-6)   rda_worker: [](#__codelineno-4-7)     image: cfxregistry.cloudfabrix.io/ubuntu-rda-worker-all:daily [](#__codelineno-4-8)     restart: always [](#__codelineno-4-9)     network_mode: host [](#__codelineno-4-10)     mem_limit: 16G [](#__codelineno-4-11)     memswap_limit: 16G [](#__codelineno-4-12)     shm_size: 1gb [](#__codelineno-4-13)     volumes: [](#__codelineno-4-14)     - /opt/rdaf/network_config:/network_config [](#__codelineno-4-15)     - /opt/rdaf/worker/config:/loggingConfigs [](#__codelineno-4-16)     - /opt/rdaf/worker/logs:/logs [](#__codelineno-4-17)     logging: [](#__codelineno-4-18)       driver: "json-file" [](#__codelineno-4-19)       options: [](#__codelineno-4-20)         max-size: "25m" [](#__codelineno-4-21)         max-file: "5" [](#__codelineno-4-22)     environment: [](#__codelineno-4-23)       RESOURCE_NAME: [](#__codelineno-4-24)       RDA_NETWORK_CONFIG: /network_config/rda_network_config.json [](#__codelineno-4-25)       LOGGER_CONFIG_FILE: /loggingConfigs/common.yml [](#__codelineno-4-26)       WORKER_GROUP: rda_worker_group01 [](#__codelineno-4-27)       LABELS: name=rda_worker_01 [](#__codelineno-4-28)       RDA_SELF_HEALTH_RESTART_AFTER_FAILURES: 3 [](#__codelineno-4-29)       CAPACITY_FILTER: mem_percent < 95 [](#__codelineno-4-30) [](#__codelineno-4-31) EOF`

Tip

If you are in an HTTP Proxy environment, please configure the HTTP Proxy environment variables as shown below. If there are any target endpoint(s) that don't need to go through the HTTP Proxy, please specify their IP addresses or FQDN names as comma-separated values under the `no_proxy` and `NO_PROXY` environment variables.

`[](#__codelineno-5-1) version: '3.1' [](#__codelineno-5-2) services: [](#__codelineno-5-3)   rda_worker: [](#__codelineno-5-4)     image: cfxregistry.cloudfabrix.io/ubuntu-rda-worker-all:daily [](#__codelineno-5-5)     restart: always [](#__codelineno-5-6)     network_mode: host [](#__codelineno-5-7)     mem_limit: 16G [](#__codelineno-5-8)     memswap_limit: 16G [](#__codelineno-5-9)     shm_size: 1gb [](#__codelineno-5-10)     volumes: [](#__codelineno-5-11)     - /opt/rdaf/network_config:/network_config [](#__codelineno-5-12)     - /opt/rdaf/worker/config:/loggingConfigs [](#__codelineno-5-13)     - /opt/rdaf/worker/logs:/logs [](#__codelineno-5-14)     logging: [](#__codelineno-5-15)       driver: "json-file" [](#__codelineno-5-16)       options: [](#__codelineno-5-17)         max-size: "25m" [](#__codelineno-5-18)         max-file: "5" [](#__codelineno-5-19)     environment: [](#__codelineno-5-20)       RESOURCE_NAME: [](#__codelineno-5-21)       RDA_NETWORK_CONFIG: /network_config/rda_network_config.json [](#__codelineno-5-22)       LOGGER_CONFIG_FILE: /loggingConfigs/common.yml [](#__codelineno-5-23)       WORKER_GROUP: rda_worker_group01 [](#__codelineno-5-24)       LABELS: name=rda_worker_01 [](#__codelineno-5-25)       RDA_SELF_HEALTH_RESTART_AFTER_FAILURES: 3 [](#__codelineno-5-26)       CAPACITY_FILTER: mem_percent < 95 [](#__codelineno-5-27)       http_proxy: "http://user:password@192.168.122.107:3128" [](#__codelineno-5-28)       https_proxy: "http://user:password@192.168.122.107:3128" [](#__codelineno-5-29)       no_proxy: "127.0.0.1" [](#__codelineno-5-30)       HTTP_PROXY: "http://user:password@192.168.122.107:3128" [](#__codelineno-5-31)       HTTPS_PROXY: "http://user:password@192.168.122.107:3128" [](#__codelineno-5-32)       NO_PROXY: "127.0.0.1"`

Tip

**Note-1:** RDA worker(s) communicates with RDA Fabric that is running in cloud or on-premise datacenter over ports 4222/TCP & 9443/TCP. Please make sure RDA worker(s) has outbound network access over these network ports. In addition, make sure RDA Fabric is configured to allow inbound network traffic for the same ports to accept the traffic from RDA worker(s).

**Note-2:** Please verify **rda\_network\_config.json** is configured with publicly accessible IP/FQDN of RDA Fabric for NATs and Minio endpoints.

**Step-4:** **Bring Up RDA Worker**

`[](#__codelineno-6-1) cd /opt/rdaf/worker [](#__codelineno-6-2) [](#__codelineno-6-3) docker-compose -f rda-worker-docker-compose.yml pull  [](#__codelineno-6-4) docker-compose -f rda-worker-docker-compose.yml up -d`

Note

If Ubuntu version is v22.04.2 LTS or above & Docker Compose version is v2.16.0 or above, Use the following Commands mentioned below

`[](#__codelineno-7-1) cd /opt/rdaf/worker [](#__codelineno-7-2) [](#__codelineno-7-3) docker compose -f rda-worker-docker-compose.yml pull [](#__codelineno-7-4) docker compose -f rda-worker-docker-compose.yml up -d`   

**Step-5:** **Check Worker Status**

Check worker node status using `docker ps` command and ensure that worker is up and running, without any restarts. If you see that the worker is restarting, make sure you copied the RDA network config file to the correct location.

`[](#__codelineno-8-1) docker ps | grep worker`

**Step-6:** **Verify RDA Worker in RDA Fabric portal**

A newly installed worker will authenticate with the RDA Fabric platform and it will show up in RDA Fabric portal under `Fabric Health --> Workers`.

**Step-7:** **Verify Worker using RDA Client (rdac) utility**

If you have installed RDA Client (rdac) command line utility, you can also verify newly created worker using `rdac pods` command.

### **1.2 RDA Event Gateway Installation**

**Prerequisites:**

*   Linux OS
*   Memory - 8GB
*   Disk - 50GB
*   Python 3.7.4 or above
*   Docker container runtime environment (18.09.2 or above)
*   Docker-compose utility (1.27.x or above)

#### **1.2.1 Installation Steps**

**Step-1:**

The RDA event gateway registers and communicates with the RDA Fabirc platform using a configuration file that contains your tenant ID, data fabric access tokens, and object storage credentials.

Download RDA Fabric Configuration from the portal by going to `Configuration --> Fabric Configuration --> RDA network configuration` and copy it to the local filesystem where the event gateway is going to be installed.

*   Save the file as `rda_network_config.json`

![RDAFNetworkConfig](https://bot-docs.cloudfabrix.io/images/rda-network-config.png)

*   Create the below directory structure

``[](#__codelineno-9-1) sudo mkdir -p /opt/rdaf/network_config [](#__codelineno-9-2) sudo mkdir -p /opt/rdaf/event_gateway/config/main [](#__codelineno-9-3) sudo mkdir -p /opt/rdaf/event_gateway/config/snmptrap [](#__codelineno-9-4) sudo mkdir -p /opt/rdaf/event_gateway/certs [](#__codelineno-9-5) sudo mkdir -p /opt/rdaf/event_gateway/logs [](#__codelineno-9-6) sudo mkdir -p /opt/rdaf/event_gateway/log_archive [](#__codelineno-9-7) sudo chown -R `id -u`:`id -g` /opt/rdaf``

*   Copy the downloaded RDA Fabric configuration file as shown below.

`[](#__codelineno-10-1) cp rda_network_config.json /opt/rdaf/network_config/rda_network_config.json`

**Step-2:** **Docker Login**

Run the below command to create and save the docker login session into CloudFabrix's secure docker repository.

`[](#__codelineno-11-1) docker login -u='readonly' -p='readonly' cfxregistry.cloudfabrix.io`

**Step-3:** **Create Docker Compose File**

Create docker compose configuration file for RDA event gateway as shown below.

Info

**Note:** Optionally change the agent group name in the docker-compose file by updating the AGENT\_GROUP value. In this example, the agent group name is specified as `event_gateway_site01`

`[](#__codelineno-12-1) cd /opt/rdaf/event_gateway [](#__codelineno-12-2) [](#__codelineno-12-3) cat > event-gateway-docker-compose.yml <<EOF [](#__codelineno-12-4) version: '3.1' [](#__codelineno-12-5) services: [](#__codelineno-12-6)   rda_event_gateway: [](#__codelineno-12-7)     image: cfxregistry.cloudfabrix.io/ubuntu-rda-event-gateway:daily [](#__codelineno-12-8)     restart: always [](#__codelineno-12-9)     network_mode: host [](#__codelineno-12-10)     mem_limit: 6G [](#__codelineno-12-11)     memswap_limit: 6G [](#__codelineno-12-12)     volumes: [](#__codelineno-12-13)     - /opt/rdaf/network_config:/network_config [](#__codelineno-12-14)     - /opt/rdaf/event_gateway/config:/event_gw_config [](#__codelineno-12-15)     - /opt/rdaf/event_gateway/certs:/certs [](#__codelineno-12-16)     - /opt/rdaf/event_gateway/logs:/logs [](#__codelineno-12-17)     - /opt/rdaf/event_gateway/log_archive:/tmp/log_archive [](#__codelineno-12-18)     logging: [](#__codelineno-12-19)       driver: "json-file" [](#__codelineno-12-20)       options: [](#__codelineno-12-21)         max-size: "25m" [](#__codelineno-12-22)         max-file: "5" [](#__codelineno-12-23)     environment: [](#__codelineno-12-24)       RDA_NETWORK_CONFIG: /network_config/rda_network_config.json [](#__codelineno-12-25)       EVENT_GW_MAIN_CONFIG: /event_gw_config/main/main.yml [](#__codelineno-12-26)       EVENT_GW_SNMP_TRAP_CONFIG: /event_gw_config/snmptrap/trap_template.json [](#__codelineno-12-27)       EVENT_GW_SNMP_TRAP_ALERT_CONFIG: /event_gw_config/snmptrap/trap_to_alert_go.yaml [](#__codelineno-12-28)       AGENT_GROUP: event_gateway_site01 [](#__codelineno-12-29)       EVENT_GATEWAY_CONFIG_DIR: /event_gw_config [](#__codelineno-12-30)       LOGGER_CONFIG_FILE: /event_gw_config/main/logging.yml [](#__codelineno-12-31)       RDA_SELF_HEALTH_RESTART_AFTER_FAILURES: 3 [](#__codelineno-12-32)     entrypoint: ["/docker-entry-point.sh"] [](#__codelineno-12-33) EOF`

**Step-4:** **Create SNMP Trap Configuration File**

Info

**Note:** Download \* [trap\_to\_alert\_go.yaml](https://macaw-amer.s3.amazonaws.com/releases/rda-edge-services/event_gateway/trap_to_alert_go.yaml "Trap_To_Alert File")
 file and copy to /opt/rdaf/event\_gateway/config/snmptrap directory

`[](#__codelineno-13-1) cd /opt/rdaf/event_gateway/config/snmptrap/ [](#__codelineno-13-2) [](#__codelineno-13-3) wget https://macaw-amer.s3.amazonaws.com/releases/rda-edge-services/event_gateway/trap_to_alert_go.yaml`

`[](#__codelineno-14-1) cd /opt/rdaf/event_gateway/config/snmptrap [](#__codelineno-14-2) [](#__codelineno-14-3) cat > trap_template.json <<EOF [](#__codelineno-14-4) { [](#__codelineno-14-5)     "1.3.6.1.6.3.1.1.5.4": { [](#__codelineno-14-6)         "action": "forward", [](#__codelineno-14-7)         "template": { [](#__codelineno-14-8)             "message": "Link status changed to up for interface '{{vbValue[3]}}' for device {{ipAddress}}", [](#__codelineno-14-9)             "device": "{{ipAddress}}", [](#__codelineno-14-10)             "trapOid": "{{trapOid}}", [](#__codelineno-14-11)             "snmpVersion": "{{snmpVersion}}", [](#__codelineno-14-12)             "timestamp": "{{timestamp}}", [](#__codelineno-14-13)             "timestampEpoch": "{{timestampEpoch}}" [](#__codelineno-14-14)         } [](#__codelineno-14-15)     }, [](#__codelineno-14-16)     "1.3.6.1.6.3.1.1.5.3": { [](#__codelineno-14-17)         "action": "forward", [](#__codelineno-14-18)         "template": { [](#__codelineno-14-19)             "message": "Link status changed to down for interface '{{vbValue[3]}}' for device {{ipAddress}}", [](#__codelineno-14-20)             "device": "{{ipAddress}}", [](#__codelineno-14-21)             "trapOid": "{{trapOid}}", [](#__codelineno-14-22)             "snmpVersion": "{{snmpVersion}}", [](#__codelineno-14-23)             "timestamp": "{{timestamp}}", [](#__codelineno-14-24)             "timestampEpoch": "{{timestampEpoch}}" [](#__codelineno-14-25)         } [](#__codelineno-14-26)     } [](#__codelineno-14-27) } [](#__codelineno-14-28) EOF`

**Step-5:** **Bring Up Event Gateway**

`[](#__codelineno-15-1) cd /opt/rdaf/event_gateway [](#__codelineno-15-2) [](#__codelineno-15-3) docker-compose -f event-gateway-docker-compose.yml pull  [](#__codelineno-15-4) docker-compose -f event-gateway-docker-compose.yml up -d`

**Step-6:** **Check event gateway status**

Check event gateway service status using `docker ps` command and ensure that event gateway is up and running, without any restarts. If you see that the event gateway is restarting, make sure you copied the RDA network configuration file to the correct location.

`[](#__codelineno-16-1) docker ps | grep gateway`

**Step-7:** **Verify RDA Event Gateway in RDA Fabric portal**

A newly installed event gateway will authenticate with the RDA Fabric platform and it will show up in RDA Fabric portal under `Configuration --> Fabric Components --> Agents --> View Details`.

**Step-8:** **Verify RDA Event Gateway using RDA Client (rdac) utility**

If you have installed RDA Client (rdac) command line utility, you can also verify newly created event gateway using `rdac agents` command.

#### **1.2.2 Installation Steps - HA**

**Nginx Load Balancer Deployment Steps**

Configuration Diagram for **Event GW** → **Nginx LB** → **CFX Platform**

![Configiration_Diagram](https://bot-docs.cloudfabrix.io/images/configuration_diagram.png)

**Prerequisites**

**1**.) Need 2 VMs to configure the Nginx Load Balancer

**2**.) CFX Event Gateways

*   Instructions on How to install Nginx Load Balancer for Event Gateway and Configure Keepalived for LB High Availability (active/passive)

**Step-1:** **Login to the LB VMs and follow the steps on each LB VM**

*   Create the required folder and file.

`[](#__codelineno-17-1) mkdir  $HOME/conf [](#__codelineno-17-2) sudo vi $HOME/conf/nginx.conf`

**nginx.conf**

`[](#__codelineno-18-1) worker_rlimit_nofile 1000000; [](#__codelineno-18-2) worker_processes auto; [](#__codelineno-18-3) events { [](#__codelineno-18-4)   worker_connections 50000; [](#__codelineno-18-5) } [](#__codelineno-18-6) [](#__codelineno-18-7) stream { [](#__codelineno-18-8)  upstream rda-eg-udp { [](#__codelineno-18-9)   hash $remote_addr consistent; [](#__codelineno-18-10)   zone  dns_zone 64k; [](#__codelineno-18-11)   server 192.168.1.180:514 fail_timeout=300s max_fails=1; [](#__codelineno-18-12)   server 192.168.1.63:514 fail_timeout=300s max_fails=1; [](#__codelineno-18-13)  } [](#__codelineno-18-14) [](#__codelineno-18-15)  server { [](#__codelineno-18-16)   listen 514; [](#__codelineno-18-17)   proxy_pass rda-eg-udp; [](#__codelineno-18-18)   proxy_timeout 1s; [](#__codelineno-18-19)   proxy_protocol on; [](#__codelineno-18-20)   proxy_connect_timeout 1s; [](#__codelineno-18-21)   error_log /var/log/nginx/tcp_514_error.log; [](#__codelineno-18-22)  } [](#__codelineno-18-23) [](#__codelineno-18-24)   server { [](#__codelineno-18-25)   listen 514 udp; [](#__codelineno-18-26)   proxy_pass rda-eg-udp; [](#__codelineno-18-27)   proxy_responses 0; [](#__codelineno-18-28)   proxy_timeout 120s; [](#__codelineno-18-29)   proxy_protocol on; [](#__codelineno-18-30)   proxy_buffer_size 10240k; [](#__codelineno-18-31)   error_log /var/log/nginx/udp_error.log; [](#__codelineno-18-32)  } [](#__codelineno-18-33)  upstream rda-eg-trap-udp { [](#__codelineno-18-34)   hash $remote_addr consistent; [](#__codelineno-18-35)   zone  dns_zone 64k; [](#__codelineno-18-36)   server 192.168.1.180:162 fail_timeout=300s max_fails=1; [](#__codelineno-18-37)   server 192.168.1.63:162 fail_timeout=300s max_fails=1; [](#__codelineno-18-38)  } [](#__codelineno-18-39) [](#__codelineno-18-40)  server { [](#__codelineno-18-41)   listen 162 udp; [](#__codelineno-18-42)   proxy_pass rda-eg-trap-udp; [](#__codelineno-18-43)   proxy_responses 0; [](#__codelineno-18-44)   proxy_timeout 120s; [](#__codelineno-18-45)   proxy_protocol on; [](#__codelineno-18-46)   proxy_buffer_size 10240k; [](#__codelineno-18-47)   error_log /var/log/nginx/udp_trap_error.log; [](#__codelineno-18-48)  } [](#__codelineno-18-49) [](#__codelineno-18-50)  server { [](#__codelineno-18-51)   listen 162; [](#__codelineno-18-52)   proxy_pass rda-eg-trap-udp; [](#__codelineno-18-53)   proxy_timeout 1s; [](#__codelineno-18-54)   proxy_protocol on; [](#__codelineno-18-55)   proxy_connect_timeout 1s; [](#__codelineno-18-56)   error_log /var/log/nginx/tcp_162_error.log; [](#__codelineno-18-57)  } [](#__codelineno-18-58) [](#__codelineno-18-59) } [](#__codelineno-18-60) [](#__codelineno-18-61) http { [](#__codelineno-18-62)  server { [](#__codelineno-18-63)   listen 9080 default_server; [](#__codelineno-18-64)   access_log off; [](#__codelineno-18-65) [](#__codelineno-18-66)   location /lb-status { [](#__codelineno-18-67)       return 200 'OK'; [](#__codelineno-18-68)       add_header Content-Type text/plain; [](#__codelineno-18-69)   } [](#__codelineno-18-70)   location /nginx_status { [](#__codelineno-18-71)     stub_status; [](#__codelineno-18-72)   } [](#__codelineno-18-73)  } [](#__codelineno-18-74) }`

Note

The lines that are highlighted above presume two event gateways. If a user has more event gateways, add additional lines to the upstream configuration for each upstream mentioned above. At least two is the recommended number.

*   Deploy nginx LB using the docker-compose

`[](#__codelineno-19-1) cat > nginx-docker-compose.yml <<EOF [](#__codelineno-19-2) version: '3' [](#__codelineno-19-3) [](#__codelineno-19-4) [](#__codelineno-19-5) services: [](#__codelineno-19-6)    nginx: [](#__codelineno-19-7)      image: nginx:1.25 [](#__codelineno-19-8)      container_name: nginx [](#__codelineno-19-9)      ports: [](#__codelineno-19-10)        - "514:514/udp" [](#__codelineno-19-11)        - "514:514/tcp" [](#__codelineno-19-12)        - "162:162/udp" [](#__codelineno-19-13)        - "162:162/tcp" [](#__codelineno-19-14)        - "9080:9080/tcp" [](#__codelineno-19-15)      volumes: [](#__codelineno-19-16)        - ./conf/nginx.conf:/etc/nginx/nginx.conf [](#__codelineno-19-17)        - /opt/rdaf/logs/nginx:/var/log/nginx [](#__codelineno-19-18)      restart: always [](#__codelineno-19-19) EOF`

`[](#__codelineno-20-1) docker-compose -f nginx-docker-compose.yml pull [](#__codelineno-20-2) docker-compose -f nginx-docker-compose.yml up -d`

**Step-2:** **Setup keepalived on LB VM 1**

*   Create `master-keepalived.conf` file

`[](#__codelineno-21-1) sudo vi $HOME/master-keepalived.conf`

`[](#__codelineno-22-1) global_defs { [](#__codelineno-22-2)   script_user root [](#__codelineno-22-3)   enable_script_security [](#__codelineno-22-4) } [](#__codelineno-22-5) vrrp_script chk_health { [](#__codelineno-22-6)   script "/usr/local/bin/nginx_healthcheck.sh" [](#__codelineno-22-7)   interval 2 [](#__codelineno-22-8) } [](#__codelineno-22-9) vrrp_instance rdaf_vrrp_ext { [](#__codelineno-22-10)   interface ens160 [](#__codelineno-22-11)   state MASTER [](#__codelineno-22-12)   virtual_router_id 11 [](#__codelineno-22-13)   priority 255 [](#__codelineno-22-14)   virtual_ipaddress { [](#__codelineno-22-15)     192.168.102.71/24 [](#__codelineno-22-16)   } [](#__codelineno-22-17)   track_script { [](#__codelineno-22-18)     chk_health [](#__codelineno-22-19)   } [](#__codelineno-22-20)   authentication { [](#__codelineno-22-21)     auth_type PASS [](#__codelineno-22-22)     auth_pass 1a2b3c4d [](#__codelineno-22-23)   } [](#__codelineno-22-24) }`

Note

Update/replace the virtual IP in the above file where highlighted as per the environment.

*   Copy the file to the path below.

`[](#__codelineno-23-1) sudo cp $HOME/master-keepalived.conf /etc/keepalived/keepalived.conf`

*   Create the `nginx_healthcheck.sh` and copy the file in given path `Nginx_healthcheck.sh`

`[](#__codelineno-24-1) #!/bin/bash [](#__codelineno-24-2) [](#__codelineno-24-3) HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:9080/lb-status) [](#__codelineno-24-4) [](#__codelineno-24-5) if [[ $HTTP_STATUS -ge 200 && $HTTP_STATUS -lt 300 ]]; then [](#__codelineno-24-6)     curl -s -o /dev/null -w "%{http_code}" http://localhost:514 # dummy TCP request [](#__codelineno-24-7)     curl -s -o /dev/null -w "%{http_code}" http://localhost:162 # dummy TCP request [](#__codelineno-24-8)     exit 0  # Success [](#__codelineno-24-9) else [](#__codelineno-24-10)     curl -s -o /dev/null -w "%{http_code}" http://localhost:514 # dummy TCP request [](#__codelineno-24-11)     curl -s -o /dev/null -w "%{http_code}" http://localhost:162 # dummy TCP request [](#__codelineno-24-12)     exit 1  # Failure [](#__codelineno-24-13) fi`

*   **copy** `nginx_healthcheck.sh` to `/usr/local/bin`

`[](#__codelineno-25-1) chmod 777 nginx_healthcheck.sh [](#__codelineno-25-2) sudo cp nginx_healthcheck.sh /usr/local/bin`

*   Usage of the script

`[](#__codelineno-26-1) ./nginx_healthcheck.sh`

*   start keepalived

`[](#__codelineno-27-1) sudo systemctl enable keepalived [](#__codelineno-27-2) sudo systemctl restart keepalived [](#__codelineno-27-3) sudo systemctl status keepalived`

*   To check the virtual IP in the output, run the below command.

`[](#__codelineno-28-1) ip add show`

*   Configure the firewalls using the below commands.

 `[](#__codelineno-29-1)  sudo ufw allow from 224.0.0.18 [](#__codelineno-29-2)  sudo ufw allow to 224.0.0.18 [](#__codelineno-29-3)  sudo ufw allow 514/udp [](#__codelineno-29-4)  sudo ufw allow 514/tcp [](#__codelineno-29-5)  sudo ufw allow 162/udp [](#__codelineno-29-6)  sudo ufw allow 162/tcp [](#__codelineno-29-7)  sudo ufw allow 9080/tcp [](#__codelineno-29-8)  sudo ufw reload`

Note

If there are any changes,the necessary ports must be updated accordingly.

*   Check if LB is accessible via virtual IP by running the following command

`[](#__codelineno-30-1) curl http://<virtual IP>:9080/lb-status`

Note

The command above should return as 'OK'

**Step-3:** **Setup keepalived on LB VM 2**

*   Create `backup-keepalived.conf` file.

`[](#__codelineno-31-1) sudo vi $HOME/backup-keepalived.conf`

`[](#__codelineno-32-1) global_defs { [](#__codelineno-32-2)   script_user root [](#__codelineno-32-3)   enable_script_security [](#__codelineno-32-4) } [](#__codelineno-32-5) vrrp_script chk_health { [](#__codelineno-32-6)   script "/usr/bin/pgrep nginx" [](#__codelineno-32-7)   interval 1 [](#__codelineno-32-8) } [](#__codelineno-32-9) vrrp_instance rdaf_vrrp_ext { [](#__codelineno-32-10)   interface ens160 [](#__codelineno-32-11)   state BACKUP [](#__codelineno-32-12)   virtual_router_id 11 [](#__codelineno-32-13)   priority 100 [](#__codelineno-32-14)   virtual_ipaddress { [](#__codelineno-32-15)     192.168.102.71/24 [](#__codelineno-32-16)   } [](#__codelineno-32-17)   track_script { [](#__codelineno-32-18)     chk_health [](#__codelineno-32-19)   } [](#__codelineno-32-20)   authentication { [](#__codelineno-32-21)     auth_type PASS [](#__codelineno-32-22)     auth_pass 1a2b3c4d [](#__codelineno-32-23)   } [](#__codelineno-32-24) }`

Note

update/replace the highlighted virtual IP in the above file. It should be the same as the previous config that was in LB1

*   Copy the file to the path below

`[](#__codelineno-33-1) sudo cp $HOME/backup-keepalived.conf /etc/keepalived/keepalived.conf`

*   Create the `nginx_healthcheck.sh` and copy the file in given path `Nginx_healthcheck.sh`

`[](#__codelineno-34-1) #!/bin/bash [](#__codelineno-34-2) [](#__codelineno-34-3) HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:9080/lb-status) [](#__codelineno-34-4) [](#__codelineno-34-5) if [[ $HTTP_STATUS -ge 200 && $HTTP_STATUS -lt 300 ]]; then [](#__codelineno-34-6)     curl -s -o /dev/null -w "%{http_code}" http://localhost:514 # dummy TCP request [](#__codelineno-34-7)     curl -s -o /dev/null -w "%{http_code}" http://localhost:162 # dummy TCP request [](#__codelineno-34-8)     exit 0  # Success [](#__codelineno-34-9) else [](#__codelineno-34-10)     curl -s -o /dev/null -w "%{http_code}" http://localhost:514 # dummy TCP request [](#__codelineno-34-11)     curl -s -o /dev/null -w "%{http_code}" http://localhost:162 # dummy TCP request [](#__codelineno-34-12)     exit 1  # Failure [](#__codelineno-34-13) fi`

*   **copy** `nginx_healthcheck.sh` to `/usr/local/bin`

`[](#__codelineno-35-1) chmod 777 nginx_healthcheck.sh [](#__codelineno-35-2) sudo cp nginx_healthcheck.sh /usr/local/bin`

*   Usage of the script

`[](#__codelineno-36-1) ./nginx_healthcheck.sh`

*   start keepalived

`[](#__codelineno-37-1) sudo systemctl enable keepalived [](#__codelineno-37-2) sudo systemctl restart keepalived [](#__codelineno-37-3) sudo systemctl status keepalived`

*   To check the virtual IP in the output, run the below command.

`[](#__codelineno-38-1) ip add show`

Note

The Virtual IP will not show until LB2 has become active.

*   Configure the firewalls using the below commands.

 `[](#__codelineno-39-1)  sudo ufw allow from 224.0.0.18 [](#__codelineno-39-2)  sudo ufw allow to 224.0.0.18 [](#__codelineno-39-3)  sudo ufw allow 514/udp [](#__codelineno-39-4)  sudo ufw allow 514/tcp [](#__codelineno-39-5)  sudo ufw allow 162/udp [](#__codelineno-39-6)  sudo ufw allow 162/tcp [](#__codelineno-39-7)  sudo ufw allow 9080/tcp [](#__codelineno-39-8)  sudo ufw reload`

Note

If there are any changes,the necessary ports must be updated accordingly.

*   Check if LB is accessible via virtual IP by running the following command

`[](#__codelineno-40-1) curl http://<virtual IP>:9080/lb-status`

Note

The command above should return as 'OK'

**Verification Steps**

Send events to virtual ip instead of event gateway IP; below is an example that you can refer to

`[](#__codelineno-41-1) echo "test message" | nc -u 192.168.102.71 514 -w 1`

#### **1.2.3 SSL Configuration for endpoints**

Run the below command on event gateway to generate self-signed certificate files. Fill in the answers for the below prompts.

`[](#__codelineno-42-1) openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`

*   Country Name (2 letter code)
*   State or Province Name (full name)
*   Locality Name (eg, city)
*   Organization Name (eg, company)
*   Organizational Unit Name (eg, section)
*   Common Name (eg, your name or your server's hostname)
*   Email Address

Above command generates two files under the current working directory, `cert.pem` and `key.pem`

Copy above files to `/opt/rdaf/event_gateway/certs directory`

`[](#__codelineno-43-1) cp cert.pem /opt/rdaf/event_gateway/certs [](#__codelineno-43-2) cp key.pem /opt/rdaf/event_gateway/certs`

#### **1.2.4 Endpoints Configuration**

RDA event gateway support below end point types.

*   **Syslog over TCP:** Recieve syslog events over TCP protocol
*   **Syslog over UDP:** Recieve syslog events over UDP protocol
*   **HTTP:** Receive log events over HTTP protocol
*   **TCP:** Receive log events over TCP protocol
*   **SNMP Traps:** Receive SNMP traps over UDP protocol
*   **Filebeat:** Receive log events over HTTP protocol from log shipping agents such as `filebeat` & `winlogbeat`

Event gateway with the default configuration for each of the above end points as shown below. The endpoint configuration file is located @ `/opt/rdaf/event_gateway/config/endpoint.yml`

`[](#__codelineno-44-1) endpoints: [](#__codelineno-44-2) [](#__codelineno-44-3) # Endpoint - Syslog Log events over TCP protocol [](#__codelineno-44-4) # attrs: <Custom attributes to be added for each log event, provide one or more attributes in key: value format> [](#__codelineno-44-5) # stream: <Write the log events to a Stream within RDA Fabric> [](#__codelineno-44-6) - name: syslog_tcp_events [](#__codelineno-44-7)   enabled: false [](#__codelineno-44-8)   type: syslog_tcp [](#__codelineno-44-9)   port: 5140 [](#__codelineno-44-10)   ssl: false [](#__codelineno-44-11)   ssl_cert_dir: /certs [](#__codelineno-44-12)   attrs: [](#__codelineno-44-13)     site_code: event_gateway_site01 # Site Name / Code where Event gateway is deployed [](#__codelineno-44-14)     archive_name: syslog_events_archive # Log archive name [](#__codelineno-44-15)   stream: "NULL" [](#__codelineno-44-16)   direct_to_stream: syslog_tcp_event_stream [](#__codelineno-44-17) [](#__codelineno-44-18) # Endpoint - Syslog Log events over UDP protocol [](#__codelineno-44-19) # attrs: <Custom attributes to be added for each log event, provide one or more attributes in key: value format> [](#__codelineno-44-20) # stream: <Write the log events to a Stream within RDA Fabric> [](#__codelineno-44-21) - name: syslog_udp_events [](#__codelineno-44-22)   enabled: false [](#__codelineno-44-23)   type: syslog_udp [](#__codelineno-44-24)   port: 5141 [](#__codelineno-44-25)   attrs: [](#__codelineno-44-26)     site_code: event_gateway_site01 # Site Name / Code where Event gateway is deployed [](#__codelineno-44-27)     archive_name: syslog_events_archive # Log archive name [](#__codelineno-44-28)   stream: "NULL" [](#__codelineno-44-29)   direct_to_stream: syslog_udp_event_stream [](#__codelineno-44-30) [](#__codelineno-44-31) # Endpoint - Events over HTTP protocol [](#__codelineno-44-32) # attrs: <Custom attributes to be added for each log event, provide one or more attributes in key: value format> [](#__codelineno-44-33) # stream: <Write the log events to a Stream within RDA Fabric> [](#__codelineno-44-34) - name: http_events [](#__codelineno-44-35)   enabled: false [](#__codelineno-44-36)   type: http [](#__codelineno-44-37)   ssl: false [](#__codelineno-44-38)   ssl_cert_dir: /certs [](#__codelineno-44-39)   content_type: auto [](#__codelineno-44-40)   port: 5142 [](#__codelineno-44-41)   attrs: [](#__codelineno-44-42)     site_code: event_gateway_site01 # Site Name / Code where Event gateway is deployed [](#__codelineno-44-43)     archive_name: http_events_archive # Log archive name [](#__codelineno-44-44)   stream: "NULL" [](#__codelineno-44-45)   direct_to_stream: http_event_stream [](#__codelineno-44-46) [](#__codelineno-44-47) # Endpoint - Events in JSON format over TCP protocol [](#__codelineno-44-48) # attrs: <Custom attributes to be added for each log event, provide one or more attributes in key: value format> [](#__codelineno-44-49) # stream: <Write the log events to a Stream within RDA Fabric> [](#__codelineno-44-50) - name: tcp_json_events [](#__codelineno-44-51)   enabled: false [](#__codelineno-44-52)   type: tcp_json [](#__codelineno-44-53)   ssl: false [](#__codelineno-44-54)   ssl_cert_dir: /certs [](#__codelineno-44-55)   port: 5143 [](#__codelineno-44-56)   attrs: [](#__codelineno-44-57)     site_code: event_gateway_site01 # Site Name / Code where Event gateway is deployed [](#__codelineno-44-58)     archive_name: tcp_json_events_archive # Log archive name [](#__codelineno-44-59)   stream: "NULL" [](#__codelineno-44-60)   direct_to_stream: tcp_json_event_stream [](#__codelineno-44-61) [](#__codelineno-44-62) # Endpoint - Events from Filebeat agent [](#__codelineno-44-63) # type: filebeat - It is applicable for both Filebeat and Winlogbeat log shipping agents [](#__codelineno-44-64) # attrs: <Custom attributes to be added for each log event, provide one or more attributes in key: value format> [](#__codelineno-44-65) # stream: <Write the log events to a Stream within RDA Fabric> [](#__codelineno-44-66) - name: filebeat_events # URL is implicit, http://ip:port/filebeat_events [](#__codelineno-44-67)   type: filebeat [](#__codelineno-44-68)   enabled: false [](#__codelineno-44-69)   ssl: false [](#__codelineno-44-70)   ssl_cert_dir: /certs [](#__codelineno-44-71)   xpack_features: min [](#__codelineno-44-72)   port: 5144 [](#__codelineno-44-73)   attrs: [](#__codelineno-44-74)     site_code: event_gateway_site01 # Site Name / Code where Event gateway is deployed [](#__codelineno-44-75)     archive_name: filebeat_log_events_archive # Log archive name [](#__codelineno-44-76)   stream: "NULL" [](#__codelineno-44-77)   direct_to_stream: filebeat_event_stream [](#__codelineno-44-78) [](#__codelineno-44-79) # Endpoint - Windows log events from Winlogbeat agent [](#__codelineno-44-80) # type: filebeat - It is applicable for both Filebeat and Winlogbeat log shipping agents [](#__codelineno-44-81) # attrs: <Custom attributes to be added for each log event, provide one or more attributes in key: value format> [](#__codelineno-44-82) # stream: <Write the log events to a Stream within RDA Fabric> [](#__codelineno-44-83) - name: winlogbeat_events # URL is implicit, http://ip:port/winlogbeat_events [](#__codelineno-44-84)   type: filebeat [](#__codelineno-44-85)   enabled: false [](#__codelineno-44-86)   ssl: false [](#__codelineno-44-87)   ssl_cert_dir: /certs [](#__codelineno-44-88)   xpack_features: min [](#__codelineno-44-89)   port: 5145 [](#__codelineno-44-90)   attrs: [](#__codelineno-44-91)     site_code: event_gateway_site01 # Site Name / Code where Event gateway is deployed [](#__codelineno-44-92)     archive_name: winlogbeat_log_events_archive # Log archive name [](#__codelineno-44-93)   stream: "NULL" [](#__codelineno-44-94)   direct_to_stream: winlogbeat_event_stream [](#__codelineno-44-95) [](#__codelineno-44-96) # Endpoint - SNMP Traps over UDP protocol using go language  [](#__codelineno-44-97) # attrs: <Custom attributes to be added for each trap event, provide one or more attributes in key: value format> [](#__codelineno-44-98) # stream: <Write the log events to a Stream within RDA Fabric> [](#__codelineno-44-99) - name: snmp_trap_events [](#__codelineno-44-100)   enabled: false [](#__codelineno-44-101)   type: snmp_trap_go [](#__codelineno-44-102)   port: 5146 [](#__codelineno-44-103)   community: cfxrda [](#__codelineno-44-104)   attrs: [](#__codelineno-44-105)     site_code: event_gateway_site01 # Site Name / Code where Event gateway is deployed [](#__codelineno-44-106)     archive_name: snmp_trap_events_archive # Log archive name [](#__codelineno-44-107)   stream: "NULL" [](#__codelineno-44-108)   direct_to_stream: snmp_trap_event_stream [](#__codelineno-44-109) [](#__codelineno-44-110) # Endpoint - SNMP Traps over UDP protocol using python [](#__codelineno-44-111) # attrs: <Custom attributes to be added for each trap event, provide one or more attributes in key: value format> [](#__codelineno-44-112) # stream: <Write the log events to a Stream within RDA Fabric> [](#__codelineno-44-113) - name: snmp_trap_events [](#__codelineno-44-114)   enabled: false [](#__codelineno-44-115)   type: snmp_trap [](#__codelineno-44-116)   port: 5147 [](#__codelineno-44-117)   community: cfxrda [](#__codelineno-44-118)   attrs: [](#__codelineno-44-119)     site_code: event_gateway_site01 # Site Name / Code where Event gateway is deployed [](#__codelineno-44-120)     archive_name: snmp_trap_events_archive # Log archive name [](#__codelineno-44-121)   stream: "NULL" [](#__codelineno-44-122)   direct_to_stream: snmp_trap_event_stream`

Note

As highlighted above to enable events make the particular **enabled** section as **`true`**

Info

For **filebeat** type endpoint, the supported version of the filebeat and winlogbeat log shipping agent is 7.8.1

#### 1.2.5 Log Archival

Below document provides instructions on how to setup and configure Log Archiving feature in RDA Fabric platform.

##### ****1.2.5.1 About****

Log Archival is a feature in the RDA Fabric platform that allows for the storage of all real-time ingested log messages or events for extended periods, ranging from 6 months to 1 year or more. These logs are stored in a compressed format at a rate of 80% to 90%.

The supported target is any S3 API compatible object storage.

As the first step, you need to configure a log archival repository that points to an S3 object storage endpoint. Each log archival repository may contain one or more named archives, which store the logs in a compressed format with minute-level granularity.

In addition, you need to configure the Event Gateway to save logs to one of the configured log archival repositories. Archived log data can be recalled or replayed at any time using RDA bots or the `rdac` command-line utility.

##### ****1.2.5.2 Add Log Archival Repository****

Log archival repository can be configured through RDAF platform's UI portal or through `rdac` command-line utility.

**Adding a Log Archival repository to utilize RDA Fabric platform's S3 storage using the `rdac` CLI.**

Login as **rdauser** user into one of the RDA Fabric platform VMs using an SSH client (ex: putty) on which `rdac` CLI was installed.

Run the following `rdac` command to add a Log Archival repository and to utilize RDA Fabric platform's S3 object storage service.

`[](#__codelineno-45-1) rdac logarchive add-platform --repo logarchive_repo \ [](#__codelineno-45-2)     --retention 30 \ [](#__codelineno-45-3)     --prefix production`

**\--repo:** Specify Log Archival repository name

**\--retention:** Specify in number of days after which older Log Archival data to be deleted/purged

**\--prefix:** Specify a prefix which can be used to identify archived logs (ex: production or stage etc)

Tip

Please note that when you add a Log Archival repository using the `rdac` CLI command to utilize RDA Fabric platform's S3 object storage service, it will automatically appear in the RDA Fabric's UI under **Configuration** → **RDA Integrations** → **Log Archives**

**Adding a Log Archival repository using external S3 object storage in the RDA Fabric Portal through UI.**

*   Login into RDAF platform's UI portal
*   Click on **Configuration** → **RDA Integrations** → **Log Archives** → **Add Repository**

Tip

Before configuring the log archival repository in the RDA Fabric platform, create an S3 bucket with **read, write, and delete** permissions on the target S3 object storage. This step is only necessary when external S3 object storage is being used.

[![](https://bot-docs.cloudfabrix.io/images/rda_log_archival/add_repository.png)](/images/rda_log_archival/add_repository.png)

| Field Name | Mandatory | Description |
| --- | --- | --- |
| `Name` | yes | Enter Log Archival repository name |
| `Host or Endpoint` | yes | S3 API compatible storage DNS Name or IP Address |
| `Use HTTPS` | no  | Select this option to enable S3 APIs to be encrypted over HTTP protocol |
| `Access Key` | yes | Enter Access Key to access the configured S3 bucket for Log Archival repository |
| `Secret Key` | yes | Enter Secret Key to access the configured S3 bucket for Log Archival repository |
| `Bucket` | yes | Specify the S3 bucket name that is configured for Log Archival repository |
| `Object Prefix` | no  | Specify a prefix which can be used to identify archived logs (ex: production or stage etc) |
| `Manage Lifecycle of Archives` | no  | Select this option if the older Log Archival data to be deleted/purged after certain amount of time |
| `Delete Old Data After (days)` | no  | Specify in number of days after which older Log Archival data to be deleted/purged |

##### ****1.2.5.3 Configure Log Archival Repository in Event Gateway****

After configuring the Log Archival repository on RDA Fabric platform, Event Gateway need to be configured to utilize the configured repository to start archiving the ingested logs.

Log in as the `rdauser` user (or another configured user) to the machine where the RDA Event Gateway is installed using an SSH client (e.g., PuTTY).

*   **Update Event Gateway `service` configuration:**

Edit the Event Gateway's main configuration file `/opt/rdaf/event_gateway/config/main/main.yml` and enable Log Archival repository configuration as shown below.

`[](#__codelineno-46-1) vi /opt/rdaf/event_gateway/config/main/main.yml`

`[](#__codelineno-47-1) # This is the main configuration for Event Gateway. [](#__codelineno-47-2) # Changes to this file only take affect after Event Gateway container restart [](#__codelineno-47-3) [](#__codelineno-47-4) # Name of the site at which Even Gateway is deployed [](#__codelineno-47-5) # If not specified, uses ENV variable RDA_SITE_NAME. This option will override ENV variable value [](#__codelineno-47-6) site_name: event_gateway_site01 [](#__codelineno-47-7) [](#__codelineno-47-8) # Number of processes for publishing messages to RDA Stream. This will override ENV variable NUM_PROCESSES [](#__codelineno-47-9) num_procs: 1 [](#__codelineno-47-10) [](#__codelineno-47-11) ... [](#__codelineno-47-12) ... [](#__codelineno-47-13) [](#__codelineno-47-14) # Log archival settings [](#__codelineno-47-15) archival: [](#__codelineno-47-16)     enabled: true [](#__codelineno-47-17)     # local directory where log files (JSONs and then .gz files) will be saved [](#__codelineno-47-18)     local_dir: /tmp/log_archive/ [](#__codelineno-47-19) [](#__codelineno-47-20)     # Name of the archival. Must be only letters and digits and optionally _- [](#__codelineno-47-21)     name: "acme_log_archive" [](#__codelineno-47-22) [](#__codelineno-47-23)     # Local .gz files are deleted immediately after copying to destination (minio or s3) [](#__codelineno-47-24)     # If not able to push to minio, how long to keep in local directory [](#__codelineno-47-25)     local_retain_max_hours: 2 [](#__codelineno-47-26) [](#__codelineno-47-27)     # Archival destination. If not specified, archival will be disabled [](#__codelineno-47-28)     destination_repository: "logarchive_repo"`

**enabled:** `true` to enable or `false` to disable Log Archival configuration

**local\_dir:** default is set to `/tmp/log_archive/`. This path is used to temporarily store Log Archival data locally when the configured S3 object storage is inaccessible.

**name:** Specify Log Archival name

**local\_retain\_max\_hours:** Specify number of hours to retain the Log Archival data locally when the configured S3 object storage is inaccessible. Local .gz files are deleted immediately after copying them to the repository on S3 object storage. Default value is **2 (hours)**

**destination\_repository:** Specify the Log Archival repository name that is configured in **section 2.1**

*   **Update Event Gateway `endpoint` configuration:**

Log Archival is optional and it can be configured for each endpoint.

Edit Event Gateway's `endpoint` configuration file `/opt/rdaf/event_gateway/config/endpoint.yml` and configure the Log Archival for each endpoint.

Tip

The `archive_name` parameter is optional. When **NOT** configured for an endpoint, the **Log Archive name** that is configured in the Event Gateway's `main.yml` configuration file will be used.

`[](#__codelineno-48-1) vi /opt/rdaf/event_gateway/config/endpoint.yml`

`[](#__codelineno-49-1) endpoints: [](#__codelineno-49-2) [](#__codelineno-49-3) # Endpoint - Syslog Log events over TCP protocol [](#__codelineno-49-4) # attrs: <Custom attributes to be added for each log event, provide one or more attributes in key: value format> [](#__codelineno-49-5) # stream: <Write the log events to a Stream within RDA Fabric> [](#__codelineno-49-6) - name: syslog_tcp_events [](#__codelineno-49-7)   enabled: true [](#__codelineno-49-8)   type: syslog_tcp [](#__codelineno-49-9)   port: 5140 [](#__codelineno-49-10)   ssl: false [](#__codelineno-49-11)   ssl_cert_dir: /certs [](#__codelineno-49-12)   attrs: [](#__codelineno-49-13)     site_code: event_gateway_site01 # Site Name / Code where Event gateway is deployed [](#__codelineno-49-14)     archive_name: syslog_tcp_log_archive # Log archive name [](#__codelineno-49-15)   stream: syslog_tcp_event_stream [](#__codelineno-49-16) [](#__codelineno-49-17) # Endpoint - Syslog Log events over UDP protocol [](#__codelineno-49-18) # attrs: <Custom attributes to be added for each log event, provide one or more attributes in key: value format> [](#__codelineno-49-19) # stream: <Write the log events to a Stream within RDA Fabric> [](#__codelineno-49-20) - name: syslog_udp_events [](#__codelineno-49-21)   enabled: true [](#__codelineno-49-22)   type: syslog_udp [](#__codelineno-49-23)   port: 5141 [](#__codelineno-49-24)   attrs: [](#__codelineno-49-25)     site_code: event_gateway_site01 # Site Name / Code where Event gateway is deployed [](#__codelineno-49-26)     archive_name: syslog_udp_log_archive # Log archive name [](#__codelineno-49-27)   stream: syslog_udp_event_stream`

**archive\_name:** Specify the log archive name (optional).

Please restart the Event Gateway container after making the above changes.

`[](#__codelineno-50-1) docker ps | grep rda-event-gateway`

`[](#__codelineno-51-1) docker restart <rda-event-gateway container ID>`

Tip

Please check `rda-event-gateway` service logs to verify there are no configuration errors.

`[](#__codelineno-52-1) tail -f /opt/rdaf/event_gateway/logs/event_gateway.log`

`[](#__codelineno-53-1) docker logs -f <rda-event-gateway container ID>`

##### ****1.2.5.4 Log Archive Management using `rdac` CLI****

`rdac` CLI supports Log Archival feature configuration and management using the below commands.

`[](#__codelineno-54-1) rdac logarchive --help`

*   Following are the available sub commands

| Sub Commands | Description |
| --- | --- |
| replay | Replay the data from given archive for a specified time interval with specified label |
| repos | List of all log archive repositories |
| add-platform | Add current platform Minio as logarchive repository |
| names | List archive names in a given repository |
| data-size | Show size of data available for given archive for a specified time interval |
| data-read | Read the data from given archive for a specified time interval |
| download | Download the data from given archive for a specified time interval |
| merge-files | Merge multiple locally downloaded Log Archive (.gz) filles into a single CSV/Parquet file |

**Log Archive Replay:** `replay`

It replays the archived log data from a given log archive name for a specified time interval.

**Options:**

**\--repo:** Specify the Log Archival repository name

**\--name:** Specify the Log Archival name for an endpoint

**\--from:** Specify the start date and time from which log messages should be replayed. ISO datetime format is supported. (ex: 2023-10-29T20:45:24 or Oct 29 2023, 10am etc)

**\--to:** Specify the end date and time up to which log messages should be replayed. ISO datetime format is supported. (ex: 2023-10-29T20:45:24 or Oct 29 2023, 10am etc)

**\--max\_rows:** Specify the maximum number of log messages to retrieve. When not specified, all log messages within the specified time duration will be replayed. **(Optional)**

**\--speed:** Specify the log replay speed. 1 means close to the original speed. < 1 means slower than original. > 1 means faster than original. Please note that these speeds are approximate and cannot be guaranteed. 0 means no introduced latency, it will attempt to replay as fast as possible. **(Optional) default value is set to 1**

**\--batch\_size:** Specify the number of log messages to retrieve in each iteration. **(Optional) default value is set to 100**

**\--stream:** Specify the stream name for ingesting the replayed log messages.

**\--label:** Specify a custom label or name (e.g., 'production logs replay') to tag the replayed log messages. This label is useful for reporting and identifying different replay actions. **(Optional)**

**\--site:** Specify the RDA Worker site name where the log replay job should be submitted.

Please refer to the below `rdac logarchive replay` command as an example.

`[](#__codelineno-55-1) rdac logarchive replay --repo logarchive \ [](#__codelineno-55-2)     --name syslog_tcp_log_archive \ [](#__codelineno-55-3)     --from 'Oct 29 2023, 10am' --to 'Oct 20 2023, 11.30pm' \ [](#__codelineno-55-4)     --max_rows 2 \ [](#__codelineno-55-5)     --stream syslog_tcp_event_stream_replay \ [](#__codelineno-55-6)     --site rda-site-01`

[Replay CLI Output](#__tabbed_1_1)
[Replay Logs Output](#__tabbed_1_2)

`[](#__codelineno-56-1) @dm:logarchive-replay  [](#__codelineno-56-2)     repo = 'logarchive' & [](#__codelineno-56-3)     archive = 'syslog_tcp_log_archive' & [](#__codelineno-56-4)     from = '2023-10-29 10:00:00' &  [](#__codelineno-56-5)     minutes = -12240 & [](#__codelineno-56-6)     to = '2023-10-20 22:00:00' & [](#__codelineno-56-7)     label = 'Replay from CLI' & [](#__codelineno-56-8)     max_rows = 2 &  [](#__codelineno-56-9)     speed = 0 &  [](#__codelineno-56-10)     batch_size = 100 [](#__codelineno-56-11) [](#__codelineno-56-12) --> @rn:write-stream name = 'syslog_tcp_event_stream_replay' [](#__codelineno-56-13) [](#__codelineno-56-14) { [](#__codelineno-56-15)   "status": "started", [](#__codelineno-56-16)   "reason": "", [](#__codelineno-56-17)   "now": "2023-10-29T21:07:00.412547", [](#__codelineno-56-18)   "pipeline-name": "log_replay: Replay from CLI", [](#__codelineno-56-19)   "status-subject": "tenants.032a23f3e54444f4b4e3ae69e7a3f5fb.worker.group.f4a56ba6388c.direct.45b07876", [](#__codelineno-56-20)   "jobid": "8fd1d6109881409090fde448215002b3", [](#__codelineno-56-21)   "attributes": {}, [](#__codelineno-56-22)   "pipeline-checksums": { [](#__codelineno-56-23)     "log_replay: Replay from CLI": "9651d110" [](#__codelineno-56-24)   } [](#__codelineno-56-25) } [](#__codelineno-56-26) Completed:` 

`[](#__codelineno-57-1) rdac read-stream --name syslog_tcp_event_stream_replay`

`[](#__codelineno-58-1) [ [](#__codelineno-58-2)   { [](#__codelineno-58-3)     "archive_name": "syslog_tcp_log_archive", [](#__codelineno-58-4)     "raw": "<14>1 2023-10-29T20:45:24.299351Z - - - - - \ufeff2023-10-29T20:45:24.299093+00:00 k8rdapfm01 kernel: [430992.418760] [UFW BLOCK] IN=tunl0 OUT=cali9e5fd88ad03 MAC= SRC=192.168.126.117 DST=192.168.110.222 LEN=112 TOS=0x00 PREC=0x00 TTL=62 ID=58098 DF PROTO=UDP SPT=50442 DPT=53 LEN=92 MARK=0x10000 ", [](#__codelineno-58-5)     "rda_gw_client_ip": "192.168.125.45", [](#__codelineno-58-6)     "rda_gw_ep_name": "syslog_tcp_events", [](#__codelineno-58-7)     "rda_gw_ep_type": "syslog_tcp", [](#__codelineno-58-8)     "rda_gw_timestamp": "2023-10-29T20:45:24.584935+00:00", [](#__codelineno-58-9)     "rda_stream": "NULL", [](#__codelineno-58-10)     "site_code": "event_gateway_site01", [](#__codelineno-58-11)     "syslog_facility": "user", [](#__codelineno-58-12)     "syslog_facility_num": 1, [](#__codelineno-58-13)     "syslog_severity": "INFORMATIONAL", [](#__codelineno-58-14)     "syslog_severity_num": 6 [](#__codelineno-58-15)   }, [](#__codelineno-58-16)   { [](#__codelineno-58-17)     "archive_name": "syslog_tcp_log_archive", [](#__codelineno-58-18)     "raw": "<14>1 2023-10-29T20:45:24.547496Z - - - - - \ufeff2023-10-29T20:45:24.547242+00:00 k8rdapfm01 systemd[1]: run-docker-runtime\\x2drunc-moby-e84a74691b038cbc0729e2f689b2dd2bc5f12636555c68aad763d5c6e977b54f-runc.dLNMgh.mount: Succeeded.", [](#__codelineno-58-19)     "rda_gw_client_ip": "192.168.125.45", [](#__codelineno-58-20)     "rda_gw_ep_name": "syslog_tcp_events", [](#__codelineno-58-21)     "rda_gw_ep_type": "syslog_tcp", [](#__codelineno-58-22)     "rda_gw_timestamp": "2023-10-29T20:45:24.595768+00:00", [](#__codelineno-58-23)     "rda_stream": "NULL", [](#__codelineno-58-24)     "site_code": "event_gateway_site01", [](#__codelineno-58-25)     "syslog_facility": "user", [](#__codelineno-58-26)     "syslog_facility_num": 1, [](#__codelineno-58-27)     "syslog_severity": "INFORMATIONAL", [](#__codelineno-58-28)     "syslog_severity_num": 6 [](#__codelineno-58-29)   } [](#__codelineno-58-30) ]`

**Add Log Archive Repositories:** `add-platform`

It adds RDA platform's S3 object storage service (Minio) as a logarchive repository

**Options:**

**\--repo:** Specify Log Archival repository name

**\--retention:** Specify in number of days after which older Log Archival data to be deleted/purged

**\--prefix:** Specify a prefix which can be used to identify archived logs (ex: production or stage etc)

Please refer to the below `rdac logarchive add-platform` command as an example.

`[](#__codelineno-59-1) rdac logarchive add-platform --repo logarchive_repo \ [](#__codelineno-59-2)     --retention 30 \ [](#__codelineno-59-3)     --prefix production_logs`

[Example Output](#__tabbed_2_1)

`[](#__codelineno-60-1) Added logarchive_repo: logarchive_repo`

**List Log Archive Repositories:** `repo`

It lists all configured log archive repositories

Please refer to the below `rdac logarchive repos` command as an example.

`[](#__codelineno-61-1) rdac logarchive repos --json`

[Example Output](#__tabbed_3_1)

`[](#__codelineno-62-1) [ [](#__codelineno-62-2)   { [](#__codelineno-62-3)     "name": "demo_logarchive", [](#__codelineno-62-4)     "endpoint": "192.168.125.11:9443", [](#__codelineno-62-5)     "bucket": "tenants.a7bdea6599b44623b230f69526e9d543", [](#__codelineno-62-6)     "object_prefix": "demo_logs/" [](#__codelineno-62-7)   }, [](#__codelineno-62-8)   { [](#__codelineno-62-9)     "name": "logsrepo", [](#__codelineno-62-10)     "endpoint": "s3.isv.scality.com", [](#__codelineno-62-11)     "bucket": "cfx-125-11", [](#__codelineno-62-12)     "object_prefix": "/" [](#__codelineno-62-13)   }, [](#__codelineno-62-14)   { [](#__codelineno-62-15)     "name": "platform_repo", [](#__codelineno-62-16)     "endpoint": "192.168.125.11:9443", [](#__codelineno-62-17)     "bucket": "tenants.a7bdea6599b44623b230f69526e9d543", [](#__codelineno-62-18)     "object_prefix": "demo" [](#__codelineno-62-19)   } [](#__codelineno-62-20) ]`

**List Log Archives with a Repository:** `names`

It lists log archive names in a given log archival repository.

**Options:**

**\--repo:** Specify Log Archival repository name

Please refer to the below `rdac logarchive names` command as an example.

`[](#__codelineno-63-1) rdac logarchive names --repo logarchive --json`

[Example Output](#__tabbed_4_1)

`[](#__codelineno-64-1) [ [](#__codelineno-64-2)   { [](#__codelineno-64-3)     "arhive_name": "sythentic-syslogs", [](#__codelineno-64-4)     "num_days": 275, [](#__codelineno-64-5)     "first_day": "2022/12/06", [](#__codelineno-64-6)     "last_day": "2023/10/04" [](#__codelineno-64-7)   } [](#__codelineno-64-8) ]`

**List Log Archives Data Size:** `data-size`

It shows the size of data (in bytes) available for given log archive for a specified time interval

**Options:**

**\--repo:** Specify Log Archival repository name

**\--name:** Specify the Log Archival name for an endpoint

**\--from:** Specify the start date and time from which log messages should be replayed. ISO datetime format is supported. (ex: 2023-10-29T20:45:24 or Oct 29 2023, 10am etc)

**\--minutes:** Specify the time in minutes relative to the date and time specified in the `--from` option.

Please refer to the below `rdac logarchive data-size` command as an example.

`[](#__codelineno-65-1) rdac logarchive data-size --repo logarchive \ [](#__codelineno-65-2)     --name syslog_events_archive \ [](#__codelineno-65-3)     --from 'Oct 10 2023, 10am' --minutes 30`

[Example Output](#__tabbed_5_1)

`[](#__codelineno-66-1) +---------------------+-------------------+------------------------+ [](#__codelineno-66-2) | Timestamp           |   Number of Files | Compressed Data Size   | [](#__codelineno-66-3) |---------------------+-------------------+------------------------| [](#__codelineno-66-4) | 2023-10-10T10:00:00 |                 1 | 22,441                 | [](#__codelineno-66-5) | 2023-10-10T10:01:00 |                 1 | 21,588                 | [](#__codelineno-66-6) | 2023-10-10T10:02:00 |                 1 | 19,009                 | [](#__codelineno-66-7) | 2023-10-10T10:03:00 |                 1 | 24,985                 | [](#__codelineno-66-8) ... [](#__codelineno-66-9) ... [](#__codelineno-66-10) | 2023-10-10T10:27:00 |                 1 | 18,662                 | [](#__codelineno-66-11) | 2023-10-10T10:28:00 |                 1 | 19,322                 | [](#__codelineno-66-12) | 2023-10-10T10:29:00 |                 1 | 21,968                 | [](#__codelineno-66-13) | 2023-10-10T10:30:00 |                 1 | 20,764                 | [](#__codelineno-66-14) | TOTAL               |                31 | 650,720                | [](#__codelineno-66-15) +---------------------+-------------------+------------------------+`

**Read Data from Log Archive:** `data-read`

It reads the data from a given log archive for a specified time interval and prints the output on the console.

**Options:**

**\--repo:** Specify Log Archival repository name

**\--name:** Specify the Log Archival name for an endpoint

**\--from:** Specify the start date and time from which log messages should be replayed. ISO datetime format is supported. (ex: 2023-10-29T20:45:24 or Oct 29 2023, 10am etc)

**\--minutes:** Specify the time in minutes relative to the date and time specified in the `--from` option.

Please refer to the below `rdac logarchive data-read` command as an example.

`[](#__codelineno-67-1) rdac logarchive data-read --repo logarchive \ [](#__codelineno-67-2)     --name syslog_events_archive \ [](#__codelineno-67-3)     --from 'Oct 10 2023, 10am' \ [](#__codelineno-67-4)     --minutes 30 \ [](#__codelineno-67-5)     --max_rows 2`

[Example Output](#__tabbed_6_1)

`[](#__codelineno-68-1) [ [](#__codelineno-68-2) { [](#__codelineno-68-3)   "rda_gw_ep_type": "syslog_udp", [](#__codelineno-68-4)   "rda_gw_seq": 3666473, [](#__codelineno-68-5)   "raw": "<163>2023-10-10T10:00:00.318Z R810-dev-2.engr.cloudfabrix.com Hostd: error hostd[36F40B70] [Originator@6876 sub=Default opID=0778c9cb] Unable to convert Vigor value 'centos8-64' of type 'char const*' to VIM type 'Vim::Vm::GuestOsDescriptor::GuestOsIdentifier'\n", [](#__codelineno-68-6)   "rda_gw_client_ip": "192.168.158.210", [](#__codelineno-68-7)   "rda_gw_ep_name": "syslog_udp_events", [](#__codelineno-68-8)   "rda_gw_timestamp": "2023-10-10T10:00:00.349091+00:00", [](#__codelineno-68-9)   "rda_stream": "syslog_udp_event_stream", [](#__codelineno-68-10)   "syslog_facility": "local4", [](#__codelineno-68-11)   "syslog_facility_num": 20, [](#__codelineno-68-12)   "syslog_severity": "ERROR", [](#__codelineno-68-13)   "syslog_severity_num": 3, [](#__codelineno-68-14)   "site_code": "event_gateway_site01", [](#__codelineno-68-15)   "archive_name": "syslog_events_archive" [](#__codelineno-68-16) }, [](#__codelineno-68-17) { [](#__codelineno-68-18)   "rda_gw_ep_type": "syslog_udp", [](#__codelineno-68-19)   "rda_gw_seq": 3666474, [](#__codelineno-68-20)   "raw": "<163>2023-10-10T10:00:00.319Z R810-dev-2.engr.cloudfabrix.com Hostd: error hostd[36840B70] [Originator@6876 sub=Default opID=0778c9ca] Unable to convert Vigor value 'centos8-64' of type 'char const*' to VIM type 'Vim::Vm::GuestOsDescriptor::GuestOsIdentifier'\n", [](#__codelineno-68-21)   "rda_gw_client_ip": "192.168.158.210", [](#__codelineno-68-22)   "rda_gw_ep_name": "syslog_udp_events", [](#__codelineno-68-23)   "rda_gw_timestamp": "2023-10-10T10:00:00.349602+00:00", [](#__codelineno-68-24)   "rda_stream": "syslog_udp_event_stream", [](#__codelineno-68-25)   "syslog_facility": "local4", [](#__codelineno-68-26)   "syslog_facility_num": 20, [](#__codelineno-68-27)   "syslog_severity": "ERROR", [](#__codelineno-68-28)   "syslog_severity_num": 3, [](#__codelineno-68-29)   "site_code": "event_gateway_site01", [](#__codelineno-68-30)   "archive_name": "syslog_events_archive" [](#__codelineno-68-31) }, [](#__codelineno-68-32) ]`

**Download Log Data from Log Archive:** `download`

It downloads the compressed log data (.gz) files from given log archive for a specified time interval.

**Options:**

**\--repo:** Specify Log Archival repository name

**\--name:** Specify the Log Archival name for an endpoint

**\--from:** Specify the start date and time from which log messages should be replayed. ISO datetime format is supported. (ex: 2023-10-29T20:45:24 or Oct 29 2023, 10am etc)

**\--minutes:** Specify the time in minutes relative to the date and time specified in the `--from` option.

Please refer to the below `rdac logarchive download` command as an example.

`[](#__codelineno-69-1) rdac logarchive download --repo logarchive --name syslog_events_archive \ [](#__codelineno-69-2)     --from 'Oct 10 2023, 10am' \ [](#__codelineno-69-3)     --minutes 1440 \ [](#__codelineno-69-4)     --out ./log_archive_download`

[Example Output](#__tabbed_7_1)

`[](#__codelineno-70-1) Downloaded object /syslog_events_archive/2023/10/10/10/00/2d2b42a9.gz [](#__codelineno-70-2) Downloaded object /syslog_events_archive/2023/10/10/10/01/2d2b42a9.gz [](#__codelineno-70-3) Downloaded object /syslog_events_archive/2023/10/10/10/02/2d2b42a9.gz [](#__codelineno-70-4) Downloaded object /syslog_events_archive/2023/10/10/10/03/2d2b42a9.gz [](#__codelineno-70-5) ... [](#__codelineno-70-6) Downloaded object /syslog_events_archive/2023/10/10/10/14/2d2b42a9.gz [](#__codelineno-70-7) Downloaded object /syslog_events_archive/2023/10/10/10/15/2d2b42a9.gz`

**Merge Log Data files:** `merge-files`

It merges multiple locally downloaded Log Archive (.gz) filles into a single CSV/Parquet file.

Please refer to the below `rdac logarchive merge-files` command as an example.

`[](#__codelineno-71-1) rdac logarchive merge-files --folder ./log_archive_download/syslog_events_archive/2023/10/25/10/10/ \ [](#__codelineno-71-2)     --tofile ./log_archive_download/log_archive_merge.csv`

[Example Output](#__tabbed_8_1)

`[](#__codelineno-72-1) Total rows in final dataframe: 1 [](#__codelineno-72-2) { [](#__codelineno-72-3)   "mem_total_gb": 47.034, [](#__codelineno-72-4)   "mem_available_gb": 26.113, [](#__codelineno-72-5)   "mem_percent": 44.5, [](#__codelineno-72-6)   "mem_used_gb": 19.703, [](#__codelineno-72-7)   "mem_free_gb": 1.327 [](#__codelineno-72-8) } [](#__codelineno-72-9) Saving CSV file: /logarchive`

##### ****1.2.5.5 Log Archive Replay****

Archived log messages can be replayed on-demand as per user's requirement either using `rdac logarchive` CLI or through RDA Fabric platform's UI portal.

Tip

For log messages replay using `rdac logarchive` CLI, please refer **Log Archival Management using rdac CLI** section.

The steps below outline how to replay log messages from the RDA Fabric platform's UI portal.

**1.** Login into UI portal and go to **Main Menu** --> **Configuration** --> **RDA Integrations** --> **Log Archives** --> Click on **Log Archive Repository** --> Select one of the **Log Archive** name and click on **Replay**

![rda_log_archival_Log_Archives](https://bot-docs.cloudfabrix.io/images/rda_log_archival/log_archives.png)

**2.** After Clicking on **Replay** you need to give the UTC Timeslot of your required logs to replay as shown below in the Screenshot

![rda_log_archival_Logs_Replay](https://bot-docs.cloudfabrix.io/images/rda_log_archival/logs_replay.png)

Note

Specify the **stream name** for ingesting the replayed log messages. Specify **Label** name (e.g., 'production logs replay') to tag the replayed log messages. This label is useful for reporting and identifying different replay actions.

##### ****1.2.5.6 Log Archive Bots****

RDA Fabric platform also provides **logarchive** bots which can be used in RDA pipelines. Below screenshot shows the available **logarchive** bots.

![rda_log_archival_Logarchive_Bots](https://bot-docs.cloudfabrix.io/images/rda_log_archival/logarchive_bots.png)

*   The following pipeline provides an example on how to use `logarchive-replay` bot within a RDA pipeline.

[Pipeline](#__tabbed_9_1)
[Replay Logs Output](#__tabbed_9_2)

`[](#__codelineno-73-1) @dm:logarchive-replay repo = "logarchive_repo" and  [](#__codelineno-73-2)                 archive = 'syslog_tcp_log_archive' and  [](#__codelineno-73-3)                 from = "2023-10-26 17:24:14" and  [](#__codelineno-73-4)                 minutes = 30 and  [](#__codelineno-73-5)                 batch_size = 100 [](#__codelineno-73-6) [](#__codelineno-73-7) --> @rn:write-stream name = 'logarchive_replay_stream'`

`[](#__codelineno-74-1) rdac read-stream --name logarchive_replay_stream`

`[](#__codelineno-75-1) [ [](#__codelineno-75-2)   { [](#__codelineno-75-3)     "archive_name": "syslog_tcp_log_archive", [](#__codelineno-75-4)     "raw": "<14>1 2023-10-29T20:45:24.299351Z - - - - - \ufeff2023-10-29T20:45:24.299093+00:00 k8rdapfm01 kernel: [430992.418760] [UFW BLOCK] IN=tunl0 OUT=cali9e5fd88ad03 MAC= SRC=192.168.126.117 DST=192.168.110.222 LEN=112 TOS=0x00 PREC=0x00 TTL=62 ID=58098 DF PROTO=UDP SPT=50442 DPT=53 LEN=92 MARK=0x10000 ", [](#__codelineno-75-5)     "rda_gw_client_ip": "192.168.125.45", [](#__codelineno-75-6)     "rda_gw_ep_name": "syslog_tcp_events", [](#__codelineno-75-7)     "rda_gw_ep_type": "syslog_tcp", [](#__codelineno-75-8)     "rda_gw_timestamp": "2023-10-29T20:45:24.584935+00:00", [](#__codelineno-75-9)     "rda_stream": "NULL", [](#__codelineno-75-10)     "site_code": "event_gateway_site01", [](#__codelineno-75-11)     "syslog_facility": "user", [](#__codelineno-75-12)     "syslog_facility_num": 1, [](#__codelineno-75-13)     "syslog_severity": "INFORMATIONAL", [](#__codelineno-75-14)     "syslog_severity_num": 6 [](#__codelineno-75-15)   }, [](#__codelineno-75-16)   { [](#__codelineno-75-17)     "archive_name": "syslog_tcp_log_archive", [](#__codelineno-75-18)     "raw": "<14>1 2023-10-29T20:45:24.547496Z - - - - - \ufeff2023-10-29T20:45:24.547242+00:00 k8rdapfm01 systemd[1]: run-docker-runtime\\x2drunc-moby-e84a74691b038cbc0729e2f689b2dd2bc5f12636555c68aad763d5c6e977b54f-runc.dLNMgh.mount: Succeeded.", [](#__codelineno-75-19)     "rda_gw_client_ip": "192.168.125.45", [](#__codelineno-75-20)     "rda_gw_ep_name": "syslog_tcp_events", [](#__codelineno-75-21)     "rda_gw_ep_type": "syslog_tcp", [](#__codelineno-75-22)     "rda_gw_timestamp": "2023-10-29T20:45:24.595768+00:00", [](#__codelineno-75-23)     "rda_stream": "NULL", [](#__codelineno-75-24)     "site_code": "event_gateway_site01", [](#__codelineno-75-25)     "syslog_facility": "user", [](#__codelineno-75-26)     "syslog_facility_num": 1, [](#__codelineno-75-27)     "syslog_severity": "INFORMATIONAL", [](#__codelineno-75-28)     "syslog_severity_num": 6 [](#__codelineno-75-29)   } [](#__codelineno-75-30) ]`

### **1.3 RDA Edge Collector Installation**

Note

**Edge Collector** or **Edge Collector Agent** wherever mentioned below in the Document refers to same component.

**Prerequisites:**

*   Linux OS
*   Memory - 8GB
*   Disk - 50GB
*   Python 3.7.4 or above
*   [Docker Version](https://docs.docker.com/engine/install/ "Docker Version")
     (18.09.2 or above)
    
*   [Docker Compose](https://docs.docker.com/compose/install/ "Docker Compose 18.09.2")
     (1.27.x and above)
    

**Installation Steps:**

**Step-1:**

The RDA Edge Collector agent registers and communicates with the RDAF platform using a configuration file that contains your tenant ID, data fabric access tokens, and object storage credentials.

Download RDA Fabric Configuration from the portal by going to `Configuration --> RDA Administration --> Network` and copy it to the local filesystem where the edge collector agent is going to be installed.

*   Save the file as `rda_network_config.json`

![RDAFNetworkConfig](https://bot-docs.cloudfabrix.io/images/rda-network-config.png)

*   Create the below directory structure

``[](#__codelineno-76-1) sudo mkdir -p /opt/rdaf/network_config [](#__codelineno-76-2) sudo mkdir -p /opt/rdaf/edgecollector/cred [](#__codelineno-76-3) sudo chown -R `id -u`:`id -g` /opt/rdaf``

*   Copy the downloaded RDA Fabric configuration file as shown below.

`[](#__codelineno-77-1) cp rda_network_config.json /opt/rdaf/network_config/rda_network_config.json`

**Step-2:** **Docker Login**

Run the below command to create and save the docker login session into CloudFabrix's secure docker repository.

`[](#__codelineno-78-1) docker login -u='readonly' -p='readonly' cfxregistry.cloudfabrix.io`

**Step-3:** **Create Docker Compose File**

Create docker compose configuration file for RDA Edge Collector as shown below.

Tip

**Note-1:** Optionally change the edge collector's group name (also known as **Site**) in the docker-compose file by updating the **agent-group-name** value. In this example, the edge collector's group name is specified as **ec-group-01**

**Note-2:** Adjust **mem\_limit** and **memswap\_limit** as per the workload requirements. In the below configuration, these parameters are set to **6GB**

`[](#__codelineno-79-1) cd /opt/rdaf/edgecollector [](#__codelineno-79-2) [](#__codelineno-79-3) cat > rda-edgecollector-docker-compose.yml <<EOF [](#__codelineno-79-4) version: '3.1' [](#__codelineno-79-5) services: [](#__codelineno-79-6)  rda_edgecollector_agent: [](#__codelineno-79-7)   image: 'cfxregistry.cloudfabrix.io/cfxcollector:daily' [](#__codelineno-79-8)   container_name: rda_edgecollector_agent [](#__codelineno-79-9)   restart: always [](#__codelineno-79-10)   network_mode: host [](#__codelineno-79-11)   mem_limit: 6G [](#__codelineno-79-12)   memswap_limit: 6G [](#__codelineno-79-13)   volumes: [](#__codelineno-79-14)    - /opt/rdaf/network_config:/network_config [](#__codelineno-79-15)    - /opt/rdaf/edgecollector:/cfxedgecollector [](#__codelineno-79-16)    - /opt/rdaf/edgecollector/cred:/cred [](#__codelineno-79-17)   environment: [](#__codelineno-79-18)    RDA_NETWORK_CONFIG: /network_config/rda_network_config.json [](#__codelineno-79-19)    PYTHONPATH: /opt/cfx-rda-edgeagent [](#__codelineno-79-20)   logging: [](#__codelineno-79-21)    driver: "json-file" [](#__codelineno-79-22)    options: [](#__codelineno-79-23)     max-size: "25m" [](#__codelineno-79-24)     max-file: "5" [](#__codelineno-79-25)   ulimits: [](#__codelineno-79-26)    nproc: [](#__codelineno-79-27)     soft: 64000 [](#__codelineno-79-28)     hard: 128000 [](#__codelineno-79-29)    nofile: [](#__codelineno-79-30)     soft: 64000 [](#__codelineno-79-31)     hard: 128000 [](#__codelineno-79-32)   entrypoint: [](#__codelineno-79-33)    - /bin/bash [](#__codelineno-79-34)    - '-c' [](#__codelineno-79-35)    - >- [](#__codelineno-79-36)     cd /opt/cfx-rda-edgeagent/src/; python -c 'import edgecollector_rda_agent ; [](#__codelineno-79-37)     edgecollector_rda_agent.run()' --creddir /cred/ --agent-group-name ec-group-01 [](#__codelineno-79-38) [](#__codelineno-79-39) EOF`

**Step-4:** **Bring Up RDA Edge Collector**

`[](#__codelineno-80-1) cd /opt/rdaf/edgecollector [](#__codelineno-80-2) [](#__codelineno-80-3) docker-compose -f rda-edgecollector-docker-compose.yml pull  [](#__codelineno-80-4) docker-compose -f rda-edgecollector-docker-compose.yml up -d`

**Step-5:** **Check Edge Collector Status**

Check Edge Collector agent status using `docker ps` command and ensure that it is up and running, without any restarts. If you see that if it is restarting, make sure you copied the RDA network config file to the correct location.

`[](#__codelineno-81-1) docker ps | grep edgecollector`

**Step-6:** **Verify RDA Edge Collector in RDA Fabric portal**

A newly installed Edge Collector will authenticate with the RDA Fabric platform and it will show up in RDA Fabric portal under `Fabric Health --> Agents` .

**Step-7:** **Verify Edge Collector using RDA Client (rdac) utility**

If you have installed RDA Client (rdac) command line utility, you can also verify newly created Edge Collector using `rdac agents` command.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!