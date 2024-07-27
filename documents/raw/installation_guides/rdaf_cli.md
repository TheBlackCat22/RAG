 



Guide to Install RDAF deployment CLI for Non-Kubernetes Environment.
====================================================================

**1\. RDAF Deployment CLI for Non-Kubernetes**
----------------------------------------------

RDA Fabric deployment CLI is a comprehensive command line management tool that is used to setup, install/deploy and manage CloudFabrix on-premise Docker registry, RDA Fabric platform, infrastructure and application services.

RDA Fabric platform, infrastructure and application services are supported to be deployed on a **Kubernetes Cluster** or as a **Standalone Container Services** using `docker-compose` utility.

Please refer for [RDAF Platform deployment on **Kubernetes Cluster**](/installation_guides/rdaf_k8s_cli/)

RDAF CLI uses docker-compose as underlying container management utility for deploying and managing RDA Fabric environment when it need to be deployed on non-kubernetes cluster environment.

RDAF CLI can be installed on on-premise docker registry VM if it is provisioned or on one of the RDA Fabric platform VMs or both to install, configure and manage on-premise docker registry service and RDA Fabric platform services.

### **1.1 CLI Installation or Upgrade:**

Please download the RDAF deployment bundles from the below provided links.

Tip

In a restricted environment where there is no direct internet access, please download **RDAF Deployment CLI offline bundle.**

**RDAF Deployment CLI offline bundle for RHEL:** [offline-rhel-1.2.2.tar.gz](https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/offline-rhel-1.2.2.tar.gz "RHEL offline-rhel-1.2.1.tar.gz")

**RDAF Deployment CLI offline bundle for Ubuntu:** [offline-ubuntu-1.2.2.tar.gz](https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/offline-ubuntu-1.2.2.tar.gz "Ubuntu offline-ubuntu-1.2.2.tar.gz")

**RDAF Deployment CLI bundle:** [rdafcli-1.2.2.tar.gz](https://macaw-amer.s3.amazonaws.com/releases/rdaf-platform/1.2.2/rdafcli-1.2.2.tar.gz "rdafcli-1.2.2.tar.gz")

Note

For latest RDAF Deployment CLI versioned package, please contact **support@cloudfabrix.com**

Login as **rdauser** user into on-premise docker registry or RDA Fabric Platform VM using any SSH client tool (ex: putty)

Run the following command to install or upgrade the RDA Fabric deployment CLI tool.

|     |     |
| --- | --- |
| [1](#__codelineno-0-1)<br>[2](#__codelineno-0-2) | `pip install --user --upgrade pip pip install --user rdafcli-1.2.2.tar.gz` |

Note

Once the above commands run successfully, logout and logback in to a new session.

Run the below command to verify installed RDAF deployment CLI version

`[](#__codelineno-1-1) rdaf --version`

Run the below command to view the RDAF deployment CLI help

`[](#__codelineno-2-1) rdaf --help`

`[](#__codelineno-3-1) Documented commands (type help <topic>): [](#__codelineno-3-2) ======================================== [](#__codelineno-3-3) [](#__codelineno-3-4) app     help   platform      rdac_cli  reset    setregistry  status    worker [](#__codelineno-3-5) backup  infra  prune_images  registry  restore  setup        validate`

### **1.2 On-premise Docker Registry setup:**

CloudFabrix support hosting an on-premise docker registry which will download and synchronize RDA Fabric's platform, infrastructure and application services from CloudFabrix's public docker registry that is securely hosted on AWS and from other public docker registries as well. For more information on on-premise docker registry, please refer **[Docker registry access for RDAF platform services](https://bot-docs.cloudfabrix.io/installation_guides/deployment/#2-docker-registry-access-for-rdaf-platform-services-deployment)
**.

#### **1.2.1 rdaf registry setup**

Run rdaf registry --help to see available CLI options to deploy and manage on-premise docker registry.

|     |     |
| --- | --- |
| [1](#__codelineno-4-1)<br> [2](#__codelineno-4-2)<br> [3](#__codelineno-4-3)<br> [4](#__codelineno-4-4)<br> [5](#__codelineno-4-5)<br> [6](#__codelineno-4-6)<br> [7](#__codelineno-4-7)<br> [8](#__codelineno-4-8)<br> [9](#__codelineno-4-9)<br>[10](#__codelineno-4-10)<br>[11](#__codelineno-4-11)<br>[12](#__codelineno-4-12)<br>[13](#__codelineno-4-13)<br>[14](#__codelineno-4-14)<br>[15](#__codelineno-4-15)<br>[16](#__codelineno-4-16)<br>[17](#__codelineno-4-17)<br>[18](#__codelineno-4-18)<br>[19](#__codelineno-4-19)<br>[20](#__codelineno-4-20)<br>[21](#__codelineno-4-21)<br>[22](#__codelineno-4-22) | `rdaf registry --help usage: ('registry',) [--insecure] [-h] [--debug]                      {setup,upgrade,install,fetch,delete-images,list-tags} ... Manage the Docker registry positional arguments:   {setup,upgrade,install,fetch,delete-images,list-tags}     setup               Setup Docker Registry     upgrade             Upgrade Registry locally     install             Install Registry locally     fetch               Fetch from configured Docker registries     delete-images       Deletes tag(s) and corresponding docker images     list-tags           Lists all the tags for all images in the docker                         registry optional arguments:   --insecure            Ignore SSL certificate issues when communicating with                         various hosts   -h, --help            show this help message and exit   --debug               Enable debug logs for the CLI operations` |

Run rdaf registry setup --help to see available CLI options.

|     |     |
| --- | --- |
| [1](#__codelineno-5-1)<br> [2](#__codelineno-5-2)<br> [3](#__codelineno-5-3)<br> [4](#__codelineno-5-4)<br> [5](#__codelineno-5-5)<br> [6](#__codelineno-5-6)<br> [7](#__codelineno-5-7)<br> [8](#__codelineno-5-8)<br> [9](#__codelineno-5-9)<br>[10](#__codelineno-5-10)<br>[11](#__codelineno-5-11)<br>[12](#__codelineno-5-12)<br>[13](#__codelineno-5-13)<br>[14](#__codelineno-5-14)<br>[15](#__codelineno-5-15)<br>[16](#__codelineno-5-16)<br>[17](#__codelineno-5-17)<br>[18](#__codelineno-5-18)<br>[19](#__codelineno-5-19)<br>[20](#__codelineno-5-20)<br>[21](#__codelineno-5-21) | `rdaf registry setup --help optional arguments:   -h, --help            show this help message and exit   --install-root INSTALL_ROOT                         Path to a directory where the Docker registry will be                         installed and managed   --docker-server-host DOCKER_SERVER_HOST                         Host name or IP address of the host where the Docker                         registry will be installed   --docker-registry-source-host DOCKER_SOURCE_HOST                         The hostname/IP of the source docker registry   --docker-registry-source-port DOCKER_SOURCE_PORT                         port of the docker registry   --docker-registry-source-user DOCKER_SOURCE_USER                         The username to use while connecting to the source                         docker registry   --docker-registry-source-password DOCKER_SOURCE_PASSWORD                         The password to use while connecting to the source                         docker registry   --no-prompt           Don't prompt for inputs` |

Run the below command to setup and configure on-premise docker registry service. In the below command example, 10.99.120.140 is the machine on which on-premise registry service is going to installed.

cfxregistry.cloudfabrix.io is the CloudFabrix's public docker registry hosted on AWS from which RDA Fabric docker images are going to be downloaded.

|     |     |
| --- | --- |
| [1](#__codelineno-6-1)<br>[2](#__codelineno-6-2)<br>[3](#__codelineno-6-3)<br>[4](#__codelineno-6-4)<br>[5](#__codelineno-6-5) | `rdaf registry setup --docker-server-host 10.99.120.140 \     --docker-registry-source-host cfxregistry.cloudfabrix.io \     --docker-registry-source-port 443 \     --docker-registry-source-user readonly \     --docker-registry-source-password readonly` |

#### **1.2.2 rdaf registry install**

Run the below command to install the on-premise docker registry service.

|     |     |
| --- | --- |
| [1](#__codelineno-7-1) | `rdaf registry install --tag 1.0.3` |

Info

*   For latest tag version, please contact support@cloudfabrix.com
*   On-premise docker registry service runs on port **TCP/5000**. This port may need to be enabled on firewall device if on-premise docker registry service and RDA Fabric service VMs are deployed in different network environments.

Run the below command to upgrade the on-premise docker registry service to latest version.

|     |     |
| --- | --- |
| [1](#__codelineno-8-1) | `rdaf registry upgrade --tag <tag-name>` |

To check the status of the on-premise docker registry service, run the below command.

|     |     |
| --- | --- |
| [1](#__codelineno-9-1) | `docker ps -a \| grep docker-registry` |

#### **1.2.3 rdaf registry fetch**

Once on-premise docker registry service is installed, run the below command to download one or more tags to pre-stage the docker images for RDA Fabric services deployment for fresh install or upgrade.

`[](#__codelineno-10-1) rdaf registry fetch --tag 1.0.3.2,3.4.2,7.4.2,1.0.3`

**Minio** object storage service image need to be downloaded explicitly using the below command.

`[](#__codelineno-11-1) rdaf registry fetch --minio-tag RELEASE.2023-09-30T07-02-29Z`

Info

**Note:** It may take few minutes to few hours depends on the outbound internet access bandwidth and the number of docker images to be downloaded. The default location path for the downloaded docker images is **/opt/rdaf-registry/data/docker/registry**. This path can be overridden/changed during **rdaf registry setup** command using **\--install-root** option if needed.

#### **1.2.4 rdaf registry list-tags**

Run the below command to list the downloaded images and their corresponding tags / versions.

|     |     |
| --- | --- |
| [1](#__codelineno-12-1) | `rdaf registry list-tags` |

#### **1.2.5 rdaf registry delete-images**

Run the below command to delete one or more tags and corresponding docker images from on-premise docker registry.

|     |     |
| --- | --- |
| [1](#__codelineno-13-1) | `rdaf registry delete-images --tag <tag-1>,<tag-2>` |

Important

When **on-premise docker repository** service is used, please make sure to add the **insecure-registries** parameter to **/etc/docker/daemon.json** file and restart the **docker daemon** as shown below on **all of RDA Fabric VMs** before the deployment.

|     |     |
| --- | --- |
| [1](#__codelineno-14-1)<br> [2](#__codelineno-14-2)<br> [3](#__codelineno-14-3)<br> [4](#__codelineno-14-4)<br> [5](#__codelineno-14-5)<br> [6](#__codelineno-14-6)<br> [7](#__codelineno-14-7)<br> [8](#__codelineno-14-8)<br> [9](#__codelineno-14-9)<br>[10](#__codelineno-14-10)<br>[11](#__codelineno-14-11)<br>[12](#__codelineno-14-12)<br>[13](#__codelineno-14-13)<br>[14](#__codelineno-14-14)<br>[15](#__codelineno-14-15)<br>[16](#__codelineno-14-16) | `{  "tls": true,   "tlscacert": "/etc/tlscerts/ca/ca.pem",   "tlsverify": true,   "storage-driver": "overlay2",   "hosts": [   "unix:///var/run/docker.sock",    "tcp://0.0.0.0:2376"  ],   "tlskey": "/etc/tlscerts/server/server.key",   "debug": false,   "tlscert": "/etc/tlscerts/server/server.pem",   "experimental": false,   "insecure-registries" : ["<on-premise-docker-registry-ip-or-dns>:5000"],  "live-restore": true }` |

|     |     |
| --- | --- |
| [1](#__codelineno-15-1) | `sudo systemctl daemon-reload` |

|     |     |
| --- | --- |
| [1](#__codelineno-16-1) | `sudo systemctl restart docker` |

|     |     |
| --- | --- |
| [1](#__codelineno-17-1) | `docker info` |

[Example Output](#__tabbed_1_1)

`[](#__codelineno-18-1) ... [](#__codelineno-18-2) ... [](#__codelineno-18-3) Kernel Version: 5.4.0-110-generic [](#__codelineno-18-4)  Operating System: Ubuntu 20.04.4 LTS [](#__codelineno-18-5)  OSType: linux [](#__codelineno-18-6)  Architecture: x86_64 [](#__codelineno-18-7)  CPUs: 2 [](#__codelineno-18-8)  Total Memory: 7.741GiB [](#__codelineno-18-9)  Name: rdaf-onprem-docker-repo [](#__codelineno-18-10)  ID: OLZF:ZKWN:TIQJ:ZMNV:2STT:JHR3:3RAT:TAL5:TF47:OGVQ:LHY7:RMHH [](#__codelineno-18-11)  Docker Root Dir: /var/lib/docker [](#__codelineno-18-12)  Debug Mode: false [](#__codelineno-18-13)  Registry: https://index.docker.io/v1/ [](#__codelineno-18-14)  Labels: [](#__codelineno-18-15)  Experimental: false [](#__codelineno-18-16)  Insecure Registries: [](#__codelineno-18-17)   10.99.120.140:5000 [](#__codelineno-18-18)   127.0.0.0/8 [](#__codelineno-18-19)  Live Restore Enabled: true`

Tip

The location of the on-premise docker registry's CA certificate file `ca.crt` is located under **/opt/rdaf-registry/cert/ca**. This file `ca.crt` need to be copied to the machine on which **RDAF CLI** is used to **setup, configure and install RDA Fabric platform** and all of the required services using on-premise docker registry. This step is not applicable when cloud hosted docker registry **cfxregistry.cloudfabrix.io** is used.

### **1.3 RDAF Platform setup**

#### **1.3.1 rdaf setregistry**

When on-premise docker registry is deployed, change the default docker registry configuration to on-premise docker registry host to pull and install the RDA Fabric services.

Please refer `rdaf setregistry --help` for detailed command options.

`[](#__codelineno-19-1) Configure the Docker registry for the platform [](#__codelineno-19-2) [](#__codelineno-19-3) optional arguments: [](#__codelineno-19-4)   -h, --help            show this help message and exit [](#__codelineno-19-5)   --debug               Enable debug logs for the CLI operations (Optional) [](#__codelineno-19-6)   --host DOCKER_REGISTRY_HOST [](#__codelineno-19-7)                         Hostname/IP of the Docker registry [](#__codelineno-19-8)   --port DOCKER_REGISTRY_PORT [](#__codelineno-19-9)                         Port of the Docker registry [](#__codelineno-19-10)   --user DOCKER_REGISTRY_USER [](#__codelineno-19-11)                         Username of the Docker registry (Optional) [](#__codelineno-19-12)   --password DOCKER_REGISTRY_PASSWORD [](#__codelineno-19-13)                         Password of the Docker registry (Optional) [](#__codelineno-19-14)   --cert-path CERT_PATH [](#__codelineno-19-15)                         path of the Docker registry ca cert`

*   Copy the `ca.crt` file from on-premise registry.

``[](#__codelineno-20-1) sudo mkdir -p /opt/rdaf-registry [](#__codelineno-20-2) sudo chown -R `id -u`:`id -g` /opt/rdaf-registry``

`[](#__codelineno-21-1) scp rdauser@<on-premise-registry-ip>:/opt/rdaf-registry/cert/ca/ca.crt /opt/rdaf-registry/registry-ca-cert.crt`

*   Run the below command to set the docker-registry to on-premise one.

`[](#__codelineno-22-1) rdaf setregistry --host <on-premise-docker-registry-ip-or-dns> --port 5000 --cert-path /opt/rdaf-registry/registry-ca-cert.crt`

Tip

Please verify if **on-premise docker registry** is accessible on **port 5000** using either of the below commands.

*   **telnet `<on-premise-docker-registry-ip-or-dns>` 5000**
*   **curl -vv telnet://`<on-premise-docker-registry-ip-or-dns>`:5000**

#### **1.3.2 rdaf setup**

Run the below `rdaf setup` command to create the RDAF platform's deployment configuration. It is a pre-requisite before RDAF infrastructure, platform and application services can be installed.

It will prompt for all the necessary configuration details.

`[](#__codelineno-23-1) rdaf setup`

*   Accept the EULA

`[](#__codelineno-24-1) Do you accept the EULA? [yes/no]: yes`

*   Enter the **rdauser** SSH password for all of the RDAF hosts.

`[](#__codelineno-25-1) What is the SSH password for the SSH user used to communicate between hosts [](#__codelineno-25-2) SSH password: [](#__codelineno-25-3) Re-enter SSH password:`

Tip

Please make sure **rdauser's** SSH password on all of the RDAF hosts is same during the `rdaf setup` command.

Press **Enter** to accept the defaults.

`[](#__codelineno-26-1) Provide any Subject alt name(s) to be used while generating SAN certs [](#__codelineno-26-2) Subject alt name(s) for certs[]:`

*   Enter RDAF Platform host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts are required for the HA configuration. If it is a non-HA deployment, only one RDAF platform host's ip address or DNS name is required.

`[](#__codelineno-27-1) What are the host(s) on which you want the RDAF platform services to be installed? [](#__codelineno-27-2) Platform service host(s)[rda-platform-vm01]: 192.168.125.141,192.168.125.142`

*   Answer if the RDAF application services are going to be deployed in HA mode or standalone.

`[](#__codelineno-28-1) Will application services be installed in HA mode? [yes/No]: yes`

*   Enter RDAF Application services host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts or more are required for the HA configuration. If it is a non-HA deployment, only one RDAF application service host's ip address or DNS name is required.

`[](#__codelineno-29-1) What are the host(s) on which you want the application services to be installed? [](#__codelineno-29-2) Application service host(s)[rda-platform-vm01]: 192.168.125.143,192.168.125.144`

*   Enter the name of the Organization. In the below example, `ACME_IT_Services` is used as the Organization name. It is for a reference only.

`[](#__codelineno-30-1) What is the organization you want to use for the admin user created? [](#__codelineno-30-2) Admin organization[CloudFabrix]: ACME_IT_Services`

Press **Enter** to accept the defaults.

`[](#__codelineno-31-1) What is the ca cert to use to communicate to on-prem docker registry [](#__codelineno-31-2) Docker Registry CA cert path[]:`

*   Enter RDAF Worker service host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts or more are required for the HA configuration. If it is a non-HA deployment, only one RDAF worker service host's ip address or DNS name is required.

`[](#__codelineno-32-1) What are the host(s) on which you want the Worker to be installed? [](#__codelineno-32-2) Worker host(s)[rda-platform-vm01]: 192.168.125.145`

*   Enter ip address on which RDAF Event Gateway needs to be Installed, For HA configuration please enter comma separated values. Minimum of 2 hosts or more are required for the HA configuration. If it is a non-HA deployment, only one RDAF Event Gateway host's ip address or DNS name is required.

`[](#__codelineno-33-1) What are the host(s) on which you want the Event Gateway to be installed? [](#__codelineno-33-2) Event Gateway host(s)[rda-platform-vm01]: 192.168.125.67`

*   Enter RDAF infrastructure service `NATs` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts are required for the `NATs` HA configuration. If it is a non-HA deployment, only one RDAF `NATs` service host's ip address or DNS name is required.

`[](#__codelineno-34-1) What is the "host/path-on-host" on which you want the Nats to be deployed? [](#__codelineno-34-2) Nats host/path[192.168.125.141]: 192.168.125.145,192.168.125.146`

*   Enter RDAF infrastructure service `Minio` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 4 hosts are required for the `Minio` HA configuration. If it is a non-HA deployment, only one RDAF `Minio` service host's ip address or DNS name is required.

`[](#__codelineno-35-1) What is the "host/path-on-host" where you want Minio to be provisioned? [](#__codelineno-35-2) Minio server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147,192.168.125.148`

*   Change the default `Minio` user credentials if needed or press **Enter** to accept the defaults.

`[](#__codelineno-36-1) What is the user name you want to give for Minio root user that will be created and used by the RDAF platform? [](#__codelineno-36-2) Minio user[rdafadmin]:  [](#__codelineno-36-3) What is the password you want to use for the newly created Minio root user? [](#__codelineno-36-4) Minio password[Q8aJ63PT]:` 

*   Enter RDAF infrastructure service `MariDB` database host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `MariDB` database HA configuration. If it is a non-HA deployment, only one RDAF `MariaDB` service host's ip address or DNS name is required.

`[](#__codelineno-37-1) What is the "host/path-on-host" on which you want the MariaDB server to be provisioned? [](#__codelineno-37-2) MariaDB server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Change the default `MariaDB` user credentials if needed or press **Enter** to accept the defaults.

`[](#__codelineno-38-1) What is the user name you want to give for MariaDB admin user that will be created and used by the RDAF platform? [](#__codelineno-38-2) MariaDB user[rdafadmin]:  [](#__codelineno-38-3) What is the password you want to use for the newly created MariaDB root user? [](#__codelineno-38-4) MariaDB password[jffqjAaZ]:` 

*   Enter RDAF infrastructure service `Opensearch` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `Opensearch` HA configuration. If it is a non-HA deployment, only one RDAF `Opensearch` service host's ip address or DNS name is required.

`[](#__codelineno-39-1) What is the "host/path-on-host" on which you want the opensearch server to be provisioned? [](#__codelineno-39-2) opensearch server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Change the default `Opensearch` user credentials if needed or press **Enter** to accept the defaults.

`[](#__codelineno-40-1) What is the user name you want to give for Opensearch admin user that will be created and used by the RDAF platform? [](#__codelineno-40-2) Opensearch user[rdafadmin]:  [](#__codelineno-40-3) What is the password you want to use for the newly created Opensearch admin user? [](#__codelineno-40-4) Opensearch password[sLmr4ICX]:` 

*   Enter RDAF infrastructure service `Zookeeper` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `Zookeeper` HA configuration. If it is a non-HA deployment, only one RDAF `Zookeeper` service host's ip address or DNS name is required.

`[](#__codelineno-41-1) What is the "host/path-on-host" on which you want the Zookeeper server to be provisioned? [](#__codelineno-41-2) Zookeeper server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Enter RDAF infrastructure service `Kafka` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `Kafka` HA configuration. If it is a non-HA deployment, only one RDAF `Kafka` service host's ip address or DNS name is required.

`[](#__codelineno-42-1) What is the "host/path-on-host" on which you want the Kafka server to be provisioned? [](#__codelineno-42-2) Kafka server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Enter RDAF infrastructure service `Redis` host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 3 hosts are required for the `Redis` HA configuration. If it is a non-HA deployment, only one RDAF `Redis` service host's ip address or DNS name is required.

`[](#__codelineno-43-1) What is the "host/path-on-host" on which you want the Redis server to be provisioned? [](#__codelineno-43-2) Redis server host/path[192.168.125.141]: 192.168.125.145,192.168.125.146,192.168.125.147`

*   Enter RDAF infrastructure service `HAProxy` (load-balancer) host(s) ip address or DNS name. For HA configuration, please enter comma separated values. Minimum of 2 hosts are required for the `HAProxy` HA configuration. If it is a non-HA deployment, only one RDAF `HAProxy` service host's ip address or DNS name is required.

`[](#__codelineno-44-1) What is the host on which you want HAProxy to be provisioned? [](#__codelineno-44-2) HAProxy host[192.168.125.141]: 192.168.125.145,192.168.125.146`

*   Select the network interface name which is used for UI portal access. Ex: `eth0` or `ens160` etc.

`[](#__codelineno-45-1) What is the network interface on which you want the rdaf to be accessible externally? [](#__codelineno-45-2) Advertised external interface[eth0]: ens160`

*   Enter the `HAProxy` service's virtual IP address when it is configured in HA configuration. Virtual IP address should be an unused IP address. This step is not applicable when `HAProxy` service is deployed in non-HA configuration.

`[](#__codelineno-46-1) What is the host on which you want the platform to be externally accessible? [](#__codelineno-46-2) Advertised external host[192.168.125.143]: 192.168.125.149`

*   Enter the ip address of the Internal accessible advertised host

`[](#__codelineno-47-1) Do you want to specify an internal advertised host? [yes/No]: No`

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

#### **1.3.4.1 rdaf infra**

`rdaf infra` command is used to deploy and manage RDAF infrastructure services. Run the below command to view available CLI options.

`[](#__codelineno-48-1) usage: infra [--insecure] [-h] [--debug] {status,install,upgrade,up,down} ... [](#__codelineno-48-2) [](#__codelineno-48-3) Manage infra services [](#__codelineno-48-4) [](#__codelineno-48-5) positional arguments: [](#__codelineno-48-6)   {status,install,upgrade,up,down} [](#__codelineno-48-7)     status              Status of the RDAF Infra [](#__codelineno-48-8)     install             Install the RDAF Infra containers [](#__codelineno-48-9)     upgrade             Upgrade the RDAF Infra containers [](#__codelineno-48-10)     up                  Crate the RDAF Infra Containers [](#__codelineno-48-11)     down                Delete the RDAF Infra Containers [](#__codelineno-48-12)     healthcheck         Check the liveness/health of Infra services. [](#__codelineno-48-13) [](#__codelineno-48-14) optional arguments: [](#__codelineno-48-15)   --insecure            Ignore SSL certificate issues when communicating with [](#__codelineno-48-16)                         various hosts [](#__codelineno-48-17)   -h, --help            show this help message and exit [](#__codelineno-48-18)   --debug               Enable debug logs for the CLI operations`

##### **1.3.4.1.1 Install infra services**

`rdaf infra install` command is used to deploy / install RDAF infrastructure services. Run the below command to view the available CLI options.

`[](#__codelineno-49-1) usage: infra install [-h] --tag TAG [--service SERVICES] [](#__codelineno-49-2) [](#__codelineno-49-3) optional arguments: [](#__codelineno-49-4)   -h, --help          show this help message and exit [](#__codelineno-49-5)   --tag TAG           Tag to use for the docker images of the infra components [](#__codelineno-49-6)   --service SERVICES  Restrict the scope of the command to a specific service`

Run the below command to deploy all RDAF infrastructure services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com.)

`[](#__codelineno-50-1) rdaf infra install --tag 1.0.3`

Run the below command to install a specific RDAF infrastructure service. Below are the supported infrastructure services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com)

*   haproxy
*   nats
*   mariadb
*   opensearch
*   kafka
*   zookeeper
*   redis
*   graphdb

`[](#__codelineno-51-1) rdaf infra install --service haproxy --tag 1.0.3.2`

##### **1.3.4.1.2 Status check**

Run the below command to see the status of all of the deployed RDAF infrastructure services.

`[](#__codelineno-52-1) rdaf infra status`

[Example Output](#__tabbed_2_1)

`[](#__codelineno-53-1) +----------------------+----------------+-----------------+--------------+--------------------+ [](#__codelineno-53-2)   | Name               | Host           | Status          | Container Id | Tag                | [](#__codelineno-53-3)   +--------------------+----------------+-----------------+--------------+--------------------+ [](#__codelineno-53-4)   | haproxy            | 192.168.133.97 | Up 3 days       | 41208fa98fa6 | 1.0.3.2            | [](#__codelineno-53-5)   | haproxy            | 192.168.133.98 | Up 3 days       | 3891dded450a | 1.0.3.2            | [](#__codelineno-53-6)   |keepalived          | 192.168.133.97 | active          | N/A          | N/A                | [](#__codelineno-53-7)   | keepalived         | 192.168.133.98 | active          | N/A          | N/A                | [](#__codelineno-53-8)   | nats               | 192.168.133.97 | Up 3 days       | f4405859b336 | 1.0.3              | [](#__codelineno-53-9)   | nats               | 192.168.133.98 | Up 3 days       | e8bd7ec195cb | 1.0.3              | [](#__codelineno-53-10)   | minio              | 192.168.133.93 | Up 3 days       | 13a00b450e74 | RELEASE.2023-09-30 | [](#__codelineno-53-11)   |                    |                |                 |              | T07-02-29Z         | [](#__codelineno-53-12)   | minio              | 192.168.133.97 | Up 3 days       | 1727f382a70a | RELEASE.2023-09-30 | [](#__codelineno-53-13)   |                    |                |                 |              | T07-02-29Z         | [](#__codelineno-53-14)   | minio              | 192.168.133.98 | Up 3 days       | d011be7b43c9 | RELEASE.2023-09-30 | [](#__codelineno-53-15)   |                    |                |                 |              | T07-02-29Z         | [](#__codelineno-53-16)   | minio              | 192.168.133.99 | Up 3 days       | 240eb6fbe918 | RELEASE.2023-09-30 | [](#__codelineno-53-17)   |                    |                |                 |              | T07-02-29Z         | [](#__codelineno-53-18)   | mariadb            | 192.168.133.97 | Up 3 days       | 6a1b26cd8f6c | 1.0.3              | [](#__codelineno-53-19)   | mariadb            | 192.168.133.98 | Up 3 days       | 2328874827de | 1.0.3              | [](#__codelineno-53-20)   | mariadb            | 192.168.133.99 | Up 3 days       | 65159da97d95 | 1.0.3              | [](#__codelineno-53-21)   | opensearch         | 192.168.133.97 | Up 3 days       | 8f550b70d7ce | 1.0.3              | [](#__codelineno-53-22)   | opensearch         | 192.168.133.98 | Up 3 days       | 83bdd9bece04 | 1.0.3              | [](#__codelineno-53-23)   | opensearch         | 192.168.133.99 | Up 3 days       | 0225e9f6222d | 1.0.3              | [](#__codelineno-53-24)   +--------------------+----------------+-----------------+--------------+--------------------+`

##### **1.3.4.1.3 Start/Stop infra services**

Run the below command to start / stop all RDAF infrastructure services.

`[](#__codelineno-54-1) rdaf infra up [](#__codelineno-54-2) rdaf infra down`

Run the below commands to start / stop a specific RDAF infrastructure service.

`[](#__codelineno-55-1) rdaf infra up --service minio [](#__codelineno-55-2) rdaf infra down --service minio`

Danger

Stopping and Starting RDAF infrastructure service or services is a disruptive operation which will impact all of the RDAF dependant services and causes a downtime. When RDAF platform is deployed in Production environment, please perform these operations only during a scheduled downtime.

##### **1.3.4.1.4 Upgrade infra services**

Run the below command to upgrade all RDAF infrastructure services to a newer version.

`[](#__codelineno-56-1) rdaf infra upgrade --tag 1.0.3`

Run the below command to upgrade a specific RDAF infrastructure service to a newer version.

`[](#__codelineno-57-1) rdaf infra upgrade --service nats --tag 1.0.3`

Tip

Above shown tag version is a sample one and for a reference only, for actual newer versioned tag, please contact CloudFabrix support team at support@cloudfabrix.com

Danger

Please take full configuration and data backup of RDAF platform before any upgrade process. Upgrading RDAF infrastructure service or services is a disruptive operation which will impact all of the RDAF dependant services and causes a downtime. When RDAF platform is deployed in Production environment, please perform upgrade operation only during a scheduled downtime.

##### **1.3.4.1.5 Check Infra services liveness / health status**

Run the below command to verify RDAF infrastructure service's liveness / health status. This command helps to quickly identify any infrastructure service's availability or accessibility issues.

`[](#__codelineno-58-1) rdaf infra healthcheck`

[Example Output](#__tabbed_3_1)

`[](#__codelineno-59-1) 2022-10-26 02:18:14,565 [rdaf.cmd.infra] INFO     - Running Health Check on Infra services [](#__codelineno-59-2) 2022-10-26 02:18:14,565 [rdaf.cmd.infra] INFO     - Running Health Check on haproxy on host 192.168.125.41 [](#__codelineno-59-3) 2022-10-26 02:18:14,691 [rdaf.cmd.infra] INFO     - Running Health Check on nats on host 192.168.125.41 [](#__codelineno-59-4) 2022-10-26 02:18:14,812 [rdaf.cmd.infra] INFO     - Running Health Check on minio on host 192.168.125.41 [](#__codelineno-59-5) 2022-10-26 02:18:15,001 [rdaf.cmd.infra] INFO     - Running Health Check on mariadb on host 192.168.125.41 [](#__codelineno-59-6) 2022-10-26 02:18:15,152 [rdaf.cmd.infra] INFO     - Running Health Check on opensearch on host 192.168.125.41 [](#__codelineno-59-7) 2022-10-26 02:18:15,775 [rdaf.cmd.infra] INFO     - Running Health Check on zookeeper on host 192.168.125.41 [](#__codelineno-59-8) 2022-10-26 02:18:15,904 [rdaf.cmd.infra] INFO     - Running Health Check on kafka on host 192.168.125.41 [](#__codelineno-59-9) 2022-10-26 02:18:16,399 [rdaf.cmd.infra] INFO     - Running Health Check on redis on host 192.168.125.41 [](#__codelineno-59-10) 2022-10-26 02:18:16,546 [rdaf.cmd.infra] INFO     - Running Health Check on redis-sentinel on host 192.168.125.41 [](#__codelineno-59-11) +----------------+-----------------+--------+------------------------+----------------+--------------+ [](#__codelineno-59-12) | Name           | Check           | Status | Reason                 | Host           | Container Id | [](#__codelineno-59-13) +----------------+-----------------+--------+------------------------+----------------+--------------+ [](#__codelineno-59-14) | haproxy        | Port Connection | OK     | N/A                    | 192.168.125.41 | e905acafc36b | [](#__codelineno-59-15) | haproxy        | Service Status  | OK     | N/A                    | 192.168.125.41 | e905acafc36b | [](#__codelineno-59-16) | haproxy        | Firewall Port   | OK     | N/A                    | 192.168.125.41 | e905acafc36b | [](#__codelineno-59-17) | nats           | Port Connection | OK     | N/A                    | 192.168.125.41 | 83d674da41dd | [](#__codelineno-59-18) | nats           | Service Status  | OK     | N/A                    | 192.168.125.41 | 83d674da41dd | [](#__codelineno-59-19) | nats           | Firewall Port   | OK     | N/A                    | 192.168.125.41 | 83d674da41dd | [](#__codelineno-59-20) | minio          | Port Connection | OK     | N/A                    | 192.168.125.41 | ba13e7023d9f | [](#__codelineno-59-21) | minio          | Service Status  | OK     | N/A                    | 192.168.125.41 | ba13e7023d9f | [](#__codelineno-59-22) | minio          | Firewall Port   | OK     | N/A                    | 192.168.125.41 | ba13e7023d9f | [](#__codelineno-59-23) | mariadb        | Port Connection | OK     | N/A                    | 192.168.125.41 | 2fb8ca0233ec | [](#__codelineno-59-24) | mariadb        | Service Status  | OK     | N/A                    | 192.168.125.41 | 2fb8ca0233ec | [](#__codelineno-59-25) | mariadb        | Firewall Port   | OK     | N/A                    | 192.168.125.41 | 2fb8ca0233ec | [](#__codelineno-59-26) | opensearch     | Port Connection | OK     | N/A                    | 192.168.125.41 | 9cde1a3ab673 | [](#__codelineno-59-27) | opensearch     | Service Status  | Failed | 401 Client Error:      | 192.168.125.41 | 9cde1a3ab673 | [](#__codelineno-59-28) |                |                 |        | Unauthorized for url:  |                |              | [](#__codelineno-59-29) |                |                 |        | https://192.168.125.41:9 |              |              | [](#__codelineno-59-30) |                |                 |        | 200/_cluster/stats     |                |              | [](#__codelineno-59-31) | opensearch     | Firewall Port   | OK     | N/A                    | 192.168.125.41 | 9cde1a3ab673 | [](#__codelineno-59-32) | zookeeper      | Port Connection | OK     | N/A                    | 192.168.125.41 | c04cc08417ed | [](#__codelineno-59-33) | zookeeper      | Service Status  | OK     | N/A                    | 192.168.125.41 | c04cc08417ed | [](#__codelineno-59-34) | zookeeper      | Firewall Port   | OK     | N/A                    | 192.168.125.41 | c04cc08417ed | [](#__codelineno-59-35) | kafka          | Port Connection | OK     | N/A                    | 192.168.125.41 | 813e6a5235cd | [](#__codelineno-59-36) | kafka          | Service Status  | OK     | N/A                    | 192.168.125.41 | 813e6a5235cd | [](#__codelineno-59-37) | kafka          | Firewall Port   | OK     | N/A                    | 192.168.125.41 | 813e6a5235cd | [](#__codelineno-59-38) | redis          | Port Connection | OK     | N/A                    | 192.168.125.41 | 95657dd850a7 | [](#__codelineno-59-39) | redis          | Service Status  | OK     | N/A                    | 192.168.125.41 | 95657dd850a7 | [](#__codelineno-59-40) | redis          | Firewall Port   | OK     | N/A                    | 192.168.125.41 | 95657dd850a7 | [](#__codelineno-59-41) | redis-sentinel | Port Connection | OK     | N/A                    | 192.168.125.41 | 9e0d540aa777 | [](#__codelineno-59-42) | redis-sentinel | Service Status  | OK     | N/A                    | 192.168.125.41 | 9e0d540aa777 | [](#__codelineno-59-43) | redis-sentinel | Firewall Port   | OK     | N/A                    | 192.168.125.41 | 9e0d540aa777 | [](#__codelineno-59-44) +----------------+-----------------+--------+------------------------+--------------+--------------+`

#### **1.3.4 rdaf platform**

`rdaf platform` command is used to deploy and manage RDAF core platform services. Run the below command to view available CLI options.

`[](#__codelineno-60-1) usage: platform [-h] [--debug] {} ... [](#__codelineno-60-2) [](#__codelineno-60-3) Manage the RDAF Platform [](#__codelineno-60-4) [](#__codelineno-60-5) positional arguments: [](#__codelineno-60-6)   {}                commands [](#__codelineno-60-7)     add-service-host [](#__codelineno-60-8)                     Add extra service vm [](#__codelineno-60-9)     status          Status of the RDAF Platform [](#__codelineno-60-10)     up              Create the RDAF Platform Containers [](#__codelineno-60-11)     down            Deleting the RDAF Platform Containers [](#__codelineno-60-12)     install         Install the RDAF platform containers [](#__codelineno-60-13)     upgrade         Upgrade the RDAF platform containers [](#__codelineno-60-14)     generate-certs  Generate certificates for hosts belonging to this [](#__codelineno-60-15)                     installation [](#__codelineno-60-16)     reset-admin-user [](#__codelineno-60-17)                     reset the password of user [](#__codelineno-60-18) [](#__codelineno-60-19) optional arguments: [](#__codelineno-60-20)   -h, --help        show this help message and exit [](#__codelineno-60-21)   --debug           Enable debug logs for the CLI operations`

##### **1.3.4.1 Install platform services**

`rdaf platform install` command is used to deploy / install RDAF core platform services. Run the below command to view the available CLI options.

`[](#__codelineno-61-1) usage: platform install [-h] --tag TAG [--service SERVICES] [](#__codelineno-61-2) [](#__codelineno-61-3) optional arguments: [](#__codelineno-61-4)   -h, --help          show this help message and exit [](#__codelineno-61-5)   --tag TAG           Tag to use for the docker images of the platform [](#__codelineno-61-6)                       components [](#__codelineno-61-7)   --service SERVICES  Restrict the scope of the command to specific service`

Run the below command to deploy all RDAF core platform services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com)

`[](#__codelineno-62-1) rdaf platform install --tag 3.4.2`

As part of the installation of RDAF core platform services, it creates a default tenant admin user called `admin@cfx.com`

The default password for `admin@cfx.com` is **admin1234**

On first login onto RDAF UI portal, it prompts for resetting the above default password to user's choice.

In order to access RDAF UI portal, open a web browser and type the HAProxy server's IP address if it is a non-HA deployment or HAProxy server's virtual IP address if it is an HA deployment as shown below.

`[](#__codelineno-63-1) https://192.168.125.148`

##### **1.3.4.2 Status check**

Run the below command to see the status of all of the deployed RDAF infrastructure services.

`[](#__codelineno-64-1) rdaf platform status`

[Example Output](#__tabbed_4_1)

`[](#__codelineno-65-1) +--------------------+----------------+-----------+--------------+-------+ [](#__codelineno-65-2) | Name               | Host           | Status    | Container Id | Tag   | [](#__codelineno-65-3) +--------------------+----------------+-----------+--------------+-------+ [](#__codelineno-65-4) | rda_api_server     | 192.168.133.92 | Up 3 days | b2c91b3f5b8d | 3.4.2 | [](#__codelineno-65-5) | rda_api_server     | 192.168.133.93 | Up 3 days | 2c7e6e79e0d1 | 3.4.2 | [](#__codelineno-65-6) | rda_registry       | 192.168.133.92 | Up 3 days | 464161ddae16 | 3.4.2 | [](#__codelineno-65-7) | rda_registry       | 192.168.133.93 | Up 3 days | 946366995e8a | 3.4.2 | [](#__codelineno-65-8) | rda_scheduler      | 192.168.133.92 | Up 3 days | e6ab76d712fa | 3.4.2 | [](#__codelineno-65-9) | rda_scheduler      | 192.168.133.93 | Up 3 days | 93910af6e17e | 3.4.2 | [](#__codelineno-65-10) | rda_collector      | 192.168.133.92 | Up 3 days | 9c6e2a641ece | 3.4.2 | [](#__codelineno-65-11) | rda_collector      | 192.168.133.93 | Up 3 days | 2694023681e0 | 3.4.2 | [](#__codelineno-65-12) | rda_asset_dependen | 192.168.133.92 | Up 3 days | ef475644d1bd | 3.4.2 | [](#__codelineno-65-13) | cy                 |                |           |              |       | [](#__codelineno-65-14) | rda_asset_dependen | 192.168.133.93 | Up 3 days | 6c8570b3bb9c | 3.4.2 | [](#__codelineno-65-15) | cy                 |                |           |              |       | [](#__codelineno-65-16) | rda_identity       | 192.168.133.92 | Up 3 days | eadd3c3d5c8e | 3.4.2 | [](#__codelineno-65-17) | rda_identity       | 192.168.133.93 | Up 3 days | 32b7aca03e4a | 3.4.2 | [](#__codelineno-65-18) | rda_fsm            | 192.168.133.92 | Up 3 days | d553502dad1a | 3.4.2 | [](#__codelineno-65-19) | rda_fsm            | 192.168.133.93 | Up 3 days | 14ae04b1c4d2 | 3.4.2 | [](#__codelineno-65-20) | rda_chat_helper    | 192.168.133.92 | Up 3 days | 302a80076309 | 3.4.2 | [](#__codelineno-65-21) | rda_chat_helper    | 192.168.133.93 | Up 3 days | 601c21a8493d | 3.4.2 | [](#__codelineno-65-22) | cfx-rda-access-    | 192.168.133.92 | Up 3 days | 44e7cc4d1764 | 3.4.2 | [](#__codelineno-65-23) | manager            |                |           |              |       | [](#__codelineno-65-24) | cfx-rda-access-    | 192.168.133.93 | Up 3 days | 688b5aa2c895 | 3.4.2 | [](#__codelineno-65-25) | manager            |                |           |              |       | [](#__codelineno-65-26) +--------------------+----------------+-----------+--------------+-------+` 

##### **1.3.4.3 Upgrade platform services**

Run the below command to upgrade all RDAF core platform services to a newer version.

`[](#__codelineno-66-1) rdaf platform upgrade --tag 3.4.2`

Below are the RDAF core platform services

*   cfx-rda-access-manager
*   cfx-rda-resource-manager
*   cfx-rda-user-preferences
*   portal-backend
*   portal-frontend
*   rda\_api\_server
*   rda\_asm
*   rda\_asset\_dependency
*   rda\_collector
*   rda\_identity
*   rda\_registry
*   rda\_sched\_admin
*   rda\_scheduler

Run the below command to upgrade a specific RDAF core platform service to a newer version.

`[](#__codelineno-67-1) rdaf platform upgrade --service rda_collector --tag 3.4.2`

Tip

Above shown tag version is a sample one and for a reference only, for actual newer versioned tag, please contact CloudFabrix support team at support@cloudfabrix.com

Danger

Please take full configuration and data backup of RDAF platform before any upgrade process. Upgrading RDAF core platform service or services is a disruptive operation which will impact all of the RDAF dependant services and causes a downtime. When RDAF platform is deployed in Production environment, please perform upgrade operation only during a scheduled downtime.

##### **1.3.4.4 Start/Stop platform services**

Run the below commands to start / stop all RDAF core platform services.

`[](#__codelineno-68-1) rdaf platform up [](#__codelineno-68-2) rdaf platform down`

Run the below commands to start / stop a specific RDAF core platform service.

`[](#__codelineno-69-1) rdaf platform up --service rda_collector [](#__codelineno-69-2) rdaf platform down --service rda_collector`

Danger

Stopping and Starting RDAF core platform service or services is a disruptive operation which will impact all of the RDAF dependant services and causes a downtime. When RDAF platform is deployed in Production environment, please perform these operations only during a scheduled downtime.

##### **1.3.4.5 Reset password**

Run the below command to reset the default user's **admin@cfx.com** password to factory default. i.e. **admin1234** and will force the user to reset the default password to tenant admin user's choice.

`[](#__codelineno-70-1) rdaf platform reset-admin-user`

Warning

Use above command option only in a scenario where tenant admin users are not able to access RDAF UI portal because of external IAM (identity and access management) tool such as Active Directory / LDAP / SSO is down or not accessible and default tenant admin user's password is forgotten or lost.

##### **1.3.4.6 Generate SSL Certificates**

Self-signed SSL certificates are used for RDAF infrastructure, core platform services and for RDAF CLI as well. This manual step is not usually needed as it will be run automatically during `rdaf setup` execution.

However, this command is useful to re-generate self-signed SSL certificates and overwrite existing ones if there is a need.

`[](#__codelineno-71-1) rdaf platform generate-certs --overwrite`

After re-generating the SSL certificates, please restart RDAF infrastructure, core platform, application, worker and agent services.

Danger

Re-generating self-signed SSL certificates is a disruptive operation which will impact all of the RDAF dependant services and causes a downtime. When RDAF platform is deployed in Production environment, please perform these operations only during a scheduled downtime.

##### **1.3.4.7 Add new service host**

RDAF platform's application services can be distributed on multiple hosts to distributed the workload and to run them in high-availability mode.

After deploying initial RDAF platform's application services, if there is a need, using the below command, a new RDAF platform's application services host can be added to the configuration after which existing application services can be re-deployed to be run on this new host to distribute the workload.

`[](#__codelineno-72-1) rdaf platform add-service-host --ssh-password <SSH_PASSWORD> <ip-address-or-dns-name>`

#### **1.3.5 rdaf app**

`rdaf app` command is used to deploy and manage RDAF application services. Run the below command to view available CLI options.

The supported application services are below.

*   **OIA:** Operations Intelligence and Analytics (Also known as **AIOps**)
*   **AIA:** Asset Intelligence and Analytics

`[](#__codelineno-73-1) usage: ('app',) [-h] [--debug] {} ... [](#__codelineno-73-2) [](#__codelineno-73-3) Manage the RDAF Apps [](#__codelineno-73-4) [](#__codelineno-73-5) positional arguments: [](#__codelineno-73-6)   {}             commands [](#__codelineno-73-7)     status       Status of the App [](#__codelineno-73-8)     up           Create the App serviceContainers [](#__codelineno-73-9)     down         Delete the App service Containers [](#__codelineno-73-10)     install      Install the App service containers [](#__codelineno-73-11)     upgrade      Upgrade the App service containers [](#__codelineno-73-12)     update-config [](#__codelineno-73-13)                  Updated configurations of one or more components [](#__codelineno-73-14) [](#__codelineno-73-15) optional arguments: [](#__codelineno-73-16)   -h, --help     show this help message and exit [](#__codelineno-73-17)   --debug        Enable debug logs for the CLI operations`

##### **1.3.5.1 Install OIA/AIA services**

`rdaf app install` command is used to deploy / install RDAF OIA/AIA application services. Run the below command to view the available CLI options.

`[](#__codelineno-74-1) usage: ('app',) install [-h] --tag TAG [--service SERVICES] {AIA,OIA} [](#__codelineno-74-2) [](#__codelineno-74-3) positional arguments: [](#__codelineno-74-4)   {AIA,OIA}           Select the APP to act on [](#__codelineno-74-5) [](#__codelineno-74-6) optional arguments: [](#__codelineno-74-7)   -h, --help          show this help message and exit [](#__codelineno-74-8)   --tag TAG           Tag to use for the docker images of the app components [](#__codelineno-74-9)   --service SERVICES  Restrict the scope of the command to specific service`

Run the below command to deploy RDAF **OIA** / **AIA** application services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com)

`[](#__codelineno-75-1) rdaf app install OIA --tag 7.4.2`

##### **1.3.5.2 Start/Stop app services**

Run the below command to start / stop all RDAF application **OIA** services.

`[](#__codelineno-76-1) rdaf app up OIA [](#__codelineno-76-2) rdaf app down OIA`

Run the below command to start / stop all RDAF application **AIA** services.

`[](#__codelineno-77-1) rdaf app up AIA [](#__codelineno-77-2) rdaf app down AIA`

Run the below commands to start / stop a specific RDAF application **OIA** service.

`[](#__codelineno-78-1) rdaf app up OIA --service cfx-rda-alert-ingester [](#__codelineno-78-2) rdaf app down OIA --service cfx-rda-alert-ingester`

Below are the RDAF OIA application services

*   all-alerts-cfx-rda-dataset-caas
*   cfx-rda-alert-ingester
*   cfx-rda-alert-processor
*   cfx-rda-app-builder
*   cfx-rda-app-controller
*   cfx-rda-collaboration
*   cfx-rda-configuration-service
*   cfx-rda-event-consumer
*   cfx-rda-file-browser
*   cfx-rda-ingestion-tracker
*   cfx-rda-irm-service
*   cfx-rda-ml-config
*   cfx-rda-notification-service
*   cfx-rda-reports-registry
*   cfx-rda-smtp-server
*   cfx-rda-webhook-server
*   current-alerts-cfx-rda-dataset-caas

Danger

Stopping and Starting RDAF application OIA / AIA service or services is a disruptive operation which will impact the availability of these application services. When RDAF platform is deployed in Production environment, please perform these operations only during a scheduled downtime.

##### **1.3.5.3 Status check**

Run the below command to see the status of all of the deployed RDAF application services.

`[](#__codelineno-79-1) rdaf app status`

[Example Output](#__tabbed_5_1)

  `[](#__codelineno-80-1)   +--------------------+----------------+-----------+--------------+-------+ [](#__codelineno-80-2)   | Name               | Host           | Status    | Container Id | Tag   | [](#__codelineno-80-3)   +--------------------+----------------+-----------+--------------+-------+ [](#__codelineno-80-4)   | cfx-rda-app-       | 192.168.133.96 | Up 3 days | 133c976d2e64 | 7.4.2 | [](#__codelineno-80-5)   | controller         |                |           |              |       | [](#__codelineno-80-6)   | cfx-rda-app-       | 192.168.133.92 | Up 3 days | fc155ecf6f47 | 7.4.2 | [](#__codelineno-80-7)   | controller         |                |           |              |       | [](#__codelineno-80-8)   | cfx-rda-reports-   | 192.168.133.96 | Up 3 days | e7412d9eb3f1 | 7.4.2 | [](#__codelineno-80-9)   | registry           |                |           |              |       | [](#__codelineno-80-10)   | cfx-rda-reports-   | 192.168.133.92 | Up 3 days | 9bc6ec617744 | 7.4.2 | [](#__codelineno-80-11)   | registry           |                |           |              |       | [](#__codelineno-80-12)   | cfx-rda-           | 192.168.133.96 | Up 3 days | 40859a933dc7 | 7.4.2 | [](#__codelineno-80-13)   | notification-      |                |           |              |       | [](#__codelineno-80-14)   | service            |                |           |              |       | [](#__codelineno-80-15)   | cfx-rda-           | 192.168.133.92 | Up 3 days | 3b2757fe7313 | 7.4.2 | [](#__codelineno-80-16)   | notification-      |                |           |              |       | [](#__codelineno-80-17)   | service            |                |           |              |       | [](#__codelineno-80-18)   | cfx-rda-file-      | 192.168.133.96 | Up 3 days | ac9e1576332c | 7.4.2 | [](#__codelineno-80-19)   | browser            |                |           |              |       | [](#__codelineno-80-20)   | cfx-rda-file-      | 192.168.133.92 | Up 3 days | 3b0332b0a703 | 7.4.2 | [](#__codelineno-80-21)   | browser            |                |           |              |       | [](#__codelineno-80-22)   | cfx-rda-           | 192.168.133.96 | Up 3 days | 6982a9bdebe1 | 7.4.2 | [](#__codelineno-80-23)   | configuration-     |                |           |              |       | [](#__codelineno-80-24)   | service            |                |           |              |       | [](#__codelineno-80-25)   | cfx-rda-           | 192.168.133.92 | Up 3 days | 7ee95287f65f | 7.4.2 | [](#__codelineno-80-26)   | configuration-     |                |           |              |       | [](#__codelineno-80-27)   | service            |                |           |              |       | [](#__codelineno-80-28)   | cfx-rda-alert-     | 192.168.133.96 | Up 3 days | 582d55c8da74 | 7.4.2 | [](#__codelineno-80-29)   | ingester           |                |           |              |       | [](#__codelineno-80-30)   | cfx-rda-alert-     | 192.168.133.92 | Up 3 days | f14ad552ed3e | 7.4.2 | [](#__codelineno-80-31)   | ingester           |                |           |              |       | [](#__codelineno-80-32)   +--------------------+----------------+-----------+--------------+-------+`

##### **1.3.5.4 Upgrade app OIA/AIA services**

Run the below command to upgrade all RDAF **OIA** / **AIA** application services to a newer version.

`[](#__codelineno-81-1) rdaf app upgrade OIA --tag 7.4.2`

`[](#__codelineno-82-1) rdaf app upgrade AIA --tag 7.4.2`

Below are the RDAF OIA application services

*   all-alerts-cfx-rda-dataset-caas
*   cfx-rda-alert-ingester
*   cfx-rda-alert-processor
*   cfx-rda-app-builder
*   cfx-rda-app-controller
*   cfx-rda-collaboration
*   cfx-rda-configuration-service
*   cfx-rda-event-consumer
*   cfx-rda-file-browser
*   cfx-rda-ingestion-tracker
*   cfx-rda-irm-service
*   cfx-rda-ml-config
*   cfx-rda-notification-service
*   cfx-rda-reports-registry
*   cfx-rda-smtp-server
*   cfx-rda-webhook-server
*   current-alerts-cfx-rda-dataset-caas

Run the below command to upgrade a specific RDAF **OIA** application service to a newer version.

`[](#__codelineno-83-1) rdaf app upgrade OIA --service cfx-rda-webhook-server --tag 7.4.2`

Tip

Above shown tag version is a sample one and for a reference only, for actual newer versioned tag, please contact CloudFabrix support team at support@cloudfabrix.com

Danger

Please take full configuration and data backup of RDAF platform before any upgrade process. Upgrading RDAF OIA / AIA application service or services is a disruptive operation which will impact the availability of these services. When RDAF platform is deployed in Production environment, please perform upgrade operation only during a scheduled downtime.

##### **1.3.5.5 Update HAProxy configuration**

Run the below command to update the necessary HAProxy load-balancer configuration for RDAF **OIA** / **AIA** application services.

`[](#__codelineno-84-1) rdaf app update-config OIA`

`[](#__codelineno-85-1) rdaf app update-config AIA`

After deploying the RDAF OIA application services, it is mandatory to run the `rdaf app update-config` which will apply and restart the HAProxy load-balancer service automatically.

#### **1.3.6 rdaf worker**

`rdaf worker` command is used to deploy and manage RDAF worker services. Run the below command to view available CLI options.

`[](#__codelineno-86-1) usage: worker [-h] [--debug] {} ... [](#__codelineno-86-2) [](#__codelineno-86-3) Manage the RDAF Worker [](#__codelineno-86-4) [](#__codelineno-86-5) positional arguments: [](#__codelineno-86-6)   {}               commands [](#__codelineno-86-7)     add-worker-host [](#__codelineno-86-8)                    Add extra worker vm [](#__codelineno-86-9)     status         Status of the RDAF Worker [](#__codelineno-86-10)     up             Create the RDAF Worker Containers [](#__codelineno-86-11)     down           Delete the RDAF Worker Containers [](#__codelineno-86-12)     install        Install the RDAF Worker containers [](#__codelineno-86-13)     upgrade        Upgrade the RDAF Worker containers [](#__codelineno-86-14) [](#__codelineno-86-15) optional arguments: [](#__codelineno-86-16)   -h, --help       show this help message and exit [](#__codelineno-86-17)   --debug          Enable debug logs for the CLI operations`

##### **1.3.6.1 Install worker service(s)**

`rdaf worker install` command is used to deploy / install RDAF worker services. Run the below command to view the available CLI options.

`[](#__codelineno-87-1) usage: worker install [-h] --tag TAG [](#__codelineno-87-2) [](#__codelineno-87-3) optional arguments: [](#__codelineno-87-4)   -h, --help  show this help message and exit [](#__codelineno-87-5)   --tag TAG   Tag to use for the docker images of the worker components`

Run the below command to deploy all RDAF worker services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com)

`[](#__codelineno-88-1) rdaf worker install --tag 3.4.2`

##### **1.3.6.2 Status check**

Run the below command to see the status of all of the deployed RDAF worker services.

`[](#__codelineno-89-1) rdaf worker status`

[Example Output](#__tabbed_6_1)

  `[](#__codelineno-90-1)   +------------+----------------+-----------+--------------+-------+ [](#__codelineno-90-2)   | Name       | Host           | Status    | Container Id | Tag   | [](#__codelineno-90-3)   +------------+----------------+-----------+--------------+-------+ [](#__codelineno-90-4)   | rda_worker | 192.168.133.96 | Up 4 days | bfeb469c3277 | 3.4.2 | [](#__codelineno-90-5)   | rda_worker | 192.168.133.92 | Up 4 days | 43385833db75 | 3.4.2 | [](#__codelineno-90-6)   +------------+----------------+-----------+--------------+-------+`

##### **1.3.6.3 Upgrade worker services**

Run the below command to upgrade all RDAF worker service(s) to a newer version.

`[](#__codelineno-91-1) rdaf worker upgrade --tag 3.4.2`

Tip

Above shown tag version is a sample one and for a reference only, for actual newer versioned tag, please contact CloudFabrix support team at support@cloudfabrix.com

Danger

Upgrading RDAF worker service or services is a disruptive operation which will impact all of the worker jobs. When RDAF platform is deployed in Production environment, please perform upgrade operation only during a scheduled downtime.

##### **1.3.6.4 Start/Stop worker services**

Run the below commands to start / stop all RDAF worker services.

`[](#__codelineno-92-1) rdaf worker up [](#__codelineno-92-2) rdaf worker down`

Danger

Stopping and Starting RDAF worker service(s) is a disruptive operation which will impact all of the worker jobs. When RDAF platform is deployed in Production environment, please perform these operations only during a scheduled downtime.

##### **1.3.6.5 Add new worker host**

RDAF platform's worker services can be distributed on multiple hosts to distributed the workload.

After deploying initial RDAF platform's worker services, if there is a need, using the below command, a new RDAF platform's worker host can be added to the configuration after which new jobs can be run on this new worker host to distribute the workload.

`[](#__codelineno-93-1) rdaf worker add-worker-host --ssh-password <SSH_PASSWORD> <ip-address-or-dns-name>`

### **1.3.7 rdaf prune\_images**

After upgrading the RDAF infrastructure, core platform, application and worker services, run the below command to clean up the un-used docker images. This command helps to clean up and free the disk space on **/var/lib/docker** mount point.

`[](#__codelineno-94-1) rdaf prune_images`

### **1.3.8 rdaf validate**

`rdaf validate` command helps to verify or validate the below two configurations.

*   **values-yaml:** `values.yml` is a configuration file which allows the user to modify RDAF service's parameter(s) based on the deployment requirements. This file resides under **/opt/rdaf/deployment-scripts** directory on RDAF platform VM on which `rdaf setup` was run.

`[](#__codelineno-95-1) rdaf validate values-yaml`

*   **configs:** This command option verifies some of the pre-requisites on all RDAF hosts.

Below are the checks it performs.

*   SSH access and port check
*   Docker is installed or not
*   Docker-Compose is installed or not
*   Firewall ports are opened or not for RDAF services

`[](#__codelineno-96-1) rdaf validate configs`

[Example Output](#__tabbed_7_1)

`[](#__codelineno-97-1) 2022-09-06 00:30:40,660 [rdaf.cmd.validate] INFO     - checking connection for the host 192.168.125.146 [](#__codelineno-97-2) 2022-09-06 00:30:40,701 [rdaf.cmd.validate] INFO     - ssh check for host 192.168.125.146 successful [](#__codelineno-97-3) 2022-09-06 00:30:40,701 [rdaf.cmd.validate] INFO     - checking connection for the host 192.168.125.143 [](#__codelineno-97-4) 2022-09-06 00:30:40,791 [rdaf.cmd.validate] INFO     - ssh check for host 192.168.125.143 successful [](#__codelineno-97-5) 2022-09-06 00:30:40,792 [rdaf.cmd.validate] INFO     - checking connection for the host 192.168.125.149 [](#__codelineno-97-6) .... [](#__codelineno-97-7) 2022-09-06 00:30:40,949 [rdaf.cmd.validate] INFO     - ssh check for host 192.168.125.144 successful [](#__codelineno-97-8) 2022-09-06 00:30:41,112 [rdaf.cmd.validate] INFO     - Docker is installed on host 192.168.125.146 [](#__codelineno-97-9) 2022-09-06 00:30:41,317 [rdaf.cmd.validate] INFO     - Docker is installed on host 192.168.125.143 [](#__codelineno-97-10) .... [](#__codelineno-97-11) 2022-09-06 00:30:42,036 [rdaf.cmd.validate] INFO     - Docker-compose is installed on host 192.168.125.146 [](#__codelineno-97-12) 2022-09-06 00:30:42,189 [rdaf.cmd.validate] INFO     - Docker-compose is installed on host 192.168.125.143 [](#__codelineno-97-13) .... [](#__codelineno-97-14) 2022-09-06 00:30:42,899 [rdaf.cmd.validate] INFO     - port is open 7222 on host 192.168.125.143 of component haproxy [](#__codelineno-97-15) 2022-09-06 00:30:42,900 [rdaf.cmd.validate] INFO     - port is open 9443 on host 192.168.125.143 of component haproxy [](#__codelineno-97-16) 2022-09-06 00:30:42,900 [rdaf.cmd.validate] INFO     - port is open 3307 on host 192.168.125.143 of component haproxy [](#__codelineno-97-17) .... [](#__codelineno-97-18) 2022-09-06 00:30:43,134 [rdaf.cmd.validate] INFO     - port is open 8808 on host 192.168.125.144 of component haproxy [](#__codelineno-97-19) 2022-09-06 00:30:43,364 [rdaf.cmd.validate] INFO     - port is open 4222 on host 192.168.125.143 of component nats [](#__codelineno-97-20) .... [](#__codelineno-97-21) 2022-09-06 00:30:47,060 [rdaf.cmd.validate] INFO     - port is open 9093 on host 192.168.125.144 of component kafka [](#__codelineno-97-22) 2022-09-06 00:30:47,264 [rdaf.cmd.validate] INFO     - port is open 9092 on host 192.168.125.145 of component kafka [](#__codelineno-97-23) 2022-09-06 00:30:47,264 [rdaf.cmd.validate] INFO     - port is open 9093 on host 192.168.125.145 of component kafka [](#__codelineno-97-24) 2022-09-06 00:30:47,521 [rdaf.cmd.validate] INFO     - port is open 6379 on host 192.168.125.143 of component redis [](#__codelineno-97-25) 2022-09-06 00:30:47,763 [rdaf.cmd.validate] INFO     - port is open 6379 on host 192.168.125.144 of component redis [](#__codelineno-97-26) 2022-09-06 00:30:47,974 [rdaf.cmd.validate] INFO     - port is open 6379 on host 192.168.125.145 of component redis [](#__codelineno-97-27) 2022-09-06 00:30:48,222 [rdaf.cmd.validate] INFO     - port is open 26379 on host 192.168.125.143 of component redis-sentinel [](#__codelineno-97-28) 2022-09-06 00:30:48,456 [rdaf.cmd.validate] INFO     - port is open 26379 on host 192.168.125.144 of component redis-sentinel [](#__codelineno-97-29) 2022-09-06 00:30:48,668 [rdaf.cmd.validate] INFO     - port is open 26379 on host 192.168.125.145 of component redis-sentinel`

### **1.3.9 rdaf rdac\_cli**

`rdaf rdac_cli` command allows you to install and upgrade RDA client CLI utility which interacts with RDA Fabric services and operations.

`[](#__codelineno-98-1) rdaf rdac_cli -h`

`[](#__codelineno-99-1) usage: rdac-cli [-h] [--debug] {} ... [](#__codelineno-99-2) [](#__codelineno-99-3) Install RDAC CLI [](#__codelineno-99-4) [](#__codelineno-99-5) positional arguments: [](#__codelineno-99-6)   {}          commands [](#__codelineno-99-7)     install   Install the RDAC CLI [](#__codelineno-99-8)     upgrade   Upgrade the RDAC CLI [](#__codelineno-99-9) [](#__codelineno-99-10) optional arguments: [](#__codelineno-99-11)   -h, --help  show this help message and exit [](#__codelineno-99-12)   --debug     Enable debug logs for the CLI operations`

*   To install RDA client CLI, run the below command

`[](#__codelineno-100-1) rdaf rdac_cli install --tag <tag-name>`

*   To upgrade RDA client CLI version, run the below command

`[](#__codelineno-101-1) rdaf rdac_cli upgrade --tag <tag-name>`

*   Run the below command to see RDA client CLI help and available subcommand options.

`[](#__codelineno-102-1) rdac -h`

[Example Output](#__tabbed_8_1)

`[](#__codelineno-103-1) Run with one of the following commands [](#__codelineno-103-2) [](#__codelineno-103-3)   agent-bots                List all bots registered by agents for the current tenant [](#__codelineno-103-4)   agents                    List all agents for the current tenant [](#__codelineno-103-5)   alert-rules               Alert Rule management commands [](#__codelineno-103-6)   bot-catalog-generation-from-file  Generate bot catalog for given sources [](#__codelineno-103-7)   bot-package               Bot Package management commands [](#__codelineno-103-8)   bots-by-source            List bots available for given sources [](#__codelineno-103-9)   check-credentials         Perform credential check for one or more sources on a worker pod [](#__codelineno-103-10)   checksum                  Compute checksums for pipeline contents locally for a given JSON file [](#__codelineno-103-11)   compare                   Commands to compare different RDA systems using different RDA Config files [](#__codelineno-103-12)   content-to-object         Convert data from a column into objects [](#__codelineno-103-13)   copy-to-objstore          Deploy files specified in a ZIP file to the Object Store [](#__codelineno-103-14)   dashboard                 User defined dashboard management commands [](#__codelineno-103-15)   dashgroup                 User defined dashboard-group management commands [](#__codelineno-103-16)   dataset                   Dataset management commands [](#__codelineno-103-17)   demo                      Demo related commands [](#__codelineno-103-18)   deployment                Service Blueprints (Deployments) management commands [](#__codelineno-103-19)   event-gw-status           List status of all ingestion endpoints at all the event gateways [](#__codelineno-103-20)   evict                     Evict a job from a worker pod [](#__codelineno-103-21)   file-ops                  Perform various operations on local files [](#__codelineno-103-22)   file-to-object            Convert files from a column into objects [](#__codelineno-103-23)   fmt-template              Formatting Templates management commands [](#__codelineno-103-24)   healthcheck               Perform healthcheck on each of the Pods [](#__codelineno-103-25)   invoke-agent-bot          Invoke a bot published by an agent [](#__codelineno-103-26)   jobs                      List all jobs for the current tenant [](#__codelineno-103-27)   logarchive                Logarchive management commands [](#__codelineno-103-28)   object                    RDA Object management commands [](#__codelineno-103-29)   output                    Get the output of a Job using jobid. [](#__codelineno-103-30)   pipeline                  Pipeline management commands [](#__codelineno-103-31)   playground                Start Webserver to access RDA Playground [](#__codelineno-103-32)   pods                      List all pods for the current tenant [](#__codelineno-103-33)   project                   Project management commands. Projects can be used to link different tenants / projects from this RDA Fabric or a remote RDA Fabric. [](#__codelineno-103-34)   pstream                   Persistent Stream management commands [](#__codelineno-103-35)   purge-outputs             Purge outputs of completed jobs [](#__codelineno-103-36)   read-stream               Read messages from an RDA stream [](#__codelineno-103-37)   reco-engine               Recommendation Engine management commands [](#__codelineno-103-38)   restore                   Commands to restore backed-up artifacts to an RDA Platform [](#__codelineno-103-39)   run                       Run a pipeline on a worker pod [](#__codelineno-103-40)   run-get-output            Run a pipeline on a worker, and Optionally, wait for the completion, get the final output [](#__codelineno-103-41)   schedule                  Pipeline execution schedule management commands [](#__codelineno-103-42)   schema                    Dataset Model Schema management commands [](#__codelineno-103-43)   secret                    Credentials (Secrets) management commands [](#__codelineno-103-44)   set-pod-log-level         Update the logging level for a given RDA Pod. [](#__codelineno-103-45)   shell                     Start RDA Client interactive shell [](#__codelineno-103-46)   site-profile              Site Profile management commands [](#__codelineno-103-47)   site-summary              Show summary by Site and Overall [](#__codelineno-103-48)   stack                     Application Dependency Mapping (Stack) management commands [](#__codelineno-103-49)   staging-area              Staging Area based data ingestion management commands [](#__codelineno-103-50)   subscription              Show current CloudFabrix RDA subscription details [](#__codelineno-103-51)   synthetics                Data synthesizing management commands [](#__codelineno-103-52)   verify-pipeline           Verify the pipeline on a worker pod [](#__codelineno-103-53)   viz                       Visualize data from a file within the console (terminal) [](#__codelineno-103-54)   watch                     Commands to watch various streams such sas trace, logs and change notifications by microservices [](#__codelineno-103-55)   web-server                Start Webserver to access RDA Client data using REST APIs [](#__codelineno-103-56)   worker-obj-info           List all worker pods with their current Object Store configuration [](#__codelineno-103-57)   write-stream              Write data to the specified stream [](#__codelineno-103-58) [](#__codelineno-103-59) positional arguments: [](#__codelineno-103-60)   command     RDA subcommand to run [](#__codelineno-103-61) [](#__codelineno-103-62) optional arguments: [](#__codelineno-103-63)   -h, --help  show this help message and exit`

Tip

Please refer [RDA Client CLI Usage](https://bot-docs.cloudfabrix.io/beginners_guide/rdac/#3-list-of-all-rda-cli-sub-commands)
 for detailed information.

### **1.3.10 rdaf backup**

Using `rdaf backup` command, RDAF configuration and data can be backed up periodically which can be used to restore in case of a recovery scenario.

`rdaf backup -h`

`[](#__codelineno-104-1) usage: backup [--insecure] [-h] [--debug] --dest-dir BACKUP_DEST_DIR [](#__codelineno-104-2)               [--create-tar] [--service SERVICES] [](#__codelineno-104-3) [](#__codelineno-104-4) Backup the RDAF platform [](#__codelineno-104-5) [](#__codelineno-104-6) optional arguments: [](#__codelineno-104-7)   --insecure            Ignore SSL certificate issues when communicating with [](#__codelineno-104-8)                         various hosts [](#__codelineno-104-9)   -h, --help            show this help message and exit [](#__codelineno-104-10)   --debug               Enable debug logs for the CLI operations [](#__codelineno-104-11)   --dest-dir BACKUP_DEST_DIR [](#__codelineno-104-12)                         Directory into which the backup will be stored [](#__codelineno-104-13)   --create-tar          Creates a tar file for the backed up data [](#__codelineno-104-14)   --service SERVICES    Backup only the specified components`

For `--service` is an optional argument, and below are the supported options, when specified, respective service's configuration and data will be backed up.

*   **haproxy** (configuration backup)
*   **mariadb** (configuration and DB backup)
*   **minio** (configuration and data backup)
*   **opensearch** (configuration and index backup)
*   **kafka** (configuration and data backup)
*   **zookeeper** (configuration and data backup)
*   **redis** (configuration backup)
*   **config** (system configuration such as rdaf.cfg, values.yml etc and certificates backup)

When `--service` option is not specified, all of the above service's configuration and data will be backed up.

Run the below command to take RDAF system's full configuration and data backup.

`rdaf backup --dest-dir /opt/backup --create-tar`

Tip

Please make sure to pre-create `/opt/backup` folder or a local or an NFS mount point and provide appropriate user permissions.

``[](#__codelineno-105-1) sudo mkdir -p /opt/backup && sudo chown -R `id -u`:`id -g` /opt/backup``

**Note:** For RDAF platform's configuration and application data backup, it is a pre-requisite to mount an NFS volume on all of the VMs. It is used to store the backup data and for restore using RDAF CLI tool.

Run the below command to take specific service's configuration and data backup.

`[](#__codelineno-106-1) rdaf backup --dest-dir /opt/backup --create-tar --service mariadb`

`[](#__codelineno-107-1) rdaf backup --dest-dir /opt/backup --create-tar --service minio`

`[](#__codelineno-108-1) rdaf backup --dest-dir /opt/backup --create-tar --service opensearch`

Run the below command to take more than one service's configuration and data backup.

`[](#__codelineno-109-1) rdaf backup --dest-dir /opt/backup --create-tar --service mariadb --service minio --service opensearch`

Warning

Though RDAF CLI takes backup of complete configuration and application data, it does not take backup of the OS (RHEL / Ubuntu) on which the RDA Fabric services are deployed. It is recommended to use 3rd party tools like Veeam, HP Dataprotect, Cohesity, Netbackup etc. to take full VM level backup on periodic basis.

3rd party VM level backup need to be used to recover RDAF VMs if OS is unable to boot RHEL / Ubuntu OS.

### **1.3.11 rdaf restore**

Using `rdaf restore` command, RDAF configuration and data can be restored from the previously taken backup.

Warning

While restoring RDAF services data from the backup, please make sure to stop both application and platform services.

`[](#__codelineno-110-1) rdaf app down <OIA/AIA>`

`[](#__codelineno-111-1) rdaf platform down`

For restoring the below service's data from the backup, please make sure their service is up and running.

`mariadb` `minio` `opensearch`

Below command shows the above service's running status.

`[](#__codelineno-112-1) rdaf infra status`

Below command shows the above service's functional status.

`[](#__codelineno-113-1) rdaf infra healthcheck`

`rdaf restore -h`

`[](#__codelineno-114-1) usage: restore [--insecure] [-h] [--debug] [--no-prompt] [--service SERVICES] [](#__codelineno-114-2)                (--from-dir BACKUP_SRC_DIR | --from-tar BACKUP_SRC_TAR) [](#__codelineno-114-3) [](#__codelineno-114-4) Restore the RDAF platform from a previously backed up state [](#__codelineno-114-5) [](#__codelineno-114-6) optional arguments: [](#__codelineno-114-7)   --insecure            Ignore SSL certificate issues when communicating with [](#__codelineno-114-8)                         various hosts [](#__codelineno-114-9)   -h, --help            show this help message and exit [](#__codelineno-114-10)   --debug               Enable debug logs for the CLI operations [](#__codelineno-114-11)   --no-prompt           Don't prompt for inputs [](#__codelineno-114-12)   --service SERVICES    Restore only the specified components [](#__codelineno-114-13)   --from-dir BACKUP_SRC_DIR [](#__codelineno-114-14)                         The directory which contains the backed up [](#__codelineno-114-15)                         installation state [](#__codelineno-114-16)   --from-tar BACKUP_SRC_TAR [](#__codelineno-114-17)                         The tar.gz file which contains the backed up [](#__codelineno-114-18)                         installation state`

For `--service` is an optional argument, and below are the supported options, when specified, respective service's configuration and data will be restored.

*   **haproxy** (configuration backup)
*   **mariadb** (configuration and DB backup)
*   **minio** (configuration and data backup)
*   **opensearch** (configuration and index backup)
*   **kafka** (configuration and data backup)
*   **zookeeper** (configuration and data backup)
*   **redis** (configuration backup)
*   **config** (system configuration such as rdaf.cfg, values.yml etc and certificates backup)

When `--service` option is not specified, all of the above service's configuration and data will be restored.

When the backup was taken **without** `--create-tar` option, please use `--from-dir` option and specify the backup folder as shown below.

Run the below command to restore RDAF system's full configuration and data from the backup folder.

`[](#__codelineno-115-1) rdaf restore --from-dir /opt/backup/2022-11-25-1669346503.565267`

When the backup was taken **with** `--create-tar` option, please use `--from-tar` option and specify the backup tar file path as shown below.

Run the below command to restore RDAF system's full configuration and data from the backup tar file.

`[](#__codelineno-116-1) rdaf restore --from-tar /opt/backup/2022-11-25-1669346503.565267/rdaf-backup-2022-11-25-1669346503.565267.tar.gz`

Run the below command to restore **specific service's configuration and data** from the **backup folder**.

`[](#__codelineno-117-1) rdaf restore --from-dir /opt/backup/2022-11-25-1669346503.565267 --service mariadb`

`[](#__codelineno-118-1) rdaf restore --from-dir /opt/backup/2022-11-25-1669346503.565267 --service minio`

`[](#__codelineno-119-1) rdaf restore --from-dir /opt/backup/2022-11-25-1669346503.565267 --service opensearch`

`[](#__codelineno-120-1) rdaf restore --from-dir /opt/backup/2022-11-25-1669346503.565267 --service config`

Run the below command to restore **more than one service's configuration and data** from the **backup folder**.

`[](#__codelineno-121-1) rdaf restore --from-dir /opt/backup/2022-11-25-1669346503.565267 --service mariadb --service minio`

Run the below command to restore **specific service's configuration and data** from the **backup tar file**.

`[](#__codelineno-122-1) rdaf restore --from-tar /opt/backup/2022-11-25-1669346503.565267/rdaf-backup-2022-11-25-1669346503.565267.tar.gz --service mariadb`

Run the below command to restore **more than one service's configuration and data** from the **backup tar file**.

`[](#__codelineno-123-1) rdaf restore --from-tar /opt/backup/2022-11-25-1669346503.565267/rdaf-backup-2022-11-25-1669346503.565267.tar.gz --service mariadb --service minio`

### **1.3.12 rdaf log\_monitoring**

`rdaf log_monitoring` command is used to deploy and manage log monitoring services, through which the RDAF infrastructure, platform, application, and worker service logs are streamed in real-time.

As part of the log monitoring services, it installs the following services:

*   **Fluentbit:** It is a log shipping agent that streams the logs in real-time and ingests them into the `Logstash` service.
*   **Logstash:** It is a log processing agent that normalizes and extracts key attributes from log messages, such as timestamp, severity, process name, process function, container name, etc., before ingesting them into an index store service for analytics and visualization.

Run the below command to view available CLI options.

`[](#__codelineno-124-1) rdaf log_monitoring`

`[](#__codelineno-125-1) usage: log_monitoring [-h] [--debug] [](#__codelineno-125-2)                       {upgrade,install,status,up,down,start,stop} ... [](#__codelineno-125-3) [](#__codelineno-125-4) Manage the RDAF log monitoring [](#__codelineno-125-5) [](#__codelineno-125-6) positional arguments: [](#__codelineno-125-7)   {upgrade,install,status,up,down,start,stop} [](#__codelineno-125-8)                         commands [](#__codelineno-125-9)     upgrade             Upgrade log monitoring components [](#__codelineno-125-10)     install             Install log monitoring components [](#__codelineno-125-11)     status              Status of the RDAF log monitoring [](#__codelineno-125-12)     up                  Create the RDAF log monitoring Containers [](#__codelineno-125-13)     down                Delete the RDAF log monitoring Containers [](#__codelineno-125-14)     start               Start the RDAF log monitoring Containers [](#__codelineno-125-15)     stop                Stop the RDAF log monitoring Containers [](#__codelineno-125-16) [](#__codelineno-125-17) optional arguments: [](#__codelineno-125-18)   -h, --help            show this help message and exit [](#__codelineno-125-19)   --debug               Enable debug logs for the CLI operations`

#### **1.3.12.1 Install Log Monitoring**

`rdaf log_monitoring install` command is used to deploy / install RDAF log monitoring services. Run the below command to view the available CLI options.

`[](#__codelineno-126-1) rdaf log_monitoring install`

`[](#__codelineno-127-1) usage: log_monitoring install [-h] --log-monitoring-host LOG_MONITORING_HOST [](#__codelineno-127-2)                               --tag TAG [--no-prompt] [](#__codelineno-127-3) log_monitoring install: error: the following arguments are required: --log-monitoring-host, --tag`

To deploy all RDAF log monitoring services, execute the following command. Please note that it is mandatory to specify the host for the **Logstash** service deployment using the `--log-monitoring-host` option.

Note

Below shown **Logstash** host ip address is for a reference only. For the latest log monitoring services tag, please contact CloudFabrix support team at support@cloudfabrix.com.

`[](#__codelineno-128-1) rdaf log_monitoring install --tag 1.0.2 --log-monitoring-host 192.168.125.52`

[Example Output](#__tabbed_9_1)

`[](#__codelineno-129-1) {"status":"CREATED","message":"'rdaf-log-monitoring' created."} [](#__codelineno-129-2) {"status":"CREATED","message":"'role-log-monitoring' created."} [](#__codelineno-129-3) {"status":"OK","message":"'rdaf-log-monitoring' updated."} [](#__codelineno-129-4) {"status":"CREATED","message":"'role-log-monitoring' created."} [](#__codelineno-129-5) { [](#__codelineno-129-6)   "retention_days": 15, [](#__codelineno-129-7)   "timestamp": "@timestamp", [](#__codelineno-129-8)   "search_case_insensitive": true, [](#__codelineno-129-9)   "_settings": { [](#__codelineno-129-10)     "number_of_shards": 3, [](#__codelineno-129-11)     "number_of_replicas": 1, [](#__codelineno-129-12)     "refresh_interval": "60s" [](#__codelineno-129-13)   } [](#__codelineno-129-14) } [](#__codelineno-129-15) Persistent stream saved. [](#__codelineno-129-16) 2023-11-02 05:04:08,842 [rdaf.component.haproxy] INFO     - Updated HAProxy configuration at /opt/rdaf/config/haproxy/haproxy.cfg on 192.168.125.53 [](#__codelineno-129-17) ... [](#__codelineno-129-18) ... [](#__codelineno-129-19) [+] Running 1/1 [](#__codelineno-129-20)  ⠿ Container fluent-bit-fluentbit-1  Started                                                                                                                                            0.4s [](#__codelineno-129-21) 2023-11-02 05:06:05,138 [rdaf.component.log_monitoring] INFO     - Restarting logstash services on host 192.168.125.53 [](#__codelineno-129-22) [+] Running 1/1 [](#__codelineno-129-23)  ⠿ Container logstash-logstash-1  Started                                                                                                                                               0.4s [](#__codelineno-129-24) 2023-11-02 05:06:05,617 [rdaf.component.log_monitoring] INFO     - Restarting fluentbit services on host 192.168.125.53 [](#__codelineno-129-25) [+] Running 1/1 [](#__codelineno-129-26)  ⠿ Container fluent-bit-fluentbit-1  Started                                                                                                                                           10.8s [](#__codelineno-129-27) 2023-11-02 05:06:16,488 [rdaf.component.minio] INFO     - configuring minio services logs [](#__codelineno-129-28) Successfully applied new settings. [](#__codelineno-129-29) Successfully applied new settings. [](#__codelineno-129-30) 2023-11-02 05:06:16,936 [rdaf.component.log_monitoring] INFO     - Successfully installed and configured rdaf log streaming`

#### **1.3.12.2 Status check**

Run the below command to see the status of all of the deployed RDAF log monitoring services.

`[](#__codelineno-130-1) rdaf log_monitoring status`

[Example Output](#__tabbed_10_1)

`[](#__codelineno-131-1) +---------------------+----------------------+---------------------------+-------------------------+---------+ [](#__codelineno-131-2) | Name                | Host                 | Status                    | Container Id            | Tag     | [](#__codelineno-131-3) +---------------------+----------------------+---------------------------+-------------------------+---------+ [](#__codelineno-131-4) | logstash            | 192.168.125.53       | Up About a minute         | 62b3b7c81472            | 1.0.2   | [](#__codelineno-131-5) | fluentbit           | 192.168.125.53       | Up About a minute         | c5f8a6f340b3            | 1.0.2   | [](#__codelineno-131-6) +---------------------+----------------------+---------------------------+-------------------------+---------+`

#### **1.3.12.3 Upgrade Log Monitoring**

Run the below command to upgrade all RDAF log monitoring to a newer version.

`[](#__codelineno-132-1) rdaf log_monitoring upgrade --tag <new-tag-version>`

#### **1.3.12.4 Restart Log Monitoring services**

**Restarting the log monitoring service using `rdaf` CLI commands.**

**a**) **To Stop**

Run the below command to **Stop** all RDAF log monitoring services.

`[](#__codelineno-133-1) rdaf log_monitoring down`

[Example Output](#__tabbed_11_1)

`[](#__codelineno-134-1) --------------------------------------------------------------------------------------------------------------------------- [](#__codelineno-134-2) 2023-11-02 05:20:53,313 [rdaf.component.log_monitoring] INFO     - Deleting logstash service on host 192.168.125.53 [](#__codelineno-134-3) [+] Running 1/1  ⠿ Container logstash-logstash-1  Stopped                                                                                                                                               0.3s [](#__codelineno-134-4) Going to remove logstash-logstash-1 [](#__codelineno-134-5) [+] Running 1/0  ⠿ Container logstash-logstash-1  Removed                                                                                                                                               0.0s [](#__codelineno-134-6) 2023-11-02 05:20:53,639 [rdaf.component.log_monitoring] INFO     - Deleting fluent-bit service on host 192.168.125.53 [](#__codelineno-134-7) [+] Running 1/1  ⠿ Container fluent-bit-fluentbit-1  Stopped                                                                                                                                           10.8s [](#__codelineno-134-8) Going to remove fluent-bit-fluentbit-1 [](#__codelineno-134-9) [+] Running 1/0  ⠿ Container fluent-bit-fluentbit-1  Removed [](#__codelineno-134-10) [](#__codelineno-134-11) ---------------------------------------------------------------------------------------------------------------------------`

**b**) **To Start**

Run the below command to **Start** all RDAF log monitoring services.

`[](#__codelineno-135-1) rdaf log_monitoring up`

[Example Output](#__tabbed_12_1)

`[](#__codelineno-136-1) --------------------------------------------------------------------------------------------------------------------------- [](#__codelineno-136-2) 2023-11-02 05:21:33,355 [rdaf.component.log_monitoring] INFO     - Creating logstash services on host 192.168.125.53 [](#__codelineno-136-3) [+] Running 1/1 [](#__codelineno-136-4)  ⠿ Container logstash-logstash-1  Started                                                                                                                                               0.2s [](#__codelineno-136-5) 2023-11-02 05:21:33,641 [rdaf.component.log_monitoring] INFO     - Creating fluent-bit services on host 192.168.125.53 [](#__codelineno-136-6) [+] Running 1/1 [](#__codelineno-136-7)  ⠿ Container fluent-bit-fluentbit-1  Started  [](#__codelineno-136-8) [](#__codelineno-136-9) ---------------------------------------------------------------------------------------------------------------------------`

#### **1.3.12.5 Add Log Monitoring dashboard**

Login to RDAF UI portal as MSP admin user.

Go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Dashboards** --> **User Dashboards** --> Click on **Add** and create a new dashboard by copying the below Dashboard configuration for RDAF log monitoring services.

``[](#__codelineno-137-1) { [](#__codelineno-137-2)     "name": "rdaf-platform-log-analytics", [](#__codelineno-137-3)     "label": "RDAF Platform Logs", [](#__codelineno-137-4)     "description": "RDAF Platform service's log analysis dashboard", [](#__codelineno-137-5)     "version": "23.01.14.1", [](#__codelineno-137-6)     "enabled": true, [](#__codelineno-137-7)     "dashboard_style": "tabbed", [](#__codelineno-137-8)     "status_poller": { [](#__codelineno-137-9)         "stream": "rdaf_services_logs", [](#__codelineno-137-10)         "frequency": 15, [](#__codelineno-137-11)         "columns": [ [](#__codelineno-137-12)             "@timestamp" [](#__codelineno-137-13)         ], [](#__codelineno-137-14)         "sorting": [ [](#__codelineno-137-15)             { [](#__codelineno-137-16)                 "@timestamp": "desc" [](#__codelineno-137-17)             } [](#__codelineno-137-18)         ], [](#__codelineno-137-19)         "query": "`@timestamp` is after '${timestamp}'", [](#__codelineno-137-20)         "defaults": { [](#__codelineno-137-21)             "@timestamp": "$UTCNOW" [](#__codelineno-137-22)         }, [](#__codelineno-137-23)         "action": "refresh" [](#__codelineno-137-24)     }, [](#__codelineno-137-25)     "dashboard_filters": { [](#__codelineno-137-26)         "time_filter": true, [](#__codelineno-137-27)         "columns_filter": [ [](#__codelineno-137-28)             { [](#__codelineno-137-29)                 "id": "@timestamp", [](#__codelineno-137-30)                 "label": "Timestamp", [](#__codelineno-137-31)                 "type": "DATETIME" [](#__codelineno-137-32)             }, [](#__codelineno-137-33)             { [](#__codelineno-137-34)                 "id": "service_name", [](#__codelineno-137-35)                 "label": "Service Name", [](#__codelineno-137-36)                 "type": "TEXT" [](#__codelineno-137-37)             }, [](#__codelineno-137-38)             { [](#__codelineno-137-39)                 "id": "service_category", [](#__codelineno-137-40)                 "label": "Service Category", [](#__codelineno-137-41)                 "type": "TEXT" [](#__codelineno-137-42)             }, [](#__codelineno-137-43)             { [](#__codelineno-137-44)                 "id": "log_severity", [](#__codelineno-137-45)                 "label": "Log Severity", [](#__codelineno-137-46)                 "type": "TEXT" [](#__codelineno-137-47)             }, [](#__codelineno-137-48)             { [](#__codelineno-137-49)                 "id": "log", [](#__codelineno-137-50)                 "label": "Log Message", [](#__codelineno-137-51)                 "type": "TEXT" [](#__codelineno-137-52)             }, [](#__codelineno-137-53)             { [](#__codelineno-137-54)                 "id": "log.text", [](#__codelineno-137-55)                 "label": "Log Message Text", [](#__codelineno-137-56)                 "type": "SIMPLE_TEXT" [](#__codelineno-137-57)             }, [](#__codelineno-137-58)             { [](#__codelineno-137-59)                 "id": "process_name", [](#__codelineno-137-60)                 "label": "Process Name", [](#__codelineno-137-61)                 "type": "TEXT" [](#__codelineno-137-62)             }, [](#__codelineno-137-63)             { [](#__codelineno-137-64)                 "id": "process_function", [](#__codelineno-137-65)                 "label": "Process Function", [](#__codelineno-137-66)                 "type": "TEXT" [](#__codelineno-137-67)             }, [](#__codelineno-137-68)             { [](#__codelineno-137-69)                 "id": "thread_id", [](#__codelineno-137-70)                 "label": "Thread ID", [](#__codelineno-137-71)                 "type": "TEXT" [](#__codelineno-137-72)             }, [](#__codelineno-137-73)             { [](#__codelineno-137-74)                 "id": "k8s_pod_name", [](#__codelineno-137-75)                 "label": "POD Name", [](#__codelineno-137-76)                 "type": "TEXT" [](#__codelineno-137-77)             }, [](#__codelineno-137-78)             { [](#__codelineno-137-79)                 "id": "k8s_container_name", [](#__codelineno-137-80)                 "label": "Container Name", [](#__codelineno-137-81)                 "type": "TEXT" [](#__codelineno-137-82)             } [](#__codelineno-137-83)         ], [](#__codelineno-137-84)         "group_filters": [ [](#__codelineno-137-85)             { [](#__codelineno-137-86)                 "stream": "rdaf_services_logs", [](#__codelineno-137-87)                 "title": "Log Severity", [](#__codelineno-137-88)                 "group_by": [ [](#__codelineno-137-89)                     "log_severity" [](#__codelineno-137-90)                 ], [](#__codelineno-137-91)                 "ts_column": "@timestamp", [](#__codelineno-137-92)                 "agg": "value_count", [](#__codelineno-137-93)                 "column": "_id", [](#__codelineno-137-94)                 "type": "int" [](#__codelineno-137-95)             }, [](#__codelineno-137-96)             { [](#__codelineno-137-97)                 "stream": "rdaf_services_logs", [](#__codelineno-137-98)                 "title": "Service Name", [](#__codelineno-137-99)                 "group_by": [ [](#__codelineno-137-100)                     "service_name" [](#__codelineno-137-101)                 ], [](#__codelineno-137-102)                 "ts_column": "@timestamp", [](#__codelineno-137-103)                 "limit": 50, [](#__codelineno-137-104)                 "agg": "value_count", [](#__codelineno-137-105)                 "column": "_id", [](#__codelineno-137-106)                 "type": "int" [](#__codelineno-137-107)             }, [](#__codelineno-137-108)             { [](#__codelineno-137-109)                 "stream": "rdaf_services_logs", [](#__codelineno-137-110)                 "title": "Service Category", [](#__codelineno-137-111)                 "group_by": [ [](#__codelineno-137-112)                     "service_category" [](#__codelineno-137-113)                 ], [](#__codelineno-137-114)                 "ts_column": "@timestamp", [](#__codelineno-137-115)                 "agg": "value_count", [](#__codelineno-137-116)                 "column": "_id", [](#__codelineno-137-117)                 "type": "int" [](#__codelineno-137-118)             }, [](#__codelineno-137-119)             { [](#__codelineno-137-120)                 "stream": "rdaf_services_logs", [](#__codelineno-137-121)                 "title": "POD Name", [](#__codelineno-137-122)                 "group_by": [ [](#__codelineno-137-123)                     "k8s_pod_name" [](#__codelineno-137-124)                 ], [](#__codelineno-137-125)                 "ts_column": "@timestamp", [](#__codelineno-137-126)                 "agg": "value_count", [](#__codelineno-137-127)                 "limit": 200, [](#__codelineno-137-128)                 "column": "_id", [](#__codelineno-137-129)                 "type": "int" [](#__codelineno-137-130)             } [](#__codelineno-137-131)         ] [](#__codelineno-137-132)     }, [](#__codelineno-137-133)     "dashboard_sections": [ [](#__codelineno-137-134)         { [](#__codelineno-137-135)             "title": "Overall Summary", [](#__codelineno-137-136)             "show_filter": true, [](#__codelineno-137-137)             "widgets": [ [](#__codelineno-137-138)                 { [](#__codelineno-137-139)                     "title": "Log Severity Trend", [](#__codelineno-137-140)                     "widget_type": "timeseries", [](#__codelineno-137-141)                     "stream": "rdaf_services_logs", [](#__codelineno-137-142)                     "ts_column": "@timestamp", [](#__codelineno-137-143)                     "max_width": 12, [](#__codelineno-137-144)                     "height": 3, [](#__codelineno-137-145)                     "min_width": 12, [](#__codelineno-137-146)                     "chartProperties": { [](#__codelineno-137-147)                         "yAxisLabel": "Count", [](#__codelineno-137-148)                         "xAxisLabel": null, [](#__codelineno-137-149)                         "legendLocation": "bottom" [](#__codelineno-137-150)                     }, [](#__codelineno-137-151)                     "interval": "15Min", [](#__codelineno-137-152)                     "group_by": [ [](#__codelineno-137-153)                         "log_severity" [](#__codelineno-137-154)                     ], [](#__codelineno-137-155)                     "series_spec": [ [](#__codelineno-137-156)                         { [](#__codelineno-137-157)                             "column": "log_severity", [](#__codelineno-137-158)                             "agg": "value_count", [](#__codelineno-137-159)                             "type": "int" [](#__codelineno-137-160)                         } [](#__codelineno-137-161)                     ], [](#__codelineno-137-162)                     "widget_id": "06413884" [](#__codelineno-137-163)                 }, [](#__codelineno-137-164)                 { [](#__codelineno-137-165)                     "widget_type": "pie_chart", [](#__codelineno-137-166)                     "title": "Logs by Severity", [](#__codelineno-137-167)                     "stream": "rdaf_services_logs", [](#__codelineno-137-168)                     "ts_column": "@timestamp", [](#__codelineno-137-169)                     "column": "_id", [](#__codelineno-137-170)                     "agg": "value_count", [](#__codelineno-137-171)                     "group_by": [ [](#__codelineno-137-172)                         "log_severity" [](#__codelineno-137-173)                     ], [](#__codelineno-137-174)                     "type": "str", [](#__codelineno-137-175)                     "style": { [](#__codelineno-137-176)                         "color-map": { [](#__codelineno-137-177)                             "ERROR": [ [](#__codelineno-137-178)                                 "#ef5350", [](#__codelineno-137-179)                                 "#ffffff" [](#__codelineno-137-180)                             ], [](#__codelineno-137-181)                             "WARNING": [ [](#__codelineno-137-182)                                 "#FFA726", [](#__codelineno-137-183)                                 "#ffffff" [](#__codelineno-137-184)                             ], [](#__codelineno-137-185)                             "INFO": [ [](#__codelineno-137-186)                                 "#388e3c", [](#__codelineno-137-187)                                 "#ffffff" [](#__codelineno-137-188)                             ], [](#__codelineno-137-189)                             "DEBUG": [ [](#__codelineno-137-190)                                 "#000000", [](#__codelineno-137-191)                                 "#ffffff" [](#__codelineno-137-192)                             ], [](#__codelineno-137-193)                             "UNKNOWN": [ [](#__codelineno-137-194)                                 "#bcaaa4", [](#__codelineno-137-195)                                 "#ffffff" [](#__codelineno-137-196)                             ] [](#__codelineno-137-197)                         } [](#__codelineno-137-198)                     }, [](#__codelineno-137-199)                     "min_width": 4, [](#__codelineno-137-200)                     "height": 4, [](#__codelineno-137-201)                     "max_width": 4, [](#__codelineno-137-202)                     "widget_id": "b2ffa8e9" [](#__codelineno-137-203)                 }, [](#__codelineno-137-204)                 { [](#__codelineno-137-205)                     "widget_type": "pie_chart", [](#__codelineno-137-206)                     "title": "Logs by RDA Host IP", [](#__codelineno-137-207)                     "stream": "rdaf_services_logs", [](#__codelineno-137-208)                     "ts_column": "@timestamp", [](#__codelineno-137-209)                     "column": "_id", [](#__codelineno-137-210)                     "agg": "value_count", [](#__codelineno-137-211)                     "group_by": [ [](#__codelineno-137-212)                         "host" [](#__codelineno-137-213)                     ], [](#__codelineno-137-214)                     "type": "str", [](#__codelineno-137-215)                     "min_width": 4, [](#__codelineno-137-216)                     "height": 4, [](#__codelineno-137-217)                     "max_width": 4, [](#__codelineno-137-218)                     "widget_id": "a4f2d8bd" [](#__codelineno-137-219)                 }, [](#__codelineno-137-220)                 { [](#__codelineno-137-221)                     "widget_type": "pie_chart", [](#__codelineno-137-222)                     "title": "Logs by Service Category", [](#__codelineno-137-223)                     "stream": "rdaf_services_logs", [](#__codelineno-137-224)                     "ts_column": "@timestamp", [](#__codelineno-137-225)                     "column": "_id", [](#__codelineno-137-226)                     "agg": "value_count", [](#__codelineno-137-227)                     "group_by": [ [](#__codelineno-137-228)                         "service_category" [](#__codelineno-137-229)                     ], [](#__codelineno-137-230)                     "type": "str", [](#__codelineno-137-231)                     "min_width": 4, [](#__codelineno-137-232)                     "height": 4, [](#__codelineno-137-233)                     "max_width": 4, [](#__codelineno-137-234)                     "widget_id": "89ac5ce9" [](#__codelineno-137-235)                 }, [](#__codelineno-137-236)                 { [](#__codelineno-137-237)                     "widget_type": "pie_chart", [](#__codelineno-137-238)                     "title": "Logs by Service Name", [](#__codelineno-137-239)                     "stream": "rdaf_services_logs", [](#__codelineno-137-240)                     "ts_column": "@timestamp", [](#__codelineno-137-241)                     "column": "_id", [](#__codelineno-137-242)                     "agg": "value_count", [](#__codelineno-137-243)                     "group_by": "service_name", [](#__codelineno-137-244)                     "type": "int", [](#__codelineno-137-245)                     "min_width": 4, [](#__codelineno-137-246)                     "height": 4, [](#__codelineno-137-247)                     "max_width": 4, [](#__codelineno-137-248)                     "widget_id": "4b267fce" [](#__codelineno-137-249)                 } [](#__codelineno-137-250)             ] [](#__codelineno-137-251)         }, [](#__codelineno-137-252)         { [](#__codelineno-137-253)             "title": "App Services", [](#__codelineno-137-254)             "show_filter": true, [](#__codelineno-137-255)             "widgets": [ [](#__codelineno-137-256)                 { [](#__codelineno-137-257)                     "widget_type": "tabular", [](#__codelineno-137-258)                     "title": "Log Messages", [](#__codelineno-137-259)                     "stream": "rdaf_services_logs", [](#__codelineno-137-260)                     "extra_filter": "service_category in ['rda_app_svcs', 'rda_pfm_svcs']", [](#__codelineno-137-261)                     "ts_column": "@timestamp", [](#__codelineno-137-262)                     "sorting": [ [](#__codelineno-137-263)                         { [](#__codelineno-137-264)                             "@timestamp": "desc" [](#__codelineno-137-265)                         } [](#__codelineno-137-266)                     ], [](#__codelineno-137-267)                     "columns": { [](#__codelineno-137-268)                         "@timestamp": { [](#__codelineno-137-269)                             "title": "Timestamp", [](#__codelineno-137-270)                             "type": "DATETIME" [](#__codelineno-137-271)                         }, [](#__codelineno-137-272)                         "state_color2": { [](#__codelineno-137-273)                             "type": "COLOR-MAP", [](#__codelineno-137-274)                             "source-column": "log_severity", [](#__codelineno-137-275)                             "color-map": { [](#__codelineno-137-276)                                 "INFO": "#388e3c", [](#__codelineno-137-277)                                 "ERROR": "#ef5350", [](#__codelineno-137-278)                                 "WARNING": "#ffa726", [](#__codelineno-137-279)                                 "DEBUG": "#000000" [](#__codelineno-137-280)                             } [](#__codelineno-137-281)                         }, [](#__codelineno-137-282)                         "log_severity": { [](#__codelineno-137-283)                             "title": "Severity", [](#__codelineno-137-284)                             "htmlTemplateForRow": "<span class='badge' style='background-color: {{ row.state_color2 }}' > {{ row.log_severity }} </span>" [](#__codelineno-137-285)                         }, [](#__codelineno-137-286)                         "service_name": "Service Name", [](#__codelineno-137-287)                         "process_name": "Process Name", [](#__codelineno-137-288)                         "process_function": "Process Function", [](#__codelineno-137-289)                         "log": "Message" [](#__codelineno-137-290)                     }, [](#__codelineno-137-291)                     "widget_id": "6895c8f0" [](#__codelineno-137-292)                 } [](#__codelineno-137-293)             ] [](#__codelineno-137-294)         }, [](#__codelineno-137-295)         { [](#__codelineno-137-296)             "title": "Infra Services", [](#__codelineno-137-297)             "show_filter": true, [](#__codelineno-137-298)             "widgets": [ [](#__codelineno-137-299)                 { [](#__codelineno-137-300)                     "widget_type": "tabular", [](#__codelineno-137-301)                     "title": "Log Messages", [](#__codelineno-137-302)                     "stream": "rdaf_services_logs", [](#__codelineno-137-303)                     "extra_filter": "service_category in ['rda_infra_svcs']", [](#__codelineno-137-304)                     "ts_column": "@timestamp", [](#__codelineno-137-305)                     "sorting": [ [](#__codelineno-137-306)                         { [](#__codelineno-137-307)                             "@timestamp": "desc" [](#__codelineno-137-308)                         } [](#__codelineno-137-309)                     ], [](#__codelineno-137-310)                     "columns": { [](#__codelineno-137-311)                         "@timestamp": { [](#__codelineno-137-312)                             "title": "Timestamp", [](#__codelineno-137-313)                             "type": "DATETIME" [](#__codelineno-137-314)                         }, [](#__codelineno-137-315)                         "log_severity": { [](#__codelineno-137-316)                             "title": "Severity", [](#__codelineno-137-317)                             "htmlTemplateForRow": "<span class='badge' style='background-color: {{ row.state_color2 }}' > {{ row.log_severity }} </span>" [](#__codelineno-137-318)                         }, [](#__codelineno-137-319)                         "state_color2": { [](#__codelineno-137-320)                             "type": "COLOR-MAP", [](#__codelineno-137-321)                             "source-column": "log_severity", [](#__codelineno-137-322)                             "color-map": { [](#__codelineno-137-323)                                 "INFO": "#388e3c", [](#__codelineno-137-324)                                 "ERROR": "#ef5350", [](#__codelineno-137-325)                                 "WARNING": "#ffa726", [](#__codelineno-137-326)                                 "DEBUG": "#000000", [](#__codelineno-137-327)                                 "UNKNOWN": "#bcaaa4" [](#__codelineno-137-328)                             } [](#__codelineno-137-329)                         }, [](#__codelineno-137-330)                         "service_name": "Service Name", [](#__codelineno-137-331)                         "process_name": "Process Name", [](#__codelineno-137-332)                         "log": "Message", [](#__codelineno-137-333)                         "minio_object": "Minio Object" [](#__codelineno-137-334)                     }, [](#__codelineno-137-335)                     "widget_id": "98f10587" [](#__codelineno-137-336)                 } [](#__codelineno-137-337)             ] [](#__codelineno-137-338)         } [](#__codelineno-137-339)     ] [](#__codelineno-137-340) }``

### **1.3.13 rdaf reset**

`rdaf reset` command allows the user to reset the RDAF platform configuration by performing the below operations.

*   Stop RDAF application, worker, platform & infrastructure services
*   Delete RDAF application, worker, platform & infrastructure services and its data
*   Delete all Docker images and volumes RDAF application, worker, platform & infrastructure services
*   Delete RDAF platform configuration

Danger

**rdaf reset** command is a disruptive operation as it clears entire RDAF platform footprint. It's primary purpose is to use only in Demo or POC environments (**"NOT" in Production**) where it requires to re-install entire RDAF platform from scratch.

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!