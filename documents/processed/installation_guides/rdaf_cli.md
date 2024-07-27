 



# Guide to Install RDAF deployment CLI for Non-Kubernetes Environment.

## **1\. RDAF Deployment CLI for Non-Kubernetes**

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


```
pip install --user --upgrade pip pip install --user rdafcli-1.2.2.tar.gz
```

Note

Once the above commands run successfully, logout and logback in to a new session.

Run the below command to verify installed RDAF deployment CLI version
```
 rdaf --version

```

Run the below command to view the RDAF deployment CLI help
```
 rdaf --help

```
```
 Documented commands (type help <topic>): 
 ======================================== 
 
 app     help   platform      rdac_cli  reset    setregistry  status    worker 
 backup  infra  prune_images  registry  restore  setup        validate

```

### **1.2 On-premise Docker Registry setup:**

CloudFabrix support hosting an on-premise docker registry which will download and synchronize RDA Fabric's platform, infrastructure and application services from CloudFabrix's public docker registry that is securely hosted on AWS and from other public docker registries as well. For more information on on-premise docker registry, please refer **[Docker registry access for RDAF platform services](https://bot-docs.cloudfabrix.io/installation_guides/deployment/#2-docker-registry-access-for-rdaf-platform-services-deployment)
**.

#### **1.2.1 rdaf registry setup**

Run rdaf registry --help to see available CLI options to deploy and manage on-premise docker registry.

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
 | `rdaf registry --help usage: ('registry',) [--insecure] [-h] [--debug]                      {setup,upgrade,install,fetch,delete-images,list-tags} ... Manage the Docker registry positional arguments:   {setup,upgrade,install,fetch,delete-images,list-tags}     setup               Setup Docker Registry     upgrade             Upgrade Registry locally     install             Install Registry locally     fetch               Fetch from configured Docker registries     delete-images       Deletes tag(s) and corresponding docker images     list-tags           Lists all the tags for all images in the docker                         registry optional arguments:   --insecure            Ignore SSL certificate issues when communicating with                         various hosts   -h, --help            show this help message and exit   --debug               Enable debug logs for the CLI operations` |

Run rdaf registry setup --help to see available CLI options.

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
 | `rdaf registry setup --help optional arguments:   -h, --help            show this help message and exit   --install-root INSTALL_ROOT                         Path to a directory where the Docker registry will be                         installed and managed   --docker-server-host DOCKER_SERVER_HOST                         Host name or IP address of the host where the Docker                         registry will be installed   --docker-registry-source-host DOCKER_SOURCE_HOST                         The hostname/IP of the source docker registry   --docker-registry-source-port DOCKER_SOURCE_PORT                         port of the docker registry   --docker-registry-source-user DOCKER_SOURCE_USER                         The username to use while connecting to the source                         docker registry   --docker-registry-source-password DOCKER_SOURCE_PASSWORD                         The password to use while connecting to the source                         docker registry   --no-prompt           Don't prompt for inputs` |

Run the below command to setup and configure on-premise docker registry service. In the below command example, 10.99.120.140 is the machine on which on-premise registry service is going to installed.

cfxregistry.cloudfabrix.io is the CloudFabrix's public docker registry hosted on AWS from which RDA Fabric docker images are going to be downloaded.


```
rdaf registry setup --docker-server-host 10.99.120.140 \     --docker-registry-source-host cfxregistry.cloudfabrix.io \     --docker-registry-source-port 443 \     --docker-registry-source-user readonly \     --docker-registry-source-password readonly
```

#### **1.2.2 rdaf registry install**

Run the below command to install the on-premise docker registry service.


```
rdaf registry install --tag 1.0.3
```

Info

*   For latest tag version, please contact support@cloudfabrix.com
*   On-premise docker registry service runs on port **TCP/5000**. This port may need to be enabled on firewall device if on-premise docker registry service and RDA Fabric service VMs are deployed in different network environments.

Run the below command to upgrade the on-premise docker registry service to latest version.


```
rdaf registry upgrade --tag <tag-name>
```

To check the status of the on-premise docker registry service, run the below command.


```
docker ps -a \| grep docker-registry
```

#### **1.2.3 rdaf registry fetch**

Once on-premise docker registry service is installed, run the below command to download one or more tags to pre-stage the docker images for RDA Fabric services deployment for fresh install or upgrade.
```
 rdaf registry fetch --tag 1.0.3.2,3.4.2,7.4.2,1.0.3

```

**Minio** object storage service image need to be downloaded explicitly using the below command.
```
 rdaf registry fetch --minio-tag RELEASE.2023-09-30T07-02-29Z

```

Info

**Note:** It may take few minutes to few hours depends on the outbound internet access bandwidth and the number of docker images to be downloaded. The default location path for the downloaded docker images is **/opt/rdaf-registry/data/docker/registry**. This path can be overridden/changed during **rdaf registry setup** command using **\--install-root** option if needed.

#### **1.2.4 rdaf registry list-tags**

Run the below command to list the downloaded images and their corresponding tags / versions.


```
rdaf registry list-tags
```

#### **1.2.5 rdaf registry delete-images**

Run the below command to delete one or more tags and corresponding docker images from on-premise docker registry.


```
rdaf registry delete-images --tag <tag-1>,<tag-2>
```

Important

When **on-premise docker repository** service is used, please make sure to add the **insecure-registries** parameter to **/etc/docker/daemon.json** file and restart the **docker daemon** as shown below on **all of RDA Fabric VMs** before the deployment.

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
 | `{  "tls": true,   "tlscacert": "/etc/tlscerts/ca/ca.pem",   "tlsverify": true,   "storage-driver": "overlay2",   "hosts": [   "unix:///var/run/docker.sock",    "tcp://0.0.0.0:2376"  ],   "tlskey": "/etc/tlscerts/server/server.key",   "debug": false,   "tlscert": "/etc/tlscerts/server/server.pem",   "experimental": false,   "insecure-registries" : ["<on-premise-docker-registry-ip-or-dns>:5000"],  "live-restore": true }` |


```
sudo systemctl daemon-reload
```


```
sudo systemctl restart docker
```


```
docker info
```

[Example Output](#__tabbed_1_1)
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

Tip

The location of the on-premise docker registry's CA certificate file `ca.crt` is located under **/opt/rdaf-registry/cert/ca**. This file `ca.crt` need to be copied to the machine on which **RDAF CLI** is used to **setup, configure and install RDA Fabric platform** and all of the required services using on-premise docker registry. This step is not applicable when cloud hosted docker registry **cfxregistry.cloudfabrix.io** is used.

### **1.3 RDAF Platform setup**

#### **1.3.1 rdaf setregistry**

When on-premise docker registry is deployed, change the default docker registry configuration to on-premise docker registry host to pull and install the RDA Fabric services.

Please refer `rdaf setregistry --help` for detailed command options.
```
 Configure the Docker registry for the platform 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --debug               Enable debug logs for the CLI operations (Optional) 
   --host DOCKER_REGISTRY_HOST 
                         Hostname/IP of the Docker registry 
   --port DOCKER_REGISTRY_PORT 
                         Port of the Docker registry 
   --user DOCKER_REGISTRY_USER 
                         Username of the Docker registry (Optional) 
   --password DOCKER_REGISTRY_PASSWORD 
                         Password of the Docker registry (Optional) 
   --cert-path CERT_PATH 
                         path of the Docker registry ca cert

```

*   Copy the `ca.crt` file from on-premise registry.

`
```
 sudo mkdir -p /opt/rdaf-registry 
 sudo chown -R `id -u`:`id -g` /opt/rdaf-registry`
```
```
 scp rdauser@<on-premise-registry-ip>:/opt/rdaf-registry/cert/ca/ca.crt /opt/rdaf-registry/registry-ca-cert.crt

```

*   Run the below command to set the docker-registry to on-premise one.
```
 rdaf setregistry --host <on-premise-docker-registry-ip-or-dns> --port 5000 --cert-path /opt/rdaf-registry/registry-ca-cert.crt

```

Tip

Please verify if **on-premise docker registry** is accessible on **port 5000** using either of the below commands.

*   **telnet `<on-premise-docker-registry-ip-or-dns>` 5000**
*   **curl -vv telnet://`<on-premise-docker-registry-ip-or-dns>`:5000**

#### **1.3.2 rdaf setup**

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

#### **1.3.4.1 rdaf infra**

`rdaf infra` command is used to deploy and manage RDAF infrastructure services. Run the below command to view available CLI options.
```
 usage: infra [--insecure] [-h] [--debug] {status,install,upgrade,up,down} ... 
 
 Manage infra services 
 
 positional arguments: 
   {status,install,upgrade,up,down} 
     status              Status of the RDAF Infra 
     install             Install the RDAF Infra containers 
     upgrade             Upgrade the RDAF Infra containers 
     up                  Crate the RDAF Infra Containers 
     down                Delete the RDAF Infra Containers 
     healthcheck         Check the liveness/health of Infra services. 
 
 optional arguments: 
   --insecure            Ignore SSL certificate issues when communicating with 
                         various hosts 
   -h, --help            show this help message and exit 
   --debug               Enable debug logs for the CLI operations

```

##### **1.3.4.1.1 Install infra services**

`rdaf infra install` command is used to deploy / install RDAF infrastructure services. Run the below command to view the available CLI options.
```
 usage: infra install [-h] --tag TAG [--service SERVICES] 
 
 optional arguments: 
   -h, --help          show this help message and exit 
   --tag TAG           Tag to use for the docker images of the infra components 
   --service SERVICES  Restrict the scope of the command to a specific service

```

Run the below command to deploy all RDAF infrastructure services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com.)
```
 rdaf infra install --tag 1.0.3

```

Run the below command to install a specific RDAF infrastructure service. Below are the supported infrastructure services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com)

*   haproxy
*   nats
*   mariadb
*   opensearch
*   kafka
*   zookeeper
*   redis
*   graphdb
```
 rdaf infra install --service haproxy --tag 1.0.3.2

```

##### **1.3.4.1.2 Status check**

Run the below command to see the status of all of the deployed RDAF infrastructure services.
```
 rdaf infra status

```

[Example Output](#__tabbed_2_1)
```
 +----------------------+----------------+-----------------+--------------+--------------------+ 
   | Name               | Host           | Status          | Container Id | Tag                | 
   +--------------------+----------------+-----------------+--------------+--------------------+ 
   | haproxy            | 192.168.133.97 | Up 3 days       | 41208fa98fa6 | 1.0.3.2            | 
   | haproxy            | 192.168.133.98 | Up 3 days       | 3891dded450a | 1.0.3.2            | 
   |keepalived          | 192.168.133.97 | active          | N/A          | N/A                | 
   | keepalived         | 192.168.133.98 | active          | N/A          | N/A                | 
   | nats               | 192.168.133.97 | Up 3 days       | f4405859b336 | 1.0.3              | 
   | nats               | 192.168.133.98 | Up 3 days       | e8bd7ec195cb | 1.0.3              | 
   | minio              | 192.168.133.93 | Up 3 days       | 13a00b450e74 | RELEASE.2023-09-30 | 
   |                    |                |                 |              | T07-02-29Z         | 
   | minio              | 192.168.133.97 | Up 3 days       | 1727f382a70a | RELEASE.2023-09-30 | 
   |                    |                |                 |              | T07-02-29Z         | 
   | minio              | 192.168.133.98 | Up 3 days       | d011be7b43c9 | RELEASE.2023-09-30 | 
   |                    |                |                 |              | T07-02-29Z         | 
   | minio              | 192.168.133.99 | Up 3 days       | 240eb6fbe918 | RELEASE.2023-09-30 | 
   |                    |                |                 |              | T07-02-29Z         | 
   | mariadb            | 192.168.133.97 | Up 3 days       | 6a1b26cd8f6c | 1.0.3              | 
   | mariadb            | 192.168.133.98 | Up 3 days       | 2328874827de | 1.0.3              | 
   | mariadb            | 192.168.133.99 | Up 3 days       | 65159da97d95 | 1.0.3              | 
   | opensearch         | 192.168.133.97 | Up 3 days       | 8f550b70d7ce | 1.0.3              | 
   | opensearch         | 192.168.133.98 | Up 3 days       | 83bdd9bece04 | 1.0.3              | 
   | opensearch         | 192.168.133.99 | Up 3 days       | 0225e9f6222d | 1.0.3              | 
   +--------------------+----------------+-----------------+--------------+--------------------+

```

##### **1.3.4.1.3 Start/Stop infra services**

Run the below command to start / stop all RDAF infrastructure services.
```
 rdaf infra up 
 rdaf infra down

```

Run the below commands to start / stop a specific RDAF infrastructure service.
```
 rdaf infra up --service minio 
 rdaf infra down --service minio

```

Danger

Stopping and Starting RDAF infrastructure service or services is a disruptive operation which will impact all of the RDAF dependant services and causes a downtime. When RDAF platform is deployed in Production environment, please perform these operations only during a scheduled downtime.

##### **1.3.4.1.4 Upgrade infra services**

Run the below command to upgrade all RDAF infrastructure services to a newer version.
```
 rdaf infra upgrade --tag 1.0.3

```

Run the below command to upgrade a specific RDAF infrastructure service to a newer version.
```
 rdaf infra upgrade --service nats --tag 1.0.3

```

Tip

Above shown tag version is a sample one and for a reference only, for actual newer versioned tag, please contact CloudFabrix support team at support@cloudfabrix.com

Danger

Please take full configuration and data backup of RDAF platform before any upgrade process. Upgrading RDAF infrastructure service or services is a disruptive operation which will impact all of the RDAF dependant services and causes a downtime. When RDAF platform is deployed in Production environment, please perform upgrade operation only during a scheduled downtime.

##### **1.3.4.1.5 Check Infra services liveness / health status**

Run the below command to verify RDAF infrastructure service's liveness / health status. This command helps to quickly identify any infrastructure service's availability or accessibility issues.
```
 rdaf infra healthcheck

```

[Example Output](#__tabbed_3_1)
```
 2022-10-26 02:18:14,565 [rdaf.cmd.infra] INFO     - Running Health Check on Infra services 
 2022-10-26 02:18:14,565 [rdaf.cmd.infra] INFO     - Running Health Check on haproxy on host 192.168.125.41 
 2022-10-26 02:18:14,691 [rdaf.cmd.infra] INFO     - Running Health Check on nats on host 192.168.125.41 
 2022-10-26 02:18:14,812 [rdaf.cmd.infra] INFO     - Running Health Check on minio on host 192.168.125.41 
 2022-10-26 02:18:15,001 [rdaf.cmd.infra] INFO     - Running Health Check on mariadb on host 192.168.125.41 
 2022-10-26 02:18:15,152 [rdaf.cmd.infra] INFO     - Running Health Check on opensearch on host 192.168.125.41 
 2022-10-26 02:18:15,775 [rdaf.cmd.infra] INFO     - Running Health Check on zookeeper on host 192.168.125.41 
 2022-10-26 02:18:15,904 [rdaf.cmd.infra] INFO     - Running Health Check on kafka on host 192.168.125.41 
 2022-10-26 02:18:16,399 [rdaf.cmd.infra] INFO     - Running Health Check on redis on host 192.168.125.41 
 2022-10-26 02:18:16,546 [rdaf.cmd.infra] INFO     - Running Health Check on redis-sentinel on host 192.168.125.41 
 +----------------+-----------------+--------+------------------------+----------------+--------------+ 
 | Name           | Check           | Status | Reason                 | Host           | Container Id | 
 +----------------+-----------------+--------+------------------------+----------------+--------------+ 
 | haproxy        | Port Connection | OK     | N/A                    | 192.168.125.41 | e905acafc36b | 
 | haproxy        | Service Status  | OK     | N/A                    | 192.168.125.41 | e905acafc36b | 
 | haproxy        | Firewall Port   | OK     | N/A                    | 192.168.125.41 | e905acafc36b | 
 | nats           | Port Connection | OK     | N/A                    | 192.168.125.41 | 83d674da41dd | 
 | nats           | Service Status  | OK     | N/A                    | 192.168.125.41 | 83d674da41dd | 
 | nats           | Firewall Port   | OK     | N/A                    | 192.168.125.41 | 83d674da41dd | 
 | minio          | Port Connection | OK     | N/A                    | 192.168.125.41 | ba13e7023d9f | 
 | minio          | Service Status  | OK     | N/A                    | 192.168.125.41 | ba13e7023d9f | 
 | minio          | Firewall Port   | OK     | N/A                    | 192.168.125.41 | ba13e7023d9f | 
 | mariadb        | Port Connection | OK     | N/A                    | 192.168.125.41 | 2fb8ca0233ec | 
 | mariadb        | Service Status  | OK     | N/A                    | 192.168.125.41 | 2fb8ca0233ec | 
 | mariadb        | Firewall Port   | OK     | N/A                    | 192.168.125.41 | 2fb8ca0233ec | 
 | opensearch     | Port Connection | OK     | N/A                    | 192.168.125.41 | 9cde1a3ab673 | 
 | opensearch     | Service Status  | Failed | 401 Client Error:      | 192.168.125.41 | 9cde1a3ab673 | 
 |                |                 |        | Unauthorized for url:  |                |              | 
 |                |                 |        | https://192.168.125.41:9 |              |              | 
 |                |                 |        | 200/_cluster/stats     |                |              | 
 | opensearch     | Firewall Port   | OK     | N/A                    | 192.168.125.41 | 9cde1a3ab673 | 
 | zookeeper      | Port Connection | OK     | N/A                    | 192.168.125.41 | c04cc08417ed | 
 | zookeeper      | Service Status  | OK     | N/A                    | 192.168.125.41 | c04cc08417ed | 
 | zookeeper      | Firewall Port   | OK     | N/A                    | 192.168.125.41 | c04cc08417ed | 
 | kafka          | Port Connection | OK     | N/A                    | 192.168.125.41 | 813e6a5235cd | 
 | kafka          | Service Status  | OK     | N/A                    | 192.168.125.41 | 813e6a5235cd | 
 | kafka          | Firewall Port   | OK     | N/A                    | 192.168.125.41 | 813e6a5235cd | 
 | redis          | Port Connection | OK     | N/A                    | 192.168.125.41 | 95657dd850a7 | 
 | redis          | Service Status  | OK     | N/A                    | 192.168.125.41 | 95657dd850a7 | 
 | redis          | Firewall Port   | OK     | N/A                    | 192.168.125.41 | 95657dd850a7 | 
 | redis-sentinel | Port Connection | OK     | N/A                    | 192.168.125.41 | 9e0d540aa777 | 
 | redis-sentinel | Service Status  | OK     | N/A                    | 192.168.125.41 | 9e0d540aa777 | 
 | redis-sentinel | Firewall Port   | OK     | N/A                    | 192.168.125.41 | 9e0d540aa777 | 
 +----------------+-----------------+--------+------------------------+--------------+--------------+

```

#### **1.3.4 rdaf platform**

`rdaf platform` command is used to deploy and manage RDAF core platform services. Run the below command to view available CLI options.
```
 usage: platform [-h] [--debug] {} ... 
 
 Manage the RDAF Platform 
 
 positional arguments: 
   {}                commands 
     add-service-host 
                     Add extra service vm 
     status          Status of the RDAF Platform 
     up              Create the RDAF Platform Containers 
     down            Deleting the RDAF Platform Containers 
     install         Install the RDAF platform containers 
     upgrade         Upgrade the RDAF platform containers 
     generate-certs  Generate certificates for hosts belonging to this 
                     installation 
     reset-admin-user 
                     reset the password of user 
 
 optional arguments: 
   -h, --help        show this help message and exit 
   --debug           Enable debug logs for the CLI operations

```

##### **1.3.4.1 Install platform services**

`rdaf platform install` command is used to deploy / install RDAF core platform services. Run the below command to view the available CLI options.
```
 usage: platform install [-h] --tag TAG [--service SERVICES] 
 
 optional arguments: 
   -h, --help          show this help message and exit 
   --tag TAG           Tag to use for the docker images of the platform 
                       components 
   --service SERVICES  Restrict the scope of the command to specific service

```

Run the below command to deploy all RDAF core platform services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com)
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

##### **1.3.4.2 Status check**

Run the below command to see the status of all of the deployed RDAF infrastructure services.
```
 rdaf platform status

```

[Example Output](#__tabbed_4_1)
```
 +--------------------+----------------+-----------+--------------+-------+ 
 | Name               | Host           | Status    | Container Id | Tag   | 
 +--------------------+----------------+-----------+--------------+-------+ 
 | rda_api_server     | 192.168.133.92 | Up 3 days | b2c91b3f5b8d | 3.4.2 | 
 | rda_api_server     | 192.168.133.93 | Up 3 days | 2c7e6e79e0d1 | 3.4.2 | 
 | rda_registry       | 192.168.133.92 | Up 3 days | 464161ddae16 | 3.4.2 | 
 | rda_registry       | 192.168.133.93 | Up 3 days | 946366995e8a | 3.4.2 | 
 | rda_scheduler      | 192.168.133.92 | Up 3 days | e6ab76d712fa | 3.4.2 | 
 | rda_scheduler      | 192.168.133.93 | Up 3 days | 93910af6e17e | 3.4.2 | 
 | rda_collector      | 192.168.133.92 | Up 3 days | 9c6e2a641ece | 3.4.2 | 
 | rda_collector      | 192.168.133.93 | Up 3 days | 2694023681e0 | 3.4.2 | 
 | rda_asset_dependen | 192.168.133.92 | Up 3 days | ef475644d1bd | 3.4.2 | 
 | cy                 |                |           |              |       | 
 | rda_asset_dependen | 192.168.133.93 | Up 3 days | 6c8570b3bb9c | 3.4.2 | 
 | cy                 |                |           |              |       | 
 | rda_identity       | 192.168.133.92 | Up 3 days | eadd3c3d5c8e | 3.4.2 | 
 | rda_identity       | 192.168.133.93 | Up 3 days | 32b7aca03e4a | 3.4.2 | 
 | rda_fsm            | 192.168.133.92 | Up 3 days | d553502dad1a | 3.4.2 | 
 | rda_fsm            | 192.168.133.93 | Up 3 days | 14ae04b1c4d2 | 3.4.2 | 
 | rda_chat_helper    | 192.168.133.92 | Up 3 days | 302a80076309 | 3.4.2 | 
 | rda_chat_helper    | 192.168.133.93 | Up 3 days | 601c21a8493d | 3.4.2 | 
 | cfx-rda-access-    | 192.168.133.92 | Up 3 days | 44e7cc4d1764 | 3.4.2 | 
 | manager            |                |           |              |       | 
 | cfx-rda-access-    | 192.168.133.93 | Up 3 days | 688b5aa2c895 | 3.4.2 | 
 | manager            |                |           |              |       | 
 +--------------------+----------------+-----------+--------------+-------+

``` 

##### **1.3.4.3 Upgrade platform services**

Run the below command to upgrade all RDAF core platform services to a newer version.
```
 rdaf platform upgrade --tag 3.4.2

```

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
```
 rdaf platform upgrade --service rda_collector --tag 3.4.2

```

Tip

Above shown tag version is a sample one and for a reference only, for actual newer versioned tag, please contact CloudFabrix support team at support@cloudfabrix.com

Danger

Please take full configuration and data backup of RDAF platform before any upgrade process. Upgrading RDAF core platform service or services is a disruptive operation which will impact all of the RDAF dependant services and causes a downtime. When RDAF platform is deployed in Production environment, please perform upgrade operation only during a scheduled downtime.

##### **1.3.4.4 Start/Stop platform services**

Run the below commands to start / stop all RDAF core platform services.
```
 rdaf platform up 
 rdaf platform down

```

Run the below commands to start / stop a specific RDAF core platform service.
```
 rdaf platform up --service rda_collector 
 rdaf platform down --service rda_collector

```

Danger

Stopping and Starting RDAF core platform service or services is a disruptive operation which will impact all of the RDAF dependant services and causes a downtime. When RDAF platform is deployed in Production environment, please perform these operations only during a scheduled downtime.

##### **1.3.4.5 Reset password**

Run the below command to reset the default user's **admin@cfx.com** password to factory default. i.e. **admin1234** and will force the user to reset the default password to tenant admin user's choice.
```
 rdaf platform reset-admin-user

```

Warning

Use above command option only in a scenario where tenant admin users are not able to access RDAF UI portal because of external IAM (identity and access management) tool such as Active Directory / LDAP / SSO is down or not accessible and default tenant admin user's password is forgotten or lost.

##### **1.3.4.6 Generate SSL Certificates**

Self-signed SSL certificates are used for RDAF infrastructure, core platform services and for RDAF CLI as well. This manual step is not usually needed as it will be run automatically during `rdaf setup` execution.

However, this command is useful to re-generate self-signed SSL certificates and overwrite existing ones if there is a need.
```
 rdaf platform generate-certs --overwrite

```

After re-generating the SSL certificates, please restart RDAF infrastructure, core platform, application, worker and agent services.

Danger

Re-generating self-signed SSL certificates is a disruptive operation which will impact all of the RDAF dependant services and causes a downtime. When RDAF platform is deployed in Production environment, please perform these operations only during a scheduled downtime.

##### **1.3.4.7 Add new service host**

RDAF platform's application services can be distributed on multiple hosts to distributed the workload and to run them in high-availability mode.

After deploying initial RDAF platform's application services, if there is a need, using the below command, a new RDAF platform's application services host can be added to the configuration after which existing application services can be re-deployed to be run on this new host to distribute the workload.
```
 rdaf platform add-service-host --ssh-password <SSH_PASSWORD> <ip-address-or-dns-name>

```

#### **1.3.5 rdaf app**

`rdaf app` command is used to deploy and manage RDAF application services. Run the below command to view available CLI options.

The supported application services are below.

*   **OIA:** Operations Intelligence and Analytics (Also known as **AIOps**)
*   **AIA:** Asset Intelligence and Analytics
```
 usage: ('app',) [-h] [--debug] {} ... 
 
 Manage the RDAF Apps 
 
 positional arguments: 
   {}             commands 
     status       Status of the App 
     up           Create the App serviceContainers 
     down         Delete the App service Containers 
     install      Install the App service containers 
     upgrade      Upgrade the App service containers 
     update-config 
                  Updated configurations of one or more components 
 
 optional arguments: 
   -h, --help     show this help message and exit 
   --debug        Enable debug logs for the CLI operations

```

##### **1.3.5.1 Install OIA/AIA services**

`rdaf app install` command is used to deploy / install RDAF OIA/AIA application services. Run the below command to view the available CLI options.
```
 usage: ('app',) install [-h] --tag TAG [--service SERVICES] {AIA,OIA} 
 
 positional arguments: 
   {AIA,OIA}           Select the APP to act on 
 
 optional arguments: 
   -h, --help          show this help message and exit 
   --tag TAG           Tag to use for the docker images of the app components 
   --service SERVICES  Restrict the scope of the command to specific service

```

Run the below command to deploy RDAF **OIA** / **AIA** application services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com)
```
 rdaf app install OIA --tag 7.4.2

```

##### **1.3.5.2 Start/Stop app services**

Run the below command to start / stop all RDAF application **OIA** services.
```
 rdaf app up OIA 
 rdaf app down OIA

```

Run the below command to start / stop all RDAF application **AIA** services.
```
 rdaf app up AIA 
 rdaf app down AIA

```

Run the below commands to start / stop a specific RDAF application **OIA** service.
```
 rdaf app up OIA --service cfx-rda-alert-ingester 
 rdaf app down OIA --service cfx-rda-alert-ingester

```

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
```
 rdaf app status

```

[Example Output](#__tabbed_5_1)
```
   +--------------------+----------------+-----------+--------------+-------+ 
   | Name               | Host           | Status    | Container Id | Tag   | 
   +--------------------+----------------+-----------+--------------+-------+ 
   | cfx-rda-app-       | 192.168.133.96 | Up 3 days | 133c976d2e64 | 7.4.2 | 
   | controller         |                |           |              |       | 
   | cfx-rda-app-       | 192.168.133.92 | Up 3 days | fc155ecf6f47 | 7.4.2 | 
   | controller         |                |           |              |       | 
   | cfx-rda-reports-   | 192.168.133.96 | Up 3 days | e7412d9eb3f1 | 7.4.2 | 
   | registry           |                |           |              |       | 
   | cfx-rda-reports-   | 192.168.133.92 | Up 3 days | 9bc6ec617744 | 7.4.2 | 
   | registry           |                |           |              |       | 
   | cfx-rda-           | 192.168.133.96 | Up 3 days | 40859a933dc7 | 7.4.2 | 
   | notification-      |                |           |              |       | 
   | service            |                |           |              |       | 
   | cfx-rda-           | 192.168.133.92 | Up 3 days | 3b2757fe7313 | 7.4.2 | 
   | notification-      |                |           |              |       | 
   | service            |                |           |              |       | 
   | cfx-rda-file-      | 192.168.133.96 | Up 3 days | ac9e1576332c | 7.4.2 | 
   | browser            |                |           |              |       | 
   | cfx-rda-file-      | 192.168.133.92 | Up 3 days | 3b0332b0a703 | 7.4.2 | 
   | browser            |                |           |              |       | 
   | cfx-rda-           | 192.168.133.96 | Up 3 days | 6982a9bdebe1 | 7.4.2 | 
   | configuration-     |                |           |              |       | 
   | service            |                |           |              |       | 
   | cfx-rda-           | 192.168.133.92 | Up 3 days | 7ee95287f65f | 7.4.2 | 
   | configuration-     |                |           |              |       | 
   | service            |                |           |              |       | 
   | cfx-rda-alert-     | 192.168.133.96 | Up 3 days | 582d55c8da74 | 7.4.2 | 
   | ingester           |                |           |              |       | 
   | cfx-rda-alert-     | 192.168.133.92 | Up 3 days | f14ad552ed3e | 7.4.2 | 
   | ingester           |                |           |              |       | 
   +--------------------+----------------+-----------+--------------+-------+
 ```

##### **1.3.5.4 Upgrade app OIA/AIA services**

Run the below command to upgrade all RDAF **OIA** / **AIA** application services to a newer version.
```
 rdaf app upgrade OIA --tag 7.4.2

```
```
 rdaf app upgrade AIA --tag 7.4.2

```

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
```
 rdaf app upgrade OIA --service cfx-rda-webhook-server --tag 7.4.2

```

Tip

Above shown tag version is a sample one and for a reference only, for actual newer versioned tag, please contact CloudFabrix support team at support@cloudfabrix.com

Danger

Please take full configuration and data backup of RDAF platform before any upgrade process. Upgrading RDAF OIA / AIA application service or services is a disruptive operation which will impact the availability of these services. When RDAF platform is deployed in Production environment, please perform upgrade operation only during a scheduled downtime.

##### **1.3.5.5 Update HAProxy configuration**

Run the below command to update the necessary HAProxy load-balancer configuration for RDAF **OIA** / **AIA** application services.
```
 rdaf app update-config OIA

```
```
 rdaf app update-config AIA

```

After deploying the RDAF OIA application services, it is mandatory to run the `rdaf app update-config` which will apply and restart the HAProxy load-balancer service automatically.

#### **1.3.6 rdaf worker**

`rdaf worker` command is used to deploy and manage RDAF worker services. Run the below command to view available CLI options.
```
 usage: worker [-h] [--debug] {} ... 
 
 Manage the RDAF Worker 
 
 positional arguments: 
   {}               commands 
     add-worker-host 
                    Add extra worker vm 
     status         Status of the RDAF Worker 
     up             Create the RDAF Worker Containers 
     down           Delete the RDAF Worker Containers 
     install        Install the RDAF Worker containers 
     upgrade        Upgrade the RDAF Worker containers 
 
 optional arguments: 
   -h, --help       show this help message and exit 
   --debug          Enable debug logs for the CLI operations

```

##### **1.3.6.1 Install worker service(s)**

`rdaf worker install` command is used to deploy / install RDAF worker services. Run the below command to view the available CLI options.
```
 usage: worker install [-h] --tag TAG 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --tag TAG   Tag to use for the docker images of the worker components

```

Run the below command to deploy all RDAF worker services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at support@cloudfabrix.com)
```
 rdaf worker install --tag 3.4.2

```

##### **1.3.6.2 Status check**

Run the below command to see the status of all of the deployed RDAF worker services.
```
 rdaf worker status

```

[Example Output](#__tabbed_6_1)
```
   +------------+----------------+-----------+--------------+-------+ 
   | Name       | Host           | Status    | Container Id | Tag   | 
   +------------+----------------+-----------+--------------+-------+ 
   | rda_worker | 192.168.133.96 | Up 4 days | bfeb469c3277 | 3.4.2 | 
   | rda_worker | 192.168.133.92 | Up 4 days | 43385833db75 | 3.4.2 | 
   +------------+----------------+-----------+--------------+-------+
 ```

##### **1.3.6.3 Upgrade worker services**

Run the below command to upgrade all RDAF worker service(s) to a newer version.
```
 rdaf worker upgrade --tag 3.4.2

```

Tip

Above shown tag version is a sample one and for a reference only, for actual newer versioned tag, please contact CloudFabrix support team at support@cloudfabrix.com

Danger

Upgrading RDAF worker service or services is a disruptive operation which will impact all of the worker jobs. When RDAF platform is deployed in Production environment, please perform upgrade operation only during a scheduled downtime.

##### **1.3.6.4 Start/Stop worker services**

Run the below commands to start / stop all RDAF worker services.
```
 rdaf worker up 
 rdaf worker down

```

Danger

Stopping and Starting RDAF worker service(s) is a disruptive operation which will impact all of the worker jobs. When RDAF platform is deployed in Production environment, please perform these operations only during a scheduled downtime.

##### **1.3.6.5 Add new worker host**

RDAF platform's worker services can be distributed on multiple hosts to distributed the workload.

After deploying initial RDAF platform's worker services, if there is a need, using the below command, a new RDAF platform's worker host can be added to the configuration after which new jobs can be run on this new worker host to distribute the workload.
```
 rdaf worker add-worker-host --ssh-password <SSH_PASSWORD> <ip-address-or-dns-name>

```

### **1.3.7 rdaf prune\_images**

After upgrading the RDAF infrastructure, core platform, application and worker services, run the below command to clean up the un-used docker images. This command helps to clean up and free the disk space on **/var/lib/docker** mount point.
```
 rdaf prune_images

```

### **1.3.8 rdaf validate**

`rdaf validate` command helps to verify or validate the below two configurations.

*   **values-yaml:** `values.yml` is a configuration file which allows the user to modify RDAF service's parameter(s) based on the deployment requirements. This file resides under **/opt/rdaf/deployment-scripts** directory on RDAF platform VM on which `rdaf setup` was run.
```
 rdaf validate values-yaml

```

*   **configs:** This command option verifies some of the pre-requisites on all RDAF hosts.

Below are the checks it performs.

*   SSH access and port check
*   Docker is installed or not
*   Docker-Compose is installed or not
*   Firewall ports are opened or not for RDAF services
```
 rdaf validate configs

```

[Example Output](#__tabbed_7_1)
```
 2022-09-06 00:30:40,660 [rdaf.cmd.validate] INFO     - checking connection for the host 192.168.125.146 
 2022-09-06 00:30:40,701 [rdaf.cmd.validate] INFO     - ssh check for host 192.168.125.146 successful 
 2022-09-06 00:30:40,701 [rdaf.cmd.validate] INFO     - checking connection for the host 192.168.125.143 
 2022-09-06 00:30:40,791 [rdaf.cmd.validate] INFO     - ssh check for host 192.168.125.143 successful 
 2022-09-06 00:30:40,792 [rdaf.cmd.validate] INFO     - checking connection for the host 192.168.125.149 
 .... 
 2022-09-06 00:30:40,949 [rdaf.cmd.validate] INFO     - ssh check for host 192.168.125.144 successful 
 2022-09-06 00:30:41,112 [rdaf.cmd.validate] INFO     - Docker is installed on host 192.168.125.146 
 2022-09-06 00:30:41,317 [rdaf.cmd.validate] INFO     - Docker is installed on host 192.168.125.143 
 .... 
 2022-09-06 00:30:42,036 [rdaf.cmd.validate] INFO     - Docker-compose is installed on host 192.168.125.146 
 2022-09-06 00:30:42,189 [rdaf.cmd.validate] INFO     - Docker-compose is installed on host 192.168.125.143 
 .... 
 2022-09-06 00:30:42,899 [rdaf.cmd.validate] INFO     - port is open 7222 on host 192.168.125.143 of component haproxy 
 2022-09-06 00:30:42,900 [rdaf.cmd.validate] INFO     - port is open 9443 on host 192.168.125.143 of component haproxy 
 2022-09-06 00:30:42,900 [rdaf.cmd.validate] INFO     - port is open 3307 on host 192.168.125.143 of component haproxy 
 .... 
 2022-09-06 00:30:43,134 [rdaf.cmd.validate] INFO     - port is open 8808 on host 192.168.125.144 of component haproxy 
 2022-09-06 00:30:43,364 [rdaf.cmd.validate] INFO     - port is open 4222 on host 192.168.125.143 of component nats 
 .... 
 2022-09-06 00:30:47,060 [rdaf.cmd.validate] INFO     - port is open 9093 on host 192.168.125.144 of component kafka 
 2022-09-06 00:30:47,264 [rdaf.cmd.validate] INFO     - port is open 9092 on host 192.168.125.145 of component kafka 
 2022-09-06 00:30:47,264 [rdaf.cmd.validate] INFO     - port is open 9093 on host 192.168.125.145 of component kafka 
 2022-09-06 00:30:47,521 [rdaf.cmd.validate] INFO     - port is open 6379 on host 192.168.125.143 of component redis 
 2022-09-06 00:30:47,763 [rdaf.cmd.validate] INFO     - port is open 6379 on host 192.168.125.144 of component redis 
 2022-09-06 00:30:47,974 [rdaf.cmd.validate] INFO     - port is open 6379 on host 192.168.125.145 of component redis 
 2022-09-06 00:30:48,222 [rdaf.cmd.validate] INFO     - port is open 26379 on host 192.168.125.143 of component redis-sentinel 
 2022-09-06 00:30:48,456 [rdaf.cmd.validate] INFO     - port is open 26379 on host 192.168.125.144 of component redis-sentinel 
 2022-09-06 00:30:48,668 [rdaf.cmd.validate] INFO     - port is open 26379 on host 192.168.125.145 of component redis-sentinel

```

### **1.3.9 rdaf rdac\_cli**

`rdaf rdac_cli` command allows you to install and upgrade RDA client CLI utility which interacts with RDA Fabric services and operations.
```
 rdaf rdac_cli -h

```
```
 usage: rdac-cli [-h] [--debug] {} ... 
 
 Install RDAC CLI 
 
 positional arguments: 
   {}          commands 
     install   Install the RDAC CLI 
     upgrade   Upgrade the RDAC CLI 
 
 optional arguments: 
   -h, --help  show this help message and exit 
   --debug     Enable debug logs for the CLI operations

```

*   To install RDA client CLI, run the below command
```
 rdaf rdac_cli install --tag <tag-name>

```

*   To upgrade RDA client CLI version, run the below command
```
 rdaf rdac_cli upgrade --tag <tag-name>

```

*   Run the below command to see RDA client CLI help and available subcommand options.
```
 rdac -h

```

[Example Output](#__tabbed_8_1)
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

### **1.3.10 rdaf backup**

Using `rdaf backup` command, RDAF configuration and data can be backed up periodically which can be used to restore in case of a recovery scenario.

`rdaf backup -h`
```
 usage: backup [--insecure] [-h] [--debug] --dest-dir BACKUP_DEST_DIR 
               [--create-tar] [--service SERVICES] 
 
 Backup the RDAF platform 
 
 optional arguments: 
   --insecure            Ignore SSL certificate issues when communicating with 
                         various hosts 
   -h, --help            show this help message and exit 
   --debug               Enable debug logs for the CLI operations 
   --dest-dir BACKUP_DEST_DIR 
                         Directory into which the backup will be stored 
   --create-tar          Creates a tar file for the backed up data 
   --service SERVICES    Backup only the specified components

```

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

`
```
 sudo mkdir -p /opt/backup && sudo chown -R `id -u`:`id -g` /opt/backup`
```

**Note:** For RDAF platform's configuration and application data backup, it is a pre-requisite to mount an NFS volume on all of the VMs. It is used to store the backup data and for restore using RDAF CLI tool.

Run the below command to take specific service's configuration and data backup.
```
 rdaf backup --dest-dir /opt/backup --create-tar --service mariadb

```
```
 rdaf backup --dest-dir /opt/backup --create-tar --service minio

```
```
 rdaf backup --dest-dir /opt/backup --create-tar --service opensearch

```

Run the below command to take more than one service's configuration and data backup.
```
 rdaf backup --dest-dir /opt/backup --create-tar --service mariadb --service minio --service opensearch

```

Warning

Though RDAF CLI takes backup of complete configuration and application data, it does not take backup of the OS (RHEL / Ubuntu) on which the RDA Fabric services are deployed. It is recommended to use 3rd party tools like Veeam, HP Dataprotect, Cohesity, Netbackup etc. to take full VM level backup on periodic basis.

3rd party VM level backup need to be used to recover RDAF VMs if OS is unable to boot RHEL / Ubuntu OS.

### **1.3.11 rdaf restore**

Using `rdaf restore` command, RDAF configuration and data can be restored from the previously taken backup.

Warning

While restoring RDAF services data from the backup, please make sure to stop both application and platform services.
```
 rdaf app down <OIA/AIA>

```
```
 rdaf platform down

```

For restoring the below service's data from the backup, please make sure their service is up and running.

`mariadb` `minio` `opensearch`

Below command shows the above service's running status.
```
 rdaf infra status

```

Below command shows the above service's functional status.
```
 rdaf infra healthcheck

```

`rdaf restore -h`
```
 usage: restore [--insecure] [-h] [--debug] [--no-prompt] [--service SERVICES] 
                (--from-dir BACKUP_SRC_DIR | --from-tar BACKUP_SRC_TAR) 
 
 Restore the RDAF platform from a previously backed up state 
 
 optional arguments: 
   --insecure            Ignore SSL certificate issues when communicating with 
                         various hosts 
   -h, --help            show this help message and exit 
   --debug               Enable debug logs for the CLI operations 
   --no-prompt           Don't prompt for inputs 
   --service SERVICES    Restore only the specified components 
   --from-dir BACKUP_SRC_DIR 
                         The directory which contains the backed up 
                         installation state 
   --from-tar BACKUP_SRC_TAR 
                         The tar.gz file which contains the backed up 
                         installation state

```

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
```
 rdaf restore --from-dir /opt/backup/2022-11-25-1669346503.565267

```

When the backup was taken **with** `--create-tar` option, please use `--from-tar` option and specify the backup tar file path as shown below.

Run the below command to restore RDAF system's full configuration and data from the backup tar file.
```
 rdaf restore --from-tar /opt/backup/2022-11-25-1669346503.565267/rdaf-backup-2022-11-25-1669346503.565267.tar.gz

```

Run the below command to restore **specific service's configuration and data** from the **backup folder**.
```
 rdaf restore --from-dir /opt/backup/2022-11-25-1669346503.565267 --service mariadb

```
```
 rdaf restore --from-dir /opt/backup/2022-11-25-1669346503.565267 --service minio

```
```
 rdaf restore --from-dir /opt/backup/2022-11-25-1669346503.565267 --service opensearch

```
```
 rdaf restore --from-dir /opt/backup/2022-11-25-1669346503.565267 --service config

```

Run the below command to restore **more than one service's configuration and data** from the **backup folder**.
```
 rdaf restore --from-dir /opt/backup/2022-11-25-1669346503.565267 --service mariadb --service minio

```

Run the below command to restore **specific service's configuration and data** from the **backup tar file**.
```
 rdaf restore --from-tar /opt/backup/2022-11-25-1669346503.565267/rdaf-backup-2022-11-25-1669346503.565267.tar.gz --service mariadb

```

Run the below command to restore **more than one service's configuration and data** from the **backup tar file**.
```
 rdaf restore --from-tar /opt/backup/2022-11-25-1669346503.565267/rdaf-backup-2022-11-25-1669346503.565267.tar.gz --service mariadb --service minio

```

### **1.3.12 rdaf log\_monitoring**

`rdaf log_monitoring` command is used to deploy and manage log monitoring services, through which the RDAF infrastructure, platform, application, and worker service logs are streamed in real-time.

As part of the log monitoring services, it installs the following services:

*   **Fluentbit:** It is a log shipping agent that streams the logs in real-time and ingests them into the `Logstash` service.
*   **Logstash:** It is a log processing agent that normalizes and extracts key attributes from log messages, such as timestamp, severity, process name, process function, container name, etc., before ingesting them into an index store service for analytics and visualization.

Run the below command to view available CLI options.
```
 rdaf log_monitoring

```
```
 usage: log_monitoring [-h] [--debug] 
                       {upgrade,install,status,up,down,start,stop} ... 
 
 Manage the RDAF log monitoring 
 
 positional arguments: 
   {upgrade,install,status,up,down,start,stop} 
                         commands 
     upgrade             Upgrade log monitoring components 
     install             Install log monitoring components 
     status              Status of the RDAF log monitoring 
     up                  Create the RDAF log monitoring Containers 
     down                Delete the RDAF log monitoring Containers 
     start               Start the RDAF log monitoring Containers 
     stop                Stop the RDAF log monitoring Containers 
 
 optional arguments: 
   -h, --help            show this help message and exit 
   --debug               Enable debug logs for the CLI operations

```

#### **1.3.12.1 Install Log Monitoring**

`rdaf log_monitoring install` command is used to deploy / install RDAF log monitoring services. Run the below command to view the available CLI options.
```
 rdaf log_monitoring install

```
```
 usage: log_monitoring install [-h] --log-monitoring-host LOG_MONITORING_HOST 
                               --tag TAG [--no-prompt] 
 log_monitoring install: error: the following arguments are required: --log-monitoring-host, --tag

```

To deploy all RDAF log monitoring services, execute the following command. Please note that it is mandatory to specify the host for the **Logstash** service deployment using the `--log-monitoring-host` option.

Note

Below shown **Logstash** host ip address is for a reference only. For the latest log monitoring services tag, please contact CloudFabrix support team at support@cloudfabrix.com.
```
 rdaf log_monitoring install --tag 1.0.2 --log-monitoring-host 192.168.125.52

```

[Example Output](#__tabbed_9_1)
```
 {"status":"CREATED","message":"'rdaf-log-monitoring' created."} 
 {"status":"CREATED","message":"'role-log-monitoring' created."} 
 {"status":"OK","message":"'rdaf-log-monitoring' updated."} 
 {"status":"CREATED","message":"'role-log-monitoring' created."} 
 { 
   "retention_days": 15, 
   "timestamp": "@timestamp", 
   "search_case_insensitive": true, 
   "_settings": { 
     "number_of_shards": 3, 
     "number_of_replicas": 1, 
     "refresh_interval": "60s" 
   } 
 } 
 Persistent stream saved. 
 2023-11-02 05:04:08,842 [rdaf.component.haproxy] INFO     - Updated HAProxy configuration at /opt/rdaf/config/haproxy/haproxy.cfg on 192.168.125.53 
 ... 
 ... 
 [+] Running 1/1 
  ⠿ Container fluent-bit-fluentbit-1  Started                                                                                                                                            0.4s 
 2023-11-02 05:06:05,138 [rdaf.component.log_monitoring] INFO     - Restarting logstash services on host 192.168.125.53 
 [+] Running 1/1 
  ⠿ Container logstash-logstash-1  Started                                                                                                                                               0.4s 
 2023-11-02 05:06:05,617 [rdaf.component.log_monitoring] INFO     - Restarting fluentbit services on host 192.168.125.53 
 [+] Running 1/1 
  ⠿ Container fluent-bit-fluentbit-1  Started                                                                                                                                           10.8s 
 2023-11-02 05:06:16,488 [rdaf.component.minio] INFO     - configuring minio services logs 
 Successfully applied new settings. 
 Successfully applied new settings. 
 2023-11-02 05:06:16,936 [rdaf.component.log_monitoring] INFO     - Successfully installed and configured rdaf log streaming

```

#### **1.3.12.2 Status check**

Run the below command to see the status of all of the deployed RDAF log monitoring services.
```
 rdaf log_monitoring status

```

[Example Output](#__tabbed_10_1)
```
 +---------------------+----------------------+---------------------------+-------------------------+---------+ 
 | Name                | Host                 | Status                    | Container Id            | Tag     | 
 +---------------------+----------------------+---------------------------+-------------------------+---------+ 
 | logstash            | 192.168.125.53       | Up About a minute         | 62b3b7c81472            | 1.0.2   | 
 | fluentbit           | 192.168.125.53       | Up About a minute         | c5f8a6f340b3            | 1.0.2   | 
 +---------------------+----------------------+---------------------------+-------------------------+---------+

```

#### **1.3.12.3 Upgrade Log Monitoring**

Run the below command to upgrade all RDAF log monitoring to a newer version.
```
 rdaf log_monitoring upgrade --tag <new-tag-version>

```

#### **1.3.12.4 Restart Log Monitoring services**

**Restarting the log monitoring service using `rdaf` CLI commands.**

**a**) **To Stop**

Run the below command to **Stop** all RDAF log monitoring services.
```
 rdaf log_monitoring down

```

[Example Output](#__tabbed_11_1)
```
 --------------------------------------------------------------------------------------------------------------------------- 
 2023-11-02 05:20:53,313 [rdaf.component.log_monitoring] INFO     - Deleting logstash service on host 192.168.125.53 
 [+] Running 1/1  ⠿ Container logstash-logstash-1  Stopped                                                                                                                                               0.3s 
 Going to remove logstash-logstash-1 
 [+] Running 1/0  ⠿ Container logstash-logstash-1  Removed                                                                                                                                               0.0s 
 2023-11-02 05:20:53,639 [rdaf.component.log_monitoring] INFO     - Deleting fluent-bit service on host 192.168.125.53 
 [+] Running 1/1  ⠿ Container fluent-bit-fluentbit-1  Stopped                                                                                                                                           10.8s 
 Going to remove fluent-bit-fluentbit-1 
 [+] Running 1/0  ⠿ Container fluent-bit-fluentbit-1  Removed 
 
 ---------------------------------------------------------------------------------------------------------------------------

```

**b**) **To Start**

Run the below command to **Start** all RDAF log monitoring services.
```
 rdaf log_monitoring up

```

[Example Output](#__tabbed_12_1)
```
 --------------------------------------------------------------------------------------------------------------------------- 
 2023-11-02 05:21:33,355 [rdaf.component.log_monitoring] INFO     - Creating logstash services on host 192.168.125.53 
 [+] Running 1/1 
  ⠿ Container logstash-logstash-1  Started                                                                                                                                               0.2s 
 2023-11-02 05:21:33,641 [rdaf.component.log_monitoring] INFO     - Creating fluent-bit services on host 192.168.125.53 
 [+] Running 1/1 
  ⠿ Container fluent-bit-fluentbit-1  Started  
 
 ---------------------------------------------------------------------------------------------------------------------------

```

#### **1.3.12.5 Add Log Monitoring dashboard**

Login to RDAF UI portal as MSP admin user.

Go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Dashboards** --> **User Dashboards** --> Click on **Add** and create a new dashboard by copying the below Dashboard configuration for RDAF log monitoring services.

`
```
 { 
     "name": "rdaf-platform-log-analytics", 
     "label": "RDAF Platform Logs", 
     "description": "RDAF Platform service's log analysis dashboard", 
     "version": "23.01.14.1", 
     "enabled": true, 
     "dashboard_style": "tabbed", 
     "status_poller": { 
         "stream": "rdaf_services_logs", 
         "frequency": 15, 
         "columns": [ 
             "@timestamp" 
         ], 
         "sorting": [ 
             { 
                 "@timestamp": "desc" 
             } 
         ], 
         "query": "`@timestamp` is after '${timestamp}'", 
         "defaults": { 
             "@timestamp": "$UTCNOW" 
         }, 
         "action": "refresh" 
     }, 
     "dashboard_filters": { 
         "time_filter": true, 
         "columns_filter": [ 
             { 
                 "id": "@timestamp", 
                 "label": "Timestamp", 
                 "type": "DATETIME" 
             }, 
             { 
                 "id": "service_name", 
                 "label": "Service Name", 
                 "type": "TEXT" 
             }, 
             { 
                 "id": "service_category", 
                 "label": "Service Category", 
                 "type": "TEXT" 
             }, 
             { 
                 "id": "log_severity", 
                 "label": "Log Severity", 
                 "type": "TEXT" 
             }, 
             { 
                 "id": "log", 
                 "label": "Log Message", 
                 "type": "TEXT" 
             }, 
             { 
                 "id": "log.text", 
                 "label": "Log Message Text", 
                 "type": "SIMPLE_TEXT" 
             }, 
             { 
                 "id": "process_name", 
                 "label": "Process Name", 
                 "type": "TEXT" 
             }, 
             { 
                 "id": "process_function", 
                 "label": "Process Function", 
                 "type": "TEXT" 
             }, 
             { 
                 "id": "thread_id", 
                 "label": "Thread ID", 
                 "type": "TEXT" 
             }, 
             { 
                 "id": "k8s_pod_name", 
                 "label": "POD Name", 
                 "type": "TEXT" 
             }, 
             { 
                 "id": "k8s_container_name", 
                 "label": "Container Name", 
                 "type": "TEXT" 
             } 
         ], 
         "group_filters": [ 
             { 
                 "stream": "rdaf_services_logs", 
                 "title": "Log Severity", 
                 "group_by": [ 
                     "log_severity" 
                 ], 
                 "ts_column": "@timestamp", 
                 "agg": "value_count", 
                 "column": "_id", 
                 "type": "int" 
             }, 
             { 
                 "stream": "rdaf_services_logs", 
                 "title": "Service Name", 
                 "group_by": [ 
                     "service_name" 
                 ], 
                 "ts_column": "@timestamp", 
                 "limit": 50, 
                 "agg": "value_count", 
                 "column": "_id", 
                 "type": "int" 
             }, 
             { 
                 "stream": "rdaf_services_logs", 
                 "title": "Service Category", 
                 "group_by": [ 
                     "service_category" 
                 ], 
                 "ts_column": "@timestamp", 
                 "agg": "value_count", 
                 "column": "_id", 
                 "type": "int" 
             }, 
             { 
                 "stream": "rdaf_services_logs", 
                 "title": "POD Name", 
                 "group_by": [ 
                     "k8s_pod_name" 
                 ], 
                 "ts_column": "@timestamp", 
                 "agg": "value_count", 
                 "limit": 200, 
                 "column": "_id", 
                 "type": "int" 
             } 
         ] 
     }, 
     "dashboard_sections": [ 
         { 
             "title": "Overall Summary", 
             "show_filter": true, 
             "widgets": [ 
                 { 
                     "title": "Log Severity Trend", 
                     "widget_type": "timeseries", 
                     "stream": "rdaf_services_logs", 
                     "ts_column": "@timestamp", 
                     "max_width": 12, 
                     "height": 3, 
                     "min_width": 12, 
                     "chartProperties": { 
                         "yAxisLabel": "Count", 
                         "xAxisLabel": null, 
                         "legendLocation": "bottom" 
                     }, 
                     "interval": "15Min", 
                     "group_by": [ 
                         "log_severity" 
                     ], 
                     "series_spec": [ 
                         { 
                             "column": "log_severity", 
                             "agg": "value_count", 
                             "type": "int" 
                         } 
                     ], 
                     "widget_id": "06413884" 
                 }, 
                 { 
                     "widget_type": "pie_chart", 
                     "title": "Logs by Severity", 
                     "stream": "rdaf_services_logs", 
                     "ts_column": "@timestamp", 
                     "column": "_id", 
                     "agg": "value_count", 
                     "group_by": [ 
                         "log_severity" 
                     ], 
                     "type": "str", 
                     "style": { 
                         "color-map": { 
                             "ERROR": [ 
                                 "#ef5350", 
                                 "#ffffff" 
                             ], 
                             "WARNING": [ 
                                 "#FFA726", 
                                 "#ffffff" 
                             ], 
                             "INFO": [ 
                                 "#388e3c", 
                                 "#ffffff" 
                             ], 
                             "DEBUG": [ 
                                 "#000000", 
                                 "#ffffff" 
                             ], 
                             "UNKNOWN": [ 
                                 "#bcaaa4", 
                                 "#ffffff" 
                             ] 
                         } 
                     }, 
                     "min_width": 4, 
                     "height": 4, 
                     "max_width": 4, 
                     "widget_id": "b2ffa8e9" 
                 }, 
                 { 
                     "widget_type": "pie_chart", 
                     "title": "Logs by RDA Host IP", 
                     "stream": "rdaf_services_logs", 
                     "ts_column": "@timestamp", 
                     "column": "_id", 
                     "agg": "value_count", 
                     "group_by": [ 
                         "host" 
                     ], 
                     "type": "str", 
                     "min_width": 4, 
                     "height": 4, 
                     "max_width": 4, 
                     "widget_id": "a4f2d8bd" 
                 }, 
                 { 
                     "widget_type": "pie_chart", 
                     "title": "Logs by Service Category", 
                     "stream": "rdaf_services_logs", 
                     "ts_column": "@timestamp", 
                     "column": "_id", 
                     "agg": "value_count", 
                     "group_by": [ 
                         "service_category" 
                     ], 
                     "type": "str", 
                     "min_width": 4, 
                     "height": 4, 
                     "max_width": 4, 
                     "widget_id": "89ac5ce9" 
                 }, 
                 { 
                     "widget_type": "pie_chart", 
                     "title": "Logs by Service Name", 
                     "stream": "rdaf_services_logs", 
                     "ts_column": "@timestamp", 
                     "column": "_id", 
                     "agg": "value_count", 
                     "group_by": "service_name", 
                     "type": "int", 
                     "min_width": 4, 
                     "height": 4, 
                     "max_width": 4, 
                     "widget_id": "4b267fce" 
                 } 
             ] 
         }, 
         { 
             "title": "App Services", 
             "show_filter": true, 
             "widgets": [ 
                 { 
                     "widget_type": "tabular", 
                     "title": "Log Messages", 
                     "stream": "rdaf_services_logs", 
                     "extra_filter": "service_category in ['rda_app_svcs', 'rda_pfm_svcs']", 
                     "ts_column": "@timestamp", 
                     "sorting": [ 
                         { 
                             "@timestamp": "desc" 
                         } 
                     ], 
                     "columns": { 
                         "@timestamp": { 
                             "title": "Timestamp", 
                             "type": "DATETIME" 
                         }, 
                         "state_color2": { 
                             "type": "COLOR-MAP", 
                             "source-column": "log_severity", 
                             "color-map": { 
                                 "INFO": "#388e3c", 
                                 "ERROR": "#ef5350", 
                                 "WARNING": "#ffa726", 
                                 "DEBUG": "#000000" 
                             } 
                         }, 
                         "log_severity": { 
                             "title": "Severity", 
                             "htmlTemplateForRow": "<span class='badge' style='background-color: {{ row.state_color2 }}' > {{ row.log_severity }} </span>" 
                         }, 
                         "service_name": "Service Name", 
                         "process_name": "Process Name", 
                         "process_function": "Process Function", 
                         "log": "Message" 
                     }, 
                     "widget_id": "6895c8f0" 
                 } 
             ] 
         }, 
         { 
             "title": "Infra Services", 
             "show_filter": true, 
             "widgets": [ 
                 { 
                     "widget_type": "tabular", 
                     "title": "Log Messages", 
                     "stream": "rdaf_services_logs", 
                     "extra_filter": "service_category in ['rda_infra_svcs']", 
                     "ts_column": "@timestamp", 
                     "sorting": [ 
                         { 
                             "@timestamp": "desc" 
                         } 
                     ], 
                     "columns": { 
                         "@timestamp": { 
                             "title": "Timestamp", 
                             "type": "DATETIME" 
                         }, 
                         "log_severity": { 
                             "title": "Severity", 
                             "htmlTemplateForRow": "<span class='badge' style='background-color: {{ row.state_color2 }}' > {{ row.log_severity }} </span>" 
                         }, 
                         "state_color2": { 
                             "type": "COLOR-MAP", 
                             "source-column": "log_severity", 
                             "color-map": { 
                                 "INFO": "#388e3c", 
                                 "ERROR": "#ef5350", 
                                 "WARNING": "#ffa726", 
                                 "DEBUG": "#000000", 
                                 "UNKNOWN": "#bcaaa4" 
                             } 
                         }, 
                         "service_name": "Service Name", 
                         "process_name": "Process Name", 
                         "log": "Message", 
                         "minio_object": "Minio Object" 
                     }, 
                     "widget_id": "98f10587" 
                 } 
             ] 
         } 
     ] 
 }`
```

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