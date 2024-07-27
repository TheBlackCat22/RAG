 



# Guide to Install and Configure RDA Fabric platform in on-premise environment.

## **1\. RDAF platform and it's components**

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

## **2\. Docker registry access for RDAF platform services deployment**

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

## **3\. HTTP Proxy support for deployment**

RHELUbuntu

Optionally, RDA Fabric docker images can also be accessed over HTTP proxy during the deployment if one is configured to control the internet access.

On all of the RDA Fabric machines where the services going to be deployed, should be configured with HTTP proxy settings.

*   Edit **/etc/environment** file and define HTTP Proxy server settings as shown below.


```
http_proxy="http://<username>:<password>@192.168.142.10:3128" https_proxy="http://<username>:<password>@192.168.142.10:3128" no_proxy="localhost,127.0.0.1,192.168.192.201,192.168.192.202,192.168.192.203,192.168.192.204,*.rhel.pool.ntp.org,*.us.pool.ntp.org" HTTP_PROXY="http://<username>:<password>@192.168.142.10:3128" HTTPS_PROXY="http://<username>:<password>@192.168.142.10:3128" NO_PROXY="localhost,127.0.0.1,192.168.192.201,192.168.192.202,192.168.192.203,192.168.192.204,*.rhel.pool.ntp.org,*.us.pool.ntp.org" export http_proxy https_proxy no_proxy HTTP_PROXY HTTPS_PROXY NO_PROXY
```

Info

**Note:** IP Address details are given for a reference only. They need to be replaced with appropriate HTTP Proxy server IP and port applicable to your environment.

Warning

**Note:** For **no\_proxy** and **NO\_PROXY** environment variables, please include loopback and IP addresses of all RDA platform, infrastructure, application and worker nodes. This will ensure to avoid internal RDA Fabric's application traffic going through HTTP proxy server.

Additionally, include any target applications or devices IP address or DNS names where it doesn't require to go through HTTP Proxy server.

Optionally, RDA Fabric docker images can also be accessed over HTTP proxy during the deployment if one is configured to control the internet access.

On all of the RDA Fabric machines where the services going to be deployed, should be configured with HTTP proxy settings.

*   Edit **/etc/profile.d/proxy.sh** file and define HTTP Proxy server settings as shown below.


```
sudo vi /etc/profile.d/proxy.sh
```


```
http_proxy="http://<username>:<password>@192.168.142.10:3128" https_proxy="http://<username>:<password>@192.168.142.10:3128" no_proxy="localhost,127.0.0.1,192.168.192.201,192.168.192.202,192.168.192.203,192.168.192.204,*.rhel.pool.ntp.org,*.us.pool.ntp.org" HTTP_PROXY="http://<username>:<password>@192.168.142.10:3128" HTTPS_PROXY="http://<username>:<password>@192.168.142.10:3128" NO_PROXY="localhost,127.0.0.1,192.168.192.201,192.168.192.202,192.168.192.203,192.168.192.204,*.rhel.pool.ntp.org,*.us.pool.ntp.org" export http_proxy https_proxy no_proxy HTTP_PROXY HTTPS_PROXY NO_PROXY
```

*   Update file permissions with **execute** and source the file or logout and login again to enable the http proxy settings.


```
sudo chmod +x /etc/profile.d/proxy.sh source /etc/profile.d/proxy.sh
```

*   Configure http proxy for APT package manager by editing **/etc/apt/apt.conf.d/80proxy** file as shown below.


```
sudo vi /etc/apt/apt.conf.d/80proxy
```


```
Acquire::http::proxy "http://<username>:<password>@192.168.142.10:3128"; Acquire::https::proxy "http://<username>:<password>@192.168.142.10:3128";
```

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
```
 sudo vi /etc/hosts

```
```
 127.0.0.1  localhost 
 54.177.20.202 cfxregistry.cloudfabrix.io 
 54.146.255.141 quay.io

```

Note

quay.io is having a dynamic ip, so before updating the host file check the ip again by using the command mentioned below.
```
 ping quay.io

```

Example Output

![images Quay.Io ](https://bot-docs.cloudfabrix.io/images/quay_io.png)

*   Please check the DNS Server Settings by using the below command
```
 resolvectl status

```

Example Output
```
 Current DNS Server: 192.168.159.101 
         DNS Servers: 192.168.159.101 
                       192.168.159.100

```

*   To update the additional DNS Servers please run the below command
```
 vi /etc/netplan/00-netcfg.yaml

```

Example Output
```
 network: 
     version: 2 
     renderer: networkd 
     ethernets: 
       ens160: 
         dhcp4: no 
         dhcp6: no 
         addresses: [192.168.125.66/24] 
         gateway4:  192.168.125.1 
         nameservers: 
           addresses: [192.168.159.101,192.168.159.100]

```

*   To apply the above changes please run the below command
```
 sudo netplan apply

```

*   If you still see any DNS Server settings issue, please run the below commands
```
 sudo systemctl restart systemd-resolved

```
```
 sudo systemctl status systemd-resolved

```

*   Configure Docker Daemon with HTTP Proxy server settings.


```
sudo mkdir -p /etc/systemd/system/docker.service.d cd /etc/systemd/system/docker.service.d
```

Create a file called **http-proxy.conf** under above directory and add the HTTP Proxy configuration lines as shown below.


```
vi http-proxy.conf
```


```
[Service] Environment="HTTP_PROXY=http://<username>:<password>@192.168.142.10:3128" Environment="HTTPS_PROXY=http://<username>:<password>@192.168.142.10:3128" Environment="NO_PROXY=localhost,127.0.0.1,192.168.192.201,192.168.192.202,192.168.192.203,192.168.192.204,*.rhel.pool.ntp.org,*.us.pool.ntp.org"
```

Warning

**Note:** If there is an username and password required for HTTP Proxy server authentication, and if the username has any special characters like "\\" (ex: username\\domain), it need to be entered in HTTP encoded format. This is applicable only for Docker daemon. Please follow the below instructions.

**HTTP Encode / Decode URL:** [https://www.urlencoder.org](https://www.urlencoder.org)

If the username is john\\acme.com : The HTTP encoded value is john%%5Cacme.com and the HTTP Proxy configuration looks like below.


```
[Service] Environment="HTTP_PROXY=http://john%5Cacme.com:password@192.168.142.10:3128" Environment="HTTPS_PROXY=http://john%5Cacme.com:password@192.168.142.10:3128" Environment="NO_PROXY=localhost,127.0.0.1,192.168.192.201,192.168.192.202,192.168.192.203,192.168.192.204,*.rhel.pool.ntp.org,*.us.pool.ntp.org"
```

*   Restart the RDA Platform, Infrastructure, Application and Worker node VMs to apply the HTTP Proxy server settings.
    
*   To apply the HTTP Proxy server settings at the docker level please run the below 2 given commands
```
 sudo systemctl daemon-reload

```
```
 sudo systemctl restart docker

```

*   After restarting the docker services please verify the configuration by checking the docker environment using below command
```
 sudo systemctl show --property=Environment docker

```

Example Output
```
 Environment=HTTP_PROXY=http://192.168.125.66:3128 HTTPS_PROXY=https://192.168.125.66:3129 NO_PROXY=localhost,127.0.0.1,cfxregistry.cloudfabrix.io

```

Note

You can find more info about docker proxy configuration in below URL [https://docs.docker.com/config/daemon/systemd/#httphttps-proxy](https://docs.docker.com/config/daemon/systemd/#httphttps-proxy "https://docs.docker.com/config/daemon/systemd/#httphttps-proxy")

*   Verify if you are able to connect to CloudFabrix docker registry URL running the below command.
```
 curl -vv https://cfxregistry.cloudfabrix.io:443

```

Example Output
```
 curl -vv https://cfxregistry.cloudfabrix.io:443 
 * Rebuilt URL to: https://cfxregistry.cloudfabrix.io:443/ 
 *   Trying 54.177.20.202... 
 * TCP_NODELAY set 
 * Connected to cfxregistry.cloudfabrix.io (54.177.20.202) port 443 (#0) 
 * ALPN, offering h2 
 * ALPN, offering http/1.1 
 * successfully set certificate verify locations: 
 *   CAfile: /etc/pki/tls/certs/ca-bundle.crt 
   CApath: none 
 * TLSv1.3 (OUT), TLS handshake, Client hello (1): 
 * TLSv1.3 (IN), TLS handshake, Server hello (2): 
 * TLSv1.2 (IN), TLS handshake, Certificate (11): 
 . 
 . 
 . 
 *  SSL certificate verify ok. 
 > GET / HTTP/1.1 
 > Host: cfxregistry.cloudfabrix.io 
 > User-Agent: curl/7.61.1 
 > Accept: */* 
 > 
 < HTTP/1.1 200 OK

```

*   After configuring the Docker deamon, Please run the below `docker login` command to verify if Docker daemon is able to access CloudFabrix docker registry service.
```
 docker login -u=readonly -p=readonly cfxregistry.cloudfabrix.io

```

Example Output
```
 WARNING! Using --password via the CLI is insecure. Use --password-stdin. 
 WARNING! Your password will be stored unencrypted in /home/rdauser/.docker/config.json. 
 Configure a credential helper to remove this warning. See 
 https://docs.docker.com/engine/reference/commandline/login/#credentials-store 
 
 Login Succeeded

```

**Login Succeeded** should be seen as shown in the above command's output.

## **4\. RDAF platform resource requirements**

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

## **5\. RDAF platform VMs deployment using OVF**

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


```
sudo tzselect sudo timedatectl sudo timedatectl set-timezone Europe/London
```

Important

The **date & time** settings should be in **sync** across all of RDA Fabric VMs for the application services to function appropriately.

To manually sync VM's time with NTP server, run the below commands.


```
sudo systemctl stop chronyd sudo chronyd -q 'server <ntp-server-ip> iburst' sudo systemctl start chronyd
```

To configure and update the NTP server settings, please update **/etc/chrony/chrony.conf** with NTP server details and restart the **Chronyd** service


```
sudo systemctl stop chronyd sudo vi /etc/chrony/chrony.conf # Add the below line at the end of the file. Repeat the line for each NTP server's IP Address server <ntp-server-ip> prefer iburst sudo systemctl start chronyd
```

**Firewall Configuration:**

Ubuntu 20.xRHEL 8.x

Run the below commands to open or close application service ports within the firewall service if needed.


```
sudo ufw allow <port-number>/<tcp/udp> sudo ufw deny <port-number>/<tcp/udp>
```

Run the below commands to open or close application service ports within the firewall service if needed.


```
sudo firewall-cmd --add-port <port-number>/<tcp/udp> --permanent sudo firewall-cmd --remove-port <port-number>/<tcp/udp> --permanent sudo firewall-cmd --reload
```

**Verify network bandwidth between RDAF VMs:**

For production deployment, the network bandwidth between RDAF VMs should be minimum of 10Gbps. CloudFabrix provided OVF comes with `iperf` utility which can be used to measure the network bandwidth.

UbuntuRHEL

To verify network bandwidth between RDAF platform service VM and infrastructure VM, follow the below steps.

Login into RDAF platform service VM as **rdauser** using SSH client to access the CLI and start `iperf` utility as a server.

Info

By default `iperf` listens on port **5001** over tcp

Enable the `iperf` server port using the below command.
```
 sudo ufw allow 5001/tcp

```

Start the `iperf` server as shown below.
```
 iperf -s

```

Example Output
```
 $ iperf -s 
 
 ------------------------------------------------------------ 
 Server listening on TCP port 5001 
 TCP window size: 85.3 KByte (default) 
 ------------------------------------------------------------

```

Now, login into RDAF infrastructure service VM as **rdauser** using SSH client to access the CLI and start `iperf` utility as a client.
```
 iperf -c <RDAF-Platform-VM-IP>

```

`operf` utility connects to RDAF platform service VM as shown below. It will connect and verify the network bandwidth speed.

Example Output
```
 ------------------------------------------------------------ 
 Client connecting to 192.168.125.143, TCP port 5001 
 TCP window size: 2.86 MByte (default) 
 ------------------------------------------------------------ 
 [  3] local 192.168.125.141 port 10654 connected with 192.168.125.143 port 5001 
 [ ID] Interval       Transfer     Bandwidth 
 [  3]  0.0-10.0 sec  21.2 GBytes  18.2 Gbits/sec

```

Repeat the above steps between all of the RDAF VMs in both directions to make sure the network bandwidth speed is minimum of 10Gbps.

To verify network bandwidth between RDAF platform service VM and infrastructure VM, follow the below steps.

Login into RDAF platform service VM as **rdauser** using SSH client to access the CLI and start `iperf` utility as a server.

Info

By default `iperf` listens on port **5001** over tcp

Enable the `iperf` server port using the below command.
```
 sudo firewall-cmd --add-port 5001/tcp --permanent 
 sudo firewall-cmd --reload

```

Start the `iperf` server as shown below.
```
 iperf -s

```
```
 $ iperf -s 
 
 ------------------------------------------------------------ 
 Server listening on TCP port 5001 
 TCP window size: 85.3 KByte (default) 
 ------------------------------------------------------------

```

Now, login into RDAF infrastructure service VM as **rdauser** using SSH client to access the CLI and start `iperf` utility as a client.
```
 iperf -c <RDAF-Platform-VM-IP>

```

`operf` utility connects to RDAF platform service VM as shown below. It will connect and verify the network bandwidth speed.

Example Output
```
 ------------------------------------------------------------ 
 Client connecting to 192.168.125.143, TCP port 5001 
 TCP window size: 2.86 MByte (default) 
 ------------------------------------------------------------ 
 [  3] local 192.168.125.141 port 10654 connected with 192.168.125.143 port 5001 
 [ ID] Interval       Transfer     Bandwidth 
 [  3]  0.0-10.0 sec  21.2 GBytes  18.2 Gbits/sec

```

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


```
lsblk -S
```

Example Output
```
 NAME HCTL       TYPE VENDOR   MODEL         REV TRAN 
 sda  2:0:0:0    disk VMware   Virtual_disk 1.0   
 sdb  2:0:1:0    disk VMware   Virtual_disk 1.0   
 sdc  2:0:2:0    disk VMware   Virtual_disk 1.0   
 sdd  2:0:3:0    disk VMware   Virtual_disk 1.0

```

Run the below command to see the new disk along with used disks with their mount points


```
lsblk
```

Example Output
```
 NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT 
 ... 
 sda                         8:0    0   75G  0 disk  
 ├─sda1                      8:1    0    1M  0 part  
 ├─sda2                      8:2    0  1.5G  0 part /boot 
 └─sda3                      8:3    0 48.5G  0 part  
   └─ubuntu--vg-ubuntu--lv 253:0    0 48.3G  0 lvm  / 
 sdb                         8:16   0   25G  0 disk /var/lib/docker 
 sdc                         8:32   0   25G  0 disk /opt 
 sdd                         8:48   0   50G  0 disk

```

In the above example command outputs, the newly added disk is **sdd** and it's size is 50GB

**Step-7:** Run the below command to create a new **XFS** filesystem and create a mount point directory.


```
sudo mkfs.xfs /dev/sdd sudo mkdir /minio-data
```

**Step-8:** Run the below command to get the **UUID** of the newly created filesystem on **/dev/sdd**


```
sudo blkid /dev/sdd
```

**Step-9:** Update **/etc/fstab** to mount the **/dev/sdd** disk to **/minio-data** mount point


```
sudo vi /etc/fstab
```

Add the below line and save the **/etc/fstab** file.


```
UUID=<UUID-from-step-8>    /minio-data   xfs defaults    0   0
```

**Step-10:** Mount the **/minio-data** mount point and verify the mount point is mounted.


```
sudo mount -a df -h
```

Example Output
```
 Filesystem                         Size  Used Avail Use% Mounted on 
 /dev/mapper/ubuntu--vg-ubuntu--lv   48G  8.3G   37G  19% / 
 ... 
 /dev/sda2                          1.5G  209M  1.2G  16% /boot 
 /dev/sdb                            25G  211M   25G   1% /var/lib/docker 
 /dev/sdc                            25G  566M   25G   3% /opt 
 /dev/sdd                            50G  390M   50G   1% /minio-data

```

### **5.3 Extending the Root (/) filesystem**

Ubuntu

Warning

**Note-1:** The below provided instructions to extend the **Root (/)** filesystem are applicable only for the virtual machines that are provisioned using CloudFabrix provided Ubuntu OVF

**Note-2:** As a precautionary step, please take VMware VM snapshot before making the changes to **Root (/)** filesystem.

**Step-1:** Check on which disk the **Root (/)** filesystem was created using the below command. In the below example, it was created on disk **/dev/sda** and **partition 3** i.e. **sda3**.

On partition **sda3**, a logical volume **ubuntu--vg-ubuntu--lv** was created and mounted as **Root (/)** filesystem.
```
 lsblk

```

Example Output
```
 NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT 
 loop0                       7:0    0   62M  1 loop  
 loop1                       7:1    0   62M  1 loop /snap/core20/1593 
 loop2                       7:2    0 67.2M  1 loop /snap/lxd/21835 
 loop3                       7:3    0 67.8M  1 loop /snap/lxd/22753 
 loop4                       7:4    0 44.7M  1 loop /snap/snapd/15904 
 loop5                       7:5    0   47M  1 loop /snap/snapd/16292 
 loop7                       7:7    0   62M  1 loop /snap/core20/1611 
 sda                         8:0    0   75G  0 disk  
 ├─sda1                      8:1    0    1M  0 part  
 ├─sda2                      8:2    0  1.5G  0 part /boot 
 └─sda3                      8:3    0 48.5G  0 part  
 └─ubuntu--vg-ubuntu--lv     253:0  0 48.3G  0 lvm  / 
 sdb                         8:16   0  100G  0 disk /var/lib/docker 
 sdc                         8:32   0   75G  0 disk /opt

```

**Step-2:** Verify the **SCSI disk id** of the disk on which **Root (/)** filesystem was created using the below command.

In the below example, the SCSI disk id of root disk **sda** is 2:0:0:0, i.e. the SCSI disk id is 0 (third digit)
```
 lsblk -S

```

Example Output
```
 NAME HCTL       TYPE VENDOR   MODEL         REV TRAN 
 sda  2:0:0:0    disk VMware   Virtual_disk 1.0   
 sdb  2:0:1:0    disk VMware   Virtual_disk 1.0   
 sdc  2:0:2:0    disk VMware   Virtual_disk 1.0

```  

**Step-3:** Edit the virtual machine's properties on vCenter and identify the Root disk **sda** using the above SCSI disk id **2:0:0:0** as highlighted in the below screenshot.

Increase the disk size from 75GB to higher desired value in GB.

![CFXOVFRootExtend](https://bot-docs.cloudfabrix.io/images/ovf/ubuntu_ovf_extend_root_disk.png)

**Step-4:** Login back to Ubuntu VM CLI using SSH client as **rdauser**

Switch to **sudo** user
```
 sudo -s

```

Execute the below command to rescan the **Root disk** i.e. **sda** to reflect the increased disk size.
```
 echo '1' > /sys/class/scsi_disk/2\:0\:0\:0/device/rescan

```

Execute the below command to see the increased size for Root disk **sda**
```
 lsblk

```

Example Output
```
 NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT 
 loop0                       7:0    0   62M  1 loop /snap/core20/1611 
 loop1                       7:1    0 67.8M  1 loop /snap/lxd/22753 
 loop2                       7:2    0 67.2M  1 loop /snap/lxd/21835 
 loop3                       7:3    0   62M  1 loop  
 loop4                       7:4    0   47M  1 loop /snap/snapd/16292 
 loop5                       7:5    0 44.7M  1 loop /snap/snapd/15904 
 loop6                       7:6    0   62M  1 loop /snap/core20/1593 
 sda                         8:0    0  100G  0 disk  
 ├─sda1                      8:1    0    1M  0 part  
 ├─sda2                      8:2    0  1.5G  0 part /boot 
 └─sda3                      8:3    0 48.5G  0 part  
 └─ubuntu--vg-ubuntu--lv     253:0  0 48.3G  0 lvm  / 
 sdb                         8:16   0   25G  0 disk /var/lib/docker 
 sdc                         8:32   0   25G  0 disk /opt

```

**Step-5:** In the above command output, identify the **Root (/) filesystem's** disk partition, i.e. **sda3**

Run the below command **cfdisk** to resize the **Root (/)** filesystem.
```
 cfdisk

```

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
```
 swapoff /swap.img

```

Resize the physical volume of **Root (/)** filesystem i.e. **/dev/sda3**
```
 pvresize /dev/sda3

```

Resize the logical volume of **Root (/) filesystem** i.e. **/dev/mapper/ubuntu--vg-ubuntu--lv**. In the below example, the logical volume of **Root (/)** filesystem is increased by 20GB
```
 lvextend -L +20G /dev/mapper/ubuntu--vg-ubuntu--lv

```

Resize the **Root (/) filesystem**
```
 resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv

```

Enable the swap after resizing the **Root (/)** filesystem
```
 swapon /swap.img

```

**Step-7:**

Verify the increased **Root (/)** filesystem disk's space using the below command.
```
 df -h

```
```
 Filesystem                         Size  Used Avail Use% Mounted on 
 udev                               3.9G     0  3.9G   0% /dev 
 tmpfs                              793M   50M  744M   7% /run 
 /dev/mapper/ubuntu--vg-ubuntu--lv   68G  8.6G   56G  14% / 
 tmpfs                              3.9G     0  3.9G   0% /dev/shm 
 tmpfs                              5.0M     0  5.0M   0% /run/lock 
 tmpfs                              3.9G     0  3.9G   0% /sys/fs/cgroup 
 /dev/loop2                          68M   68M     0 100% /snap/lxd/21835 
 /dev/loop4                          47M   47M     0 100% /snap/snapd/16292 
 /dev/loop1                          68M   68M     0 100% /snap/lxd/22753 
 /dev/loop5                          45M   45M     0 100% /snap/snapd/15904 
 /dev/sda2                          1.5G  209M  1.2G  16% /boot 
 /dev/sdb                            25G  211M   25G   1% /var/lib/docker 
 /dev/sdc                            25G  566M   25G   3% /opt

```

## **6\. RDAF Platform VMs deployment on RHEL/Ubuntu OS**

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
```
 sudo subscription-manager register 
 sudo subscription-manager attach

```

*   Create a new user called **rdauser** and configure the password.
```
 sudo adduser rdauser 
 sudo passwd rdauser 
 sudo chown -R rdauser:rdauser /home/rdauser 
 sudo groupadd docker 
 sudo usermod -aG docker rdauser

```

*   Add **rdauser** to **/etc/sudoers** file. Add the below line at the end of the sudoers file.
```
 rdauser ALL=(ALL) NOPASSWD:ALL

```

*   Modify the SSH service configuration with the below settings. Edit **/etc/ssh/sshd\_config** file and update the below settings as shown below.
```
 PasswordAuthentication yes 
 MaxSessions 10 
 LoginGraceTime 2m

```

*   Restart the SSH service
```
 sudo systemctl restart sshd

```

*   Logout and Login back as newly created user **rdauser**
    
*   Format the disks with **xfs** filesystem and mount the disks as per the disk requirements outlined in **[RDA Fabric VMs resource requirements](#4-rdaf-platform-resource-requirements)
    ** section.
```
 sudo mkfs.xfs /dev/<disk-name>

```

*   Make sure disk mounts are updated in **/etc/fstab** to make them persistent across VM reboots.
    
*   In /etc/fstab, use filesystem's **UUID** instead of using SCSI disk names. Below command provides **UUID** of filesystem created on a disk or disk partition.
```
 sudo blkid /dev/<disk-name>

```

Sample disk mount point entry on **/etc/fstab** file.
```
 UUID=60174ace-e1f6-497e-90e2-7d889e6c5695    /opt   xfs defaults    0   0

```

**Installing OS utilities and Python**

*   Run the below commands to install the required software packages.


```
sudo yum install -y gcc openssl-devel bzip2-devel sqlite-devel xz-devel ncurses-devel readline readline-devel gdbm-devel tcl-devel tk-devel make libffi-devel or sudo dnf install -y gcc openssl-devel bzip2-devel sqlite-devel xz-devel ncurses-devel readline readline-devel gdbm-devel tcl-devel tk-devel make libffi-devel
```


```
sudo yum install -y install -y wget telnet net-tools unzip tar sysstat bind-utils iperf3 xinetd jq yum-utils device-mapper-persistent-data lvm2 mysql or sudo dnf install -y install -y wget telnet net-tools unzip tar sysstat bind-utils iperf3 xinetd jq yum-utils device-mapper-persistent-data lvm2 mysql
```

*   Download and install the below software packages.


```
wget https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/s/sshpass-1.06-9.el8.x86_64.rpm sudo rpm -ivh sshpass-1.06-9.el8.x86_64.rpm
```


```
wget https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/n/nload-0.7.4-16.el8.x86_64.rpm sudo rpm -ivh nload-0.7.4-16.el8.x86_64.rpm
```

*   Download and install **Python 3.7.4** or above. Skip this step if **Python** is already installed as part of the OS install.

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
 | `cd /opt sudo wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz sudo tar xvf Python-3.7.4.tgz sudo chown -R rdauser:rdauser Python-3.7.4 cd /opt/Python-3.7.4 ./configure --enable-optimizations sudo make -j8 build_all sudo make altinstall sudo /usr/local/bin/python3.7 -m venv /opt/PYTHON37 sudo chown -R rdauser:rdauser /opt/PYTHON37 sudo rm -f /opt/Python-3.7.4.tgz sudo alternatives --set python /usr/bin/python3.7 sudo ln -s /usr/local/bin/python3.7 /usr/bin/python sudo ln -s /usr/local/bin/pip3.7 /usr/bin/pip` |

**Installing Docker and Docker-compose**

*   Run the below commands to install docker runtime environment


```
sudo yum config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo or sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
```


```
sudo yum -y install --nobest --allowerasing docker-ce-20.10.5-3.el8 or sudo dnf -y install --nobest --allowerasing docker-ce-20.10.5-3.el8
```


```
sudo systemctl enable docker sudo systemctl start docker sudo systemctl status docker
```

*   Configure docker service configuration updating **/etc/docker/daemon.json** as shown below.
```
 sudo vi /etc/docker/daemon.json

```

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
 | `{ "tls": true,  "tlscacert": "/etc/tlscerts/ca/ca.pem",  "tlsverify": true,  "storage-driver": "overlay2",  "hosts": [ "unix:///var/run/docker.sock",  "tcp://0.0.0.0:2376" ],  "tlskey": "/etc/tlscerts/server/server.key",  "debug": false,  "tlscert": "/etc/tlscerts/server/server.pem",  "experimental": false,  "live-restore": true }` |

*   Download and execute macaw-docker.py script to configure TLS for docker service. (Note: Make sure python2.7 is installed)


```
mkdir ~/cfx-config-files cd ~/cfx-config-files wget https://macaw-amer.s3.amazonaws.com/images/misc/RHEL-bin-files.tar.gz tar -xzvf RHEL-bin-files.tar.gz sudo python2.7 macaw-docker.py
```

*   Edit **/lib/systemd/system/docker.service** file and update the below line and restart the docker service
```
 From: 
 ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock 
 
 To: 
 ExecStart=/usr/bin/dockerd

```

*   Restart docker service and verify the status


```
sudo systemctl restart docker sudo systemctl status docker
```

*   Update `/etc/sysctl.conf` file with below performance tuning settings.
```
 #Performance Tuning. 
 net.ipv4.tcp_rmem = 4096 87380 16777216 
 net.ipv4.tcp_wmem = 4096 65536 16777216 
 net.core.rmem_max = 16777216 
 net.core.wmem_max = 16777216 
 net.core.netdev_max_backlog = 2500 
 net.core.somaxconn = 65000 
 net.ipv4.tcp_ecn = 0 
 net.ipv4.tcp_window_scaling = 1 
 net.ipv4.ip_local_port_range = 10000 65535 
 vm.max_map_count = 1048575 
 net.core.wmem_default=262144 
 net.core.wmem_max=4194304 
 net.core.rmem_default=262144 
 net.core.rmem_max=4194304 
 
 #file max 
 fs.file-max=518144 
 
 #swapiness 
 vm.swappiness = 1 
 #Set runtime for kernel.randomize_va_space 
 kernel.randomize_va_space = 2 
 
 net.ipv4.ip_forward = 1 
 net.ipv4.ip_nonlocal_bind=1

```

*   Install **JAVA** software package


```
sudo mkdir -p /opt/java sudo tar xf ~/cfx-config-files/jdk-8u281-linux-x64.tar.gz -C /opt/java --strip-components 1
```

*   Add the **JAVA** software binary to **PATH** variable
```
 vi ~/.bash_profile 
 PATH=/opt/java/bin:$PATH

```
```
 source ~/.bash_profile

```

*   Reboot the host
```
 sudo reboot

```

*   Once Ubuntu 20.04.x or above OS version is deployed, please apply the below configuration.
    
*   Create a new user called **rdauser** and configure the password.
```
 sudo adduser rdauser 
 sudo passwd rdauser

```
```
 sudo chown -R rdauser:rdauser /home/rdauser 
 sudo groupadd docker 
 sudo usermod -aG docker rdauser

```

*   Add **rdauser** to **/etc/sudoers** file. Add the below line at the end of the sudoers file.
```
 rdauser ALL=(ALL) NOPASSWD:ALL

```

*   Modify the SSH service configuration with the below settings. Edit **/etc/ssh/sshd\_config** file and update as shown below.
```
 PasswordAuthentication yes 
 MaxSessions 10 
 LoginGraceTime 2m

```

*   Restart the SSH service
```
 sudo systemctl restart sshd

```

*   Logout and Login back as newly created user **rdauser**
    
*   Format the disks with **xfs** filesystem and mount the disks as per the disk requirements outlined in **[RDA Fabric VMs resource requirements](#4-rdaf-platform-resource-requirements)
    ** section.
```
 sudo mkfs.xfs /dev/<disk-name>

```

*   Make sure disk mounts are updated in **/etc/fstab** to make them persistent across VM reboots.
    
*   In /etc/fstab, use filesystem's **UUID** instead of using SCSI disk names. Below command provides **UUID** of filesystem created on a disk or disk partition.
```
 sudo blkid /dev/<disk-name>

```

Sample disk mount point entry on **/etc/fstab** file.
```
 UUID=60174ace-e1f6-497e-90e2-7d889e6c5695    /opt   xfs defaults    0   0

```

**Installing OS utilities and Python**

*   Run the below commands to install the required software packages.
```
 sudo apt update

```


```
sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev
```


```
sudo apt install -y wget telnet net-tools unzip tar sysstat bind9-utils iperf3 xinetd jq lvm2 sshpass mysql-client
```

*   Download and install **Python 3.7.4** or above. Skip this step if **Python 3.7.4 or above** is already installed as part of the OS install.

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
 | `cd /opt sudo wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz sudo tar xvf Python-3.7.4.tgz sudo chown -R rdauser:rdauser Python-3.7.4 cd /opt/Python-3.7.4 ./configure --enable-optimizations sudo make -j8 build_all sudo make altinstall sudo /usr/local/bin/python3.7 -m venv /opt/PYTHON37 sudo chown -R rdauser:rdauser /opt/PYTHON37 sudo rm -f /opt/Python-3.7.4.tgz sudo alternatives --set python /usr/bin/python3.7 sudo ln -s /usr/local/bin/python3.7 /usr/bin/python sudo ln -s /usr/local/bin/pip3.7 /usr/bin/pip` |

**Installing Docker and Docker-compose**

*   Run the below commands to install docker runtime environment


```
sudo apt-get install -y ca-certificates curl gnupg lsb-release
```


```
sudo mkdir -p /etc/apt/keyrings curl -fsSL https://download.docker.com/linux/ubuntu/gpg \| sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \       $(lsb_release -cs) stable" \| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```


```
sudo apt-get update -y
```


```
sudo apt-get install docker-ce=5:20.10.12~3-0~ubuntu-focal docker-ce-cli=5:20.10.12~3-0~ubuntu-focal containerd.io docker-compose-plugin
```


```
sudo systemctl enable docker
```

*   Edit **/lib/systemd/system/docker.service** file and update the below line and restart the docker service
```
 sudo vi /lib/systemd/system/docker.service 
 
 From: 
 ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock 
 
 To: 
 ExecStart=/usr/bin/dockerd

```

*   Configure docker service configuration updating **/etc/docker/daemon.json** as shown below.
```
 sudo vi /etc/docker/daemon.json

```

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
 | `{ "tls": true,  "tlscacert": "/etc/tlscerts/ca/ca.pem",  "tlsverify": true,  "storage-driver": "overlay2",  "hosts": [ "unix:///var/run/docker.sock",  "tcp://0.0.0.0:2376" ],  "tlskey": "/etc/tlscerts/server/server.key",  "debug": false,  "tlscert": "/etc/tlscerts/server/server.pem",  "experimental": false,  "live-restore": true }` |

*   Start and verify the docker service


```
sudo systemctl daemon-reload sudo systemctl start docker sudo systemctl status docker
```

*   Update `/etc/sysctl.conf` file with below performance tuning settings.
```
 #Performance Tuning. 
 net.ipv4.tcp_rmem = 4096 87380 16777216 
 net.ipv4.tcp_wmem = 4096 65536 16777216 
 net.core.rmem_max = 16777216 
 net.core.wmem_max = 16777216 
 net.core.netdev_max_backlog = 2500 
 net.core.somaxconn = 65000 
 net.ipv4.tcp_ecn = 0 
 net.ipv4.tcp_window_scaling = 1 
 net.ipv4.ip_local_port_range = 10000 65535 
 vm.max_map_count = 1048575 
 net.core.wmem_default=262144 
 net.core.wmem_max=4194304 
 net.core.rmem_default=262144 
 net.core.rmem_max=4194304 
 
 #file max 
 fs.file-max=518144 
 
 #swapiness 
 vm.swappiness = 1 
 #Set runtime for kernel.randomize_va_space 
 kernel.randomize_va_space = 2 
 
 net.ipv4.ip_forward = 1 
 net.ipv4.ip_nonlocal_bind=1

```

*   Download and execute macaw-docker.py script to configure TLS for docker service.


```
mkdir ~/cfx-config-files cd ~/cfx-config-files wget https://macaw-amer.s3.amazonaws.com/images/misc/RHEL-bin-files.tar.gz tar -xzvf RHEL-bin-files.tar.gz
```

*   Install **JAVA** software package


```
sudo mkdir -p /opt/java sudo tar xf ~/cfx-config-files/jdk-8u281-linux-x64.tar.gz -C /opt/java --strip-components 1
```

*   Add the **JAVA** software binary to **PATH** variable
```
 vi ~/.bashrc 
 PATH=/opt/java/bin:$PATH

```
```
 source ~/.bashrc

```

*   Reboot the host
```
 sudo reboot

```

## **7\. RDAF Platform Installation**

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
```
 wget https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/rdafcli-1.2.2.tar.gz

```

*   Install the `rdaf & rdafk8s` CLI to version 1.2.2
```
 pip install --user --upgrade pip 
 pip install --user rdafcli-1.2.2.tar.gz

```

*   Verify the installed `rdaf & rdafk8s` CLI version is upgraded to 1.2.2
```
 rdaf --version 
 rdafk8s --version

```

*   Download the RDAF Deployment CLI's newer version 1.2.2 bundle and copy it to RDAF management VM on which `rdaf & rdafk8s` deployment CLI was installed.

For RHEL OS EnvironmentFor Ubuntu OS Environment
```
 wget  https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/offline-rhel-1.2.2.tar.gz

```

*   Extract the `rdaf` CLI software bundle contents
```
 tar -xvzf offline-rhel-1.2.2.tar.gz

```

*   Change the directory to the extracted directory
```
 cd offline-rhel-1.2.2

```

*   Install the `rdaf`CLI to version 1.2.2
```
 pip install --user rdafcli-1.2.2.tar.gz  -f ./ --no-index

```

*   Verify the installed `rdaf` CLI version
```
 rdaf --version 
 rdafk8s --version

```
```
 wget  https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/offline-ubuntu-1.2.2.tar.gz

```

*   Extract the `rdaf` CLI software bundle contents
```
 tar -xvzf offline-ubuntu-1.2.2.tar.gz

```

*   Change the directory to the extracted directory
```
 cd offline-ubuntu-1.2.2

```

*   Upgrade the `rdaf`CLI to version 1.2.2
```
 pip install --user rdafcli-1.2.2.tar.gz  -f ./ --no-index

```

*   Verify the installed `rdaf` CLI version
```
 rdaf --version 
 rdafk8s --version

```

With Internet AccessWithout Internet Access

*   Download the RDAF Deployment CLI's newer version 1.2.2 bundle
```
 wget https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/rdafcli-1.2.2.tar.gz

```

*   Install the `rdaf` CLI to version 1.2.2
```
 pip install --user --upgrade pip 
 pip install --user rdafcli-1.2.2.tar.gz

```

*   Verify the installed `rdaf` CLI version is upgraded to 1.2.2
```
 rdaf --version

```

*   Download the RDAF Deployment CLI's newer version 1.2.2 bundle and copy it to RDAF management VM on which `rdaf & rdafk8s` deployment CLI was installed.

For RHEL OS EnvironmentFor Ubuntu OS Environment
```
 wget  https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/offline-rhel-1.2.2.tar.gz

```

*   Extract the `rdaf` CLI software bundle contents
```
 tar -xvzf offline-rhel-1.2.2.tar.gz

```

*   Change the directory to the extracted directory
```
 cd offline-rhel-1.2.2

```

*   Install the `rdaf`CLI to version 1.2.2
```
 pip install --user rdafcli-1.2.2.tar.gz -f ./ --no-index

```

*   Verify the installed `rdaf` CLI version
```
 rdaf --version 
 rdafk8s --version

```
```
 wget  https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/offline-ubuntu-1.2.2.tar.gz

```

*   Extract the `rdaf` CLI software bundle contents
```
 tar -xvzf offline-ubuntu-1.2.2.tar.gz

```

*   Change the directory to the extracted directory
```
 cd offline-ubuntu-1.2.2

```

*   Install the `rdaf`CLI to version 1.2.2
```
 pip install --user rdafcli-1.2.2.tar.gz -f ./ --no-index

```

*   Verify the installed `rdaf` CLI version
```
 rdaf --version 
 rdafk8s --version

```

### ****7.3 RDAF On-Premise Docker Registry Setup****

CloudFabrix support hosting an on-premise docker registry which will download and synchronize RDA Fabric's platform, infrastructure and application services from CloudFabrix's public docker registry that is securely hosted on AWS and from other public docker registries as well. For more information on on-premise docker registry, please refer **[Docker registry access for RDAF platform services](https://bot-docs.cloudfabrix.io/installation_guides/deployment/#2-docker-registry-access-for-rdaf-platform-services-deployment)
**.

**rdaf registry setup**

Run the below command to setup and configure on-premise docker registry service. In the below command example, 10.99.120.140 is the machine on which on-premise registry service is going to installed.

cfxregistry.cloudfabrix.io is the CloudFabrix's public docker registry hosted on AWS from which RDA Fabric docker images are going to be downloaded.


```
rdaf registry setup --docker-server-host 10.99.120.140 \     --docker-registry-source-host cfxregistry.cloudfabrix.io \     --docker-registry-source-port 443 \     --docker-registry-source-user readonly \     --docker-registry-source-password readonly
```

**rdaf registry install**

Run the below command to install the on-premise docker registry service.


```
rdaf registry install --tag 1.0.3
```

Info

*   For latest tag version, please contact support@cloudfabrix.com
*   On-premise docker registry service runs on port **TCP/5000**. This port may need to be enabled on firewall device if on-premise docker registry service and RDA Fabric service VMs are deployed in different network environments.

To check the status of the on-premise docker registry service, run the below command.


```
docker ps -a \| grep docker-registry
```

**rdaf registry fetch**

Once on-premise docker registry service is installed, run the below command to download one or more tags to pre-stage the docker images for RDA Fabric services deployment for fresh install.
```
 rdaf registry fetch --tag 1.0.3.2,3.4.2,7.4.2,1.0.3

```

**Minio** object storage service image need to be downloaded explicitly using the below command.
```
 rdaf registry fetch --minio-tag RELEASE.2023-09-30T07-02-29Z

```

Info

**Note:** It may take few minutes to few hours depends on the outbound internet access bandwidth and the number of docker images to be downloaded. The default location path for the downloaded docker images is **/opt/rdaf-registry/data/docker/registry**. This path can be overridden/changed during **rdaf registry setup** command using **\--install-root** option if needed.

**rdaf registry list-tags**

Run the below command to list the downloaded images and their corresponding tags / versions.


```
rdaf registry list-tags
```

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
 | `{ "tls": true,  "tlscacert": "/etc/tlscerts/ca/ca.pem",  "tlsverify": true,  "storage-driver": "overlay2",  "hosts": [   "unix:///var/run/docker.sock",    "tcp://0.0.0.0:2376" ],  "tlskey": "/etc/tlscerts/server/server.key",  "debug": false,  "tlscert": "/etc/tlscerts/server/server.pem",  "experimental": false,  "insecure-registries" : ["<on-premise-docker-registry-ip-or-dns>:5000"], "live-restore": true }` |


```
sudo systemctl daemon-reload
```


```
sudo systemctl restart docker
```


```
docker info
```

Example Output
```
 ... 
 ... 
 Kernel Version: 5.4.0-110-generic 
 Operating System: Ubuntu 20.04.4 LTS 
 OSType: linux 
 Architecture: x86_64 
 CPUs: 2 
 Total Memory: 7.741GiB 
 Name: rdaf-onprem-docker-repo 
 ID: OLZF:ZKWN:TIQJ:ZMNV:2STT:JHR3:3RAT:TAL5:TF47:OGVQ:LHY7:RMHH 
 Docker Root Dir: /var/lib/docker 
 Debug Mode: false 
 Registry: https://index.docker.io/v1/ 
 Labels: 
 Experimental: false 
 Insecure Registries: 
   10.99.120.140:5000 
   127.0.0.0/8 
 Live Restore Enabled: true

```

**rdafk8s setregistry**

When on-premise docker registry is deployed, set the default docker registry configuration to on-premise docker registry host to pull and install the RDA Fabric platform services.

*   Before proceeding, please copy the `/opt/rdaf-registry/cert/ca/ca.crt` file from on-premise registry VM.

`
```
 sudo mkdir -p /opt/rdaf-registry 
 sudo chown -R `id -u`:`id -g` /opt/rdaf-registry`
```
```
 scp rdauser@<on-premise-registry-ip>:/opt/rdaf-registry/cert/ca/ca.crt /opt/rdaf-registry/registry-ca-cert.crt

```

Tip

The location of the on-premise docker registry's CA certificate file `ca.crt` is located under **/opt/rdaf-registry/cert/ca**. This file `ca.crt` need to be copied to the machine on which **RDAF CLI** is used to **setup, configure and install RDA Fabric platform** and all of the required services using on-premise docker registry. This step is not applicable when cloud hosted docker registry **cfxregistry.cloudfabrix.io** is used. Also, this step is not needed, when on-premise docker registry service VM is used to setup, configure and deploy RDAF platform as well.

*   Run the below command to set the docker-registry to on-premise one.
```
 rdafk8s setregistry --host <on-premise-docker-registry-ip-or-dns> --port 5000 --cert-path /opt/rdaf-registry/registry-ca-cert.crt

```

Tip

Please verify if on-premise registry is accessible on port 5000 using either of the below commands.

*   **telnet `<on-premise-docker-registry-ip-or-dns>` 5000**
*   **curl -vv telnet://`<on-premise-docker-registry-ip-or-dns>`:5000**

**rdafk8s setup**

Run the below `rdafk8s setup` command to create the RDAF platform's deployment configuration. It is a pre-requisite before RDAF infrastructure, platform and application services can be installed on Kubernetes Cluser.

It will prompt for all the necessary configuration details.
```
 rdafk8s setup

```

*   Accept the EULA
```
 Do you accept the EULA? [yes/no]: yes

```

*   Enter the **rdauser** SSH password for all of the Kubernetes worker nodes on which RDAF services are going to be installed.
```
 What is the SSH password for the SSH user used to communicate between hosts 
 SSH password: 
 Re-enter SSH password:

```

Tip

Please make sure **rdauser's** SSH password on all of the Kubernetes cluster worker nodes is same during the `rdafk8s setup` command.

*   Enter additional IP address(es) or DNS names that can be as SANs (Subject alt names) while generating self-signed certificates. This is an optional configuration, but it is important to include any public facing IP addresse(s) that is/are different from worker node's ip addresses which are specified as part of the `rdafk8s setup` command.

Tip

SANs (Subject alt names) also known as **multi-domain certificates** which allows to create a single unified SSL certificate which includes more than one Common Name (CN). Common Name can be an IP Address or DNS Name or a wildcard DNS Name (ex: \*.acme.com)
```
 Provide any Subject alt name(s) to be used while generating SAN certs 
 Subject alt name(s) for certs[]: 100.30.10.10

```

*   Enter Kubernetes worker node IPs on which **RDAF Platform services** need to be installed. For HA configuration, please enter comma separated values. Minimum of 2 worker nodes are required for the HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's ip address or DNS name is required.
```
 What are the host(s) on which you want the RDAF platform services to be installed? 
 Platform service host(s)[rda-platform-vm01]: 192.168.125.141,192.168.125.142

```

*   Answer if the RDAF application services are going to be deployed in HA mode or standalone.
```
 Will application services be installed in HA mode? [yes/No]: yes

```

*   Enter Kubernetes worker node IPs on which **RDAF Application services (OIA/AIA)** need to be installed. For HA configuration, please enter comma separated values. Minimum of 2 hosts or more are required for the HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's ip address or DNS name is required.
```
 What are the host(s) on which you want the application services to be installed? 
 Application service host(s)[rda-platform-vm01]: 192.168.125.143,192.168.125.144

```

*   Enter the name of the Organization. In the below example, `ACME_IT_Services` is used as the Organization name. It is for a reference only.
```
 What is the organization you want to use for the admin user created? 
 Admin organization[CloudFabrix]: ACME_IT_Services

```

Press **Enter** to accept the defaults.
```
 What is the ca cert to use to communicate to on-prem docker registry 
 Docker Registry CA cert path[]:

```

*   Enter Kubernetes worker node IPs on which **RDAF Worker services** need to be installed. For HA configuration, please enter comma separated values. Minimum of 2 hosts or more are required for the HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's ip address or DNS name is required.
```
 What are the host(s) on which you want the Worker to be installed? 
 Worker host(s)[rda-platform-vm01]: 192.168.125.145

```

*   Enter Kubernetes worker node IPs on which **RDAF NATs** infrastructure service need to be installed. For HA configuration, please enter comma separated values. Minimum of 2 Kubernetes worker nodes are required for the `NATs` HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's IP or DNS Name is required.
```
 What is the "host/path-on-host" on which you want the Nats to be deployed? 
 Nats host/path[192.168.125.141]: 192.168.125.145,192.168.125.146

```

*   Enter Kubernetes worker node IPs on which **RDAF Minio** infrastructure service need to be installed. For HA configuration, please enter comma separated values. Minimum of 4 Kubernetes worker nodes are required for the `Minio` HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's IP or DNS Name is required.
```
 What is the "host/path-on-host" where you want Minio to be provisioned? 
 Minio server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147,192.168.125.148

```

*   Change the default `Minio` user credentials if needed or press **Enter** to accept the defaults.
```
 What is the user name you want to give for Minio root user that will be created and used by the RDAF platform? 
 Minio user[rdafadmin]:  
 What is the password you want to use for the newly created Minio root user? 
 Minio password[Q8aJ63PT]:

``` 

*   Enter Kubernetes worker node IPs on which **RDAF MariaDB** infrastructure service need to be installed. For HA configuration, please enter comma separated values. Minimum of 3 Kubernetes worker nodes are required for the `MariDB` database HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's IP or DNS Name is required.
```
 What is the "host/path-on-host" on which you want the MariaDB server to be provisioned? 
 MariaDB server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147

```

*   Change the default `MariaDB` user credentials if needed or press **Enter** to accept the defaults.
```
 What is the user name you want to give for MariaDB admin user that will be created and used by the RDAF platform? 
 MariaDB user[rdafadmin]:  
 What is the password you want to use for the newly created MariaDB root user? 
 MariaDB password[jffqjAaZ]:

``` 

*   Enter Kubernetes worker node IPs on which **RDAF Opensearch** infrastructure service need to be installed. For HA configuration, please enter comma separated values. Minimum of 3 Kubernetes worker nodes are required for the `Opensearch` HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's IP or DNS Name is required.
```
 What is the "host/path-on-host" on which you want the opensearch server to be provisioned? 
 opensearch server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147

```

*   Change the default `Opensearch` user credentials if needed or press **Enter** to accept the defaults.
```
 What is the user name you want to give for Opensearch admin user that will be created and used by the RDAF platform? 
 Opensearch user[rdafadmin]:  
 What is the password you want to use for the newly created Opensearch admin user? 
 Opensearch password[sLmr4ICX]:

``` 

*   Enter Kubernetes worker node IPs on which **RDAF Zookeeper** infrastructure service need to be installed. For HA configuration, please enter comma separated values. Minimum of 3 Kubernetes worker nodes are required for the `Zookeeper` HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's IP or DNS Name is required.
```
 What is the "host/path-on-host" on which you want the Zookeeper server to be provisioned? 
 Zookeeper server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147

```

*   Enter Kubernetes worker node IPs on which **RDAF Kafka** infrastructure service need to be installed. For HA configuration, please enter comma separated values. Minimum of 3 Kubernetes worker nodes are required for the `Kafka` HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's IP or DNS Name is required.
```
 What is the "host/path-on-host" on which you want the Kafka server to be provisioned? 
 Kafka server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147

```

*   Enter Kubernetes worker node IPs on which **RDAF Redis** infrastructure service need to be installed. For HA configuration, please enter comma separated values. Minimum of 3 Kubernetes worker nodes are required for the `Redis` HA configuration. If it is a non-HA deployment, only one Kubernetes worker node's IP or DNS Name is required.
```
 What is the "host/path-on-host" on which you want the Redis server to be provisioned? 
 Redis server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147

```

*   Enter RDAF infrastructure service `HAProxy` (load-balancer) host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts are required for the `HAProxy` HA configuration. If it is a non-HA deployment, only one RDAF `HAProxy` service host's ip address or DNS name is required.
```
 What is the host on which you want HAProxy to be provisioned? 
 HAProxy host[192.168.125.141]: 192.168.125.145,192.168.125.146

```

*   Select the network interface name which is used for UI portal access. Ex: `eth0` or `ens160` etc.
```
 What is the network interface on which you want the rdaf to be accessible externally? 
 Advertised external interface[eth0]: ens160

```

*   Enter the `HAProxy` service's virtual IP address when it is configured in HA configuration. Virtual IP address should be an unused IP address. This step is not applicable when `HAProxy` service is deployed in non-HA configuration.
```
 What is the host on which you want the platform to be externally accessible? 
 Advertised external host[192.168.125.143]: 192.168.125.149

```

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
 | `{ "tls": true,  "tlscacert": "/etc/tlscerts/ca/ca.pem",  "tlsverify": true,  "storage-driver": "overlay2",  "hosts": [   "unix:///var/run/docker.sock",    "tcp://0.0.0.0:2376" ],  "tlskey": "/etc/tlscerts/server/server.key",  "debug": false,  "tlscert": "/etc/tlscerts/server/server.pem",  "experimental": false,  "insecure-registries" : ["<on-premise-docker-registry-ip-or-dns>:5000"], "live-restore": true }` |


```
sudo systemctl daemon-reload
```


```
sudo systemctl restart docker
```


```
docker info
```

Example Output
```
 ... 
 ... 
 Kernel Version: 5.4.0-110-generic 
 Operating System: Ubuntu 20.04.4 LTS 
 OSType: linux 
 Architecture: x86_64 
 CPUs: 2 
 Total Memory: 7.741GiB 
 Name: rdaf-onprem-docker-repo 
 ID: OLZF:ZKWN:TIQJ:ZMNV:2STT:JHR3:3RAT:TAL5:TF47:OGVQ:LHY7:RMHH 
 Docker Root Dir: /var/lib/docker 
 Debug Mode: false 
 Registry: https://index.docker.io/v1/ 
 Labels: 
 Experimental: false 
 Insecure Registries: 
   10.99.120.140:5000 
   127.0.0.0/8 
 Live Restore Enabled: true

```

**rdaf setregistry**

When on-premise docker registry is deployed, set the default docker registry configuration to on-premise docker registry host to pull and install the RDA Fabric platform services.

*   Before proceeding, please copy the `/opt/rdaf-registry/cert/ca/ca.crt` file from on-premise registry VM.

`
```
 sudo mkdir -p /opt/rdaf-registry 
 sudo chown -R `id -u`:`id -g` /opt/rdaf-registry`
```
```
 scp rdauser@<on-premise-registry-ip>:/opt/rdaf-registry/cert/ca/ca.crt /opt/rdaf-registry/registry-ca-cert.crt

```

Tip

The location of the on-premise docker registry's CA certificate file `ca.crt` is located under **/opt/rdaf-registry/cert/ca**. This file `ca.crt` need to be copied to the machine on which **RDAF CLI** is used to **setup, configure and install RDA Fabric platform** and all of the required services using on-premise docker registry. This step is not applicable when cloud hosted docker registry **cfxregistry.cloudfabrix.io** is used. Also, this step is not needed, when on-premise docker registry service VM is used to setup, configure and deploy RDAF platform as well.

*   Run the below command to set the docker-registry to on-premise one.
```
 rdaf setregistry --host <on-premise-docker-registry-ip-or-dns> --port 5000 --cert-path /opt/rdaf-registry/registry-ca-cert.crt

```

Tip

Please verify if on-premise registry is accessible on port 5000 using either of the below commands.

*   **telnet `<on-premise-docker-registry-ip-or-dns>` 5000**
*   **curl -vv telnet://`<on-premise-docker-registry-ip-or-dns>`:5000**

**rdaf setup**

Run the below `rdaf setup` command to create the RDAF platform's deployment configuration. It is a pre-requisite before RDAF infrastructure, platform and application services can be installed.

It will prompt for all the necessary configuration details.
```
 rdaf setup

```

*   Accept the EULA
```
 Do you accept the EULA? [yes/no]: yes

```

*   Enter the **rdauser** SSH password for all of the RDAF hosts.
```
 What is the SSH password for the SSH user used to communicate between hosts 
 SSH password: 
 Re-enter SSH password:

```

Tip

Please make sure **rdauser's** SSH password on all of the RDAF hosts is same during the `rdaf setup` command.

Press **Enter** to accept the defaults.
```
 Provide any Subject alt name(s) to be used while generating SAN certs 
 Subject alt name(s) for certs[]:

```

*   Enter RDAF Platform host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts are required for the HA configuration. If it is a non-HA deployment, only one RDAF platform host's ip address or DNS name is required.
```
 What are the host(s) on which you want the RDAF platform services to be installed? 
 Platform service host(s)[rda-platform-vm01]: 192.168.125.141,192.168.125.142

```

*   Answer if the RDAF application services are going to be deployed in HA mode or standalone.
```
 Will application services be installed in HA mode? [yes/No]: yes

```

*   Enter RDAF Application services host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts or more are required for the HA configuration. If it is a non-HA deployment, only one RDAF application service host's ip address or DNS name is required.
```
 What are the host(s) on which you want the application services to be installed? 
 Application service host(s)[rda-platform-vm01]: 192.168.125.143,192.168.125.144

```

*   Enter the name of the Organization. In the below example, `ACME_IT_Services` is used as the Organization name. It is for a reference only.
```
 What is the organization you want to use for the admin user created? 
 Admin organization[CloudFabrix]: ACME_IT_Services

```

Press **Enter** to accept the defaults.
```
 What is the ca cert to use to communicate to on-prem docker registry 
 Docker Registry CA cert path[]:

```

*   Enter RDAF Worker service host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts or more are required for the HA configuration. If it is a non-HA deployment, only one RDAF worker service host's ip address or DNS name is required.
```
 What are the host(s) on which you want the Worker to be installed? 
 Worker host(s)[rda-platform-vm01]: 192.168.125.145

```

*   Enter ip address on which RDAF Event Gateway needs to be Installed, For HA configuration please enter comma separated values. Minimum of 2 hosts or more are required for the HA configuration. If it is a non-HA deployment, only one RDAF Event Gateway host's ip address or DNS name is required.
```
 What are the host(s) on which you want the Event Gateway to be installed? 
 Event Gateway host(s)[rda-platform-vm01]: 192.168.125.67

```

*   Enter RDAF infrastructure service `NATs` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts are required for the `NATs` HA configuration. If it is a non-HA deployment, only one RDAF `NATs` service host's ip address or DNS name is required.
```
 What is the "host/path-on-host" on which you want the Nats to be deployed? 
 Nats host/path[192.168.125.141]: 192.168.125.145,192.168.125.146

```

*   Enter RDAF infrastructure service `Minio` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 4 hosts are required for the `Minio` HA configuration. If it is a non-HA deployment, only one RDAF `Minio` service host's ip address or DNS name is required.
```
 What is the "host/path-on-host" where you want Minio to be provisioned? 
 Minio server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147,192.168.125.148

```

*   Change the default `Minio` user credentials if needed or press **Enter** to accept the defaults.
```
 What is the user name you want to give for Minio root user that will be created and used by the RDAF platform? 
 Minio user[rdafadmin]:  
 What is the password you want to use for the newly created Minio root user? 
 Minio password[Q8aJ63PT]:

``` 

*   Enter RDAF infrastructure service `MariDB` database host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `MariDB` database HA configuration. If it is a non-HA deployment, only one RDAF `MariaDB` service host's ip address or DNS name is required.
```
 What is the "host/path-on-host" on which you want the MariaDB server to be provisioned? 
 MariaDB server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147

```

*   Change the default `MariaDB` user credentials if needed or press **Enter** to accept the defaults.
```
 What is the user name you want to give for MariaDB admin user that will be created and used by the RDAF platform? 
 MariaDB user[rdafadmin]:  
 What is the password you want to use for the newly created MariaDB root user? 
 MariaDB password[jffqjAaZ]:

``` 

*   Enter RDAF infrastructure service `Opensearch` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `Opensearch` HA configuration. If it is a non-HA deployment, only one RDAF `Opensearch` service host's ip address or DNS name is required.
```
 What is the "host/path-on-host" on which you want the opensearch server to be provisioned? 
 opensearch server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147

```

*   Change the default `Opensearch` user credentials if needed or press **Enter** to accept the defaults.
```
 What is the user name you want to give for Opensearch admin user that will be created and used by the RDAF platform? 
 Opensearch user[rdafadmin]:  
 What is the password you want to use for the newly created Opensearch admin user? 
 Opensearch password[sLmr4ICX]:

``` 

*   Enter RDAF infrastructure service `Zookeeper` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `Zookeeper` HA configuration. If it is a non-HA deployment, only one RDAF `Zookeeper` service host's ip address or DNS name is required.
```
 What is the "host/path-on-host" on which you want the Zookeeper server to be provisioned? 
 Zookeeper server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147

```

*   Enter RDAF infrastructure service `Kafka` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `Kafka` HA configuration. If it is a non-HA deployment, only one RDAF `Kafka` service host's ip address or DNS name is required.
```
 What is the "host/path-on-host" on which you want the Kafka server to be provisioned? 
 Kafka server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147

```

*   Enter RDAF infrastructure service `Redis` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `Redis` HA configuration. If it is a non-HA deployment, only one RDAF `Redis` service host's ip address or DNS name is required.
```
 What is the "host/path-on-host" on which you want the Redis server to be provisioned? 
 Redis server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147

```

*   Enter RDAF infrastructure service `GraphDB` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `GraphDB` HA configuration. If it is a non-HA deployment, only one RDAF `GraphDB` service host's ip address or DNS name is required.
```
 What is the "host/path-on-host" on which you want the GraphDB to be deployed? 
 GraphDB host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147

```

*   Enter RDAF infrastructure service `HAProxy` (load-balancer) host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts are required for the `HAProxy` HA configuration. If it is a non-HA deployment, only one RDAF `HAProxy` service host's ip address or DNS name is required.
```
 What is the host on which you want HAProxy to be provisioned? 
 HAProxy host[192.168.125.141]: 192.168.125.145,192.168.125.146

```

*   Select the network interface name which is used for UI portal access. Ex: `eth0` or `ens160` etc.
```
 What is the network interface on which you want the rdaf to be accessible externally? 
 Advertised external interface[eth0]: ens160

```

*   Enter the `HAProxy` service's virtual IP address when it is configured in HA configuration. Virtual IP address should be an unused IP address. This step is not applicable when `HAProxy` service is deployed in non-HA configuration.
```
 What is the host on which you want the platform to be externally accessible? 
 Advertised external host[192.168.125.143]: 192.168.125.149

```

*   Enter the ip address of the Internal accessible advertised host
```
 Do you want to specify an internal advertised host? [yes/No]: No

```

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
```
 rdafk8s infra install --tag 1.0.3

```

Run the below command to install a specific RDAF infrastructure service. Below are the supported infrastructure services.

*   haproxy
*   nats
*   mariadb
*   opensearch
*   kafka
*   redis
*   graphdb

Run the below command to upgrade the **haproxy** service.
```
 rdafk8s infra upgrade --service haproxy --tag 1.0.3.2

```

**1.5.1 Status check**

Run the below command to see the status of all of the deployed RDAF infrastructure services.
```
 rdafk8s infra status

```

Example Output
```
 +-----------------------+----------------+----------------+--------------+------------------------------+ 
 | Name                  | Host           | Status         | Container Id | Tag                          | 
 +-----------------------+----------------+----------------+--------------+------------------------------+ 
 | haproxy               | 192.168.108.31 | Up 3 hours     | 217fe8852f2d | 1.0.3.2                      | 
 | rda-nats              | 192.168.108.31 | Up 3 Hours ago | 58cf96d50a3c | 1.0.3                        | 
 | rda-minio             | 192.168.108.31 | Up 3 Hours ago | 6704c211e803 | RELEASE.2023-09-30T07-02-29Z | 
 | rda-mariadb           | 192.168.108.31 | Up 3 Hours ago | d83f0e0e3c0c | 1.0.3                        | 
 | rda-opensearch        | 192.168.108.31 | Up 3 Hours ago | f36fd18bc397 | 1.0.3                        | 
 | rda-kafka-controller  | 192.168.108.31 | Up 3 Hours ago | 0bb0d3e6580a | 1.0.3                        | 
 | rda-redis-master      | 192.168.108.31 | Up 3 Hours ago | 1afcc9a825d4 | 1.0.3                        | 
 | rda-redis-replica     | 192.168.108.31 | Up 3 Hours ago | b797195153de | 1.0.3                        | 
 | rda-graphdb[operator] | 192.168.108.31 | Up 3 Hours ago | 2491c9e12c53 | 1.0.3                        | 
 | rda-graphdb[server]   | 192.168.108.31 | Up 3 Hours ago | 98a139960fbd | 1.0.3                        | 
 +-----------------------+----------------+----------------+--------------+------------------------------+

```

Below are the Kubernetes Cluster `kubectl get pods` commands to check the status of RDA Fabric infrastructure services.
```
 kubectl get pods -n rda-fabric -l app_category=rdaf-infra

```

Example Output
```
 NAME                            READY   STATUS    RESTARTS        AGE 
 opensearch-cluster-master-0     1/1     Running   0               7m12s 
 rda-kafka-0                     1/1     Running   2 (5m26s ago)   7m10s 
 rda-kafka-zookeeper-0           1/1     Running   0               7m10s 
 rda-mariadb-mariadb-galera-0    1/1     Running   0               8m8s 
 rda-minio-65f755bb5f-9tjdm      1/1     Running   0               8m25s 
 rda-nats-0                      3/3     Running   0               8m57s 
 rda-nats-box-7b7b46969b-79lnf   1/1     Running   0               8m57s 
 rda-redis-master-0              1/1     Running   0               7m9s 
 rda-redis-replicas-0            1/1     Running   0               7m9s

```

Below `kubectl get pods` command provides additional details of deployed RDAF Infrastructure services (PODs) along with their worker node(s) on which they were deployed.
```
 kubectl get pods -n rda-fabric -o wide -l app_category=rdaf-infra

```

In order to get detailed status of the each RDAF Infrastructure service POD, run the below `kubectl describe pod` command.
```
 kubectl describe pod rda-nats-0 -n rda-fabric

```

Example Output
```
 Name:         rda-nats-0 
 Namespace:    rda-fabric 
 Priority:     0 
 Node:         k8rdapfm01/192.168.125.45 
 Start Time:   Sun, 12 Feb 2023 00:36:39 +0000 
 Labels:       app=rda-fabric-services 
                 app_category=rdaf-infra 
                 app_component=rda-nats 
                 controller-revision-hash=rda-nats-64747cd755 
 ... 
 ... 
 Events: 
 Type    Reason     Age   From               Message 
 ----    ------     ----  ----               ------- 
 Normal  Scheduled  10m   default-scheduler  Successfully assigned rda-fabric/rda-nats-0 to k8rdapfm01 
 Normal  Pulling    10m   kubelet            Pulling image "192.168.125.140:5000/rda-platform-nats:1.0.2" 
 Normal  Pulled     10m   kubelet            Successfully pulled image "192.168.125.140:5000/rda-platform-nats:1.0.2" in 3.102792187s 
 Normal  Created    10m   kubelet            Created container nats

```

Note

Below steps are applicable only if RDAF Application (OIA/AIA) services are going to be installed.

*   Run the below command to update the necessary HAProxy load-balancer configuration for RDAF **OIA** / **AIA** application services.
```
 rdafk8s app update-config OIA

```
```
 rdafk8s app update-config AIA

```

After deploying the RDAF OIA application services, it is mandatory to run the `rdaf app update-config` which will apply and restart the HAProxy load-balancer service automatically.

`rdaf infra install` command is used to deploy / install RDAF infrastructure services.

Run the below command to deploy all RDAF infrastructure services.
```
 rdaf infra install --tag 1.0.3

```

It deploys the below RDAF Infrastructure services.

*   haproxy
*   nats
*   mariadb
*   opensearch
*   kafka
*   redis
*   graphdb

Run the below command to upgrade the **haproxy** service.
```
 rdaf infra upgrade --service haproxy --tag 1.0.3.2

```

**1.5.1 Status check**

Run the below command to see the status of all of the deployed RDAF infrastructure services.
```
 rdaf infra status

```

Example Output
```
 +-----------------------+--------------+----------------+--------------+------------------------------+ 
 | Name                  | Host         | Status         | Container Id | Tag                          | 
 +-----------------------+--------------+----------------+--------------+------------------------------+ 
 | haproxy               | 192.168.108.31 | Up 3 hours     | 217fe8852f2d | 1.0.3.2                      | 
 | rda-nats              | 192.168.108.31 | Up 3 Hours ago | 58cf96d50a3c | 1.0.3                        | 
 | rda-minio             | 192.168.108.31 | Up 3 Hours ago | 6704c211e803 | RELEASE.2023-09-30T07-02-29Z | 
 | rda-mariadb           | 192.168.108.31 | Up 3 Hours ago | d83f0e0e3c0c | 1.0.3                        | 
 | rda-opensearch        | 192.168.108.31 | Up 3 Hours ago | f36fd18bc397 | 1.0.3                        | 
 | rda-kafka-controller  | 192.168.108.31 | Up 3 Hours ago | 0bb0d3e6580a | 1.0.3                        | 
 | rda-redis-master      | 192.168.108.31 | Up 3 Hours ago | 1afcc9a825d4 | 1.0.3                        | 
 | rda-redis-replica     | 192.168.108.31 | Up 3 Hours ago | b797195153de | 1.0.3                        | 
 | rda-graphdb[operator] | 192.168.108.31 | Up 3 Hours ago | 2491c9e12c53 | 1.0.3                        | 
 | rda-graphdb[server]   | 192.168.108.31 | Up 3 Hours ago | 98a139960fbd | 1.0.3                        | 
 +-----------------------+--------------+----------------+--------------+------------------------------+

```

**Check Infra services liveness / health status**

Run the below command to verify RDAF infrastructure service's liveness / health status. This command helps to quickly identify any infrastructure service's availability or accessibility issues.
```
 rdaf infra healthcheck

```

Example Output
```
 +----------------+-----------------+--------+------------------------------+----------------+--------------+ 
 | Name           | Check           | Status | Reason                       | Host           | Container Id | 
 +----------------+-----------------+--------+------------------------------+----------------+--------------+ 
 | haproxy        | Port Connection | OK     | N/A                          | 192.168.107.63 | a78256a09ee6 | 
 | haproxy        | Service Status  | OK     | N/A                          | 192.168.107.63 | a78256a09ee6 | 
 | haproxy        | Firewall Port   | OK     | N/A                          | 192.168.107.63 | a78256a09ee6 | 
 | haproxy        | Port Connection | OK     | N/A                          | 192.168.107.64 | 968fe5c56865 | 
 | haproxy        | Service Status  | OK     | N/A                          | 192.168.107.64 | 968fe5c56865 | 
 | haproxy        | Firewall Port   | OK     | N/A                          | 192.168.107.64 | 968fe5c56865 | 
 | keepalived     | Service Status  | OK     | N/A                          | 192.168.107.63 | N/A          | 
 | keepalived     | Service Status  | OK     | N/A                          | 192.168.107.64 | N/A          | 
 | nats           | Port Connection | OK     | N/A                          | 192.168.107.63 | ca708ba9a4ae | 
 | nats           | Service Status  | OK     | N/A                          | 192.168.107.63 | ca708ba9a4ae | 
 | nats           | Firewall Port   | OK     | N/A                          | 192.168.107.63 | ca708ba9a4ae | 
 +----------------+-----------------+--------+------------------------------+----------------+--------------+

```

Note

Below steps are applicable only if RDAF Application (OIA/AIA) services are going to be installed.

*   Run the below command to update the necessary HAProxy load-balancer configuration for RDAF **OIA** / **AIA** application services.
```
 rdaf app update-config OIA

```
```
 rdaf app update-config AIA

```

After deploying the RDAF OIA application services, it is mandatory to run the `rdaf app update-config` which will apply and restart the HAProxy load-balancer service automatically.

### ****7.6 RDAF Platform Services Installation****

KubernetesNon-Kubernetes

`rdafk8s platform install` command is used to deploy / install RDAF core platform services.

Run the below command to deploy all RDAF core platform services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com)
```
 rdafk8s platform install --tag 3.4.2

```

As part of the installation of RDAF core platform services, it creates a default tenant admin user called `admin@cfx.com`

The default password for `admin@cfx.com` is **admin1234**

On first login onto RDAF UI portal, it prompts for resetting the above default password to user's choice.

In order to access RDAF UI portal, open a web browser and type the HAProxy server's IP address if it is a non-HA deployment or HAProxy server's virtual IP address if it is an HA deployment as shown below.
```
 https://192.168.125.148

```

**Status check**

Run the below command to see the status of all of the deployed RDAF core platform services.
```
 rdafk8s platform status

```

Example Output
```
 +---------------------+----------------+---------------+----------------+-------+ 
 | Name                | Host           | Status        | Container Id   | Tag   | 
 +---------------------+----------------+---------------+----------------+-------+ 
 | rda-api-server      | 192.168.131.46 | Up 1 Days ago | faf4cdd79dd4   | 3.4.2 | 
 | rda-api-server      | 192.168.131.44 | Up 1 Days ago | 409c81c1000d   | 3.4.2 | 
 | rda-registry        | 192.168.131.46 | Up 1 Days ago | fa2682e9f7bb   | 3.4.2 | 
 | rda-registry        | 192.168.131.45 | Up 1 Days ago | 91eca9476848   | 3.4.2 | 
 | rda-identity        | 192.168.131.46 | Up 1 Days ago | 4e5e337eabe7   | 3.4.2 | 
 | rda-identity        | 192.168.131.44 | Up 1 Days ago | b10571cfa217   | 3.4.2 | 
 | rda-fsm             | 192.168.131.44 | Up 1 Days ago | 1cea17b4d5e0   | 3.4.2 | 
 | rda-fsm             | 192.168.131.46 | Up 1 Days ago | ac34fce6b2aa   | 3.4.2 | 
 | rda-chat-helper     | 192.168.131.45 | Up 1 Days ago | ea083e20a082   | 3.4.2 | 
 +---------------------+---------------+---------------+----------------+--------+

```

Below are the Kubernetes Cluster `kubectl` commands to check the status of RDA Fabric core platform services.
```
 kubectl get pods -n rda-fabric -l app_category=rdaf-platform

```

Example Output
```
 NAME                                    READY   STATUS    RESTARTS   AGE 
 rda-access-manager-668d68bb67-tks95     1/1     Running   0          11d 
 rda-api-server-b6c888bdd-nv4jm          1/1     Running   0          11d 
 rda-asset-dependency-7969f7b657-cmx24   1/1     Running   0          11d 
 rda-collector-6bd6c79475-52hvg          1/1     Running   0          11d 
 rda-identity-679864f487-74xtd           1/1     Running   0          11d 
 rda-portal-59dbd8cc6d-b2sfn             2/2     Running   0          11d 
 rda-registry-7767f58949-jw6s8           1/1     Running   0          11d 
 rda-resource-manager-84c9995887-bmzw4   1/1     Running   0          11d 
 rda-scheduler-5b87b9798f-fxztt          1/1     Running   0          11d 
 rda-user-preferences-7469dfb75d-b4l5r   1/1     Running   0          11d

```

Below `kubectl get pods` command provides additional details of deployed RDAF core platform services (PODs) along with their worker node(s) on which they were deployed.
```
 kubectl get pods -n rda-fabric -o wide -l app_category=rdaf-platform

```

In order to get detailed status of the each RDAF core platform service POD, run the below `kubectl describe pod` command.
```
 kubectl describe pod rda-collector-6bd6c79475-52hvg  -n rda-fabric

```

Example Output
```
 Name:         rda-collector-6bd6c79475-52hvg 
 Namespace:    rda-fabric 
 Priority:     0 
 Node:         hari-k8-cluster-infra10819/192.168.108.19 
 Start Time:   Tue, 31 Jan 2023 05:00:57 +0000 
 Labels:       app=rda-fabric-services 
                 app_category=rdaf-platform 
                 app_component=rda-collector 
                 pod-template-hash=6bd6c79475 
 ... 
 ... 
 QoS Class:                   Burstable 
 Node-Selectors:              rdaf_platform_services=allow 
 Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s 
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s 
                             pod-type=rda-tenant:NoSchedule 
 Events:                      <none>

```

`rdaf platform install` command is used to deploy / install RDAF core platform services.

Run the below command to deploy all RDAF core platform services.
```
 rdaf platform install --tag 3.4.2

```

As part of the installation of RDAF core platform services, it creates a default tenant admin user called `admin@cfx.com`

The default password for `admin@cfx.com` is **admin1234**

On first login onto RDAF UI portal, it prompts for resetting the above default password to user's choice.

In order to access RDAF UI portal, open a web browser and type the HAProxy server's IP address if it is a non-HA deployment or HAProxy server's virtual IP address if it is an HA deployment as shown below.
```
 https://192.168.125.148

```

**Status check**

Run the below command to see the status of all of the deployed RDAF infrastructure services.
```
 rdaf platform status

```

Example Output
```
 +--------------------------+----------------+------------+--------------+-------+ 
 | Name                     | Host           | Status     | Container Id | Tag   | 
 +--------------------------+----------------+------------+--------------+-------+ 
 | rda_api_server           | 192.168.107.61 | Up 5 hours | 6fc70d6b82aa | 3.4.2 | 
 | rda_api_server           | 192.168.107.62 | Up 5 hours | afa31a2c614b | 3.4.2 | 
 | rda_registry             | 192.168.107.61 | Up 5 hours | 9f8adbb08b95 | 3.4.2 | 
 | rda_registry             | 192.168.107.62 | Up 5 hours | cc8e5d27eb0a | 3.4.2 | 
 | rda_scheduler            | 192.168.107.61 | Up 5 hours | f501e240e7a3 | 3.4.2 | 
 | rda_scheduler            | 192.168.107.62 | Up 5 hours | c5b2b258efe1 | 3.4.2 | 
 | rda_collector            | 192.168.107.61 | Up 5 hours | 2260fc37ebe5 | 3.4.2 | 
 | rda_collector            | 192.168.107.62 | Up 5 hours | 3e7ab4518394 | 3.4.2 | 
 +--------------------------+----------------+------------+--------------+-------+

```

### ****7.7 RDAF Client (rdac) CLI Installation****

KubernetesNon-Kubernetes

`rdafk8s rdac_cli` command allows you to install RDA client CLI utility which interacts with RDA Fabric services and operations.

*   To install RDA client CLI, run the below command
```
 rdafk8s rdac_cli install --tag 3.4.2

```

*   Run the below command to see RDA client CLI help and available subcommand options.
```
 rdac -h

```

Example Output
```
 Run with one of the following commands 
 
     agent-bots                List all bots registered by agents for the current tenant 
     agents                    List all agents for the current tenant 
     alert-rules               Alert Rule management commands 
     bot-catalog-generation-from-file  Generate bot catalog for given sources 
     bot-package               Bot Package management commands 
     bots-by-source            List bots available for given sources 
     check-credentials         Perform credential check for one or more sources on a worker pod 
     checksum                  Compute checksums for pipeline contents locally for a given JSON file 
     compare                   Commands to compare different RDA systems using different RDA Config files 
     content-to-object         Convert data from a column into objects 
     copy-to-objstore          Deploy files specified in a ZIP file to the Object Store 
     dashboard                 User defined dashboard management commands 
     dashgroup                 User defined dashboard-group management commands 
     dataset                   Dataset management commands 
     demo                      Demo related commands 
     deployment                Service Blueprints (Deployments) management commands 
     event-gw-status           List status of all ingestion endpoints at all the event gateways 
     evict                     Evict a job from a worker pod 
     file-ops                  Perform various operations on local files 
     file-to-object            Convert files from a column into objects 
     fmt-template              Formatting Templates management commands 
     healthcheck               Perform healthcheck on each of the Pods 
     invoke-agent-bot          Invoke a bot published by an agent 
     jobs                      List all jobs for the current tenant 
     logarchive                Logarchive management commands 
     object                    RDA Object management commands 
     output                    Get the output of a Job using jobid. 
     pipeline                  Pipeline management commands 
     playground                Start Webserver to access RDA Playground 
     pods                      List all pods for the current tenant 
     project                   Project management commands. Projects can be used to link different tenants / projects from this RDA Fabric or a remote RDA Fabric. 
     pstream                   Persistent Stream management commands 
     purge-outputs             Purge outputs of completed jobs 
     read-stream               Read messages from an RDA stream 
     reco-engine               Recommendation Engine management commands 
     restore                   Commands to restore backed-up artifacts to an RDA Platform 
     run                       Run a pipeline on a worker pod 
     run-get-output            Run a pipeline on a worker, and Optionally, wait for the completion, get the final output 
     schedule                  Pipeline execution schedule management commands 
     schema                    Dataset Model Schema management commands 
     secret                    Credentials (Secrets) management commands 
     set-pod-log-level         Update the logging level for a given RDA Pod. 
     shell                     Start RDA Client interactive shell 
     site-profile              Site Profile management commands 
     site-summary              Show summary by Site and Overall 
     stack                     Application Dependency Mapping (Stack) management commands 
     staging-area              Staging Area based data ingestion management commands 
     subscription              Show current CloudFabrix RDA subscription details 
     synthetics                Data synthesizing management commands 
     verify-pipeline           Verify the pipeline on a worker pod 
     viz                       Visualize data from a file within the console (terminal) 
     watch                     Commands to watch various streams such sas trace, logs and change notifications by microservices 
     web-server                Start Webserver to access RDA Client data using REST APIs 
     worker-obj-info           List all worker pods with their current Object Store configuration 
     write-stream              Write data to the specified stream 
 
 positional arguments: 
     command     RDA subcommand to run 
 
 optional arguments: 
     -h, --help  show this help message and exit

```

Tip

Please refer [RDA Client CLI Usage](https://bot-docs.cloudfabrix.io/beginners_guide/rdac/#3-list-of-all-rda-cli-sub-commands)
 for detailed information.

*   Set RDA Fabric platform's application configuration as `rda` using the below command.
```
 rdac rda-app-configure --type rda

```

Note

Other supported options for above command are below:

*   `rda`: Choose this option when **only RDA Fabric platform** need to be installed along with RDA Worker and RDA Event Gateway services without OIA (AIOps) application services.
    
*   `aiops`: Choose this option when **Operations Intelligence (OIA, a.k.a AIOps)** application need to be installed.
    
*   `asset`: Choose this option when **Asset Intelligence (AIA)** application need to be installed. (**Note:** AIA application type is deprecated and all of it's capabilities are available through base RDA Fabric platform itself. For more information, please contact cfx-support@cloudfabric.com)
    
*   `all`: Choose this option, when all of the supported applications need to be installed.
    

*   Please restart the RDAF Platform services using the below command.
```
 rdafk8s platform down --force

```
```
 rdafk8s platform up

```

*   Run the below `rdac healthcheck` command to check the health status of all of the **RDAF core platform services**.

All of the dependency checks should show as **ok** under **Status** column.
```
 rdac healthcheck

```

Example Output
```
 +-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-------------------------------------------------------+ 
 | Cat       | Pod-Type                               | Host         | ID       | Site        | Health Parameter                                    | Status   | Message                                               | 
 |-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-------------------------------------------------------| 
 | rda_infra | api-server                             | rda-api-serv | b1b910d9 |             | service-status                                      | ok       |                                                       | 
 | rda_infra | api-server                             | rda-api-serv | b1b910d9 |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_app   | asset-dependency                       | rda-asset-de | 090669bf |             | service-status                                      | ok       |                                                       | 
 | rda_app   | asset-dependency                       | rda-asset-de | 090669bf |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_app   | authenticator                          | rda-identity | 57905b20 |             | service-status                                      | ok       |                                                       | 
 | rda_app   | authenticator                          | rda-identity | 57905b20 |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_app   | authenticator                          | rda-identity | 57905b20 |             | DB-connectivity                                     | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | service-status                                      | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | service-dependency:registry                         | ok       | 1 pod(s) found for registry                           | 
 | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | service-initialization-status                       | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | DB-connectivity                                     | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | service-status                                      | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | service-initialization-status                       | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | DB-connectivity                                     | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-status                                      | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-dependency:registry                         | ok       | 1 pod(s) found for registry                           | 
 | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-dependency:cfxdimensions-app-access-manager | ok       | 1 pod(s) found for cfxdimensions-app-access-manager   | 
 | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-initialization-status                       | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | DB-connectivity                                     | ok       |                                                       | 
 | rda_infra | collector                              | rda-collecto | 99553e51 |             | service-status                                      | ok       |                                                       | 
 | rda_infra | collector                              | rda-collecto | 99553e51 |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_infra | collector                              | rda-collecto | 99553e51 |             | opensearch-connectivity:default                     | ok       |                                                       | 
 | rda_infra | registry                               | rda-registry | a46cd712 |             | service-status                                      | ok       |                                                       | 
 | rda_infra | registry                               | rda-registry | a46cd712 |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_infra | scheduler                              | rda-schedule | d5537051 |             | service-status                                      | ok       |                                                       | 
 | rda_infra | scheduler                              | rda-schedule | d5537051 |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_infra | scheduler                              | rda-schedule | d5537051 |             | DB-connectivity                                     | ok       |                                                       | 
 | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | service-status                                      | ok       |                                                       | 
 | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | service-dependency:registry                         | ok       | 1 pod(s) found for registry                           | 
 | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | service-initialization-status                       | ok       |                                                       | 
 | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | DB-connectivity                                     | ok       |                                                       | 
 +-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-------------------------------------------------------+

```

`rdaf rdac_cli` command allows you to install RDA client CLI utility which interacts with RDA Fabric services and operations.

*   To install RDA client CLI, run the below command
```
 rdaf rdac_cli install --tag 3.4.2

```

*   Run the below command to see RDA client CLI help and available subcommand options.
```
 rdac -h

```

Example Output
```
 Run with one of the following commands 
 
     agent-bots                List all bots registered by agents for the current tenant 
     agents                    List all agents for the current tenant 
     alert-rules               Alert Rule management commands 
     bot-catalog-generation-from-file  Generate bot catalog for given sources 
     bot-package               Bot Package management commands 
     bots-by-source            List bots available for given sources 
     check-credentials         Perform credential check for one or more sources on a worker pod 
     checksum                  Compute checksums for pipeline contents locally for a given JSON file 
     compare                   Commands to compare different RDA systems using different RDA Config files 
     content-to-object         Convert data from a column into objects 
     copy-to-objstore          Deploy files specified in a ZIP file to the Object Store 
     dashboard                 User defined dashboard management commands 
     dashgroup                 User defined dashboard-group management commands 
     dataset                   Dataset management commands 
     demo                      Demo related commands 
     deployment                Service Blueprints (Deployments) management commands 
     event-gw-status           List status of all ingestion endpoints at all the event gateways 
     evict                     Evict a job from a worker pod 
     file-ops                  Perform various operations on local files 
     file-to-object            Convert files from a column into objects 
     fmt-template              Formatting Templates management commands 
     healthcheck               Perform healthcheck on each of the Pods 
     invoke-agent-bot          Invoke a bot published by an agent 
     jobs                      List all jobs for the current tenant 
     logarchive                Logarchive management commands 
     object                    RDA Object management commands 
     output                    Get the output of a Job using jobid. 
     pipeline                  Pipeline management commands 
     playground                Start Webserver to access RDA Playground 
     pods                      List all pods for the current tenant 
     project                   Project management commands. Projects can be used to link different tenants / projects from this RDA Fabric or a remote RDA Fabric. 
     pstream                   Persistent Stream management commands 
     purge-outputs             Purge outputs of completed jobs 
     read-stream               Read messages from an RDA stream 
     reco-engine               Recommendation Engine management commands 
     restore                   Commands to restore backed-up artifacts to an RDA Platform 
     run                       Run a pipeline on a worker pod 
     run-get-output            Run a pipeline on a worker, and Optionally, wait for the completion, get the final output 
     schedule                  Pipeline execution schedule management commands 
     schema                    Dataset Model Schema management commands 
     secret                    Credentials (Secrets) management commands 
     set-pod-log-level         Update the logging level for a given RDA Pod. 
     shell                     Start RDA Client interactive shell 
     site-profile              Site Profile management commands 
     site-summary              Show summary by Site and Overall 
     stack                     Application Dependency Mapping (Stack) management commands 
     staging-area              Staging Area based data ingestion management commands 
     subscription              Show current CloudFabrix RDA subscription details 
     synthetics                Data synthesizing management commands 
     verify-pipeline           Verify the pipeline on a worker pod 
     viz                       Visualize data from a file within the console (terminal) 
     watch                     Commands to watch various streams such sas trace, logs and change notifications by microservices 
     web-server                Start Webserver to access RDA Client data using REST APIs 
     worker-obj-info           List all worker pods with their current Object Store configuration 
     write-stream              Write data to the specified stream 
 
 positional arguments: 
     command     RDA subcommand to run 
 
 optional arguments: 
     -h, --help  show this help message and exit

```

Tip

Please refer [RDA Client CLI Usage](https://bot-docs.cloudfabrix.io/beginners_guide/rdac/#3-list-of-all-rda-cli-sub-commands)
 for detailed information.

*   Set RDA Fabric platform's application configuration as `rda` using the below command.
```
 rdac rda-app-configure --type rda

```

Note

Other supported options for above command are below:

*   `rda`: Choose this option when **only RDA Fabric platform** need to be installed along with RDA Worker and RDA Event Gateway services without OIA (AIOps) application services.
    
*   `aiops`: Choose this option when **Operations Intelligence (OIA, a.k.a AIOps)** application need to be installed.
    
*   `asset`: Choose this option when **Asset Intelligence (AIA)** application need to be installed. (**Note:** AIA application type is deprecated and all of it's capabilities are available through base RDA Fabric platform itself. For more information, please contact cfx-support@cloudfabric.com)
    
*   `all`: Choose this option, when all of the supported applications need to be installed.
    

*   Please restart the RDAF Platform services using the below command.
```
 rdaf platform down

```
```
 rdaf platform up

```

*   Run the below `rdac healthcheck` command to check the health status of all of the **RDAF core platform services**.

All of the dependency checks should show as **ok** under **Status** column.
```
 rdac healthcheck

```

Example Output
```
 +-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-------------------------------------------------------+ 
 | Cat       | Pod-Type                               | Host         | ID       | Site        | Health Parameter                                    | Status   | Message                                               | 
 |-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-------------------------------------------------------| 
 | rda_infra | api-server                             | rda-api-serv | b1b910d9 |             | service-status                                      | ok       |                                                       | 
 | rda_infra | api-server                             | rda-api-serv | b1b910d9 |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_app   | asset-dependency                       | rda-asset-de | 090669bf |             | service-status                                      | ok       |                                                       | 
 | rda_app   | asset-dependency                       | rda-asset-de | 090669bf |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_app   | authenticator                          | rda-identity | 57905b20 |             | service-status                                      | ok       |                                                       | 
 | rda_app   | authenticator                          | rda-identity | 57905b20 |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_app   | authenticator                          | rda-identity | 57905b20 |             | DB-connectivity                                     | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | service-status                                      | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | service-dependency:registry                         | ok       | 1 pod(s) found for registry                           | 
 | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | service-initialization-status                       | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-access-manager       | rda-access-m | 6338ad29 |             | DB-connectivity                                     | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | service-status                                      | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | service-initialization-status                       | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-notification-service | rda-notifica | bb9e3e7b |             | DB-connectivity                                     | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-status                                      | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-dependency:registry                         | ok       | 1 pod(s) found for registry                           | 
 | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-dependency:cfxdimensions-app-access-manager | ok       | 1 pod(s) found for cfxdimensions-app-access-manager   | 
 | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | service-initialization-status                       | ok       |                                                       | 
 | rda_app   | cfxdimensions-app-resource-manager     | rda-resource | e5a28e16 |             | DB-connectivity                                     | ok       |                                                       | 
 | rda_infra | collector                              | rda-collecto | 99553e51 |             | service-status                                      | ok       |                                                       | 
 | rda_infra | collector                              | rda-collecto | 99553e51 |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_infra | collector                              | rda-collecto | 99553e51 |             | opensearch-connectivity:default                     | ok       |                                                       | 
 | rda_infra | registry                               | rda-registry | a46cd712 |             | service-status                                      | ok       |                                                       | 
 | rda_infra | registry                               | rda-registry | a46cd712 |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_infra | scheduler                              | rda-schedule | d5537051 |             | service-status                                      | ok       |                                                       | 
 | rda_infra | scheduler                              | rda-schedule | d5537051 |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_infra | scheduler                              | rda-schedule | d5537051 |             | DB-connectivity                                     | ok       |                                                       | 
 | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | service-status                                      | ok       |                                                       | 
 | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | minio-connectivity                                  | ok       |                                                       | 
 | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | service-dependency:registry                         | ok       | 1 pod(s) found for registry                           | 
 | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | service-initialization-status                       | ok       |                                                       | 
 | rda_app   | user-preferences                       | rda-user-pre | fd09d3ba |             | DB-connectivity                                     | ok       |                                                       | 
 +-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-------------------------------------------------------+

```

### ****7.8 RDAF Worker Services Installation****

KubernetesNon-Kubernetes

`rdafk8s worker install` command is used to deploy / install RDAF worker services.

Run the below command to deploy all RDAF worker services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com)
```
 rdafk8s worker install --tag 3.4.2

```

**Status check**

Run the below command to see the status of all of the deployed RDAF worker services.
```
 rdafk8s worker status

```

Example Output
```
 +------------+-----------------+---------------+--------------+---------------------+ 
 | Name       | Host            | Status        | Container Id | Tag                 | 
 +------------+-----------------+---------------+--------------+---------------------+ 
 | rda_worker | 192.168.125.149 | Up 18 seconds | 29cdeefd9d95 |       3.4.2         | 
 +------------+-----------------+---------------+--------------+---------------------+

```

Below are the Kubernetes Cluster `kubectl get pods` commands to check the status of RDA Fabric worker services.
```
 kubectl get pods -n rda-fabric -l app_category=rdaf-worker

```

Example Output
```
 NAME                          READY   STATUS    RESTARTS   AGE 
 rda-worker-749b977b95-cf757   1/1     Running   0          11d 
 rda-worker-749b977b95-xkb5w   1/1     Running   0          11d

```

Below `kubectl get pods` command provides additional details of deployed RDAF worker services (PODs) along with their worker node(s) on which they were deployed.
```
 kubectl get pods -n rda-fabric -o wide -l app_category=rdaf-worker

```

In order to get detailed status of the each RDAF worker service POD, run the below `kubectl describe pod` command.
```
 kubectl describe pod rda-collector-6bd6c79475-52hvg  -n rda-fabric

```

Example Output
```
 Name:         rda-worker-749b977b95-cf757 
 Namespace:    rda-fabric 
 Priority:     0 
 Node:         hari-k8-cluster-infra10820/192.168.108.20 
 Start Time:   Tue, 31 Jan 2023 05:18:11 +0000 
 Labels:       app=rda-fabric-services 
                 app_category=rdaf-worker 
                 app_component=rda-worker 
                 pod-template-hash=749b977b95 
 ... 
 ... 
 QoS Class:                   Burstable 
 Node-Selectors:              rdaf_worker_services=allow 
 Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s 
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s 
                             pod-type=rda-tenant:NoSchedule 
 Events:                      <none>

```

`rdaf worker install` command is used to deploy / install RDAF worker services.

Run the below command to deploy all RDAF worker services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com)
```
 rdaf worker install --tag 3.4.2

```

**Status check**

Run the below command to see the status of all of the deployed RDAF worker services.
```
 rdaf worker status

```

Example Output
```
 +------------+-----------------+---------------+--------------+-----------------+ 
 | Name       | Host            | Status        | Container Id | Tag             | 
 +------------+-----------------+---------------+--------------+-----------------+ 
 | rda_worker | 192.168.125.149 | Up 18 seconds | 29cdeefd9d95 |       3.4.2     | 
 +------------+-----------------+---------------+--------------+-----------------+

```

### ****7.9 RDAF App Services Installation****

KubernetesNon-Kubernetes

Please refer the below document to deploy / install RDAF OIA (a.k.a AIOps) application services

*   [**OIA:** Install / Upgrade Operations Intelligence and Analytics (**AIOps**)](https://bot-docs.cloudfabrix.io/installation_guides/oia_deployment/)
    

Please refer the below document to deploy / install RDAF OIA (a.k.a AIOps) application services

*   [**OIA:** Install / Upgrade Operations Intelligence and Analytics (**AIOps**)](https://bot-docs.cloudfabrix.io/installation_guides/oia_deployment/)
    

## **8\. SSL Certificates Installation**

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


```
openssl crl2pkcs7 -nocrl -certfile server-ssl-certificate.crt \| openssl pkcs7 -print_certs -noout
```

![CFX-SSL-Cert1](https://bot-docs.cloudfabrix.io/images/ssl-cert/cfx-rda-ssl-01.png)

Once you have the SSL certificate files as mentioned above, you need to create an SSL certificate chain by grouping them together as a single file in PEM format.

Th below diagram shows a valid CA signed SSL certificate chain flow for reference.

![CFX-SSL-Cert2](https://bot-docs.cloudfabrix.io/images/ssl-cert/cfx-rda-ssl-02.png)

Run the below command to create a valid SSL certificate chain. (supported format is PEM)


```
cat server-ssl-private.key server-ssl-certificate.crt trusted-ca-intermediate-root.crt trusted-ca-root.crt > cfx-ssl-haproxy.pem
```

**OR**


```
cat server-ssl-private.key server-ssl-certificate.crt trusted-ca-intermediate-and-root-chain.crt > cfx-ssl-haproxy.pem
```

![CFX-SSL-Cert3](https://bot-docs.cloudfabrix.io/images/ssl-cert/cfx-rda-ssl-03.png)

Info

**Note:** The final consolidated SSL certificate chain output is saved to **cfx-ssl-haproxy.pem** file which will be applied to HA Proxy configuration later in this document. The filename used here for reference only.

### **8.2 CA-signed SSL certificate verification:**

Info

**openssl** tool is a pre-requisite for performing SSL certificate validation checks

**Step 1:** Run the below commands to verify both server's SSL certificate and private key. The output of these two commands should match exactly the same.


```
openssl x509 -noout -modulus -in server-ssl-certificate.crt \| openssl md5
```


```
openssl rsa -noout -modulus -in server-ssl-private.key \| openssl md5
```

**Step 2:** Run the below commands to verify server's SSL certificate, intermediate & root certificate's (chain) date is valid and not expired.


```
openssl x509 -noout -in server-ssl-certificate.crt -dates
```


```
openssl x509 -noout -in trusted-ca-root.crt -dates
```


```
openssl x509 -noout -in trusted-ca-intermediate-root.crt -dates
```

**Step 3:** Run the below commands to verify the public keys contained in the private key file and the server certificate file are the same. The output of these two commands should match.


```
openssl x509 -in server-ssl-certificate.crt -noout -pubkey
```


```
openssl rsa -in server-ssl-private.key -pubout
```

**Step 4:** Run the below command to verify the validity of the certificate chain. The response should come out as **OK**.


```
openssl verify -CAfile trusted-ca-root.crt server-ssl-certificate.crt
```

**OR**


```
openssl verify -CAfile trusted-ca-intermediate-and-root-chain.crt server-ssl-certificate.crt
```

**Step 5:** Run the below command to see and verify SSL certificate chain order is correct.


```
openssl crl2pkcs7 -nocrl -certfile cfx-ssl-haproxy.pem \| openssl pkcs7 -print_certs -noout
```

Please refer to the below screenshot on how to validate the SSL certificate chain order.

![CFX-SSL-Cert4](https://bot-docs.cloudfabrix.io/images/ssl-cert/cfx-rda-ssl-04.png)

Verify if the SSL certificate and key is in PEM format.


```
openssl rsa -inform PEM -in server-ssl-private.key
```


```
openssl x509 -inform PEM -in server-ssl-certificate.crt
```

### **8.3 CA-signed SSL Certificate Installation for HA Proxy service:**

**Step 1:** Go to HAProxy service's certificates path on VM host(s) where HAProxy service was installed.


```
/opt/rdaf/cert/<HAProxy IP>/
```

**Step 2:** Take a backup of the existing HA Proxy service's SSL certificate


```
cp haproxy.pem haproxy.pem.backup
```

**Step 3:** Copy the CA-signed SSL certificate chain file that is in PEM format to this location as **haproxy.pem**


```
cp <ssl-cert-path>/cfx-ssl-haproxy.pem haproxy.pem
```

**Step 4:** Restart HA Proxy container


```
docker ps -a \| grep haproxy
```


```
docker restart <haproxy-container-id>
```

**Step 5:** Verify HA Proxy service logs to make sure there are no errors after installing CA signed SSL server certificate chain file.


```
docker logs -f <haproxy-container-id> --tail 200
```

**Step 6:** Run the below **openssl** command to verify the newly installed SSL certificate and check SSL verification is shown as **OK** without any validation failures.


```
openssl s_client -connect <cfx-platform-FQDN>:443
```

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


```
openssl pkcs12 -in server-ssl-certificate.pfx -out server-ssl-certificate.pem -nodes
```

*   **Convert P7B to PEM**


```
openssl pkcs7 -print_certs -in server-ssl-certificate.p7b -out server-ssl-certificate.pem
```

*   **Convert DER to PEM**


```
openssl x509 -inform der -in server-ssl-certificate.cer -out server-ssl-certificate.pem
```

You can use the following commands to check if your certificate files are already in the required format:

*   **Check and verify if your key is in PEM format**


```
openssl rsa -inform PEM -in server-ssl-private.key
```

*   **Check and verify if your certificate is in PEM format**


```
openssl x509 -inform PEM -in server-ssl-certificate.pem
```

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!