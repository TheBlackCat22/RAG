 



Guide to RDAF Start, Stop Operations
====================================

This section explains how to safely start and stop the RDAF infrastructure, platform, application and worker services.

**1\. Starting RDAF Services**
------------------------------

Login into RDAF platform VM using SSH client as **rdauser** for CLI access and start the below RDAF services in sequence.

*   Infrastructure Services
*   Platform Services
*   Worker Services
*   Application Services

**Starting RDAF infrastructure services:**

`[](#__codelineno-0-1) rdaf infra up`

Verify RDAF infrastructure services status and make sure all of them are up & running.

`[](#__codelineno-1-1) rdaf infra status`

Example Output

`[](#__codelineno-2-1) +----------------+-----------------+---------------+--------------+--------------------------+ [](#__codelineno-2-2) | Name           | Host            | Status        | Container Id | Tag                      | [](#__codelineno-2-3) +----------------+-----------------+---------------+--------------+--------------------------+ [](#__codelineno-2-4) | haproxy        | 192.168.125.143 | Up 41 seconds | b68f8335d8ff | 1.0.1                    | [](#__codelineno-2-5) | haproxy        | 192.168.125.144 | Up 41 seconds | 9df14432767c | 1.0.1                    | [](#__codelineno-2-6) | keepalived     | 192.168.125.143 | active        | N/A          | N/A                      | [](#__codelineno-2-7) | keepalived     | 192.168.125.144 | active        | N/A          | N/A                      | [](#__codelineno-2-8) | nats           | 192.168.125.143 | Up 38 seconds | 4f1413239096 | 1.0.1                    | [](#__codelineno-2-9) | nats           | 192.168.125.144 | Up 38 seconds | 0762f5ef3d5e | 1.0.1                    | [](#__codelineno-2-10) | minio          | 192.168.125.143 | Up 37 seconds | c93731b02f95 | RELEASE.2022-05-08T23-50 | [](#__codelineno-2-11) |                |                 |               |              | -31Z                     | [](#__codelineno-2-12) | minio          | 192.168.125.144 | Up 37 seconds | 1b2b545cbd4a | RELEASE.2022-05-08T23-50 | [](#__codelineno-2-13) |                |                 |               |              | -31Z                     | [](#__codelineno-2-14) | minio          | 192.168.125.145 | Up 37 seconds | 289f96a2832e | RELEASE.2022-05-08T23-50 | [](#__codelineno-2-15) |                |                 |               |              | -31Z                     | [](#__codelineno-2-16) | minio          | 192.168.125.146 | Up 36 seconds | f6571bd5e000 | RELEASE.2022-05-08T23-50 | [](#__codelineno-2-17) |                |                 |               |              | -31Z                     | [](#__codelineno-2-18) | mariadb        | 192.168.125.143 | Up 36 seconds | 4e5ca8860c87 | 1.0.1                    | [](#__codelineno-2-19) | mariadb        | 192.168.125.144 | Up 35 seconds | 2c5a4986a6c1 | 1.0.1                    | [](#__codelineno-2-20) | mariadb        | 192.168.125.145 | Up 35 seconds | cf6656241efa | 1.0.1                    | [](#__codelineno-2-21) | opensearch     | 192.168.125.143 | Up 34 seconds | b04ece438490 | 1.0.1                    | [](#__codelineno-2-22) | opensearch     | 192.168.125.144 | Up 34 seconds | ab53cf0abf6d | 1.0.1                    | [](#__codelineno-2-23) | opensearch     | 192.168.125.145 | Up 34 seconds | 7c75c0cffe4a | 1.0.1                    | [](#__codelineno-2-24) | zookeeper      | 192.168.125.143 | Up 33 seconds | 14b23a0ce5d3 | 1.0.1                    | [](#__codelineno-2-25) | zookeeper      | 192.168.125.144 | Up 33 seconds | 51630587c9c2 | 1.0.1                    | [](#__codelineno-2-26) | zookeeper      | 192.168.125.145 | Up 32 seconds | 1eca7a3a0f70 | 1.0.1                    | [](#__codelineno-2-27) | kafka          | 192.168.125.143 | Up 11 seconds | 0278470dd416 | 1.0.1                    | [](#__codelineno-2-28) | kafka          | 192.168.125.144 | Up 12 seconds | ab3e888056a7 | 1.0.1                    | [](#__codelineno-2-29) | kafka          | 192.168.125.145 | Up 30 seconds | 972b78f159c3 | 1.0.1                    | [](#__codelineno-2-30) | redis          | 192.168.125.143 | Up 30 seconds | 4d3dbd1111f7 | 1.0.1                    | [](#__codelineno-2-31) | redis          | 192.168.125.144 | Up 29 seconds | abe4da626997 | 1.0.1                    | [](#__codelineno-2-32) | redis          | 192.168.125.145 | Up 29 seconds | 9fe580fa5e81 | 1.0.1                    | [](#__codelineno-2-33) | redis-sentinel | 192.168.125.143 | Up 28 seconds | c054e0bcf113 | 1.0.1                    | [](#__codelineno-2-34) | redis-sentinel | 192.168.125.144 | Up 28 seconds | a66fe0d2bdf3 | 1.0.1                    | [](#__codelineno-2-35) | redis-sentinel | 192.168.125.145 | Up 27 seconds | ac523a8c6ffb | 1.0.1                    | [](#__codelineno-2-36) +----------------+---------------+---------------+--------------+--------------------------+`

Info

**Note:** Please wait for 60 seconds before starting RDAF platform services

**Starting RDAF platform services:**

`[](#__codelineno-3-1) rdaf platform up`

Verify RDAF platform services status and make sure all of them are up & running.

`[](#__codelineno-4-1) rdaf platform status`

Example Output

`[](#__codelineno-5-1) +--------------------------+-----------------+---------------+--------------+---------+ [](#__codelineno-5-2) | Name                     | Host            | Status        | Container Id | Tag     | [](#__codelineno-5-3) +--------------------------+-----------------+---------------+--------------+---------+ [](#__codelineno-5-4) | cfx-rda-access-manager   | 192.168.125.141 | Up 42 seconds | e4f20012a888 | 3.0.5.8 | [](#__codelineno-5-5) | cfx-rda-resource-manager | 192.168.125.141 | Up 41 seconds | 52bd03970a53 | 3.0.5.8 | [](#__codelineno-5-6) | cfx-rda-user-preferences | 192.168.125.141 | Up 41 seconds | 289e90b70b85 | 3.0.5.8 | [](#__codelineno-5-7) | portal-backend           | 192.168.125.141 | Up 41 seconds | 1887eb44d63d | 3.0.5.8 | [](#__codelineno-5-8) | portal-frontend          | 192.168.125.141 | Up 40 seconds | 75fd3f691ad8 | 3.0.5.8 | [](#__codelineno-5-9) | rda_api_server           | 192.168.125.141 | Up 39 seconds | fcbbca53641f | 3.0.5.8 | [](#__codelineno-5-10) | rda_asm                  | 192.168.125.141 | Up 38 seconds | f931d1e748ae | 3.0.5.8 | [](#__codelineno-5-11) | rda_asset_dependency     | 192.168.125.141 | Up 37 seconds | e68e03eabe78 | 3.0.5.8 | [](#__codelineno-5-12) | rda_collector            | 192.168.125.141 | Up 36 seconds | 3c65bad1e013 | 3.0.5.8 | [](#__codelineno-5-13) | rda_identity             | 192.168.125.141 | Up 35 seconds | 94d67dcb82b9 | 3.0.5.8 | [](#__codelineno-5-14) | rda_registry             | 192.168.125.141 | Up 34 seconds | 752a0d8dd352 | 3.0.5.8 | [](#__codelineno-5-15) | rda_sched_admin          | 192.168.125.141 | Up 33 seconds | eabc9a908afb | 3.0.5.8 | [](#__codelineno-5-16) | rda_scheduler            | 192.168.125.141 | Up 32 seconds | 1b136bac290f | 3.0.5.8 | [](#__codelineno-5-17) +--------------------------+---------------+---------------+--------------+---------+`

Info

**Note:** Please wait for 60 seconds before starting RDAF worker services

**Starting RDAF worker services:**

`[](#__codelineno-6-1) rdaf worker up`

Verify RDAF worker services status and make sure all of them are up & running.

`[](#__codelineno-7-1) rdaf worker status`

Example Output

`[](#__codelineno-8-1) +------------+-----------------+--------------+--------------+---------+ [](#__codelineno-8-2) | Name       | Host            | Status       | Container Id | Tag     | [](#__codelineno-8-3) +------------+-----------------+--------------+--------------+---------+ [](#__codelineno-8-4) | rda_worker | 192.168.125.149 | Up 30 seconds | 8a933d1b82df | 3.0.5.8 | [](#__codelineno-8-5) | rda_worker | 192.168.125.150 | Up 35 seconds | 2a934r1b52dw | 3.0.5.8 | [](#__codelineno-8-6) +------------+---------------+--------------+--------------+---------+`

**Starting RDAF application services:**

To start OIA application services

`[](#__codelineno-9-1) rdaf app up OIA`

Verify RDAF application services status and make sure all of them are up & running.

`[](#__codelineno-10-1) rdaf app status`

Example Output

`[](#__codelineno-11-1) +--------------------------+-----------------+---------------+--------------+---------+ [](#__codelineno-11-2) | Name                     | Host            | Status        | Container Id | Tag     | [](#__codelineno-11-3) +--------------------------+-----------------+---------------+--------------+---------+ [](#__codelineno-11-4) | all-alerts-cfx-rda-      | 192.168.125.146 | Up 40 seconds | d9aed36ddf4b | 7.0.0.0 | [](#__codelineno-11-5) | dataset-caas             |                 |               |              |         | [](#__codelineno-11-6) | cfx-rda-alert-ingester   | 192.168.125.146 | Up 39 seconds | ef4f031a7b45 | 7.0.0.0 | [](#__codelineno-11-7) | cfx-rda-alert-processor  | 192.168.125.146 | Up 38 seconds | de9de2959dce | 7.0.0.0 | [](#__codelineno-11-8) | cfx-rda-app-builder      | 192.168.125.146 | Up 38 seconds | 438b53f06c61 | 7.0.0.0 | [](#__codelineno-11-9) | cfx-rda-app-controller   | 192.168.125.146 | Up 37 seconds | 2cb10582f881 | 7.0.0.0 | [](#__codelineno-11-10) | cfx-rda-collaboration    | 192.168.125.146 | Up 36 seconds | 407055e4b862 | 7.0.0.0 | [](#__codelineno-11-11) | cfx-rda-configuration-   | 192.168.125.146 | Up 35 seconds | b7b08bcb923e | 7.0.0.0 | [](#__codelineno-11-12) | service                  |                 |               |              |         | [](#__codelineno-11-13) | cfx-rda-event-consumer   | 192.168.125.146 | Up 35 seconds | 73ef798cf0bf | 7.0.0.0 | [](#__codelineno-11-14) | cfx-rda-file-browser     | 192.168.125.146 | Up 34 seconds | 12135eeccb2d | 7.0.0.0 | [](#__codelineno-11-15) | cfx-rda-ingestion-       | 192.168.125.146 | Up 33 seconds | a2010475d060 | 7.0.0.0 | [](#__codelineno-11-16) | tracker                  |                 |               |              |         | [](#__codelineno-11-17) | cfx-rda-irm-service      | 192.168.125.146 | Up 32 seconds | 0e969df37ad0 | 7.0.0.0 | [](#__codelineno-11-18) | cfx-rda-ml-config        | 192.168.125.146 | Up 31 seconds | c907949bff1d | 7.0.0.0 | [](#__codelineno-11-19) | cfx-rda-notification-    | 192.168.125.146 | Up 31 seconds | 215c67affb68 | 7.0.0.0 | [](#__codelineno-11-20) | service                  |                 |               |              |         | [](#__codelineno-11-21) | cfx-rda-reports-registry | 192.168.125.146 | Up 30 seconds | 21828b867a03 | 7.0.0.0 | [](#__codelineno-11-22) | cfx-rda-smtp-server      | 192.168.125.146 | Up 29 seconds | ee6c90d25afe | 7.0.0.0 | [](#__codelineno-11-23) | cfx-rda-webhook-server   | 192.168.125.146 | Up 28 seconds | 4659fe639e3c | 7.0.0.0 | [](#__codelineno-11-24) | current-alerts-cfx-rda-  | 192.168.125.146 | Up 27 seconds | 9c6d30851fe3 | 7.0.0.0 | [](#__codelineno-11-25) | dataset-caas             |                 |               |              |         | [](#__codelineno-11-26) +--------------------------+---------------+---------------+--------------+---------+`

**2\. Stopping RDAF Services**
------------------------------

Login into RDAF platform VM using SSH client as **rdauser** for CLI access and stop the below RDAF services in sequence.

*   Application Services
*   Worker Services
*   Platform Services
*   Infrastructure Services

To stop RDAF OIA application services, run the below command. Wait until all of the services are stopped.

`[](#__codelineno-12-1) rdaf app down OIA`

To stop RDAF worker services, run the below command. Wait until all of the services are stopped.

`[](#__codelineno-13-1) rdaf worker down`

To stop RDAF platform services, run the below command. Wait until all of the services are stopped.

`[](#__codelineno-14-1) rdaf platform down`

To stop RDAF infrastructure services, run the below command. Wait until all of the services are stopped.

`[](#__codelineno-15-1) rdaf infra down`

**3\. MariaDB Cluster Service**
-------------------------------

MariaDB is a relational database service that is used to store RDAF platform's user configuration, platform & application service configuration and it's data. RDAF applications such as OIA and AIA uses MariaDB to store alerts, incidents, asset inventory data etc. MariaDB supports high availability natively and it can be deployed as **Master/Slave** or **Master/Master** configuration using the Galera clustering feature. Within the RDAF platform, MariaDB is deployed as **Master/Master** (Galera cluster) node configuration. MariaDB service is containerized and configured in a specific way to be compatible with RDAF platform and its application services.

For detailed general documentation, please refer to [About MariaDB](https://mariadb.org/documentation/)
 and [About Galera Cluster](https://mariadb.com/kb/en/what-is-mariadb-galera-cluster/)

**MariaDB database mount point on each cluster node:**

*   Data mount point: `/var/mysql`
    
*   DB service logs path: `/opt/rdaf/logs/mariadb/mariadb.log`
    

**MariaDB Galera Cluster graceful start & stop sequence:**

KubernetesNon-Kubernetes

Run the below RDAF CLI command from the VM it was installed to start 3 node MariaDB cluster service.

`[](#__codelineno-16-1) rdafk8s infra up --service mariadb`

The above command brings up each MariaDB Node in sequential order. It brings up `rda-mariadb-mariadb-galera-0` first to bootstrap the cluster and starts the `rda-mariadb-mariadb-galera-1` & `rda-mariadb-mariadb-galera-2` subsequently to join the MariaDB Galera cluster.

Run the below RDAF CLI command to check mariadb service's UP status.

`[](#__codelineno-17-1) rdafk8s infra status | grep mariadb`

Example Output

`[](#__codelineno-18-1) | mariadb        | 192.168.125.143 | Up 4 weeks | ebcc659a4e07 | 1.0.2              | [](#__codelineno-18-2) | mariadb        | 192.168.125.144 | Up 4 weeks | 89607a3feb76 | 1.0.2              | [](#__codelineno-18-3) | mariadb        | 192.168.125.145 | Up 4 weeks | 482cb9c1e3b3 | 1.0.2              |`

Please run the below command and wait till all of the **mariadb** pods are in **Running** state and **Ready** status is **1/1**

`[](#__codelineno-19-1) kubectl get pods -n rda-fabric -l app_category=rdaf-infra | grep -i mariadb`

Run the below commands to check the status of the **mariadb** cluster. Please verify that the cluster state is in **Synced** state.

``[](#__codelineno-20-1) MARIADB_HOST=`cat /opt/rdaf/rdaf.cfg | grep -A3 mariadb | grep datadir | awk '{print $3}' | cut -f1 -d'/'` [](#__codelineno-20-2) [](#__codelineno-20-3) MARIADB_USER=`cat /opt/rdaf/rdaf.cfg | grep -A3 mariadb | grep user | awk '{print $3}' | base64 -d` [](#__codelineno-20-4) [](#__codelineno-20-5) MARIADB_PASSWORD=`cat /opt/rdaf/rdaf.cfg | grep -A3 mariadb | grep password | awk '{print $3}' | base64 -d` [](#__codelineno-20-6) [](#__codelineno-20-7) mysql -u$MARIADB_USER -p$MARIADB_PASSWORD -h $MARIADB_HOST -P3307 -e "show status like 'wsrep_local_state_comment';"``

Example Output

`[](#__codelineno-21-1) +---------------------------+--------+ [](#__codelineno-21-2) | Variable_name             | Value  | [](#__codelineno-21-3) +---------------------------+--------+ [](#__codelineno-21-4) | wsrep_local_state_comment | Synced | [](#__codelineno-21-5) +---------------------------+--------+`

Run the below commands to check the cluster size of the **mariadb** cluster. Please verify that the cluster size is **3**.

`[](#__codelineno-22-1) mysql -u$MARIADB_USER -p$MARIADB_PASSWORD -h $MARIADB_HOST -P3307 -e "SHOW GLOBAL STATUS LIKE 'wsrep_cluster_size'";`

Example Output

`[](#__codelineno-23-1) +--------------------+-------+ [](#__codelineno-23-2) | Variable_name      | Value | [](#__codelineno-23-3) +--------------------+-------+ [](#__codelineno-23-4) | wsrep_cluster_size | 3     | [](#__codelineno-23-5) +--------------------+-------+`

Note

Once the MariaDB Galera cluster is functionally up and running, the determination of the **bootstrap node** next time to start the cluster depends on the shutdown sequence of the cluster nodes. The cluster node which was stopped last will be used to bootstrap the MariaDB Galera cluster next time.

Run the below rdaf CLI command to stop the MariaDB cluster service on 3 nodes gracefully.

`[](#__codelineno-24-1) rdafk8s infra down --service mariadb`

The above command stops the `rda-mariadb-mariadb-galera-2` first, `rda-mariadb-mariadb-galera-1` next, and finally the `rda-mariadb-mariadb-galera-0`. In this sequence, since `rda-mariadb-mariadb-galera-0` is stopped last, `rda-mariadb-mariadb-galera-0` always becomes the **bootstrap node** to start and initializes the Galera cluster appropriately.

Info

Three node MariaDB Galera cluster provides high availability with **a tolerance of 1 node failure**.

Run the below RDAF CLI command from the VM it was installed to start 3 node MariaDB cluster service.

`[](#__codelineno-25-1) rdaf infra up --service mariadb`

Run the below RDAF CLI command to check mariadb service's UP status.

`[](#__codelineno-26-1) rdaf infra status | grep mariadb`

Example Output

`[](#__codelineno-27-1) | mariadb        | 192.168.125.143 | Up 4 weeks | ebcc659a4e07 | 1.0.1              | [](#__codelineno-27-2) | mariadb        | 192.168.125.144 | Up 4 weeks | 89607a3feb76 | 1.0.1              | [](#__codelineno-27-3) | mariadb        | 192.168.125.145 | Up 4 weeks | 482cb9c1e3b3 | 1.0.1              |`

Run the below RDAF CLI command to check mariadb service's functional health check status.

`[](#__codelineno-28-1) rdaf infra healthcheck | grep mariadb`

Example Output

`[](#__codelineno-29-1) 2022-10-28 20:52:31,926 [rdaf.cmd.infra] INFO     - Running Health Check on mariadb on host 192.168.125.143 [](#__codelineno-29-2) 2022-10-28 20:52:32,313 [rdaf.cmd.infra] INFO     - Running Health Check on mariadb on host 192.168.125.144 [](#__codelineno-29-3) 2022-10-28 20:52:32,657 [rdaf.cmd.infra] INFO     - Running Health Check on mariadb on host 192.168.125.145 [](#__codelineno-29-4) | mariadb        | Port Connection | OK     | N/A             | 192.168.125.143 | ebcc659a4e07 | [](#__codelineno-29-5) | mariadb        | Service Status  | OK     | N/A             | 192.168.125.143 | ebcc659a4e07 | [](#__codelineno-29-6) | mariadb        | Firewall Port   | OK     | N/A             | 192.168.125.143 | ebcc659a4e07 | [](#__codelineno-29-7) | mariadb        | Port Connection | OK     | N/A             | 192.168.125.144 | 89607a3feb76 | [](#__codelineno-29-8) | mariadb        | Service Status  | OK     | N/A             | 192.168.125.144 | 89607a3feb76 | [](#__codelineno-29-9) | mariadb        | Firewall Port   | OK     | N/A             | 192.168.125.144 | 89607a3feb76 | [](#__codelineno-29-10) | mariadb        | Port Connection | OK     | N/A             | 192.168.125.145 | 482cb9c1e3b3 | [](#__codelineno-29-11) | mariadb        | Service Status  | OK     | N/A             | 192.168.125.145 | 482cb9c1e3b3 | [](#__codelineno-29-12) | mariadb        | Firewall Port   | OK     | N/A             | 192.168.125.145 | 482cb9c1e3b3 |`

The above command brings up each MariaDB Node in sequential order. It brings up Node01 first to bootstrap the cluster and starts the Node02 & Node03 subsequently to join the MariaDB Galera cluster.

When Node01 is started first to bootstrap the MariaDB galera cluster, it starts with the below highlighted parameter `MARIADB_GALERA_CLUSTER_BOOTSTRAP` is set to `yes` inside the MariaDB docker-compose YAML file. (**/opt/rdaf/deployment-scripts/cluster-node-ip/infra.yaml**)

  `[](#__codelineno-30-1)   mariadb: [](#__codelineno-30-2)     image: 192.168.125.140:5000/rda-platform-mariadb:1.0.1 [](#__codelineno-30-3)     restart: 'no' [](#__codelineno-30-4)     network_mode: host [](#__codelineno-30-5)     mem_limit: 8G [](#__codelineno-30-6)     memswap_limit: 8G [](#__codelineno-30-7)     oom_kill_disable: false [](#__codelineno-30-8)     volumes: [](#__codelineno-30-9)     - /var/mysql:/bitnami/mariadb/data/ [](#__codelineno-30-10)     - /opt/rdaf/config/mariadb:/opt/bitnami/mariadb/conf/bitnami/ [](#__codelineno-30-11)     - /opt/rdaf/logs/mariadb:/opt/rdaf/log/ [](#__codelineno-30-12)     logging: [](#__codelineno-30-13)       driver: json-file [](#__codelineno-30-14)       options: [](#__codelineno-30-15)         max-size: 10m [](#__codelineno-30-16)         max-file: '5' [](#__codelineno-30-17)     environment: [](#__codelineno-30-18)     - MARIADB_GALERA_MARIABACKUP_USER=rdaf_backup [](#__codelineno-30-19)     ... [](#__codelineno-30-20)     ... [](#__codelineno-30-21)     ... [](#__codelineno-30-22)     - MARIADB_GALERA_CLUSTER_ADDRESS=gcomm://192.168.125.143,192.168.125.144,192.168.125.145 [](#__codelineno-30-23)     - MARIADB_GALERA_CLUSTER_BOOTSTRAP=yes`

Note

Once the MariaDB Galera cluster is functionally up and running, the determination of the **bootstrap node** next time to start the cluster depends on the shutdown sequence of the cluster nodes. The cluster node which was stopped last should be used to bootstrap the MariaDB Galera cluster next time.

Run the below rdaf CLI command to stop the MariaDB cluster service on 3 nodes gracefully.

`[](#__codelineno-31-1) rdaf infra down --service mariadb`

The above command stops the Node03 first, Node02 next, and finally the Node01. In this sequence, since Node01 is stopped last, Node01 always becomes the **bootstrap node** to start and initializes the Galera cluster appropriately.

Info

Three node MariaDB Galera cluster provides high availability with **a tolerance of 1 node failure**.

### **3.1 MariaDB Galera cluster multi-node recovery on power failure or a full crash**

KubernetesNon-Kubernetes

If the MariaDB Galera cluster nodes are crashed because of power failure on all servers or because of some other server hardware failure, the cluster needs to be brought up carefully to avoid any data loss.

Warning

Below steps are only needed if the MariaDB cluster nodes are not able to come up and keep crash-looping while coming up.

For Kubernetes cluster environment, please follow the below steps.

Run the below command to bring down the MariaDB cluster nodes.

`[](#__codelineno-32-1) rdafk8s infra down --service mariadb`

Run the below `kubectl` command to verify all of the MariaDB pods are terminated and deleted.

`[](#__codelineno-33-1) kubectl get pods -n rda-fabric | grep mariadb`

Run the below command to delete the MariaDB stateful-set configuration.

`[](#__codelineno-34-1) helm delete rda-mariadb -n rda-fabric`

Run the below command to get the **MariaDB root user password** from Kubernetes secrets vault.

`[](#__codelineno-35-1) kubectl get secret --namespace rda-fabric rda-mariadb-mariadb-galera -o jsonpath="{.data.mariadb-root-password}" | base64 -d`

Run the below command to get the **MariaDB mariabackup user password** from Kubernetes secrets vault.

`[](#__codelineno-36-1) kubectl get secret --namespace rda-fabric rda-mariadb-mariadb-galera -o jsonpath="{.data.mariadb-galera-mariabackup-password}" | base64 -d`

Danger

*   If you get **empty password** for either of the above commands, please do not proceed further and contact **CloudFabrix support** for further assistance.
    
*   Please make sure to capture both **MariaDB root user's and mariabackup user's passwords** appropriately as these two are **critical** while bringing up the MariaDB cluster nodes.
    

Run the below command to bootstrap the cluster and bring up all of the MariaDB galera cluster nodes.

Note

*   Copy & paste the **MariaDB root user's and mariabackup user's passwords** that you extracted from the Kubernetes secret vault from the above steps.
    
*   Get the MariaDB service's tag version from the `rdafk8s infra status | grep mariadb` command output.
    

`[](#__codelineno-37-1) helm -n rda-fabric install rda-mariadb -f /opt/rdaf/deployment-scripts/mariadb-values.yaml /opt/rdaf/deployment-scripts/helm/rda-mariadb/ \ [](#__codelineno-37-2)   --set rootUser.password=<root user password> \ [](#__codelineno-37-3)   --set galera.mariabackup.password=<mariabackup user password> \ [](#__codelineno-37-4)   --set galera.bootstrap.forceBootstrap=true \ [](#__codelineno-37-5)   --set galera.bootstrap.bootstrapFromNode=1 \ [](#__codelineno-37-6)   --set galera.bootstrap.forceSafeToBootstrap=true \ [](#__codelineno-37-7)   --set podManagementPolicy=Parallel \ [](#__codelineno-37-8)   --set image.tag=<tag_version>`

Example-Output

`[](#__codelineno-38-1) helm -n rda-fabric install rda-mariadb -f /opt/rdaf/deployment-scripts/mariadb-values.yaml /opt/rdaf/deployment-scripts/helm/rda-mariadb/ \ [](#__codelineno-38-2)   --set rootUser.password=YIKy7pm2 \ [](#__codelineno-38-3)   --set galera.mariabackup.password=YIKy7pm2 \ [](#__codelineno-38-4)   --set galera.bootstrap.forceBootstrap=true \ [](#__codelineno-38-5)   --set galera.bootstrap.bootstrapFromNode=1 \ [](#__codelineno-38-6)   --set galera.bootstrap.forceSafeToBootstrap=true \ [](#__codelineno-38-7)   --set podManagementPolicy=Parallel \ [](#__codelineno-38-8)   --set image.tag=1.0.2`

Run the below command to monitor the progress of MariaDB Galera cluster nodes recovery.

`[](#__codelineno-39-1) kubectl get pods -n rda-fabric | grep mariadb`

Wait until all of the MariaDB Galera nodes are fully up and **Ready** state is in **1/1** state.

Depends on the size of the MariaDB database size and the performance of the system, the recovery may take from few minutes to 30 or more minutes.

Danger

If **MariaDB Galera cluster nodes are not able to recover** and keep crash-looping, please contact **CloudFabrix support** for further assistance.

Once MariaDB Galera cluster nodes are fully up and running, please run the below commands to verify if all of the nodes are in **Synced** state.

``[](#__codelineno-40-1) MARIADB_HOST=`cat /opt/rdaf/rdaf.cfg | grep -A3 mariadb | grep datadir | awk '{print $3}' | cut -f1 -d'/'` [](#__codelineno-40-2) [](#__codelineno-40-3) MARIADB_USER=`cat /opt/rdaf/rdaf.cfg | grep -A3 mariadb | grep user | awk '{print $3}' | base64 -d` [](#__codelineno-40-4) [](#__codelineno-40-5) MARIADB_PASSWORD=`cat /opt/rdaf/rdaf.cfg | grep -A3 mariadb | grep password | awk '{print $3}' | base64 -d` [](#__codelineno-40-6) [](#__codelineno-40-7) mysql -u$MARIADB_USER -p$MARIADB_PASSWORD -h $MARIADB_HOST -P3307 -e "show status like 'wsrep_local_state_comment';"``

Example Output

`[](#__codelineno-41-1) +---------------------------+--------+ [](#__codelineno-41-2) | Variable_name             | Value  | [](#__codelineno-41-3) +---------------------------+--------+ [](#__codelineno-41-4) | wsrep_local_state_comment | Synced | [](#__codelineno-41-5) +---------------------------+--------+`

Once the MariaDB Galera cluster nodes force bootstrapped, please run the below command to clear the force bootstrap setting so that cluster nodes can be restarted gracefully next time.

Note

*   Copy & paste the **MariaDB root user's and mariabackup user's passwords** that you extracted from the Kubernetes secret vault from the above steps.
    
*   Get the MariaDB service's tag version from the `rdafk8s infra status | grep mariadb` command output.
    

`[](#__codelineno-42-1) helm -n rda-fabric upgrade rda-mariadb -f /opt/rdaf/deployment-scripts/mariadb-values.yaml /opt/rdaf/deployment-scripts/helm/rda-mariadb/ \ [](#__codelineno-42-2)   --set rootUser.password=<root user's password> \ [](#__codelineno-42-3)   --set galera.mariabackup.password=<mariabackup user's password> \ [](#__codelineno-42-4)   --set podManagementPolicy=Parallel \ [](#__codelineno-42-5)   --set image.tag=<tag_version>`

Example-Output

`[](#__codelineno-43-1) helm -n rda-fabric upgrade rda-mariadb -f /opt/rdaf/deployment-scripts/mariadb-values.yaml /opt/rdaf/deployment-scripts/helm/rda-mariadb/ \ [](#__codelineno-43-2)   --set rootUser.password=YIKy7pm2 \ [](#__codelineno-43-3)   --set galera.mariabackup.password=YIKy7pm2 \ [](#__codelineno-43-4)   --set podManagementPolicy=Parallel \ [](#__codelineno-43-5)   --set image.tag=1.0.2`

Run the below command to monitor the progress of MariaDB Galera cluster nodes restart.

`[](#__codelineno-44-1) kubectl get pods -n rda-fabric | grep mariadb`

Wait until all of the MariaDB Galera nodes are fully up and **Ready** state is in **1/1** state.

Once MariaDB Galera cluster nodes are fully up and running, please run the below commands to verify if all of the nodes are in **Synced** state.

``[](#__codelineno-45-1) MARIADB_HOST=`cat /opt/rdaf/rdaf.cfg | grep -A3 mariadb | grep datadir | awk '{print $3}' | cut -f1 -d'/'` [](#__codelineno-45-2) [](#__codelineno-45-3) MARIADB_USER=`cat /opt/rdaf/rdaf.cfg | grep -A3 mariadb | grep user | awk '{print $3}' | base64 -d` [](#__codelineno-45-4) [](#__codelineno-45-5) MARIADB_PASSWORD=`cat /opt/rdaf/rdaf.cfg | grep -A3 mariadb | grep password | awk '{print $3}' | base64 -d` [](#__codelineno-45-6) [](#__codelineno-45-7) mysql -u$MARIADB_USER -p$MARIADB_PASSWORD -h $MARIADB_HOST -P3307 -e "show status like 'wsrep_local_state_comment';"``

Example Output

`[](#__codelineno-46-1) +---------------------------+--------+ [](#__codelineno-46-2) | Variable_name             | Value  | [](#__codelineno-46-3) +---------------------------+--------+ [](#__codelineno-46-4) | wsrep_local_state_comment | Synced | [](#__codelineno-46-5) +---------------------------+--------+`

Run the below commands to check the cluster size of the **mariadb** cluster. Please verify that the cluster size is **3**.

`[](#__codelineno-47-1) mysql -u$MARIADB_USER -p$MARIADB_PASSWORD -h $MARIADB_HOST -P3307 -e "SHOW GLOBAL STATUS LIKE 'wsrep_cluster_size'";`

Example Output

`[](#__codelineno-48-1) +--------------------+-------+ [](#__codelineno-48-2) | Variable_name      | Value | [](#__codelineno-48-3) +--------------------+-------+ [](#__codelineno-48-4) | wsrep_cluster_size | 3     | [](#__codelineno-48-5) +--------------------+-------+`

**Reset POD Management Policy to `OrderedReady`:**

Note

These steps are **optional**, but handy incase if the **POD Management policy** need to be changed from **Paralell** to **OrderedReady**

During the MariaDB Galera cluster nodes force recovery, the POD Management policy is set to `Parallel` from the initial setting of `OrderedReady`.

Below steps can be followed to change the POD Management policy back to `OrderedReady`

Run the below commands in sequence to bring down each MariaDB Galera cluster nodes.

Bring down node **rda-mariadb-mariadb-galera-2**

`[](#__codelineno-49-1) kubectl scale statefulset.apps/rda-mariadb-mariadb-galera -n rda-fabric --replicas=2`

Verify the node **rda-mariadb-mariadb-galera-2** is terminated and deleted.

`[](#__codelineno-50-1) kubectl get pods -n rda-fabric -o wide | grep mariadb`

Bring down node **rda-mariadb-mariadb-galera-1**

`[](#__codelineno-51-1) kubectl scale statefulset.apps/rda-mariadb-mariadb-galera -n rda-fabric --replicas=1`

Verify the node **rda-mariadb-mariadb-galera-1** is terminated and deleted.

`[](#__codelineno-52-1) kubectl get pods -n rda-fabric -o wide | grep mariadb`

Bring down node **rda-mariadb-mariadb-galera-0**

`[](#__codelineno-53-1) kubectl scale statefulset.apps/rda-mariadb-mariadb-galera -n rda-fabric --replicas=0`

Verify the node **rda-mariadb-mariadb-galera-0** is terminated and deleted.

`[](#__codelineno-54-1) kubectl get pods -n rda-fabric -o wide | grep mariadb`

Edit MariaDB service's `/opt/rdaf/deployment-scripts/mariadb-values.yaml` configuration file and add the parameter to set the POD Management policy to `OrderedReady`

`[](#__codelineno-55-1) vi /opt/rdaf/deployment-scripts/mariadb-values.yaml`

`[](#__codelineno-56-1) image: [](#__codelineno-56-2)   registry: 10.95.125.140:5000 [](#__codelineno-56-3)   repository: rda-platform-mariadb [](#__codelineno-56-4)   tag: 1.0.3 [](#__codelineno-56-5)   pullPolicy: IfNotPresent [](#__codelineno-56-6)   pullSecrets: [](#__codelineno-56-7)     - cfxregistry-cred [](#__codelineno-56-8) podLabels: [](#__codelineno-56-9)   app: rda-fabric-services [](#__codelineno-56-10)   app_category: rdaf-infra [](#__codelineno-56-11)   app_component: rda-mariadb [](#__codelineno-56-12) podManagementPolicy: OrderedReady [](#__codelineno-56-13) resources: [](#__codelineno-56-14)   requests: {} [](#__codelineno-56-15)   limits: [](#__codelineno-56-16)     memory: 8Gi [](#__codelineno-56-17) .... [](#__codelineno-56-18) ....`

Run the below command to delete the MariaDB stateful-set configuration.

`[](#__codelineno-57-1) helm delete rda-mariadb -n rda-fabric`

Re-deploy the MariaDB Galera cluster service using the below command.

Warning

Please make sure to use the same tag version using which initial MariaDB Galera cluster service was deployed. You can get the tag version running the below command.

`[](#__codelineno-58-1) rdafk8s infra status | grep mariadb`

`[](#__codelineno-59-1) rdafk8s infra upgrade --tag 1.0.2 --service mariadb`

Run the below command to monitor the progress of MariaDB Galera cluster nodes configuration upgrade status.

`[](#__codelineno-60-1) kubectl get pods -n rda-fabric | grep mariadb`

Wait until all of the MariaDB Galera nodes are fully up and **Ready** state is in **1/1** state.

Once MariaDB Galera cluster nodes are fully up and running, please run the below commands to verify if all of the nodes are in **Synced** state.

``[](#__codelineno-61-1) MARIADB_HOST=`cat /opt/rdaf/rdaf.cfg | grep -A3 mariadb | grep datadir | awk '{print $3}' | cut -f1 -d'/'` [](#__codelineno-61-2) [](#__codelineno-61-3) MARIADB_USER=`cat /opt/rdaf/rdaf.cfg | grep -A3 mariadb | grep user | awk '{print $3}' | base64 -d` [](#__codelineno-61-4) [](#__codelineno-61-5) MARIADB_PASSWORD=`cat /opt/rdaf/rdaf.cfg | grep -A3 mariadb | grep password | awk '{print $3}' | base64 -d` [](#__codelineno-61-6) [](#__codelineno-61-7) mysql -u$MARIADB_USER -p$MARIADB_PASSWORD -h $MARIADB_HOST -P3307 -e "show status like 'wsrep_local_state_comment';"``

Example Output

`[](#__codelineno-62-1) +---------------------------+--------+ [](#__codelineno-62-2) | Variable_name             | Value  | [](#__codelineno-62-3) +---------------------------+--------+ [](#__codelineno-62-4) | wsrep_local_state_comment | Synced | [](#__codelineno-62-5) +---------------------------+--------+`

Run the below commands to check the cluster size of the **mariadb** cluster. Please verify that the cluster size is **3**.

`[](#__codelineno-63-1) mysql -u$MARIADB_USER -p$MARIADB_PASSWORD -h $MARIADB_HOST -P3307 -e "SHOW GLOBAL STATUS LIKE 'wsrep_cluster_size'";`

Example Output

`[](#__codelineno-64-1) +--------------------+-------+ [](#__codelineno-64-2) | Variable_name      | Value | [](#__codelineno-64-3) +--------------------+-------+ [](#__codelineno-64-4) | wsrep_cluster_size | 3     | [](#__codelineno-64-5) +--------------------+-------+`

If the MariaDB Galera cluster nodes are crashed because of power failure on all servers or because of some other server hardware failure, the cluster needs to be brought up carefully in a particular order to avoid any data loss.

First, we need to identify which node is eligible to bootstrap the MariaDB Galera cluster. For that, below are the two available methods.

*   Identify the node which has highest seqno value.

Tip

A cluster node will only have positive highest seqno value when atleast one of the node was able to gracefully shutdown. This is the node that needs to be started first to bootstrap the MariaDB Galera cluster.

**OR**

*   Identify the node which has recorded the last committed transaction.

#### **3.1.1 Recover MariaDB Galera cluster using a Node which has the highest `seqno` value:**

Login into MariaDB cluster Node03 using SSH client to access the CLI. (username: **rdauser**)

Following shows the content of `grastate.dat` in Node03. In this example, this node has negative seqno and no group ID (uuid). This is the case when a node crashes during Data Definition Language (DDL) processing:

`[](#__codelineno-65-1) cat /var/mysql/grastate.dat`

Example Output

`[](#__codelineno-66-1) # GALERA saved state [](#__codelineno-66-2) version: 2.1 [](#__codelineno-66-3) uuid: 886dd8da-3d07-11e8-a109-8a3c80cebab4 [](#__codelineno-66-4) seqno: -1 [](#__codelineno-66-5) safe_to_bootstrap: 0`

Following is the content of `grastate.dat` on Node01 with the highest seqno value:

`[](#__codelineno-67-1) cat /var/mysql/grastate.dat`

Example Output

`[](#__codelineno-68-1) # GALERA saved state [](#__codelineno-68-2) version: 2.1 [](#__codelineno-68-3) uuid: 886dd8da-3d07-11e8-a109-8a3c80cebab4 [](#__codelineno-68-4) seqno: 31929 [](#__codelineno-68-5) safe_to_bootstrap: 1`

Note

If all of the 3 cluster nodes contain the value of -1 for `seqno` and 0 for `safe_to_bootstrap`, that is an indication that a full cluster crash has occurred. Go to the Next Section of this document ([**Recover MariaDB Galera cluster using a Node that has committed the last transaction**](#312-recover-mariadb-galera-cluster-using-a-node-that-has-committed-the-last-transaction)
)

The MariaDB node with the highest seqno value is an appropriate Node to bootstrap the MariaDB Galera cluster.

Follow the below steps to bootstrap and bring up the MariaDB cluster:

**Step-1:** Login into the MariaDB **bootstrap node** using an SSH client as a **rdauser** user. (**bootstrap node** is identified using one of the above-mentioned procedures)

**Step-2:** Stop the mariadb service.

Change the directory to `/opt/rdaf/deployment-scripts/<node_ip_address>` and execute the below command.

`[](#__codelineno-69-1) docker-compose -f infra.yaml --project-name infra rm -fsv mariadb`

**Step-3:** Change the directory to `/opt/rdaf/deployment-scripts/<node_ip_address>`. Edit `infra.yaml` docker-compose file and configure the environment variable as highlighted below to enable boot-strapping the mariadb cluster.

  `[](#__codelineno-70-1)   mariadb: [](#__codelineno-70-2)     image: 192.168.125.140:5000/rda-platform-mariadb:1.0.1 [](#__codelineno-70-3)     restart: 'no' [](#__codelineno-70-4)     network_mode: host [](#__codelineno-70-5)     mem_limit: 8G [](#__codelineno-70-6)     memswap_limit: 8G [](#__codelineno-70-7)     oom_kill_disable: false [](#__codelineno-70-8)     volumes: [](#__codelineno-70-9)     - /var/mysql:/bitnami/mariadb/data/ [](#__codelineno-70-10)     - /opt/rdaf/config/mariadb:/opt/bitnami/mariadb/conf/bitnami/ [](#__codelineno-70-11)     - /opt/rdaf/logs/mariadb:/opt/rdaf/log/ [](#__codelineno-70-12)     logging: [](#__codelineno-70-13)       driver: json-file [](#__codelineno-70-14)       options: [](#__codelineno-70-15)         max-size: 10m [](#__codelineno-70-16)         max-file: '5' [](#__codelineno-70-17)     environment: [](#__codelineno-70-18)     - MARIADB_GALERA_MARIABACKUP_USER=rdaf_backup [](#__codelineno-70-19)     ... [](#__codelineno-70-20)     ... [](#__codelineno-70-21)     ... [](#__codelineno-70-22)     - MARIADB_GALERA_CLUSTER_ADDRESS=gcomm://192.168.125.143,192.168.125.144,192.168.125.145 [](#__codelineno-70-23)     - MARIADB_GALERA_CLUSTER_BOOTSTRAP=yes`

**Step-4:** Edit `/var/mysql/grastate.dat` file and make sure `safe_to_bootstrap` value is set to `1` and save the file.

**Step-5:** Start the MariaDB container using the below command.

`[](#__codelineno-71-1) docker-compose -f infra.yaml --project-name infra up -d mariadb`

After starting the MariaDB container, watch the log messages @ the below log file

`/opt/rdaf/logs/mariadb/mariadb.log`

and look for the below log message which confirms the Node is completely up and in the synced state.

`WSREP: Server status change joined -> synced`

Additionally, run the below command to verify the MariaDB cluster **bootstrap node** is completely up in the synced state.

`[](#__codelineno-72-1) mysql -u <username> -p<password> -h <node-ip> -P 3306 -e "show status like 'wsrep_local_state_comment';"`

Example Output

`[](#__codelineno-73-1) +---------------------------+--------+ [](#__codelineno-73-2) | Variable_name             | Value  | [](#__codelineno-73-3) +---------------------------+--------+ [](#__codelineno-73-4) | wsrep_local_state_comment | Synced | [](#__codelineno-73-5) +---------------------------+--------+`

Once the MariaDB bootstrap cluster node is up, continue the below steps to bring up the rest of the 2 Nodes.

**Step-5:** Login into the MariaDB rest of the nodes (no specific order) using SSH client as **rdauser**.

**Step-6:** Change the directory to `/opt/rdaf/deployment-scripts/<node_ip_address>`. Edit `infra.yaml` docker-compose file and make sure the below highlighted parameter `MARIADB_GALERA_CLUSTER_BOOTSTRAP` doesn't exist, if yes, just **remove** it to disable boot-strapping the mariadb cluster.

  `[](#__codelineno-74-1)   mariadb: [](#__codelineno-74-2)     image: 192.168.125.140:5000/rda-platform-mariadb:1.0.1 [](#__codelineno-74-3)     restart: 'no' [](#__codelineno-74-4)     network_mode: host [](#__codelineno-74-5)     mem_limit: 8G [](#__codelineno-74-6)     memswap_limit: 8G [](#__codelineno-74-7)     oom_kill_disable: false [](#__codelineno-74-8)     volumes: [](#__codelineno-74-9)     - /var/mysql:/bitnami/mariadb/data/ [](#__codelineno-74-10)     - /opt/rdaf/config/mariadb:/opt/bitnami/mariadb/conf/bitnami/ [](#__codelineno-74-11)     - /opt/rdaf/logs/mariadb:/opt/rdaf/log/ [](#__codelineno-74-12)     logging: [](#__codelineno-74-13)       driver: json-file [](#__codelineno-74-14)       options: [](#__codelineno-74-15)         max-size: 10m [](#__codelineno-74-16)         max-file: '5' [](#__codelineno-74-17)     environment: [](#__codelineno-74-18)     - MARIADB_GALERA_MARIABACKUP_USER=rdaf_backup [](#__codelineno-74-19)     ... [](#__codelineno-74-20)     ... [](#__codelineno-74-21)     ... [](#__codelineno-74-22)     - MARIADB_GALERA_CLUSTER_ADDRESS=gcomm://192.168.125.143,192.168.125.144,192.168.125.145 [](#__codelineno-74-23)     - MARIADB_GALERA_CLUSTER_BOOTSTRAP=yes`

Note

The above parameter is applicable only on the MariaDB cluster's **bootstrap node** which initializes the Galera cluster.

**Step-7:** Start the MariaDB container using the below command.

`[](#__codelineno-75-1) docker-compose -f infra.yaml --project-name infra up -d mariadb`

After starting the MariaDB container, watch the log messages @ the below log file

`/opt/rdaf/logs/mariadb/mariadb.log`

and look for the below log message which confirms the Node is completely up and in the synced state.

`WSREP: Server status change joined -> synced`

Additionally, run the below command to verify the MariaDB cluster **bootstrap node** is completely up in the synced state.

`[](#__codelineno-76-1) mysql -u <username> -p<password> -h <node-ip> -P 3306 -e "show status like 'wsrep_local_state_comment';"`

Example Output

`[](#__codelineno-77-1) +---------------------------+--------+ [](#__codelineno-77-2) | Variable_name             | Value  | [](#__codelineno-77-3) +---------------------------+--------+ [](#__codelineno-77-4) | wsrep_local_state_comment | Synced | [](#__codelineno-77-5) +---------------------------+--------+`

Note

When second or third nodes are coming up after the crash and syncing up with the Cluster's bootstrap node, it may take few minutes or a little longer to be completely up and synced state.

**Step-8:** On the last MariaDB node, please follow the procedure listed in **Step-6** and **Step-7**

**Step-9:** Once the MariaDB cluster nodes are completely up and functional, login into Node01 and edit the MariaDB docker-compose file `infra.yaml` and make sure to add the highlighted parameter `MARIADB_GALERA_CLUSTER_BOOTSTRAP` as environment variable and save it. (Configuration file location: `/opt/rdaf/deployment-scripts/<node-ip-address>/infra.yaml`)

  `[](#__codelineno-78-1)   mariadb: [](#__codelineno-78-2)     image: 192.168.125.140:5000/rda-platform-mariadb:1.0.1 [](#__codelineno-78-3)     restart: 'no' [](#__codelineno-78-4)     network_mode: host [](#__codelineno-78-5)     mem_limit: 8G [](#__codelineno-78-6)     memswap_limit: 8G [](#__codelineno-78-7)     oom_kill_disable: false [](#__codelineno-78-8)     volumes: [](#__codelineno-78-9)     - /var/mysql:/bitnami/mariadb/data/ [](#__codelineno-78-10)     - /opt/rdaf/config/mariadb:/opt/bitnami/mariadb/conf/bitnami/ [](#__codelineno-78-11)     - /opt/rdaf/logs/mariadb:/opt/rdaf/log/ [](#__codelineno-78-12)     logging: [](#__codelineno-78-13)       driver: json-file [](#__codelineno-78-14)       options: [](#__codelineno-78-15)         max-size: 10m [](#__codelineno-78-16)         max-file: '5' [](#__codelineno-78-17)     environment: [](#__codelineno-78-18)     - MARIADB_GALERA_MARIABACKUP_USER=rdaf_backup [](#__codelineno-78-19)     ... [](#__codelineno-78-20)     ... [](#__codelineno-78-21)     ... [](#__codelineno-78-22)     - MARIADB_GALERA_CLUSTER_ADDRESS=gcomm://192.168.125.143,192.168.125.144,192.168.125.145 [](#__codelineno-78-23)     - MARIADB_GALERA_CLUSTER_BOOTSTRAP=yes`

On **Node2** & **Node03**, edit the MariaDB docker-compose file `infra.yaml` and make sure the above environment variable is not set. This is to make sure `rdaf` CLI starts the Node01 as cluster **bootstrap node** first when it is executed manually to bring up the MariaDB cluster nodes.

Note

MariaDB Galera cluster node order (i.e Node01, Node02 & Node03) is determined based on the order of comma-separated IP address list provided during the `rdaf setup` command which configures initial configuration of the RDAF platform.

#### **3.1.2 Recover MariaDB Galera cluster using a Node that has committed the last transaction:**

**Step-1:** Login into MariaDB cluster Node01 using SSH client to access the CLI. (username: **rdauser**)

**Step-2:** Run the below command to find the Mariadb container ID

`[](#__codelineno-79-1) docker ps -a | grep mariadb`

Note

Please make sure the MariaDB container is in a stopped state or run the below command to stop the MariaDB container.

`[](#__codelineno-80-1) docker stop -t 120 <mariadb-container-id>`

**Step-3:** Take a backup of the MariaDB configuration file.

`[](#__codelineno-81-1) cp /opt/rdaf/config/mariadb/my_custom.cnf /opt/rdaf/config/mariadb/my_custom.cnf.bak`

Change the directory to `/opt/rdaf/deployment-scripts/<node_ip_address>`. Edit `infra.yaml` docker-compose file and configure the environment variable as highlighted below to **disable** boot-strapping the mariadb cluster.

  `[](#__codelineno-82-1)   mariadb: [](#__codelineno-82-2)     image: 192.168.125.140:5000/rda-platform-mariadb:1.0.1 [](#__codelineno-82-3)     restart: 'no' [](#__codelineno-82-4)     network_mode: host [](#__codelineno-82-5)     mem_limit: 8G [](#__codelineno-82-6)     memswap_limit: 8G [](#__codelineno-82-7)     oom_kill_disable: false [](#__codelineno-82-8)     volumes: [](#__codelineno-82-9)     - /var/mysql:/bitnami/mariadb/data/ [](#__codelineno-82-10)     - /opt/rdaf/config/mariadb:/opt/bitnami/mariadb/conf/bitnami/ [](#__codelineno-82-11)     - /opt/rdaf/logs/mariadb:/opt/rdaf/log/ [](#__codelineno-82-12)     logging: [](#__codelineno-82-13)       driver: json-file [](#__codelineno-82-14)       options: [](#__codelineno-82-15)         max-size: 10m [](#__codelineno-82-16)         max-file: '5' [](#__codelineno-82-17)     environment: [](#__codelineno-82-18)     - MARIADB_GALERA_MARIABACKUP_USER=rdaf_backup [](#__codelineno-82-19)     ... [](#__codelineno-82-20)     ... [](#__codelineno-82-21)     ... [](#__codelineno-82-22)     - MARIADB_GALERA_CLUSTER_ADDRESS=gcomm://192.168.125.143,192.168.125.144,192.168.125.145 [](#__codelineno-82-23)     - MARIADB_GALERA_CLUSTER_BOOTSTRAP=no`

Note

The above environment variable `MARIADB_GALERA_CLUSTER_BOOTSTRAP` is applicable only on the MariaDB cluster's **bootstrap node** which initializes the Galera cluster.

If `MARIADB_GALERA_CLUSTER_BOOTSTRAP` is modified in `infra.yml` file, please run the below commands to stop the MariaDB service.

`[](#__codelineno-83-1) docker-compose -f infra.yaml --project-name infra rm -fsv mariadb`

**Step-4:** Edit the MariaDB configuration file and add the below specified option. (Configuration file location: `/opt/rdaf/config/mariadb/my_custom.cnf`)

`[](#__codelineno-84-1) wsrep-recover=1`

**Step-5:** Start the MariaDB service and wait for 2 to 3 minutes to allow it to be completely up.

`[](#__codelineno-85-1) docker-compose -f infra.yaml --project-name infra up -d mariadb`

**Step-6:** Tail mariadb service log and look for similar to the below message. (`/opt/rdaf/logs/mariadb/mariadb.log`)

`[](#__codelineno-86-1) 2021-06-07 9:50:36 0 [Note] WSREP: Recovered position: afa02221-c422-11eb-8a24-96c95f63c95b:397159`

Note down the above **highlighted value** and follow the same steps from **Step-4** through **Step-6** for Node02 & Node03

The MariaDB node with the latest data will have the **highest value** and that is an appropriate Node to **bootstrap** the MariaDB Galera cluster.

**Follow the below steps to bring up the MariaDB Galera cluster:**

**Step-1:** Login into the MariaDB that was identified as a **bootstrap node** (node that has the highest recovered position value) using an SSH client as a **rdauser** user.

**Step-2:** Change the directory to `/opt/rdaf/deployment-scripts/<node_ip_address>`. Edit `infra.yaml` docker-compose file and configure the environment variable as highlighted below to **enable** boot-strapping the mariadb cluster.

  `[](#__codelineno-87-1)   mariadb: [](#__codelineno-87-2)     image: 192.168.125.140:5000/rda-platform-mariadb:1.0.1 [](#__codelineno-87-3)     restart: 'no' [](#__codelineno-87-4)     network_mode: host [](#__codelineno-87-5)     mem_limit: 8G [](#__codelineno-87-6)     memswap_limit: 8G [](#__codelineno-87-7)     oom_kill_disable: false [](#__codelineno-87-8)     volumes: [](#__codelineno-87-9)     - /var/mysql:/bitnami/mariadb/data/ [](#__codelineno-87-10)     - /opt/rdaf/config/mariadb:/opt/bitnami/mariadb/conf/bitnami/ [](#__codelineno-87-11)     - /opt/rdaf/logs/mariadb:/opt/rdaf/log/ [](#__codelineno-87-12)     logging: [](#__codelineno-87-13)       driver: json-file [](#__codelineno-87-14)       options: [](#__codelineno-87-15)         max-size: 10m [](#__codelineno-87-16)         max-file: '5' [](#__codelineno-87-17)     environment: [](#__codelineno-87-18)     - MARIADB_GALERA_MARIABACKUP_USER=rdaf_backup [](#__codelineno-87-19)     ... [](#__codelineno-87-20)     ... [](#__codelineno-87-21)     ... [](#__codelineno-87-22)     - MARIADB_GALERA_CLUSTER_ADDRESS=gcomm://192.168.125.143,192.168.125.144,192.168.125.145 [](#__codelineno-87-23)     - MARIADB_GALERA_CLUSTER_BOOTSTRAP=yes`

Edit `my_custom.cnf` configuration file and make sure the below parameter is removed and save it. (Configuration file location: `/opt/rdaf/config/mariadb/my_custom.cnf`)

`[](#__codelineno-88-1) wsrep-recover=1`

**Step-3:** Edit `/var/mysql/grastate.dat` file and set `safe_to_bootstrap` value as `1` and save the file.

**Step-4:** Stop the MariaDB container using the below command. (`infra.yaml` file is under `/opt/rdaf/deployment-scripts/<node_ip_address>`)

`[](#__codelineno-89-1) docker-compose -f infra.yaml --project-name infra rm -fsv mariadb`

**Step-5:** Start the MariaDB service using the below command.

`[](#__codelineno-90-1) docker-compose -f infra.yaml --project-name infra up -d mariadb`

After starting the MariaDB service, watch the log messages @ the below log file

`[](#__codelineno-91-1) /opt/rdaf/logs/mariadb/mariadb.log`

and look for the below log message which confirms the Node is completely up and in the synced state.

`[](#__codelineno-92-1) WSREP: Server status change joined -> synced`

Additionally, run the below command to verify the MariaDB cluster **bootstrap node** is completely up in the synced state.

`[](#__codelineno-93-1) mysql -u <username> -p<password> -h <node-ip> -P 3306 -e "show status like 'wsrep_local_state_comment';"`

Example Output

`[](#__codelineno-94-1) +---------------------------+--------+ [](#__codelineno-94-2) | Variable_name             | Value  | [](#__codelineno-94-3) +---------------------------+--------+ [](#__codelineno-94-4) | wsrep_local_state_comment | Synced | [](#__codelineno-94-5) +---------------------------+--------+`

Once the MariaDB bootstrap cluster node is up, continue the below steps to bring up the rest of the 2 Nodes.

**Step-5:** Login into the MariaDB rest of the nodes (no specific order) using SSH client as **rdauser**.

**Step-6:** Change the directory to `/opt/rdaf/deployment-scripts/<node_ip_address>`. Edit `infra.yaml` docker-compose file and make sure the below highlighted parameter `MARIADB_GALERA_CLUSTER_BOOTSTRAP` doesn't exist, if yes, just **remove** it to disable boot-strapping the mariadb cluster.

  `[](#__codelineno-95-1)   mariadb: [](#__codelineno-95-2)     image: 192.168.125.140:5000/rda-platform-mariadb:1.0.1 [](#__codelineno-95-3)     restart: 'no' [](#__codelineno-95-4)     network_mode: host [](#__codelineno-95-5)     mem_limit: 8G [](#__codelineno-95-6)     memswap_limit: 8G [](#__codelineno-95-7)     oom_kill_disable: false [](#__codelineno-95-8)     volumes: [](#__codelineno-95-9)     - /var/mysql:/bitnami/mariadb/data/ [](#__codelineno-95-10)     - /opt/rdaf/config/mariadb:/opt/bitnami/mariadb/conf/bitnami/ [](#__codelineno-95-11)     - /opt/rdaf/logs/mariadb:/opt/rdaf/log/ [](#__codelineno-95-12)     logging: [](#__codelineno-95-13)       driver: json-file [](#__codelineno-95-14)       options: [](#__codelineno-95-15)         max-size: 10m [](#__codelineno-95-16)         max-file: '5' [](#__codelineno-95-17)     environment: [](#__codelineno-95-18)     - MARIADB_GALERA_MARIABACKUP_USER=rdaf_backup [](#__codelineno-95-19)     ... [](#__codelineno-95-20)     ... [](#__codelineno-95-21)     ... [](#__codelineno-95-22)     - MARIADB_GALERA_CLUSTER_ADDRESS=gcomm://192.168.125.143,192.168.125.144,192.168.125.145 [](#__codelineno-95-23)     - MARIADB_GALERA_CLUSTER_BOOTSTRAP=yes`

Note

The above environment variable `MARIADB_GALERA_CLUSTER_BOOTSTRAP` is applicable only on the MariaDB cluster's **bootstrap node** which initializes the Galera cluster.

**Step-7:** Edit `my_custom.cnf` configuration file and make sure the below parameter doesn't exist, if yes, just remove it. (Configuration file location: `/opt/rdaf/config/mariadb/my_custom.cnf`)

`[](#__codelineno-96-1) wsrep-recover=1`

**Step-8:** Start the MariaDB container using the below command. Change the directory to `/opt/rdaf/deployment-scripts/<node_ip_address>`

`[](#__codelineno-97-1) docker-compose -f infra.yaml --project-name infra up -d mariadb`

After starting the MariaDB container, watch the log messages @ the below log file

`[](#__codelineno-98-1) /opt/rdaf/logs/mariadb/mariadb.log`

and look for the below log message which confirms the Node is completely up and in the synced state.

`[](#__codelineno-99-1) WSREP: Server status change joined -> synced`

Additionally, run the below command to verify the MariaDB cluster **bootstrap node** is completely up in the synced state.

`[](#__codelineno-100-1) mysql -u <username> -p<password> -h <node-ip> -P 3306 -e "show status like 'wsrep_local_state_comment';"`

Example Output

`[](#__codelineno-101-1) +---------------------------+--------+ [](#__codelineno-101-2) | Variable_name             | Value  | [](#__codelineno-101-3) +---------------------------+--------+ [](#__codelineno-101-4) | wsrep_local_state_comment | Synced | [](#__codelineno-101-5) +---------------------------+--------+`

Note

When second or third nodes are coming up after the crash and syncing up with the Cluster's **bootstrap node**, it may take few minutes or a little longer to be completely up and in synced state.

**Step-9:** On the last MariaDB node, please follow the procedure listed in **Step-6**

**Step-10:** Once the MariaDB cluster nodes are completely up and functional, login into **Node01** and edit the MariaDB docker-compose file `infra.yaml` and make sure to add the highlighted parameter `MARIADB_GALERA_CLUSTER_BOOTSTRAP` as environment variable and save it. (Configuration file location: `/opt/rdaf/deployment-scripts/<node-ip-address>/infra.yaml`)

  `[](#__codelineno-102-1)   mariadb: [](#__codelineno-102-2)     image: 192.168.125.140:5000/rda-platform-mariadb:1.0.1 [](#__codelineno-102-3)     restart: 'no' [](#__codelineno-102-4)     network_mode: host [](#__codelineno-102-5)     mem_limit: 8G [](#__codelineno-102-6)     memswap_limit: 8G [](#__codelineno-102-7)     oom_kill_disable: false [](#__codelineno-102-8)     volumes: [](#__codelineno-102-9)     - /var/mysql:/bitnami/mariadb/data/ [](#__codelineno-102-10)     - /opt/rdaf/config/mariadb:/opt/bitnami/mariadb/conf/bitnami/ [](#__codelineno-102-11)     - /opt/rdaf/logs/mariadb:/opt/rdaf/log/ [](#__codelineno-102-12)     logging: [](#__codelineno-102-13)       driver: json-file [](#__codelineno-102-14)       options: [](#__codelineno-102-15)         max-size: 10m [](#__codelineno-102-16)         max-file: '5' [](#__codelineno-102-17)     environment: [](#__codelineno-102-18)     - MARIADB_GALERA_MARIABACKUP_USER=rdaf_backup [](#__codelineno-102-19)     ... [](#__codelineno-102-20)     ... [](#__codelineno-102-21)     ... [](#__codelineno-102-22)     - MARIADB_GALERA_CLUSTER_ADDRESS=gcomm://192.168.125.143,192.168.125.144,192.168.125.145 [](#__codelineno-102-23)     - MARIADB_GALERA_CLUSTER_BOOTSTRAP=yes`

On **Node2** & **Node03**, edit the MariaDB docker-compose file `infra.yaml` and make sure the above environment variable is not set or removed. This is to make sure `rdaf` CLI starts the Node01 as cluster **bootstrap node** first when it is executed manually to bring up the MariaDB cluster nodes.

Note

MariaDB Galera cluster node order (i.e Node01, Node02 & Node03) is determined based on the order of comma-separated IP address list provided during the `rdaf setup` command which configures initial configuration of the RDAF platform.

**4\. Install & Configure RDAF Log Streaming**
----------------------------------------------

RDAF is built on cloud native and distributed microservices architecture. When it is deployed, it installs below services.

*   Infrastructure Services
*   Core Platform Services
*   Application Services
*   Worker Services

All of these services generate log events which reflects the operational health of the RDAF platform in realtime.

As RDAF platform has many microservices, it becomes difficult to monitor and analyze all of the microservices logs for any operational analysis or troubleshooting when needed.

To address the above mentioned challenge, RDAF provides below log streaming services which helps to stream the logs of all RDAF platform's microservices and ingest them into RDAF pstreams in realtime.

*   **Logstash:** It is a service which processes incoming log stream from **Fluentbit**, normalizes different log formats of RDAF service logs into a common data model and ingest them into RDAF's Opensearch index store. Additionally, it supports forwarding the processed logs to external log management tools such as **Splunk, Elasticsearch, IBM Qradar** etc..
*   **Fluentbit:** It is a very light weight log shipping agent which monitors the RDAF service logs and forward them to **Logstash** service in realtime.

Once the RDAF platform service's logs are ingested into pstreams, they can be visualized and analyzed using RDAF's composable dashboards or use `rdac pstream query` or `rdac pstream tail` CLI options to access the logs in realtime.

The following section provides you the instructions on how to install and configure both **Logstash** and **Fluentbit** log streaming services.

### **4.1 Logstash Installation & Configuration**

Important

**Pre-requisites:**

*   Install **Logstash** on where **RDAF CLI** was installed and the **rdaf setup** was run.
*   Access to **/opt/rdaf/rdaf.cfg** configuration file
*   Access to **/opt/rdaf/config/network\_config/config.json** configuration file
*   Access to **/opt/rdaf/cert/ca/ca.crt** certificate file
*   **rdac CLI** was installed, please refer [RDAC CLI Installation](https://bot-docs.cloudfabrix.io/beginners_guide/rdac/)
    

Tip

To use `rdac.py` as a regular command, follow the below steps

`[](#__codelineno-103-1) sudo cp rdac.py /usr/bin/rdac [](#__codelineno-103-2) sudo chmod +x /usr/bin/rdac [](#__codelineno-103-3) rdac --help`

**Step-1:**

Run the below command to create and save the docker login session into CloudFabrix's secure docker repository.

`[](#__codelineno-104-1) docker login -u='readonly' -p='readonly' cfxregistry.cloudfabrix.io`

Run the below sequence of commands to create the required directory structure and set the permissions.

``[](#__codelineno-105-1) sudo mkdir -p /opt/logstash/config [](#__codelineno-105-2) sudo mkdir -p /opt/logstash/config/cert [](#__codelineno-105-3) sudo mkdir -p /opt/logstash/pipeline [](#__codelineno-105-4) sudo mkdir -p /opt/logstash/templates [](#__codelineno-105-5) sudo mkdir -p /opt/logstash/data [](#__codelineno-105-6) sudo mkdir -p /opt/logstash/logs [](#__codelineno-105-7) sudo chown -R `id -u`:`id -g` /opt/logstash``

**Step-2:**

Copy the CA certificate to Logstash configuration folder

`[](#__codelineno-106-1) cp /opt/rdaf/cert/ca/ca.crt /opt/logstash/config/cert/ca.crt`

**Step-3:**

Enable the required firewall ports for Logstash to receive the log events from Fluentbit

`[](#__codelineno-107-1) sudo ufw allow 5045/tcp [](#__codelineno-107-2) sudo ufw allow 5046/tcp`

**Step-4:**

Create the required RDAF pstreams to ingest the RDAF service logs.

``[](#__codelineno-108-1) tenant_id=`cat /opt/rdaf/config/network_config/config.json | grep tenant_id | awk '{print $2}' | cut -f2 -d"\""` [](#__codelineno-108-2) [](#__codelineno-108-3) rdac pstream add --name rdaf_services_logs --index $tenant_id-stream-rdaf_services_logs --retention_days 15 --timestamp @timestamp``

**Step-5:**

Run the below command to view and verify the above RDAF pstreams are created.

`[](#__codelineno-109-1) rdac pstream list`

**Step-6:**

Create the docker-compose file as shown below, install and bring the service up.

`[](#__codelineno-110-1) cd /opt/logstash [](#__codelineno-110-2) [](#__codelineno-110-3) cat > logstash-docker-compose.yml <<'EOF' [](#__codelineno-110-4) version: '3' [](#__codelineno-110-5) [](#__codelineno-110-6) services: [](#__codelineno-110-7)   logstash: [](#__codelineno-110-8)     image: "cfxregistry.cloudfabrix.io/rda-platform-logstash:1.0.2" [](#__codelineno-110-9)     container_name: rda_logstash [](#__codelineno-110-10)     hostname: rda_logstash [](#__codelineno-110-11)     network_mode: host [](#__codelineno-110-12)     restart: always [](#__codelineno-110-13)     oom_kill_disable: false [](#__codelineno-110-14)     user: root [](#__codelineno-110-15)     mem_limit: 6G [](#__codelineno-110-16)     memswap_limit: 6G [](#__codelineno-110-17)     logging: [](#__codelineno-110-18)       driver: "json-file" [](#__codelineno-110-19)       options: [](#__codelineno-110-20)         max-size: "25m" [](#__codelineno-110-21)         max-file: "5" [](#__codelineno-110-22)     volumes: [](#__codelineno-110-23)       - /opt/logstash/config:/usr/share/logstash/config [](#__codelineno-110-24)       - /opt/logstash/pipeline:/usr/share/logstash/pipeline [](#__codelineno-110-25)       - /opt/logstash/templates:/usr/share/logstash/templates [](#__codelineno-110-26)       - /opt/logstash/data:/usr/share/logstash/data [](#__codelineno-110-27)       - /opt/logstash/logs:/usr/share/logstash/logs [](#__codelineno-110-28)     environment: [](#__codelineno-110-29)       LS_JAVA_OPTS: -Xmx4g -Xms4g [](#__codelineno-110-30)     command: logstash [](#__codelineno-110-31) [](#__codelineno-110-32) EOF`

`[](#__codelineno-111-1) docker-compose -f logstash-docker-compose.yml up -d [](#__codelineno-111-2) sleep 30`

**Step-7:**

Configure the Logstash service and restart it.

``[](#__codelineno-112-1) tenant_id=`cat /opt/rdaf/config/network_config/config.json | grep tenant_id | awk '{print $2}' | cut -f2 -d"\""` [](#__codelineno-112-2) opensearch_host=`cat /opt/rdaf/rdaf.cfg | grep -A3 "\[opensearch\]" | grep datadir | awk '{print $3}' | cut -f1 -d"/"` [](#__codelineno-112-3) opensearch_user=`cat /opt/rdaf/rdaf.cfg | grep -A3 "\[opensearch\]" | grep user | awk '{print $3}' | base64 -d` [](#__codelineno-112-4) opensearch_password=`cat /opt/rdaf/rdaf.cfg | grep -A3 "\[opensearch\]" | grep password | awk '{print $3}' | base64 -d` [](#__codelineno-112-5) [](#__codelineno-112-6) sed -i "s/TENANT_ID/$tenant_id/g" /opt/logstash/pipeline/rda_services.conf [](#__codelineno-112-7) sed -i "s/localhost/$opensearch_host/g" /opt/logstash/pipeline/rda_services.conf [](#__codelineno-112-8) sed -i "s/OS_USERNAME/$opensearch_user/g" /opt/logstash/pipeline/rda_services.conf [](#__codelineno-112-9) sed -i "s/OS_PASSWORD/$opensearch_password/g" /opt/logstash/pipeline/rda_services.conf [](#__codelineno-112-10) [](#__codelineno-112-11) sed -i "s/TENANT_ID/$tenant_id/g" /opt/logstash/pipeline/rda_minio.conf [](#__codelineno-112-12) sed -i "s/localhost/$opensearch_host/g" /opt/logstash/pipeline/rda_minio.conf [](#__codelineno-112-13) sed -i "s/OS_USERNAME/$opensearch_user/g" /opt/logstash/pipeline/rda_minio.conf [](#__codelineno-112-14) sed -i "s/OS_PASSWORD/$opensearch_password/g" /opt/logstash/pipeline/rda_minio.conf [](#__codelineno-112-15) [](#__codelineno-112-16) logstash_container_id=`docker ps -a | grep rda-platform-logstash | awk '{print $1}'` [](#__codelineno-112-17) [](#__codelineno-112-18) docker restart $logstash_container_id``

### **4.2 Fluentbit Installation & Configuration**

Important

**Pre-requisites:**

*   **Logstash** service was installed, please refer above section for installing the **Logstash** service.
*   Firewall ports **5045 & 5046** are open on Logstash host.

Install & configure **Fluentbit** log shipping agent on all of the RDAF infrastructure, platform, application and worker service VMs.

**Step-1:**

Run the below command to create and save the docker login session into CloudFabrix's secure docker repository.

`[](#__codelineno-113-1) docker login -u='readonly' -p='readonly' cfxregistry.cloudfabrix.io`

Run the below sequence of commands to create the required directory structure and set the permissions.

``[](#__codelineno-114-1) sudo mkdir -p /opt/fluent-bit/config [](#__codelineno-114-2) sudo mkdir -p /opt/fluent-bit/logs [](#__codelineno-114-3) sudo mkdir -p /opt/fluent-bit/data [](#__codelineno-114-4) sudo chown -R `id -u`:`id -g` /opt/fluent-bit``

**Step-2:**

Create the docker-compose file as shown below, install and bring the service up.

`[](#__codelineno-115-1) cd /opt/fluent-bit [](#__codelineno-115-2) [](#__codelineno-115-3) cat > fluentbit-docker-compose.yml <<'EOF' [](#__codelineno-115-4) version: "3" [](#__codelineno-115-5) services: [](#__codelineno-115-6)   fluentbit: [](#__codelineno-115-7)     container_name: rda-platform-fluentbit [](#__codelineno-115-8)     image: cfxregistry.cloudfabrix.io/rda-platform-fluent-bit:1.0.2 [](#__codelineno-115-9)     restart: always [](#__codelineno-115-10)     network_mode: host [](#__codelineno-115-11)     oom_kill_disable: false [](#__codelineno-115-12)     mem_limit: 4G [](#__codelineno-115-13)     memswap_limit: 4G [](#__codelineno-115-14)     logging: [](#__codelineno-115-15)       driver: "json-file" [](#__codelineno-115-16)       options: [](#__codelineno-115-17)         max-size: "25m" [](#__codelineno-115-18)         max-file: "5" [](#__codelineno-115-19)     volumes: [](#__codelineno-115-20)       - /opt/fluent-bit/config:/fluent-bit/config [](#__codelineno-115-21)       - /opt/fluent-bit/logs:/fluent-bit/logs [](#__codelineno-115-22)       - /opt/fluent-bit/data:/fluent-bit/data [](#__codelineno-115-23)       - /opt/rdaf/logs:/applogs [](#__codelineno-115-24)       - /var/log:/syslog:ro [](#__codelineno-115-25)     entrypoint: ["/fluent-bit/bin/docker-entry-point.sh"] [](#__codelineno-115-26) [](#__codelineno-115-27) EOF`

`[](#__codelineno-116-1) docker-compose -f fluentbit-docker-compose.yml up -d [](#__codelineno-116-2) sleep 5`

**Step-3:**

Configure the Fluentbit log shipping agent and restart it.

Set the **Logstash IP Address** for below variable.

`[](#__codelineno-117-1) export logstash_ip=<LOGSTASH_IP_ADDRESS>`

Warning

Please make sure to set the correct **Logstash host's IP address** to above variable before running the below commands.

``[](#__codelineno-118-1) sed -i "s/localhost/$logstash_ip/g" /opt/fluent-bit/config/fluent-bit-output.conf [](#__codelineno-118-2) [](#__codelineno-118-3) fluentbit_container_id=`docker ps -a | grep rda-platform-fluent-bit | awk '{print $1}'` [](#__codelineno-118-4) [](#__codelineno-118-5) docker restart $fluentbit_container_id``

### **4.3 Enabling Minio service logs**

Minio object storage service does not write the server and audit log messages to disk, instead, it provides an option to configure a webhook endpoint to push the server and audit log events.

Follow the below steps to enable and stream the Minio logs to **Logstash** service.

Important

*   Run the below commands where `rdaf setup` was run
*   Access to `/opt/rdaf/rdaf.cfg`
*   `mc` CLI (Minio Client)

Run the below commands to configure Minio service to push the server and audit logs to **Logstash** service.

*   Configure Minio service access settings using `mc` CLI (Minio Client)

``[](#__codelineno-119-1) minio_host=`cat /opt/rdaf/rdaf.cfg | grep -A3 "\[minio\]" | grep datadir | awk '{print $3}' | cut -f1 -d"/"` [](#__codelineno-119-2) minio_user=`cat /opt/rdaf/rdaf.cfg | grep -A3 "\[minio\]" | grep user | awk '{print $3}' | base64 -d` [](#__codelineno-119-3) minio_password=`cat /opt/rdaf/rdaf.cfg | grep -A4 "\[minio\]" | grep password | awk '{print $3}' | base64 -d` [](#__codelineno-119-4) [](#__codelineno-119-5) mc alias set myminio http://$minio_host:9000 $minio_user $minio_password``

*   Set the **Logstash IP Address** for below variable.

`[](#__codelineno-120-1) export logstash_ip=<LOGSTASH_IP_ADDRESS>`

Warning

Please make sure to set the correct **Logstash host's IP address** to above variable before running the below commands.

*   Configure the Minio service to forward both server and audit logs to **Logstash** service.

`[](#__codelineno-121-1) mc admin config set myminio/ logger_webhook:"rdaf_log_streaming" endpoint="http://$logstash_ip:5046" [](#__codelineno-121-2) mc admin config set myminio/ audit_webhook:"rdaf_log_streaming" endpoint="http://$logstash_ip:5046"`

### **4.4 Search and Query RDAF service logs from pstreams**

RDAF service logs are ingested into the below pstream which can be queried or tailed using **rdac CLI**

**PStream Name:**

*   **rdaf\_services\_logs:** It indexes the RDAF service logs from below
    *   OS syslog / messages
    *   MariaDB
    *   NATs
    *   Kafka
    *   Zookeeper
    *   Opensearch
    *   Minio
    *   HAProxy Supervisor
    *   RDA core platform services
    *   OIA & AIA application services
    *   RDA Portal backend service
    *   RDA Portal frontend service
    *   RDA HAProxy Access Logs

Below are the **extracted / enriched / normalized attributes** which can be used to query the logs from the above pstreams.

| **Attribute Name** | **Attribute Value** |
| --- | --- |
| `service_name` | `rda_access_manager`  <br>`rda_alert_ingester`  <br> `rda_alert_processor`  <br>`rda_all_alerts_caas`  <br>`rda_api_server`  <br>`rda_app_builder`  <br>`rda_app_controller`  <br>`rda_asset_dependency`  <br>`rda_collaboration`  <br>`rda_collector`  <br>`rda_config_service`  <br>`rda_current_alerts_caas`  <br>`rda_event_consumer`  <br>`rda_file_browser`  <br>`rda_haproxy`  <br>`rda_identity`  <br>`rda_ingestion_tracker`  <br> `rda_irm_service`  <br>`rda_kafka`  <br>`rda_mariadb`  <br>`rda_minio`  <br>`rda_ml_config`  <br>`rda_nats`  <br>`rda_notification_service`  <br> `rda_opensearch`  <br>`rda_os_syslog`  <br>`rda_portal_backend`  <br>`rda_portal_frontend`  <br>`rda_registry`  <br>`rda_reports_registry`  <br> `rda_resource_manager`  <br>`rda_schedule_admin`  <br>`rda_scheduler`  <br>`rda_smtp_server`  <br>`rda_user_preferences`  <br>`rda_webhook_server`  <br>`rda_worker`  <br>`rda_zookeeper` |
| `service_category` | `rda_app_svcs`  <br>`rda_pfm_svcs`  <br>`rda_infra_svcs` |
| `service_host` | `Hostname` of RDAF VM. Ex: `rda-platform-vm01` |
| `log_severity` | `INFO`  <br>`WARNING`  <br>`ERROR`  <br>`DEBUG`  <br>`TRACE` |
| `log_message` | Extracted log message. Ex: `pod age greater than 60 pod_id: 1091635f, pod_type:cfxdimensions-app-access-manager, inactive_pods: {'d0a17813', '1091635f', '766cbf82'}` |
| `process_name` | RDAF platform or app service's internal process name captured within the log message. Ex: `rda_messaging.nats_client` |
| `process_function` | RDAF platform or app service's internal process function name captured within the log message. Ex: `health_check` |
| `thread_id` | RDAF platform or app service's internal thread ID captured within the log message. Ex: `Thread-9` |
| `log` | Full raw log message. Ex: `2022-09-22 01:47:59,611 [PID=8:TID=Thread-9:rda_messaging.nats_client:health_check:435] INFO - Sef health check successfull` |
| `host` | RDAF VM host's IP Address. Ex: `192.168.10.11` |

**Tail logs from pstream:**

Example

Run the below command to tail pstream **rdaf\_services\_logs** for RDAF platform **registry** service.

`[](#__codelineno-122-1) rdac pstream tail --name rdaf_services_logs --ts @timestamp --query "service_name = 'rda_registry'" --out_cols 'log'`

`--query` supports CFXQL query. However it doesn't support `get` columns option.

`--out_cols` use this option to get specific attributes from the pstream as shown in the above example.

`--json` use this option to get the log output in JSON format. However, it doesn't support limiting the selective attributes listed under `--out_cols` option.

Run the below command to tail only **ERROR** messages across all RDAF platform and application services.

`[](#__codelineno-123-1) rdac pstream tail --name rdaf_services_logs --ts @timestamp --query "log_severity = 'ERROR'" --out_cols 'service_name,log'`

**Query logs from pstream:**

Example

Run the below command to query the pstream **rdaf\_services\_logs** for **ERROR** messages from all services within last 24 hours.

``[](#__codelineno-124-1) rdac pstream query --name rdaf_services_logs --ts @timestamp --query '"\`@timestamp\`" is after -1d and log_severity = 'ERROR' get service_name,log' --json``

### **4.5 Add RDAF Log Analytics Dashboard to the portal**

Login into RDAF portal as a tenant admin user.

Go to **Configuration** menu and click on **Artifacts**

Under **Dashboards** section, click on **View Details**

Click on **Add YAML** button to add a new RDAF Log Analytics dashboard.

Copy and Paste the below content to it and click on **Save**

``[](#__codelineno-125-1) { [](#__codelineno-125-2)     "name": "rdaf-platform-log-analytics", [](#__codelineno-125-3)     "label": "RDAF Platform Logs", [](#__codelineno-125-4)     "description": "RDAF Platform service's log analysis dashboard", [](#__codelineno-125-5)     "version": "22.9.22.1", [](#__codelineno-125-6)     "enabled": true, [](#__codelineno-125-7)     "dashboard_style": "tabbed", [](#__codelineno-125-8)     "status_poller": { [](#__codelineno-125-9)         "stream": "rdaf_services_logs", [](#__codelineno-125-10)         "frequency": 15, [](#__codelineno-125-11)         "columns": [ [](#__codelineno-125-12)             "@timestamp" [](#__codelineno-125-13)         ], [](#__codelineno-125-14)         "sorting": [ [](#__codelineno-125-15)             { [](#__codelineno-125-16)                 "@timestamp": "desc" [](#__codelineno-125-17)             } [](#__codelineno-125-18)         ], [](#__codelineno-125-19)         "query": "`@timestamp` is after '${timestamp}'", [](#__codelineno-125-20)         "defaults": { [](#__codelineno-125-21)             "@timestamp": "$UTCNOW" [](#__codelineno-125-22)         }, [](#__codelineno-125-23)         "action": "refresh" [](#__codelineno-125-24)     }, [](#__codelineno-125-25)     "dashboard_filters": { [](#__codelineno-125-26)         "time_filter": true, [](#__codelineno-125-27)         "columns_filter": [ [](#__codelineno-125-28)             { [](#__codelineno-125-29)                 "id": "@timestamp", [](#__codelineno-125-30)                 "label": "Timestamp", [](#__codelineno-125-31)                 "type": "DATETIME" [](#__codelineno-125-32)             }, [](#__codelineno-125-33)             { [](#__codelineno-125-34)                 "id": "service_name", [](#__codelineno-125-35)                 "label": "Service Name", [](#__codelineno-125-36)                 "type": "TEXT" [](#__codelineno-125-37)             }, [](#__codelineno-125-38)             { [](#__codelineno-125-39)                 "id": "service_category", [](#__codelineno-125-40)                 "label": "Service Category", [](#__codelineno-125-41)                 "type": "TEXT" [](#__codelineno-125-42)             }, [](#__codelineno-125-43)             { [](#__codelineno-125-44)                 "id": "log_severity", [](#__codelineno-125-45)                 "label": "Log Severity", [](#__codelineno-125-46)                 "type": "TEXT" [](#__codelineno-125-47)             }, [](#__codelineno-125-48)             { [](#__codelineno-125-49)                 "id": "log", [](#__codelineno-125-50)                 "label": "Log Message", [](#__codelineno-125-51)                 "type": "TEXT" [](#__codelineno-125-52)             }, [](#__codelineno-125-53)             { [](#__codelineno-125-54)                 "id": "process_name", [](#__codelineno-125-55)                 "label": "Process Name", [](#__codelineno-125-56)                 "type": "TEXT" [](#__codelineno-125-57)             }, [](#__codelineno-125-58)             { [](#__codelineno-125-59)                 "id": "process_function", [](#__codelineno-125-60)                 "label": "Process Function", [](#__codelineno-125-61)                 "type": "TEXT" [](#__codelineno-125-62)             }, [](#__codelineno-125-63)             { [](#__codelineno-125-64)                 "id": "thread_id", [](#__codelineno-125-65)                 "label": "Thread ID", [](#__codelineno-125-66)                 "type": "TEXT" [](#__codelineno-125-67)             }, [](#__codelineno-125-68)             { [](#__codelineno-125-69)                 "id": "service_host", [](#__codelineno-125-70)                 "label": "Hostname", [](#__codelineno-125-71)                 "type": "TEXT" [](#__codelineno-125-72)             }, [](#__codelineno-125-73)             { [](#__codelineno-125-74)                 "id": "host", [](#__codelineno-125-75)                 "label": "IP Address", [](#__codelineno-125-76)                 "type": "TEXT" [](#__codelineno-125-77)             } [](#__codelineno-125-78)         ], [](#__codelineno-125-79)         "group_filters": [ [](#__codelineno-125-80)             { [](#__codelineno-125-81)                 "stream": "rdaf_services_logs", [](#__codelineno-125-82)                 "title": "Log Severity", [](#__codelineno-125-83)                 "group_by": [ [](#__codelineno-125-84)                     "log_severity" [](#__codelineno-125-85)                 ], [](#__codelineno-125-86)                 "ts_column": "@timestamp", [](#__codelineno-125-87)                 "agg": "value_count", [](#__codelineno-125-88)                 "column": "_id", [](#__codelineno-125-89)                 "type": "int" [](#__codelineno-125-90)             }, [](#__codelineno-125-91)             { [](#__codelineno-125-92)                 "stream": "rdaf_services_logs", [](#__codelineno-125-93)                 "title": "Service Name", [](#__codelineno-125-94)                 "group_by": [ [](#__codelineno-125-95)                     "service_name" [](#__codelineno-125-96)                 ], [](#__codelineno-125-97)                 "ts_column": "@timestamp", [](#__codelineno-125-98)                 "agg": "value_count", [](#__codelineno-125-99)                 "column": "_id", [](#__codelineno-125-100)                 "type": "int" [](#__codelineno-125-101)             }, [](#__codelineno-125-102)             { [](#__codelineno-125-103)                 "stream": "rdaf_services_logs", [](#__codelineno-125-104)                 "title": "Service Category", [](#__codelineno-125-105)                 "group_by": [ [](#__codelineno-125-106)                     "service_category" [](#__codelineno-125-107)                 ], [](#__codelineno-125-108)                 "ts_column": "@timestamp", [](#__codelineno-125-109)                 "agg": "value_count", [](#__codelineno-125-110)                 "column": "_id", [](#__codelineno-125-111)                 "type": "int" [](#__codelineno-125-112)             }, [](#__codelineno-125-113)             { [](#__codelineno-125-114)                 "stream": "rdaf_services_logs", [](#__codelineno-125-115)                 "title": "RDA Hostname", [](#__codelineno-125-116)                 "group_by": [ [](#__codelineno-125-117)                     "service_host" [](#__codelineno-125-118)                 ], [](#__codelineno-125-119)                 "ts_column": "@timestamp", [](#__codelineno-125-120)                 "agg": "value_count", [](#__codelineno-125-121)                 "column": "_id", [](#__codelineno-125-122)                 "type": "int" [](#__codelineno-125-123)             }, [](#__codelineno-125-124)             { [](#__codelineno-125-125)                 "stream": "rdaf_services_logs", [](#__codelineno-125-126)                 "title": "RDA Host IPAddress", [](#__codelineno-125-127)                 "group_by": [ [](#__codelineno-125-128)                     "service_host" [](#__codelineno-125-129)                 ], [](#__codelineno-125-130)                 "ts_column": "@timestamp", [](#__codelineno-125-131)                 "agg": "value_count", [](#__codelineno-125-132)                 "column": "_id", [](#__codelineno-125-133)                 "type": "int" [](#__codelineno-125-134)             } [](#__codelineno-125-135)         ] [](#__codelineno-125-136)     }, [](#__codelineno-125-137)     "dashboard_sections": [ [](#__codelineno-125-138)         { [](#__codelineno-125-139)             "title": "Overall Summary", [](#__codelineno-125-140)             "show_filter": true, [](#__codelineno-125-141)             "widgets": [ [](#__codelineno-125-142)                 { [](#__codelineno-125-143)                     "title": "Log Severity Trend", [](#__codelineno-125-144)                     "widget_type": "timeseries", [](#__codelineno-125-145)                     "stream": "rdaf_services_logs", [](#__codelineno-125-146)                     "ts_column": "@timestamp", [](#__codelineno-125-147)                     "max_width": 12, [](#__codelineno-125-148)                     "height": 3, [](#__codelineno-125-149)                     "min_width": 12, [](#__codelineno-125-150)                     "chartProperties": { [](#__codelineno-125-151)                         "yAxisLabel": "Count", [](#__codelineno-125-152)                         "xAxisLabel": null, [](#__codelineno-125-153)                         "legendLocation": "bottom" [](#__codelineno-125-154)                     }, [](#__codelineno-125-155)                     "interval": "15Min", [](#__codelineno-125-156)                     "group_by": [ [](#__codelineno-125-157)                         "log_severity" [](#__codelineno-125-158)                     ], [](#__codelineno-125-159)                     "series_spec": [ [](#__codelineno-125-160)                         { [](#__codelineno-125-161)                             "column": "log_severity", [](#__codelineno-125-162)                             "agg": "value_count", [](#__codelineno-125-163)                             "type": "int" [](#__codelineno-125-164)                         } [](#__codelineno-125-165)                     ], [](#__codelineno-125-166)                     "widget_id": "06413884" [](#__codelineno-125-167)                 }, [](#__codelineno-125-168)                 { [](#__codelineno-125-169)                     "widget_type": "label", [](#__codelineno-125-170)                     "label": "<h3><font style=\"color: #ffffff;\"><table border=0> <tr><td width=\"50%\" align=\"left\" rowspan=1><b>TOTAL Logs:</b></td><td width=\"50%\" align=\"right\" rowspan=1>{{ \"{:,}\".format(TOTAL | int) }}</td></tr> <tr><td height=\"20px\" colspan=1></td></tr> <tr><td width=\"50%\" align=\"left\" rowspan=1><b>INFO Logs:</b></td><td width=\"50%\" align=\"right\" rowspan=1>{{ \"{:,}\".format(INFO | int) }}</td></tr> <tr><td height=\"20px\" colspan=1></td></tr> <tr><td width=\"50%\" align=\"left\" rowspan=1><b>WARN Logs:</b></td><td width=\"50%\" align=\"right\" rowspan=1>{{ \"{:,}\".format(WARNING | int) }}</td></tr> <tr><td height=\"20px\" colspan=1></td></tr> <tr><td width=\"50%\" align=\"left\" rowspan=1><b>ERROR Logs:</b></td><td width=\"50%\" align=\"right\" rowspan=1>{{ \"{:,}\".format(ERROR | int) }}</td></tr> <tr><td height=\"20px\" colspan=1></td></tr> </table></font></h3>", [](#__codelineno-125-171)                     "min_width": 3, [](#__codelineno-125-172)                     "max_width": 4, [](#__codelineno-125-173)                     "height": 4, [](#__codelineno-125-174)                     "style": { [](#__codelineno-125-175)                         "backgroundColor": "#1976d2", [](#__codelineno-125-176)                         "color": "#ffffff" [](#__codelineno-125-177)                     }, [](#__codelineno-125-178)                     "segments": [ [](#__codelineno-125-179)                         { [](#__codelineno-125-180)                             "variable": "TOTAL", [](#__codelineno-125-181)                             "agg": "value_count", [](#__codelineno-125-182)                             "type": "int", [](#__codelineno-125-183)                             "stream": "rdaf_services_logs", [](#__codelineno-125-184)                             "ts_column": "@timestamp", [](#__codelineno-125-185)                             "extra_filter": "", [](#__codelineno-125-186)                             "column": "service_category.keyword" [](#__codelineno-125-187)                         }, [](#__codelineno-125-188)                         { [](#__codelineno-125-189)                             "variable": "INFO", [](#__codelineno-125-190)                             "agg": "value_count", [](#__codelineno-125-191)                             "type": "int", [](#__codelineno-125-192)                             "stream": "rdaf_services_logs", [](#__codelineno-125-193)                             "ts_column": "@timestamp", [](#__codelineno-125-194)                             "extra_filter": "log_severity is 'INFO'", [](#__codelineno-125-195)                             "column": "log_severity.keyword" [](#__codelineno-125-196)                         }, [](#__codelineno-125-197)                         { [](#__codelineno-125-198)                             "variable": "WARNING", [](#__codelineno-125-199)                             "agg": "value_count", [](#__codelineno-125-200)                             "type": "int", [](#__codelineno-125-201)                             "stream": "rdaf_services_logs", [](#__codelineno-125-202)                             "ts_column": "@timestamp", [](#__codelineno-125-203)                             "extra_filter": "log_severity is 'WARNING'", [](#__codelineno-125-204)                             "column": "log_severity.keyword" [](#__codelineno-125-205)                         }, [](#__codelineno-125-206)                         { [](#__codelineno-125-207)                             "variable": "ERROR", [](#__codelineno-125-208)                             "agg": "value_count", [](#__codelineno-125-209)                             "type": "int", [](#__codelineno-125-210)                             "stream": "rdaf_services_logs", [](#__codelineno-125-211)                             "ts_column": "@timestamp", [](#__codelineno-125-212)                             "extra_filter": "log_severity is 'ERROR'", [](#__codelineno-125-213)                             "column": "log_severity.keyword" [](#__codelineno-125-214)                         }, [](#__codelineno-125-215)                         { [](#__codelineno-125-216)                             "variable": "DEBUG", [](#__codelineno-125-217)                             "agg": "value_count", [](#__codelineno-125-218)                             "type": "int", [](#__codelineno-125-219)                             "stream": "rdaf_services_logs", [](#__codelineno-125-220)                             "ts_column": "@timestamp", [](#__codelineno-125-221)                             "extra_filter": "log_severity = 'DEBUG'", [](#__codelineno-125-222)                             "column": "log_severity.keyword" [](#__codelineno-125-223)                         } [](#__codelineno-125-224)                     ], [](#__codelineno-125-225)                     "widget_id": "5ae002f1" [](#__codelineno-125-226)                 }, [](#__codelineno-125-227)                 { [](#__codelineno-125-228)                     "widget_type": "pie_chart", [](#__codelineno-125-229)                     "title": "Logs by Severity", [](#__codelineno-125-230)                     "stream": "rdaf_services_logs", [](#__codelineno-125-231)                     "ts_column": "@timestamp", [](#__codelineno-125-232)                     "column": "_id", [](#__codelineno-125-233)                     "agg": "value_count", [](#__codelineno-125-234)                     "group_by": [ [](#__codelineno-125-235)                         "log_severity" [](#__codelineno-125-236)                     ], [](#__codelineno-125-237)                     "type": "str", [](#__codelineno-125-238)                     "style": { [](#__codelineno-125-239)                         "color-map": { [](#__codelineno-125-240)                             "ERROR": [ [](#__codelineno-125-241)                                 "#ef5350", [](#__codelineno-125-242)                                 "#ffffff" [](#__codelineno-125-243)                             ], [](#__codelineno-125-244)                             "WARNING": [ [](#__codelineno-125-245)                                 "#FFA726", [](#__codelineno-125-246)                                 "#ffffff" [](#__codelineno-125-247)                             ], [](#__codelineno-125-248)                             "INFO": [ [](#__codelineno-125-249)                                 "#388e3c", [](#__codelineno-125-250)                                 "#ffffff" [](#__codelineno-125-251)                             ], [](#__codelineno-125-252)                             "DEBUG": [ [](#__codelineno-125-253)                                 "#000000", [](#__codelineno-125-254)                                 "#ffffff" [](#__codelineno-125-255)                             ], [](#__codelineno-125-256)                             "UNKNOWN": [ [](#__codelineno-125-257)                                 "#bcaaa4", [](#__codelineno-125-258)                                 "#ffffff" [](#__codelineno-125-259)                             ] [](#__codelineno-125-260)                         } [](#__codelineno-125-261)                     }, [](#__codelineno-125-262)                     "min_width": 4, [](#__codelineno-125-263)                     "height": 4, [](#__codelineno-125-264)                     "max_width": 4, [](#__codelineno-125-265)                     "widget_id": "b2ffa8e9" [](#__codelineno-125-266)                 }, [](#__codelineno-125-267)                 { [](#__codelineno-125-268)                     "widget_type": "pie_chart", [](#__codelineno-125-269)                     "title": "Logs by RDA Host", [](#__codelineno-125-270)                     "stream": "rdaf_services_logs", [](#__codelineno-125-271)                     "ts_column": "@timestamp", [](#__codelineno-125-272)                     "column": "_id", [](#__codelineno-125-273)                     "agg": "value_count", [](#__codelineno-125-274)                     "group_by": [ [](#__codelineno-125-275)                         "service_host" [](#__codelineno-125-276)                     ], [](#__codelineno-125-277)                     "type": "str", [](#__codelineno-125-278)                     "min_width": 4, [](#__codelineno-125-279)                     "height": 2, [](#__codelineno-125-280)                     "max_width": 4, [](#__codelineno-125-281)                     "widget_id": "79355cb8" [](#__codelineno-125-282)                 }, [](#__codelineno-125-283)                 { [](#__codelineno-125-284)                     "widget_type": "pie_chart", [](#__codelineno-125-285)                     "title": "Logs by RDA Host IP", [](#__codelineno-125-286)                     "stream": "rdaf_services_logs", [](#__codelineno-125-287)                     "ts_column": "@timestamp", [](#__codelineno-125-288)                     "column": "_id", [](#__codelineno-125-289)                     "agg": "value_count", [](#__codelineno-125-290)                     "group_by": [ [](#__codelineno-125-291)                         "host" [](#__codelineno-125-292)                     ], [](#__codelineno-125-293)                     "type": "str", [](#__codelineno-125-294)                     "min_width": 4, [](#__codelineno-125-295)                     "height": 4, [](#__codelineno-125-296)                     "max_width": 4, [](#__codelineno-125-297)                     "widget_id": "a4f2d8bd" [](#__codelineno-125-298)                 }, [](#__codelineno-125-299)                 { [](#__codelineno-125-300)                     "widget_type": "pie_chart", [](#__codelineno-125-301)                     "title": "Logs by Service Category", [](#__codelineno-125-302)                     "stream": "rdaf_services_logs", [](#__codelineno-125-303)                     "ts_column": "@timestamp", [](#__codelineno-125-304)                     "column": "_id", [](#__codelineno-125-305)                     "agg": "value_count", [](#__codelineno-125-306)                     "group_by": [ [](#__codelineno-125-307)                         "service_category" [](#__codelineno-125-308)                     ], [](#__codelineno-125-309)                     "type": "str", [](#__codelineno-125-310)                     "min_width": 4, [](#__codelineno-125-311)                     "height": 4, [](#__codelineno-125-312)                     "max_width": 4, [](#__codelineno-125-313)                     "widget_id": "89ac5ce9" [](#__codelineno-125-314)                 }, [](#__codelineno-125-315)                 { [](#__codelineno-125-316)                     "widget_type": "pie_chart", [](#__codelineno-125-317)                     "title": "Logs by Service Name", [](#__codelineno-125-318)                     "stream": "rdaf_services_logs", [](#__codelineno-125-319)                     "ts_column": "@timestamp", [](#__codelineno-125-320)                     "column": "_id", [](#__codelineno-125-321)                     "agg": "value_count", [](#__codelineno-125-322)                     "group_by": [ [](#__codelineno-125-323)                         "service_name" [](#__codelineno-125-324)                     ], [](#__codelineno-125-325)                     "type": "str", [](#__codelineno-125-326)                     "min_width": 4, [](#__codelineno-125-327)                     "height": 4, [](#__codelineno-125-328)                     "max_width": 4, [](#__codelineno-125-329)                     "widget_id": "4b267fce" [](#__codelineno-125-330)                 } [](#__codelineno-125-331)             ] [](#__codelineno-125-332)         }, [](#__codelineno-125-333)         { [](#__codelineno-125-334)             "title": "App Services", [](#__codelineno-125-335)             "show_filter": true, [](#__codelineno-125-336)             "widgets": [ [](#__codelineno-125-337)                 { [](#__codelineno-125-338)                     "widget_type": "tabular", [](#__codelineno-125-339)                     "title": "Log Messages", [](#__codelineno-125-340)                     "stream": "rdaf_services_logs", [](#__codelineno-125-341)                     "extra_filter": "service_category in ['rda_app_svcs', 'rda_pfm_svcs']", [](#__codelineno-125-342)                     "ts_column": "@timestamp", [](#__codelineno-125-343)                     "sorting": [ [](#__codelineno-125-344)                         { [](#__codelineno-125-345)                             "@timestamp": "desc" [](#__codelineno-125-346)                         } [](#__codelineno-125-347)                     ], [](#__codelineno-125-348)                     "columns": { [](#__codelineno-125-349)                         "@timestamp": { [](#__codelineno-125-350)                             "title": "Timestamp", [](#__codelineno-125-351)                             "type": "DATETIME" [](#__codelineno-125-352)                         }, [](#__codelineno-125-353)                         "state_color2": { [](#__codelineno-125-354)                             "type": "COLOR-MAP", [](#__codelineno-125-355)                             "source-column": "log_severity", [](#__codelineno-125-356)                             "color-map": { [](#__codelineno-125-357)                                 "INFO": "#388e3c", [](#__codelineno-125-358)                                 "ERROR": "#ef5350", [](#__codelineno-125-359)                                 "WARNING": "#ffa726", [](#__codelineno-125-360)                                 "DEBUG": "#000000" [](#__codelineno-125-361)                             } [](#__codelineno-125-362)                         }, [](#__codelineno-125-363)                         "log_severity": { [](#__codelineno-125-364)                             "title": "Severity", [](#__codelineno-125-365)                             "htmlTemplateForRow": "<span class='badge' style='background-color: {{ row.state_color2 }}' > {{ row.log_severity }} </span>" [](#__codelineno-125-366)                         }, [](#__codelineno-125-367)                         "service_name": "Service Name", [](#__codelineno-125-368)                         "process_name": "Process Name", [](#__codelineno-125-369)                         "process_function": "Process Function", [](#__codelineno-125-370)                         "log": "Message" [](#__codelineno-125-371)                     }, [](#__codelineno-125-372)                     "widget_id": "6895c8f0" [](#__codelineno-125-373)                 } [](#__codelineno-125-374)             ] [](#__codelineno-125-375)         }, [](#__codelineno-125-376)         { [](#__codelineno-125-377)             "title": "Infra Services", [](#__codelineno-125-378)             "show_filter": true, [](#__codelineno-125-379)             "widgets": [ [](#__codelineno-125-380)                 { [](#__codelineno-125-381)                     "widget_type": "tabular", [](#__codelineno-125-382)                     "title": "Log Messages", [](#__codelineno-125-383)                     "stream": "rdaf_services_logs", [](#__codelineno-125-384)                     "extra_filter": "service_category in ['rda_infra_svcs']", [](#__codelineno-125-385)                     "ts_column": "@timestamp", [](#__codelineno-125-386)                     "sorting": [ [](#__codelineno-125-387)                         { [](#__codelineno-125-388)                             "@timestamp": "desc" [](#__codelineno-125-389)                         } [](#__codelineno-125-390)                     ], [](#__codelineno-125-391)                     "columns": { [](#__codelineno-125-392)                         "@timestamp": { [](#__codelineno-125-393)                             "title": "Timestamp", [](#__codelineno-125-394)                             "type": "DATETIME" [](#__codelineno-125-395)                         }, [](#__codelineno-125-396)                         "log_severity": { [](#__codelineno-125-397)                             "title": "Severity", [](#__codelineno-125-398)                             "htmlTemplateForRow": "<span class='badge' style='background-color: {{ row.state_color2 }}' > {{ row.log_severity }} </span>" [](#__codelineno-125-399)                         }, [](#__codelineno-125-400)                         "state_color2": { [](#__codelineno-125-401)                             "type": "COLOR-MAP", [](#__codelineno-125-402)                             "source-column": "log_severity", [](#__codelineno-125-403)                             "color-map": { [](#__codelineno-125-404)                                 "INFO": "#388e3c", [](#__codelineno-125-405)                                 "ERROR": "#ef5350", [](#__codelineno-125-406)                                 "WARNING": "#ffa726", [](#__codelineno-125-407)                                 "DEBUG": "#000000", [](#__codelineno-125-408)                                 "UNKNOWN": "#bcaaa4" [](#__codelineno-125-409)                             } [](#__codelineno-125-410)                         }, [](#__codelineno-125-411)                         "service_name": "Service Name", [](#__codelineno-125-412)                         "process_name": "Process Name", [](#__codelineno-125-413)                         "log": "Message", [](#__codelineno-125-414)                         "minio_object": "Minio Object" [](#__codelineno-125-415)                     }, [](#__codelineno-125-416)                     "widget_id": "98f10587" [](#__codelineno-125-417)                 } [](#__codelineno-125-418)             ] [](#__codelineno-125-419)         } [](#__codelineno-125-420)     ], [](#__codelineno-125-421)     "saved_time": "2022-09-30T06:34:19.205249" [](#__codelineno-125-422) }``

Click on the added dashboard **rdaf-platform-log-analytics** to visualize the logs.

![Chart](https://bot-docs.cloudfabrix.io/images/rdaf_logs/rdaf_logs_dashboard.png)

### **4.6 Un-installing Logstash and Fluentbit**

Follow the below steps to un-install both Logstash and Fluentbit services.

**Un-installing Logstash service:**

*   Login into RDAF host as **rdauser** (using SSH client) on which **Logstash** service was installed
    
*   Stop the **Logstash** service and remove the container
    

`[](#__codelineno-126-1) docker rm -f $(docker ps -a | grep rda-platform-logstash | awk '{print $1}')`

*   Remove the **Logstash** docker image

`[](#__codelineno-127-1) docker rmi $(docker images | grep rda-platform-logstash | awk '{print $3}')`

*   Remove the **Logstash** service configuration

Danger

Below steps will remove all of the existing **Logstash** configuration data.

`[](#__codelineno-128-1) rm -rf /opt/logstash/*`

**Un-installing Fluentbit service:**

*   Login into RDAF host as **rdauser** (using SSH client) on which **Fluentbit** service was installed
    
*   Stop the **Fluentbit** service and remove the container
    

`[](#__codelineno-129-1) docker rm -f $(docker ps -a | grep rda-platform-fluent-bit | awk '{print $1}')`

*   Remove the **Fluentbit** docker image

`[](#__codelineno-130-1) docker rmi $(docker images | grep rda-platform-fluent-bit | awk '{print $3}')`

*   Remove the **Fluentbit** service configuration

Danger

Below steps will remove all of the existing **Fluentbit** configuration data.

`[](#__codelineno-131-1) rm -rf /opt/fluent-bit/*`

**5\. RDAF\-Cli Backup and Restore**
------------------------------------

RDAF Infra/Platform holds data, operational configuration via following components. These components need to be backed up periodically so that in case of any issues or problems, the RDAF Infra/Platform as part of the RDA Fabric can be recreated by restoring a stable snapshot from the backup.

*   Maria DB
    
*   Minio
    
*   Opensearch
    
*   All configs
    
*   Certs
    
*   Deployment-yamls
    

To avoid user mistakes while taking backups, RDAF framework provides backup support via the RDAF CLI on the platform instance. Below are the steps

### **5.1 Prerequisites**

*   Destination directory for backup should be a shared directory among cli, and all infra vms.
    
*   For Non k8s setups, Opensearch data backup directory should be a shared directory among cli, and all infra vms. This directory is referenced in the `/opt/rdaf/deployment-scripts/values.yaml file`. By default, the value mentioned for Opensearch data backup in the above file is `/opt/opensearch-backup`. This backup location can be changed to the required shared directory, in case if infra services are already deployed before this change.
    
*   For Non k8s setups users can use 'rdaf infra upgrade --tag \--service opensearch' to upgrade the directory-path. By default, users can input the required shared directory path in `values.yaml` and then, deploy infra components install.
    
*   For k8s setups, Opensearch backup PV uses the path `/opt/backup/opensearch`. This path should be mounted in all Opensearch vms.
    

**Where are the backup files stored?**

Backup files are saved in **nfs mounted volume** that is shared between the cli vm and all the vms having infra containers.

Note

This nfs mounted volume should have rdauser user permissions.

### **5.2 Backup Command Details**

Kubernetes SetupsNon-Kubernetes Setups

`[](#__codelineno-132-1) rdafk8s backup [--debug] --dest-dir <nfs mounted volume to store backups>  [--service <any infra service> or the word ‘config’]`

`[](#__codelineno-133-1) rdaf backup [--debug] --dest-dir <nfs mounted volume to store backups>  [--service <any infra service> or the word ‘config’]`

*   `--dest-dir` should be nfs mounted volume to store backup.
    
*   `--service` is optional. If not used, it takes backup of all operational config files, certs, mariadb, minio, opensearch data. This option can contain any infra service. For mariadb/minio/opensearch, it collects the databases/buckets/indices data along with their configs. Users can give all the infra component names or ‘config’ keyword under --service option
    
*   `--create-tar` option creates tar file of the backed-up content in the destination directory (along with regular backed-up content inside destination directory as shown below).
    

Example

`[](#__codelineno-134-1) [rdauser@svc1-133-94 ~]$ ls /cfx-backup/2022-11-13-1668409114.741395 [](#__codelineno-134-2) cert  config  data  deployment-scripts  rdaf-backup-2022-11-13-1668409114.741395.tar.gz  rdaf-backup.cfg  rdaf.cfg [](#__codelineno-134-3) [rdauser@svc1-133-94 ~]$`

Note

RDAF backup CLI will not take backup of service logs

### **5.3 Backed Up Data Structure**

Inside the selected backup directory, another folder is created with date, for example:- `2021-07-17-1626586567.934014` for each backup triggered. Following captures sample folder structure of this directory:

`[rdauser@svc1-133-94 2022-11-08-1667898481.39201]$ ls`

output

`cert config data deployment-scripts rdaf-backup.cfg rdaf.cfg`

*   For full backup or for backing up mariadb/minio/nats, the mariadb/minio/nats data gets stored under the ‘data’ folder. For other components, data folder will be an empty folder.
    
*   Config section has the backup from `/opt/rdaf/config directory`, from all the vms of the setup.
    
*   Cert has certs from `/opt/rdaf/cert dir`
    
*   Deployment-scripts has backup from `/opt/rdaf/deployment-scripts directory`, from all the vms of the setup.
    
*   `rdaf-backup.cfg` Contains the cli version,components, opensearch snapshot-id, useful during restore.
    
*   For Opensearch data in non k8s setups, the backup will be stored in the directory that was mentioned in the `/opt/rdaf/deployment-scripts/values.yaml` file for Opensearch. This should be a shared directory among cli, and all Opensearch vms.
    
*   For k8s setups, data will be stored in `/opt/backup/opensearch` (This path should be mounted across all opensearch vms).
    

### **5.4 Periodic Collection of Backup**

To collect backups in regular intervals, we need to add/place the backup command in crontab. Sample line that needs to be placed in crontab is captured below:-

Kubernetes SetupsNon-Kubernetes Setups

`[](#__codelineno-135-1) 58 20 * * * /home/rdauser/.local/bin/rdafk8s backup --debug --dest-dir DestDir > Required-log-file`

`[](#__codelineno-136-1) 58 20 * * * /home/rdauser/.local/bin/rdaf backup --debug --dest-dir DestDir > Required-log-file`

Dest-Dir is the nfs mounted volume dedicated for storing backups.

Required-log-file is the log file along with the path, where users want the backup log to be written to.

### **5.5 Rdaf restore**

RDAF cli supports restoring data for the below components from the backups collected by the rdaf backup command.

*   Mariadb
    
*   Minio
    
*   Opensearch
    
*   Operational configuration (and other necessary files)
    
*   Any other infra component (All required configuration files will be copied here. Except mariadb, minio, opensearch, nats, there is separate data section for other infra components)
    

CLI to restore **Mysql**, **Minio**, **Opensearch**, Operational configuration is as given below.

Kubernetes SetupsNon-Kubernetes Setups

`[](#__codelineno-137-1) rdafk8s restore [--service {any infra component/’config’ keyword}] --from-dir [](#__codelineno-137-2) “nfs-mounted-volume/required-backupfile-involume” [--no-prompt]`

`[](#__codelineno-138-1) rdaf restore [--service {any infra component/’config’ keyword}] --from-dir   [](#__codelineno-138-2) “nfs-mounted-volume/required-backupfile-involume” [--no-prompt]`

Tip

We can use `--from-tar` instead of `--from-dir`, if we have used `--create-tar` while taking backup. To restore use the `tar.gz` file

Note

We don't restore any service logs

### **5.6 Full Restore**

`--service` option is optional, if not used, it will restore all the Operational configs, mariadb data, minio buckets, Opensearch indices, nats data.

Kubernetes SetupsNon-Kubernetes Setups

`[](#__codelineno-139-1) rdafk8s restore --from-dir “nfs-mounted-volume/required-backupfile-involume” [--no-prompt]`

`[](#__codelineno-140-1) rdaf restore --from-dir “nfs-mounted-volume/required-backupfile-involume” [--no-prompt]`

### **5.7 CloudFabrix Certified Restore Procedures**

Kubernetes SetupsNon-Kubernetes Setups

RDAF Restore – Platform/Service VMs are in-tact, All Services are also healthy. The purpose is just to roll back to an earlier snapshot

or

Upgrade is done to the app/platform, and if the upgrade fails, and if we want to revert to the previous snapshot taken before starting upgrade.

**Below are the steps to achieve the above.**

*   Take a full backup.

`[](#__codelineno-141-1) rdafk8s backup --debug --dest-dir <nfs mounted backup volume>`

Note

This is to make sure we have a latest snapshot

*   Verify RDAF OIA/AIA (AIOps) application services status by running the Below Command

`[](#__codelineno-142-1) rdafk8s app status`

Example

`[](#__codelineno-143-1) +-------------------------------+--------------+-------------------+--------------+---------+ [](#__codelineno-143-2) | Name                          | Host         | Status            | Container Id | Tag     | [](#__codelineno-143-3) +-------------------------------+--------------+-------------------+--------------+---------+ [](#__codelineno-143-4) | rda-alert-ingester            | 111.92.12.42 | Up 2 Weeks ago    | 447c7dab089d | 7.3.2   | [](#__codelineno-143-5) |                               |              |                   |              |         | [](#__codelineno-143-6) | rda-alert-ingester            | 111.92.12.42 | Up 2 Weeks ago    | 750a0d229eb8 | 7.3.2   | [](#__codelineno-143-7) |                               |              |                   |              |         | [](#__codelineno-143-8) | rda-alert-processor           | 111.92.12.42 | Up 15 Minutes ago | 6bf8bad1cf25 | 7.3     | [](#__codelineno-143-9) |                               |              |                   |              |         | [](#__codelineno-143-10) | rda-alert-processor           | 111.92.12.42 | Up 1 Minutes ago  | c953c4c94fd8 | 7.3     | [](#__codelineno-143-11) |                               |              |                   |              |         | [](#__codelineno-143-12) | rda-alert-processor-companion | 111.92.12.42 | Up 2 Weeks ago    | ccc85377da0d | 7.3     | [](#__codelineno-143-13) |                               |              |                   |              |         | [](#__codelineno-143-14) | rda-alert-processor-companion | 111.92.12.42 | Up 1 Days ago     | bd1b23a15fb2 | 7.3     | [](#__codelineno-143-15) |                               |              |                   |              |         | [](#__codelineno-143-16) | rda-app-controller            | 111.92.12.42 | Up 2 Weeks ago    | 363536fa5086 | 7.3     | [](#__codelineno-143-17) |                               |              |                   |              |         | [](#__codelineno-143-18) | rda-app-controller            | 111.92.12.42 | Up 2 Weeks ago    | f18ea5bee53e | 7.3     | [](#__codelineno-143-19) +---------------+---------------+--------------+-------------------+--------------+---------+`

*   Down RDAF Application services (AIA/OIA) and verify that all services are down

`[](#__codelineno-144-1) rdafk8s app down <AIA/OIA>`

*   Verify RDAF Worker services status by running the Below Command

`[](#__codelineno-145-1) rdafk8s worker status`

Example

`[](#__codelineno-146-1) +------------+--------------+----------------+--------------+-----+ [](#__codelineno-146-2) | Name       | Host         | Status         | Container Id | Tag | [](#__codelineno-146-3) +------------+--------------+----------------+--------------+-----+ [](#__codelineno-146-4) | rda-worker | 111.92.12.43 | Up 1 Weeks ago | c3bcc73eefa4 | 3.3 | [](#__codelineno-146-5) |            |              |                |              |     | [](#__codelineno-146-6) | rda-worker | 111.92.12.43 | Up 6 Days ago  | 31a649221da4 | 3.3 | [](#__codelineno-146-7) |            |              |                |              |     | [](#__codelineno-146-8) +------------+--------------+----------------+--------------+-----+`

*   Down RDAF Worker services and verify that Worker services are down

`[](#__codelineno-147-1) rdafk8s worker down`

*   Down log monitoring services and verify that log monitoring services are down

`[](#__codelineno-148-1) rdafk8s log_monitoring down`

*   Verify RDAF Platform services status by running the Below Command

`[](#__codelineno-149-1) rdafk8s platform status`

Example

`[](#__codelineno-150-1) +----------------------+--------------+----------------+--------------+-----+ [](#__codelineno-150-2) | Name                 | Host         | Status         | Container Id | Tag | [](#__codelineno-150-3) +----------------------+--------------+----------------+--------------+-----+ [](#__codelineno-150-4) | rda-api-server       | 111.92.12.41 | Up 2 Weeks ago | fd2f23dd546c | 3.3 | [](#__codelineno-150-5) |                      |              |                |              |     | [](#__codelineno-150-6) | rda-api-server       | 111.92.12.41 | Up 2 Weeks ago | 3a8ef8f95c6b | 3.3 | [](#__codelineno-150-7) |                      |              |                |              |     | [](#__codelineno-150-8) | rda-registry         | 111.92.12.41 | Up 2 Weeks ago | bf034c853eb4 | 3.3 | [](#__codelineno-150-9) |                      |              |                |              |     | [](#__codelineno-150-10) | rda-registry         | 111.92.12.41 | Up 2 Weeks ago | b66fc19c90bb | 3.3 | [](#__codelineno-150-11) |                      |              |                |              |     | [](#__codelineno-150-12) | rda-identity         | 111.92.12.41 | Up 2 Weeks ago | d6909f3295b3 | 3.3 | [](#__codelineno-150-13) |                      |              |                |              |     | [](#__codelineno-150-14) | rda-identity         | 111.92.12.41 | Up 2 Weeks ago | bc3813d4350a | 3.3 | [](#__codelineno-150-15) |                      |              |                |              |     | [](#__codelineno-150-16) | rda-fsm              | 111.92.12.41 | Up 2 Weeks ago | 14af867823c7 | 3.3 | [](#__codelineno-150-17) |                      |              |                |              |     | [](#__codelineno-150-18) | rda-fsm              | 111.92.12.41 | Up 2 Weeks ago | 5fe613b3025b | 3.3 | [](#__codelineno-150-19) |                      |              |                |              |     | [](#__codelineno-150-20) | rda-chat-helper      | 111.92.12.41 | Up 2 Weeks ago | e4ac9b2ee0ca | 3.3 | [](#__codelineno-150-21) +----------------------+--------------+----------------+--------------+-----+`

*   Down RDAF platform services and verify that Worker services are down

`[](#__codelineno-151-1) rdafk8s platform down`

*   To down the mariadb

Down all services except minio, opensearch services

`[](#__codelineno-152-1) rdafk8s infra down --service mariadb`

`[](#__codelineno-153-1) rdafk8s infra up --service minio`

`[](#__codelineno-154-1) rdafk8s infra up --service opensearch`

*   **Now Execute the Restore Steps**

Note

Mariadb pods should be down, Minio , Nats and Opensearch pods should be running while running restore.

`[](#__codelineno-155-1) rdafk8s restore --debug --from-dir <nfs-mounted-volume/required-backup-folder>` 

Or

`[](#__codelineno-156-1) rdafk8s restore --debug --from-dir <nfs-mounted-volume/required-backup-folder>  --no-prompt >>restore.log  (for redirecting logs to a file)`

Note

1.In the above command the required-backup folder is different from the backup folder which we created as part of backup creation earlier. It should be the directory, to which we want the data to be restored to.

2.We have to use `--from-tar` instead of `--from-dir` if we have backup as `tar.gz` file.

3.Make sure no errors are ignored during the restore operation.

*   For starting mariadb , follow the below steps

Now start the infra

`[](#__codelineno-157-1) rdafk8s infra up --service mariadb`

Please check if all infra pods are up using

`[](#__codelineno-158-1) kubectl get pods -n rda-fabric`

Please check if all infra containers are up and no containers are restarting using

`[](#__codelineno-159-1) rdafk8s infra status`

`[](#__codelineno-160-1) +-------------------+--------------+-----------------+--------------+------------------------------+ [](#__codelineno-160-2) | Name              | Host         | Status          | Container Id | Tag                          | [](#__codelineno-160-3) +-------------------+--------------+-----------------+--------------+------------------------------+ [](#__codelineno-160-4) | haproxy           | 10.95.131.41 | Up 3 months     | fd008d37d1e0 | 1.0.2.1                      | [](#__codelineno-160-5) |                   |              |                 |              |                              | [](#__codelineno-160-6) | haproxy           | 10.95.131.42 | Up 3 months     | 098f770bec0e | 1.0.2.1                      | [](#__codelineno-160-7) |                   |              |                 |              |                              | [](#__codelineno-160-8) | keepalived        | 10.95.131.41 | active          | N/A          | N/A                          | [](#__codelineno-160-9) |                   |              |                 |              |                              | [](#__codelineno-160-10) | keepalived        | 10.95.131.42 | active          | N/A          | N/A                          | [](#__codelineno-160-11) |                   |              |                 |              |                              | [](#__codelineno-160-12) | rda-nats          | 10.95.131.41 | Up 25 Weeks ago | ace867e71b4c | 1.0.2.1                      | [](#__codelineno-160-13) |                   |              |                 |              |                              | [](#__codelineno-160-14) | rda-nats          | 10.95.131.42 | Up 11 Weeks ago | 914c738aaa5b | 1.0.2.1                      | [](#__codelineno-160-15) +-------------------+--------------+-----------------+--------------+------------------------------+`

and

`[](#__codelineno-161-1) rdafk8s infra healthcheck`

Now, start the platform again.

`[](#__codelineno-162-1) rdafk8s platform up`

Run the following Commands and all are healthy/without any errors.

`[](#__codelineno-163-1) kubectl get pods -n rda-fabric`

`[](#__codelineno-164-1) rdac pods`

`[](#__codelineno-165-1) rdac healthcheck`

Now, start the worker

`[](#__codelineno-166-1) rdafk8s worker up`

Run the following Commands

`[](#__codelineno-167-1) kubectl get pods -n rda-fabric`

`[](#__codelineno-168-1) rdac pods`

Start the log\_monitoring services

`[](#__codelineno-169-1) rdafk8s log_monitoring up`

Verify that log\_monitoring services are up using the below Commands

`[](#__codelineno-170-1) kubectl get pods -n rda-fabric`

`[](#__codelineno-171-1) rdafk8s log_monitoring status`

Now start the app

`[](#__codelineno-172-1) rdafk8s app up OIA`

Check using these Commands

`[](#__codelineno-173-1) kubectl get pods -n rda-fabric`

`[](#__codelineno-174-1) rdafk8s app status`

`[](#__codelineno-175-1) rdac pods`

Example

`[](#__codelineno-176-1) +-------+----------------------------------------+-------------+----------------+----------+-------------+-------------------+--------+--------------+---------------+--------------+ [](#__codelineno-176-2) | Cat   | Pod-Type                               | Pod-Ready   | Host           | ID       | Site        | Age               |   CPUs |   Memory(GB) | Active Jobs   | Total Jobs   | [](#__codelineno-176-3) |-------+----------------------------------------+-------------+----------------+----------+-------------+-------------------+--------+--------------+---------------+--------------| [](#__codelineno-176-4) | App   | alert-ingester                         | True        | rda-alert-inge | c089c592 |             | 17 days, 20:14:00 |      8 |        31.33 |               |              | [](#__codelineno-176-5) | App   | alert-ingester                         | True        | rda-alert-inge | 1d3782ca |             | 17 days, 20:13:52 |      8 |        31.33 |               |              | [](#__codelineno-176-6) | App   | alert-processor                        | True        | rda-alert-proc | 6f194a11 |             | 0:12:31           |      8 |        31.33 |               |              | [](#__codelineno-176-7) | App   | alert-processor                        | True        | rda-alert-proc | 8bf388b9 |             | 0:08:49           |      8 |        31.33 |               |              | [](#__codelineno-176-8) | App   | alert-processor-companion              | True        | rda-alert-proc | af40d4d9 |             | 19 days, 6:09:53  |      8 |        31.33 |               |              | [](#__codelineno-176-9) | App   | alert-processor-companion              | True        | rda-alert-proc | e4ebf974 |             | 2 days, 3:23:07   |      8 |        31.33 |               |              | [](#__codelineno-176-10) | App   | asset-dependency                       | True        | rda-asset-depe | 50d810be |             | 19 days, 6:30:21  |      8 |        31.33 |               |              | [](#__codelineno-176-11) | App   | asset-dependency                       | True        | rda-asset-depe | 326c4f86 |             | 19 days, 6:30:21  |      8 |        31.33 |               |              | [](#__codelineno-176-12) | App   | authenticator                          | True        | rda-identity-7 | 9d251ca9 |             | 19 days, 6:30:18  |      8 |        31.33 |               |              | [](#__codelineno-176-13) | App   | authenticator                          | True        | rda-identity-7 | 6cff78a4 |             | 19 days, 6:30:21  |      8 |        31.33 |               |              | [](#__codelineno-176-14) +-------+----------------------------------------+-------------+----------------+----------+-------------+-------------------+--------+--------------+---------------+--------------+`

`[](#__codelineno-177-1) rdac healthcheck`

Example

`[](#__codelineno-178-1) +-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+ [](#__codelineno-178-2) | Cat       | Pod-Type                               | Host         | ID       | Site        | Health Parameter                                    | Status   | Message                                                                                                                                                                                                                                                                                 | [](#__codelineno-178-3) |-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| [](#__codelineno-178-4) | rda_app   | alert-ingester                         | rda-alert-in | 1d3782ca |             | service-status                                      | ok       |                                                                                                                                                                                                                                                                                         | [](#__codelineno-178-5) | rda_app   | alert-ingester                         | rda-alert-in | 1d3782ca |             | minio-connectivity                                  | ok       |                                                                                                                                                                                                                                                                                         | [](#__codelineno-178-6) | rda_app   | alert-ingester                         | rda-alert-in | 1d3782ca |             | service-dependency:configuration-service            | ok       | 2 pod(s) found for configuration-service                                                                                                                                                                                                                                                | [](#__codelineno-178-7) | rda_app   | alert-ingester                         | rda-alert-in | 1d3782ca |             | service-initialization-status                       | ok       |                                                                                                                                                                                                                                                                                         | [](#__codelineno-178-8) | rda_app   | alert-ingester                         | rda-alert-in | 1d3782ca |             | kafka-connectivity                                  | ok       | Cluster=nzyeX9qkR-ChWXC0fRvSyQ, Broker=0, Brokers=[0, 2, 1]                                                                                                                                                                                                                             | [](#__codelineno-178-9) | rda_app   | alert-ingester                         | rda-alert-in | c089c592 |             | service-status                                      | ok       |                                                                                                                                                                                                                                                                                         | [](#__codelineno-178-10) | rda_app   | alert-ingester                         | rda-alert-in | c089c592 |             | minio-connectivity                                  | ok       |                                                                                                                                                                                                                                                                                         | [](#__codelineno-178-11) | rda_app   | alert-ingester                         | rda-alert-in | c089c592 |             | service-dependency:configuration-service            | ok       | 2 pod(s) found for configuration-service                                                                                                                                                                                                                                                | [](#__codelineno-178-12) | rda_app   | alert-ingester                         | rda-alert-in | c089c592 |             | service-initialization-status                       | ok       |                                                                                                                                                                                                                                                                                         | [](#__codelineno-178-13) | rda_app   | alert-ingester                         | rda-alert-in | c089c592 |             | kafka-connectivity                                  | ok       | Cluster=nzyeX9qkR-ChWXC0fRvSyQ, Broker=0, Brokers=[0, 2, 1]                                                                                                                                                                                                                             | [](#__codelineno-178-14) +-----------+----------------------------------------+--------------+----------+-------------+-----------------------------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+`

RDAF Restore – Platform/Service VMs are in-tact, All Services are also healthy. The purpose is just to roll back to an earlier snapshot

or

Upgrade is done to the app/platform, and if the upgrade fails, and if we want to revert to the previous snapshot taken before starting upgrade.

**Below are the steps to achieve the above.**

*   Take a full backup.

`[](#__codelineno-179-1) rdaf backup --debug --dest-dir <nfs mounted backup volume>`

Note

This is to make sure we have a latest snapshot

*   Verify RDAF OIA/AIA (AIOps) application services status by running the Below Command

`[](#__codelineno-180-1) rdaf app status`

Example

 `[](#__codelineno-181-1)  +-----------------------------------+----------------+------------+--------------+-------+ [](#__codelineno-181-2)  | Name                              | Host           | Status     | Container Id | Tag   | [](#__codelineno-181-3)  +-----------------------------------+----------------+------------+--------------+-------+ [](#__codelineno-181-4)  | cfx-rda-app-controller            | 192.168.107.67 | Up 3 hours | 399c4de2e5f9 | daily | [](#__codelineno-181-5)  |                                   |                |            |              |       | [](#__codelineno-181-6)  | cfx-rda-app-controller            | 192.168.107.66 | Up 3 hours | f8928bea6837 | daily | [](#__codelineno-181-7)  |                                   |                |            |              |       | [](#__codelineno-181-8)  | cfx-rda-reports-registry          | 192.168.107.67 | Up 3 hours | c4d6ab852b9e | daily | [](#__codelineno-181-9)  |                                   |                |            |              |       | [](#__codelineno-181-10)  | cfx-rda-reports-registry          | 192.168.107.66 | Up 3 hours | 5816845142b2 | daily | [](#__codelineno-181-11)  |                                   |                |            |              |       | [](#__codelineno-181-12)  | cfx-rda-notification-service      | 192.168.107.67 | Up 3 hours | 202e4282eca4 | daily | [](#__codelineno-181-13)  |                                   |                |            |              |       | [](#__codelineno-181-14)  | cfx-rda-notification-service      | 192.168.107.66 | Up 3 hours | efbb103f54ec | daily | [](#__codelineno-181-15)  |                                   |                |            |              |       | [](#__codelineno-181-16)  | cfx-rda-file-browser              | 192.168.107.67 | Up 3 hours | cdb24f11a38b | daily | [](#__codelineno-181-17)  |                                   |                |            |              |       | [](#__codelineno-181-18)  | cfx-rda-file-browser              | 192.168.107.66 | Up 3 hours | db8ccb256595 | daily | [](#__codelineno-181-19)  |                                   |                |            |              |       | [](#__codelineno-181-20)  | cfx-rda-configuration-service     | 192.168.107.67 | Up 3 hours | ddc7075e0da8 | daily | [](#__codelineno-181-21)  |                                   |                |            |              |       | [](#__codelineno-181-22)  | cfx-rda-configuration-service     | 192.168.107.66 | Up 3 hours | 946b7e1c098f | daily | [](#__codelineno-181-23)  |                                   |                |            |              |       | [](#__codelineno-181-24)  | cfx-rda-alert-ingester            | 192.168.107.67 | Up 3 hours | 3901e1cee9dd | daily | [](#__codelineno-181-25)  +-----------------------------------+----------------+------------+--------------+-------+`

*   Bring down RDAF Application services (AIA/OIA) and verify that all services are down

`[](#__codelineno-182-1) rdaf app down <AIA/OIA>`

*   Verify RDAF Worker services status by running the Below Command

`[](#__codelineno-183-1) rdaf worker status`

Example

`[](#__codelineno-184-1) +------------+----------------+-------------+--------------+------------------------------------+ [](#__codelineno-184-2) | Name       | Host           | Status      | Container Id | Tag                                | [](#__codelineno-184-3) +------------+----------------+-------------+--------------+------------------------------------+ [](#__codelineno-184-4) | rda_worker | 192.168.131.46 | Up 3 hours  | 6e6c190df92f | daily                              | [](#__codelineno-184-5) |            |                |             |              |                                    | [](#__codelineno-184-6) | rda_worker | 192.168.131.47 | Up 3 hours  | 0f8350735ee8 | daily                              | [](#__codelineno-184-7) |            |                |             |              |                                    | [](#__codelineno-184-8) | rda_worker | 192.168.131.46 | Up 31 hours | 16db3960ab64 | 500d94c8dad1767f24fdb254da16542b90 | [](#__codelineno-184-9) |            |                |             |              | 7e505975dfc464f82c671d4c5a3a04     | [](#__codelineno-184-10) +------------+----------------+-------------+--------------+------------------------------------+`

*   Bring down RDAF Worker services and verify that Worker services are down

`[](#__codelineno-185-1) rdaf worker down`

*   Verify RDAF Platform services status by running the Below Command

`[](#__codelineno-186-1) rdaf platform status`

Example

`[](#__codelineno-187-1) +--------------------------+----------------+------------------+--------------+-------+ [](#__codelineno-187-2) | Name                     | Host           | Status           | Container Id | Tag   | [](#__codelineno-187-3) +--------------------------+----------------+------------------+--------------+-------+ [](#__codelineno-187-4) | rda_api_server           | 192.168.107.61 | Up About an hour | 5b924dddc5cf | daily | [](#__codelineno-187-5) |                          |                |                  |              |       | [](#__codelineno-187-6) | rda_api_server           | 192.168.107.62 | Up About an hour | 2919b3d6d505 | daily | [](#__codelineno-187-7) |                          |                |                  |              |       | [](#__codelineno-187-8) | rda_registry             | 192.168.107.61 | Up About an hour | 1571eb62ab3e | daily | [](#__codelineno-187-9) |                          |                |                  |              |       | [](#__codelineno-187-10) | rda_registry             | 192.168.107.62 | Up About an hour | 0b64dafc8d28 | daily | [](#__codelineno-187-11) |                          |                |                  |              |       | [](#__codelineno-187-12) | rda_scheduler            | 192.168.107.61 | Up About an hour | 4d0786562537 | daily | [](#__codelineno-187-13) |                          |                |                  |              |       | [](#__codelineno-187-14) | rda_scheduler            | 192.168.107.62 | Up About an hour | ddad47f50fb2 | daily | [](#__codelineno-187-15) |                          |                |                  |              |       | [](#__codelineno-187-16) | rda_collector            | 192.168.107.61 | Up About an hour | 3e71a7308ab3 | daily | [](#__codelineno-187-17) |                          |                |                  |              |       | [](#__codelineno-187-18) | rda_collector            | 192.168.107.62 | Up About an hour | c16a93539535 | daily | [](#__codelineno-187-19) +--------------------------+----------------+------------------+--------------+-------+`

*   Bring down RDAF platform services and verify that Worker services are down

`[](#__codelineno-188-1) rdaf platform down`

*   Verify RDAF Infra services status by running the Below Command

`[](#__codelineno-189-1) rdaf infra status`

Example

`[](#__codelineno-190-1) +----------------------+----------------+------------------+--------------+------------------------------+ [](#__codelineno-190-2) | Name                 | Host           | Status           | Container Id | Tag                          | [](#__codelineno-190-3) +----------------------+----------------+------------------+--------------+------------------------------+ [](#__codelineno-190-4) | haproxy              | 192.168.107.63 | Up About an hour | cf89a08204ac | 1.0.3                        | [](#__codelineno-190-5) |                      |                |                  |              |                              | [](#__codelineno-190-6) | haproxy              | 192.168.107.64 | Up About an hour | d920531f9b0f | 1.0.3                        | [](#__codelineno-190-7) |                      |                |                  |              |                              | [](#__codelineno-190-8) | keepalived           | 192.168.107.63 | active           | N/A          | N/A                          | [](#__codelineno-190-9) |                      |                |                  |              |                              | [](#__codelineno-190-10) | keepalived           | 192.168.107.64 | active           | N/A          | N/A                          | [](#__codelineno-190-11) |                      |                |                  |              |                              | [](#__codelineno-190-12) | nats                 | 192.168.107.63 | Up About an hour | 0e2c38762d71 | 1.0.3                        | [](#__codelineno-190-13) |                      |                |                  |              |                              | [](#__codelineno-190-14) | nats                 | 192.168.107.63 | Up About an hour | 8d21ff09ce3b | 1.0.3                        | [](#__codelineno-190-15) |                      |                |                  |              |                              | [](#__codelineno-190-16) | minio                | 192.168.107.64 | Up About an hour | f3b29b36ec85 | RELEASE.2023-09-30T07-02-29Z | [](#__codelineno-190-17) |                      |                |                  |              |                              | [](#__codelineno-190-18) | minio                | 192.168.107.63 | Up About an hour | f0448e7b7f66 | RELEASE.2023-09-30T07-02-29Z | [](#__codelineno-190-19) |                      |                |                  |              |                              | [](#__codelineno-190-20) | minio                | 192.168.107.64 | Up About an hour | 9ec7ea77e539 | RELEASE.2023-09-30T07-02-29Z | [](#__codelineno-190-21) |                      |                |                  |              |                              | [](#__codelineno-190-22) | minio                | 192.168.107.63 | Up About an hour | 8aee1d166684 | RELEASE.2023-09-30T07-02-29Z | [](#__codelineno-190-23) +----------------------+----------------+------------------+--------------+------------------------------+`

Bring down all services except minio, opensearch services

`[](#__codelineno-191-1) rdaf infra down`

`[](#__codelineno-192-1) rdaf infra up --service minio`

`[](#__codelineno-193-1) rdaf infra up --service opensearch`

*   **Now Execute the Restore Steps**

Note

Mariadb containers should be exited, Minio and Opensearch containers should be running while running restore.

`[](#__codelineno-194-1) rdaf restore --debug --from-dir <nfs-mounted-volume/required-backup-folder>`

Note

1.  In the above command the required-backup folder is different from the backup folder which we created as part of backup creation earlier. It should be the directory, to which we want the data to be restored to.
    
2.  Make sure no errors are ignored during the restore operation.
    

Now start the infra components

`[](#__codelineno-195-1) rdaf infra up`

Please check if all infra containers are up and no containers are in restarting status using below command

`[](#__codelineno-196-1) rdaf infra status`

and

`[](#__codelineno-197-1) rdaf infra healthcheck`

Example

`[](#__codelineno-198-1) +----------------+-----------------+--------+----------------------+----------------+--------------+ [](#__codelineno-198-2) | Name           | Check           | Status | Reason               | Host           | Container Id | [](#__codelineno-198-3) +----------------+-----------------+--------+----------------------+----------------+--------------+ [](#__codelineno-198-4) | haproxy        | Port Connection | OK     | N/A                  | 192.168.107.63 | fdb5a96537b8 | [](#__codelineno-198-5) | haproxy        | Service Status  | OK     | N/A                  | 192.168.107.63 | fdb5a96537b8 | [](#__codelineno-198-6) | haproxy        | Firewall Port   | OK     | N/A                  | 192.168.107.64 | fdb5a96537b8 | [](#__codelineno-198-7) | haproxy        | Port Connection | OK     | N/A                  | 192.168.107.63 | f370fcb66b13 | [](#__codelineno-198-8) | haproxy        | Service Status  | OK     | N/A                  | 192.168.107.63 | f370fcb66b13 | [](#__codelineno-198-9) | haproxy        | Firewall Port   | OK     | N/A                  | 192.168.107.63 | f370fcb66b13 | [](#__codelineno-198-10) | keepalived     | Service Status  | OK     | N/A                  | 192.168.107.63 | N/A          | [](#__codelineno-198-11) | keepalived     | Service Status  | OK     | N/A                  | 192.168.107.64 | N/A          | [](#__codelineno-198-12) | nats           | Port Connection | OK     | N/A                  | 192.168.107.63 | 129efa5b015c | [](#__codelineno-198-13) | nats           | Service Status  | OK     | N/A                  | 192.168.107.63 | 129efa5b015c | [](#__codelineno-198-14) | nats           | Firewall Port   | OK     | N/A                  | 192.168.107.64 | 129efa5b015c | [](#__codelineno-198-15) | nats           | Port Connection | OK     | N/A                  | 192.168.107.63 | fe5f190108b0 | [](#__codelineno-198-16) | nats           | Service Status  | OK     | N/A                  | 192.168.107.63 | fe5f190108b0 | [](#__codelineno-198-17) | nats           | Firewall Port   | OK     | N/A                  | 192.168.107.63 | fe5f190108b0 | [](#__codelineno-198-18) | minio          | Port Connection | OK     | N/A                  | 192.168.107.64 | 19ccfdeab789 | [](#__codelineno-198-19) +----------------+-----------------+--------+----------------------+----------------+--------------+`

Now, start the platform services

`[](#__codelineno-199-1) rdaf platform up`

Run below Commands

`[](#__codelineno-200-1) rdac pods`

`[](#__codelineno-201-1) rdac healthcheck`

Now, start the worker

`[](#__codelineno-202-1) rdaf worker up`

Now, start the app services

`[](#__codelineno-203-1) rdaf app up OIA/AIA`

****6\. CFX Self Monitor Service****
------------------------------------

### **6.1 What is CFX Self Monitor**

**CFX Self Monitor** is an application service to monitor RDAF deployments to automatically ensure that the setups are healthy and functioning properly. It can be used to monitor RDAF deployments e.g.,

*   Production deployments
    
*   Demo deployments
    
*   Longevity testing
    
*   Basic sanity checks for new deployments
    
*   Pre / Post upgrade verification of existing deployments
    

### ****6.2 Examples of Health and Functionality Checks****

Below are some of the health checks it performs, but not limited to:

*   Ensure all the RDA Fabric pods are up and running and have not restarted
    
*   Ensure there are some alerts received and incidents created in last 24 hours
    
*   Ensure users are able to login
    
*   Ensure basic UI functionality is working
    
*   Others...
    

### ****6.3 What CFX Self Monitor service is "NOT"****

The purpose of CFX Self Service is not to:

*   Replace general infrastructure monitoring applications like prometheus, zabbix etc.
    
*   Monitor kubernetes deployment & pods
    
*   Develop tests / system tests
    

The idea is to check the health and basic functionality of RDAF overall. It is not a complete end-to-end testing framework to test every feature.

### ****6.4 Features****

*   Sanity test cases are written using yaml
    
*   Automatically run the checks and send messages with results. (Currently, **Slack** and **Webex teams** notifications are supported)
    
*   Customize deployment specific parameters (API username / password etc.)
    
*   Ability to customize the test suites that come out of the box (e.g Expected RDA pods that need to be present)
    
*   Enable / Disable test suites
    
*   Add new deployment specific test suites in yaml without having to change source code or commit them to source code management systems
    
*   Current framework supports writing test cases for the output of rdac commands and API responses
    

### ****6.5 Getting Started****

CFX Self Monitor service is deployed as a docker container. Please follow the below steps configuring and bringing it up.

**1**. Create a new user (e.g., `monitoring@cfx.com`) with **MSP Read Only User** role in RDAF portal UI.

Tip

Please refer **RDAF Platform Administration** for more information on creating a **new user** and assigning **MSP Read Only User** role

**2**: Login into RDAF UI portal with new user account to update the default password **changeme**

**3**: Create a file called `/opt/rdaf_self_monitor/resources/tmp/portal_pwd` and update it with newly created user's password.

Note

Please skip the below step, if `config.json` file already exists in the below mentioned path with appropriate RDAF network configuration.

**4**. Download the **RDA Network Configuration** from RDAF UI portal: **Main Menu --> Configuration --> RDA Administration --> Network** and save the configuration into `/opt/rdaf/config/network_config/config.json` file

**5**. Create the below directory structure and create a docker-compose file for CFX Self Monitor service.

``[](#__codelineno-204-1) sudo mkdir -p /opt/rdaf_self_monitor/resources/tmp [](#__codelineno-204-2) sudo mkdir -p /opt/rdaf_self_monitor/tests [](#__codelineno-204-3) sudo chown -R `id -u`:`id -g` /opt/rdaf_self_monitor [](#__codelineno-204-4) touch /opt/rdaf_self_monitor/resources/settings.json``

Example

`[](#__codelineno-205-1) cd /opt/rdaf_self_monitor [](#__codelineno-205-2) [](#__codelineno-205-3) cat > cfx-self-monitor-docker-compose.yml <<EOF [](#__codelineno-205-4) version: '3.1' [](#__codelineno-205-5) services: [](#__codelineno-205-6)   cfx_self_monitor: [](#__codelineno-205-7)     image: cfxregistry.cloudfabrix.io/ubuntu-cfx-self-monitor:daily [](#__codelineno-205-8)     restart: unless-stopped [](#__codelineno-205-9)     mem_limit: 4G [](#__codelineno-205-10)     memswap_limit: 4G [](#__codelineno-205-11)     oom_kill_disable: false [](#__codelineno-205-12)     volumes: [](#__codelineno-205-13)     - /opt/rdaf/config/network_config/:/network_config [](#__codelineno-205-14)     - /opt/rdaf_self_monitor/:/cfx_self_monitor [](#__codelineno-205-15)     environment: [](#__codelineno-205-16)       RDA_NETWORK_CONFIG: /network_config/config.json [](#__codelineno-205-17)       CFX_SELF_MONITORING_DIR: /cfx_self_monitor [](#__codelineno-205-18)     privileged: true [](#__codelineno-205-19)     secrets: [](#__codelineno-205-20)       - portal_pwd [](#__codelineno-205-21) secrets: [](#__codelineno-205-22)   portal_pwd: [](#__codelineno-205-23)     file: /opt/rdaf_self_monitor/resources/tmp/portal_pwd [](#__codelineno-205-24) [](#__codelineno-205-25) EOF`

**5**. Docker Login

Run the below command to create and save the docker login session into CloudFabrix's secure docker repository.

`[](#__codelineno-206-1) docker login -u='readonly' -p='readonly' cfxregistry.cloudfabrix.io`

**6**. Bring up the CFX Self Monitor service.

`[](#__codelineno-207-1) cd /opt/rdaf_self_monitor [](#__codelineno-207-2) docker-compose -f cfx-self-monitor-docker-compose.yml pull  [](#__codelineno-207-3) docker-compose -f cfx-self-monitor-docker-compose.yml up -d`

### ****6.6 Customization****

There are several customizations provided in CFX Self Monitor service.

#### ****6.6.1 Customizing Deployment Specific Parameters****

The `settings.json` file in `/opt/rdaf_self_monitor/resources` directory has deployment specific customizations.

ExampleSample Configuration

`[](#__codelineno-208-1) { [](#__codelineno-208-2)   "deployment_name": "Customer ACME Staging Deployment", [](#__codelineno-208-3)   "portal_url": "https://<URL Of THE PORTAL>", [](#__codelineno-208-4)   "portal_uname": "monitoring@cfx.com", [](#__codelineno-208-5)   "webex": { [](#__codelineno-208-6)     "comment": "Look at the instructions below for how to get these from webex", [](#__codelineno-208-7)     "token": "WEBEX TOKEN", [](#__codelineno-208-8)     "roomId": "WEBEX ROOM ID" [](#__codelineno-208-9)   }, [](#__codelineno-208-10)   "slack": { [](#__codelineno-208-11)     "comment": "Look at the instructions below for how to get these from slack", [](#__codelineno-208-12)     "token": "SLACK TOKEN", [](#__codelineno-208-13)     "channel": "SLACK CHANNEL NAME", [](#__codelineno-208-14)     "channel_id": "SLACK CHANNEL ID", [](#__codelineno-208-15)     "team": { [](#__codelineno-208-16)       "user_name_to_ids": { [](#__codelineno-208-17)         "comment": "This is for readability purposes only to find name from id. Not used in the code", [](#__codelineno-208-18)         "U1HST5K6X": "John Doe", [](#__codelineno-208-19)         "UCAPL0CBT": "Chris J", [](#__codelineno-208-20)       }, [](#__codelineno-208-21)       "comment": "List the slack user ids to mentioned with @ while sending slack messages", [](#__codelineno-208-22)       "critical": ["<@U1HST5K6X>", "<@UCAPL0CBT>"], [](#__codelineno-208-23)       "high": ["<@U1HST5K6X>"], [](#__codelineno-208-24)       "medium": [], [](#__codelineno-208-25)       "low": [] [](#__codelineno-208-26)     } [](#__codelineno-208-27)   }, [](#__codelineno-208-28)   "suites": { [](#__codelineno-208-29)     "comment": "Test case customizations: How to change variables of test cases", [](#__codelineno-208-30)     "test_get_menu": { "variables": {"mandatory_apps": ["Administration", "User Dashboards"]}}, [](#__codelineno-208-31)     "test_get_deployed_apps": { [](#__codelineno-208-32)       "comment": "Example of how to disable a test suite - Disable test_get_deployed_apps suite", [](#__codelineno-208-33)       "variables": {"mandatory_apps": ["dummy"]} [](#__codelineno-208-34)     } [](#__codelineno-208-35)   } [](#__codelineno-208-36) }`

`[](#__codelineno-209-1) { [](#__codelineno-209-2)   "deployment_name": "Cloudfabix RDAF Deployment - Production", [](#__codelineno-209-3)   "portal_url": "https://10.11.5.63", [](#__codelineno-209-4)   "portal_uname": "monitoring@cfx.com", [](#__codelineno-209-5)   "slack": { [](#__codelineno-209-6)     "token": "xoxb-4596399623-4807485567556-XXXXXXXXXXXXXXXXXX", [](#__codelineno-209-7)     "channel": "cfx-rdaf-production-health", [](#__codelineno-209-8)     "channel_id": "C04SDTTABCD", [](#__codelineno-209-9)     "team": { [](#__codelineno-209-10)       "user_name_to_ids": { [](#__codelineno-209-11)         "$comment": "This is for readability purposes only to find name from id. Not used in the code", [](#__codelineno-209-12)         "U1HST5K6X": "John Doe", [](#__codelineno-209-13)         "UCAPL0CBT": "Jennifer Lawrance", [](#__codelineno-209-14)         "UCBFANC8M": "Ravikumar P", [](#__codelineno-209-15)         "U03A93YCGQ1": "David Singh", [](#__codelineno-209-16)         "UCAC311EU": "Bruce Lee" [](#__codelineno-209-17)       }, [](#__codelineno-209-18)       "critical": [ [](#__codelineno-209-19)         "<@U1HST5K6X>", [](#__codelineno-209-20)         "<@UCAPL0CBT>", [](#__codelineno-209-21)         "<@UCBFANC8M>", [](#__codelineno-209-22)         "<@U03A93YCGQ1>", [](#__codelineno-209-23)         "<@UCAC311EU>" [](#__codelineno-209-24)       ], [](#__codelineno-209-25)       "high": [ [](#__codelineno-209-26)         "<@U1HST5K6X>", [](#__codelineno-209-27)         "<@UCAPL0CBT>", [](#__codelineno-209-28)         "<@UCBFANC8M>" [](#__codelineno-209-29)       ], [](#__codelineno-209-30)       "medium": [ [](#__codelineno-209-31)         "<@U1HST5K6X>", [](#__codelineno-209-32)         "<@UCAPL0CBT>" [](#__codelineno-209-33)       ], [](#__codelineno-209-34)       "low": [] [](#__codelineno-209-35)     } [](#__codelineno-209-36)   }, [](#__codelineno-209-37)   "suites": { [](#__codelineno-209-38)     "test_pstream_status": { [](#__codelineno-209-39)       "enabled": false [](#__codelineno-209-40)     }, [](#__codelineno-209-41)     "test_get_menu": { [](#__codelineno-209-42)       "variables": { [](#__codelineno-209-43)         "mandatory_apps": [ [](#__codelineno-209-44)           "Administration", [](#__codelineno-209-45)           "User Dashboards" [](#__codelineno-209-46)         ] [](#__codelineno-209-47)       } [](#__codelineno-209-48)     }, [](#__codelineno-209-49)     "test_get_deployed_apps": { [](#__codelineno-209-50)       "enabled": false, [](#__codelineno-209-51)       "variables": { [](#__codelineno-209-52)         "mandatory_apps": [ [](#__codelineno-209-53)           "OIA" [](#__codelineno-209-54)         ] [](#__codelineno-209-55)       } [](#__codelineno-209-56)     }, [](#__codelineno-209-57)     "test_get_dashboards": { [](#__codelineno-209-58)       "enabled": false [](#__codelineno-209-59)     }, [](#__codelineno-209-60)     "test_pods": { [](#__codelineno-209-61)       "variables": { [](#__codelineno-209-62)         "pods": [ [](#__codelineno-209-63)           { [](#__codelineno-209-64)             "type": "worker", [](#__codelineno-209-65)             "count": 4 [](#__codelineno-209-66)           }, [](#__codelineno-209-67)           { [](#__codelineno-209-68)             "type": "alert-ingester", [](#__codelineno-209-69)             "count": 2 [](#__codelineno-209-70)           }, [](#__codelineno-209-71)           { [](#__codelineno-209-72)             "type": "alert-processor", [](#__codelineno-209-73)             "count": 2 [](#__codelineno-209-74)           }, [](#__codelineno-209-75)           { [](#__codelineno-209-76)             "type": "alert-processor-companion", [](#__codelineno-209-77)             "count": 2 [](#__codelineno-209-78)           }, [](#__codelineno-209-79)           { [](#__codelineno-209-80)             "type": "asset-dependency", [](#__codelineno-209-81)             "count": 2 [](#__codelineno-209-82)           }, [](#__codelineno-209-83)           { [](#__codelineno-209-84)             "type": "authenticator", [](#__codelineno-209-85)             "count": 2 [](#__codelineno-209-86)           }, [](#__codelineno-209-87)           { [](#__codelineno-209-88)             "type": "cfx-app-controller", [](#__codelineno-209-89)             "count": 2 [](#__codelineno-209-90)           }, [](#__codelineno-209-91)           { [](#__codelineno-209-92)             "type": "cfxdimensions-app-access-manager", [](#__codelineno-209-93)             "count": 2 [](#__codelineno-209-94)           }, [](#__codelineno-209-95)           { [](#__codelineno-209-96)             "type": "cfxdimensions-app-collaboration", [](#__codelineno-209-97)             "count": 2 [](#__codelineno-209-98)           }, [](#__codelineno-209-99)           { [](#__codelineno-209-100)             "type": "cfxdimensions-app-file-browser", [](#__codelineno-209-101)             "count": 2 [](#__codelineno-209-102)           }, [](#__codelineno-209-103)           { [](#__codelineno-209-104)             "type": "cfxdimensions-app-irm_service", [](#__codelineno-209-105)             "count": 2 [](#__codelineno-209-106)           }, [](#__codelineno-209-107)           { [](#__codelineno-209-108)             "type": "cfxdimensions-app-notification-service", [](#__codelineno-209-109)             "count": 2 [](#__codelineno-209-110)           }, [](#__codelineno-209-111)           { [](#__codelineno-209-112)             "type": "cfxdimensions-app-resource-manager", [](#__codelineno-209-113)             "count": 2 [](#__codelineno-209-114)           }, [](#__codelineno-209-115)           { [](#__codelineno-209-116)             "type": "configuration-service", [](#__codelineno-209-117)             "count": 2 [](#__codelineno-209-118)           }, [](#__codelineno-209-119)           { [](#__codelineno-209-120)             "type": "event-consumer", [](#__codelineno-209-121)             "count": 2 [](#__codelineno-209-122)           }, [](#__codelineno-209-123)           { [](#__codelineno-209-124)             "type": "ingestion-tracker", [](#__codelineno-209-125)             "count": 2 [](#__codelineno-209-126)           }, [](#__codelineno-209-127)           { [](#__codelineno-209-128)             "type": "ml-config", [](#__codelineno-209-129)             "count": 2 [](#__codelineno-209-130)           }, [](#__codelineno-209-131)           { [](#__codelineno-209-132)             "type": "reports-registry", [](#__codelineno-209-133)             "count": 2 [](#__codelineno-209-134)           }, [](#__codelineno-209-135)           { [](#__codelineno-209-136)             "type": "smtp-server", [](#__codelineno-209-137)             "count": 2 [](#__codelineno-209-138)           }, [](#__codelineno-209-139)           { [](#__codelineno-209-140)             "type": "user-preferences", [](#__codelineno-209-141)             "count": 2 [](#__codelineno-209-142)           }, [](#__codelineno-209-143)           { [](#__codelineno-209-144)             "type": "webhook-server", [](#__codelineno-209-145)             "count": 2 [](#__codelineno-209-146)           }, [](#__codelineno-209-147)           { [](#__codelineno-209-148)             "type": "api-server", [](#__codelineno-209-149)             "count": 2 [](#__codelineno-209-150)           }, [](#__codelineno-209-151)           { [](#__codelineno-209-152)             "type": "collector", [](#__codelineno-209-153)             "count": 2 [](#__codelineno-209-154)           }, [](#__codelineno-209-155)           { [](#__codelineno-209-156)             "type": "registry", [](#__codelineno-209-157)             "count": 2 [](#__codelineno-209-158)           }, [](#__codelineno-209-159)           { [](#__codelineno-209-160)             "type": "scheduler", [](#__codelineno-209-161)             "count": 2 [](#__codelineno-209-162)           } [](#__codelineno-209-163)         ] [](#__codelineno-209-164)       } [](#__codelineno-209-165)     } [](#__codelineno-209-166)   } [](#__codelineno-209-167) }`

*   **deployment\_name:** Name of the RDAF deployment. (e.g., RDAF Production Deployment)
    
*   **portal\_url:** Base URL to access the RDAF UI portal (e.g., https://10.97.10.10)
    
*   **portal\_uname:** Enter the username that was created under **Getting Started** section.
    
*   **slack:** Configure the Slack integration to enable the CFX Self Monitor service to send notification messages.
    
    *   **token:** Enter the `secret token` to establish a Slack connection
        
    *   **channel:** Enter the Slack channel name to which the notifications to be sent.
        
    *   **channel\_id:** ID of the Slack channel [https://help.socialintents.com/article/148-how-to-find-your-slack-team-id-and-slack-channel-id](https://help.socialintents.com/article/148-how-to-find-your-slack-team-id-and-slack-channel-id)
        
    *   **team:** Information about the support team for this deployment.
        
    *   **critical:** List of user IDs to be @mentioned for each severity (e.g., `Critical, Warning, Info etc.`). [https://www.workast.com/help/article/how-to-find-a-slack-user-id/](https://www.workast.com/help/article/how-to-find-a-slack-user-id/)
        
*   **webex:** Configure the Webex space or teams to enable the CFX Self Monitor service to send notification messages.
    
    *   **token:** Enter the token to establish a connection to the Webex space
        
    *   **roomId:** Enter the Webex room id to which the notifications to be sent.
        
*   **suites:** -> See follow up sections for details
    

#### ****6.6.2 Integrations For Messaging****

##### ****6.6.2.1 Webex****

1.  Create a webex bot:[https://developer.webex.com/my-apps/new/bot](https://developer.webex.com/my-apps/new/bot)
    
2.  Once the user creates the bot, it displays a token ID. Copy that token ID. This is the token you enter in **settings.json**\-> **webex**\-> **token**
    
3.  Go to webex spaces application, and create a space. Add the above bot as a member of the space.
    
4.  Get the list of rooms by executing the API from this URL:[https://developer.webex.com/docs/api/v1/rooms/list-rooms](https://developer.webex.com/docs/api/v1/rooms/list-rooms)
    
5.  Find out the space the user created above and copy the roomId. This is the roomId user should enter in **settings.json**\-> **webex**\-> **roomId**
    

##### ****6.6.2.2 Slack****

Please refer [Configure Slack to receive notifications over a Webhook](https://api.slack.com/messaging/webhooks)

#### ****6.6.3 Enable/Disable Test Suites****

By default, all the test suites bundled are executed. In order to disable a particular test suite, add the following in the settings.json

`[](#__codelineno-210-1) { [](#__codelineno-210-2)     ... [](#__codelineno-210-3)     "suites": { [](#__codelineno-210-4)         "test_pods": { [](#__codelineno-210-5)             "enabled": false [](#__codelineno-210-6)         } [](#__codelineno-210-7)     } [](#__codelineno-210-8) }`

#### ****6.6.4 Customize Test Parameters****

Each test suite has certain parameters that can be customized. User can see these parameters by opening the test suite yaml file.

The user can see below an example of customising a test parameter, This example changes the name mandatory applications to be returned with getMenu api call

Example

`[](#__codelineno-211-1) { [](#__codelineno-211-2)     ... [](#__codelineno-211-3)     "suites": { [](#__codelineno-211-4)         "test_get_menu": { "variables": {"mandatory_apps": ["Administration", "User Dashboards"]}} [](#__codelineno-211-5)     } [](#__codelineno-211-6) }`

#### ****6.6.5 Create New Test Suites (Advanced Usage)****

If a user wants to add new test suites in addition to the ones bundled with the application, the user can create the test suite as an yaml file and place it under (`/opt/rdaf_self_monitor/tests/api` or `/cfx_self_monitor/tests/rdac`). This directory corresponds to `/opt/rdaf_self_monitor/tests` on the host machine in the given `docker-compose yaml` file

In order to write test cases, the user must possess the following expertise.

**1**. **jsonpath**

a) [https://pypi.org/project/jsonpath-ng/](https://pypi.org/project/jsonpath-ng/)

b) [https://blogboard.io/blog/knowledge/jsonpath-python/](https://blogboard.io/blog/knowledge/jsonpath-python/)

c) [https://jsonpath.com/](https://jsonpath.com/)

**2**. **jinja templating**

a) [https://jinja.palletsprojects.com/en/3.1.x/](https://jinja.palletsprojects.com/en/3.1.x/)

b) [http://jinja.quantprogramming.com/](http://jinja.quantprogramming.com/)

****7\. Monitor RDAF Platform using Telegraf Agent****
------------------------------------------------------

**What is Telegraf Agent**

Telegraf is an open-source agent for collecting metrics and data on the system it's running on or from other services. Below are some of the key capabilities of Telegraf agent.

**Data Collection:** Telegraf collects metrics from configured sources. It can gather CPU, memory, disk, and I/O metrics, as well as data from a host of services and APIs.

**Intermediate Processing:** Telegraf has the ability to process and transform the data it collects. This can include aggregating metrics, converting values, or filtering out unnecessary data points before they are sent to the database.

**Data Output:** Telegraf can send the collected data to various destinations, utilizing its output plugins. This includes time series databases like InfluxDB, other databases like MongoDB, or services like Kafka, AWS CloudWatch, among others.

**Lightweight & Efficient:** It uses minimal system memory and CPU resources.

**Flexibility:** It can operate in different modes, acting either as an agent on a host gathering various system and application metrics or in a more decentralized way to collect metrics from remote sources over the network.

### ****7.1 Installation****

The Telegraf agent needs to be installed on all the virtual machines in the RDA Fabric platform to collect metrics from configured resources such as CPU, memory, disk, and network of both the host OS and containers.

Log into each RDA Fabric platform virtual machine as **rdauser** using an SSH client such as **PuTTY**

Run the commands below to create the directory structure for the Telegraf agent and assign appropriate user permissions.

`[](#__codelineno-212-1) sudo mkdir -p /opt/rdaf_telegraf/conf.d [](#__codelineno-212-2) sudo mkdir -p /opt/rdaf_telegraf/templates [](#__codelineno-212-3) sudo mkdir -p /opt/rdaf_telegraf/certs [](#__codelineno-212-4) sudo mkdir -p /opt/rdaf_telegraf/logs [](#__codelineno-212-5) sudo chown -R rdauser:rdauser /opt/rdaf_telegraf`

Create docker compose configuration file for Telegraf agent as shown below.

`[](#__codelineno-213-1) cd /opt/rdaf_telegraf [](#__codelineno-213-2) [](#__codelineno-213-3) cat > telegraf-docker-compose.yml <<EOF [](#__codelineno-213-4) version: '3.6' [](#__codelineno-213-5) services: [](#__codelineno-213-6)   telegraf: [](#__codelineno-213-7)     image: cfxregistry.cloudfabrix.io/rda-platform-telegraf:1.0.3 [](#__codelineno-213-8)     container_name: rda-telegraf [](#__codelineno-213-9)     restart: always [](#__codelineno-213-10)     network_mode: host [](#__codelineno-213-11)     mem_limit: 6G [](#__codelineno-213-12)     memswap_limit: 6G [](#__codelineno-213-13)     shm_size: 1gb [](#__codelineno-213-14)     ulimits: [](#__codelineno-213-15)       memlock: 514688 [](#__codelineno-213-16)     logging: [](#__codelineno-213-17)       driver: "json-file" [](#__codelineno-213-18)       options: [](#__codelineno-213-19)         max-size: "25m" [](#__codelineno-213-20)         max-file: "5" [](#__codelineno-213-21)     environment: [](#__codelineno-213-22)     - HOST_PROC=/host/proc [](#__codelineno-213-23)     - HOST_SYS=/host/sys [](#__codelineno-213-24)     - HOST_MOUNT_PREFIX=/host/rootfs [](#__codelineno-213-25)     - HOST_ETC=/host/etc [](#__codelineno-213-26)     volumes: [](#__codelineno-213-27)       - /opt/rdaf_telegraf:/etc/telegraf/ [](#__codelineno-213-28)       - /opt/rdaf_telegraf/conf.d:/etc/telegraf/conf.d [](#__codelineno-213-29)       - /opt/rdaf_telegraf/templates:/etc/telegraf/templates [](#__codelineno-213-30)       - /opt/rdaf_telegraf/certs:/etc/telegraf/certs [](#__codelineno-213-31)       - /opt/rdaf_telegraf/logs:/opt/rdaf/logs/telegraf/ [](#__codelineno-213-32)       - /var/run/docker.sock:/var/run/docker.sock:ro [](#__codelineno-213-33)       - /proc:/host/proc:ro [](#__codelineno-213-34)       - /sys:/host/sys:ro [](#__codelineno-213-35)       - /dev:/dev:ro [](#__codelineno-213-36)       - /etc:/host/etc:ro [](#__codelineno-213-37)       - /var/run/utmp:/var/run/utmp:ro [](#__codelineno-213-38)       - /:/host/rootfs:ro [](#__codelineno-213-39)       - /var/log:/host/log:ro [](#__codelineno-213-40)       - /opt/rdaf/logs:/host/rdaf/logs:ro [](#__codelineno-213-41) [](#__codelineno-213-42) [](#__codelineno-213-43) EOF`

### ****7.2 Configuration****

**Install SSL Certificates for Docker Daemon:**

Execute the following commands to copy the **Host OS SSL certificates** into the **Telegraf configuration** directory. This will enable Telegraf to collect metrics from the RDAF platform's container services.

`[](#__codelineno-214-1) sudo cp /etc/tlscerts/server/server.pem /opt/rdaf_telegraf/certs/server.pem [](#__codelineno-214-2) sudo cp /etc/tlscerts/server/server.key /opt/rdaf_telegraf/certs/server.key [](#__codelineno-214-3) sudo cp /etc/tlscerts/ca/ca.pem /opt/rdaf_telegraf/certs/server_ca.pem`

Update the Docker service's TLS configuration with the following command:

`[](#__codelineno-215-1) sudo sed -i "s/\"tlsverify\": true,/\"tlsverify\": false,/g" /etc/docker/daemon.json`

Restart the Docker daemon service to apply the changes.

`[](#__codelineno-216-1) sudo systemctl daemon-reload [](#__codelineno-216-2) sudo systemctl restart docker`

**Install SSL Certificates for RDAF Platform's Kafka:**

Telegraf agent sends collected metrics to the target RDAF platform's Kafka cluster services. The SSL certificates of target RDAF platform can be found under `/opt/rdaf/cert` folder.

Copy the CA certificate from `/opt/rdaf/cert/ca/ca.pem` to `/opt/rdaf_telegraf/certs/rdaf_ca.pem`

Copy the RDAF Platform's server certificate from `/opt/rdaf/cert/rdaf/rdaf.pem` to `/opt/rdaf_telegraf/certs/rdaf.pem`

Copy the RDAF Platform's server certificate key from `/opt/rdaf/cert/rdaf/rdaf.key` to `/opt/rdaf_telegraf/certs/rdaf.key`

**Configure Telegraf for Docker Metric Collection:**

Run the below commands to create Docker containers metric collection configuration file.

`[](#__codelineno-217-1) cd /opt/rdaf_telegraf/conf.d [](#__codelineno-217-2) [](#__codelineno-217-3) cat > docker.conf <<EOF [](#__codelineno-217-4) [[inputs.docker]] [](#__codelineno-217-5)   interval = "120s" [](#__codelineno-217-6)   endpoint = "unix:///var/run/docker.sock" [](#__codelineno-217-7)   gather_services = false [](#__codelineno-217-8)   source_tag = true [](#__codelineno-217-9)   container_name_include = [] [](#__codelineno-217-10)   container_name_exclude = [] [](#__codelineno-217-11)   container_state_include = ["created", "restarting", "running", "removing", "paused", "exited", "dead"] [](#__codelineno-217-12)   container_state_exclude = [] [](#__codelineno-217-13)   storage_objects = [] [](#__codelineno-217-14)   timeout = "5s" [](#__codelineno-217-15)   perdevice = false [](#__codelineno-217-16)   #perdevice_include = ["cpu","blkio","network"] [](#__codelineno-217-17)   total = true [](#__codelineno-217-18)   total_include = ["cpu", "blkio", "network"] [](#__codelineno-217-19)   docker_label_include = [] [](#__codelineno-217-20)   docker_label_exclude = ["DOCKERFILE", "author", "com.docker.compose.config-hash", "com.docker.compose.container-number", "com.docker.compose.depends_on", "com.docker.compose.image", "com.docker.compose.oneoff", "com.docker.compose.project.working_dir", "com.docker.compose.version", "io.macaw.buildtime", "io.macaw.builtby", "io.macaw.os", "io.macaw.os.buildtime", "org.opencontainers.image.base.name", "org.opencontainers.image.created", "org.opencontainers.image.description", "org.opencontainers.image.licenses", "org.opencontainers.image.ref.name", "org.opencontainers.image.title", "org.opencontainers.image.version", "org.opencontainers.image.vendor", "org.opencontainers.image.url", "org.opencontainers.image.source", "org.opencontainers.image.revision", "org.opencontainers.image.ref", "org.opencontainers.image.documentation", "org.opencontainers.image.authors", "org.opencontainers", "org.label-schema.version", "org.label-schema.vendor", "org.label-schema.vcs-url", "org.label-schema.url", "org.label-schema.schema-version", "org.label-schema.name", "org.label-schema.license", "org.label-schema.description", "org.label-schema.build-date", "org.label-schema", "org", "com.vmware.cp.artifact.flavor", "com.vmware.cp.artifact", "io.buildah.version", "io.k8s.description", "io.k8s.display-name", "io.openshift.expose-services", "io.openshift.tags", "vendor", "version", "description", "summary", "distribution-scope", "maintainer", "url", "vcs-ref", "vcs-type", "com", "com.redhat", "com.redhat.component", "com.redhat.license_terms"] [](#__codelineno-217-21)   #tls_ca = "/etc/telegraf/certs/server_ca.pem" [](#__codelineno-217-22)   #tls_cert = "/etc/telegraf/certs/server.pem" [](#__codelineno-217-23)   #tls_key = "/etc/telegraf/certs/server.key" [](#__codelineno-217-24)   #insecure_skip_verify = true [](#__codelineno-217-25)   tags = {category = "docker_metrics"} [](#__codelineno-217-26)   fieldexclude = ["container_id"] [](#__codelineno-217-27) [](#__codelineno-217-28) EOF`

**Configure Telegraf to send Metrics to RDAF Kafka:**

Configure the Telegraf to post the metrics to RDAF Platform's Kafka cluster by creating and configuring the below configuration file `kafka_out.conf`

`[](#__codelineno-218-1) cd /opt/rdaf_telegraf/conf.d [](#__codelineno-218-2) [](#__codelineno-218-3) cat > kafka_output.conf <<EOF [](#__codelineno-218-4) [](#__codelineno-218-5) # Host OS Metrics [](#__codelineno-218-6) [[outputs.kafka]] [](#__codelineno-218-7) brokers = ["192.168.10.10:9093", "192.168.10.11:9093", 192.168.10.12:9093] [](#__codelineno-218-8) topic = "<rdaf_tenant_id>.external.host_os_metrics" [](#__codelineno-218-9) data_format = "json" [](#__codelineno-218-10) json_timestamp_units = "1ns" [](#__codelineno-218-11) json_timestamp_format = "2006-01-02T15:04:05.000000Z" [](#__codelineno-218-12) enable_tls = true [](#__codelineno-218-13) [](#__codelineno-218-14) # Copy from RDAF Platform CA Cert file @ /opt/rdaf/cert/ca/ca.pem [](#__codelineno-218-15) tls_ca = "/etc/telegraf/certs/rdaf_ca.pem" [](#__codelineno-218-16) [](#__codelineno-218-17) # Copy from RDAF Platform Server Cert file @ /opt/rdaf/cert/rdaf/rdaf.pem [](#__codelineno-218-18) tls_cert = "/etc/telegraf/certs/rdaf.pem" [](#__codelineno-218-19) [](#__codelineno-218-20) # Copy from RDAF Platform Server Cert Key file @ /opt/rdaf/cert/rdaf/rdaf.key [](#__codelineno-218-21) tls_key = "/etc/telegraf/certs/rdaf.key" [](#__codelineno-218-22) [](#__codelineno-218-23) insecure_skip_verify = true [](#__codelineno-218-24) sasl_username = "<username>" [](#__codelineno-218-25) sasl_password = "<password>" [](#__codelineno-218-26) sasl_mechanism = "SCRAM-SHA-256" [](#__codelineno-218-27) [](#__codelineno-218-28) [outputs.kafka.tagpass] [](#__codelineno-218-29) category = ["host_os_metrics"] [](#__codelineno-218-30) [](#__codelineno-218-31) ################################################################################ [](#__codelineno-218-32) [](#__codelineno-218-33) # Docker Metrics [](#__codelineno-218-34) [[outputs.kafka]] [](#__codelineno-218-35) brokers = ["192.168.10.10:9093", "192.168.10.11:9093", 192.168.10.12:9093] [](#__codelineno-218-36) topic = "<rdaf_tenant_id>.external.docker_metrics" [](#__codelineno-218-37) data_format = "json" [](#__codelineno-218-38) json_timestamp_units = "1ns" [](#__codelineno-218-39) json_timestamp_format = "2006-01-02T15:04:05.000000Z" [](#__codelineno-218-40) enable_tls = true [](#__codelineno-218-41) [](#__codelineno-218-42) # Copy from RDAF Platform CA Cert file @ /opt/rdaf/cert/ca/ca.pem [](#__codelineno-218-43) tls_ca = "/etc/telegraf/certs/rdaf_ca.pem" [](#__codelineno-218-44) [](#__codelineno-218-45) # Copy from RDAF Platform Server Cert file @ /opt/rdaf/cert/rdaf/rdaf.pem [](#__codelineno-218-46) tls_cert = "/etc/telegraf/certs/rdaf.pem" [](#__codelineno-218-47) [](#__codelineno-218-48) # Copy from RDAF Platform Server Cert Key file @ /opt/rdaf/cert/rdaf/rdaf.key [](#__codelineno-218-49) tls_key = "/etc/telegraf/certs/rdaf.key" [](#__codelineno-218-50) [](#__codelineno-218-51) insecure_skip_verify = true [](#__codelineno-218-52) sasl_username = "<username>" [](#__codelineno-218-53) sasl_password = "<password>" [](#__codelineno-218-54) sasl_mechanism = "SCRAM-SHA-256" [](#__codelineno-218-55) [](#__codelineno-218-56) [outputs.kafka.tagpass] [](#__codelineno-218-57) category = ["docker_metrics"] [](#__codelineno-218-58) [](#__codelineno-218-59) EOF`

Please update the above highlighted parameters by getting RDAF platform's Kafka service settings from `/opt/rdaf/rdaf.cfg` configuration file.

Below is the sample Kafka configuration settings from `/opt/rdaf/rdaf.cfg` configuration file.

`[](#__codelineno-219-1) ... [](#__codelineno-219-2) [kafka] [](#__codelineno-219-3) datadir = 192.168.121.84/kafka-logs+/kafka-controller [](#__codelineno-219-4) host = 192.168.121.84 [](#__codelineno-219-5) kraft_cluster_id = MzBlZjkwYTRkY2M0MTFlZW [](#__codelineno-219-6) external_user = 20da0f30ed3442e88a93d205e0fa6f36.external [](#__codelineno-219-7) external_password = dFFrRDRIcDlKRQ== [](#__codelineno-219-8) ...`

**host** is Kafka's IP address, please update **brokers** parameter with it.

**external\_user** is Kafka's username, please update **sasl\_username** parameter with it. The username also has RDAF platform's **tenant id**. In the above example, `20da0f30ed3442e88a93d205e0fa6f36` is the **tenant id**. Please update **topic** parameter with it as a prefix to the Kafka topic.

**external\_password** is Kafka's password, please update **sasl\_password** parameter with it.

Note

Kafka's password is in **base64 encoded** format, please run the below command to decode it. Below mentioned encoded format is for a reference only.

`[](#__codelineno-220-1) echo dFFrRDRIcDlKRQ== | base64 -d`

Run the below commands to start the **Telegraf agent** service.

`[](#__codelineno-221-1) cd /opt/rdaf_telegraf [](#__codelineno-221-2) [](#__codelineno-221-3) docker-compose -f telegraf-docker-compose.yml pull  [](#__codelineno-221-4) docker-compose -f telegraf-docker-compose.yml up -d`

Once Telegraf agent container service is up and running, please wait for 60 seconds run the below command.

``[](#__codelineno-222-1) HOST_IP=`hostname -I | awk '{print $1}'` [](#__codelineno-222-2) sed -i "s/host_ip = \"\"/host_ip = \"$HOST_IP\"/g" /opt/rdaf_telegraf/telegraf.conf``

Edit `/opt/rdaf_telegraf/telegraf.conf` file and update the below highlighted parameter to tag the monitored RDAF platform environment. These configured global tags will be included in all of the metric payload for analytics and reporting.

Also, comment out the last 3 highlighted lines as shown below.

`[](#__codelineno-223-1) [global_tags] [](#__codelineno-223-2) host_ip = "192.168.10.10" [](#__codelineno-223-3) deployment = "Production_AIOps" [](#__codelineno-223-4) [](#__codelineno-223-5) .... [](#__codelineno-223-6) #[[outputs.discard]] [](#__codelineno-223-7) #[outputs.discard.tagpass] [](#__codelineno-223-8) #category = ["host_os_metrics", "docker_metrics", "opensearch_metrics"]`

Restart the Telegraf agent container service.

`[](#__codelineno-224-1) docker ps -a | grep -i telegraf`

`[](#__codelineno-225-1) docker restart <telegraf_container_id>`

### ****7.3 Pstream settings****

Once the Telegraf agents are installed and configured to collect metrics, a **Pstream** must be created on the **target RDAF platform** to process and store the incoming data from both **Host OS and Docker container** metrics.

Log into RDAF platform to which the Metrics are ingested and go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Persistent Streams** --> Click on **Add**

**Create Pstream for Host OS Metrics:**

Create the Pstream for Host OS metrics using the below settings.

**Pstream Name:** host\_os\_metrics

`[](#__codelineno-226-1) { [](#__codelineno-226-2)     "retention_days": 7, [](#__codelineno-226-3)     "search_case_insensitive": true, [](#__codelineno-226-4)     "messaging_platform_settings": { [](#__codelineno-226-5)         "platform": "kafka-external", [](#__codelineno-226-6)         "kafka-params": { [](#__codelineno-226-7)             "topics": [ [](#__codelineno-226-8)                 "host_os_metrics" [](#__codelineno-226-9)             ], [](#__codelineno-226-10)             "auto.offset.reset": "latest", [](#__codelineno-226-11)             "consumer_poll_timeout": 1.0, [](#__codelineno-226-12)             "batch_max_size": 1000, [](#__codelineno-226-13)             "batch_max_time_seconds": 2 [](#__codelineno-226-14)         } [](#__codelineno-226-15)     }, [](#__codelineno-226-16)     "auto_expand": [ [](#__codelineno-226-17)         "tags", [](#__codelineno-226-18)         "fields" [](#__codelineno-226-19)     ], [](#__codelineno-226-20)     "_settings": { [](#__codelineno-226-21)         "number_of_shards": 3, [](#__codelineno-226-22)         "number_of_replicas": 1, [](#__codelineno-226-23)         "refresh_interval": "30s" [](#__codelineno-226-24)     } [](#__codelineno-226-25) }`

**Create Pstream for Docker Container Metrics:**

Create the Pstream for Docker container metrics using the below settings.

**Pstream Name:** docker\_metrics

`[](#__codelineno-227-1) { [](#__codelineno-227-2)     "retention_days": 7, [](#__codelineno-227-3)     "search_case_insensitive": true, [](#__codelineno-227-4)     "messaging_platform_settings": { [](#__codelineno-227-5)         "platform": "kafka-external", [](#__codelineno-227-6)         "kafka-params": { [](#__codelineno-227-7)             "topics": [ [](#__codelineno-227-8)                 "docker_metrics" [](#__codelineno-227-9)             ], [](#__codelineno-227-10)             "auto.offset.reset": "latest", [](#__codelineno-227-11)             "consumer_poll_timeout": 1.0, [](#__codelineno-227-12)             "batch_max_size": 1000, [](#__codelineno-227-13)             "batch_max_time_seconds": 2 [](#__codelineno-227-14)         } [](#__codelineno-227-15)     }, [](#__codelineno-227-16)     "auto_expand": [ [](#__codelineno-227-17)         "tags", [](#__codelineno-227-18)         "fields" [](#__codelineno-227-19)     ], [](#__codelineno-227-20)     "_settings": { [](#__codelineno-227-21)         "number_of_shards": 3, [](#__codelineno-227-22)         "number_of_replicas": 1, [](#__codelineno-227-23)         "refresh_interval": "30s" [](#__codelineno-227-24)     } [](#__codelineno-227-25) }`

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!