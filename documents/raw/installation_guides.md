 



RDA Studio Installation Guide
=============================

This document provides instructions on how to deploy RDA Studio in RDA Fabric platform's environment.

RDA Studio Software installation prerequisites

CloudFabrix supports Windows, Linux, and Mac OS environments to install, configure and run RDA studio software. Below are the prerequisites which need to be in place before RDA studio can be installed and configured.

1\. Prerequisites
-----------------

Before you proceed, make sure you meet the following requirements

Windows 10 / Linux / Mac OS X with the below software are installed

*   CPU - 2
*   Memory - 8 GB
*   Disk - 50 GB
*   [Docker version 18.09.2 (or above)](https://docs.docker.com/engine/install/)
    
*   [Docker-compose (1.27.x and above)](https://docs.docker.com/compose/install/)
    
*   Python 3.7.4 (recommended) or above
*   pip3 utility

Internet Connectivity to download the 'RDA' studio docker image.

*   CloudFabrix docker registry URL: cfxregistry.cloudfabrix.io
*   If there is HTTP Proxy in place, please refer to Docker documentation on how to configure HTTP Proxy settings for the Docker service.

Verify Prerequisites

Make sure the below commands are in the PATH variable in the user's login profile.

Run the below commands to verify currently installed RDA prerequisites.

`[](#__codelineno-0-1) docker --version`

`[](#__codelineno-1-1) docker-compose --version`

`[](#__codelineno-2-1) python3 --version`

`[](#__codelineno-3-1) pip3 --version`

2\. Linux OS Environment
------------------------

**RDA software installation on Linux OS**

  
**Step 1:**

Login to Linux box using standard ssh tool (eg. putty or using ssh client)

`[](#__codelineno-4-1) uname -a`

On Ubuntu VM, sample output is as follows: Linux rda-studio-vm 5.4.0-144-generic #161-Ubuntu SMP Fri Feb 3 14:49:04 UTC 2023 x86\_64 x86\_64 x86\_64 GNU/Linux

**Step 2:**

  
Create the following directory structure after logging into Linux machine for setting up directory structure for the RDA Studio  

``[](#__codelineno-5-1) sudo mkdir -p /opt/rda_studio/cfxdx/home/ [](#__codelineno-5-2) sudo mkdir -p /opt/rda_studio/cfxdx/config/network_config [](#__codelineno-5-3) sudo mkdir -p /opt/rda_studio/cfxdx/output [](#__codelineno-5-4) sudo chown -R `id -u`:`id -g` /opt/rda_studio``

**Step 3:**

Create rda-studio.yaml file for RDA studio

`[](#__codelineno-6-1) cd /opt/rda_studio/ [](#__codelineno-6-2) [](#__codelineno-6-3) cat > rda-studio.yaml << EOF [](#__codelineno-6-4) version: '3.1' [](#__codelineno-6-5) services: [](#__codelineno-6-6)   cfxdx: [](#__codelineno-6-7)     image: cfxregistry.cloudfabrix.io/ubuntu-cfxdx-nb-nginx-all:daily [](#__codelineno-6-8)     restart: unless-stopped [](#__codelineno-6-9)     mem_limit: 6G [](#__codelineno-6-10)     memswap_limit: 6G [](#__codelineno-6-11)     volumes: [](#__codelineno-6-12)       - /opt/rda_studio/cfxdx/home/:/root [](#__codelineno-6-13)       - /opt/rda_studio/cfxdx/config/network_config/:/tmp/config/ [](#__codelineno-6-14)       - /opt/rda_studio/cfxdx/output:/tmp/output/ [](#__codelineno-6-15)       - /opt/rda_studio/cfxdx/config/network_config/:/network_config [](#__codelineno-6-16)     ports: [](#__codelineno-6-17)       - "9998:9998" [](#__codelineno-6-18)       - "443:443" [](#__codelineno-6-19)     environment: [](#__codelineno-6-20)       NLTK_DATA : "/root/nltk_data" [](#__codelineno-6-21)       CFXDX_CONFIG_FILE: /tmp/config/conf.yml [](#__codelineno-6-22)       RDA_NETWORK_CONFIG: /network_config/config.json [](#__codelineno-6-23)       RDA_USER: rdademo [](#__codelineno-6-24)       RDA_PASSWORD: rdademo1234 [](#__codelineno-6-25) [](#__codelineno-6-26) EOF`

Tip

If you have deployed **on-premise docker regsitry** VM and downloaded the RDA Fabric images including RDA Studio, please specify the on-premise docker registry VM's ip address as shown below. Otherwise, skip this step.

`[](#__codelineno-7-1) vi rda-studio.yaml`

`[](#__codelineno-8-1) services: [](#__codelineno-8-2)   cfxdx: [](#__codelineno-8-3)     image: <on-premise-docker-registry-ip>:5000/ubuntu-cfxdx-nb-nginx-all:daily [](#__codelineno-8-4)     restart: unless-stopped [](#__codelineno-8-5)     volumes: [](#__codelineno-8-6)       - /opt/rda_studio/cfxdx/home/:/root [](#__codelineno-8-7)       - /opt/rda_studio/cfxdx/config/:/tmp/config/ [](#__codelineno-8-8)       - /opt/rda_studio/cfxdx/output:/tmp/output/ [](#__codelineno-8-9)       - /opt/rda_studio/cfxdx/config/network_config/:/network_config [](#__codelineno-8-10)     ports: [](#__codelineno-8-11)       - "9998:9998" [](#__codelineno-8-12)       - "443:443" [](#__codelineno-8-13)     environment: [](#__codelineno-8-14)       CFXDX_CONFIG_FILE: /tmp/config/conf.yml [](#__codelineno-8-15)       RDA_NETWORK_CONFIG: /network_config/config.json [](#__codelineno-8-16)       RDA_USER: rdademo [](#__codelineno-8-17)       RDA_PASSWORD: rdademo1234`

Tip

If you are in an HTTP Proxy environment, please configure the HTTP Proxy environment variables as shown below. If there are any target endpoint(s) that don't need to go through the HTTP Proxy, please specify their IP addresses or FQDN names as comma-separated values under the `no_proxy` and `NO_PROXY` environment variables.

`[](#__codelineno-9-1) services: [](#__codelineno-9-2)   cfxdx: [](#__codelineno-9-3)     image: <on-premise-docker-registry-ip>:5000/ubuntu-cfxdx-nb-nginx-all:daily [](#__codelineno-9-4)     restart: unless-stopped [](#__codelineno-9-5)     volumes: [](#__codelineno-9-6)       - /opt/rda_studio/cfxdx/home/:/root [](#__codelineno-9-7)       - /opt/rda_studio/cfxdx/config/:/tmp/config/ [](#__codelineno-9-8)       - /opt/rda_studio/cfxdx/output:/tmp/output/ [](#__codelineno-9-9)       - /opt/rda_studio/cfxdx/config/network_config/:/network_config [](#__codelineno-9-10)     ports: [](#__codelineno-9-11)       - "9998:9998" [](#__codelineno-9-12)       - "443:443" [](#__codelineno-9-13) [](#__codelineno-9-14)     environment: [](#__codelineno-9-15)       CFXDX_CONFIG_FILE: /tmp/config/conf.yml [](#__codelineno-9-16)       RDA_NETWORK_CONFIG: /network_config/config.json [](#__codelineno-9-17)       RDA_USER: rdademo [](#__codelineno-9-18)       RDA_PASSWORD: rdademo1234 [](#__codelineno-9-19)       http_proxy: "http://user:password@192.168.122.107:3128" [](#__codelineno-9-20)       https_proxy: "http://user:password@192.168.122.107:3128" [](#__codelineno-9-21)       no_proxy: "127.0.0.1" [](#__codelineno-9-22)       HTTP_PROXY: "http://user:password@192.168.122.107:3128" [](#__codelineno-9-23)       HTTPS_PROXY: "http://user:password@192.168.122.107:3128" [](#__codelineno-9-24)       NO_PROXY: "127.0.0.1"`

**Step-4:**

The RDA Studio service registers and communicates with the RDAF platform using a configuration file that contains your tenant ID, data fabric access tokens, and object storage credentials.

Download RDA Fabric Configuration from the portal by going to `Configuration --> RDA Administration --> Network` and copy it to the local filesystem where the RDA Studio node is going to be installed.

*   Save the file as `config.json`

![RDAFNetworkConfig](https://bot-docs.cloudfabrix.io/images/rda-network-config.png)

**Step-5:**

*   Copy the downloaded RDA Fabric configuration file to the VM or host on which RDA Studio is going to be installed and copy the file to below mentioned path.

`[](#__codelineno-10-1) cp ~/config.json /opt/rda_studio/cfxdx/config/network_config/config.json`

**Step-6:**:

**Docker Login**

Run the below command to create and save the docker login session into CloudFabrix's secure docker repository.

`[](#__codelineno-11-1) docker login -u='readonly' -p='readonly' cfxregistry.cloudfabrix.io`

Tip

**Note-1:** RDA Studio communicates with RDA Fabric that is running in cloud or on-premise datacenter over ports 4222/TCP & 9443/TCP. Please make sure RDA Studio has outbound network access over these network ports. In addition, make sure RDA Fabric is configured to allow inbound network traffic for the same ports to accept the traffic from RDA Studio.

**Note-2:** Please verify **config.json** is configured with publicly accessible IP/FQDN of RDA Fabric for NATs and Minio endpoints.

**Step-7:**

Tip

If Ubuntu version is v22.04.2 LTS or above & Docker Compose version is v2.16.0 or above, Use the following Commands mentioned below

`[](#__codelineno-12-1) cd /opt/rda_studio [](#__codelineno-12-2) [](#__codelineno-12-3) docker-compose -f rda-studio.yaml pull [](#__codelineno-12-4) docker-compose -f rda-studio.yaml up -d`

[Additional Steps for Ubuntu](#__tabbed_1_1)

This section provides additional steps to deploy RDA Studio on Ubuntu OS (Certified on 18.04). Using the currently logged-in user, run the following commands to make sure the user has sufficient permissions.

`[](#__codelineno-13-1) sudo groupadd docker [](#__codelineno-13-2) sudo gpasswd -a $USER docker [](#__codelineno-13-3) docker ps` 

*   If the above command throws an error **permission denied error**, run the following command to provide sufficient privileges to the currently logged-in user to run `docker`.

`[](#__codelineno-14-1) sudo chmod 666 /var/run/docker.sock`

\- Run the following commands to install \`docker-compose\`\` for the currently logged-in user.

`[](#__codelineno-15-1) sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose [](#__codelineno-15-2) sudo chmod +x /usr/local/bin/docker-compose [](#__codelineno-15-3) sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose`

Open firewall to allow 9998,443 port

`[](#__codelineno-16-1) sudo ufw allow 9998/tcp [](#__codelineno-16-2) sudo ufw allow 443/tcp`

**Step-8:**  
To access RDA Studio UI, open up a browser and enter the URL as https://ipaddress:9998 OR https://ipaddress:443  
  
**Note:** _Access RDA using https://rda-studio-ip-address:9998/ OR https://rda-studio-ip-address:443  
_

_The default user name is 'rdademo' and the password is 'rdademo1234'_  
  
![RDA related files](https://bot-docs.cloudfabrix.io/images/rda_studio_ui_password_macos.png)

Default landing page of RDA Studio on Mac OS

**Note:** Default username/password can be changed from docker-compose.yml file under RDA studio install directory.

|     |     |
| --- | --- |
| [1](#__codelineno-17-1)<br>[2](#__codelineno-17-2)<br>[3](#__codelineno-17-3)<br>[4](#__codelineno-17-4) | `environment:   CFXDX_CONFIG_FILE: /tmp/config/conf.yml   RDA_USER: rdademo   RDA_PASSWORD: rdademo1234` |

**Note:** _Default username/password can be changed from docker-compose.yml file under RDA install directory._  

3\. Mac OS Environment
----------------------

**Note:** Please check the [Prerequisites](#1-prerequisites)
 - Installation Prerequisites before you proceed.

**Note:** Make sure the below commands are in the PATH variable in the user's login profile.

Run the below commands to verify currently installed RDA prerequisites.

Verify Prerequisites

Make sure the below commands are in the PATH variable in the user's login profile.

Run the below commands to verify currently installed RDA prerequisites.

`[](#__codelineno-18-1) docker --version`

`[](#__codelineno-19-1) docker-compose --version`

`[](#__codelineno-20-1) python3 --version`

`[](#__codelineno-21-1) pip3 --version`

**Step-1:**

Create a virtual environment using python3

|     |     |
| --- | --- |
| [1](#__codelineno-22-1)<br>[2](#__codelineno-22-2)<br>[3](#__codelineno-22-3) | `python3 -m venv <name of the environment> eg. $ python3 -m venv rda-venv` |

**Step-2:**

Source virtual env that was created in Step 2 as shown below.  

|     |     |
| --- | --- |
| [1](#__codelineno-23-1)<br>[2](#__codelineno-23-2)<br>[3](#__codelineno-23-3) | `$ cd rda-venv  $ source bin/activate (rda-venv)$` |

**Step-3:**

Install docker-compose tool needed to install RDA as shown below

|     |     |
| --- | --- |
| [1](#__codelineno-24-1)<br>[2](#__codelineno-24-2)<br>[3](#__codelineno-24-3)<br>[4](#__codelineno-24-4) | `(rda-venv)$  pip3 install docker-compose (rda-venv)$  docker-compose --version docker-compose version 1.29.0, build 07737305 (rda-venv)$` |

**Note:** _Make sure docker-compose is installed properly_

**Step-4:**

Create the following directory structure after logging into Linux machine for setting up directory structure for the first RDA Studio

`[](#__codelineno-25-1) mkdir -p /Users/$(whoami)/rda_studio/cfxdx/home [](#__codelineno-25-2) mkdir -p /Users/$(whoami)/rda_studio/cfxdx/config/network_config [](#__codelineno-25-3) mkdir -p /Users/$(whoami)/rda_studio/cfxdx/output`

**Note:** Above /home/$(whoami) is example User's home directory. Users can update as per mac user account.

**Step-5:**

Create rda-studio.yaml file for RDA studio

`[](#__codelineno-26-1) cd /Users/$(whoami)/rda_studio/ [](#__codelineno-26-2) [](#__codelineno-26-3) cat > rda-studio.yaml << EOF [](#__codelineno-26-4) [](#__codelineno-26-5) services: [](#__codelineno-26-6)   cfxdx: [](#__codelineno-26-7)     image: cfxregistry.cloudfabrix.io/ubuntu-cfxdx-nb-nginx-all:daily [](#__codelineno-26-8)     restart: unless-stopped [](#__codelineno-26-9)     volumes: [](#__codelineno-26-10)       - /Users/$(whoami)/rda_studio/cfxdx/home:/root [](#__codelineno-26-11)       - /Users/$(whoami)/rda_studio/cfxdx/config:/tmp/config [](#__codelineno-26-12)       - /Users/$(whoami)/rda_studio/cfxdx/output:/tmp/output [](#__codelineno-26-13)       - /Users/$(whoami)/rda_studio/cfxdx/config/network_config:/network_config [](#__codelineno-26-14)     ports: [](#__codelineno-26-15)       - "9998:9998" [](#__codelineno-26-16)       - "443:443" [](#__codelineno-26-17)     environment: [](#__codelineno-26-18)       NLTK_DATA : "/root/nltk_data" [](#__codelineno-26-19)       CFXDX_CONFIG_FILE: /tmp/config/conf.yml [](#__codelineno-26-20)       RDA_NETWORK_CONFIG: /network_config/config.json [](#__codelineno-26-21)       RDA_USER: rdademo [](#__codelineno-26-22)       RDA_PASSWORD: rdademo1234 [](#__codelineno-26-23) [](#__codelineno-26-24) EOF`

**Step-6:**

The RDA Stdio node registers and communicates with the RDAF platform using a configuration file that contains your tenant ID, data fabric access tokens, and object storage credentials.

Download RDA Fabric Configuration from the portal by going to `Configuration --> RDA Administration --> Network` and copy it to the local filesystem where the worker node is going to be installed.

*   Save the file as `config.json`

![RDAFNetworkConfig](https://bot-docs.cloudfabrix.io/images/rda-network-config.png)

**Step-7:**

*   Copy the downloaded RDA Fabric configuration file as shown below.

`[](#__codelineno-27-1) cp config.json /Users/$(whoami)/rda_studio/cfxdx/config/network_config/config.json`

**Step-8:**

Docker Login

Run the below command to create and save the docker login session into CloudFabrix's secure docker repository.

`[](#__codelineno-28-1) docker login -u='readonly' -p='readonly' cfxregistry.cloudfabrix.io`

Tip

**Note-1:** Make sure docker is up and running before Step-9

**Step-9:**

`[](#__codelineno-29-1) cd /Users/$(whoami)/rda_studio [](#__codelineno-29-2) [](#__codelineno-29-3) docker-compose -f rda-studio.yaml pull [](#__codelineno-29-4) docker-compose -f rda-studio.yaml up -d`

**Step-10:**

To access RDA Studio interface, open up a browser and enter the URL as https://ipaddress:9998 OR https://ipaddress:443

**Note:** _Access RDA using https://rda-studio-ip-address:9998/ OR https://rda-studio-ip-address:443  
_

_The default user name is rdademo and the password is rdademo1234_  
  
![RDA related files](https://bot-docs.cloudfabrix.io/images/rda_studio_ui_password_macos.png)

Default landing page of RDA Studio on Mac OS

**Note:** Default username/password can be changed from docker-compose.yml file under RDA studio install directory.

|     |     |
| --- | --- |
| [1](#__codelineno-30-1)<br>[2](#__codelineno-30-2)<br>[3](#__codelineno-30-3)<br>[4](#__codelineno-30-4) | `environment:   CFXDX_CONFIG_FILE: /tmp/config/conf.yml   RDA_USER: rdademo   RDA_PASSWORD: rdademo1234` |

**Note:** _Default username/password can be changed from docker-compose.yml file under RDA install directory._  

4\. Windows OS Environment
--------------------------

**Note:** Please check the [Prerequisites](#1-prerequisites)
 - Installation Prerequisites before you proceed.

**Note:** Make sure the below commands are in the PATH variable in the user's login profile.

Verify Prerequisites

Make sure the below commands are in the PATH variable in the user's login profile.

Run the below commands to verify currently installed RDA prerequisites.

`[](#__codelineno-31-1) docker.exe --version [](#__codelineno-31-2) OR [](#__codelineno-31-3) docker --version`

`[](#__codelineno-32-1) docker-compose.exe --version [](#__codelineno-32-2) OR [](#__codelineno-32-3) docker-compose --version`

`[](#__codelineno-33-1) python3.exe --version [](#__codelineno-33-2) OR  [](#__codelineno-33-3) python3 --version`

`[](#__codelineno-34-1) pip3.exe --version [](#__codelineno-34-2) OR [](#__codelineno-34-3) pip3 --version`

**Step-1:**  
Create the following directory structure after logging into Windows machine for setting up directory structure for the RDA Studio.

Tip

Assumption is that, user will execute the below commands from "C:\\" directory.

`[](#__codelineno-35-1) C:\ [](#__codelineno-35-2) C:\mkdir rda_studio [](#__codelineno-35-3) C:\mkdir rda_studio\cfxdx\home [](#__codelineno-35-4) C:\mkdir rda_studio\cfxdx\config\network_config [](#__codelineno-35-5) C:\mkdir rda_studio\cfxdx\output`

**Step-2:**  
Create rda-studio.yaml file for RDA studio using your favorite studio (notepad or wordpad). You can copy the following rda-studio.yaml content to a file 'rda-studio.yaml and copy to the following location --> C:\\rda\_studio\\

Tip

Copy and paste the following lines to C:\\rda\_studio\\rda-studio.yaml using your favorite editor and save the file.

`[](#__codelineno-36-1) services: [](#__codelineno-36-2)   cfxdx: [](#__codelineno-36-3)     image: cfxregistry.cloudfabrix.io/ubuntu-cfxdx-nb-nginx-all:daily [](#__codelineno-36-4)     restart: unless-stopped [](#__codelineno-36-5)     volumes: [](#__codelineno-36-6)       - C:\\rda_studio\\cfxdx\\home\\:/root [](#__codelineno-36-7)       - C:\\rda_studio\cfxdx\\config\\:/tmp/config/ [](#__codelineno-36-8)       - C:\\rda_studio\\cfxdx\\output\\:/tmp/output/ [](#__codelineno-36-9)       - C:\\rda_studio\\cfxdx\config\\network_config\\:/network_config [](#__codelineno-36-10)     ports: [](#__codelineno-36-11)       - "9998:9998" [](#__codelineno-36-12)       - "443:443" [](#__codelineno-36-13)     environment: [](#__codelineno-36-14)       NLTK_DATA : "/root/nltk_data" [](#__codelineno-36-15)       CFXDX_CONFIG_FILE: /tmp/config/conf.yml [](#__codelineno-36-16)       RDA_NETWORK_CONFIG: /network_config/config.json [](#__codelineno-36-17)       RDA_USER: rdademo [](#__codelineno-36-18)       RDA_PASSWORD: rdademo1234`

**Step-3:**  
Once the above yaml content is saved to rda-studio.yaml file, copy the file to following location.

`[](#__codelineno-37-1) C:\copy rda-studio.yaml C:\rda_studio`

**Step-4:**  

The RDA Stdio node registers and communicates with the RDAF platform using a configuration file that contains your tenant ID, data fabric access tokens, and object storage credentials.

Download RDA Fabric Configuration from the portal by going to `Configuration --> RDA Administration --> Network` and copy it to the local filesystem where the worker node is going to be installed.

*   Save the file as `config.json`

![RDAFNetworkConfig](https://bot-docs.cloudfabrix.io/images/rda-network-config.png)

**Step-5:**  

*   Copy the downloaded RDA Fabric configuration file as shown below.

`[](#__codelineno-38-1) copy config.json C:\rda_studio\cfxdx\config\network_config\config.json`

**Step-6:**  

Docker Login

Run the below command to create and save the docker login session into CloudFabrix's secure docker repository.

`[](#__codelineno-39-1) docker login -u='readonly' -p='readonly' cfxregistry.cloudfabrix.io`

Tip

**Note-1:** Make sure docker is up and running before Step-7

**Step-7:**

`[](#__codelineno-40-1) cd C:\rda_studio\ [](#__codelineno-40-2) [](#__codelineno-40-3) docker-compose -f rda-studio.yaml pull [](#__codelineno-40-4) docker-compose -f rda-studio.yaml up -d`

**Step-8:**

To access RDA Studio interface, open up a browser and enter the URL as https://ipaddress:9998 OR https://ipaddress:443

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!