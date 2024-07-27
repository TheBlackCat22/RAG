 



Guide to Application Dependency Mapping using RDA Bots
======================================================

This guide has following sections:

1.  **[Application Dependency Mapping (ADM) concept in RDA Fabric](#section_1)
    **
2.  **[Application Dependency Mapping (ADM) artifacts in RDA Fabric](#section_2)
    **
3.  **[Creating Nodes & Edges pstream for an ADM topology stack in RDA Fabric](#section_3)
    **
4.  **[Ingesting Nodes data for an ADM topology stack in RDA Fabric](#section_4)
    **
5.  **[Ingesting Edges data for an ADM topology stack in RDA Fabric](#section_5)
    **
6.  **[Generating an ADM topology stack in RDA Fabric](#section_6)
    **

1\. Application Dependency Mapping concept in RDA
-------------------------------------------------

Application Dependency Mappings (ADM) are essential for implementation of any Observability and AIOps projects. RDA provides necessary bots to automatically create & manage ADMs from any Cloud Native, Traditional Datacenter and Hybrid Cloud infrastructure.

RDA uses [Stacks](/beginners_guide/data_at_rest/#3-application-dependency-mappings-stacks)
 artifact as a way to refer to Application Dependency Mappings. Using Stacks, following can be accomplished:

*   Automatically identify impacted entities when an alert is detected (Impact Analysis)
*   Root cause identification
*   Identify cohorts (Similar entities in a business application): Critical for doing metric & event correlation.

Application dependency mapping in RDA is established using LRID (left to right impact declaration) model. Within the LRID model, each object is identified as either impacting node (left) or impacted node (right).

The direction of the impact is from left node to right node, i.e. node(s) listed under **Left node** impacts the node(s) listed under **Right node**. Below table provides a sample example of LRID model. **Relation Type** defines how **Left node** is related to **Right node**.

| Left node | Right node | Relation Type |
| --- | --- | --- |
| web01 | bizapp\_ecommerce | member-of |
| app01 | web01 | depended-by |
| dbhost01 | app01 | depended-by |
| esxihost01 | vm01 | runs |
| datastore01 | vm01 | contains |
| lun01 | datastore01 | depended-by |
| storage\_controller01 | lun01 | contains |

In the above example of application dependency mapping for a Business application called **bizapp\_ecommerce**, it's underlying resource objects are defined as either **Left node** or **Right node** based on how they impact their neighbouring nodes and subsequently the upstream Business application.

What is a node ? - A node is an application or infrastructure component such as Web server, App server, Database, Virtual Machine, Switch, Server, Storage, Volume etc. which are connected to each other within the ADM stack.

![ADM](https://bot-docs.cloudfabrix.io/images/guide/cfx_adm.png)

2\. Application Dependency Mapping artifacts in RDA
---------------------------------------------------

In order to generate an application dependency mapping (ADM) topology as depicted in the above picture, below are two types of datasets that need to be generated.

*   **Nodes pstream:** Nodes pstream consists of the properties of each node (such as application component, vm, server, switch, storage volume etc.) within the ADM topology. Additional to selecting each node's important properties such as name, ip address, uuid, mac address, version etc., below are the mandatory properties that need to be defined for each node:
    
    *   **layer:** Supported values are application, application component, virtualization, compute, network, storage
    *   **node\_id:** Unique identifier of a node within the ADM topology
    *   **node\_type:** Supported values are application, Webserver, Appserver, Database, Infraservice, Container, Process, Service, VM, OS, Host, Server, Switch, Router, Firewall, Load Balancer, LUN, Volume, Storage Pool, Storage Controller
    *   **node\_label:** User friendly label name for each node within the ADM topology
*   **Edges pstream:** In edges pstream, each node is classified either as left node or right node using it's **node\_id** that was defined in the above nodes pstream. Below are the properties that need to be defined within the edges pstream.
    
    *   **left\_id:** `node_id` of a node which is an impacting node
    *   **right\_id:** `node_id` of a node which is an impacted node
    *   **left\_label:** `node_label` of a node which is an impacting node
    *   **right\_label:** `node_label` of a node which is an impacted node
    *   **left\_node\_type:** `node_type` of a node which is an impacting node
    *   **right\_node\_type:** `node_type` of a node which is an impacted node
    *   **relation\_type:** It defines how **Left node** is related to **Right node**. Below are some of the supported relation types, but not limited to
        *   runs
        *   runs-on
        *   connects
        *   connected-to
        *   member-of
        *   contains
        *   depended-by

3\. Creating Nodes & Edges pstream for an ADM topology stack in RDA Fabric
--------------------------------------------------------------------------

Login into RDAF UI portal and go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Persistent Streams**

**Add Nodes Pstream:**

Click on **Add** button to create a new **persistent stream**

Select **Datastore** type and Enter **persistent stream** name.

Enter the **persistent stream name** as `demo_topology_nodes_stream`

Enter the below given configuration settings and click on **Save** button

`[](#__codelineno-0-1) { [](#__codelineno-0-2)     "unique_keys": [ [](#__codelineno-0-3)         "node_id" [](#__codelineno-0-4)     ], [](#__codelineno-0-5)     "default_values": { [](#__codelineno-0-6)         "iconURL": "Not Available" [](#__codelineno-0-7)     }, [](#__codelineno-0-8)     "search_case_insensitive": true, [](#__codelineno-0-9)     "_settings": { [](#__codelineno-0-10)         "number_of_shards": 3, [](#__codelineno-0-11)         "number_of_replicas": 1, [](#__codelineno-0-12)         "refresh_interval": "1s" [](#__codelineno-0-13)     } [](#__codelineno-0-14) }`

**Add Edges Pstream:**

Click on **Add** button to create a new **persistent stream**

Select **Datastore** type and Enter **persistent stream** name.

Enter the **persistent stream name** as `demo_topology_edges_stream`

Enter the below given configuration settings and click on **Save** button

`[](#__codelineno-1-1) { [](#__codelineno-1-2)     "unique_keys": [ [](#__codelineno-1-3)         "left_id", [](#__codelineno-1-4)         "right_id" [](#__codelineno-1-5)     ], [](#__codelineno-1-6)     "search_case_insensitive": true, [](#__codelineno-1-7)     "_settings": { [](#__codelineno-1-8)         "number_of_shards": 3, [](#__codelineno-1-9)         "number_of_replicas": 1, [](#__codelineno-1-10)         "refresh_interval": "1s" [](#__codelineno-1-11)     } [](#__codelineno-1-12) }`

4\. Ingesting Nodes data for an ADM topology stack in RDA Fabric
----------------------------------------------------------------

Login into RDAF UI portal and go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Pipelines**

Click on **Add with Text** button to create a new **Topology Nodes Pipeline**

Enter **Pipeline Name** as `demo_topology_nodes_pipeline`

Enter **Version** as `01`

Enter the **Pipeline Content** (please see below)

Click on **Save** to save the pipeline

Click on **demo\_topology\_nodes\_pipeline** settings (3 dot button) and click on **Run** button from the menu to execute the pipeline.

After submitting the pipeline job, Click on **demo\_topology\_nodes\_pipeline** settings (3 dot button) and click on **View Traces** to see the progress of the pipeline.

Below one is a sample pipeline that ingests Nodes data into **Nodes pstream** using 2 tier application stack's sample data.

Info

When any of the **node\_id** field or any other field which is going to be used as **left\_id** or **right\_id** and if it has has numeric value, please make sure to set it's data type as **String** using the below bot.

|     |     |
| --- | --- |
| [1](#__codelineno-2-1) | `--> @dm:to-type columns = 'node_id' & type = 'str'` |

|     |     |
| --- | --- |
| [1](#__codelineno-3-1)<br>  [2](#__codelineno-3-2)<br>  [3](#__codelineno-3-3)<br>  [4](#__codelineno-3-4)<br>  [5](#__codelineno-3-5)<br>  [6](#__codelineno-3-6)<br>  [7](#__codelineno-3-7)<br>  [8](#__codelineno-3-8)<br>  [9](#__codelineno-3-9)<br> [10](#__codelineno-3-10)<br> [11](#__codelineno-3-11)<br> [12](#__codelineno-3-12)<br> [13](#__codelineno-3-13)<br> [14](#__codelineno-3-14)<br> [15](#__codelineno-3-15)<br> [16](#__codelineno-3-16)<br> [17](#__codelineno-3-17)<br> [18](#__codelineno-3-18)<br> [19](#__codelineno-3-19)<br> [20](#__codelineno-3-20)<br> [21](#__codelineno-3-21)<br> [22](#__codelineno-3-22)<br> [23](#__codelineno-3-23)<br> [24](#__codelineno-3-24)<br> [25](#__codelineno-3-25)<br> [26](#__codelineno-3-26)<br> [27](#__codelineno-3-27)<br> [28](#__codelineno-3-28)<br> [29](#__codelineno-3-29)<br> [30](#__codelineno-3-30)<br> [31](#__codelineno-3-31)<br> [32](#__codelineno-3-32)<br> [33](#__codelineno-3-33)<br> [34](#__codelineno-3-34)<br> [35](#__codelineno-3-35)<br> [36](#__codelineno-3-36)<br> [37](#__codelineno-3-37)<br> [38](#__codelineno-3-38)<br> [39](#__codelineno-3-39)<br> [40](#__codelineno-3-40)<br> [41](#__codelineno-3-41)<br> [42](#__codelineno-3-42)<br> [43](#__codelineno-3-43)<br> [44](#__codelineno-3-44)<br> [45](#__codelineno-3-45)<br> [46](#__codelineno-3-46)<br> [47](#__codelineno-3-47)<br> [48](#__codelineno-3-48)<br> [49](#__codelineno-3-49)<br> [50](#__codelineno-3-50)<br> [51](#__codelineno-3-51)<br> [52](#__codelineno-3-52)<br> [53](#__codelineno-3-53)<br> [54](#__codelineno-3-54)<br> [55](#__codelineno-3-55)<br> [56](#__codelineno-3-56)<br> [57](#__codelineno-3-57)<br> [58](#__codelineno-3-58)<br> [59](#__codelineno-3-59)<br> [60](#__codelineno-3-60)<br> [61](#__codelineno-3-61)<br> [62](#__codelineno-3-62)<br> [63](#__codelineno-3-63)<br> [64](#__codelineno-3-64)<br> [65](#__codelineno-3-65)<br> [66](#__codelineno-3-66)<br> [67](#__codelineno-3-67)<br> [68](#__codelineno-3-68)<br> [69](#__codelineno-3-69)<br> [70](#__codelineno-3-70)<br> [71](#__codelineno-3-71)<br> [72](#__codelineno-3-72)<br> [73](#__codelineno-3-73)<br> [74](#__codelineno-3-74)<br> [75](#__codelineno-3-75)<br> [76](#__codelineno-3-76)<br> [77](#__codelineno-3-77)<br> [78](#__codelineno-3-78)<br> [79](#__codelineno-3-79)<br> [80](#__codelineno-3-80)<br> [81](#__codelineno-3-81)<br> [82](#__codelineno-3-82)<br> [83](#__codelineno-3-83)<br> [84](#__codelineno-3-84)<br> [85](#__codelineno-3-85)<br> [86](#__codelineno-3-86)<br> [87](#__codelineno-3-87)<br> [88](#__codelineno-3-88)<br> [89](#__codelineno-3-89)<br> [90](#__codelineno-3-90)<br> [91](#__codelineno-3-91)<br> [92](#__codelineno-3-92)<br> [93](#__codelineno-3-93)<br> [94](#__codelineno-3-94)<br> [95](#__codelineno-3-95)<br> [96](#__codelineno-3-96)<br> [97](#__codelineno-3-97)<br> [98](#__codelineno-3-98)<br> [99](#__codelineno-3-99)<br>[100](#__codelineno-3-100)<br>[101](#__codelineno-3-101)<br>[102](#__codelineno-3-102)<br>[103](#__codelineno-3-103)<br>[104](#__codelineno-3-104)<br>[105](#__codelineno-3-105)<br>[106](#__codelineno-3-106)<br>[107](#__codelineno-3-107)<br>[108](#__codelineno-3-108)<br>[109](#__codelineno-3-109)<br>[110](#__codelineno-3-110)<br>[111](#__codelineno-3-111)<br>[112](#__codelineno-3-112)<br>[113](#__codelineno-3-113)<br>[114](#__codelineno-3-114)<br>[115](#__codelineno-3-115)<br>[116](#__codelineno-3-116)<br>[117](#__codelineno-3-117)<br>[118](#__codelineno-3-118)<br>[119](#__codelineno-3-119)<br>[120](#__codelineno-3-120)<br>[121](#__codelineno-3-121)<br>[122](#__codelineno-3-122)<br>[123](#__codelineno-3-123)<br>[124](#__codelineno-3-124)<br>[125](#__codelineno-3-125)<br>[126](#__codelineno-3-126)<br>[127](#__codelineno-3-127)<br>[128](#__codelineno-3-128)<br>[129](#__codelineno-3-129)<br>[130](#__codelineno-3-130)<br>[131](#__codelineno-3-131)<br>[132](#__codelineno-3-132)<br>[133](#__codelineno-3-133)<br>[134](#__codelineno-3-134)<br>[135](#__codelineno-3-135)<br>[136](#__codelineno-3-136)<br>[137](#__codelineno-3-137)<br>[138](#__codelineno-3-138)<br>[139](#__codelineno-3-139)<br>[140](#__codelineno-3-140)<br>[141](#__codelineno-3-141)<br>[142](#__codelineno-3-142)<br>[143](#__codelineno-3-143)<br>[144](#__codelineno-3-144)<br>[145](#__codelineno-3-145)<br>[146](#__codelineno-3-146)<br>[147](#__codelineno-3-147)<br>[148](#__codelineno-3-148)<br>[149](#__codelineno-3-149)<br>[150](#__codelineno-3-150)<br>[151](#__codelineno-3-151)<br>[152](#__codelineno-3-152)<br>[153](#__codelineno-3-153)<br>[154](#__codelineno-3-154)<br>[155](#__codelineno-3-155)<br>[156](#__codelineno-3-156)<br>[157](#__codelineno-3-157)<br>[158](#__codelineno-3-158)<br>[159](#__codelineno-3-159)<br>[160](#__codelineno-3-160)<br>[161](#__codelineno-3-161)<br>[162](#__codelineno-3-162)<br>[163](#__codelineno-3-163)<br>[164](#__codelineno-3-164)<br>[165](#__codelineno-3-165)<br>[166](#__codelineno-3-166)<br>[167](#__codelineno-3-167)<br>[168](#__codelineno-3-168)<br>[169](#__codelineno-3-169)<br>[170](#__codelineno-3-170)<br>[171](#__codelineno-3-171)<br>[172](#__codelineno-3-172)<br>[173](#__codelineno-3-173)<br>[174](#__codelineno-3-174)<br>[175](#__codelineno-3-175)<br>[176](#__codelineno-3-176)<br>[177](#__codelineno-3-177)<br>[178](#__codelineno-3-178)<br>[179](#__codelineno-3-179)<br>[180](#__codelineno-3-180)<br>[181](#__codelineno-3-181)<br>[182](#__codelineno-3-182)<br>[183](#__codelineno-3-183)<br>[184](#__codelineno-3-184)<br>[185](#__codelineno-3-185)<br>[186](#__codelineno-3-186)<br>[187](#__codelineno-3-187)<br>[188](#__codelineno-3-188)<br>[189](#__codelineno-3-189)<br>[190](#__codelineno-3-190)<br>[191](#__codelineno-3-191)<br>[192](#__codelineno-3-192)<br>[193](#__codelineno-3-193)<br>[194](#__codelineno-3-194)<br>[195](#__codelineno-3-195)<br>[196](#__codelineno-3-196)<br>[197](#__codelineno-3-197)<br>[198](#__codelineno-3-198)<br>[199](#__codelineno-3-199)<br>[200](#__codelineno-3-200)<br>[201](#__codelineno-3-201)<br>[202](#__codelineno-3-202)<br>[203](#__codelineno-3-203)<br>[204](#__codelineno-3-204)<br>[205](#__codelineno-3-205)<br>[206](#__codelineno-3-206)<br>[207](#__codelineno-3-207)<br>[208](#__codelineno-3-208)<br>[209](#__codelineno-3-209)<br>[210](#__codelineno-3-210)<br>[211](#__codelineno-3-211)<br>[212](#__codelineno-3-212)<br>[213](#__codelineno-3-213)<br>[214](#__codelineno-3-214)<br>[215](#__codelineno-3-215)<br>[216](#__codelineno-3-216)<br>[217](#__codelineno-3-217)<br>[218](#__codelineno-3-218)<br>[219](#__codelineno-3-219)<br>[220](#__codelineno-3-220)<br>[221](#__codelineno-3-221)<br>[222](#__codelineno-3-222)<br>[223](#__codelineno-3-223)<br>[224](#__codelineno-3-224)<br>[225](#__codelineno-3-225)<br>[226](#__codelineno-3-226)<br>[227](#__codelineno-3-227)<br>[228](#__codelineno-3-228)<br>[229](#__codelineno-3-229)<br>[230](#__codelineno-3-230)<br>[231](#__codelineno-3-231)<br>[232](#__codelineno-3-232)<br>[233](#__codelineno-3-233)<br>[234](#__codelineno-3-234)<br>[235](#__codelineno-3-235)<br>[236](#__codelineno-3-236)<br>[237](#__codelineno-3-237)<br>[238](#__codelineno-3-238)<br>[239](#__codelineno-3-239)<br>[240](#__codelineno-3-240) | `## A Sample RDA pipeline to create ADM nodes and writes into Nodes pstream using the demo data ## The Demo data was generated from an APM tool which has the inventory data of one or more Business applications, ## Web/App services, Database services etc. ## Step-1: ## Load the business application dataset and define each business application node's properties. ## Start a new block in the pipeline @c:new-block     ## Load the demo business application dataset     --> @files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_biz_application_dataset.csv'     ## Filter stale applications if there are any     --> *dm:filter app_name does not contain 'Petclinic'     ## Add a new field called 'layer' and define it as 'Application'     --> @dm:eval             layer = "'Application'"     ## Add a new field called 'node_type' and define it as 'Application'     --> @dm:eval             node_type = "'Application'"     ## Clone the field 'app_name' to 'node_label'     --> @dm:map             from = 'app_name' & to = 'node_label'     ## Clone the field 'app_id' to 'node_id'     --> @dm:map             from = 'app_id' & to = 'node_id'     ## Set the app_id & node_id columns / field's data type as String     --> @dm:to-type columns = 'app_id,node_id' & type = 'str'     ## Save the business application nodes data as a temporary in-memory dataset for further use within this pipeline     --> @dm:save             name = 'temp-biz_application_nodes'     ## Write to Topology Nodes Pstream     --> @rn:write-stream name = 'demo_topology_nodes_stream' ## Step-2: ## Load the database services dataset and define each database service's node properties. ## Start a new block in the pipeline --> @c:new-block     ## Load the demo database service connections dataset     --> @files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_apps_to_db_conn_dataset.csv'     ## Filter the records from 'exitPointType' field if it contains DB and JDBC values, remove any stale application connections and get the required fields     --> *dm:filter             exitPointType contains 'DB\|JDBC' &             app_name does not contain 'Petclinic'             get HOST,app_name     ## Remove the duplicate records using HOST field     --> @dm:dedup             columns = 'HOST'     ## Save the database service connections data as a temporary in-memory dataset for further use within this pipeline     --> @dm:save             name = 'temp-db_backend_connections' ## Start a new block in the pipeline --> @c:new-block     ## Load the demo database servers dataset     --> @files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_db_server_nodes_dataset.csv'     ## Filter the records that contain any stale DB services and get the required fields and rename them     --> *dm:filter name does not contain 'linux-petclinic-db01'             get host as 'db_dns_name',ipAddress as 'db_ip_address',name as 'db_hostname',id as 'db_id'     ## Set the db_id column / field's data type as String     --> @dm:to-type columns = 'db_id' & type = 'str'     ## Remove the duplicate records using db_ip_address field     --> @dm:dedup             columns = 'db_ip_address'     ## Save the database servers data as a temporary in-memory dataset for further use within this pipeline     --> @dm:save             name = 'temp-db_servers' ## Start a new block in the pipeline --> @c:new-block     ## Reload the saved in-memory dataset 'temp-db_servers'     --> @dm:recall             name = 'temp-db_servers'     ## Enrich the DB server dataset with DB service connections dataset and add the app_name field     --> @dm:enrich             dict = 'temp-db_backend_connections' &             src_key_cols = 'db_ip_address' &             dict_key_cols = 'HOST' &             enrich_cols = 'app_name'     ## Remove/Exclude a field called HOST     --> @dm:selectcolumns             exclude = '^HOST$'     ## Add a new field called 'layer' and define it as 'Application Component'     --> @dm:eval             layer = "'Application Component'"     ## Add a new field called 'node_type' and define it as 'Database'     --> @dm:eval             node_type = "'Database'"     ## Rename the field 'db_id' as 'node_id'     --> @dm:rename-columns             node_id = 'db_id'     ## Derive database node's 'node_label' field from other fields 'db_hostname' & 'node_type'     --> @dm:map             from = 'db_hostname' &             to = 'node_label'     ## Enrich the database node's dataset with business application's node_id     --> @dm:enrich             dict = 'temp-biz_application_nodes' &             src_key_cols = 'app_name' &             dict_key_cols = 'app_name' &             enrich_cols = 'app_id' &             enrich_cols_as = 'biz_app_id'     ## Set the biz_app_id column / field's data type as String     --> @dm:to-type columns = 'biz_app_id' & type = 'str'     ## Save the database nodes data as a temporary in-memory dataset for further use within this pipeline     --> @dm:save             name = 'temp-application_database_nodes'     ## Write to Topology Nodes Pstream     --> @rn:write-stream name = 'demo_topology_nodes_stream' ## Step-3: ## Load the applications (web/app server) dataset and define each application service's node properties. ## Start a new block in the pipeline --> @c:new-block     ## Load the demo applications (web/app server) dataset     --> @files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_application_nodes_dataset.csv'     ## Filter the records from 'ipAddress' field if it has a special character and a private IP address,     ## remove any stale application services and get few required fields and rename them     --> *dm:filter             ipAddress does not contain ':' &             ipAddress does not contain '172.17.0.1' &             ipAddress does not contain '192.168.115' &             app_name does not contain 'Petclinic'             get name as 'app_hostname',             tierName as 'app_tier',             ipAddress as 'app_ip_address',             app_name as 'app_web_name',             id as 'app_web_id'     ## Set the app_web_id column / field's data type as String     --> @dm:to-type columns = 'app_web_id' & type = 'str'     ## Filter the application nodes that are Web server applications     --> *dm:filter             app_tier = 'Web'     ## Add a new field called 'layer' and define it as 'Application Component'     --> @dm:eval             layer = "'Application Component'"     ## Add a new field called 'node_type' and define it as 'Webserver'     --> @dm:eval             node_type = "'Webserver'"     ## Rename the field 'app_id' as 'node_id'     --> @dm:rename-columns             node_id = 'app_web_id'     ## Derive application service's 'node_label' field from other fields 'app_name' & 'node_type'     --> @dm:map             from = 'app_web_name,node_type' &             to = 'node_label' &             func = 'join' &             sep = '_'     ## Enrich the application service node's dataset with business application's node_id     --> @dm:enrich             dict = 'temp-biz_application_nodes' &             src_key_cols = 'app_web_name' &             dict_key_cols = 'app_name' &             enrich_cols = 'app_id' &             enrich_cols_as = 'biz_app_id'     ## Rename the app_name field     --> @dm:rename-columns biz_app_name = 'app_name'     ## Set the biz_app_id column / field's data type as String     --> @dm:to-type columns = 'biz_app_id' & type = 'str'     ## Remove/Exclude a field called app_name & app_web_name     --> @dm:selectcolumns             exclude = '^app_name$\|^app_web_name$'     ## Enrich the application service node's dataset with database service's node_id and DB Hostname     --> @dm:enrich             dict = 'temp-application_database_nodes' &             src_key_cols = 'biz_app_id' &             dict_key_cols = 'biz_app_id' &             enrich_cols = 'node_id,db_hostname' &             enrich_cols_as = 'db_node_id,db_hostname'     ## Set the db_node_id column / field's data type as String     --> @dm:to-type columns = 'db_node_id' & type = 'str'     ## Save the application web/app service nodes data as a temporary in-memory dataset for further use within this pipeline     --> @dm:save             name = 'temp-application_web_service_nodes'     ## Write to Topology Nodes Pstream     --> @rn:write-stream name = 'demo_topology_nodes_stream' ## Step-4: ## Concatenate all of the nodes of Business application, Web/App services and Database services ## Start a new block in the pipeline --> @c:new-block     ## Use the below bot to combine all of node datasets that were created above     --> @dm:concat names = '^temp-biz_application_nodes$\|^temp-application_database_nodes$\|^temp-application_web_service_nodes$'     ## Set the node_id column / field's data type as String     --> @dm:to-type columns = 'node_id' & type = 'str'     ## Save the combined nodes as ADM nodes dataset     --> @dm:save name = 'rda_adm_biz_app_db_nodes_databaset'` |

5\. Ingesting Edges data for an ADM topology stack in RDA Fabric
----------------------------------------------------------------

Login into RDAF UI portal and go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Pipelines**

Click on **Add with Text** button to create a new **Topology Edges Pipeline**

Enter **Pipeline Name** as `demo_topology_edges_pipeline`

Enter **Version** as `01`

Enter the **Pipeline Content** (please see below)

Click on **Save** to save the pipeline

Click on **demo\_topology\_edges\_pipeline** settings (3 dot button) and click on **Run** button from the menu to execute the pipeline.

After submitting the pipeline job, Click on **demo\_topology\_edges\_pipeline** settings (3 dot button) and click on **View Traces** to see the progress of the pipeline.

Below one is a sample pipeline that ingests Nodes data into **Nodes pstream** using 2 tier application stack's sample data.

Below one is a sample pipeline that ingests Edges data into **Edges pstream** using 2 tier application stack's sample data.

|     |     |
| --- | --- |
| [1](#__codelineno-4-1)<br>  [2](#__codelineno-4-2)<br>  [3](#__codelineno-4-3)<br>  [4](#__codelineno-4-4)<br>  [5](#__codelineno-4-5)<br>  [6](#__codelineno-4-6)<br>  [7](#__codelineno-4-7)<br>  [8](#__codelineno-4-8)<br>  [9](#__codelineno-4-9)<br> [10](#__codelineno-4-10)<br> [11](#__codelineno-4-11)<br> [12](#__codelineno-4-12)<br> [13](#__codelineno-4-13)<br> [14](#__codelineno-4-14)<br> [15](#__codelineno-4-15)<br> [16](#__codelineno-4-16)<br> [17](#__codelineno-4-17)<br> [18](#__codelineno-4-18)<br> [19](#__codelineno-4-19)<br> [20](#__codelineno-4-20)<br> [21](#__codelineno-4-21)<br> [22](#__codelineno-4-22)<br> [23](#__codelineno-4-23)<br> [24](#__codelineno-4-24)<br> [25](#__codelineno-4-25)<br> [26](#__codelineno-4-26)<br> [27](#__codelineno-4-27)<br> [28](#__codelineno-4-28)<br> [29](#__codelineno-4-29)<br> [30](#__codelineno-4-30)<br> [31](#__codelineno-4-31)<br> [32](#__codelineno-4-32)<br> [33](#__codelineno-4-33)<br> [34](#__codelineno-4-34)<br> [35](#__codelineno-4-35)<br> [36](#__codelineno-4-36)<br> [37](#__codelineno-4-37)<br> [38](#__codelineno-4-38)<br> [39](#__codelineno-4-39)<br> [40](#__codelineno-4-40)<br> [41](#__codelineno-4-41)<br> [42](#__codelineno-4-42)<br> [43](#__codelineno-4-43)<br> [44](#__codelineno-4-44)<br> [45](#__codelineno-4-45)<br> [46](#__codelineno-4-46)<br> [47](#__codelineno-4-47)<br> [48](#__codelineno-4-48)<br> [49](#__codelineno-4-49)<br> [50](#__codelineno-4-50)<br> [51](#__codelineno-4-51)<br> [52](#__codelineno-4-52)<br> [53](#__codelineno-4-53)<br> [54](#__codelineno-4-54)<br> [55](#__codelineno-4-55)<br> [56](#__codelineno-4-56)<br> [57](#__codelineno-4-57)<br> [58](#__codelineno-4-58)<br> [59](#__codelineno-4-59)<br> [60](#__codelineno-4-60)<br> [61](#__codelineno-4-61)<br> [62](#__codelineno-4-62)<br> [63](#__codelineno-4-63)<br> [64](#__codelineno-4-64)<br> [65](#__codelineno-4-65)<br> [66](#__codelineno-4-66)<br> [67](#__codelineno-4-67)<br> [68](#__codelineno-4-68)<br> [69](#__codelineno-4-69)<br> [70](#__codelineno-4-70)<br> [71](#__codelineno-4-71)<br> [72](#__codelineno-4-72)<br> [73](#__codelineno-4-73)<br> [74](#__codelineno-4-74)<br> [75](#__codelineno-4-75)<br> [76](#__codelineno-4-76)<br> [77](#__codelineno-4-77)<br> [78](#__codelineno-4-78)<br> [79](#__codelineno-4-79)<br> [80](#__codelineno-4-80)<br> [81](#__codelineno-4-81)<br> [82](#__codelineno-4-82)<br> [83](#__codelineno-4-83)<br> [84](#__codelineno-4-84)<br> [85](#__codelineno-4-85)<br> [86](#__codelineno-4-86)<br> [87](#__codelineno-4-87)<br> [88](#__codelineno-4-88)<br> [89](#__codelineno-4-89)<br> [90](#__codelineno-4-90)<br> [91](#__codelineno-4-91)<br> [92](#__codelineno-4-92)<br> [93](#__codelineno-4-93)<br> [94](#__codelineno-4-94)<br> [95](#__codelineno-4-95)<br> [96](#__codelineno-4-96)<br> [97](#__codelineno-4-97)<br> [98](#__codelineno-4-98)<br> [99](#__codelineno-4-99)<br>[100](#__codelineno-4-100)<br>[101](#__codelineno-4-101)<br>[102](#__codelineno-4-102)<br>[103](#__codelineno-4-103)<br>[104](#__codelineno-4-104)<br>[105](#__codelineno-4-105)<br>[106](#__codelineno-4-106)<br>[107](#__codelineno-4-107)<br>[108](#__codelineno-4-108)<br>[109](#__codelineno-4-109)<br>[110](#__codelineno-4-110)<br>[111](#__codelineno-4-111)<br>[112](#__codelineno-4-112)<br>[113](#__codelineno-4-113)<br>[114](#__codelineno-4-114)<br>[115](#__codelineno-4-115)<br>[116](#__codelineno-4-116)<br>[117](#__codelineno-4-117)<br>[118](#__codelineno-4-118)<br>[119](#__codelineno-4-119)<br>[120](#__codelineno-4-120)<br>[121](#__codelineno-4-121)<br>[122](#__codelineno-4-122)<br>[123](#__codelineno-4-123)<br>[124](#__codelineno-4-124)<br>[125](#__codelineno-4-125)<br>[126](#__codelineno-4-126)<br>[127](#__codelineno-4-127)<br>[128](#__codelineno-4-128) | `## A Sample RDA pipeline to create ADM edges and writes into Edges pstream using the demo data ## The Demo data was generated from an APM tool which has the inventory data of one or more Business applications, ## Web/App services, Database services etc. ## 'Nodes pstream' that was generated will be used as input for populating the 'Edges pstream' ## Step-1: ## Load the 'Nodes dataset' and establish relationship between Web/App, DB and Biz application nodes ## Start a new block in the pipeline --> @c:new-block     ## Reload the 'Nodes dataset'     --> @dm:recall              name = 'rda_adm_biz_app_db_nodes_databaset'     ## Define relationship between Web/App and Biz application nodes     ## Here, Web/App node is going to be classified as impacting node (Left node) and      ## Biz application node is going to be classified as impacted node (Right node)     ## Filter the Web/App nodes     --> *dm:filter node_type = 'Webserver'             get node_id as 'left_id',             node_label as 'left_label',             node_type as 'left_node_type',             biz_app_id as 'right_id',             biz_app_name as 'right_label'     ## Define right_node_type field     --> @dm:eval right_node_type = "'Application'"     ## Add relationship type between Web/App and Biz application nodes     --> @dm:eval              relation_type = "'member-of'"     ## Save it as in-memory dataset for further use with in the pipeline     --> @dm:save             name = 'temp-web_biz_app_relationship'     ## Define relationship between Database and Biz application nodes     ## Here, Database node is going to be classified as impacting node (Left node) and      ## Biz application node is going to be classified as impacted node (Right node)     ## Reload the 'Nodes dataset'     --> @dm:recall              name = 'rda_adm_biz_app_db_nodes_databaset'     ## Filter the Database nodes     --> *dm:filter node_type = 'Database'             get node_id as 'left_id',             node_label as 'left_label',             node_type as 'left_node_type',             biz_app_id as 'right_id',             app_name as 'right_label'     ## Define right_node_type field     --> @dm:eval right_node_type = "'Application'"     ## Add relationship type between Database and Biz application nodes     --> @dm:eval              relation_type = "'member-of'"     ## Save it as in-memory dataset for further use with in the pipeline     --> @dm:save             name = 'temp-db_biz_app_relationship'     ## Define relationship between Web/App and Database nodes     ## Here, Database node is going to be classified as impacting node (Left node) and      ## Web/App node is going to be classified as impacted node (Right node)     ## Reload the 'Nodes dataset'     --> @dm:recall              name = 'rda_adm_biz_app_db_nodes_databaset'     ## Filter the Database nodes     --> *dm:filter node_type = 'Webserver'             get node_id as 'right_id',             node_label as 'right_label',             node_type as 'right_node_type',             db_node_id as 'left_id',             db_hostname as 'left_label'     ## Define left_node_type field     --> @dm:eval left_node_type = "'Database'"     ## Add relationship type between Database and Biz application nodes     --> @dm:eval              relation_type = "'connected-by'"     ## Save it as in-memory dataset for further use with in the pipeline     --> @dm:save             name = 'temp-webapp_db_relationship' ## Step-2: ## Concatenate all of the Edge (relationships) datasets of Business application, Web/App services and Database services ## Start a new block in the pipeline --> @c:new-block     ## Use the below bot to combine all of edge (relationships) datasets that were created above     --> @dm:concat names = '^temp-web_biz_app_relationship$\|^temp-db_biz_app_relationship$\|^temp-webapp_db_relationship$'     ## Set the lef_id,right_id columns / field's data type as String     --> @dm:to-type columns = 'left_id,right_id' & type = 'str'     ## Remove any trailing whitespaces for left_id     --> @dm:map attr = 'left_id' & func = 'strip'     ## Remove any trailing whitespaces for right_id     --> @dm:map attr = 'right_id' & func = 'strip'     ## Filter out if Left Node and Right Nodes are same     --> *dm:filter left_id != right_id     ## Filter out if Left Node's Label is empty     --> *dm:filter left_label is not empty     ## Filter out if Right Node's Label is empty     --> *dm:filter right_label is not empty     ## Remove Duplicate records of left_id & right_id together     --> @dm:dedup columns = 'left_id,right_id'     ## Filter selective fields and write to Topology Edges Pstream     --> *dm:filter * get left_label,left_id,left_node_type,relation_type,right_id,right_label,right_node_type     ## Write to Topology Edges Pstream     --> @rn:write-stream name = 'demo_topology_edges_stream'` |

5\. Generating an ADM topology stack in RDA Fabric
--------------------------------------------------

Login into RDAF UI portal and go to **Main Menu** --> **Configuration** --> **RDA Administration** --> **Stacks**

Click on **Add Stack** button to create a new **Topology Stack**

Enter the Stack Name as as **demo\_app\_topology**

Enter the Description as **Demo Application Topology**

Select the Stack Type as **Dynamic**

Enter the below configuration settings for the stack using **Nodes pstream** and **Edges pstream** and Click on **Save** button.

`[](#__codelineno-5-1) { [](#__codelineno-5-2)     "name": "demo_app_topology", [](#__codelineno-5-3)     "description": "Demo Application Topology", [](#__codelineno-5-4)     "saved_time": "2023-11-16T19:28:26.628904", [](#__codelineno-5-5)     "is_dynamic": true, [](#__codelineno-5-6)     "hierarchical": true, [](#__codelineno-5-7)     "dynamic_nodes": { [](#__codelineno-5-8)         "stream": "demo_topology_nodes_stream", [](#__codelineno-5-9)         "query": "timestamp is after -90d", [](#__codelineno-5-10)         "limit": 0, [](#__codelineno-5-11)         "sorting": null [](#__codelineno-5-12)     }, [](#__codelineno-5-13)     "dynamic_relationships": { [](#__codelineno-5-14)         "stream": "demo_topology_edges_stream", [](#__codelineno-5-15)         "query": "timestamp is after -90d", [](#__codelineno-5-16)         "limit": 0, [](#__codelineno-5-17)         "sorting": null [](#__codelineno-5-18)     } [](#__codelineno-5-19) }`

To see the final ADM topology stack, click on the **demo\_app\_topology** stack name which was created or click on the **View Topology** from the action buttons.

![ADM](https://bot-docs.cloudfabrix.io/images/guide/cfx_adm_sample_stack2.png)

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!