 



# Installing OIA (Operations Intelligence & Analytics)

This document provides instructions about fresh Installation & Upgrades for **OIA application (Operations Intelligence & Analytics, a.k.a AIOps)**. It is an application that is installed on top of RDA Fabric platform.

## **1\. Setup & Install**

**Pre-requisites:**

Below are the pre-requisites which need to be in place before installing the OIA (AIOps) application services.

**RDAF Deployment CLI Version:** 1.2.1

**RDAF Infrastructure Services Tag Version:** 1.0.3

**RDAF Core Platform & Worker Services Tag Version:** 3.4.1

**RDAF Client (RDAC) Tag Version:** 3.4.1

*   [**Install and Configure RDAF Deployment CLI (for Non-Kubernetes or Kubernetes)**](https://bot-docs.cloudfabrix.io/installation_guides/rdaf_cli/)
    
*   [**Setup & Configure Docker On-premise Registry**](https://bot-docs.cloudfabrix.io/installation_guides/rdaf_cli/#131-rdaf-setregistry)
     and download all RDAF Platform's service images (**Infrastructure, Core Platform, Application and Worker services**)
*   [**Setup and Install RDAF Infrastructure and Platform services**](https://bot-docs.cloudfabrix.io/installation_guides/rdaf_cli/#132-rdaf-setup)
    
*   [**Install RDAF Worker services**](https://bot-docs.cloudfabrix.io/installation_guides/rdaf_cli/#136-rdaf-worker)
    
*   [**Setup and Install RDAC CLI**](https://bot-docs.cloudfabrix.io/installation_guides/rdaf_cli/#139-rdaf-rdac_cli)
    

Warning

Please complete all of the above pre-requisites before installing the OIA (AIOps) application services.

Login as **rdauser** user into on-premise docker registry or RDA Fabric Platform VM on which **RDAF deployment CLI** was installed (ex: putty)

Before installing the **OIA (AIOps)** application services, please run the below command to update HAProxy (Loadbalancer) configuration.

[Kubernetes](#__tabbed_1_1)
[Non-Kubernetes](#__tabbed_1_2)
```
 rdafk8s app update-config OIA

```
```
 rdaf app update-config OIA

```

Run the below `rdaf` or `rdafk8s`command, to make sure all of the **RDAF infrastructure services** are up and running.

[Kubernetes](#__tabbed_2_1)
[Non-Kubernetes](#__tabbed_2_2)
```
 rdafk8s infra status

```
```
 rdaf infra status

```

Run the below `rdac pods` command, to make sure all of the **RDAF core platform and worker services** are up and running.
```
 rdac pods

```

[Example Output](#__tabbed_3_1)
```
 +-------+----------------------------------------+----------------+----------+-------------+----------+--------+--------------+---------------+--------------+ 
 | Cat   | Pod-Type                               | Host           | ID       | Site        | Age      |   CPUs |   Memory(GB) | Active Jobs   | Total Jobs   | 
 |-------+----------------------------------------+----------------+----------+-------------+----------+--------+--------------+---------------+--------------| 
 | App   | asset-dependency                       | rda-asset-depe | 090669bf |             | 20:18:21 |      8 |        47.03 |               |              | 
 | App   | authenticator                          | rda-identity-5 | 57905b20 |             | 20:19:11 |      8 |        47.03 |               |              | 
 | App   | cfxdimensions-app-access-manager       | rda-access-man | 6338ad29 |             | 20:18:44 |      8 |        47.03 |               |              | 
 | App   | cfxdimensions-app-notification-service | rda-notificati | bb9e3e7b |             | 20:09:52 |      8 |        31.33 |               |              | 
 | App   | cfxdimensions-app-resource-manager     | rda-resource-m | e5a28e16 |             | 20:18:34 |      8 |        47.03 |               |              | 
 | App   | user-preferences                       | rda-user-prefe | fd09d3ba |             | 20:18:08 |      8 |        47.03 |               |              | 
 | Infra | api-server                             | rda-api-server | b1b910d9 |             | 20:19:22 |      8 |        47.03 |               |              | 
 | Infra | collector                              | rda-collector- | 99553e51 |             | 20:18:17 |      8 |        47.03 |               |              | 
 | Infra | registry                               | rda-registry-7 | a46cd712 |             | 20:19:15 |      8 |        47.03 |               |              | 
 | Infra | scheduler                              | rda-scheduler- | d5537051 | *leader*    | 20:18:26 |      8 |        47.03 |               |              | 
 | Infra | worker                                 | rda-worker-54d | 1f769792 | rda-site-01 | 20:06:48 |      4 |        15.6  | 0             | 0            | 
 +-------+----------------------------------------+----------------+----------+-------------+----------+--------+--------------+---------------+--------------+

```

Run the below `rdac healthcheck` command to check the health status of all of the **RDAF core platform and worker services**.

All of the dependency checks should show as **ok** under **Status** column.
```
 rdac healthcheck

```

[Example Output](#__tabbed_4_1)
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
 | rda_infra | worker                                 | rda-worker-5 | 1f769792 | rda-site-01 | service-status                                      | ok       |                                                       | 
 | rda_infra | worker                                 | rda-worker-5 | 1f769792 | rda-site-01 | minio-connectivity                                  | ok       |                                                       | 
 +-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-------------------------------------------------------+

```

**Installing OIA (AIOps) Application Services:**

Set RDA Fabric platform's application configuration as `aiops` using the below command.
```
 rdac rda-app-configure --type aiops

```

Note

Other supported options for above command are below:

*   `rda`: Choose this option when **only RDA Fabric platform** need to be installed along with RDA Worker and RDA Event Gateway services without AIOps (OIA) or Asset Intelligence (AIA) applications.
    
*   `aiops`: Choose this option when **Operations Intelligence (OIA, a.k.a AIOps)** application need to be installed.
    
*   `asset`: Choose this option when **Asset Intelligence (AIA)** application need to be installed. (**Note:** AIA application type is deprecated and all of it's capabilities are available through base RDA Fabric platform itself. For more information, please contact cfx-support@cloudfabric.com)
    
*   `all`: Choose this option, when all of the supported applications need to be installed.
    

Run the below command to deploy RDAF OIA (AIOps) application services. (Note: Below shown tag name is a sample one for a reference only, for actual tag, please contact CloudFabrix support team at **support@cloudfabrix.com**)

[Kubernetes](#__tabbed_5_1)
[Non-Kubernetes](#__tabbed_5_2)
```
 rdafk8s app install OIA --tag 7.4.1

```
```
 rdaf app install OIA --tag 7.4.1

```

After installing the OIA (AIOps) application services, run the below command to see the running status of the deployed application services.

[Kubernetes](#__tabbed_6_1)
[Non-Kubernetes](#__tabbed_6_2)
```
 rdafk8s app status

```

[Example Output](#__tabbed_7_1)
```
 +---------------------------------+----------------+-----------------+--------------+-------+ 
 | Name                            | Host           | Status          | Container Id | Tag   | 
 +---------------------------------+----------------+-----------------+--------------+-------+ 
 | rda-alert-ingester              | 192.168.125.46 | Up 20 Hours ago | 610bb0e286d6 | 7.4.1 | 
 | rda-alert-processor             | 192.168.125.46 | Up 20 Hours ago | 79ee6788f73e | 7.4.1 | 
 | rda-app-controller              | 192.168.125.46 | Up 20 Hours ago | 6c672102d5ff | 7.4.1 | 
 | rda-collaboration               | 192.168.125.46 | Up 20 Hours ago | 34f25c05afce | 7.4.1 | 
 | rda-configuration-service       | 192.168.125.46 | Up 20 Hours ago | 112ccaf4b0e6 | 7.4.1 | 
 | rda-dataset-caas-all-alerts     | 192.168.125.46 | Up 20 Hours ago | 2b48d4dfbfd0 | 7.4.1 | 
 | rda-dataset-caas-current-alerts | 192.168.125.46 | Up 20 Hours ago | 03cdc77ddf1f | 7.4.1 | 
 | rda-event-consumer              | 192.168.125.46 | Up 20 Hours ago | 21113ba951a1 | 7.4.1 | 
 | rda-file-browser                | 192.168.125.46 | Up 20 Hours ago | 425dac228fc9 | 7.4.1 | 
 | rda-ingestion-tracker           | 192.168.125.46 | Up 20 Hours ago | 8a984a536a97 | 7.4.1 | 
 | rda-irm-service                 | 192.168.125.46 | Up 20 Hours ago | 258aadc0c1af | 7.4.1 | 
 | rda-ml-config                   | 192.168.125.46 | Up 20 Hours ago | bf23d58903f7 | 7.4.1 | 
 | rda-notification-service        | 192.168.125.46 | Up 20 Hours ago | a15c5232b25d | 7.4.1 | 
 | rda-reports-registry            | 192.168.125.46 | Up 20 Hours ago | 3890b5dfb8ae | 7.4.1 | 
 | rda-smtp-server                 | 192.168.125.46 | Up 20 Hours ago | 6aadab781947 | 7.4.1 | 
 | rda-webhook-server              | 192.168.125.46 | Up 20 Hours ago | 6bf555aed18b | 7.4.1 | 
 +---------------------------------+--------------+-----------------+--------------+-------+

```
```
 rdaf app status

```

[Example Output](#__tabbed_8_1)
```
 +---------------------------------+----------------+-----------------+--------------+-------+ 
 | Name                            | Host           | Status          | Container Id | Tag   | 
 +---------------------------------+----------------+-----------------+--------------+-------+ 
 | rda-alert-ingester              | 192.168.125.46 | Up 20 Hours ago | 610bb0e286d6 | 7.4.1 | 
 | rda-alert-processor             | 192.168.125.46 | Up 20 Hours ago | 79ee6788f73e | 7.4.1 | 
 | rda-app-controller              | 192.168.125.46 | Up 20 Hours ago | 6c672102d5ff | 7.4.1 | 
 | rda-collaboration               | 192.168.125.46 | Up 20 Hours ago | 34f25c05afce | 7.4.1 | 
 | rda-configuration-service       | 192.168.125.46 | Up 20 Hours ago | 112ccaf4b0e6 | 7.4.1 | 
 | rda-dataset-caas-all-alerts     | 192.168.125.46 | Up 20 Hours ago | 2b48d4dfbfd0 | 7.4.1 | 
 | rda-dataset-caas-current-alerts | 192.168.125.46 | Up 20 Hours ago | 03cdc77ddf1f | 7.4.1 | 
 | rda-event-consumer              | 192.168.125.46 | Up 20 Hours ago | 21113ba951a1 | 7.4.1 | 
 | rda-file-browser                | 192.168.125.46 | Up 20 Hours ago | 425dac228fc9 | 7.4.1 | 
 | rda-ingestion-tracker           | 192.168.125.46 | Up 20 Hours ago | 8a984a536a97 | 7.4.1 | 
 | rda-irm-service                 | 192.168.125.46 | Up 20 Hours ago | 258aadc0c1af | 7.4.1 | 
 | rda-ml-config                   | 192.168.125.46 | Up 20 Hours ago | bf23d58903f7 | 7.4.1 | 
 | rda-notification-service        | 192.168.125.46 | Up 20 Hours ago | a15c5232b25d | 7.4.1 | 
 | rda-reports-registry            | 192.168.125.46 | Up 20 Hours ago | 3890b5dfb8ae | 7.4.1 | 
 | rda-smtp-server                 | 192.168.125.46 | Up 20 Hours ago | 6aadab781947 | 7.4.1 | 
 | rda-webhook-server              | 192.168.125.46 | Up 20 Hours ago | 6bf555aed18b | 7.4.1 | 
 +---------------------------------+--------------+-----------------+--------------+-------+

```

**Configuring OIA (AIOps) Application:**

Login into RDAF portal as **admin@cfx.com** user.

Create a new **Service Blueprint** for OIA (AIOps) application and Machine Learning (ML) application.

**For OIA (AIOps) Application:** Go to **Main Menu** --> **Configuration** --> **Artifacts** --> **Service Blueprints** --> **View details** --> Click on **Add** and copy & paste the below configuration and Click on **Save**
```
 name: cfxOIA 
 id: 81a1a2202 
 version: 2023_02_12_01 
 category: ITOM 
 comment: Operations Intelligence & Analytics (AIOps) 
 enabled: true 
 type: Service 
 provider: CloudFabrix Software, Inc. 
 attrs: {} 
 apps: 
     -   label: cfxOIA 
         appType: dimensions 
         appName: incident-room-manager 
         icon_url: /assets/img/applications/OIA.png 
         permission: app:irm:read 
 service_pipelines: []

```

**For Machine Learning (ML) Application:** Go to **Main Menu** --> **Configuration** --> **Artifacts** --> **Service Blueprints** --> **View details** --> Click on **Add** and copy & paste the below configuration and Click on **Save**
```
 name: cfxML 
 id: 81a1a030 
 version: 2023_02_12_01 
 category: ITOM 
 comment: Machine Learning (ML) Experiments 
 enabled: true 
 type: Service 
 provider: CloudFabrix Software, Inc. 
 attrs: {} 
 apps: 
     -   label: cfxML 
         appType: dimensions 
         appName: ml-config 
         icon_url: /assets/img/applications/ML.png 
         permission: app:irm:read 
 service_pipelines: []

```

![CFXOIA_App_ML_App_Add](https://bot-docs.cloudfabrix.io/images/oia/cfxoia_app_ml_app_add.png)

## **2\. Upgrades**

Please refer to the following documents for guidance on upgrading the OIA (AIOps) application services to the newer version.

### **2.1 Latest Version**

*   [**Upgrade Document From 7.4/7.4.1 to 7.4.2/7.4.2.1**](/installation_guides/oia_upgrades/upgrade_to_3.4.2_and_7.4.2/)
    

### **2.2 Previous Versions**

*   [**Upgrade Document From 7.3/7.4 to 7.4.1**](/installation_guides/oia_upgrades/upgrade_to_3.4.1_and_7.4.1/)
    
*   [**Upgrade Document From 7.3 to 7.4**](/installation_guides/oia_upgrades/upgrade_to_3.4_and_7.4/)
    
*   [**Upgrade Document From 7.2.2.2 to 7.3**](/installation_guides/oia_upgrades/upgrade_to_3.3_and_7.3/)
    
*   [**Upgrade Document From 7.2.2.1 to 7.2.2.2**](/installation_guides/oia_upgrades/archived/upgrade_to_3.2.2.2_and_7.2.2.2/)
    
*   [**Upgrade Document From 7.2.1.x to 7.2.2.1**](/installation_guides/oia_upgrades/archived/upgrade_to_3.2.1.3_and_7.2.2.1/)
    
*   [**Upgrade Document From 7.2.1.x to 7.2.2**](/installation_guides/oia_upgrades/archived/upgrade_to_3.2.1.x_and_7.2.2/)
    

### **2.3 Archived Versions**

*   [**Upgrade Document From 7.2.0.x to 7.2.1.1**](/installation_guides/oia_upgrades/archived/upgrade_to_3.2.1.3_and_7.2.1.1_and_7.2.1.5/)
    
*   [**Upgrade Document From 7.0.x to 7.0.6**](/installation_guides/oia_upgrades/archived/upgrade_to_3.1.0_and_7.0.6/)
    

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!