 



Guide to Install and Configure RDA Fabric platform in on-premise environment.
=============================================================================

**1\. RDAF platform and it's components**
-----------------------------------------

Robotic Data Automation Fabric (RDAF) is designed to manage data in a multi-cloud and multi-site environments at scale. It is built on microservices and distributed architecture which can be deployed in a Kubernetes cluster infrastructure or in a native docker container environment which is managed through RDA Fabric (RDAF) deployment CLI.

RDAF deployment CLI is built on top of docker-compose container management utility to automate the lifecycle management of RDAF platform components which includes, install, upgrades, patching, backup, recovery, other management and maintenance operations.

RDAF platform consists below set of services which can be deployed in a single virtual machine or a baremetal server or spread across multiple virtual machines or baremetal servers.

*   **RDA core platform services**
    
    *   registry
    *   api-server
    *   identity
    *   collector
    *   scheduler
    *   scheduler-admin
    *   portal-ui
    *   portal-backend
*   **RDA infrastructure services**
    
    *   NATs
    *   MariaDB
    *   Minio
    *   Opensearch
    *   Kafka / Zookeeper
    *   Redis
    *   HAproxy
    *   GraphDB

Note

**Note:** CloudFabrix RDAF platform integrates with above opensource services and uses them as back-end components. However, these opensource service images are not bundled with RDAF platform by default. Customers can download CloudFabrix validated versions from publicly available docker repository (ex: quay.io or docker hub) and deploy them with GPL / AGPL or Commercial license as per their support requirements. RDAF deployment tool provides a hook to assist the Customer to download these opensource software images (supported versions) from the Customer's chosen repository.

*   **RDA application services**
    
    *   cfxOIA (Operations Intelligence & Analytics)
    *   cfxAIA (Asset Intelligence & Analytics)
*   **RDA worker service**
    
*   **RDA event gateway**
*   **RDA edgecollector**
*   **RDA studio**

**2\. Docker registry access for RDAF platform services deployment**
--------------------------------------------------------------------

CloudFabrix provides secure docker images registry hosted on AWS cloud which contains all of the required docker images to deploy RDA Fabric platform, infrastructure and application services.

For deploying RDA Fabric services, the environment need to have access to CloudFabrix docker registry hosted on AWS cloud over internet. Below is the docker registry URL and port.

**Outbound internet access:**

*   **URL**: https://cfxregistry.cloudfabrix.io
*   **Port**: 443

Below picture illustrates network access flow from on-premise environment to access CloudFabrix docker registry hosted on AWS cloud.

**Docker registry hosted on AWS cloud**

Tip

Please click on the picture below to enlarge and to go back to the page please click on the back arrow button on the top.

[![](https://bot-docs.cloudfabrix.io/images/docker-repository/cfx-aws-hosted-docker-repository.png)](/images/docker-repository/cfx-aws-hosted-docker-repository.png)

Additionally, CloudFabrix also support hosting an on-premise docker registry in a restricted environment where RDA Fabric VMs do not have direct internet access with or without HTTP proxy.

Once on-premise docker registry service is installed within the Customer's DMZ environment, it communicates with docker registry service hosted on AWS cloud and replicates the selective images required for RDA Fabric deployment for a new installation, on-going updates and patches.

RDA Fabric VMs will pull the images from on-premise docker registry locally.

Below picture illustrates network access flow from on-premise environment to access CloudFabrix docker registry hosted on AWS cloud.

**Docker registry hosted On-premise**

Tip

Please click on the picture below to enlarge and to go back to the page please click on the back arrow button on the top.

[![](https://bot-docs.cloudfabrix.io/images/docker-repository/cfx-on-premise-docker-repository.png)](/images/docker-repository/cfx-on-premise-docker-repository.png)

Please refer **[On-premise Docker registry setup](https://bot-docs.cloudfabrix.io/installation_guides/rdaf_cli/#12-on-premise-docker-registry-setup)
** to setup, configure, install and manage on-premise docker registry service and images.

Tip

On-premise docker registry server is recommended to be deployed. However, it is an optional service if there is no restriction in accessing the internet. With on-premise docker registry server, images can be downloaded offline and keep them ready for a fresh install or an update. It will avoid any network glitches or issues in downloading the images from internet during a production environment's installation or upgrade.

**3\. HTTP Proxy support for deployment**
-----------------------------------------

RHELUbuntu

Optionally, RDA Fabric docker images can also be accessed over HTTP proxy during the deployment if one is configured to control the internet access.

On all of the RDA Fabric machines where the services going to be deployed, should be configured with HTTP proxy settings.

*   Edit **/etc/environment** file and define HTTP Proxy server settings as shown below.

|     |     |
| --- | --- |
| [1](#__codelineno-0-1)<br>[2](#__codelineno-0-2)<br>[3](#__codelineno-0-3)<br>[4](#__codelineno-0-4)<br>[5](#__codelineno-0-5)<br>[6](#__codelineno-0-6)<br>[7](#__codelineno-0-7) | `http_proxy="http://<username>:<password>@192.168.142.10:3128" https_proxy="http://<username>:<password>@192.168.142.10:3128" no_proxy="localhost,127.0.0.1,192.168.192.201,192.168.192.202,192.168.192.203,192.168.192.204,*.rhel.pool.ntp.org,*.us.pool.ntp.org" HTTP_PROXY="http://<username>:<password>@192.168.142.10:3128" HTTPS_PROXY="http://<username>:<password>@192.168.142.10:3128" NO_PROXY="localhost,127.0.0.1,192.168.192.201,192.168.192.202,192.168.192.203,192.168.192.204,*.rhel.pool.ntp.org,*.us.pool.ntp.org" export http_proxy https_proxy no_proxy HTTP_PROXY HTTPS_PROXY NO_PROXY` |

Info

**Note:** IP Address details are given for a reference only. They need to be replaced with appropriate HTTP Proxy server IP and port applicable to your environment.

Warning

**Note:** For **no\_proxy** and **NO\_PROXY** environment variables, please include loopback and IP addresses of all RDA platform, infrastructure, application and worker nodes. This will ensure to avoid internal RDA Fabric's application traffic going through HTTP proxy server.

Additionally, include any target applications or devices IP address or DNS names where it doesn't require to go through HTTP Proxy server.

Optionally, RDA Fabric docker images can also be accessed over HTTP proxy during the deployment if one is configured to control the internet access.

On all of the RDA Fabric machines where the services going to be deployed, should be configured with HTTP proxy settings.

*   Edit **/etc/profile.d/proxy.sh** file and define HTTP Proxy server settings as shown below.

|     |     |
| --- | --- |
| [1](#__codelineno-1-1) | `sudo vi /etc/profile.d/proxy.sh` |

|     |     |
| --- | --- |
| [1](#__codelineno-2-1)<br>[2](#__codelineno-2-2)<br>[3](#__codelineno-2-3)<br>[4](#__codelineno-2-4)<br>[5](#__codelineno-2-5)<br>[6](#__codelineno-2-6)<br>[7](#__codelineno-2-7) | `http_proxy="http://<username>:<password>@192.168.142.10:3128" https_proxy="http://<username>:<password>@192.168.142.10:3128" no_proxy="localhost,127.0.0.1,192.168.192.201,192.168.192.202,192.168.192.203,192.168.192.204,*.rhel.pool.ntp.org,*.us.pool.ntp.org" HTTP_PROXY="http://<username>:<password>@192.168.142.10:3128" HTTPS_PROXY="http://<username>:<password>@192.168.142.10:3128" NO_PROXY="localhost,127.0.0.1,192.168.192.201,192.168.192.202,192.168.192.203,192.168.192.204,*.rhel.pool.ntp.org,*.us.pool.ntp.org" export http_proxy https_proxy no_proxy HTTP_PROXY HTTPS_PROXY NO_PROXY` |

*   Update file permissions with **execute** and source the file or logout and login again to enable the http proxy settings.

|     |     |
| --- | --- |
| [1](#__codelineno-3-1)<br>[2](#__codelineno-3-2) | `sudo chmod +x /etc/profile.d/proxy.sh source /etc/profile.d/proxy.sh` |

*   Configure http proxy for APT package manager by editing **/etc/apt/apt.conf.d/80proxy** file as shown below.

|     |     |
| --- | --- |
| [1](#__codelineno-4-1) | `sudo vi /etc/apt/apt.conf.d/80proxy` |

|     |     |
| --- | --- |
| [1](#__codelineno-5-1)<br>[2](#__codelineno-5-2) | `Acquire::http::proxy "http://<username>:<password>@192.168.142.10:3128"; Acquire::https::proxy "http://<username>:<password>@192.168.142.10:3128";` |

Info

**Note:** IP Address details are given for a reference only. They need to be replaced with appropriate HTTP Proxy server IP and port applicable to your environment. **Username** and **Password** fields are optional and needed only if the HTTP Proxy is enabled with user authentication.

Warning

**Note:** For **no\_proxy** and **NO\_PROXY** environment variables, please include loopback and IP addresses of all RDA platform, infrastructure, application and worker nodes. This will ensure to avoid internal RDA Fabric's application traffic going through HTTP proxy server.

Additionally, include any target applications or devices IP address or DNS names where it doesn't require to go through HTTP Proxy server.

**DNS Resolution and CFX Registry Access Issues**

Note

If the above proxy settings are not working and seeing DNS challenge or CFX registry access, Please follow the below steps

*   Steps to resolve DNS issues and access to CFX registry

![images Authentication Failure1 ](https://bot-docs.cloudfabrix.io/images/authentication_fialure1.png)

*   To update the DNS records we need to update the below domains in `etc/hosts` file

`[](#__codelineno-6-1) sudo vi /etc/hosts`

`[](#__codelineno-7-1) 127.0.0.1  localhost [](#__codelineno-7-2) 54.177.20.202 cfxregistry.cloudfabrix.io [](#__codelineno-7-3) 54.146.255.141 quay.io`

Note

quay.io is having a dynamic ip, so before updating the host file check the ip again by using the command mentioned below.

`[](#__codelineno-8-1) ping quay.io`

Example Output

![images Quay.Io ](https://bot-docs.cloudfabrix.io/images/quay_io.png)

*   Please check the DNS Server Settings by using the below command

`[](#__codelineno-9-1) resolvectl status`

Example Output

`[](#__codelineno-10-1) Current DNS Server: 192.168.159.101 [](#__codelineno-10-2)         DNS Servers: 192.168.159.101 [](#__codelineno-10-3)                       192.168.159.100`

*   To update the additional DNS Servers please run the below command

`[](#__codelineno-11-1) vi /etc/netplan/00-netcfg.yaml`

Example Output

`[](#__codelineno-12-1) network: [](#__codelineno-12-2)     version: 2 [](#__codelineno-12-3)     renderer: networkd [](#__codelineno-12-4)     ethernets: [](#__codelineno-12-5)       ens160: [](#__codelineno-12-6)         dhcp4: no [](#__codelineno-12-7)         dhcp6: no [](#__codelineno-12-8)         addresses: [192.168.125.66/24] [](#__codelineno-12-9)         gateway4:  192.168.125.1 [](#__codelineno-12-10)         nameservers: [](#__codelineno-12-11)           addresses: [192.168.159.101,192.168.159.100]`

*   To apply the above changes please run the below command

`[](#__codelineno-13-1) sudo netplan apply`

*   If you still see any DNS Server settings issue, please run the below commands

`[](#__codelineno-14-1) sudo systemctl restart systemd-resolved`

`[](#__codelineno-15-1) sudo systemctl status systemd-resolved`

*   Configure Docker Daemon with HTTP Proxy server settings.

|     |     |
| --- | --- |
| [1](#__codelineno-16-1)<br>[2](#__codelineno-16-2) | `sudo mkdir -p /etc/systemd/system/docker.service.d cd /etc/systemd/system/docker.service.d` |

Create a file called **http-proxy.conf** under above directory and add the HTTP Proxy configuration lines as shown below.

|     |     |
| --- | --- |
| [1](#__codelineno-17-1) | `vi http-proxy.conf` |

|     |     |
| --- | --- |
| [1](#__codelineno-18-1)<br>[2](#__codelineno-18-2)<br>[3](#__codelineno-18-3)<br>[4](#__codelineno-18-4) | `[Service] Environment="HTTP_PROXY=http://<username>:<password>@192.168.142.10:3128" Environment="HTTPS_PROXY=http://<username>:<password>@192.168.142.10:3128" Environment="NO_PROXY=localhost,127.0.0.1,192.168.192.201,192.168.192.202,192.168.192.203,192.168.192.204,*.rhel.pool.ntp.org,*.us.pool.ntp.org"` |

Warning

**Note:** If there is an username and password required for HTTP Proxy server authentication, and if the username has any special characters like "\\" (ex: username\\domain), it need to be entered in HTTP encoded format. This is applicable only for Docker daemon. Please follow the below instructions.

**HTTP Encode / Decode URL:** [https://www.urlencoder.org](https://www.urlencoder.org)

If the username is john\\acme.com : The HTTP encoded value is john%%5Cacme.com and the HTTP Proxy configuration looks like below.

|     |     |
| --- | --- |
| [1](#__codelineno-19-1)<br>[2](#__codelineno-19-2)<br>[3](#__codelineno-19-3)<br>[4](#__codelineno-19-4) | `[Service] Environment="HTTP_PROXY=http://john%5Cacme.com:password@192.168.142.10:3128" Environment="HTTPS_PROXY=http://john%5Cacme.com:password@192.168.142.10:3128" Environment="NO_PROXY=localhost,127.0.0.1,192.168.192.201,192.168.192.202,192.168.192.203,192.168.192.204,*.rhel.pool.ntp.org,*.us.pool.ntp.org"` |

*   Restart the RDA Platform, Infrastructure, Application and Worker node VMs to apply the HTTP Proxy server settings.
    
*   To apply the HTTP Proxy server settings at the docker level please run the below 2 given commands
    

`[](#__codelineno-20-1) sudo systemctl daemon-reload`

`[](#__codelineno-21-1) sudo systemctl restart docker`

*   After restarting the docker services please verify the configuration by checking the docker environment using below command

`[](#__codelineno-22-1) sudo systemctl show --property=Environment docker`

Example Output

`[](#__codelineno-23-1) Environment=HTTP_PROXY=http://192.168.125.66:3128 HTTPS_PROXY=https://192.168.125.66:3129 NO_PROXY=localhost,127.0.0.1,cfxregistry.cloudfabrix.io`

Note

You can find more info about docker proxy configuration in below URL [https://docs.docker.com/config/daemon/systemd/#httphttps-proxy](https://docs.docker.com/config/daemon/systemd/#httphttps-proxy "https://docs.docker.com/config/daemon/systemd/#httphttps-proxy")

*   Verify if you are able to connect to CloudFabrix docker registry URL running the below command.

`[](#__codelineno-24-1) curl -vv https://cfxregistry.cloudfabrix.io:443`

Example Output

`[](#__codelineno-25-1) curl -vv https://cfxregistry.cloudfabrix.io:443 [](#__codelineno-25-2) * Rebuilt URL to: https://cfxregistry.cloudfabrix.io:443/ [](#__codelineno-25-3) *   Trying 54.177.20.202... [](#__codelineno-25-4) * TCP_NODELAY set [](#__codelineno-25-5) * Connected to cfxregistry.cloudfabrix.io (54.177.20.202) port 443 (#0) [](#__codelineno-25-6) * ALPN, offering h2 [](#__codelineno-25-7) * ALPN, offering http/1.1 [](#__codelineno-25-8) * successfully set certificate verify locations: [](#__codelineno-25-9) *   CAfile: /etc/pki/tls/certs/ca-bundle.crt [](#__codelineno-25-10)   CApath: none [](#__codelineno-25-11) * TLSv1.3 (OUT), TLS handshake, Client hello (1): [](#__codelineno-25-12) * TLSv1.3 (IN), TLS handshake, Server hello (2): [](#__codelineno-25-13) * TLSv1.2 (IN), TLS handshake, Certificate (11): [](#__codelineno-25-14) . [](#__codelineno-25-15) . [](#__codelineno-25-16) . [](#__codelineno-25-17) *  SSL certificate verify ok. [](#__codelineno-25-18) > GET / HTTP/1.1 [](#__codelineno-25-19) > Host: cfxregistry.cloudfabrix.io [](#__codelineno-25-20) > User-Agent: curl/7.61.1 [](#__codelineno-25-21) > Accept: */* [](#__codelineno-25-22) > [](#__codelineno-25-23) < HTTP/1.1 200 OK`

*   After configuring the Docker deamon, Please run the below `docker login` command to verify if Docker daemon is able to access CloudFabrix docker registry service.

`[](#__codelineno-26-1) docker login -u=readonly -p=readonly cfxregistry.cloudfabrix.io`

Example Output

`[](#__codelineno-27-1) WARNING! Using --password via the CLI is insecure. Use --password-stdin. [](#__codelineno-27-2) WARNING! Your password will be stored unencrypted in /home/rdauser/.docker/config.json. [](#__codelineno-27-3) Configure a credential helper to remove this warning. See [](#__codelineno-27-4) https://docs.docker.com/engine/reference/commandline/login/#credentials-store [](#__codelineno-27-5) [](#__codelineno-27-6) Login Succeeded`

**Login Succeeded** should be seen as shown in the above command's output.

**4\. RDAF platform resource requirements**
-------------------------------------------

RDA Fabric platform deployment can vary from simple to advanced depends on type of the environment and requirements.

A simple deployment can consist of one or more VMs for smaller and non-critical environments, while an advanced deployment consists of many RDA Fabric VMs to support high-availability, scale and for business critical environments.

**CloudFabrix provided OVF support:** VMware vSphere 6.0 or above

### **4.1 Single VM deployment:**

The below configuration can be used for a demo or POC environments. In this single VM configuration, all of RDA Fabric platform, infrastructure and application services will be installed.

For deployment and configuration options, Please refer **[OVF based deployment](#5-rdaf-platform-vms-deployment-using-ovf)
** or **[Deployment on RHEL/Ubuntu OS](#6-rdaf-platform-vms-deployment-on-rhelubuntu-os)
** section within this document.

| Quantity | VM Type | CPU / Memory / Network | Storage |
| --- | --- | --- | --- |
| 1   | `OVF Profile`: RDA Fabric Infra Instance  <br>`Services`: Platform, Infrastructure, Application & Worker | `CPU`: 8  <br>`Memory`: 64GB  <br>`Network`:1 Gbps/10 Gbps | `/ (root)`: 75GB  <br>`/opt`: 50GB  <br>`/var/lib/docker`: 100GB  <br>`/minio-data`: 50GB  <br>`/kafka-logs`: 25GB  <br>`/zookeeper`: 15GB  <br>`/var/mysql`: 50GB  <br>`/opensearch`: 50GB  <br>`/graphdb`: 50GB |

### **4.2 Distributed VM deployment:**

The below configuration can be used to distribute the RDA Fabric services for smaller or non-critical environments.

For deployment and configuration options, Please refer **[OVF based deployment](#5-rdaf-platform-vms-deployment-using-ovf)
** or **[Deployment on RHEL/Ubuntu OS](#6-rdaf-platform-vms-deployment-on-rhelubuntu-os)
** section within this document.

| Quantity | OVF Profile | CPU / Memory / Network | Storage |
| --- | --- | --- | --- |
| 1   | `OVF Profile`: RDA Fabric Infra Instance  <br>`Services`: Platform & Infrastructure | `CPU`: 8  <br>`Memory`: 32GB  <br>`Network`:1 Gbps/10 Gbps | `/ (root)`: 75GB  <br>`/opt`: 50GB  <br>`/var/lib/docker`: 50GB  <br>`/minio-data`: 50GB  <br>`/kafka-logs`: 25GB  <br>`/zookeeper`: 15GB  <br>`/var/mysql`: 50GB  <br>`/opensearch`: 50GB  <br>`/grapgdb`: 50GB |
| 1   | `OVF Profile`: RDA Fabric Platform Instance  <br>`Services`: Application (OIA/AIA) | `CPU`: 8  <br>`Memory`: 48GB  <br>`Network`:1 Gbps/10 Gbps | `/ (root)`: 75GB  <br>`/opt`: 50GB  <br>`/var/lib/docker`: 50GB |
| 1   | `OVF Profile`: RDA Fabric Platform Instance  <br>`Services`: RDA Worker | `CPU`: 8  <br>`Memory`: 32GB  <br>`Network`:1 Gbps/10 Gbps | `/ (root)`: 75GB  <br>`/opt`: 25GB  <br>`/var/lib/docker`: 25GB |

### **4.3 HA, Scale and Production deployment:**

The below configuration can be used to distribute the RDA Fabric services for production environment to be highly-available and to support larger workloads.

For deployment and configuration options, Please refer **[OVF based deployment](#5-rdaf-platform-vms-deployment-using-ovf)
** or **[Deployment on RHEL/Ubuntu OS](#6-rdaf-platform-vms-deployment-on-rhelubuntu-os)
** section within this document.

| Quantity | OVF Profile | CPU / Memory / Network | Storage |
| --- | --- | --- | --- |
| 3   | `OVF Profile`: RDA Fabric Infra Instance  <br>`Services`: Infrastructure | `CPU`: 8  <br>`Memory`: 48GB  <br>`Network`: 10 Gbps | **SSD Only**  <br>`/ (root)`: 75GB  <br>`/opt`: 50GB  <br>`/var/lib/docker`: 50GB  <br>`/minio-data`: 100GB  <br>`/kafka-logs`: 50GB  <br>`/zookeeper`: 25GB  <br>`/var/mysql`: 150GB  <br>`/opensearch`: 100GB  <br>`/graphdb`: 50GB |
| 2   | `OVF Profile`: RDA Fabric Platform Instance  <br>`Services`: RDA Platform | `CPU`: 4  <br>`Memory`: 24GB  <br>`Network`: 10 Gbps | `/ (root)`: 75GB  <br>`/opt`: 50GB  <br>`/var/lib/docker`: 50GB |
| 3 or more | `OVF Profile`: RDA Fabric Platform Instance  <br>`Services`: Application (OIA/AIA) | `CPU`: 8  <br>`Memory`: 48GB  <br>`Network`: 10 Gbps | `/ (root)`: 75GB  <br>`/opt`: 50GB  <br>`/var/lib/docker`: 50GB |
| 3 or more | `OVF Profile`: RDA Fabric Platform Instance  <br>`Services`: RDA Worker | `CPU`: 8  <br>`Memory`: 32GB  <br>`Network`: 10 Gbps | `/ (root)`: 75GB  <br>`/opt`: 25GB  <br>`/var/lib/docker`: 25GB |

Important

For a production rollout, RDA Fabric platform's resources such as **CPU**, **Memory** and **Storage** need to be sized appropriately depends on the environment size in terms of alert ingestion per minute, total number of assets for discovery and frequency, data retention of assets, alerts/events, incidents and observability data. Please contact **support@cloudfabrix.com** for a guidance on resource sizing.

Important

**Minio service** requires minimum of 4 VMs to run it in HA mode and to provide 1 node failure tolerance. For this requirement, an additional disk `/minio-data` need to be added on one of the RDA Fabric Platform or Application VMs. So, the Minio cluster service spans across 3 RDA Fabric Infrastructure VMs + 1 of the RDA Fabric Platform or Application VMs. Please refer **[Adding additional disk for Minio](#52-adding-additional-disk-for-minio-4th-ha-node)
** for more information on how to add and configure it.

### **4.4 Network layout and ports:**

Please refer the below picture which outlines the network access layout between the RDAF services and the used ports by them. These are applicable for both Kubernetes and non Kubernetes environments as well.

Tip

Please click on the picture below to enlarge and to go back to the page please click on the back arrow button on the top.

[![](https://bot-docs.cloudfabrix.io/images/rdaf_aiops_network_layout.png)](/images/rdaf_aiops_network_layout.png)

**RDAF Services & Network ports:**

| Service Type | Service Name | Network Ports |
| --- | --- | --- |
| RDAF Infrastructure Service | Minio | 9000/TCP (Internal)  <br>9443/TCP (External) |
| RDAF Infrastructure Service | MariDB | 3306/TCP (Internal)  <br>3307/TCP (Internal)  <br>4567/TCP (Internal)  <br>4568/TCP (Internal)  <br>4444/TCP (Internal) |
| RDAF Infrastructure Service | Opensearch | 9200/TCP (Internal)  <br>9300/TCP (Internal)  <br>9600/TCP (Internal) |
| RDAF Infrastructure Service | Kafka | 9092/TCP (Internal)  <br>9093/TCP (Internal & External) |
| RDAF Infrastructure Service | Zookeeper | 2181/TCP (Internal)  <br>2888/TCP (Internal) |
| RDAF Infrastructure Service | NATs | 4222/TCP (External)  <br>6222/TCP (Internal)  <br>8222/TCP (Internal) |
| RDAF Infrastructure Service | Redis | 6379/TCP (Internal) |
| RDAF Infrastructure Service | Redis-Sentinel | 26379/TCP (Internal) |
| RDAF Infrastructure Service | HAProxy | 443/TCP (External)  <br>7443/TCP (External)  <br>25/TCP (External)  <br>7222/TCP (External) |
| RDAF Core Platform Service | RDA API Server | 8807/TCP (Internal)  <br>8808/TCP (Internal) |
| RDAF Core Platform Service | RDA Portal Backend | 7780/TCP (Internal) |
| RDAF Core Platform Service | RDA Portal Frontend (Nginx) | 8080/TCP (Internal) |
| RDAF Application Service | RDA Webhook Server | 8888/TCP (Internal) |
| RDAF Application Service | RDA SMTP Server | 8456/TCP (Internal) |
| RDAF Monitoring Service | Log Monitoring | 5048/TCP (Internal)  <br>5049/TCP (External) |

**Internal Network ports:** These ports are used by RDAF services for internal communication between them.

**External Network ports:** These ports are exposed for incoming traffic into RDAF platform, such as, portal UI access, RDA Fabric access (NATs,Minio & Kafka) for RDA workers & agents that were deployed at the edge locations, Webhook based alerts, SMTP email based alerts etc.

**Asset Discovery and Integrations:** Network Ports

| Access Protocol Details | Endpoint Network Ports |
| --- | --- |
| **Windows AD or LDAP - Identity and Access Management** - RDAF platform  <br>\--> endpoints (Windows AD or LDAP) | 389/TCP  <br>636/TCP |
| **SSH based discovery** - RDA Worker/Agent (EdgeCollector)  <br>\--> endpoints (Ex: Linux/Unix, Network/Storage Devices) | 22/TCP |
| **HTTP API based discovery/Integration:**  <br>RDA Worker / AIOps app --> endpoints (Ex: SNOW, CMDB, vCenter, K8s, AWS etc..) | 443/TCP  <br>80/TCP  <br>8080/TCP |
| **Windows OS discovery using WinRM/SSH protocol**  <br>RDA Worker --> Windows Servers | 5985/TCP  <br>5986/TCP  <br>22/TCP |
| **SNMP based discovery:** - RDA Agent (EdgeCollector) --> endpoints (Ex: network devices like switches, routers,  <br>firewall, load balancers etc) | 161/UDP  <br>161/TCP |

**5\. RDAF platform VMs deployment using OVF**
----------------------------------------------

Download the latest OVF image from CloudFabrix (or contact support@cloudfabrix.com).

Supported VMware vSphere version: 6.5 or above

*   **OVF OS Version:** Ubuntu 20.04.4 LTS
    
*   **OVF Download Link:** [https://macaw-amer.s3.amazonaws.com/images/vmware/v2.0.11/CFX-Ubuntu-v2.0.11.zip](https://macaw-amer.s3.amazonaws.com/images/vmware/v2.0.11/CFX-Ubuntu-v2.0.11.zip)
    

**Step-1:** Login to VMware vCenter Webclient to install RDA Fabric platform VMs using the downloaded OVF image.

Info

**Note:** It is expected that the user who is deploying VMs for CloudFabrix RDA Fabric platform, have sufficient VMware vCenter privileges. Also, has necessary pre-requisite credentials and details handy (e.g IP Address/FQDN, Gateway, DNS & NTP server details).

**Step-2:** Select a vSphere cluster/resource pool in vCenter and right click on it and then select -> Deploy OVF Template as shown below.

![CFX-OVF-Step01](https://bot-docs.cloudfabrix.io/images/ovf/cfx-rda-ovf-step01.png)

**Step-3:** Select the OVF image from the location it was downloaded.

![CFX-OVF-Step02](https://bot-docs.cloudfabrix.io/images/ovf/cfx-rda-ovf-step02.png)

Info

**Note:** When VMware vSphere Webclient is used to deploy OVF, it expects to select all the files necessary to deploy OVF template. Select all the binary files (.ovf, .mf, .vmdk files) for deploying VM.

![CFX-OVF-Step03](https://bot-docs.cloudfabrix.io/images/ovf/cfx-rda-ovf-step03.png) ![CFX-OVF-Step04](https://bot-docs.cloudfabrix.io/images/ovf/cfx-rda-ovf-step04.png)

**Step-4:** Click Next and Enter appropriate '**VM Name**' and select an appropriate Datacenter on which it is going to be deployed.

![CFX-OVF-Step05](https://bot-docs.cloudfabrix.io/images/ovf/cfx-rda-ovf-step05.png)

**Step-5:** Click Next and select an appropriate vSphere Cluster / Resource pool where the RDA Fabric VM is going to be deployed.

![CFX-OVF-Step06](https://bot-docs.cloudfabrix.io/images/ovf/cfx-rda-ovf-step06.png)

**Step-6:** Click Next and you are navigated to deployment configuration view. The following configuration options are available to choose from during the deployment.

*   **RDA Fabric Platform Instance:** Select this option to deploy any of the RDA Fabric services such as Platform, Application, Worker, Event gateway and Edge collector. For HA configuration, multiple instances need to be provisioned.
    
*   **RDA Fabric Infra Instance:** Select this option to deploy RDA Fabric infrastructure services such as MariaDB, Kafka, Zookeeper, Minio, NATs, Redis and Opensearch. For HA configuration, multiple instances need to be provisioned.
    

![CFX-OVF-Step07](https://bot-docs.cloudfabrix.io/images/ovf/cfx-rda-ovf-step07.png)

**Step-7:** Click Next and you are navigated to selecting the Datastore (Virtual Storage). Select **Datastore / Datastore Cluster** where you want to deploy the VM. Make sure you select 'Thin Provision' option as highlighted in the below screenshot.

![CFX-OVF-Step08](https://bot-docs.cloudfabrix.io/images/ovf/cfx-rda-ovf-step08.png)

**Step-8:** Click Next and you are navigated to **Network port-group** view. Select the appropriate Virtual Network port-group as shown below.

![CFX-OVF-Step09](https://bot-docs.cloudfabrix.io/images/ovf/cfx-rda-ovf-step09.png)

**Step-9:** Click Next and you are taken to Network Settings/Properties as shown below. Please enter all the necessary details such as password, network settings and disk size as per the requirements.

*   Default OVF username and password is **rdauser** and **rdauser1234** (Update the password field to change default password)

Warning

**Note:** Please make sure to configure same password for **rdauser** user on all of the RDA Fabric VMs.

![CFX-OVF-Step10](https://bot-docs.cloudfabrix.io/images/ovf/cfx-rda-ovf-step10.png)

**Step-10:** Adjust the Disk size settings based on the environment size. For production deployments, please adjust the disk size for **/var/lib/docker** and **/opt** to 75GB.

![CFX-OVF-Step11](https://bot-docs.cloudfabrix.io/images/ovf/cfx-rda-ovf-step11.png)

**Step-11:** Click Next to see a summary of OVF deployment settings and Click on **Finish** to deploy the VM.

**Step-12:** Before powering ON the deployed VM, Edit the VM settings and adjust the **CPU** and **Memory** settings based on the environment size. For any help/guidance on resource sizing, please contact support@cloudfabrix.com.

**Step-13:** Power ON the Vs and wait until it is completely up with OVF settings. It usually takes around 2 to 5 minutes.

Info

**Note:** Repeat the above OVF deployment steps (step-1 through step-13) for provisioning additional required VMs for RDA Fabric platform.

### **5.1 Post OS Image / OVF Deployment Configuration**

Below steps are applicable for both Ubuntu 20.x and RHEL 8.x environments.

**Step 1:** Login into RDA Fabric VMs using any SSH client (ex: putty). Default username is **rdauser**

**Step 2:** Verify that NTP time is in sync on all of the RDA Fabric Platform, Infrastructure, Application, Worker & On-premise docker service VMs.

**Timezone settings:** Below are some of the useful commands to view / change / set Timezone on RDA Fabric VMs.

|     |     |
| --- | --- |
| [1](#__codelineno-28-1)<br>[2](#__codelineno-28-2)<br>[3](#__codelineno-28-3)<br>[4](#__codelineno-28-4)<br>[5](#__codelineno-28-5) | `sudo tzselect sudo timedatectl sudo timedatectl set-timezone Europe/London` |

Important

The **date & time** settings should be in **sync** across all of RDA Fabric VMs for the application services to function appropriately.

To manually sync VM's time with NTP server, run the below commands.

|     |     |
| --- | --- |
| [1](#__codelineno-29-1)<br>[2](#__codelineno-29-2)<br>[3](#__codelineno-29-3) | `sudo systemctl stop chronyd sudo chronyd -q 'server <ntp-server-ip> iburst' sudo systemctl start chronyd` |

To configure and update the NTP server settings, please update **/etc/chrony/chrony.conf** with NTP server details and restart the **Chronyd** service

|     |     |
| --- | --- |
| [1](#__codelineno-30-1)<br>[2](#__codelineno-30-2)<br>[3](#__codelineno-30-3)<br>[4](#__codelineno-30-4)<br>[5](#__codelineno-30-5)<br>[6](#__codelineno-30-6)<br>[7](#__codelineno-30-7) | `sudo systemctl stop chronyd sudo vi /etc/chrony/chrony.conf # Add the below line at the end of the file. Repeat the line for each NTP server's IP Address server <ntp-server-ip> prefer iburst sudo systemctl start chronyd` |

**Firewall Configuration:**

Ubuntu 20.xRHEL 8.x

Run the below commands to open or close application service ports within the firewall service if needed.

|     |     |
| --- | --- |
| [1](#__codelineno-31-1)<br>[2](#__codelineno-31-2) | `sudo ufw allow <port-number>/<tcp/udp> sudo ufw deny <port-number>/<tcp/udp>` |

Run the below commands to open or close application service ports within the firewall service if needed.

|     |     |
| --- | --- |
| [1](#__codelineno-32-1)<br>[2](#__codelineno-32-2)<br>[3](#__codelineno-32-3) | `sudo firewall-cmd --add-port <port-number>/<tcp/udp> --permanent sudo firewall-cmd --remove-port <port-number>/<tcp/udp> --permanent sudo firewall-cmd --reload` |

**Verify network bandwidth between RDAF VMs:**

For production deployment, the network bandwidth between RDAF VMs should be minimum of 10Gbps. CloudFabrix provided OVF comes with `iperf` utility which can be used to measure the network bandwidth.

UbuntuRHEL

To verify network bandwidth between RDAF platform service VM and infrastructure VM, follow the below steps.

Login into RDAF platform service VM as **rdauser** using SSH client to access the CLI and start `iperf` utility as a server.

Info

By default `iperf` listens on port **5001** over tcp

Enable the `iperf` server port using the below command.

`[](#__codelineno-33-1) sudo ufw allow 5001/tcp`

Start the `iperf` server as shown below.

`[](#__codelineno-34-1) iperf -s`

Example Output

`[](#__codelineno-35-1) $ iperf -s [](#__codelineno-35-2) [](#__codelineno-35-3) ------------------------------------------------------------ [](#__codelineno-35-4) Server listening on TCP port 5001 [](#__codelineno-35-5) TCP window size: 85.3 KByte (default) [](#__codelineno-35-6) ------------------------------------------------------------`

Now, login into RDAF infrastructure service VM as **rdauser** using SSH client to access the CLI and start `iperf` utility as a client.

`[](#__codelineno-36-1) iperf -c <RDAF-Platform-VM-IP>`

`operf` utility connects to RDAF platform service VM as shown below. It will connect and verify the network bandwidth speed.

Example Output

`[](#__codelineno-37-1) ------------------------------------------------------------ [](#__codelineno-37-2) Client connecting to 192.168.125.143, TCP port 5001 [](#__codelineno-37-3) TCP window size: 2.86 MByte (default) [](#__codelineno-37-4) ------------------------------------------------------------ [](#__codelineno-37-5) [  3] local 192.168.125.141 port 10654 connected with 192.168.125.143 port 5001 [](#__codelineno-37-6) [ ID] Interval       Transfer     Bandwidth [](#__codelineno-37-7) [  3]  0.0-10.0 sec  21.2 GBytes  18.2 Gbits/sec`

Repeat the above steps between all of the RDAF VMs in both directions to make sure the network bandwidth speed is minimum of 10Gbps.

To verify network bandwidth between RDAF platform service VM and infrastructure VM, follow the below steps.

Login into RDAF platform service VM as **rdauser** using SSH client to access the CLI and start `iperf` utility as a server.

Info

By default `iperf` listens on port **5001** over tcp

Enable the `iperf` server port using the below command.

`[](#__codelineno-38-1) sudo firewall-cmd --add-port 5001/tcp --permanent [](#__codelineno-38-2) sudo firewall-cmd --reload`

Start the `iperf` server as shown below.

`[](#__codelineno-39-1) iperf -s`

`[](#__codelineno-40-1) $ iperf -s [](#__codelineno-40-2) [](#__codelineno-40-3) ------------------------------------------------------------ [](#__codelineno-40-4) Server listening on TCP port 5001 [](#__codelineno-40-5) TCP window size: 85.3 KByte (default) [](#__codelineno-40-6) ------------------------------------------------------------`

Now, login into RDAF infrastructure service VM as **rdauser** using SSH client to access the CLI and start `iperf` utility as a client.

`[](#__codelineno-41-1) iperf -c <RDAF-Platform-VM-IP>`

`operf` utility connects to RDAF platform service VM as shown below. It will connect and verify the network bandwidth speed.

Example Output

`[](#__codelineno-42-1) ------------------------------------------------------------ [](#__codelineno-42-2) Client connecting to 192.168.125.143, TCP port 5001 [](#__codelineno-42-3) TCP window size: 2.86 MByte (default) [](#__codelineno-42-4) ------------------------------------------------------------ [](#__codelineno-42-5) [  3] local 192.168.125.141 port 10654 connected with 192.168.125.143 port 5001 [](#__codelineno-42-6) [ ID] Interval       Transfer     Bandwidth [](#__codelineno-42-7) [  3]  0.0-10.0 sec  21.2 GBytes  18.2 Gbits/sec`

Repeat the above steps between all of the RDAF VMs in both directions to make sure the network bandwidth speed is minimum of 10Gbps.

### **5.2 Adding additional disk for Minio 4th HA node**

Info

This step is only applicable for Minio infrastructure service when RDA Fabric VMs are deployed in HA configuration. Minio service requires minimum of 4 nodes to form HA cluster to provide 1 node failure tolerance.

**Step-1:** Login into VMware vCenter and Shutdown one of the RDA Fabric platform or application services VM.

**Step-2:** Edit the VM settings of RDA Fabric platform services VM that was shutdown in the above. Add a new disk and allocate the same size as other Minio service nodes. Please refer **[Minio disk size (/minio-data) for HA configuration](#43-ha-scale-and-production-deployment)
**

**Step-3:** Edit the VM settings of RDA Fabric platform services VM again on which new disk was added and note down the SCSI Disk ID as shown below.

![CFX-OVF-Add-Disk](https://bot-docs.cloudfabrix.io/images/ovf/cfx-rda-ovf-add-new-disk.png)

**Step-4:** Power ON the RDA Fabric platform services VM on which a new disk has been added in the above step.

**Step-5:** Login into RDA Fabric Platform VM using any SSH client (ex: putty). Default username is **rdauser**

**Step-6:** Run the below command to list all of the SCSI disks of the VM with their SCSI Disk IDs

|     |     |
| --- | --- |
| [1](#__codelineno-43-1) | `lsblk -S` |

Example Output

`[](#__codelineno-44-1) NAME HCTL       TYPE VENDOR   MODEL         REV TRAN [](#__codelineno-44-2) sda  2:0:0:0    disk VMware   Virtual_disk 1.0   [](#__codelineno-44-3) sdb  2:0:1:0    disk VMware   Virtual_disk 1.0   [](#__codelineno-44-4) sdc  2:0:2:0    disk VMware   Virtual_disk 1.0   [](#__codelineno-44-5) sdd  2:0:3:0    disk VMware   Virtual_disk 1.0`

Run the below command to see the new disk along with used disks with their mount points

|     |     |
| --- | --- |
| [1](#__codelineno-45-1) | `lsblk` |

Example Output

`[](#__codelineno-46-1) NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT [](#__codelineno-46-2) ... [](#__codelineno-46-3) sda                         8:0    0   75G  0 disk  [](#__codelineno-46-4) ├─sda1                      8:1    0    1M  0 part  [](#__codelineno-46-5) ├─sda2                      8:2    0  1.5G  0 part /boot [](#__codelineno-46-6) └─sda3                      8:3    0 48.5G  0 part  [](#__codelineno-46-7)   └─ubuntu--vg-ubuntu--lv 253:0    0 48.3G  0 lvm  / [](#__codelineno-46-8) sdb                         8:16   0   25G  0 disk /var/lib/docker [](#__codelineno-46-9) sdc                         8:32   0   25G  0 disk /opt [](#__codelineno-46-10) sdd                         8:48   0   50G  0 disk`

In the above example command outputs, the newly added disk is **sdd** and it's size is 50GB

**Step-7:** Run the below command to create a new **XFS** filesystem and create a mount point directory.

|     |     |
| --- | --- |
| [1](#__codelineno-47-1)<br>[2](#__codelineno-47-2) | `sudo mkfs.xfs /dev/sdd sudo mkdir /minio-data` |

**Step-8:** Run the below command to get the **UUID** of the newly created filesystem on **/dev/sdd**

|     |     |
| --- | --- |
| [1](#__codelineno-48-1) | `sudo blkid /dev/sdd` |

**Step-9:** Update **/etc/fstab** to mount the **/dev/sdd** disk to **/minio-data** mount point

|     |     |
| --- | --- |
| [1](#__codelineno-49-1) | `sudo vi /etc/fstab` |

Add the below line and save the **/etc/fstab** file.

|     |     |
| --- | --- |
| [1](#__codelineno-50-1) | `UUID=<UUID-from-step-8>    /minio-data   xfs defaults    0   0` |

**Step-10:** Mount the **/minio-data** mount point and verify the mount point is mounted.

|     |     |
| --- | --- |
| [1](#__codelineno-51-1)<br>[2](#__codelineno-51-2)<br>[3](#__codelineno-51-3) | `sudo mount -a df -h` |

Example Output

`[](#__codelineno-52-1) Filesystem                         Size  Used Avail Use% Mounted on [](#__codelineno-52-2) /dev/mapper/ubuntu--vg-ubuntu--lv   48G  8.3G   37G  19% / [](#__codelineno-52-3) ... [](#__codelineno-52-4) /dev/sda2                          1.5G  209M  1.2G  16% /boot [](#__codelineno-52-5) /dev/sdb                            25G  211M   25G   1% /var/lib/docker [](#__codelineno-52-6) /dev/sdc                            25G  566M   25G   3% /opt [](#__codelineno-52-7) /dev/sdd                            50G  390M   50G   1% /minio-data`

### **5.3 Extending the Root (/) filesystem**

Ubuntu

Warning

**Note-1:** The below provided instructions to extend the **Root (/)** filesystem are applicable only for the virtual machines that are provisioned using CloudFabrix provided Ubuntu OVF

**Note-2:** As a precautionary step, please take VMware VM snapshot before making the changes to **Root (/)** filesystem.

**Step-1:** Check on which disk the **Root (/)** filesystem was created using the below command. In the below example, it was created on disk **/dev/sda** and **partition 3** i.e. **sda3**.

On partition **sda3**, a logical volume **ubuntu--vg-ubuntu--lv** was created and mounted as **Root (/)** filesystem.

`[](#__codelineno-53-1) lsblk`

Example Output

`[](#__codelineno-54-1) NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT [](#__codelineno-54-2) loop0                       7:0    0   62M  1 loop  [](#__codelineno-54-3) loop1                       7:1    0   62M  1 loop /snap/core20/1593 [](#__codelineno-54-4) loop2                       7:2    0 67.2M  1 loop /snap/lxd/21835 [](#__codelineno-54-5) loop3                       7:3    0 67.8M  1 loop /snap/lxd/22753 [](#__codelineno-54-6) loop4                       7:4    0 44.7M  1 loop /snap/snapd/15904 [](#__codelineno-54-7) loop5                       7:5    0   47M  1 loop /snap/snapd/16292 [](#__codelineno-54-8) loop7                       7:7    0   62M  1 loop /snap/core20/1611 [](#__codelineno-54-9) sda                         8:0    0   75G  0 disk  [](#__codelineno-54-10) ├─sda1                      8:1    0    1M  0 part  [](#__codelineno-54-11) ├─sda2                      8:2    0  1.5G  0 part /boot [](#__codelineno-54-12) └─sda3                      8:3    0 48.5G  0 part  [](#__codelineno-54-13) └─ubuntu--vg-ubuntu--lv     253:0  0 48.3G  0 lvm  / [](#__codelineno-54-14) sdb                         8:16   0  100G  0 disk /var/lib/docker [](#__codelineno-54-15) sdc                         8:32   0   75G  0 disk /opt`

**Step-2:** Verify the **SCSI disk id** of the disk on which **Root (/)** filesystem was created using the below command.

In the below example, the SCSI disk id of root disk **sda** is 2:0:0:0, i.e. the SCSI disk id is 0 (third digit)

`[](#__codelineno-55-1) lsblk -S`

Example Output

`[](#__codelineno-56-1) NAME HCTL       TYPE VENDOR   MODEL         REV TRAN [](#__codelineno-56-2) sda  2:0:0:0    disk VMware   Virtual_disk 1.0   [](#__codelineno-56-3) sdb  2:0:1:0    disk VMware   Virtual_disk 1.0   [](#__codelineno-56-4) sdc  2:0:2:0    disk VMware   Virtual_disk 1.0`  

**Step-3:** Edit the virtual machine's properties on vCenter and identify the Root disk **sda** using the above SCSI disk id **2:0:0:0** as highlighted in the below screenshot.

Increase the disk size from 75GB to higher desired value in GB.

![CFXOVFRootExtend](https://bot-docs.cloudfabrix.io/images/ovf/ubuntu_ovf_extend_root_disk.png)

**Step-4:** Login back to Ubuntu VM CLI using SSH client as **rdauser**

Switch to **sudo** user

`[](#__codelineno-57-1) sudo -s`

Execute the below command to rescan the **Root disk** i.e. **sda** to reflect the increased disk size.

`[](#__codelineno-58-1) echo '1' > /sys/class/scsi_disk/2\:0\:0\:0/device/rescan`

Execute the below command to see the increased size for Root disk **sda**

`[](#__codelineno-59-1) lsblk`

Example Output

`[](#__codelineno-60-1) NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT [](#__codelineno-60-2) loop0                       7:0    0   62M  1 loop /snap/core20/1611 [](#__codelineno-60-3) loop1                       7:1    0 67.8M  1 loop /snap/lxd/22753 [](#__codelineno-60-4) loop2                       7:2    0 67.2M  1 loop /snap/lxd/21835 [](#__codelineno-60-5) loop3                       7:3    0   62M  1 loop  [](#__codelineno-60-6) loop4                       7:4    0   47M  1 loop /snap/snapd/16292 [](#__codelineno-60-7) loop5                       7:5    0 44.7M  1 loop /snap/snapd/15904 [](#__codelineno-60-8) loop6                       7:6    0   62M  1 loop /snap/core20/1593 [](#__codelineno-60-9) sda                         8:0    0  100G  0 disk  [](#__codelineno-60-10) ├─sda1                      8:1    0    1M  0 part  [](#__codelineno-60-11) ├─sda2                      8:2    0  1.5G  0 part /boot [](#__codelineno-60-12) └─sda3                      8:3    0 48.5G  0 part  [](#__codelineno-60-13) └─ubuntu--vg-ubuntu--lv     253:0  0 48.3G  0 lvm  / [](#__codelineno-60-14) sdb                         8:16   0   25G  0 disk /var/lib/docker [](#__codelineno-60-15) sdc                         8:32   0   25G  0 disk /opt`

**Step-5:** In the above command output, identify the **Root (/) filesystem's** disk partition, i.e. **sda3**

Run the below command **cfdisk** to resize the **Root (/)** filesystem.

`[](#__codelineno-61-1) cfdisk`

*   Highlight **/dev/sda3** partition using **Down** arrow on the keyboard as shown in the below screen, use **Left/Right** arrow to highlight the **Resize** option and hit **Enter**

![CFXOVFRootResize01](https://bot-docs.cloudfabrix.io/images/ovf/ubuntu_resize_root_disk_01.png)

*   Adjust the disk **Resize** in **GB** as desired.

Warning

The **Resize** disk value in GB cannot be smaller than the current size of the **Root (/)** filesystem.

![CFXOVFRootResize02](https://bot-docs.cloudfabrix.io/images/ovf/ubuntu_resize_root_disk_02.png)

*   Once the **/dev/sda3** partition is resized, use **Left/Right** arrow to highlight the **Write** option and hit **Enter**
*   Confirm the resize by typing **yes** and hit **Enter**
*   Use **Left/Right** arrow to highlight the **Quit** option and hit **Enter** to quit the Disk resizing utility.

![CFXOVFRootResize03](https://bot-docs.cloudfabrix.io/images/ovf/ubuntu_resize_root_disk_03.png) ![CFXOVFRootResize04](https://bot-docs.cloudfabrix.io/images/ovf/ubuntu_resize_root_disk_04.png)

**Step-6:**

Disable the swap before resizing the **Root (/)** filesystem using the below command.

`[](#__codelineno-62-1) swapoff /swap.img`

Resize the physical volume of **Root (/)** filesystem i.e. **/dev/sda3**

`[](#__codelineno-63-1) pvresize /dev/sda3`

Resize the logical volume of **Root (/) filesystem** i.e. **/dev/mapper/ubuntu--vg-ubuntu--lv**. In the below example, the logical volume of **Root (/)** filesystem is increased by 20GB

`[](#__codelineno-64-1) lvextend -L +20G /dev/mapper/ubuntu--vg-ubuntu--lv`

Resize the **Root (/) filesystem**

`[](#__codelineno-65-1) resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv`

Enable the swap after resizing the **Root (/)** filesystem

`[](#__codelineno-66-1) swapon /swap.img`

**Step-7:**

Verify the increased **Root (/)** filesystem disk's space using the below command.

`[](#__codelineno-67-1) df -h`

`[](#__codelineno-68-1) Filesystem                         Size  Used Avail Use% Mounted on [](#__codelineno-68-2) udev                               3.9G     0  3.9G   0% /dev [](#__codelineno-68-3) tmpfs                              793M   50M  744M   7% /run [](#__codelineno-68-4) /dev/mapper/ubuntu--vg-ubuntu--lv   68G  8.6G   56G  14% / [](#__codelineno-68-5) tmpfs                              3.9G     0  3.9G   0% /dev/shm [](#__codelineno-68-6) tmpfs                              5.0M     0  5.0M   0% /run/lock [](#__codelineno-68-7) tmpfs                              3.9G     0  3.9G   0% /sys/fs/cgroup [](#__codelineno-68-8) /dev/loop2                          68M   68M     0 100% /snap/lxd/21835 [](#__codelineno-68-9) /dev/loop4                          47M   47M     0 100% /snap/snapd/16292 [](#__codelineno-68-10) /dev/loop1                          68M   68M     0 100% /snap/lxd/22753 [](#__codelineno-68-11) /dev/loop5                          45M   45M     0 100% /snap/snapd/15904 [](#__codelineno-68-12) /dev/sda2                          1.5G  209M  1.2G  16% /boot [](#__codelineno-68-13) /dev/sdb                            25G  211M   25G   1% /var/lib/docker [](#__codelineno-68-14) /dev/sdc                            25G  566M   25G   3% /opt`

**6\. RDAF Platform VMs deployment on RHEL/Ubuntu OS**
------------------------------------------------------

Below steps outlines the required pre-requisites and the configuration to be applied on RHEL or Ubuntu OS VM instances when CloudFabrix provided OVF is not used, to deploy and install RDA Fabric platform, infrastructure, application, worker and on-premise docker registry services.

**Software Pre-requisites:**

*   **RHEL:** RHEL 8.3 or above
*   **Ubuntu:** Ubuntu 20.04.x or above
*   **Python:** 3.7.4 or above
*   **Docker:** 20.10.x or above
*   **Docker-compose:** 1.29.x or above

For resource requirements such as CPU, Memory, Network and Storage, please refer **[RDA Fabric VMs resource requirements](#4-rdaf-platform-resource-requirements)
**

RHELUbuntu

*   Once RHEL 8.3 or above OS version is deployed, register and apply the OS licenses using the below commands

`[](#__codelineno-69-1) sudo subscription-manager register [](#__codelineno-69-2) sudo subscription-manager attach`

*   Create a new user called **rdauser** and configure the password.

`[](#__codelineno-70-1) sudo adduser rdauser [](#__codelineno-70-2) sudo passwd rdauser [](#__codelineno-70-3) sudo chown -R rdauser:rdauser /home/rdauser [](#__codelineno-70-4) sudo groupadd docker [](#__codelineno-70-5) sudo usermod -aG docker rdauser`

*   Add **rdauser** to **/etc/sudoers** file. Add the below line at the end of the sudoers file.

`[](#__codelineno-71-1) rdauser ALL=(ALL) NOPASSWD:ALL`

*   Modify the SSH service configuration with the below settings. Edit **/etc/ssh/sshd\_config** file and update the below settings as shown below.

`[](#__codelineno-72-1) PasswordAuthentication yes [](#__codelineno-72-2) MaxSessions 10 [](#__codelineno-72-3) LoginGraceTime 2m`

*   Restart the SSH service

`[](#__codelineno-73-1) sudo systemctl restart sshd`

*   Logout and Login back as newly created user **rdauser**
    
*   Format the disks with **xfs** filesystem and mount the disks as per the disk requirements outlined in **[RDA Fabric VMs resource requirements](#4-rdaf-platform-resource-requirements)
    ** section.
    

`[](#__codelineno-74-1) sudo mkfs.xfs /dev/<disk-name>`

*   Make sure disk mounts are updated in **/etc/fstab** to make them persistent across VM reboots.
    
*   In /etc/fstab, use filesystem's **UUID** instead of using SCSI disk names. Below command provides **UUID** of filesystem created on a disk or disk partition.
    

`[](#__codelineno-75-1) sudo blkid /dev/<disk-name>`

Sample disk mount point entry on **/etc/fstab** file.

`[](#__codelineno-76-1) UUID=60174ace-e1f6-497e-90e2-7d889e6c5695    /opt   xfs defaults    0   0`

**Installing OS utilities and Python**

*   Run the below commands to install the required software packages.

|     |     |
| --- | --- |
| [1](#__codelineno-77-1)<br>[2](#__codelineno-77-2)<br>[3](#__codelineno-77-3)<br>[4](#__codelineno-77-4)<br>[5](#__codelineno-77-5) | `sudo yum install -y gcc openssl-devel bzip2-devel sqlite-devel xz-devel ncurses-devel readline readline-devel gdbm-devel tcl-devel tk-devel make libffi-devel or sudo dnf install -y gcc openssl-devel bzip2-devel sqlite-devel xz-devel ncurses-devel readline readline-devel gdbm-devel tcl-devel tk-devel make libffi-devel` |

|     |     |
| --- | --- |
| [1](#__codelineno-78-1)<br>[2](#__codelineno-78-2)<br>[3](#__codelineno-78-3)<br>[4](#__codelineno-78-4)<br>[5](#__codelineno-78-5) | `sudo yum install -y install -y wget telnet net-tools unzip tar sysstat bind-utils iperf3 xinetd jq yum-utils device-mapper-persistent-data lvm2 mysql or sudo dnf install -y install -y wget telnet net-tools unzip tar sysstat bind-utils iperf3 xinetd jq yum-utils device-mapper-persistent-data lvm2 mysql` |

*   Download and install the below software packages.

|     |     |
| --- | --- |
| [1](#__codelineno-79-1)<br>[2](#__codelineno-79-2)<br>[3](#__codelineno-79-3) | `wget https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/s/sshpass-1.06-9.el8.x86_64.rpm sudo rpm -ivh sshpass-1.06-9.el8.x86_64.rpm` |

|     |     |
| --- | --- |
| [1](#__codelineno-80-1)<br>[2](#__codelineno-80-2)<br>[3](#__codelineno-80-3) | `wget https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/n/nload-0.7.4-16.el8.x86_64.rpm sudo rpm -ivh nload-0.7.4-16.el8.x86_64.rpm` |

*   Download and install **Python 3.7.4** or above. Skip this step if **Python** is already installed as part of the OS install.

|     |     |
| --- | --- |
| [1](#__codelineno-81-1)<br> [2](#__codelineno-81-2)<br> [3](#__codelineno-81-3)<br> [4](#__codelineno-81-4)<br> [5](#__codelineno-81-5)<br> [6](#__codelineno-81-6)<br> [7](#__codelineno-81-7)<br> [8](#__codelineno-81-8)<br> [9](#__codelineno-81-9)<br>[10](#__codelineno-81-10)<br>[11](#__codelineno-81-11)<br>[12](#__codelineno-81-12)<br>[13](#__codelineno-81-13)<br>[14](#__codelineno-81-14)<br>[15](#__codelineno-81-15)<br>[16](#__codelineno-81-16)<br>[17](#__codelineno-81-17)<br>[18](#__codelineno-81-18)<br>[19](#__codelineno-81-19)<br>[20](#__codelineno-81-20)<br>[21](#__codelineno-81-21)<br>[22](#__codelineno-81-22)<br>[23](#__codelineno-81-23)<br>[24](#__codelineno-81-24)<br>[25](#__codelineno-81-25)<br>[26](#__codelineno-81-26)<br>[27](#__codelineno-81-27) | `cd /opt sudo wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz sudo tar xvf Python-3.7.4.tgz sudo chown -R rdauser:rdauser Python-3.7.4 cd /opt/Python-3.7.4 ./configure --enable-optimizations sudo make -j8 build_all sudo make altinstall sudo /usr/local/bin/python3.7 -m venv /opt/PYTHON37 sudo chown -R rdauser:rdauser /opt/PYTHON37 sudo rm -f /opt/Python-3.7.4.tgz sudo alternatives --set python /usr/bin/python3.7 sudo ln -s /usr/local/bin/python3.7 /usr/bin/python sudo ln -s /usr/local/bin/pip3.7 /usr/bin/pip` |

**Installing Docker and Docker-compose**

*   Run the below commands to install docker runtime environment

|     |     |
| --- | --- |
| [1](#__codelineno-82-1)<br>[2](#__codelineno-82-2)<br>[3](#__codelineno-82-3)<br>[4](#__codelineno-82-4)<br>[5](#__codelineno-82-5) | `sudo yum config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo or sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo` |

|     |     |
| --- | --- |
| [1](#__codelineno-83-1)<br>[2](#__codelineno-83-2)<br>[3](#__codelineno-83-3)<br>[4](#__codelineno-83-4)<br>[5](#__codelineno-83-5) | `sudo yum -y install --nobest --allowerasing docker-ce-20.10.5-3.el8 or sudo dnf -y install --nobest --allowerasing docker-ce-20.10.5-3.el8` |

|     |     |
| --- | --- |
| [1](#__codelineno-84-1)<br>[2](#__codelineno-84-2)<br>[3](#__codelineno-84-3) | `sudo systemctl enable docker sudo systemctl start docker sudo systemctl status docker` |

*   Configure docker service configuration updating **/etc/docker/daemon.json** as shown below.

`[](#__codelineno-85-1) sudo vi /etc/docker/daemon.json`

|     |     |
| --- | --- |
| [1](#__codelineno-86-1)<br> [2](#__codelineno-86-2)<br> [3](#__codelineno-86-3)<br> [4](#__codelineno-86-4)<br> [5](#__codelineno-86-5)<br> [6](#__codelineno-86-6)<br> [7](#__codelineno-86-7)<br> [8](#__codelineno-86-8)<br> [9](#__codelineno-86-9)<br>[10](#__codelineno-86-10)<br>[11](#__codelineno-86-11)<br>[12](#__codelineno-86-12)<br>[13](#__codelineno-86-13)<br>[14](#__codelineno-86-14)<br>[15](#__codelineno-86-15) | `{ "tls": true,  "tlscacert": "/etc/tlscerts/ca/ca.pem",  "tlsverify": true,  "storage-driver": "overlay2",  "hosts": [ "unix:///var/run/docker.sock",  "tcp://0.0.0.0:2376" ],  "tlskey": "/etc/tlscerts/server/server.key",  "debug": false,  "tlscert": "/etc/tlscerts/server/server.pem",  "experimental": false,  "live-restore": true }` |

*   Download and execute macaw-docker.py script to configure TLS for docker service. (Note: Make sure python2.7 is installed)

|     |     |
| --- | --- |
| [1](#__codelineno-87-1)<br>[2](#__codelineno-87-2)<br>[3](#__codelineno-87-3)<br>[4](#__codelineno-87-4)<br>[5](#__codelineno-87-5)<br>[6](#__codelineno-87-6)<br>[7](#__codelineno-87-7)<br>[8](#__codelineno-87-8)<br>[9](#__codelineno-87-9) | `mkdir ~/cfx-config-files cd ~/cfx-config-files wget https://macaw-amer.s3.amazonaws.com/images/misc/RHEL-bin-files.tar.gz tar -xzvf RHEL-bin-files.tar.gz sudo python2.7 macaw-docker.py` |

*   Edit **/lib/systemd/system/docker.service** file and update the below line and restart the docker service

`[](#__codelineno-88-1) From: [](#__codelineno-88-2) ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock [](#__codelineno-88-3) [](#__codelineno-88-4) To: [](#__codelineno-88-5) ExecStart=/usr/bin/dockerd`

*   Restart docker service and verify the status

|     |     |
| --- | --- |
| [1](#__codelineno-89-1)<br>[2](#__codelineno-89-2) | `sudo systemctl restart docker sudo systemctl status docker` |

*   Update `/etc/sysctl.conf` file with below performance tuning settings.

`[](#__codelineno-90-1) #Performance Tuning. [](#__codelineno-90-2) net.ipv4.tcp_rmem = 4096 87380 16777216 [](#__codelineno-90-3) net.ipv4.tcp_wmem = 4096 65536 16777216 [](#__codelineno-90-4) net.core.rmem_max = 16777216 [](#__codelineno-90-5) net.core.wmem_max = 16777216 [](#__codelineno-90-6) net.core.netdev_max_backlog = 2500 [](#__codelineno-90-7) net.core.somaxconn = 65000 [](#__codelineno-90-8) net.ipv4.tcp_ecn = 0 [](#__codelineno-90-9) net.ipv4.tcp_window_scaling = 1 [](#__codelineno-90-10) net.ipv4.ip_local_port_range = 10000 65535 [](#__codelineno-90-11) vm.max_map_count = 1048575 [](#__codelineno-90-12) net.core.wmem_default=262144 [](#__codelineno-90-13) net.core.wmem_max=4194304 [](#__codelineno-90-14) net.core.rmem_default=262144 [](#__codelineno-90-15) net.core.rmem_max=4194304 [](#__codelineno-90-16) [](#__codelineno-90-17) #file max [](#__codelineno-90-18) fs.file-max=518144 [](#__codelineno-90-19) [](#__codelineno-90-20) #swapiness [](#__codelineno-90-21) vm.swappiness = 1 [](#__codelineno-90-22) #Set runtime for kernel.randomize_va_space [](#__codelineno-90-23) kernel.randomize_va_space = 2 [](#__codelineno-90-24) [](#__codelineno-90-25) net.ipv4.ip_forward = 1 [](#__codelineno-90-26) net.ipv4.ip_nonlocal_bind=1`

*   Install **JAVA** software package

|     |     |
| --- | --- |
| [1](#__codelineno-91-1)<br>[2](#__codelineno-91-2) | `sudo mkdir -p /opt/java sudo tar xf ~/cfx-config-files/jdk-8u281-linux-x64.tar.gz -C /opt/java --strip-components 1` |

*   Add the **JAVA** software binary to **PATH** variable

`[](#__codelineno-92-1) vi ~/.bash_profile [](#__codelineno-92-2) PATH=/opt/java/bin:$PATH`

`[](#__codelineno-93-1) source ~/.bash_profile`

*   Reboot the host

`[](#__codelineno-94-1) sudo reboot`

*   Once Ubuntu 20.04.x or above OS version is deployed, please apply the below configuration.
    
*   Create a new user called **rdauser** and configure the password.
    

`[](#__codelineno-95-1) sudo adduser rdauser [](#__codelineno-95-2) sudo passwd rdauser`

`[](#__codelineno-96-1) sudo chown -R rdauser:rdauser /home/rdauser [](#__codelineno-96-2) sudo groupadd docker [](#__codelineno-96-3) sudo usermod -aG docker rdauser`

*   Add **rdauser** to **/etc/sudoers** file. Add the below line at the end of the sudoers file.

`[](#__codelineno-97-1) rdauser ALL=(ALL) NOPASSWD:ALL`

*   Modify the SSH service configuration with the below settings. Edit **/etc/ssh/sshd\_config** file and update as shown below.

`[](#__codelineno-98-1) PasswordAuthentication yes [](#__codelineno-98-2) MaxSessions 10 [](#__codelineno-98-3) LoginGraceTime 2m`

*   Restart the SSH service

`[](#__codelineno-99-1) sudo systemctl restart sshd`

*   Logout and Login back as newly created user **rdauser**
    
*   Format the disks with **xfs** filesystem and mount the disks as per the disk requirements outlined in **[RDA Fabric VMs resource requirements](#4-rdaf-platform-resource-requirements)
    ** section.
    

`[](#__codelineno-100-1) sudo mkfs.xfs /dev/<disk-name>`

*   Make sure disk mounts are updated in **/etc/fstab** to make them persistent across VM reboots.
    
*   In /etc/fstab, use filesystem's **UUID** instead of using SCSI disk names. Below command provides **UUID** of filesystem created on a disk or disk partition.
    

`[](#__codelineno-101-1) sudo blkid /dev/<disk-name>`

Sample disk mount point entry on **/etc/fstab** file.

`[](#__codelineno-102-1) UUID=60174ace-e1f6-497e-90e2-7d889e6c5695    /opt   xfs defaults    0   0`

**Installing OS utilities and Python**

*   Run the below commands to install the required software packages.

`[](#__codelineno-103-1) sudo apt update`

|     |     |
| --- | --- |
| [1](#__codelineno-104-1) | `sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev` |

|     |     |
| --- | --- |
| [1](#__codelineno-105-1) | `sudo apt install -y wget telnet net-tools unzip tar sysstat bind9-utils iperf3 xinetd jq lvm2 sshpass mysql-client` |

*   Download and install **Python 3.7.4** or above. Skip this step if **Python 3.7.4 or above** is already installed as part of the OS install.

|     |     |
| --- | --- |
| [1](#__codelineno-106-1)<br> [2](#__codelineno-106-2)<br> [3](#__codelineno-106-3)<br> [4](#__codelineno-106-4)<br> [5](#__codelineno-106-5)<br> [6](#__codelineno-106-6)<br> [7](#__codelineno-106-7)<br> [8](#__codelineno-106-8)<br> [9](#__codelineno-106-9)<br>[10](#__codelineno-106-10)<br>[11](#__codelineno-106-11)<br>[12](#__codelineno-106-12)<br>[13](#__codelineno-106-13)<br>[14](#__codelineno-106-14)<br>[15](#__codelineno-106-15)<br>[16](#__codelineno-106-16)<br>[17](#__codelineno-106-17)<br>[18](#__codelineno-106-18)<br>[19](#__codelineno-106-19)<br>[20](#__codelineno-106-20)<br>[21](#__codelineno-106-21)<br>[22](#__codelineno-106-22)<br>[23](#__codelineno-106-23)<br>[24](#__codelineno-106-24)<br>[25](#__codelineno-106-25)<br>[26](#__codelineno-106-26)<br>[27](#__codelineno-106-27) | `cd /opt sudo wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz sudo tar xvf Python-3.7.4.tgz sudo chown -R rdauser:rdauser Python-3.7.4 cd /opt/Python-3.7.4 ./configure --enable-optimizations sudo make -j8 build_all sudo make altinstall sudo /usr/local/bin/python3.7 -m venv /opt/PYTHON37 sudo chown -R rdauser:rdauser /opt/PYTHON37 sudo rm -f /opt/Python-3.7.4.tgz sudo alternatives --set python /usr/bin/python3.7 sudo ln -s /usr/local/bin/python3.7 /usr/bin/python sudo ln -s /usr/local/bin/pip3.7 /usr/bin/pip` |

**Installing Docker and Docker-compose**

*   Run the below commands to install docker runtime environment

|     |     |
| --- | --- |
| [1](#__codelineno-107-1) | `sudo apt-get install -y ca-certificates curl gnupg lsb-release` |

|     |     |
| --- | --- |
| [1](#__codelineno-108-1)<br>[2](#__codelineno-108-2)<br>[3](#__codelineno-108-3)<br>[4](#__codelineno-108-4) | `sudo mkdir -p /etc/apt/keyrings curl -fsSL https://download.docker.com/linux/ubuntu/gpg \| sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \       $(lsb_release -cs) stable" \| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null` |

|     |     |
| --- | --- |
| [1](#__codelineno-109-1) | `sudo apt-get update -y` |

|     |     |
| --- | --- |
| [1](#__codelineno-110-1) | `sudo apt-get install docker-ce=5:20.10.12~3-0~ubuntu-focal docker-ce-cli=5:20.10.12~3-0~ubuntu-focal containerd.io docker-compose-plugin` |

|     |     |
| --- | --- |
| [1](#__codelineno-111-1) | `sudo systemctl enable docker` |

*   Edit **/lib/systemd/system/docker.service** file and update the below line and restart the docker service

`[](#__codelineno-112-1) sudo vi /lib/systemd/system/docker.service [](#__codelineno-112-2) [](#__codelineno-112-3) From: [](#__codelineno-112-4) ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock [](#__codelineno-112-5) [](#__codelineno-112-6) To: [](#__codelineno-112-7) ExecStart=/usr/bin/dockerd`

*   Configure docker service configuration updating **/etc/docker/daemon.json** as shown below.

`[](#__codelineno-113-1) sudo vi /etc/docker/daemon.json`

|     |     |
| --- | --- |
| [1](#__codelineno-114-1)<br> [2](#__codelineno-114-2)<br> [3](#__codelineno-114-3)<br> [4](#__codelineno-114-4)<br> [5](#__codelineno-114-5)<br> [6](#__codelineno-114-6)<br> [7](#__codelineno-114-7)<br> [8](#__codelineno-114-8)<br> [9](#__codelineno-114-9)<br>[10](#__codelineno-114-10)<br>[11](#__codelineno-114-11)<br>[12](#__codelineno-114-12)<br>[13](#__codelineno-114-13)<br>[14](#__codelineno-114-14)<br>[15](#__codelineno-114-15) | `{ "tls": true,  "tlscacert": "/etc/tlscerts/ca/ca.pem",  "tlsverify": true,  "storage-driver": "overlay2",  "hosts": [ "unix:///var/run/docker.sock",  "tcp://0.0.0.0:2376" ],  "tlskey": "/etc/tlscerts/server/server.key",  "debug": false,  "tlscert": "/etc/tlscerts/server/server.pem",  "experimental": false,  "live-restore": true }` |

*   Start and verify the docker service

|     |     |
| --- | --- |
| [1](#__codelineno-115-1)<br>[2](#__codelineno-115-2)<br>[3](#__codelineno-115-3) | `sudo systemctl daemon-reload sudo systemctl start docker sudo systemctl status docker` |

*   Update `/etc/sysctl.conf` file with below performance tuning settings.

`[](#__codelineno-116-1) #Performance Tuning. [](#__codelineno-116-2) net.ipv4.tcp_rmem = 4096 87380 16777216 [](#__codelineno-116-3) net.ipv4.tcp_wmem = 4096 65536 16777216 [](#__codelineno-116-4) net.core.rmem_max = 16777216 [](#__codelineno-116-5) net.core.wmem_max = 16777216 [](#__codelineno-116-6) net.core.netdev_max_backlog = 2500 [](#__codelineno-116-7) net.core.somaxconn = 65000 [](#__codelineno-116-8) net.ipv4.tcp_ecn = 0 [](#__codelineno-116-9) net.ipv4.tcp_window_scaling = 1 [](#__codelineno-116-10) net.ipv4.ip_local_port_range = 10000 65535 [](#__codelineno-116-11) vm.max_map_count = 1048575 [](#__codelineno-116-12) net.core.wmem_default=262144 [](#__codelineno-116-13) net.core.wmem_max=4194304 [](#__codelineno-116-14) net.core.rmem_default=262144 [](#__codelineno-116-15) net.core.rmem_max=4194304 [](#__codelineno-116-16) [](#__codelineno-116-17) #file max [](#__codelineno-116-18) fs.file-max=518144 [](#__codelineno-116-19) [](#__codelineno-116-20) #swapiness [](#__codelineno-116-21) vm.swappiness = 1 [](#__codelineno-116-22) #Set runtime for kernel.randomize_va_space [](#__codelineno-116-23) kernel.randomize_va_space = 2 [](#__codelineno-116-24) [](#__codelineno-116-25) net.ipv4.ip_forward = 1 [](#__codelineno-116-26) net.ipv4.ip_nonlocal_bind=1`

*   Download and execute macaw-docker.py script to configure TLS for docker service.

|     |     |
| --- | --- |
| [1](#__codelineno-117-1)<br>[2](#__codelineno-117-2)<br>[3](#__codelineno-117-3)<br>[4](#__codelineno-117-4)<br>[5](#__codelineno-117-5)<br>[6](#__codelineno-117-6)<br>[7](#__codelineno-117-7) | `mkdir ~/cfx-config-files cd ~/cfx-config-files wget https://macaw-amer.s3.amazonaws.com/images/misc/RHEL-bin-files.tar.gz tar -xzvf RHEL-bin-files.tar.gz` |

*   Install **JAVA** software package

|     |     |
| --- | --- |
| [1](#__codelineno-118-1)<br>[2](#__codelineno-118-2) | `sudo mkdir -p /opt/java sudo tar xf ~/cfx-config-files/jdk-8u281-linux-x64.tar.gz -C /opt/java --strip-components 1` |

*   Add the **JAVA** software binary to **PATH** variable

`[](#__codelineno-119-1) vi ~/.bashrc [](#__codelineno-119-2) PATH=/opt/java/bin:$PATH`

`[](#__codelineno-120-1) source ~/.bashrc`

*   Reboot the host

`[](#__codelineno-121-1) sudo reboot`

**7\. RDAF Platform Installation**
----------------------------------

This section provides information about end to end deployment steps for RDA Fabric Platform on both **Kubernetes** and **Non-Kubernetes** environments.

Note

Please make sure to **complete** the below **pre-requisites** before proceeding to next steps to deploy RDAF Platform.

*   [**RDAF Platform Resource Requirements**](https://bot-docs.cloudfabrix.io/installation_guides/deployment/#4-rdaf-platform-resource-requirements)
    
*   [**Deploy VMs for RDAF Platform using CloudFabric provided OVFs**](https://bot-docs.cloudfabrix.io/installation_guides/deployment/#5-rdaf-platform-vms-deployment-using-ovf)
    
*   [**Deploy VMs for RDAF Platform using Custom RHEL or Ubunut OS Images**](https://bot-docs.cloudfabrix.io/installation_guides/deployment/#6-rdaf-platform-vms-deployment-on-rhelubuntu-os)
    
*   [**Network layout and Port requirements**](https://bot-docs.cloudfabrix.io/installation_guides/deployment/#44-network-layout-and-ports)
    
*   [**Configure HTTP Proxy** (if applicable)](https://bot-docs.cloudfabrix.io/installation_guides/deployment/#__tabbed_1_1)
    

### ****7.1 Install RDAF deployment CLI for K8s & Non-K8s Environments****

**Software Versions**:

KubernetesNon-Kubernetes

Below are the required container image tags for RDAF platform deployment

*   **RDAF Deployment CLI**: 1.2.2
    
*   **RDAF Registry service**: 1.0.3
    
*   **RDAF Infra services**: 1.0.3.2
    
*   **RDAF Platform**: 3.4.2
    
*   **RDAF Worker**: 3.4.2
    
*   **RDAF Client (rdac) CLI**: 3.4.2
    
*   **RDAF OIA (AIOps) Application**: 7.4.2
    
*   **RDAF Studio**: 3.4.2
    

Below are the required container image tags for RDAF platform deployment

*   **RDAF Deployment CLI**: 1.2.2
    
*   **RDAF Registry service**: 1.0.3
    
*   **RDAF Infra services**: 1.0.3.2
    
*   **RDAF Platform**: 3.4.2
    
*   **RDAF Worker**: 3.4.2
    
*   **RDAF Client (rdac) CLI**: 3.4.2
    
*   **RDAF OIA (AIOps) Application**: 7.4.2
    
*   **RDAF Studio**: 3.4.2
    

### ****7.2 RDAF Deployment CLI Installation****

Please follow the below given steps to install RDAF deployment CLI.

Note

Please install RDAF Deployment CLI on both the **on-premise docker registry** VM and the **RDAF Platform's management VM** if provisioned separately. In most cases, **on-premise docker registry** service and **RDAF platform's setup and configuration** are maintained on the same VM.

Login into the VM as **rdauser** where **RDAF deployment CLI** to be installed for docker on-premise registry service and managing Kubernetes or Non-kubernetes deployments.

KubernetesNon-Kubernetes

With Internet AccessWithout Internet Access

*   Download the RDAF Deployment CLI's newer version 1.2.2 bundle.

`[](#__codelineno-122-1) wget https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/rdafcli-1.2.2.tar.gz`

*   Install the `rdaf & rdafk8s` CLI to version 1.2.2

`[](#__codelineno-123-1) pip install --user --upgrade pip [](#__codelineno-123-2) pip install --user rdafcli-1.2.2.tar.gz`

*   Verify the installed `rdaf & rdafk8s` CLI version is upgraded to 1.2.2

`[](#__codelineno-124-1) rdaf --version [](#__codelineno-124-2) rdafk8s --version`

*   Download the RDAF Deployment CLI's newer version 1.2.2 bundle and copy it to RDAF management VM on which `rdaf & rdafk8s` deployment CLI was installed.

For RHEL OS EnvironmentFor Ubuntu OS Environment

`[](#__codelineno-125-1) wget  https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/offline-rhel-1.2.2.tar.gz`

*   Extract the `rdaf` CLI software bundle contents

`[](#__codelineno-126-1) tar -xvzf offline-rhel-1.2.2.tar.gz`

*   Change the directory to the extracted directory

`[](#__codelineno-127-1) cd offline-rhel-1.2.2`

*   Install the `rdaf`CLI to version 1.2.2

`[](#__codelineno-128-1) pip install --user rdafcli-1.2.2.tar.gz  -f ./ --no-index`

*   Verify the installed `rdaf` CLI version

`[](#__codelineno-129-1) rdaf --version [](#__codelineno-129-2) rdafk8s --version`

`[](#__codelineno-130-1) wget  https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/offline-ubuntu-1.2.2.tar.gz`

*   Extract the `rdaf` CLI software bundle contents

`[](#__codelineno-131-1) tar -xvzf offline-ubuntu-1.2.2.tar.gz`

*   Change the directory to the extracted directory

`[](#__codelineno-132-1) cd offline-ubuntu-1.2.2`

*   Upgrade the `rdaf`CLI to version 1.2.2

`[](#__codelineno-133-1) pip install --user rdafcli-1.2.2.tar.gz  -f ./ --no-index`

*   Verify the installed `rdaf` CLI version

`[](#__codelineno-134-1) rdaf --version [](#__codelineno-134-2) rdafk8s --version`

With Internet AccessWithout Internet Access

*   Download the RDAF Deployment CLI's newer version 1.2.2 bundle

`[](#__codelineno-135-1) wget https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/rdafcli-1.2.2.tar.gz`

*   Install the `rdaf` CLI to version 1.2.2

`[](#__codelineno-136-1) pip install --user --upgrade pip [](#__codelineno-136-2) pip install --user rdafcli-1.2.2.tar.gz`

*   Verify the installed `rdaf` CLI version is upgraded to 1.2.2

`[](#__codelineno-137-1) rdaf --version`

*   Download the RDAF Deployment CLI's newer version 1.2.2 bundle and copy it to RDAF management VM on which `rdaf & rdafk8s` deployment CLI was installed.

For RHEL OS EnvironmentFor Ubuntu OS Environment

`[](#__codelineno-138-1) wget  https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/offline-rhel-1.2.2.tar.gz`

*   Extract the `rdaf` CLI software bundle contents

`[](#__codelineno-139-1) tar -xvzf offline-rhel-1.2.2.tar.gz`

*   Change the directory to the extracted directory

`[](#__codelineno-140-1) cd offline-rhel-1.2.2`

*   Install the `rdaf`CLI to version 1.2.2

`[](#__codelineno-141-1) pip install --user rdafcli-1.2.2.tar.gz -f ./ --no-index`

*   Verify the installed `rdaf` CLI version

`[](#__codelineno-142-1) rdaf --version [](#__codelineno-142-2) rdafk8s --version`

`[](#__codelineno-143-1) wget  https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/offline-ubuntu-1.2.2.tar.gz`

*   Extract the `rdaf` CLI software bundle contents

`[](#__codelineno-144-1) tar -xvzf offline-ubuntu-1.2.2.tar.gz`

*   Change the directory to the extracted directory

`[](#__codelineno-145-1) cd offline-ubuntu-1.2.2`

*   Install the `rdaf`CLI to version 1.2.2

`[](#__codelineno-146-1) pip install --user rdafcli-1.2.2.tar.gz -f ./ --no-index`

*   Verify the installed `rdaf` CLI version

`[](#__codelineno-147-1) rdaf --version [](#__codelineno-147-2) rdafk8s --version`

### ****7.3 RDAF On-Premise Docker Registry Setup****

CloudFabrix support hosting an on-premise docker registry which will download and synchronize RDA Fabric's platform, infrastructure and application services from CloudFabrix's public docker registry that is securely hosted on AWS and from other public docker registries as well. For more information on on-premise docker registry, please refer **[Docker registry access for RDAF platform services](https://bot-docs.cloudfabrix.io/installation_guides/deployment/#2-docker-registry-access-for-rdaf-platform-services-deployment)
**.

**rdaf registry setup**

Run the below command to setup and configure on-premise docker registry service. In the below command example, 10.99.120.140 is the machine on which on-premise registry service is going to installed.

cfxregistry.cloudfabrix.io is the CloudFabrix's public docker registry hosted on AWS from which RDA Fabric docker images are going to be downloaded.

|     |     |
| --- | --- |
| [1](#__codelineno-148-1)<br>[2](#__codelineno-148-2)<br>[3](#__codelineno-148-3)<br>[4](#__codelineno-148-4)<br>[5](#__codelineno-148-5) | `rdaf registry setup --docker-server-host 10.99.120.140 \     --docker-registry-source-host cfxregistry.cloudfabrix.io \     --docker-registry-source-port 443 \     --docker-registry-source-user readonly \     --docker-registry-source-password readonly` |

**rdaf registry install**

Run the below command to install the on-premise docker registry service.

|     |     |
| --- | --- |
| [1](#__codelineno-149-1) | `rdaf registry install --tag 1.0.3` |

Info

*   For latest tag version, please contact support@cloudfabrix.com
*   On-premise docker registry service runs on port **TCP/5000**. This port may need to be enabled on firewall device if on-premise docker registry service and RDA Fabric service VMs are deployed in different network environments.

To check the status of the on-premise docker registry service, run the below command.

|     |     |
| --- | --- |
| [1](#__codelineno-150-1) | `docker ps -a \| grep docker-registry` |

**rdaf registry fetch**

Once on-premise docker registry service is installed, run the below command to download one or more tags to pre-stage the docker images for RDA Fabric services deployment for fresh install.

`[](#__codelineno-151-1) rdaf registry fetch --tag 1.0.3.2,3.4.2,7.4.2,1.0.3`

**Minio** object storage service image need to be downloaded explicitly using the below command.

`[](#__codelineno-152-1) rdaf registry fetch --minio-tag RELEASE.2023-09-30T07-02-29Z`

Info

**Note:** It may take few minutes to few hours depends on the outbound internet access bandwidth and the number of docker images to be downloaded. The default location path for the downloaded docker images is **/opt/rdaf-registry/data/docker/registry**. This path can be overridden/changed during **rdaf registry setup** command using **\--install-root** option if needed.

**rdaf registry list-tags**

Run the below command to list the downloaded images and their corresponding tags / versions.

|     |     |
| --- | --- |
| [1](#__codelineno-153-1) | `rdaf registry list-tags` |

Please make sure **1.0.3.2** image tag is downloaded for the below RDAF Infra service.

*   rda-platform-haproxy

Please make sure **1.0.3** image tag is downloaded for the below RDAF Infra service.

*   rda-platform-kafka
*   rda-platform-zookeeper
*   rda-platform-mariadb
*   rda-platform-opensearch
*   rda-platform-nats
*   rda-platform-busybox
*   rda-platform-nats-box
*   rda-platform-nats-boot-config
*   rda-platform-nats-server-config-reloader
*   rda-platform-prometheus-nats-exporter
*   rda-platform-redis
*   rda-platform-redis-sentinel
*   rda-platform-arangodb-starter
*   rda-platform-kube-arangodb
*   rda-platform-arangodb
*   rda-platform-kubectl
*   rda-platform-logstash
*   rda-platform-fluent-bit

Please make sure **RELEASE.2023-09-30T07-02-29Z** image tag is downloaded for the below RDAF Infra service.

*   minio

Please make sure **3.4.2** image tag is downloaded for the below RDAF Platform services.

*   rda-client-api-server
*   rda-registry
*   rda-rda-scheduler
*   rda-collector
*   rda-identity
*   rda-fsm
*   rda-asm
*   rda-stack-mgr
*   rda-access-manager
*   rda-resource-manager
*   rda-user-preferences
*   onprem-portal
*   onprem-portal-nginx
*   rda-worker-all
*   onprem-portal-dbinit
*   cfxdx-nb-nginx-all
*   rda-event-gateway
*   rda-chat-helper
*   rdac
*   rdac-full
*   cfxcollector

Please make sure **7.4.2** image tag is downloaded for the below RDAF OIA Application services.

*   rda-app-controller
*   rda-alert-processor
*   rda-file-browser
*   rda-smtp-server
*   rda-ingestion-tracker
*   rda-reports-registry
*   rda-ml-config
*   rda-event-consumer
*   rda-webhook-server
*   rda-irm-service
*   rda-alert-ingester
*   rda-collaboration
*   rda-notification-service
*   rda-configuration-service
*   rda-irm-service
*   rda-alert-processor-companion

### ****7.4 RDAF Platform Setup****

KubernetesNon-Kubernetes

Important

When **on-premise docker repository** service is used, please make sure to add the **insecure-registries** parameter to **/etc/docker/daemon.json** file and restart the **docker daemon** as shown below on **all of RDA Fabric VMs** before the deployment. This is to bypass SSL certificate validation as **on-premise docker repository** will be installed with **self-signed certificates.**

Edit **/etc/docker/daemon.json** to configure the on-premise docker repository as shown below.

|     |     |
| --- | --- |
| [1](#__codelineno-154-1)<br> [2](#__codelineno-154-2)<br> [3](#__codelineno-154-3)<br> [4](#__codelineno-154-4)<br> [5](#__codelineno-154-5)<br> [6](#__codelineno-154-6)<br> [7](#__codelineno-154-7)<br> [8](#__codelineno-154-8)<br> [9](#__codelineno-154-9)<br>[10](#__codelineno-154-10)<br>[11](#__codelineno-154-11)<br>[12](#__codelineno-154-12)<br>[13](#__codelineno-154-13)<br>[14](#__codelineno-154-14)<br>[15](#__codelineno-154-15)<br>[16](#__codelineno-154-16) | `{ "tls": true,  "tlscacert": "/etc/tlscerts/ca/ca.pem",  "tlsverify": true,  "storage-driver": "overlay2",  "hosts": [   "unix:///var/run/docker.sock",    "tcp://0.0.0.0:2376" ],  "tlskey": "/etc/tlscerts/server/server.key",  "debug": false,  "tlscert": "/etc/tlscerts/server/server.pem",  "experimental": false,  "insecure-registries" : ["<on-premise-docker-registry-ip-or-dns>:5000"], "live-restore": true }` |

|     |     |
| --- | --- |
| [1](#__codelineno-155-1) | `sudo systemctl daemon-reload` |

|     |     |
| --- | --- |
| [1](#__codelineno-156-1) | `sudo systemctl restart docker` |

|     |     |
| --- | --- |
| [1](#__codelineno-157-1) | `docker info` |

Example Output

`[](#__codelineno-158-1) ... [](#__codelineno-158-2) ... [](#__codelineno-158-3) Kernel Version: 5.4.0-110-generic [](#__codelineno-158-4) Operating System: Ubuntu 20.04.4 LTS [](#__codelineno-158-5) OSType: linux [](#__codelineno-158-6) Architecture: x86_64 [](#__codelineno-158-7) CPUs: 2 [](#__codelineno-158-8) Total Memory: 7.741GiB [](#__codelineno-158-9) Name: rdaf-onprem-docker-repo [](#__codelineno-158-10) ID: OLZF:ZKWN:TIQJ:ZMNV:2STT:JHR3:3RAT:TAL5:TF47:OGVQ:LHY7:RMHH [](#__codelineno-158-11) Docker Root Dir: /var/lib/docker [](#__codelineno-158-12) Debug Mode: false [](#__codelineno-158-13) Registry: https://index.docker.io/v1/ [](#__codelineno-158-14) Labels: [](#__codelineno-158-15) Experimental: false [](#__codelineno-158-16) Insecure Registries: [](#__codelineno-158-17)   10.99.120.140:5000 [](#__codelineno-158-18)   127.0.0.0/8 [](#__codelineno-158-19) Live Restore Enabled: true`

**rdafk8s setregistry**

When on-premise docker registry is deployed, set the default docker registry configuration to on-premise docker registry host to pull and install the RDA Fabric platform services.

*   Before proceeding, please copy the `/opt/rdaf-registry/cert/ca/ca.crt` file from on-premise registry VM.

``[](#__codelineno-159-1) sudo mkdir -p /opt/rdaf-registry [](#__codelineno-159-2) sudo chown -R `id -u`:`id -g` /opt/rdaf-registry``

`[](#__codelineno-160-1) scp rdauser@<on-premise-registry-ip>:/opt/rdaf-registry/cert/ca/ca.crt /opt/rdaf-registry/registry-ca-cert.crt`

Tip

The location of the on-premise docker registry's CA certificate file `ca.crt` is located under **/opt/rdaf-registry/cert/ca**. This file `ca.crt` need to be copied to the machine on which **RDAF CLI** is used to **setup, configure and install RDA Fabric platform** and all of the required services using on-premise docker registry. This step is not applicable when cloud hosted docker registry **cfxregistry.cloudfabrix.io** is used. Also, this step is not needed, when on-premise docker registry service VM is used to setup, configure and deploy RDAF platform as well.

*   Run the below command to set the docker-registry to on-premise one.

`[](#__codelineno-161-1) rdafk8s setregistry --host <on-premise-docker-registry-ip-or-dns> --port 5000 --cert-path /opt/rdaf-registry/registry-ca-cert.crt`

Tip

Please verify if on-premise registry is accessible on port 5000 using either of the below commands.

*   **telnet `<on-premise-docker-registry-ip-or-dns>` 5000**
*   **curl -vv telnet://`<on-premise-docker-registry-ip-or-dns>`:5000**

**rdafk8s setup**

Run the below `rdafk8s setup` command to create the RDAF platform's deployment configuration. It is a pre-requisite before RDAF infrastructure, platform and application services can be installed on Kubernetes Cluser.

It will prompt for all the necessary configuration details.

`[](#__codelineno-162-1) rdafk8s setup`

*   Accept the EULA

`[](#__codelineno-163-1) Do you accept the EULA? [yes/no]: yes`

*   Enter the **rdauser** SSH password for all of the Kubernetes worker nodes on which RDAF services are going to be installed.

`[](#__codelineno-164-1) What is the SSH password for the SSH user used to communicate between hosts [](#__codelineno-164-2) SSH password: [](#__codelineno-164-3) Re-enter SSH password:`

Tip

Please make sure **rdauser's** SSH password on all of the Kubernetes cluster worker nodes is same during the `rdafk8s setup` command.

*   Enter additional IP address(es) or DNS names that can be as SANs (Subject alt names) while generating self-signed certificates. This is an optional configuration, but it is important to include any public facing IP addresse(s) that is/are different from worker node's ip addresses which are specified as part of the `rdafk8s setup` command.

Tip

SANs (Subject alt names) also known as **multi-domain certificates** which allows to create a single unified SSL certificate which includes more than one Common Name (CN). Common Name can be an IP Address or DNS Name or a wildcard DNS Name (ex: \*.acme.com)

`[](#__codelineno-165-1) Provide any Subject alt name(s) to be used while generating SAN certs [](#__codelineno-165-2) Subject alt name(s) for certs[]: 100.30.10.10`

*   Enter Kubernetes worker node IPs on which **RDAF Platform services** need to be installed. For HA configuration, please enter comma separated values. Minimum of 2 worker nodes are required for the HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's ip address or DNS name is required.

`[](#__codelineno-166-1) What are the host(s) on which you want the RDAF platform services to be installed? [](#__codelineno-166-2) Platform service host(s)[rda-platform-vm01]: 192.168.125.141,192.168.125.142`

*   Answer if the RDAF application services are going to be deployed in HA mode or standalone.

`[](#__codelineno-167-1) Will application services be installed in HA mode? [yes/No]: yes`

*   Enter Kubernetes worker node IPs on which **RDAF Application services (OIA/AIA)** need to be installed. For HA configuration, please enter comma separated values. Minimum of 2 hosts or more are required for the HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's ip address or DNS name is required.

`[](#__codelineno-168-1) What are the host(s) on which you want the application services to be installed? [](#__codelineno-168-2) Application service host(s)[rda-platform-vm01]: 192.168.125.143,192.168.125.144`

*   Enter the name of the Organization. In the below example, `ACME_IT_Services` is used as the Organization name. It is for a reference only.

`[](#__codelineno-169-1) What is the organization you want to use for the admin user created? [](#__codelineno-169-2) Admin organization[CloudFabrix]: ACME_IT_Services`

Press **Enter** to accept the defaults.

`[](#__codelineno-170-1) What is the ca cert to use to communicate to on-prem docker registry [](#__codelineno-170-2) Docker Registry CA cert path[]:`

*   Enter Kubernetes worker node IPs on which **RDAF Worker services** need to be installed. For HA configuration, please enter comma separated values. Minimum of 2 hosts or more are required for the HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's ip address or DNS name is required.

`[](#__codelineno-171-1) What are the host(s) on which you want the Worker to be installed? [](#__codelineno-171-2) Worker host(s)[rda-platform-vm01]: 192.168.125.145`

*   Enter Kubernetes worker node IPs on which **RDAF NATs** infrastructure service need to be installed. For HA configuration, please enter comma separated values. Minimum of 2 Kubernetes worker nodes are required for the `NATs` HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's IP or DNS Name is required.

`[](#__codelineno-172-1) What is the "host/path-on-host" on which you want the Nats to be deployed? [](#__codelineno-172-2) Nats host/path[192.168.125.141]: 192.168.125.145,192.168.125.146`

*   Enter Kubernetes worker node IPs on which **RDAF Minio** infrastructure service need to be installed. For HA configuration, please enter comma separated values. Minimum of 4 Kubernetes worker nodes are required for the `Minio` HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's IP or DNS Name is required.

`[](#__codelineno-173-1) What is the "host/path-on-host" where you want Minio to be provisioned? [](#__codelineno-173-2) Minio server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147,192.168.125.148`

*   Change the default `Minio` user credentials if needed or press **Enter** to accept the defaults.

`[](#__codelineno-174-1) What is the user name you want to give for Minio root user that will be created and used by the RDAF platform? [](#__codelineno-174-2) Minio user[rdafadmin]:  [](#__codelineno-174-3) What is the password you want to use for the newly created Minio root user? [](#__codelineno-174-4) Minio password[Q8aJ63PT]:` 

*   Enter Kubernetes worker node IPs on which **RDAF MariaDB** infrastructure service need to be installed. For HA configuration, please enter comma separated values. Minimum of 3 Kubernetes worker nodes are required for the `MariDB` database HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's IP or DNS Name is required.

`[](#__codelineno-175-1) What is the "host/path-on-host" on which you want the MariaDB server to be provisioned? [](#__codelineno-175-2) MariaDB server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Change the default `MariaDB` user credentials if needed or press **Enter** to accept the defaults.

`[](#__codelineno-176-1) What is the user name you want to give for MariaDB admin user that will be created and used by the RDAF platform? [](#__codelineno-176-2) MariaDB user[rdafadmin]:  [](#__codelineno-176-3) What is the password you want to use for the newly created MariaDB root user? [](#__codelineno-176-4) MariaDB password[jffqjAaZ]:` 

*   Enter Kubernetes worker node IPs on which **RDAF Opensearch** infrastructure service need to be installed. For HA configuration, please enter comma separated values. Minimum of 3 Kubernetes worker nodes are required for the `Opensearch` HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's IP or DNS Name is required.

`[](#__codelineno-177-1) What is the "host/path-on-host" on which you want the opensearch server to be provisioned? [](#__codelineno-177-2) opensearch server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Change the default `Opensearch` user credentials if needed or press **Enter** to accept the defaults.

`[](#__codelineno-178-1) What is the user name you want to give for Opensearch admin user that will be created and used by the RDAF platform? [](#__codelineno-178-2) Opensearch user[rdafadmin]:  [](#__codelineno-178-3) What is the password you want to use for the newly created Opensearch admin user? [](#__codelineno-178-4) Opensearch password[sLmr4ICX]:` 

*   Enter Kubernetes worker node IPs on which **RDAF Zookeeper** infrastructure service need to be installed. For HA configuration, please enter comma separated values. Minimum of 3 Kubernetes worker nodes are required for the `Zookeeper` HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's IP or DNS Name is required.

`[](#__codelineno-179-1) What is the "host/path-on-host" on which you want the Zookeeper server to be provisioned? [](#__codelineno-179-2) Zookeeper server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Enter Kubernetes worker node IPs on which **RDAF Kafka** infrastructure service need to be installed. For HA configuration, please enter comma separated values. Minimum of 3 Kubernetes worker nodes are required for the `Kafka` HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's IP or DNS Name is required.

`[](#__codelineno-180-1) What is the "host/path-on-host" on which you want the Kafka server to be provisioned? [](#__codelineno-180-2) Kafka server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Enter Kubernetes worker node IPs on which **RDAF Redis** infrastructure service need to be installed. For HA configuration, please enter comma separated values. Minimum of 3 Kubernetes worker nodes are required for the `Redis` HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's IP or DNS Name is required.

`[](#__codelineno-181-1) What is the "host/path-on-host" on which you want the Redis server to be provisioned? [](#__codelineno-181-2) Redis server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Enter RDAF infrastructure service `HAProxy` (load-balancer) host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts are required for the `HAProxy` HA configuration. If it is a non-HA deployment, only one RDAF `HAProxy` service host's ip address or DNS name is required.

`[](#__codelineno-182-1) What is the host on which you want HAProxy to be provisioned? [](#__codelineno-182-2) HAProxy host[192.168.125.141]: 192.168.125.145,192.168.125.146`

*   Select the network interface name which is used for UI portal access. Ex: `eth0` or `ens160` etc.

`[](#__codelineno-183-1) What is the network interface on which you want the rdaf to be accessible externally? [](#__codelineno-183-2) Advertised external interface[eth0]: ens160`

*   Enter the `HAProxy` service's virtual IP address when it is configured in HA configuration. Virtual IP address should be an unused IP address. This step is not applicable when `HAProxy` service is deployed in non-HA configuration.

`[](#__codelineno-184-1) What is the host on which you want the platform to be externally accessible? [](#__codelineno-184-2) Advertised external host[192.168.125.143]: 192.168.125.149`

After entering the required inputs as above, `rdaf setup` generates self-signed SSL certificates, creates the required directory structure, configures SSH key based authentication on all of the RDAF hosts and generates `rdaf.cfg` configuration file under `/opt/rdaf` directory.

It creates the below director structure on all of the RDAF hosts.

*   **/opt/rdaf/cert:** It contains the generated self-signed SSL certificates for all of the RDAF hosts.
*   **/opt/rdaf/config:** It contains the required configuration file for each deployed RDAF service where applicable.
*   **/opt/rdaf/data:** It contains the persistent data for some of the RDAF services.
*   **/opt/rdaf/deployment-scripts:** It contains the docker-compose `.yml` file of the services that are configured to be provisioned on RDAF host.
*   **/opt/rdaf/logs:** It contains the RDAF services log files.

Important

When **on-premise docker repository** service is used, please make sure to add the **insecure-registries** parameter to **/etc/docker/daemon.json** file and restart the **docker daemon** as shown below on **all of RDA Fabric VMs** before the deployment. This is to bypass SSL certificate validation as **on-premise docker repository** will be installed with **self-signed certificates.**

Edit **/etc/docker/daemon.json** to configure the on-premise docker repository as shown below.

|     |     |
| --- | --- |
| [1](#__codelineno-185-1)<br> [2](#__codelineno-185-2)<br> [3](#__codelineno-185-3)<br> [4](#__codelineno-185-4)<br> [5](#__codelineno-185-5)<br> [6](#__codelineno-185-6)<br> [7](#__codelineno-185-7)<br> [8](#__codelineno-185-8)<br> [9](#__codelineno-185-9)<br>[10](#__codelineno-185-10)<br>[11](#__codelineno-185-11)<br>[12](#__codelineno-185-12)<br>[13](#__codelineno-185-13)<br>[14](#__codelineno-185-14)<br>[15](#__codelineno-185-15)<br>[16](#__codelineno-185-16) | `{ "tls": true,  "tlscacert": "/etc/tlscerts/ca/ca.pem",  "tlsverify": true,  "storage-driver": "overlay2",  "hosts": [   "unix:///var/run/docker.sock",    "tcp://0.0.0.0:2376" ],  "tlskey": "/etc/tlscerts/server/server.key",  "debug": false,  "tlscert": "/etc/tlscerts/server/server.pem",  "experimental": false,  "insecure-registries" : ["<on-premise-docker-registry-ip-or-dns>:5000"], "live-restore": true }` |

|     |     |
| --- | --- |
| [1](#__codelineno-186-1) | `sudo systemctl daemon-reload` |

|     |     |
| --- | --- |
| [1](#__codelineno-187-1) | `sudo systemctl restart docker` |

|     |     |
| --- | --- |
| [1](#__codelineno-188-1) | `docker info` |

Example Output

`[](#__codelineno-189-1) ... [](#__codelineno-189-2) ... [](#__codelineno-189-3) Kernel Version: 5.4.0-110-generic [](#__codelineno-189-4) Operating System: Ubuntu 20.04.4 LTS [](#__codelineno-189-5) OSType: linux [](#__codelineno-189-6) Architecture: x86_64 [](#__codelineno-189-7) CPUs: 2 [](#__codelineno-189-8) Total Memory: 7.741GiB [](#__codelineno-189-9) Name: rdaf-onprem-docker-repo [](#__codelineno-189-10) ID: OLZF:ZKWN:TIQJ:ZMNV:2STT:JHR3:3RAT:TAL5:TF47:OGVQ:LHY7:RMHH [](#__codelineno-189-11) Docker Root Dir: /var/lib/docker [](#__codelineno-189-12) Debug Mode: false [](#__codelineno-189-13) Registry: https://index.docker.io/v1/ [](#__codelineno-189-14) Labels: [](#__codelineno-189-15) Experimental: false [](#__codelineno-189-16) Insecure Registries: [](#__codelineno-189-17)   10.99.120.140:5000 [](#__codelineno-189-18)   127.0.0.0/8 [](#__codelineno-189-19) Live Restore Enabled: true`

**rdaf setregistry**

When on-premise docker registry is deployed, set the default docker registry configuration to on-premise docker registry host to pull and install the RDA Fabric platform services.

*   Before proceeding, please copy the `/opt/rdaf-registry/cert/ca/ca.crt` file from on-premise registry VM.

``[](#__codelineno-190-1) sudo mkdir -p /opt/rdaf-registry [](#__codelineno-190-2) sudo chown -R `id -u`:`id -g` /opt/rdaf-registry``

`[](#__codelineno-191-1) scp rdauser@<on-premise-registry-ip>:/opt/rdaf-registry/cert/ca/ca.crt /opt/rdaf-registry/registry-ca-cert.crt`

Tip

The location of the on-premise docker registry's CA certificate file `ca.crt` is located under **/opt/rdaf-registry/cert/ca**. This file `ca.crt` need to be copied to the machine on which **RDAF CLI** is used to **setup, configure and install RDA Fabric platform** and all of the required services using on-premise docker registry. This step is not applicable when cloud hosted docker registry **cfxregistry.cloudfabrix.io** is used. Also, this step is not needed, when on-premise docker registry service VM is used to setup, configure and deploy RDAF platform as well.

*   Run the below command to set the docker-registry to on-premise one.

`[](#__codelineno-192-1) rdaf setregistry --host <on-premise-docker-registry-ip-or-dns> --port 5000 --cert-path /opt/rdaf-registry/registry-ca-cert.crt`

Tip

Please verify if on-premise registry is accessible on port 5000 using either of the below commands.

*   **telnet `<on-premise-docker-registry-ip-or-dns>` 5000**
*   **curl -vv telnet://`<on-premise-docker-registry-ip-or-dns>`:5000**

**rdaf setup**

Run the below `rdaf setup` command to create the RDAF platform's deployment configuration. It is a pre-requisite before RDAF infrastructure, platform and application services can be installed.

It will prompt for all the necessary configuration details.

`[](#__codelineno-193-1) rdaf setup`

*   Accept the EULA

`[](#__codelineno-194-1) Do you accept the EULA? [yes/no]: yes`

*   Enter the **rdauser** SSH password for all of the RDAF hosts.

`[](#__codelineno-195-1) What is the SSH password for the SSH user used to communicate between hosts [](#__codelineno-195-2) SSH password: [](#__codelineno-195-3) Re-enter SSH password:`

Tip

Please make sure **rdauser's** SSH password on all of the RDAF hosts is same during the `rdaf setup` command.

Press **Enter** to accept the defaults.

`[](#__codelineno-196-1) Provide any Subject alt name(s) to be used while generating SAN certs [](#__codelineno-196-2) Subject alt name(s) for certs[]:`

*   Enter RDAF Platform host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts are required for the HA configuration. If it is a non-HA deployment, only one RDAF platform host's ip address or DNS name is required.

`[](#__codelineno-197-1) What are the host(s) on which you want the RDAF platform services to be installed? [](#__codelineno-197-2) Platform service host(s)[rda-platform-vm01]: 192.168.125.141,192.168.125.142`

*   Answer if the RDAF application services are going to be deployed in HA mode or standalone.

`[](#__codelineno-198-1) Will application services be installed in HA mode? [yes/No]: yes`

*   Enter RDAF Application services host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts or more are required for the HA configuration. If it is a non-HA deployment, only one RDAF application service host's ip address or DNS name is required.

`[](#__codelineno-199-1) What are the host(s) on which you want the application services to be installed? [](#__codelineno-199-2) Application service host(s)[rda-platform-vm01]: 192.168.125.143,192.168.125.144`

*   Enter the name of the Organization. In the below example, `ACME_IT_Services` is used as the Organization name. It is for a reference only.

`[](#__codelineno-200-1) What is the organization you want to use for the admin user created? [](#__codelineno-200-2) Admin organization[CloudFabrix]: ACME_IT_Services`

Press **Enter** to accept the defaults.

`[](#__codelineno-201-1) What is the ca cert to use to communicate to on-prem docker registry [](#__codelineno-201-2) Docker Registry CA cert path[]:`

*   Enter RDAF Worker service host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts or more are required for the HA configuration. If it is a non-HA deployment, only one RDAF worker service host's ip address or DNS name is required.

`[](#__codelineno-202-1) What are the host(s) on which you want the Worker to be installed? [](#__codelineno-202-2) Worker host(s)[rda-platform-vm01]: 192.168.125.145`

*   Enter ip address on which RDAF Event Gateway needs to be Installed, For HA configuration please enter comma separated values. Minimum of 2 hosts or more are required for the HA configuration. If it is a non-HA deployment, only one RDAF Event Gateway host's ip address or DNS name is required.

`[](#__codelineno-203-1) What are the host(s) on which you want the Event Gateway to be installed? [](#__codelineno-203-2) Event Gateway host(s)[rda-platform-vm01]: 192.168.125.67`

*   Enter RDAF infrastructure service `NATs` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts are required for the `NATs` HA configuration. If it is a non-HA deployment, only one RDAF `NATs` service host's ip address or DNS name is required.

`[](#__codelineno-204-1) What is the "host/path-on-host" on which you want the Nats to be deployed? [](#__codelineno-204-2) Nats host/path[192.168.125.141]: 192.168.125.145,192.168.125.146`

*   Enter RDAF infrastructure service `Minio` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 4 hosts are required for the `Minio` HA configuration. If it is a non-HA deployment, only one RDAF `Minio` service host's ip address or DNS name is required.

`[](#__codelineno-205-1) What is the "host/path-on-host" where you want Minio to be provisioned? [](#__codelineno-205-2) Minio server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147,192.168.125.148`

*   Change the default `Minio` user credentials if needed or press **Enter** to accept the defaults.

`[](#__codelineno-206-1) What is the user name you want to give for Minio root user that will be created and used by the RDAF platform? [](#__codelineno-206-2) Minio user[rdafadmin]:  [](#__codelineno-206-3) What is the password you want to use for the newly created Minio root user? [](#__codelineno-206-4) Minio password[Q8aJ63PT]:` 

*   Enter RDAF infrastructure service `MariDB` database host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `MariDB` database HA configuration. If it is a non-HA deployment, only one RDAF `MariaDB` service host's ip address or DNS name is required.

`[](#__codelineno-207-1) What is the "host/path-on-host" on which you want the MariaDB server to be provisioned? [](#__codelineno-207-2) MariaDB server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Change the default `MariaDB` user credentials if needed or press **Enter** to accept the defaults.

`[](#__codelineno-208-1) What is the user name you want to give for MariaDB admin user that will be created and used by the RDAF platform? [](#__codelineno-208-2) MariaDB user[rdafadmin]:  [](#__codelineno-208-3) What is the password you want to use for the newly created MariaDB root user? [](#__codelineno-208-4) MariaDB password[jffqjAaZ]:` 

*   Enter RDAF infrastructure service `Opensearch` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `Opensearch` HA configuration. If it is a non-HA deployment, only one RDAF `Opensearch` service host's ip address or DNS name is required.

`[](#__codelineno-209-1) What is the "host/path-on-host" on which you want the opensearch server to be provisioned? [](#__codelineno-209-2) opensearch server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Change the default `Opensearch` user credentials if needed or press **Enter** to accept the defaults.

`[](#__codelineno-210-1) What is the user name you want to give for Opensearch admin user that will be created and used by the RDAF platform? [](#__codelineno-210-2) Opensearch user[rdafadmin]:  [](#__codelineno-210-3) What is the password you want to use for the newly created Opensearch admin user? [](#__codelineno-210-4) Opensearch password[sLmr4ICX]:` 

*   Enter RDAF infrastructure service `Zookeeper` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `Zookeeper` HA configuration. If it is a non-HA deployment, only one RDAF `Zookeeper` service host's ip address or DNS name is required.

`[](#__codelineno-211-1) What is the "host/path-on-host" on which you want the Zookeeper server to be provisioned? [](#__codelineno-211-2) Zookeeper server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Enter RDAF infrastructure service `Kafka` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `Kafka` HA configuration. If it is a non-HA deployment, only one RDAF `Kafka` service host's ip address or DNS name is required.

`[](#__codelineno-212-1) What is the "host/path-on-host" on which you want the Kafka server to be provisioned? [](#__codelineno-212-2) Kafka server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Enter RDAF infrastructure service `Redis` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `Redis` HA configuration. If it is a non-HA deployment, only one RDAF `Redis` service host's ip address or DNS name is required.

`[](#__codelineno-213-1) What is the "host/path-on-host" on which you want the Redis server to be provisioned? [](#__codelineno-213-2) Redis server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Enter RDAF infrastructure service `GraphDB` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `GraphDB` HA configuration. If it is a non-HA deployment, only one RDAF `GraphDB` service host's ip address or DNS name is required.

`[](#__codelineno-214-1) What is the "host/path-on-host" on which you want the GraphDB to be deployed? [](#__codelineno-214-2) GraphDB host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Enter RDAF infrastructure service `HAProxy` (load-balancer) host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts are required for the `HAProxy` HA configuration. If it is a non-HA deployment, only one RDAF `HAProxy` service host's ip address or DNS name is required.

`[](#__codelineno-215-1) What is the host on which you want HAProxy to be provisioned? [](#__codelineno-215-2) HAProxy host[192.168.125.141]: 192.168.125.145,192.168.125.146`

*   Select the network interface name which is used for UI portal access. Ex: `eth0` or `ens160` etc.

`[](#__codelineno-216-1) What is the network interface on which you want the rdaf to be accessible externally? [](#__codelineno-216-2) Advertised external interface[eth0]: ens160`

*   Enter the `HAProxy` service's virtual IP address when it is configured in HA configuration. Virtual IP address should be an unused IP address. This step is not applicable when `HAProxy` service is deployed in non-HA configuration.

`[](#__codelineno-217-1) What is the host on which you want the platform to be externally accessible? [](#__codelineno-217-2) Advertised external host[192.168.125.143]: 192.168.125.149`

*   Enter the ip address of the Internal accessible advertised host

`[](#__codelineno-218-1) Do you want to specify an internal advertised host? [yes/No]: No`

Note

Internal advertized host ip is only needed when RDA Fabric VMs are configured with dual NIC interfaces, one is for management network for UI access, second one is for internal app to app communication using non-routable ip address network scheme which is isolated from management network.

Dual network configuration is primarily used to support DR solution where the RDA Fabric VMs are replicated from one site to another site using VM level replication or underlying storage array replication (volume to volume or LUN to LUN on which RDA Fabric VMs are hosted). When RDA Fabric VMs are recovered on a DR site, management network IPs need be changed as per DR site network's subnet, while secondary NIC's ip address scheme can be maintained with same as primary site to avoid RDA Fabric's application reconfiguration.

After entering the required inputs as above, `rdaf setup` generates self-signed SSL certificates, creates the required directory structure, configures SSH key based authentication on all of the RDAF hosts and generates `rdaf.cfg` configuration file under `/opt/rdaf` directory.

It creates the below director structure on all of the RDAF hosts.

*   **/opt/rdaf/cert:** It contains the generated self-signed SSL certificates for all of the RDAF hosts.
*   **/opt/rdaf/config:** It contains the required configuration file for each deployed RDAF service where applicable.
*   **/opt/rdaf/data:** It contains the persistent data for some of the RDAF services.
*   **/opt/rdaf/deployment-scripts:** It contains the docker-compose `.yml` file of the services that are configured to be provisioned on RDAF host.
*   **/opt/rdaf/logs:** It contains the RDAF services log files.

### ****7.5 RDAF Infra Services Installation****

KubernetesNon-Kubernetes

`rdafk8s infra install` command is used to deploy / install RDAF infrastructure services on Kubernetes Cluster.

Run the below command to deploy all RDAF infrastructure services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com.)

`[](#__codelineno-219-1) rdafk8s infra install --tag 1.0.3`

Run the below command to install a specific RDAF infrastructure service. Below are the supported infrastructure services.

*   haproxy
*   nats
*   mariadb
*   opensearch
*   kafka
*   redis
*   graphdb

Run the below command to upgrade the **haproxy** service.

`[](#__codelineno-220-1) rdafk8s infra upgrade --service haproxy --tag 1.0.3.2`

**1.5.1 Status check**

Run the below command to see the status of all of the deployed RDAF infrastructure services.

`[](#__codelineno-221-1) rdafk8s infra status`

Example Output

`[](#__codelineno-222-1) +-----------------------+----------------+----------------+--------------+------------------------------+ [](#__codelineno-222-2) | Name                  | Host           | Status         | Container Id | Tag                          | [](#__codelineno-222-3) +-----------------------+----------------+----------------+--------------+------------------------------+ [](#__codelineno-222-4) | haproxy               | 192.168.108.31 | Up 3 hours     | 217fe8852f2d | 1.0.3.2                      | [](#__codelineno-222-5) | rda-nats              | 192.168.108.31 | Up 3 Hours ago | 58cf96d50a3c | 1.0.3                        | [](#__codelineno-222-6) | rda-minio             | 192.168.108.31 | Up 3 Hours ago | 6704c211e803 | RELEASE.2023-09-30T07-02-29Z | [](#__codelineno-222-7) | rda-mariadb           | 192.168.108.31 | Up 3 Hours ago | d83f0e0e3c0c | 1.0.3                        | [](#__codelineno-222-8) | rda-opensearch        | 192.168.108.31 | Up 3 Hours ago | f36fd18bc397 | 1.0.3                        | [](#__codelineno-222-9) | rda-kafka-controller  | 192.168.108.31 | Up 3 Hours ago | 0bb0d3e6580a | 1.0.3                        | [](#__codelineno-222-10) | rda-redis-master      | 192.168.108.31 | Up 3 Hours ago | 1afcc9a825d4 | 1.0.3                        | [](#__codelineno-222-11) | rda-redis-replica     | 192.168.108.31 | Up 3 Hours ago | b797195153de | 1.0.3                        | [](#__codelineno-222-12) | rda-graphdb[operator] | 192.168.108.31 | Up 3 Hours ago | 2491c9e12c53 | 1.0.3                        | [](#__codelineno-222-13) | rda-graphdb[server]   | 192.168.108.31 | Up 3 Hours ago | 98a139960fbd | 1.0.3                        | [](#__codelineno-222-14) +-----------------------+----------------+----------------+--------------+------------------------------+`

Below are the Kubernetes Cluster `kubectl get pods` commands to check the status of RDA Fabric infrastructure services.

`[](#__codelineno-223-1) kubectl get pods -n rda-fabric -l app_category=rdaf-infra`

Example Output

`[](#__codelineno-224-1) NAME                            READY   STATUS    RESTARTS        AGE [](#__codelineno-224-2) opensearch-cluster-master-0     1/1     Running   0               7m12s [](#__codelineno-224-3) rda-kafka-0                     1/1     Running   2 (5m26s ago)   7m10s [](#__codelineno-224-4) rda-kafka-zookeeper-0           1/1     Running   0               7m10s [](#__codelineno-224-5) rda-mariadb-mariadb-galera-0    1/1     Running   0               8m8s [](#__codelineno-224-6) rda-minio-65f755bb5f-9tjdm      1/1     Running   0               8m25s [](#__codelineno-224-7) rda-nats-0                      3/3     Running   0               8m57s [](#__codelineno-224-8) rda-nats-box-7b7b46969b-79lnf   1/1     Running   0               8m57s [](#__codelineno-224-9) rda-redis-master-0              1/1     Running   0               7m9s [](#__codelineno-224-10) rda-redis-replicas-0            1/1     Running   0               7m9s`

Below `kubectl get pods` command provides additional details of deployed RDAF Infrastructure services (PODs) along with their worker node(s) on which they were deployed.

`[](#__codelineno-225-1) kubectl get pods -n rda-fabric -o wide -l app_category=rdaf-infra`

In order to get detailed status of the each RDAF Infrastructure service POD, run the below `kubectl describe pod` command.

`[](#__codelineno-226-1) kubectl describe pod rda-nats-0 -n rda-fabric`

Example Output

`[](#__codelineno-227-1) Name:         rda-nats-0 [](#__codelineno-227-2) Namespace:    rda-fabric [](#__codelineno-227-3) Priority:     0 [](#__codelineno-227-4) Node:         k8rdapfm01/192.168.125.45 [](#__codelineno-227-5) Start Time:   Sun, 12 Feb 2023 00:36:39 +0000 [](#__codelineno-227-6) Labels:       app=rda-fabric-services [](#__codelineno-227-7)                 app_category=rdaf-infra [](#__codelineno-227-8)                 app_component=rda-nats [](#__codelineno-227-9)                 controller-revision-hash=rda-nats-64747cd755 [](#__codelineno-227-10) ... [](#__codelineno-227-11) ... [](#__codelineno-227-12) Events: [](#__codelineno-227-13) Type    Reason     Age   From               Message [](#__codelineno-227-14) ----    ------     ----  ----               ------- [](#__codelineno-227-15) Normal  Scheduled  10m   default-scheduler  Successfully assigned rda-fabric/rda-nats-0 to k8rdapfm01 [](#__codelineno-227-16) Normal  Pulling    10m   kubelet            Pulling image "192.168.125.140:5000/rda-platform-nats:1.0.2" [](#__codelineno-227-17) Normal  Pulled     10m   kubelet            Successfully pulled image "192.168.125.140:5000/rda-platform-nats:1.0.2" in 3.102792187s [](#__codelineno-227-18) Normal  Created    10m   kubelet            Created container nats`

Note

Below steps are applicable only if RDAF Application (OIA/AIA) services are going to be installed.

*   Run the below command to update the necessary HAProxy load-balancer configuration for RDAF **OIA** / **AIA** application services.

`[](#__codelineno-228-1) rdafk8s app update-config OIA`

`[](#__codelineno-229-1) rdafk8s app update-config AIA`

After deploying the RDAF OIA application services, it is mandatory to run the `rdaf app update-config` which will apply and restart the HAProxy load-balancer service automatically.

`rdaf infra install` command is used to deploy / install RDAF infrastructure services.

Run the below command to deploy all RDAF infrastructure services.

`[](#__codelineno-230-1) rdaf infra install --tag 1.0.3`

It deploys the below RDAF Infrastructure services.

*   haproxy
*   nats
*   mariadb
*   opensearch
*   kafka
*   redis
*   graphdb

Run the below command to upgrade the **haproxy** service.

`[](#__codelineno-231-1) rdaf infra upgrade --service haproxy --tag 1.0.3.2`

**1.5.1 Status check**

Run the below command to see the status of all of the deployed RDAF infrastructure services.

`[](#__codelineno-232-1) rdaf infra status`

Example Output

`[](#__codelineno-233-1) +-----------------------+--------------+----------------+--------------+------------------------------+ [](#__codelineno-233-2) | Name                  | Host         | Status         | Container Id | Tag                          | [](#__codelineno-233-3) +-----------------------+--------------+----------------+--------------+------------------------------+ [](#__codelineno-233-4) | haproxy               | 192.168.108.31 | Up 3 hours     | 217fe8852f2d | 1.0.3.2                      | [](#__codelineno-233-5) | rda-nats              | 192.168.108.31 | Up 3 Hours ago | 58cf96d50a3c | 1.0.3                        | [](#__codelineno-233-6) | rda-minio             | 192.168.108.31 | Up 3 Hours ago | 6704c211e803 | RELEASE.2023-09-30T07-02-29Z | [](#__codelineno-233-7) | rda-mariadb           | 192.168.108.31 | Up 3 Hours ago | d83f0e0e3c0c | 1.0.3                        | [](#__codelineno-233-8) | rda-opensearch        | 192.168.108.31 | Up 3 Hours ago | f36fd18bc397 | 1.0.3                        | [](#__codelineno-233-9) | rda-kafka-controller  | 192.168.108.31 | Up 3 Hours ago | 0bb0d3e6580a | 1.0.3                        | [](#__codelineno-233-10) | rda-redis-master      | 192.168.108.31 | Up 3 Hours ago | 1afcc9a825d4 | 1.0.3                        | [](#__codelineno-233-11) | rda-redis-replica     | 192.168.108.31 | Up 3 Hours ago | b797195153de | 1.0.3                        | [](#__codelineno-233-12) | rda-graphdb[operator] | 192.168.108.31 | Up 3 Hours ago | 2491c9e12c53 | 1.0.3                        | [](#__codelineno-233-13) | rda-graphdb[server]   | 192.168.108.31 | Up 3 Hours ago | 98a139960fbd | 1.0.3                        | [](#__codelineno-233-14) +-----------------------+--------------+----------------+--------------+------------------------------+`

**Check Infra services liveness / health status**

Run the below command to verify RDAF infrastructure service's liveness / health status. This command helps to quickly identify any infrastructure service's availability or accessibility issues.

`[](#__codelineno-234-1) rdaf infra healthcheck`

Example Output

`[](#__codelineno-235-1) +----------------+-----------------+--------+------------------------------+----------------+--------------+ [](#__codelineno-235-2) | Name           | Check           | Status | Reason                       | Host           | Container Id | [](#__codelineno-235-3) +----------------+-----------------+--------+------------------------------+----------------+--------------+ [](#__codelineno-235-4) | haproxy        | Port Connection | OK     | N/A                          | 192.168.107.63 | a78256a09ee6 | [](#__codelineno-235-5) | haproxy        | Service Status  | OK     | N/A                          | 192.168.107.63 | a78256a09ee6 | [](#__codelineno-235-6) | haproxy        | Firewall Port   | OK     | N/A                          | 192.168.107.63 | a78256a09ee6 | [](#__codelineno-235-7) | haproxy        | Port Connection | OK     | N/A                          | 192.168.107.64 | 968fe5c56865 | [](#__codelineno-235-8) | haproxy        | Service Status  | OK     | N/A                          | 192.168.107.64 | 968fe5c56865 | [](#__codelineno-235-9) | haproxy        | Firewall Port   | OK     | N/A                          | 192.168.107.64 | 968fe5c56865 | [](#__codelineno-235-10) | keepalived     | Service Status  | OK     | N/A                          | 192.168.107.63 | N/A          | [](#__codelineno-235-11) | keepalived     | Service Status  | OK     | N/A                          | 192.168.107.64 | N/A          | [](#__codelineno-235-12) | nats           | Port Connection | OK     | N/A                          | 192.168.107.63 | ca708ba9a4ae | [](#__codelineno-235-13) | nats           | Service Status  | OK     | N/A                          | 192.168.107.63 | ca708ba9a4ae | [](#__codelineno-235-14) | nats           | Firewall Port   | OK     | N/A                          | 192.168.107.63 | ca708ba9a4ae | [](#__codelineno-235-15) +----------------+-----------------+--------+------------------------------+----------------+--------------+`

Note

Below steps are applicable only if RDAF Application (OIA/AIA) services are going to be installed.

*   Run the below command to update the necessary HAProxy load-balancer configuration for RDAF **OIA** / **AIA** application services.

`[](#__codelineno-236-1) rdaf app update-config OIA`

`[](#__codelineno-237-1) rdaf app update-config AIA`

After deploying the RDAF OIA application services, it is mandatory to run the `rdaf app update-config` which will apply and restart the HAProxy load-balancer service automatically.

### ****7.6 RDAF Platform Services Installation****

KubernetesNon-Kubernetes

`rdafk8s platform install` command is used to deploy / install RDAF core platform services.

Run the below command to deploy all RDAF core platform services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com)

`[](#__codelineno-238-1) rdafk8s platform install --tag 3.4.2`

As part of the installation of RDAF core platform services, it creates a default tenant admin user called `admin@cfx.com`

The default password for `admin@cfx.com` is **admin1234**

On first login onto RDAF UI portal, it prompts for resetting the above default password to user's choice.

In order to access RDAF UI portal, open a web browser and type the HAProxy server's IP address if it is a non-HA deployment or HAProxy server's virtual IP address if it is an HA deployment as shown below.

`[](#__codelineno-239-1) https://192.168.125.148`

**Status check**

Run the below command to see the status of all of the deployed RDAF core platform services.

`[](#__codelineno-240-1) rdafk8s platform status`

Example Output

`[](#__codelineno-241-1) +---------------------+----------------+---------------+----------------+-------+ [](#__codelineno-241-2) | Name                | Host           | Status        | Container Id   | Tag   | [](#__codelineno-241-3) +---------------------+----------------+---------------+----------------+-------+ [](#__codelineno-241-4) | rda-api-server      | 192.168.131.46 | Up 1 Days ago | faf4cdd79dd4   | 3.4.2 | [](#__codelineno-241-5) | rda-api-server      | 192.168.131.44 | Up 1 Days ago | 409c81c1000d   | 3.4.2 | [](#__codelineno-241-6) | rda-registry        | 192.168.131.46 | Up 1 Days ago | fa2682e9f7bb   | 3.4.2 | [](#__codelineno-241-7) | rda-registry        | 192.168.131.45 | Up 1 Days ago | 91eca9476848   | 3.4.2 | [](#__codelineno-241-8) | rda-identity        | 192.168.131.46 | Up 1 Days ago | 4e5e337eabe7   | 3.4.2 | [](#__codelineno-241-9) | rda-identity        | 192.168.131.44 | Up 1 Days ago | b10571cfa217   | 3.4.2 | [](#__codelineno-241-10) | rda-fsm             | 192.168.131.44 | Up 1 Days ago | 1cea17b4d5e0   | 3.4.2 | [](#__codelineno-241-11) | rda-fsm             | 192.168.131.46 | Up 1 Days ago | ac34fce6b2aa   | 3.4.2 | [](#__codelineno-241-12) | rda-chat-helper     | 192.168.131.45 | Up 1 Days ago | ea083e20a082   | 3.4.2 | [](#__codelineno-241-13) +---------------------+---------------+---------------+----------------+--------+`

Below are the Kubernetes Cluster `kubectl` commands to check the status of RDA Fabric core platform services.

`[](#__codelineno-242-1) kubectl get pods -n rda-fabric -l app_category=rdaf-platform`

Example Output

`[](#__codelineno-243-1) NAME                                    READY   STATUS    RESTARTS   AGE [](#__codelineno-243-2) rda-access-manager-668d68bb67-tks95     1/1     Running   0          11d [](#__codelineno-243-3) rda-api-server-b6c888bdd-nv4jm          1/1     Running   0          11d [](#__codelineno-243-4) rda-asset-dependency-7969f7b657-cmx24   1/1     Running   0          11d [](#__codelineno-243-5) rda-collector-6bd6c79475-52hvg          1/1     Running   0          11d [](#__codelineno-243-6) rda-identity-679864f487-74xtd           1/1     Running   0          11d [](#__codelineno-243-7) rda-portal-59dbd8cc6d-b2sfn             2/2     Running   0          11d [](#__codelineno-243-8) rda-registry-7767f58949-jw6s8           1/1     Running   0          11d [](#__codelineno-243-9) rda-resource-manager-84c9995887-bmzw4   1/1     Running   0          11d [](#__codelineno-243-10) rda-scheduler-5b87b9798f-fxztt          1/1     Running   0          11d [](#__codelineno-243-11) rda-user-preferences-7469dfb75d-b4l5r   1/1     Running   0          11d`

Below `kubectl get pods` command provides additional details of deployed RDAF core platform services (PODs) along with their worker node(s) on which they were deployed.

`[](#__codelineno-244-1) kubectl get pods -n rda-fabric -o wide -l app_category=rdaf-platform`

In order to get detailed status of the each RDAF core platform service POD, run the below `kubectl describe pod` command.

`[](#__codelineno-245-1) kubectl describe pod rda-collector-6bd6c79475-52hvg  -n rda-fabric`

Example Output

`[](#__codelineno-246-1) Name:         rda-collector-6bd6c79475-52hvg [](#__codelineno-246-2) Namespace:    rda-fabric [](#__codelineno-246-3) Priority:     0 [](#__codelineno-246-4) Node:         hari-k8-cluster-infra10819/192.168.108.19 [](#__codelineno-246-5) Start Time:   Tue, 31 Jan 2023 05:00:57 +0000 [](#__codelineno-246-6) Labels:       app=rda-fabric-services [](#__codelineno-246-7)                 app_category=rdaf-platform [](#__codelineno-246-8)                 app_component=rda-collector [](#__codelineno-246-9)                 pod-template-hash=6bd6c79475 [](#__codelineno-246-10) ... [](#__codelineno-246-11) ... [](#__codelineno-246-12) QoS Class:                   Burstable [](#__codelineno-246-13) Node-Selectors:              rdaf_platform_services=allow [](#__codelineno-246-14) Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s [](#__codelineno-246-15)                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s [](#__codelineno-246-16)                             pod-type=rda-tenant:NoSchedule [](#__codelineno-246-17) Events:                      <none>`

`rdaf platform install` command is used to deploy / install RDAF core platform services.

Run the below command to deploy all RDAF core platform services.

`[](#__codelineno-247-1) rdaf platform install --tag 3.4.2`

As part of the installation of RDAF core platform services, it creates a default tenant admin user called `admin@cfx.com`

The default password for `admin@cfx.com` is **admin1234**

On first login onto RDAF UI portal, it prompts for resetting the above default password to user's choice.

In order to access RDAF UI portal, open a web browser and type the HAProxy server's IP address if it is a non-HA deployment or HAProxy server's virtual IP address if it is an HA deployment as shown below.

`[](#__codelineno-248-1) https://192.168.125.148`

**Status check**

Run the below command to see the status of all of the deployed RDAF infrastructure services.

`[](#__codelineno-249-1) rdaf platform status`

Example Output

`[](#__codelineno-250-1) +--------------------------+----------------+------------+--------------+-------+ [](#__codelineno-250-2) | Name                     | Host           | Status     | Container Id | Tag   | [](#__codelineno-250-3) +--------------------------+----------------+------------+--------------+-------+ [](#__codelineno-250-4) | rda_api_server           | 192.168.107.61 | Up 5 hours | 6fc70d6b82aa | 3.4.2 | [](#__codelineno-250-5) | rda_api_server           | 192.168.107.62 | Up 5 hours | afa31a2c614b | 3.4.2 | [](#__codelineno-250-6) | rda_registry             | 192.168.107.61 | Up 5 hours | 9f8adbb08b95 | 3.4.2 | [](#__codelineno-250-7) | rda_registry             | 192.168.107.62 | Up 5 hours | cc8e5d27eb0a | 3.4.2 | [](#__codelineno-250-8) | rda_scheduler            | 192.168.107.61 | Up 5 hours | f501e240e7a3 | 3.4.2 | [](#__codelineno-250-9) | rda_scheduler            | 192.168.107.62 | Up 5 hours | c5b2b258efe1 | 3.4.2 | [](#__codelineno-250-10) | rda_collector            | 192.168.107.61 | Up 5 hours | 2260fc37ebe5 | 3.4.2 | [](#__codelineno-250-11) | rda_collector            | 192.168.107.62 | Up 5 hours | 3e7ab4518394 | 3.4.2 | [](#__codelineno-250-12) +--------------------------+----------------+------------+--------------+-------+`

### ****7.7 RDAF Client (rdac) CLI Installation****

KubernetesNon-Kubernetes

`rdafk8s rdac_cli` command allows you to install RDA client CLI utility which interacts with RDA Fabric services and operations.

*   To install RDA client CLI, run the below command

`[](#__codelineno-251-1) rdafk8s rdac_cli install --tag 3.4.2`

*   Run the below command to see RDA client CLI help and available subcommand options.

`[](#__codelineno-252-1) rdac -h`

Example Output

`[](#__codelineno-253-1) Run with one of the following commands [](#__codelineno-253-2) [](#__codelineno-253-3)     agent-bots                List all bots registered by agents for the current tenant [](#__codelineno-253-4)     agents                    List all agents for the current tenant [](#__codelineno-253-5)     alert-rules               Alert Rule management commands [](#__codelineno-253-6)     bot-catalog-generation-from-file  Generate bot catalog for given sources [](#__codelineno-253-7)     bot-package               Bot Package management commands [](#__codelineno-253-8)     bots-by-source            List bots available for given sources [](#__codelineno-253-9)     check-credentials         Perform credential check for one or more sources on a worker pod [](#__codelineno-253-10)     checksum                  Compute checksums for pipeline contents locally for a given JSON file [](#__codelineno-253-11)     compare                   Commands to compare different RDA systems using different RDA Config files [](#__codelineno-253-12)     content-to-object         Convert data from a column into objects [](#__codelineno-253-13)     copy-to-objstore          Deploy files specified in a ZIP file to the Object Store [](#__codelineno-253-14)     dashboard                 User defined dashboard management commands [](#__codelineno-253-15)     dashgroup                 User defined dashboard-group management commands [](#__codelineno-253-16)     dataset                   Dataset management commands [](#__codelineno-253-17)     demo                      Demo related commands [](#__codelineno-253-18)     deployment                Service Blueprints (Deployments) management commands [](#__codelineno-253-19)     event-gw-status           List status of all ingestion endpoints at all the event gateways [](#__codelineno-253-20)     evict                     Evict a job from a worker pod [](#__codelineno-253-21)     file-ops                  Perform various operations on local files [](#__codelineno-253-22)     file-to-object            Convert files from a column into objects [](#__codelineno-253-23)     fmt-template              Formatting Templates management commands [](#__codelineno-253-24)     healthcheck               Perform healthcheck on each of the Pods [](#__codelineno-253-25)     invoke-agent-bot          Invoke a bot published by an agent [](#__codelineno-253-26)     jobs                      List all jobs for the current tenant [](#__codelineno-253-27)     logarchive                Logarchive management commands [](#__codelineno-253-28)     object                    RDA Object management commands [](#__codelineno-253-29)     output                    Get the output of a Job using jobid. [](#__codelineno-253-30)     pipeline                  Pipeline management commands [](#__codelineno-253-31)     playground                Start Webserver to access RDA Playground [](#__codelineno-253-32)     pods                      List all pods for the current tenant [](#__codelineno-253-33)     project                   Project management commands. Projects can be used to link different tenants / projects from this RDA Fabric or a remote RDA Fabric. [](#__codelineno-253-34)     pstream                   Persistent Stream management commands [](#__codelineno-253-35)     purge-outputs             Purge outputs of completed jobs [](#__codelineno-253-36)     read-stream               Read messages from an RDA stream [](#__codelineno-253-37)     reco-engine               Recommendation Engine management commands [](#__codelineno-253-38)     restore                   Commands to restore backed-up artifacts to an RDA Platform [](#__codelineno-253-39)     run                       Run a pipeline on a worker pod [](#__codelineno-253-40)     run-get-output            Run a pipeline on a worker, and Optionally, wait for the completion, get the final output [](#__codelineno-253-41)     schedule                  Pipeline execution schedule management commands [](#__codelineno-253-42)     schema                    Dataset Model Schema management commands [](#__codelineno-253-43)     secret                    Credentials (Secrets) management commands [](#__codelineno-253-44)     set-pod-log-level         Update the logging level for a given RDA Pod. [](#__codelineno-253-45)     shell                     Start RDA Client interactive shell [](#__codelineno-253-46)     site-profile              Site Profile management commands [](#__codelineno-253-47)     site-summary              Show summary by Site and Overall [](#__codelineno-253-48)     stack                     Application Dependency Mapping (Stack) management commands [](#__codelineno-253-49)     staging-area              Staging Area based data ingestion management commands [](#__codelineno-253-50)     subscription              Show current CloudFabrix RDA subscription details [](#__codelineno-253-51)     synthetics                Data synthesizing management commands [](#__codelineno-253-52)     verify-pipeline           Verify the pipeline on a worker pod [](#__codelineno-253-53)     viz                       Visualize data from a file within the console (terminal) [](#__codelineno-253-54)     watch                     Commands to watch various streams such sas trace, logs and change notifications by microservices [](#__codelineno-253-55)     web-server                Start Webserver to access RDA Client data using REST APIs [](#__codelineno-253-56)     worker-obj-info           List all worker pods with their current Object Store configuration [](#__codelineno-253-57)     write-stream              Write data to the specified stream [](#__codelineno-253-58) [](#__codelineno-253-59) positional arguments: [](#__codelineno-253-60)     command     RDA subcommand to run [](#__codelineno-253-61) [](#__codelineno-253-62) optional arguments: [](#__codelineno-253-63)     -h, --help  show this help message and exit`

Tip

Please refer [RDA Client CLI Usage](https://bot-docs.cloudfabrix.io/beginners_guide/rdac/#3-list-of-all-rda-cli-sub-commands)
 for detailed information.

*   Set RDA Fabric platform's application configuration as `rda` using the below command.

`[](#__codelineno-254-1) rdac rda-app-configure --type rda`

Note

Other supported options for above command are below:

*   `rda`: Choose this option when **only RDA Fabric platform** need to be installed along with RDA Worker and RDA Event Gateway services without OIA (AIOps) application services.
    
*   `aiops`: Choose this option when **Operations Intelligence (OIA, a.k.a AIOps)** application need to be installed.
    
*   `asset`: Choose this option when **Asset Intelligence (AIA)** application need to be installed. (**Note:** AIA application type is deprecated and all of it's capabilities are available through base RDA Fabric platform itself. For more information, please contact cfx-support@cloudfabric.com)
    
*   `all`: Choose this option, when all of the supported applications need to be installed.
    

*   Please restart the RDAF Platform services using the below command.

`[](#__codelineno-255-1) rdafk8s platform down --force`

`[](#__codelineno-256-1) rdafk8s platform up`

*   Run the below `rdac healthcheck` command to check the health status of all of the **RDAF core platform services**.

All of the dependency checks should show as **ok** under **Status** column.

`[](#__codelineno-257-1) rdac healthcheck`

Example Output

`[](#__codelineno-258-1) +-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-------------------------------------------------------+ [](#__codelineno-258-2) | Cat       | Pod-Type                               | Host         | ID       | Site        | Health Parameter                                    | Status   | Message                                               | [](#__codelineno-258-3) |-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-------------------------------------------------------| [](#__codelineno-258-4) | rda_infra | api-server                             | rda-api-serv | b1b910d9 |             | service-status                                      | ok       |                                                       | [](#__codelineno-258-5) | rda_infra | api-server                             | rda-api-serv | b1b910d9 |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-258-6) | rda_app   | asset-dependency                       | rda-asset-de | 090669bf |             | service-status                                      | ok       |                                                       | [](#__codelineno-258-7) | rda_app   | asset-dependency                       | rda-asset-de | 090669bf |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-258-8) | rda_app   | authenticator                          | rda-identity | 57905b20 |             | service-status                                      | ok       |                                                       | [](#__codelineno-258-9) | rda_app   | authenticator                          | rda-identity | 57905b20 |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-258-10) | rda_app   | authenticator                          | rda-identity | 57905b20 |             | DB-connectivity                                     | ok       |                                                       | [](#__codelineno-258-11) | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | service-status                                      | ok       |                                                       | [](#__codelineno-258-12) | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-258-13) | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | service-dependency:registry                         | ok       | 1 pod(s) found for registry                           | [](#__codelineno-258-14) | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | service-initialization-status                       | ok       |                                                       | [](#__codelineno-258-15) | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | DB-connectivity                                     | ok       |                                                       | [](#__codelineno-258-16) | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | service-status                                      | ok       |                                                       | [](#__codelineno-258-17) | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-258-18) | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | service-initialization-status                       | ok       |                                                       | [](#__codelineno-258-19) | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | DB-connectivity                                     | ok       |                                                       | [](#__codelineno-258-20) | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-status                                      | ok       |                                                       | [](#__codelineno-258-21) | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-258-22) | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-dependency:registry                         | ok       | 1 pod(s) found for registry                           | [](#__codelineno-258-23) | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-dependency:cfxdimensions-app-access-manager | ok       | 1 pod(s) found for cfxdimensions-app-access-manager   | [](#__codelineno-258-24) | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-initialization-status                       | ok       |                                                       | [](#__codelineno-258-25) | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | DB-connectivity                                     | ok       |                                                       | [](#__codelineno-258-26) | rda_infra | collector                              | rda-collecto | 99553e51 |             | service-status                                      | ok       |                                                       | [](#__codelineno-258-27) | rda_infra | collector                              | rda-collecto | 99553e51 |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-258-28) | rda_infra | collector                              | rda-collecto | 99553e51 |             | opensearch-connectivity:default                     | ok       |                                                       | [](#__codelineno-258-29) | rda_infra | registry                               | rda-registry | a46cd712 |             | service-status                                      | ok       |                                                       | [](#__codelineno-258-30) | rda_infra | registry                               | rda-registry | a46cd712 |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-258-31) | rda_infra | scheduler                              | rda-schedule | d5537051 |             | service-status                                      | ok       |                                                       | [](#__codelineno-258-32) | rda_infra | scheduler                              | rda-schedule | d5537051 |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-258-33) | rda_infra | scheduler                              | rda-schedule | d5537051 |             | DB-connectivity                                     | ok       |                                                       | [](#__codelineno-258-34) | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | service-status                                      | ok       |                                                       | [](#__codelineno-258-35) | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-258-36) | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | service-dependency:registry                         | ok       | 1 pod(s) found for registry                           | [](#__codelineno-258-37) | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | service-initialization-status                       | ok       |                                                       | [](#__codelineno-258-38) | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | DB-connectivity                                     | ok       |                                                       | [](#__codelineno-258-39) +-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-------------------------------------------------------+`

`rdaf rdac_cli` command allows you to install RDA client CLI utility which interacts with RDA Fabric services and operations.

*   To install RDA client CLI, run the below command

`[](#__codelineno-259-1) rdaf rdac_cli install --tag 3.4.2`

*   Run the below command to see RDA client CLI help and available subcommand options.

`[](#__codelineno-260-1) rdac -h`

Example Output

`[](#__codelineno-261-1) Run with one of the following commands [](#__codelineno-261-2) [](#__codelineno-261-3)     agent-bots                List all bots registered by agents for the current tenant [](#__codelineno-261-4)     agents                    List all agents for the current tenant [](#__codelineno-261-5)     alert-rules               Alert Rule management commands [](#__codelineno-261-6)     bot-catalog-generation-from-file  Generate bot catalog for given sources [](#__codelineno-261-7)     bot-package               Bot Package management commands [](#__codelineno-261-8)     bots-by-source            List bots available for given sources [](#__codelineno-261-9)     check-credentials         Perform credential check for one or more sources on a worker pod [](#__codelineno-261-10)     checksum                  Compute checksums for pipeline contents locally for a given JSON file [](#__codelineno-261-11)     compare                   Commands to compare different RDA systems using different RDA Config files [](#__codelineno-261-12)     content-to-object         Convert data from a column into objects [](#__codelineno-261-13)     copy-to-objstore          Deploy files specified in a ZIP file to the Object Store [](#__codelineno-261-14)     dashboard                 User defined dashboard management commands [](#__codelineno-261-15)     dashgroup                 User defined dashboard-group management commands [](#__codelineno-261-16)     dataset                   Dataset management commands [](#__codelineno-261-17)     demo                      Demo related commands [](#__codelineno-261-18)     deployment                Service Blueprints (Deployments) management commands [](#__codelineno-261-19)     event-gw-status           List status of all ingestion endpoints at all the event gateways [](#__codelineno-261-20)     evict                     Evict a job from a worker pod [](#__codelineno-261-21)     file-ops                  Perform various operations on local files [](#__codelineno-261-22)     file-to-object            Convert files from a column into objects [](#__codelineno-261-23)     fmt-template              Formatting Templates management commands [](#__codelineno-261-24)     healthcheck               Perform healthcheck on each of the Pods [](#__codelineno-261-25)     invoke-agent-bot          Invoke a bot published by an agent [](#__codelineno-261-26)     jobs                      List all jobs for the current tenant [](#__codelineno-261-27)     logarchive                Logarchive management commands [](#__codelineno-261-28)     object                    RDA Object management commands [](#__codelineno-261-29)     output                    Get the output of a Job using jobid. [](#__codelineno-261-30)     pipeline                  Pipeline management commands [](#__codelineno-261-31)     playground                Start Webserver to access RDA Playground [](#__codelineno-261-32)     pods                      List all pods for the current tenant [](#__codelineno-261-33)     project                   Project management commands. Projects can be used to link different tenants / projects from this RDA Fabric or a remote RDA Fabric. [](#__codelineno-261-34)     pstream                   Persistent Stream management commands [](#__codelineno-261-35)     purge-outputs             Purge outputs of completed jobs [](#__codelineno-261-36)     read-stream               Read messages from an RDA stream [](#__codelineno-261-37)     reco-engine               Recommendation Engine management commands [](#__codelineno-261-38)     restore                   Commands to restore backed-up artifacts to an RDA Platform [](#__codelineno-261-39)     run                       Run a pipeline on a worker pod [](#__codelineno-261-40)     run-get-output            Run a pipeline on a worker, and Optionally, wait for the completion, get the final output [](#__codelineno-261-41)     schedule                  Pipeline execution schedule management commands [](#__codelineno-261-42)     schema                    Dataset Model Schema management commands [](#__codelineno-261-43)     secret                    Credentials (Secrets) management commands [](#__codelineno-261-44)     set-pod-log-level         Update the logging level for a given RDA Pod. [](#__codelineno-261-45)     shell                     Start RDA Client interactive shell [](#__codelineno-261-46)     site-profile              Site Profile management commands [](#__codelineno-261-47)     site-summary              Show summary by Site and Overall [](#__codelineno-261-48)     stack                     Application Dependency Mapping (Stack) management commands [](#__codelineno-261-49)     staging-area              Staging Area based data ingestion management commands [](#__codelineno-261-50)     subscription              Show current CloudFabrix RDA subscription details [](#__codelineno-261-51)     synthetics                Data synthesizing management commands [](#__codelineno-261-52)     verify-pipeline           Verify the pipeline on a worker pod [](#__codelineno-261-53)     viz                       Visualize data from a file within the console (terminal) [](#__codelineno-261-54)     watch                     Commands to watch various streams such sas trace, logs and change notifications by microservices [](#__codelineno-261-55)     web-server                Start Webserver to access RDA Client data using REST APIs [](#__codelineno-261-56)     worker-obj-info           List all worker pods with their current Object Store configuration [](#__codelineno-261-57)     write-stream              Write data to the specified stream [](#__codelineno-261-58) [](#__codelineno-261-59) positional arguments: [](#__codelineno-261-60)     command     RDA subcommand to run [](#__codelineno-261-61) [](#__codelineno-261-62) optional arguments: [](#__codelineno-261-63)     -h, --help  show this help message and exit`

Tip

Please refer [RDA Client CLI Usage](https://bot-docs.cloudfabrix.io/beginners_guide/rdac/#3-list-of-all-rda-cli-sub-commands)
 for detailed information.

*   Set RDA Fabric platform's application configuration as `rda` using the below command.

`[](#__codelineno-262-1) rdac rda-app-configure --type rda`

Note

Other supported options for above command are below:

*   `rda`: Choose this option when **only RDA Fabric platform** need to be installed along with RDA Worker and RDA Event Gateway services without OIA (AIOps) application services.
    
*   `aiops`: Choose this option when **Operations Intelligence (OIA, a.k.a AIOps)** application need to be installed.
    
*   `asset`: Choose this option when **Asset Intelligence (AIA)** application need to be installed. (**Note:** AIA application type is deprecated and all of it's capabilities are available through base RDA Fabric platform itself. For more information, please contact cfx-support@cloudfabric.com)
    
*   `all`: Choose this option, when all of the supported applications need to be installed.
    

*   Please restart the RDAF Platform services using the below command.

`[](#__codelineno-263-1) rdaf platform down`

`[](#__codelineno-264-1) rdaf platform up`

*   Run the below `rdac healthcheck` command to check the health status of all of the **RDAF core platform services**.

All of the dependency checks should show as **ok** under **Status** column.

`[](#__codelineno-265-1) rdac healthcheck`

Example Output

`[](#__codelineno-266-1) +-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-------------------------------------------------------+ [](#__codelineno-266-2) | Cat       | Pod-Type                               | Host         | ID       | Site        | Health Parameter                                    | Status   | Message                                               | [](#__codelineno-266-3) |-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-------------------------------------------------------| [](#__codelineno-266-4) | rda_infra | api-server                             | rda-api-serv | b1b910d9 |             | service-status                                      | ok       |                                                       | [](#__codelineno-266-5) | rda_infra | api-server                             | rda-api-serv | b1b910d9 |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-266-6) | rda_app   | asset-dependency                       | rda-asset-de | 090669bf |             | service-status                                      | ok       |                                                       | [](#__codelineno-266-7) | rda_app   | asset-dependency                       | rda-asset-de | 090669bf |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-266-8) | rda_app   | authenticator                          | rda-identity | 57905b20 |             | service-status                                      | ok       |                                                       | [](#__codelineno-266-9) | rda_app   | authenticator                          | rda-identity | 57905b20 |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-266-10) | rda_app   | authenticator                          | rda-identity | 57905b20 |             | DB-connectivity                                     | ok       |                                                       | [](#__codelineno-266-11) | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | service-status                                      | ok       |                                                       | [](#__codelineno-266-12) | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-266-13) | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | service-dependency:registry                         | ok       | 1 pod(s) found for registry                           | [](#__codelineno-266-14) | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | service-initialization-status                       | ok       |                                                       | [](#__codelineno-266-15) | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | DB-connectivity                                     | ok       |                                                       | [](#__codelineno-266-16) | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | service-status                                      | ok       |                                                       | [](#__codelineno-266-17) | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-266-18) | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | service-initialization-status                       | ok       |                                                       | [](#__codelineno-266-19) | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | DB-connectivity                                     | ok       |                                                       | [](#__codelineno-266-20) | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-status                                      | ok       |                                                       | [](#__codelineno-266-21) | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-266-22) | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-dependency:registry                         | ok       | 1 pod(s) found for registry                           | [](#__codelineno-266-23) | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-dependency:cfxdimensions-app-access-manager | ok       | 1 pod(s) found for cfxdimensions-app-access-manager   | [](#__codelineno-266-24) | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-initialization-status                       | ok       |                                                       | [](#__codelineno-266-25) | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | DB-connectivity                                     | ok       |                                                       | [](#__codelineno-266-26) | rda_infra | collector                              | rda-collecto | 99553e51 |             | service-status                                      | ok       |                                                       | [](#__codelineno-266-27) | rda_infra | collector                              | rda-collecto | 99553e51 |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-266-28) | rda_infra | collector                              | rda-collecto | 99553e51 |             | opensearch-connectivity:default                     | ok       |                                                       | [](#__codelineno-266-29) | rda_infra | registry                               | rda-registry | a46cd712 |             | service-status                                      | ok       |                                                       | [](#__codelineno-266-30) | rda_infra | registry                               | rda-registry | a46cd712 |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-266-31) | rda_infra | scheduler                              | rda-schedule | d5537051 |             | service-status                                      | ok       |                                                       | [](#__codelineno-266-32) | rda_infra | scheduler                              | rda-schedule | d5537051 |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-266-33) | rda_infra | scheduler                              | rda-schedule | d5537051 |             | DB-connectivity                                     | ok       |                                                       | [](#__codelineno-266-34) | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | service-status                                      | ok       |                                                       | [](#__codelineno-266-35) | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | minio-connectivity                                  | ok       |                                                       | [](#__codelineno-266-36) | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | service-dependency:registry                         | ok       | 1 pod(s) found for registry                           | [](#__codelineno-266-37) | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | service-initialization-status                       | ok       |                                                       | [](#__codelineno-266-38) | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | DB-connectivity                                     | ok       |                                                       | [](#__codelineno-266-39) +-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-------------------------------------------------------+`

### ****7.8 RDAF Worker Services Installation****

KubernetesNon-Kubernetes

`rdafk8s worker install` command is used to deploy / install RDAF worker services.

Run the below command to deploy all RDAF worker services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com)

`[](#__codelineno-267-1) rdafk8s worker install --tag 3.4.2`

**Status check**

Run the below command to see the status of all of the deployed RDAF worker services.

`[](#__codelineno-268-1) rdafk8s worker status`

Example Output

`[](#__codelineno-269-1) +------------+-----------------+---------------+--------------+---------------------+ [](#__codelineno-269-2) | Name       | Host            | Status        | Container Id | Tag                 | [](#__codelineno-269-3) +------------+-----------------+---------------+--------------+---------------------+ [](#__codelineno-269-4) | rda_worker | 192.168.125.149 | Up 18 seconds | 29cdeefd9d95 |       3.4.2         | [](#__codelineno-269-5) +------------+-----------------+---------------+--------------+---------------------+`

Below are the Kubernetes Cluster `kubectl get pods` commands to check the status of RDA Fabric worker services.

`[](#__codelineno-270-1) kubectl get pods -n rda-fabric -l app_category=rdaf-worker`

Example Output

`[](#__codelineno-271-1) NAME                          READY   STATUS    RESTARTS   AGE [](#__codelineno-271-2) rda-worker-749b977b95-cf757   1/1     Running   0          11d [](#__codelineno-271-3) rda-worker-749b977b95-xkb5w   1/1     Running   0          11d`

Below `kubectl get pods` command provides additional details of deployed RDAF worker services (PODs) along with their worker node(s) on which they were deployed.

`[](#__codelineno-272-1) kubectl get pods -n rda-fabric -o wide -l app_category=rdaf-worker`

In order to get detailed status of the each RDAF worker service POD, run the below `kubectl describe pod` command.

`[](#__codelineno-273-1) kubectl describe pod rda-collector-6bd6c79475-52hvg  -n rda-fabric`

Example Output

`[](#__codelineno-274-1) Name:         rda-worker-749b977b95-cf757 [](#__codelineno-274-2) Namespace:    rda-fabric [](#__codelineno-274-3) Priority:     0 [](#__codelineno-274-4) Node:         hari-k8-cluster-infra10820/192.168.108.20 [](#__codelineno-274-5) Start Time:   Tue, 31 Jan 2023 05:18:11 +0000 [](#__codelineno-274-6) Labels:       app=rda-fabric-services [](#__codelineno-274-7)                 app_category=rdaf-worker [](#__codelineno-274-8)                 app_component=rda-worker [](#__codelineno-274-9)                 pod-template-hash=749b977b95 [](#__codelineno-274-10) ... [](#__codelineno-274-11) ... [](#__codelineno-274-12) QoS Class:                   Burstable [](#__codelineno-274-13) Node-Selectors:              rdaf_worker_services=allow [](#__codelineno-274-14) Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s [](#__codelineno-274-15)                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s [](#__codelineno-274-16)                             pod-type=rda-tenant:NoSchedule [](#__codelineno-274-17) Events:                      <none>`

`rdaf worker install` command is used to deploy / install RDAF worker services.

Run the below command to deploy all RDAF worker services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com)

`[](#__codelineno-275-1) rdaf worker install --tag 3.4.2`

**Status check**

Run the below command to see the status of all of the deployed RDAF worker services.

`[](#__codelineno-276-1) rdaf worker status`

Example Output

`[](#__codelineno-277-1) +------------+-----------------+---------------+--------------+-----------------+ [](#__codelineno-277-2) | Name       | Host            | Status        | Container Id | Tag             | [](#__codelineno-277-3) +------------+-----------------+---------------+--------------+-----------------+ [](#__codelineno-277-4) | rda_worker | 192.168.125.149 | Up 18 seconds | 29cdeefd9d95 |       3.4.2     | [](#__codelineno-277-5) +------------+-----------------+---------------+--------------+-----------------+`

### ****7.9 RDAF App Services Installation****

KubernetesNon-Kubernetes

Please refer the below document to deploy / install RDAF OIA (a.k.a AIOps) application services

*   [**OIA:** Install / Upgrade Operations Intelligence and Analytics (**AIOps**)](https://bot-docs.cloudfabrix.io/installation_guides/oia_deployment/)
    

Please refer the below document to deploy / install RDAF OIA (a.k.a AIOps) application services

*   [**OIA:** Install / Upgrade Operations Intelligence and Analytics (**AIOps**)](https://bot-docs.cloudfabrix.io/installation_guides/oia_deployment/)
    

**8\. SSL Certificates Installation**
-------------------------------------

CloudFabrix's RDA Fabric platform is enabled with HTTPs (SSL/443) access by default for secure communication and it is installed with self-signed certificates during the deployment. However, for production deployments, it is highly recommended to install CA Signed certificates and the below steps help you to install them appropriately.

RDA Fabric platform uses HA Proxy service for managing UI access, incoming traffic (ex: Event / Alert notifications) securely over HTTPs (SSL/443) protocol, and internal application traffic where applicable.

Below steps to provide how to install CA Signed SSL certificates for HA Proxy service.

### **8.1 SSL Certificate Requirements:**

CloudFabrix's dimensions platform's HA Proxy service requires below CA signed SSL certificate files in PEM format.

*   server-ssl-certificate.crt (format: PEM)
*   server-ssl-private.key
*   trusted-ca-intermediate-root.crt (format: PEM)
*   trusted-ca-root.crt (format: PEM)

**OR**

*   server-ssl-certificate.crt (format: PEM)
*   server-ssl-private.key
*   trusted-ca-intermediate-root.crt & trusted-ca-root.crt chain in a single file (format: PEM)

The SSL server certificate that is obtained should match the DNS / FQDN of the cfxDimensions platform VM's IP address (This is also referred to as Common Name or CN within the certificate). Wildcard domain SSL certificate is also supported. The below screen provides an example of how to check the server's ssl certificate's CN name using **openssl** command. (In this example, the RDA Fabric platform's FQDN is cfx-rdaf.cloudfabrix.io and using a wildcard domain name (CN) SSL certificate)

|     |     |
| --- | --- |
| [1](#__codelineno-278-1) | `openssl crl2pkcs7 -nocrl -certfile server-ssl-certificate.crt \| openssl pkcs7 -print_certs -noout` |

![CFX-SSL-Cert1](https://bot-docs.cloudfabrix.io/images/ssl-cert/cfx-rda-ssl-01.png)

Once you have the SSL certificate files as mentioned above, you need to create an SSL certificate chain by grouping them together as a single file in PEM format.

Th below diagram shows a valid CA signed SSL certificate chain flow for reference.

![CFX-SSL-Cert2](https://bot-docs.cloudfabrix.io/images/ssl-cert/cfx-rda-ssl-02.png)

Run the below command to create a valid SSL certificate chain. (supported format is PEM)

|     |     |
| --- | --- |
| [1](#__codelineno-279-1) | `cat server-ssl-private.key server-ssl-certificate.crt trusted-ca-intermediate-root.crt trusted-ca-root.crt > cfx-ssl-haproxy.pem` |

**OR**

|     |     |
| --- | --- |
| [1](#__codelineno-280-1) | `cat server-ssl-private.key server-ssl-certificate.crt trusted-ca-intermediate-and-root-chain.crt > cfx-ssl-haproxy.pem` |

![CFX-SSL-Cert3](https://bot-docs.cloudfabrix.io/images/ssl-cert/cfx-rda-ssl-03.png)

Info

**Note:** The final consolidated SSL certificate chain output is saved to **cfx-ssl-haproxy.pem** file which will be applied to HA Proxy configuration later in this document. The filename used here for reference only.

### **8.2 CA-signed SSL certificate verification:**

Info

**openssl** tool is a pre-requisite for performing SSL certificate validation checks

**Step 1:** Run the below commands to verify both server's SSL certificate and private key. The output of these two commands should match exactly the same.

|     |     |
| --- | --- |
| [1](#__codelineno-281-1) | `openssl x509 -noout -modulus -in server-ssl-certificate.crt \| openssl md5` |

|     |     |
| --- | --- |
| [1](#__codelineno-282-1) | `openssl rsa -noout -modulus -in server-ssl-private.key \| openssl md5` |

**Step 2:** Run the below commands to verify server's SSL certificate, intermediate & root certificate's (chain) date is valid and not expired.

|     |     |
| --- | --- |
| [1](#__codelineno-283-1) | `openssl x509 -noout -in server-ssl-certificate.crt -dates` |

|     |     |
| --- | --- |
| [1](#__codelineno-284-1) | `openssl x509 -noout -in trusted-ca-root.crt -dates` |

|     |     |
| --- | --- |
| [1](#__codelineno-285-1) | `openssl x509 -noout -in trusted-ca-intermediate-root.crt -dates` |

**Step 3:** Run the below commands to verify the public keys contained in the private key file and the server certificate file are the same. The output of these two commands should match.

|     |     |
| --- | --- |
| [1](#__codelineno-286-1) | `openssl x509 -in server-ssl-certificate.crt -noout -pubkey` |

|     |     |
| --- | --- |
| [1](#__codelineno-287-1) | `openssl rsa -in server-ssl-private.key -pubout` |

**Step 4:** Run the below command to verify the validity of the certificate chain. The response should come out as **OK**.

|     |     |
| --- | --- |
| [1](#__codelineno-288-1) | `openssl verify -CAfile trusted-ca-root.crt server-ssl-certificate.crt` |

**OR**

|     |     |
| --- | --- |
| [1](#__codelineno-289-1) | `openssl verify -CAfile trusted-ca-intermediate-and-root-chain.crt server-ssl-certificate.crt` |

**Step 5:** Run the below command to see and verify SSL certificate chain order is correct.

|     |     |
| --- | --- |
| [1](#__codelineno-290-1) | `openssl crl2pkcs7 -nocrl -certfile cfx-ssl-haproxy.pem \| openssl pkcs7 -print_certs -noout` |

Please refer to the below screenshot on how to validate the SSL certificate chain order.

![CFX-SSL-Cert4](https://bot-docs.cloudfabrix.io/images/ssl-cert/cfx-rda-ssl-04.png)

Verify if the SSL certificate and key is in PEM format.

|     |     |
| --- | --- |
| [1](#__codelineno-291-1) | `openssl rsa -inform PEM -in server-ssl-private.key` |

|     |     |
| --- | --- |
| [1](#__codelineno-292-1) | `openssl x509 -inform PEM -in server-ssl-certificate.crt` |

### **8.3 CA-signed SSL Certificate Installation for HA Proxy service:**

**Step 1:** Go to HAProxy service's certificates path on VM host(s) where HAProxy service was installed.

|     |     |
| --- | --- |
| [1](#__codelineno-293-1) | `/opt/rdaf/cert/<HAProxy IP>/` |

**Step 2:** Take a backup of the existing HA Proxy service's SSL certificate

|     |     |
| --- | --- |
| [1](#__codelineno-294-1) | `cp haproxy.pem haproxy.pem.backup` |

**Step 3:** Copy the CA-signed SSL certificate chain file that is in PEM format to this location as **haproxy.pem**

|     |     |
| --- | --- |
| [1](#__codelineno-295-1) | `cp <ssl-cert-path>/cfx-ssl-haproxy.pem haproxy.pem` |

**Step 4:** Restart HA Proxy container

|     |     |
| --- | --- |
| [1](#__codelineno-296-1) | `docker ps -a \| grep haproxy` |

|     |     |
| --- | --- |
| [1](#__codelineno-297-1) | `docker restart <haproxy-container-id>` |

**Step 5:** Verify HA Proxy service logs to make sure there are no errors after installing CA signed SSL server certificate chain file.

|     |     |
| --- | --- |
| [1](#__codelineno-298-1) | `docker logs -f <haproxy-container-id> --tail 200` |

**Step 6:** Run the below **openssl** command to verify the newly installed SSL certificate and check SSL verification is shown as **OK** without any validation failures.

|     |     |
| --- | --- |
| [1](#__codelineno-299-1) | `openssl s_client -connect <cfx-platform-FQDN>:443` |

**Step 7:** Open an internet browser (Firefox / Chrome / Safari) and enter the RDA Fabric Platform's FQDN to access the UI securely over HTTPs (port: 443) protocol.

**https://cfx-rdaf-platform-fqdn**

### **8.4 Self Signed SSL Certificate with Custom CA Root:**

The **truststore** or **root store** is a file that contains the root certificates for Certificate Authorities (CA) that issue SSL certificates such as GoDaddy, Verisign, Network Solutions, Comodo and others. Internet browsers, operating systems and applications include list of authorized SSL certificate authorities within their root store or truststore repository file.

However, many enterprises may use Custom CA root certificates to validate and certify self-signed SSL certificates for internal use. In such scenario, when an application is being accessed through a browser or an SSL client, SSL certificate verification error may be observed. Because, neither the browser nor the SSL client will have the Custom CA root certificate within their root store / truststore repository file and hence, they will fail to recognize the authenticity of the SSL certificate and the issuer (CA) from the application.

In order to resolve this issue, update the client's root store / truststore with the Custom CA root & intermediate root certificates so that they can recognize them as a valid & trusted Certificate Authority (CA). Please refer the client's (internet browser or application) documentation on how to update their root store / truststore with custom CA root certificates.

Warning

**Note:** Please take guidance from your internal security team while using self-signed SSL certificates with Custom CA root certificates.

### **8.5 Appendix:**

**SSL Certificate Formats and Conversion:**

SSL certificate files come in different formats and most common ones that CA's (Certificate Authorities) deliver include .pfx, .p7b, .pem, .crt, .cer, and .cert. You can get more details about these different certificate formats in the following link:

[https://comodosslstore.com/resources/a-ssl-certificate-file-extension-explanation-pem-pkcs7-der-and-pkcs12/](https://comodosslstore.com/resources/a-ssl-certificate-file-extension-explanation-pem-pkcs7-der-and-pkcs12/)

If you need to convert the format of your SSL certificate files to PEM, please use the following commands:

*   **Convert PFX to PEM**

|     |     |
| --- | --- |
| [1](#__codelineno-300-1) | `openssl pkcs12 -in server-ssl-certificate.pfx -out server-ssl-certificate.pem -nodes` |

*   **Convert P7B to PEM**

|     |     |
| --- | --- |
| [1](#__codelineno-301-1) | `openssl pkcs7 -print_certs -in server-ssl-certificate.p7b -out server-ssl-certificate.pem` |

*   **Convert DER to PEM**

|     |     |
| --- | --- |
| [1](#__codelineno-302-1) | `openssl x509 -inform der -in server-ssl-certificate.cer -out server-ssl-certificate.pem` |

You can use the following commands to check if your certificate files are already in the required format:

*   **Check and verify if your key is in PEM format**

|     |     |
| --- | --- |
| [1](#__codelineno-303-1) | `openssl rsa -inform PEM -in server-ssl-private.key` |

*   **Check and verify if your certificate is in PEM format**

|     |     |
| --- | --- |
| [1](#__codelineno-304-1) | `openssl x509 -inform PEM -in server-ssl-certificate.pem` |

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!