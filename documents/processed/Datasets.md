 



# Example Datasets

This page contains datasets that are used by some of the example pipelines. Data for these datasets can be accessed from an RDA pipeline using [@files:loadfile](/Bots/file/#loadfile)
 bot.

* * *

## Dataset: demo\_adm\_application\_nodes\_dataset

This Dataset has **9 Rows** and **16 Columns**

Download Data: [CSV Format](/data/datasets/demo_adm_application_nodes_dataset.csv)
 | [Parquet Format](/data/datasets/demo_adm_application_nodes_dataset.parquet)

View Data: [Table Format](/data/datasets/demo_adm_application_nodes_dataset.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_application_nodes_dataset.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_adm_application_nodes_dataset'`

[Pipeline](#__tabbed_1_1)
[Command Line](#__tabbed_1_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_application_nodes_dataset.csv'        --> @dm:save              name = 'demo_adm_application_nodes_dataset'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_adm_application_nodes_dataset' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_application_nodes_dataset.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_adm_application_nodes_dataset)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| agentType | TEXT |     | APP\_AGENT |
| appAgentPresent | TEXT | Numerical | True |
| appAgentVersion | TEXT |     | Server Agent #21.3.0.32281 v21.3.0 GA compatible with 4.4.1.0 rcd7d7317f698cefb9003377c1af0ff3ef81ee922 release/21.3.0 |
| app\_name | TEXT |     | Petclinic-Sprint-App01 |
| id  | NUMERIC | Numerical | 235307 |
| ipAddress | TEXT |     | 172.17.0.1 |
| machineAgentPresent | TEXT | Numerical | False |
| machineAgentVersion | TEXT |     | Machine Agent v21.3.0-3059 GA compatible with 4.4.1.0 Build Date 2021-03-24 18:34:20 |
| machineId | NUMERIC | Numerical | 490670 |
| machineName | TEXT |     | localhost |
| machineOSType | TEXT |     | Linux |
| name | TEXT |     | Petclinic-Sprint-App01 |
| nodeUniqueLocalId | NUMERIC |     | None |
| tierId | NUMERIC | Numerical | 15306 |
| tierName | TEXT |     | Web |
| type | TEXT |     | Other |

  
  

* * *

## Dataset: demo\_adm\_apps\_to\_db\_conn\_dataset

This Dataset has **6 Rows** and **13 Columns**

Download Data: [CSV Format](/data/datasets/demo_adm_apps_to_db_conn_dataset.csv)
 | [Parquet Format](/data/datasets/demo_adm_apps_to_db_conn_dataset.parquet)

View Data: [Table Format](/data/datasets/demo_adm_apps_to_db_conn_dataset.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_apps_to_db_conn_dataset.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_adm_apps_to_db_conn_dataset'`

[Pipeline](#__tabbed_2_1)
[Command Line](#__tabbed_2_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_apps_to_db_conn_dataset.csv'        --> @dm:save              name = 'demo_adm_apps_to_db_conn_dataset'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_adm_apps_to_db_conn_dataset' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_apps_to_db_conn_dataset.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_adm_apps_to_db_conn_dataset)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| DATABASE | TEXT |     | wordpress |
| HOST | TEXT |     | 192.168.131.23 |
| ID  | NUMERIC | Numerical | 12199 |
| MAJOR\_VERSION | TEXT |     | 5.7.8-rc |
| PORT | NUMERIC | Numerical | 3306 |
| SCHEMA | TEXT |     | PETCLINIC |
| URL | TEXT |     | jdbc:mysql://192.168.134.71:3306/petclinic?autoReconnect=true |
| VENDOR | TEXT |     | MYSQL |
| app\_name | TEXT |     | CMS Application |
| applicationComponentNodeId | NUMERIC | Numerical | 0   |
| exitPointType | TEXT |     | DB  |
| label | TEXT |     | 192.168.131.23:3306 - wordpress - MYSQL |
| tierId | NUMERIC | Numerical | 0   |

  
  

* * *

## Dataset: demo\_adm\_biz\_application\_dataset

This Dataset has **4 Rows** and **4 Columns**

Download Data: [CSV Format](/data/datasets/demo_adm_biz_application_dataset.csv)
 | [Parquet Format](/data/datasets/demo_adm_biz_application_dataset.parquet)

View Data: [Table Format](/data/datasets/demo_adm_biz_application_dataset.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_biz_application_dataset.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_adm_biz_application_dataset'`

[Pipeline](#__tabbed_3_1)
[Command Line](#__tabbed_3_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_biz_application_dataset.csv'        --> @dm:save              name = 'demo_adm_biz_application_dataset'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_adm_biz_application_dataset' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_biz_application_dataset.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_adm_biz_application_dataset)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| account\_guid | TEXT |     | 552da6c3-341f-412b-be05-5768fe5aa455 |
| app\_id | NUMERIC | Numerical | 814 |
| app\_name | TEXT |     | Petclinic Application |
| description | TEXT |     | Petclinic sample application |

  
  

* * *

## Dataset: demo\_adm\_db\_server\_nodes\_dataset

This Dataset has **4 Rows** and **19 Columns**

Download Data: [CSV Format](/data/datasets/demo_adm_db_server_nodes_dataset.csv)
 | [Parquet Format](/data/datasets/demo_adm_db_server_nodes_dataset.parquet)

View Data: [Table Format](/data/datasets/demo_adm_db_server_nodes_dataset.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_db_server_nodes_dataset.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_adm_db_server_nodes_dataset'`

[Pipeline](#__tabbed_4_1)
[Command Line](#__tabbed_4_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_db_server_nodes_dataset.csv'        --> @dm:save              name = 'demo_adm_db_server_nodes_dataset'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_adm_db_server_nodes_dataset' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_adm_db_server_nodes_dataset.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_adm_db_server_nodes_dataset)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| backendId | NUMERIC | Numerical | 31286 |
| configId | NUMERIC | Numerical | 997 |
| cpuCores | NUMERIC | Numerical | 2   |
| createdOn | NUMERIC | Timestamp (unit=ms) | 1631761830000 |
| host | TEXT |     | 192.168.134.102 |
| id  | NUMERIC | Numerical | 903 |
| internalName | TEXT |     | dbmon:997 |
| ipAddress | TEXT |     | 192.168.134.102 |
| metadataProps | TEXT |     | \[{'key': 'version', 'value': '5.7'}\] |
| modifiedOn | NUMERIC | Timestamp (unit=ms) | 1647549473000 |
| name | TEXT |     | linux-fin-db01 |
| nameUnique | TEXT | Numerical | True |
| nodeId | NUMERIC | Numerical | 141573 |
| port | NUMERIC | Numerical | 3306 |
| role | TEXT |     | STANDALONE |
| simMachineId | NUMERIC | Numerical | 0   |
| type | TEXT |     | MYSQL |
| uniqueHostId | TEXT |     | 1d0a1d423f6b |
| version | NUMERIC | Numerical | 0   |

  
  

* * *

## Dataset: demo\_aws\_ec2\_inst\_config\_dataset

This Dataset has **6,251 Rows** and **9 Columns**

Download Data: [CSV Format](/data/datasets/demo_aws_ec2_inst_config_dataset.csv)
 | [Parquet Format](/data/datasets/demo_aws_ec2_inst_config_dataset.parquet)

View Data: [Table Format](/data/datasets/demo_aws_ec2_inst_config_dataset.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_aws_ec2_inst_config_dataset.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_aws_ec2_inst_config_dataset'`

[Pipeline](#__tabbed_5_1)
[Command Line](#__tabbed_5_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_aws_ec2_inst_config_dataset.csv'        --> @dm:save              name = 'demo_aws_ec2_inst_config_dataset'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_aws_ec2_inst_config_dataset' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_aws_ec2_inst_config_dataset.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_aws_ec2_inst_config_dataset)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| aws\_ec2\_type | TEXT |     | r6g.16xlarge |
| aws\_ec2\_cpus | NUMERIC | Numerical | 64  |
| aws\_ec2\_cpu\_speed\_ghz | NUMERIC | Numerical | 2.5 |
| aws\_ec2\_memory\_gb | NUMERIC | Numerical | 512.0 |
| aws\_ec2\_network\_speed | TEXT |     | 25 Gigabit |
| aws\_ec2\_disk\_iops\_max | NUMERIC | Numerical | 80000.0 |
| aws\_ec2\_disk\_mbps\_max | NUMERIC | Numerical | 2375.0 |
| aws\_ec2\_inst\_baremetal | TEXT | Numerical | False |
| aws\_region | TEXT |     | eu-north-1 |

  
  

* * *

## Dataset: demo\_cisco\_ucs\_blade\_inventory\_dataset

This Dataset has **16 Rows** and **9 Columns**

Download Data: [CSV Format](/data/datasets/demo_cisco_ucs_blade_inventory_dataset.csv)
 | [Parquet Format](/data/datasets/demo_cisco_ucs_blade_inventory_dataset.parquet)

View Data: [Table Format](/data/datasets/demo_cisco_ucs_blade_inventory_dataset.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_blade_inventory_dataset.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_cisco_ucs_blade_inventory_dataset'`

[Pipeline](#__tabbed_6_1)
[Command Line](#__tabbed_6_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_blade_inventory_dataset.csv'        --> @dm:save              name = 'demo_cisco_ucs_blade_inventory_dataset'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_cisco_ucs_blade_inventory_dataset' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_blade_inventory_dataset.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_cisco_ucs_blade_inventory_dataset)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| ucsm\_ip | TEXT |     | 192.168.158.8 |
| dn  | TEXT |     | sys/chassis-1/blade-6 |
| rn  | TEXT |     | blade-6 |
| model | TEXT |     | UCSB-B200-M3 |
| serial | TEXT |     | ACM1746J9ZL |
| service\_profile\_name | TEXT |     | AF-Server-Pro-C1\_S6 |
| uuid | TEXT |     | cc9ba9e0-cb43-11e3-0000-0000000000af |
| original\_uuid | TEXT |     | dc2e7bfc-a160-4f13-982b-efeafc9bef82 |
| assigned\_to\_dn | TEXT |     | org-root/org-AppFabrix/ls-AF-Server-Pro-C1\_S6 |

  
  

* * *

## Dataset: demo\_cisco\_ucs\_chassis\_inventory\_dataset

This Dataset has **4 Rows** and **7 Columns**

Download Data: [CSV Format](/data/datasets/demo_cisco_ucs_chassis_inventory_dataset.csv)
 | [Parquet Format](/data/datasets/demo_cisco_ucs_chassis_inventory_dataset.parquet)

View Data: [Table Format](/data/datasets/demo_cisco_ucs_chassis_inventory_dataset.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_chassis_inventory_dataset.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_cisco_ucs_chassis_inventory_dataset'`

[Pipeline](#__tabbed_7_1)
[Command Line](#__tabbed_7_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_chassis_inventory_dataset.csv'        --> @dm:save              name = 'demo_cisco_ucs_chassis_inventory_dataset'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_cisco_ucs_chassis_inventory_dataset' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_chassis_inventory_dataset.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_cisco_ucs_chassis_inventory_dataset)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| ucsm\_ip | TEXT |     | 192.168.158.8 |
| dn  | TEXT |     | sys/chassis-1 |
| rn  | TEXT |     | chassis-1 |
| model | TEXT |     | N20-C6508 |
| serial | TEXT |     | ACM1449GPD8 |
| vendor | TEXT |     | Cisco Systems Inc |
| conn\_path | TEXT |     | A   |

  
  

* * *

## Dataset: demo\_cisco\_ucs\_cimc\_dataset

This Dataset has **5 Rows** and **8 Columns**

Download Data: [CSV Format](/data/datasets/demo_cisco_ucs_cimc_dataset.csv)
 | [Parquet Format](/data/datasets/demo_cisco_ucs_cimc_dataset.parquet)

View Data: [Table Format](/data/datasets/demo_cisco_ucs_cimc_dataset.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_cimc_dataset.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_cisco_ucs_cimc_dataset'`

[Pipeline](#__tabbed_8_1)
[Command Line](#__tabbed_8_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_cimc_dataset.csv'        --> @dm:save              name = 'demo_cisco_ucs_cimc_dataset'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_cisco_ucs_cimc_dataset' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_cimc_dataset.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_cisco_ucs_cimc_dataset)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| Unnamed: 0 | NUMERIC | Numerical | 0   |
| ucs\_server\_cimc\_ip | TEXT |     | 192.168.158.24 |
| ucs\_server\_hostname | TEXT |     | C240-ACM1811V15Q |
| ucs\_server\_pid | TEXT |     | UCSC-C240-M3S |
| ucs\_server\_serial | TEXT |     | ACM1811V15Q |
| ucs\_server\_vendor | TEXT |     | Cisco Systems Inc |
| ucs\_server\_cimc\_mac | TEXT |     | 74:26:AC:C9:95:4B |
| ucs\_server\_bios\_uuid | TEXT |     | 3841852f-ebe9-da47-b469-3fed10d8c7ee |

  
  

* * *

## Dataset: demo\_cisco\_ucs\_fi\_cdp\_inventory\_dataset

This Dataset has **8 Rows** and **10 Columns**

Download Data: [CSV Format](/data/datasets/demo_cisco_ucs_fi_cdp_inventory_dataset.csv)
 | [Parquet Format](/data/datasets/demo_cisco_ucs_fi_cdp_inventory_dataset.parquet)

View Data: [Table Format](/data/datasets/demo_cisco_ucs_fi_cdp_inventory_dataset.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_fi_cdp_inventory_dataset.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_cisco_ucs_fi_cdp_inventory_dataset'`

[Pipeline](#__tabbed_9_1)
[Command Line](#__tabbed_9_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_fi_cdp_inventory_dataset.csv'        --> @dm:save              name = 'demo_cisco_ucs_fi_cdp_inventory_dataset'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_cisco_ucs_fi_cdp_inventory_dataset' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_fi_cdp_inventory_dataset.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_cisco_ucs_fi_cdp_inventory_dataset)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| ucsm\_ip | TEXT |     | 192.168.158.8 |
| dn  | TEXT |     | sys/switch-B/lan-neighbors/if-Ethernet1/19 |
| fi\_port\_dn | TEXT |     | sys/switch-B/slot-1/switch-ether/port-19 |
| local\_interface | TEXT |     | Ethernet1/19 |
| phy\_switch\_device\_id | TEXT |     | N5K-B.engr.acme.com(ACM144913H3) |
| phy\_switch\_ip\_address | TEXT |     | 192.168.158.10 |
| phy\_switch\_model | TEXT |     | N5K-C5010P-BF |
| phy\_switch\_interface | TEXT |     | Ethernet1/1 |
| phy\_switch\_serial | TEXT |     | ACM144913H3 |
| phy\_switch\_device\_name | TEXT |     | N5K-B.engr.acme.com |

  
  

* * *

## Dataset: demo\_cisco\_ucs\_fi\_inventory\_dataset

This Dataset has **2 Rows** and **8 Columns**

Download Data: [CSV Format](/data/datasets/demo_cisco_ucs_fi_inventory_dataset.csv)
 | [Parquet Format](/data/datasets/demo_cisco_ucs_fi_inventory_dataset.parquet)

View Data: [Table Format](/data/datasets/demo_cisco_ucs_fi_inventory_dataset.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_fi_inventory_dataset.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_cisco_ucs_fi_inventory_dataset'`

[Pipeline](#__tabbed_10_1)
[Command Line](#__tabbed_10_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_fi_inventory_dataset.csv'        --> @dm:save              name = 'demo_cisco_ucs_fi_inventory_dataset'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_cisco_ucs_fi_inventory_dataset' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_cisco_ucs_fi_inventory_dataset.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_cisco_ucs_fi_inventory_dataset)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| ucsm\_ip | TEXT |     | 192.168.158.8 |
| dn  | TEXT |     | sys/switch-A |
| rn  | TEXT |     | switch-A |
| model | TEXT |     | UCS-FI-6248UP |
| serial | TEXT |     | ACM180402FF |
| id  | TEXT |     | A   |
| oob\_if\_ip | TEXT |     | 192.168.158.5 |
| oob\_if\_mac | TEXT |     | 00:2A:6A:C0:B4:21 |

  
  

* * *

## Dataset: demo\_vcenter\_inventory

This Dataset has **1 Row** and **15 Columns**

Download Data: [CSV Format](/data/datasets/demo_vcenter_inventory.csv)
 | [Parquet Format](/data/datasets/demo_vcenter_inventory.parquet)

View Data: [Table Format](/data/datasets/demo_vcenter_inventory.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vcenter_inventory.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_vcenter_inventory'`

[Pipeline](#__tabbed_11_1)
[Command Line](#__tabbed_11_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vcenter_inventory.csv'        --> @dm:save              name = 'demo_vcenter_inventory'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_vcenter_inventory' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vcenter_inventory.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_vcenter_inventory)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| build | NUMERIC |     | 18485185 |
| collection\_timestamp | NUMERIC | Timestamp (unit=ms) | 1652391042622 |
| fullName | TEXT |     | VMware vCenter Server 6.7.0 build-18485185 |
| instanceUuid | TEXT |     | 9229d458-659f-49d6-96bf-9be0b79355e6 |
| licenseProductName | TEXT |     | VMware VirtualCenter Server |
| licenseProductVersion | NUMERIC |     | 6.0 |
| localeBuild | NUMERIC |     | 0   |
| localeVersion | TEXT |     | INTL |
| name | TEXT |     | VMware vCenter Server |
| osType | TEXT |     | linux-x64 |
| productLineId | TEXT |     | vpx |
| vcenter\_address | TEXT |     | 192.168.125.61 |
| vendor | TEXT |     | VMware, Inc. |
| version | TEXT | datetimestr | 6.7.0 |
| vcenter\_fqdn | TEXT |     | vcenter-65-dr-01.engr.acme.com |

  
  

* * *

## Dataset: demo\_vmware\_datastore\_inventory

This Dataset has **30 Rows** and **35 Columns**

Download Data: [CSV Format](/data/datasets/demo_vmware_datastore_inventory.csv)
 | [Parquet Format](/data/datasets/demo_vmware_datastore_inventory.parquet)

View Data: [Table Format](/data/datasets/demo_vmware_datastore_inventory.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_datastore_inventory.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_vmware_datastore_inventory'`

[Pipeline](#__tabbed_12_1)
[Command Line](#__tabbed_12_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_datastore_inventory.csv'        --> @dm:save              name = 'demo_vmware_datastore_inventory'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_vmware_datastore_inventory' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_datastore_inventory.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_vmware_datastore_inventory)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| capacity | NUMERIC | Timestamp (unit=ms) | 1789927620608.0 |
| capacity\_GB | NUMERIC | Numerical | 1667 |
| collection\_timestamp | NUMERIC | Timestamp (unit=ms) | 1652391085119 |
| datacenter | TEXT |     | acme-datacenter |
| dsActiveAlarms | TEXT |     | vim.alarm.Alarm:alarm-11: yellow |
| ds\_cluster\_capacity | NUMERIC | Numerical | 8796093022208.0 |
| ds\_cluster\_datastores | TEXT |     | netapp-pm-nfs-10g-01, netapp-pm-nfs-10g-02 |
| ds\_cluster\_freeSpace | NUMERIC | Timestamp (unit=ms) | 3443219832832.0 |
| ds\_cluster\_name | TEXT |     | netapp-pm-cluster01 |
| ds\_cluster\_overallStatus | TEXT |     | yellow |
| extents | TEXT |     | naa.600605b009257580237343ae0fc1af57 |
| freeSpace\_GB | NUMERIC | Numerical | 1661 |
| host\_accessMode | TEXT |     | readWrite |
| host\_accessible | TEXT | Numerical | True |
| host\_mounted | TEXT | Numerical | True |
| host\_name | TEXT |     | 192.168.131.61 |
| host\_path | TEXT |     | /vmfs/volumes/5be089af-90cd9dc0-410d-d072dca05ec8 |
| is\_accessible | TEXT | Numerical | True |
| local | TEXT | Numerical | True |
| multipleHostAccess | TEXT | Numerical | False |
| name | TEXT |     | datastore26 |
| num\_of\_hosts | NUMERIC | Numerical | 1   |
| overallStatus | NUMERIC |     | None |
| overprovisioned\_pct | NUMERIC | Numerical | 0   |
| provisioned\_GB | NUMERIC | Numerical | 6   |
| remoteHost | TEXT |     | 192.168.107.33 |
| remotePath | TEXT |     | /vol/vol\_prod\_only\_01 |
| ssd | TEXT | Numerical | False |
| type | TEXT |     | VMFS |
| uncommitted\_GB | NUMERIC | Numerical | 0   |
| url | TEXT |     | ds:///vmfs/volumes/5be089af-90cd9dc0-410d-d072dca05ec8/ |
| uuid | TEXT |     | 5be089af-90cd9dc0-410d-d072dca05ec8 |
| vcenter\_address | TEXT |     | 192.168.125.61 |
| vmfs\_version | NUMERIC | Numerical | 5.81 |
| cluster | NUMERIC |     | None |

  
  

* * *

## Dataset: demo\_vmware\_host\_inventory

This Dataset has **5 Rows** and **212 Columns**

Download Data: [CSV Format](/data/datasets/demo_vmware_host_inventory.csv)
 | [Parquet Format](/data/datasets/demo_vmware_host_inventory.parquet)

View Data: [Table Format](/data/datasets/demo_vmware_host_inventory.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_host_inventory.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_vmware_host_inventory'`

[Pipeline](#__tabbed_13_1)
[Command Line](#__tabbed_13_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_host_inventory.csv'        --> @dm:save              name = 'demo_vmware_host_inventory'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_vmware_host_inventory' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_host_inventory.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_vmware_host_inventory)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| accel3dSupported | TEXT | Numerical | False |
| accessible\_datastores | TEXT |     | netapp-prod-only-01, datastore28, netapp-prod-only-02, netapp\_oia\_dev\_01, netapp-pm-nfs-10g-01, netapp-pm-nfs-10g-02 |
| agentVmDatastore | NUMERIC |     | None |
| agentVmNetwork | NUMERIC |     | None |
| autostartmgrenabled | NUMERIC |     | None |
| backgroundSnapshotsSupported | TEXT | Numerical | False |
| canSetPhysicalNicLinkSpeed | TEXT | Numerical | True |
| capacityForVmCache | NUMERIC |     | None |
| cloneFromSnapshotSupported | TEXT | Numerical | True |
| cluster | TEXT |     | acme-cluster-01 |
| cluster\_alarm | TEXT |     | Host hardware system board status: red, Virtual machine CPU usage: yellow, Virtual machine CPU usage: red |
| cluster\_drs\_enabled | TEXT | Numerical | True |
| cluster\_effectiveCpu\_MHz | NUMERIC | Numerical | 244860 |
| cluster\_effectiveMemory\_GB | NUMERIC | Numerical | 1766 |
| cluster\_ha\_enabled | TEXT | Numerical | True |
| cluster\_numHosts | NUMERIC | Numerical | 5   |
| cluster\_totalCpu\_MHz | NUMERIC | Numerical | 279900 |
| cluster\_totalMemory\_GB | NUMERIC | Numerical | 1823 |
| collection\_timestamp | NUMERIC | Timestamp (unit=ms) | 1652391084048 |
| coniproutedefaultGateway | NUMERIC |     | None |
| coniproutegatewayDevice | NUMERIC |     | None |
| coniprouteipV6DefaultGateway | NUMERIC |     | None |
| coniprouteipV6GatewayDevice | NUMERIC |     | None |
| connectionState | TEXT |     | connected |
| cpuHwMmuSupported | TEXT | Numerical | True |
| cpuMemoryResourceConfigurationSupported | TEXT | Numerical | True |
| cpuMhz | NUMERIC | Numerical | 2799 |
| cpuModel | TEXT |     | Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz |
| cpuallocationexpandableReservation | TEXT | Numerical | False |
| cpuallocationlimit | NUMERIC | Numerical | 56000 |
| cpuallocationoverheadLimit | NUMERIC | Numerical | 0   |
| cpuallocationreservation | NUMERIC | Numerical | 56000 |
| cpuallocationsahreslevel | TEXT |     | custom |
| cpuallocationsahresshares | NUMERIC | Numerical | 4096000 |
| cryptoState | TEXT |     | incapable |
| cryptoSupported | TEXT | Numerical | True |
| dasHostState | TEXT |     | connectedToMaster |
| datacenter | TEXT |     | acme-datacenter |
| datastorePrincipalSupported | TEXT | Numerical | False |
| datastores | TEXT |     | netapp-prod-only-01, datastore28, netapp-prod-only-02, netapp\_oia\_dev\_01, netapp-pm-nfs-10g-01, netapp-pm-nfs-10g-02 |
| datetimesystemzonekey | TEXT |     | UTC |
| datetimesystemzonename | TEXT |     | UTC |
| defaultVFlashModule | TEXT |     | vfc |
| deltaDiskBackingsSupported | TEXT | Numerical | True |
| dhcpOnVnicSupported | TEXT | Numerical | True |
| diagnosticSystemPartitionNumber | NUMERIC | Numerical | 9   |
| diagnosticSystemPartitionSlots | NUMERIC | Numerical | \-15 |
| diagnosticSystemPartitionStorageType | TEXT |     | networkAttached |
| diagnosticSystemPartitionidname | TEXT |     | naa.600605b00925b1802377f5d107efff34 |
| diagnosticSystemdiagnosticType | TEXT |     | singleHost |
| distributedCpuFairness | NUMERIC | Numerical | 190 |
| distributedMemoryFairness | NUMERIC | Numerical | 257 |
| dnsConfigSupported | TEXT | Numerical | True |
| dnsconfigdomainname | TEXT |     | acme.internal |
| dnsconfighostname | TEXT |     | milesxi-dr-03 |
| dnsconfigsearchdomains | TEXT |     | acme.internal, engr.acme.com |
| dnsconfiguseddhcp | TEXT | Numerical | False |
| dnsserveripaddress | TEXT |     | 192.168.159.100, 192.168.159.101 |
| dvswitches | TEXT |     | ACME-Prod-DR-dvSwitch01 |
| eightPlusHostVmfsSharedAccessSupported | TEXT | Numerical | True |
| encryptedVMotionSupported | TEXT | Numerical | True |
| encryptionCBRCSupported | TEXT | Numerical | False |
| encryptionChangeOnAddRemoveSupported | TEXT | Numerical | False |
| encryptionFaultToleranceSupported | TEXT | Numerical | False |
| encryptionHBRSupported | TEXT | Numerical | True |
| encryptionHotOperationSupported | TEXT | Numerical | False |
| encryptionMemorySaveSupported | TEXT | Numerical | True |
| encryptionRDMSupported | TEXT | Numerical | False |
| encryptionVFlashSupported | TEXT | Numerical | False |
| encryptionWithSnapshotsSupported | TEXT | Numerical | False |
| esx\_host\_build | TEXT |     | VMware ESXi 6.7.0 build-17700523 |
| esx\_host\_hardware\_model | TEXT |     | UCSC-C240-M3S |
| esx\_host\_hardware\_vendor | TEXT |     | Cisco Systems Inc |
| esx\_host\_memory\_size | NUMERIC | Numerical | 360639045632 |
| esx\_host\_num\_cpu\_cores | NUMERIC | Numerical | 20  |
| esx\_host\_num\_cpu\_threads | NUMERIC | Numerical | 40  |
| esx\_host\_num\_hbas | NUMERIC | Numerical | 4   |
| esx\_host\_num\_nics | NUMERIC | Numerical | 6   |
| esx\_host\_status | TEXT |     | green |
| esx\_host\_version | TEXT | datetimestr | 6.7.0 |
| esxi\_host\_hw\_AssetTag | TEXT |     | Unknown |
| esxi\_host\_hw\_ServiceTag | TEXT |     | FCH1623VDBE |
| faultToleranceEnabled | TEXT | Numerical | False |
| featureCapabilitiesSupported | TEXT | Numerical | True |
| firewallIpRulesSupported | TEXT | Numerical | True |
| firewallincomingblocked | TEXT | Numerical | True |
| firewalloutgoingblocked | TEXT | Numerical | True |
| freeForVmCache | NUMERIC |     | None |
| ftSupported | TEXT | Numerical | False |
| fullName | TEXT |     | VMware ESXi 6.7.0 build-17700523 |
| gatewayId | NUMERIC |     | None |
| gatewayOnNicSupported | TEXT | Numerical | True |
| gatewayType | NUMERIC |     | None |
| hardware\_bios\_uuid | TEXT |     | dd833ac5-70e1-5b4f-af91-ea3f5065ae64 |
| hardware\_vendor | TEXT |     | Cisco Systems Inc |
| hbrNicSelectionSupported | TEXT | Numerical | True |
| host | TEXT |     | 192.168.131.63 |
| hostAccessManagerSupported | TEXT | Numerical | True |
| hostMaxVirtualDiskCapacity | NUMERIC |     | None |
| host\_alarm | NUMERIC |     | None |
| host\_id | TEXT |     | dd833ac5-70e1-5b4f-af91-ea3f5065ae64 |
| host\_overall\_cpu\_usage\_MHz | NUMERIC | Numerical | 28251 |
| hostaccesslockdownmode | TEXT |     | lockdownDisabled |
| hostport | NUMERIC | Numerical | 443 |
| hostservices | TEXT |     | Direct Console UI, ESXi Shell, SSH, Load-Based Teaming Daemon, Active Directory Service, NTP Daemon, PC/SC Smart Card Daemon, CIM Server, slpd, SNMP Server, Syslog Server, vSphere High Availability Agent, VMware vCenter Agent, X.Org Server |
| hyperthreadInfoactive | TEXT | Numerical | True |
| hyperthreadconfig | TEXT | Numerical | True |
| hyperthreadoptavailable | TEXT | Numerical | True |
| inMaintenanceMode | TEXT | Numerical | False |
| inQuarantineMode | TEXT | Numerical | False |
| inaccessible\_datastores | NUMERIC |     | None |
| ipRouteConfigSupported | TEXT | Numerical | True |
| ipV6Supported | TEXT | Numerical | True |
| ipmiSupported | TEXT | Numerical | True |
| iproutedefaultGateway | TEXT |     | 192.168.131.1 |
| iproutegatewayDevice | NUMERIC |     | None |
| iprouteipV6DefaultGateway | NUMERIC |     | None |
| iprouteipV6GatewayDevice | NUMERIC |     | None |
| iscsiSupported | TEXT | Numerical | True |
| latencySensitivitySupported | TEXT | Numerical | True |
| licenseProductName | TEXT |     | VMware ESX Server |
| licenseProductVersion | NUMERIC | Numerical | 6.0 |
| localDatastoreSupported | TEXT | Numerical | False |
| localSwapDatastoreSupported | TEXT | Numerical | True |
| localeBuild | NUMERIC | Numerical | 0   |
| localeVersion | TEXT |     | INTL |
| loginBySSLThumbprintSupported | TEXT | Numerical | True |
| maintenanceModeSupported | TEXT | Numerical | True |
| managementServerIp | TEXT |     | 192.168.125.61 |
| markAsLocalSupported | TEXT | Numerical | True |
| markAsSsdSupported | TEXT | Numerical | True |
| maxHostRunningVms | NUMERIC | Numerical | 640 |
| maxHostSupportedVcpus | NUMERIC | Numerical | 640 |
| maxNumDisksSVMotion | NUMERIC | Numerical | 256 |
| maxPortGroupsPerVswitch | NUMERIC |     | None |
| maxRegisteredVMs | NUMERIC | Numerical | 2560 |
| maxRunningVMs | NUMERIC | Numerical | 0   |
| maxSupportedVMs | NUMERIC |     | None |
| maxSupportedVcpus | NUMERIC |     | None |
| maxVcpusPerFtVm | NUMERIC | Numerical | 8   |
| memallocationexpandableReservation | TEXT | Numerical | False |
| memallocationlimit | NUMERIC | Numerical | 343547 |
| memallocationoverheadLimit | NUMERIC | Numerical | 0   |
| memallocationreservation | NUMERIC | Numerical | 343547 |
| memallocationsahreslevel | TEXT |     | custom |
| memallocationsahresshares | NUMERIC | Timestamp (unit=s) | 2147483647 |
| memorySize | NUMERIC | Numerical | 360639045632 |
| model | TEXT |     | UCSC-C240-M3S |
| nfsMountCreationRequired | TEXT | Numerical | True |
| nfsMountCreationSupported | TEXT | Numerical | True |
| nfsSupported | TEXT | Numerical | True |
| nicTeamingPolicy | TEXT |     | loadbalance\_ip, loadbalance\_srcmac, loadbalance\_srcid, failover\_explicit |
| no\_of\_dvswitches | NUMERIC | Numerical | 1   |
| no\_of\_vms | NUMERIC | Numerical | 38  |
| no\_of\_vnics | NUMERIC | Numerical | 4   |
| no\_of\_vswitches | NUMERIC | Numerical | 1   |
| ntpserveriporfqdn | TEXT |     | 0.us.pool.ntp.org, 1.us.pool.ntp.org |
| numCpuCores | NUMERIC | Numerical | 20  |
| numCpuPkgs | NUMERIC | Numerical | 2   |
| numCpuThreads | NUMERIC | Numerical | 40  |
| numHBAs | NUMERIC | Numerical | 4   |
| numNics | NUMERIC | Numerical | 6   |
| num\_of\_datastores | NUMERIC | Numerical | 6   |
| num\_of\_portgroups | NUMERIC | Numerical | 11  |
| osType | TEXT |     | vmnix-x86 |
| overallCpuUsage | NUMERIC | Numerical | 28251 |
| overallMemoryUsage\_MB | NUMERIC | Numerical | 305589 |
| powerState | TEXT |     | poweredOn |
| powerpolicyName | NUMERIC |     | None |
| powerpolicyShortName | NUMERIC |     | None |
| productLineId | TEXT |     | embeddedEsx |
| product\_vendor | TEXT |     | VMware, Inc. |
| rebootRequired | TEXT | Numerical | False |
| sanSupported | TEXT | Numerical | True |
| serialNumber | NUMERIC |     | None |
| serviceConsoleReserved | NUMERIC | Numerical | 0   |
| serviceConsoleReservedCfg | NUMERIC | Numerical | 0   |
| serviceConsoleUnReserved | NUMERIC | Numerical | 0   |
| snmpconfigenabled | NUMERIC |     | None |
| snmpconfigport | NUMERIC | Numerical | 0   |
| snmpconfigreadonlycommunities | TEXT |     | \[\] |
| snmpconfigtraptargets | TEXT |     | \[\] |
| standbyMode | TEXT |     | none |
| supportsNetworkHints | TEXT | Numerical | True |
| supportsNicTeaming | TEXT | Numerical | True |
| supportsVlan | TEXT | Numerical | True |
| swapCacheReservationInGB | NUMERIC | Numerical | 0   |
| systemdefaultautostartdelay | NUMERIC | Numerical | 0   |
| systemdefaultautostoptdelay | NUMERIC | Numerical | 0   |
| systemdefaultpoweroffaction | NUMERIC |     | None |
| total\_vm | NUMERIC | Numerical | 38  |
| uptime\_seconds | NUMERIC | Numerical | 6714635 |
| usesServiceConsoleNic | TEXT | Numerical | False |
| vFlashResourceConfigInfocapacity | NUMERIC | Numerical | 0   |
| vcenter\_address | TEXT |     | 192.168.125.61 |
| version | TEXT | datetimestr | 6.7.0 |
| vffsvolumesaccessible | NUMERIC |     | None |
| vflashresourcecapacity | NUMERIC |     | None |
| vflashresourceusage | NUMERIC | Numerical | 0   |
| virtualMachineMax | NUMERIC | Numerical | 0   |
| virtualMachineMin | NUMERIC | Numerical | 0   |
| virtualMachineReserved | NUMERIC | Numerical | 0   |
| vmfsExtentExpansionSupported | TEXT | Numerical | True |
| vmmemoryreserveallocpolicy | NUMERIC |     | None |
| vnicConfigSupported | TEXT | Numerical | True |
| vnics | TEXT |     | vmk0, vmk1, vmk2, vmk3 |
| vswitchConfigSupported | TEXT | Numerical | True |
| vswitches | TEXT |     | vSwitch0 |
| waitForHeartbeat | NUMERIC |     | None |
| connected\_switchports\_address | NUMERIC |     | None |
| connected\_switchports\_mgmtAddr | NUMERIC |     | None |
| connected\_switchports\_devId | NUMERIC |     | None |

  
  

* * *

## Dataset: demo\_vmware\_host\_vmkernel\_inventory

This Dataset has **25 Rows** and **25 Columns**

Download Data: [CSV Format](/data/datasets/demo_vmware_host_vmkernel_inventory.csv)
 | [Parquet Format](/data/datasets/demo_vmware_host_vmkernel_inventory.parquet)

View Data: [Table Format](/data/datasets/demo_vmware_host_vmkernel_inventory.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_host_vmkernel_inventory.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_vmware_host_vmkernel_inventory'`

[Pipeline](#__tabbed_14_1)
[Command Line](#__tabbed_14_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_host_vmkernel_inventory.csv'        --> @dm:save              name = 'demo_vmware_host_vmkernel_inventory'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_vmware_host_vmkernel_inventory' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_host_vmkernel_inventory.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_vmware_host_vmkernel_inventory)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| cluster | TEXT |     | acme-cluster-01 |
| collection\_timestamp | NUMERIC | Timestamp (unit=ms) | 1652391103918 |
| datacenter | TEXT |     | acme-datacenter |
| device | TEXT |     | vmk0 |
| dvPort\_connectionCookie | NUMERIC | Timestamp (unit=s) | 802328591.0 |
| dvPort\_portKey | NUMERIC | Numerical | 1003.0 |
| dvPort\_portgroup | TEXT |     | NFS-10G-VLAN-1011 |
| dvPort\_switchUuid | TEXT |     | 50 2a 06 40 e5 6b e5 80-59 d4 46 89 7c c8 b3 7a |
| faultToleranceLogging | TEXT |     | Disabled |
| host | TEXT |     | 192.168.131.63 |
| ipaddress | TEXT |     | 192.168.131.63 |
| key | TEXT |     | key-vim.host.VirtualNic-vmk0 |
| mac | TEXT |     | 60:73:5c:69:8a:e2 |
| management | TEXT |     | Enabled |
| mtu | NUMERIC | Numerical | 1500 |
| port | TEXT |     | key-vim.host.PortGroup.Port-33554436 |
| portgroup | TEXT |     | Management Network |
| subnetMask | TEXT |     | 255.255.255.0 |
| vSphereProvisioning | TEXT |     | Disabled |
| vSphereReplication | TEXT |     | Disabled |
| vSphereReplicationNFC | TEXT |     | Disabled |
| vcenter\_address | TEXT |     | 192.168.125.61 |
| vmotion | TEXT |     | Disabled |
| vsan | TEXT |     | Disabled |
| vsanWitness | TEXT |     | Disabled |

  
  

* * *

## Dataset: demo\_vmware\_storage\_inventory

This Dataset has **37 Rows** and **122 Columns**

Download Data: [CSV Format](/data/datasets/demo_vmware_storage_inventory.csv)
 | [Parquet Format](/data/datasets/demo_vmware_storage_inventory.parquet)

View Data: [Table Format](/data/datasets/demo_vmware_storage_inventory.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_storage_inventory.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_vmware_storage_inventory'`

[Pipeline](#__tabbed_15_1)
[Command Line](#__tabbed_15_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_storage_inventory.csv'        --> @dm:save              name = 'demo_vmware_storage_inventory'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_vmware_storage_inventory' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_storage_inventory.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_vmware_storage_inventory)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| authenticationCapabilities\_chapAuthSettable | TEXT | Numerical | True |
| authenticationCapabilities\_krb5AuthSettable | TEXT | Numerical | False |
| authenticationCapabilities\_mutualChapSettable | TEXT | Numerical | True |
| authenticationCapabilities\_spkmAuthSettable | TEXT | Numerical | False |
| authenticationCapabilities\_srpAuthSettable | TEXT | Numerical | False |
| authenticationCapabilities\_targetChapSettable | TEXT | Numerical | True |
| authenticationCapabilities\_targetMutualChapSettable | TEXT | Numerical | True |
| authenticationProperties\_chapAuthEnabled | TEXT | Numerical | False |
| authenticationProperties\_chapAuthenticationType | TEXT |     | chapProhibited |
| authenticationProperties\_chapInherited | NUMERIC |     | None |
| authenticationProperties\_chapName | NUMERIC |     | None |
| authenticationProperties\_chapSecret | TEXT |     | XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| authenticationProperties\_mutualChapAuthenticationType | TEXT |     | chapProhibited |
| authenticationProperties\_mutualChapInherited | NUMERIC |     | None |
| authenticationProperties\_mutualChapName | NUMERIC |     | None |
| authenticationProperties\_mutualChapSecret | TEXT |     | XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| bus | NUMERIC | Numerical | 13  |
| canBeDisabled | TEXT | Numerical | True |
| cluster | TEXT |     | acme-cluster-01 |
| collection\_timestamp | NUMERIC | Timestamp (unit=ms) | 1652391097175 |
| currentSpeedMb | NUMERIC |     | None |
| datacenter | TEXT |     | acme-datacenter |
| device | TEXT |     | vmhba0 |
| digestCapabilities\_dataDigestSettable | TEXT | Numerical | True |
| digestCapabilities\_headerDigestSettable | TEXT | Numerical | True |
| digestCapabilities\_targetDataDigestSettable | TEXT | Numerical | True |
| digestCapabilities\_targetHeaderDigestSettable | TEXT | Numerical | True |
| digestProperties\_dataDigestInherited | NUMERIC |     | None |
| digestProperties\_dataDigestType | TEXT |     | digestProhibited |
| digestProperties\_headerDigestInherited | NUMERIC |     | None |
| digestProperties\_headerDigestType | TEXT |     | digestProhibited |
| discoveryCapabilities\_iSnsDiscoverySettable | TEXT | Numerical | False |
| discoveryCapabilities\_sendTargetsDiscoverySettable | TEXT | Numerical | False |
| discoveryCapabilities\_slpDiscoverySettable | TEXT | Numerical | False |
| discoveryCapabilities\_staticTargetDiscoverySettable | TEXT | Numerical | False |
| discoveryProperties\_iSnsDiscoveryEnabled | TEXT | Numerical | False |
| discoveryProperties\_iSnsDiscoveryMethod | NUMERIC |     | None |
| discoveryProperties\_iSnsHost | NUMERIC |     | None |
| discoveryProperties\_sendTargetsDiscoveryEnabled | TEXT | Numerical | True |
| discoveryProperties\_slpDiscoveryEnabled | TEXT | Numerical | False |
| discoveryProperties\_slpDiscoveryMethod | NUMERIC |     | None |
| discoveryProperties\_slpHost | NUMERIC |     | None |
| discoveryProperties\_staticTargetDiscoveryEnabled | TEXT | Numerical | True |
| driver | TEXT |     | nfnic |
| host | TEXT |     | 192.168.131.63 |
| iScsiAlias | NUMERIC |     | None |
| iScsiName | TEXT |     | iqn.1998-01.com.vmware:milesxi-dr-03-7e533cd0 |
| ipCapabilities\_addressSettable | TEXT | Numerical | False |
| ipCapabilities\_alternateDnsServerAddressSettable | TEXT | Numerical | False |
| ipCapabilities\_arpRedirectSettable | TEXT | Numerical | False |
| ipCapabilities\_defaultGatewaySettable | TEXT | Numerical | False |
| ipCapabilities\_hostNameAsTargetAddress | TEXT | Numerical | True |
| ipCapabilities\_ipConfigurationMethodSettable | TEXT | Numerical | False |
| ipCapabilities\_ipv4EnableSettable | TEXT | Numerical | False |
| ipCapabilities\_ipv6DefaultGatewaySettable | TEXT | Numerical | False |
| ipCapabilities\_ipv6DhcpConfigurationSettable | TEXT | Numerical | False |
| ipCapabilities\_ipv6EnableSettable | TEXT | Numerical | False |
| ipCapabilities\_ipv6LinkLocalAutoConfigurationSettable | TEXT | Numerical | False |
| ipCapabilities\_ipv6MaxStaticAddressesSupported | NUMERIC | Numerical | 0.0 |
| ipCapabilities\_ipv6PrefixLength | NUMERIC | Numerical | 0.0 |
| ipCapabilities\_ipv6PrefixLengthSettable | TEXT | Numerical | False |
| ipCapabilities\_ipv6RouterAdvertisementConfigurationSettable | TEXT | Numerical | False |
| ipCapabilities\_ipv6Supported | TEXT | Numerical | False |
| ipCapabilities\_mtuSettable | TEXT | Numerical | False |
| ipCapabilities\_nameAliasSettable | TEXT | Numerical | True |
| ipCapabilities\_primaryDnsServerAddressSettable | TEXT | Numerical | False |
| ipCapabilities\_subnetMaskSettable | TEXT | Numerical | False |
| ipProperties\_address | NUMERIC |     | None |
| ipProperties\_alternateDnsServerAddress | NUMERIC |     | None |
| ipProperties\_arpRedirectEnabled | NUMERIC |     | None |
| ipProperties\_defaultGateway | NUMERIC |     | None |
| ipProperties\_dhcpConfigurationEnabled | TEXT | Numerical | False |
| ipProperties\_ipv4Enabled | NUMERIC |     | None |
| ipProperties\_ipv6Address | NUMERIC |     | None |
| ipProperties\_ipv6DefaultGateway | NUMERIC |     | None |
| ipProperties\_ipv6Enabled | NUMERIC |     | None |
| ipProperties\_ipv6SubnetMask | NUMERIC |     | None |
| ipProperties\_ipv6properties | NUMERIC |     | None |
| ipProperties\_jumboFramesEnabled | NUMERIC |     | None |
| ipProperties\_mac | NUMERIC |     | None |
| ipProperties\_mtu | NUMERIC |     | None |
| ipProperties\_primaryDnsServerAddress | NUMERIC |     | None |
| ipProperties\_subnetMask | NUMERIC |     | None |
| isSoftwareBased | TEXT | Numerical | True |
| key | TEXT |     | key-vim.host.FibreChannelHba-vmhba0 |
| maxSpeedMb | NUMERIC |     | None |
| model | TEXT |     | Cisco VIC FCoE HBA Driver |
| networkBindingSupport | TEXT |     | optional |
| nodeWorldWideName | TEXT |     | 10:00:fc:5b:39:5b:5f:65 |
| path\_adapter | TEXT |     | key-vim.host.FibreChannelHba-vmhba0 |
| path\_canonicalName | TEXT |     | naa.60a980003754354336244f5531446d50 |
| path\_devicePath | TEXT |     | /vmfs/devices/disks/naa.60a980003754354336244f5531446d50 |
| path\_displayName | TEXT |     | NETAPP Fibre Channel Disk (naa.60a980003754354336244f5531446d50) |
| path\_isWorkingPath | TEXT | Numerical | True |
| path\_key | TEXT |     | key-vim.host.MultipathInfo.Path-vmhba0:C0:T1:L1 |
| path\_localDisk | TEXT | Numerical | False |
| path\_lun | TEXT |     | key-vim.host.MultipathInfo.LogicalUnit-020001000060a980003754354336244f5531446d504c554e202020 |
| path\_lunType | TEXT |     | disk |
| path\_model | TEXT |     | LUN |
| path\_name | TEXT |     | vmhba0:C0:T1:L1 |
| path\_operationalState | TEXT |     | ok  |
| path\_pathState | TEXT |     | active |
| path\_revision | TEXT | Numerical | 820a |
| path\_scsiDiskType | TEXT |     | emulated512 |
| path\_scsiLevel | NUMERIC | Numerical | 5.0 |
| path\_serialNumber | TEXT |     | unavailable |
| path\_ssd | TEXT | Numerical | False |
| path\_state | TEXT |     | active |
| path\_transport\_address | TEXT |     | 192.168.101.102:3260 |
| path\_transport\_iScsiAlias | NUMERIC |     | None |
| path\_transport\_iScsiName | TEXT |     | iqn.1992-08.com.netapp:sn.1575046424 |
| path\_transport\_nodeWorldWideName | TEXT |     | 50:0a:09:80:8d:50:b6:fa |
| path\_transport\_portWorldWideName | TEXT |     | 50:0a:09:81:8d:50:b6:fa |
| path\_uuid | TEXT |     | 020001000060a980003754354336244f5531446d504c554e202020 |
| path\_vendor | TEXT |     | NETAPP |
| pci | TEXT |     | 0000:0d:00.0 |
| portType | TEXT |     | unknown |
| portWorldWideName | TEXT |     | 20:00:fc:5b:39:5b:5f:65 |
| speed | NUMERIC | Numerical | 8.0 |
| status | TEXT |     | online |
| storageProtocol | NUMERIC |     | None |
| vcenter\_address | TEXT |     | 192.168.125.61 |

  
  

* * *

## Dataset: demo\_vmware\_vm\_inventory

This Dataset has **1,415 Rows** and **76 Columns**

Download Data: [CSV Format](/data/datasets/demo_vmware_vm_inventory.csv)
 | [Parquet Format](/data/datasets/demo_vmware_vm_inventory.parquet)

View Data: [Table Format](/data/datasets/demo_vmware_vm_inventory.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_vm_inventory.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_vmware_vm_inventory'`

[Pipeline](#__tabbed_16_1)
[Command Line](#__tabbed_16_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_vm_inventory.csv'        --> @dm:save              name = 'demo_vmware_vm_inventory'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_vmware_vm_inventory' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_vm_inventory.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_vmware_vm_inventory)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| cluster | TEXT |     | acme-cluster-01 |
| collection\_timestamp | NUMERIC | Timestamp (unit=ms) | 1650000000000.0 |
| cpuHotAddEnabled | TEXT | Numerical | False |
| cpuHotRemoveEnabled | TEXT | Numerical | False |
| cpuReservation\_MHz | NUMERIC | Numerical | 0   |
| cpu\_usage\_MHz | NUMERIC | Numerical | 0   |
| cpuoverheadlimit\_MHz | NUMERIC |     | None |
| cpureservationlimit\_MHz | NUMERIC | Numerical | \-1 |
| cpushares | NUMERIC | Numerical | 8000 |
| createDate | TEXT |     | 2021-02-24T05:17:42.268Z |
| datacenter | TEXT |     | acme-datacenter |
| disk\_backing\_file | TEXT |     | \[netapp-pm-nfs-10g-01\] acme-s-demo-svc01/acme-s-demo-svc01.vmdk |
| disk\_bus\_num | NUMERIC | Numerical | 1   |
| disk\_capacity\_Bytes | NUMERIC | Numerical | 53687091200.0 |
| disk\_capacity\_KB | NUMERIC | Numerical | 52428800 |
| disk\_compatibilityMode | TEXT |     | physicalMode |
| disk\_controller | TEXT |     | SCSI controller 1 |
| disk\_controller\_type | TEXT |     | VMware paravirtual SCSI |
| disk\_datastore | TEXT |     | netapp-pm-nfs-10g-01 |
| disk\_diskMode | TEXT |     | persistent |
| disk\_eagerlyScrub | TEXT | Numerical | True |
| disk\_label | TEXT |     | Hard disk 1 |
| disk\_lunUuid | TEXT |     | 020001000060a980003754354336244f5531446d504c554e202020 |
| disk\_scsi\_controller\_unit\_num | NUMERIC | Numerical | 7   |
| disk\_split | TEXT | Numerical | False |
| disk\_thinProvisioned | TEXT | Numerical | True |
| disk\_unit\_num | NUMERIC | Numerical | 0   |
| disk\_writeThrough | TEXT | Numerical | False |
| guest | TEXT |     | Red Hat Enterprise Linux 7 (64-bit) |
| guestid | TEXT |     | rhel7\_64Guest |
| host | TEXT |     | 192.168.131.64 |
| host\_id | TEXT |     | 3841852f-ebe9-da47-b469-3fed10d8c7ee |
| id  | TEXT |     | 422a1198-86b2-5fd3-f62a-1baf5b2aeeb3 |
| ipAddress | TEXT |     | 192.168.133.87 |
| managedby | NUMERIC |     | None |
| maxCpuUsage\_MHz | NUMERIC | Numerical | 11196.0 |
| maxMemoryUsage\_MB | NUMERIC | Numerical | 16384.0 |
| mem\_res\_MB | NUMERIC | Numerical | 0   |
| mem\_usage\_guest\_MB | NUMERIC | Numerical | 0   |
| mem\_usage\_host\_MB | NUMERIC | Numerical | 0   |
| memoryHotAddEnabled | TEXT | Numerical | False |
| memoryReservation\_MB | NUMERIC | Numerical | 0   |
| memoryReservationlimit\_MB | NUMERIC | Numerical | \-1 |
| memorySizeMB | NUMERIC | Numerical | 32768 |
| memoryoverheadlimit\_MB | NUMERIC | Numerical | 151.0 |
| memoryshares | NUMERIC | Numerical | 327680 |
| memsize\_MB | NUMERIC | Numerical | 32768 |
| name | TEXT |     | acme-s-demo-svc01 |
| network | TEXT |     | ACME-PM-VMs-192.168.131.X |
| numCpu | NUMERIC | Numerical | 8   |
| numEthernetCards | NUMERIC | Numerical | 1   |
| numVirtualDisks | NUMERIC | Numerical | 3   |
| numVmiopBackings | NUMERIC | Numerical | 0.0 |
| numcorespersocket | NUMERIC | Numerical | 8   |
| numsockets | NUMERIC | Numerical | 1   |
| path | TEXT |     | \[netapp-pm-nfs-10g-01\] acme-s-demo-svc01/acme-s-demo-svc01.vmx |
| paused | TEXT | Numerical | False |
| powerState | TEXT |     | poweredOff |
| resourcePool | TEXT |     | ACME-Stable-Demo |
| storage\_committed | NUMERIC | Numerical | 83943365080.0 |
| storage\_name | TEXT |     | netapp-pm-nfs-10g-01 |
| storage\_uncommitted | NUMERIC | Numerical | 139000000000.0 |
| storage\_unshared | NUMERIC | Numerical | 83942659729.0 |
| storage\_url | TEXT |     | ds:///vmfs/volumes/dcc7386e-67893a84/ |
| template | TEXT | Numerical | False |
| toolsRunningStatus | TEXT |     | guestToolsNotRunning |
| toolsVersion | NUMERIC |     | None |
| toolsVersionStatus2 | TEXT |     | guestToolsUnmanaged |
| vcenter\_address | TEXT |     | 192.168.125.61 |
| version | TEXT |     | vmx-11 |
| vm\_controllers | NUMERIC |     | None |
| vm\_id | TEXT |     | vm-822 |
| vm\_nic\_connected | TEXT | Numerical | False |
| vm\_nic\_ipaddresses | TEXT |     | 192.168.133.87, fe80::c4d4:583e:4e04:fc59, fe80::2e82:4be4:2043:4841, fe80::a088:f3f3:ee19:32e |
| vm\_nic\_macAddress | TEXT |     | 00:50:56:aa:33:ab |
| vm\_nic\_network | TEXT |     | 50 2a 06 40 e5 6b e5 80-59 d4 46 89 7c c8 b3 7a |

  
  

* * *

## Dataset: demo\_vmware\_vswitch\_inventory

This Dataset has **107 Rows** and **63 Columns**

Download Data: [CSV Format](/data/datasets/demo_vmware_vswitch_inventory.csv)
 | [Parquet Format](/data/datasets/demo_vmware_vswitch_inventory.parquet)

View Data: [Table Format](/data/datasets/demo_vmware_vswitch_inventory.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_vswitch_inventory.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='demo_vmware_vswitch_inventory'`

[Pipeline](#__tabbed_17_1)
[Command Line](#__tabbed_17_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_vswitch_inventory.csv'        --> @dm:save              name = 'demo_vmware_vswitch_inventory'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'demo_vmware_vswitch_inventory' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/demo_vmware_vswitch_inventory.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_demo_vmware_vswitch_inventory)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| cdp\_address | TEXT |     | 192.168.2.250 |
| cdp\_devId | TEXT |     | c2960-s.acme.local |
| cdp\_hardwarePlatform | TEXT |     | cisco WS-C2960S-48LPD-L |
| cdp\_mgmtAddr | TEXT |     | 192.168.2.250 |
| cdp\_mtu | NUMERIC | Numerical | 0   |
| cdp\_portId | TEXT |     | GigabitEthernet1/0/17 |
| cdp\_version | NUMERIC | Numerical | 2   |
| cluster\_name | TEXT |     | acme-cluster-01 |
| collection\_timestamp | NUMERIC | Timestamp (unit=ms) | 1652391093875 |
| datacenter\_name | TEXT |     | acme-datacenter |
| failurecriteria\_checkBeacon | TEXT | Numerical | False |
| failurecriteria\_checkDuplex | TEXT | Numerical | False |
| failurecriteria\_checkErrorPercent | TEXT | Numerical | False |
| failurecriteria\_checkSpeed | TEXT |     | minimum |
| failurecriteria\_fullDuplex | TEXT | Numerical | False |
| failurecriteria\_percentage | NUMERIC | Numerical | 0.0 |
| failurecriteria\_speed | NUMERIC | Numerical | 10.0 |
| host\_id | TEXT |     | dd833ac5-70e1-5b4f-af91-ea3f5065ae64 |
| host\_name | TEXT |     | 192.168.131.63 |
| lacp\_loadbalanceAlgorithm | TEXT |     | srcDestIpTcpUdpPortVlan |
| lacp\_mode | TEXT |     | active |
| lacp\_name | TEXT |     | LACP01 |
| lacp\_uplinkNum | NUMERIC | Numerical | 2.0 |
| lacp\_uplinks | TEXT |     | LACP01-0,LACP01-1 |
| lacp\_vlan | NUMERIC |     | None |
| lldp\_chassisId | NUMERIC |     | None |
| lldp\_portId | NUMERIC |     | None |
| lldp\_timeToLive(seconds) | NUMERIC | Numerical | 0.0 |
| mtu | NUMERIC | Numerical | 1500 |
| nicOrder\_activeNic | TEXT |     | vmnic0 |
| nicOrder\_standbyNic | NUMERIC |     | None |
| nicTeaming\_notifySwitches | TEXT | Numerical | True |
| nicTeaming\_policy | TEXT |     | loadbalance\_srcid |
| nicTeaming\_reversePolicy | TEXT | Numerical | True |
| nicTeaming\_rollingOrder | TEXT | Numerical | False |
| numPorts | NUMERIC | Numerical | 7936 |
| numPortsAvailable | NUMERIC | Numerical | 7875.0 |
| numStandalonePorts | NUMERIC | Numerical | 0.0 |
| offloadPolicy\_checksumOffload | TEXT | Numerical | True |
| offloadPolicy\_tcpSegmentation | TEXT | Numerical | True |
| offloadPolicy\_zeroCopyXmit | TEXT | Numerical | True |
| pnic | TEXT |     | vmnic0 |
| pnic\_capacity\_ratio\_for\_reservation | NUMERIC | Numerical | 75.0 |
| portgroup | TEXT |     | VM Network |
| portgroup\_blocked | TEXT | Numerical | False |
| securityPolicy\_allowPromiscuous | TEXT | Numerical | False |
| securityPolicy\_forgedTransmits | TEXT | Numerical | True |
| securityPolicy\_macChanges | TEXT | Numerical | True |
| shapingPolicy\_averageBandwidth | NUMERIC |     | None |
| shapingPolicy\_burstSize | NUMERIC |     | None |
| shapingPolicy\_enabled | TEXT | Numerical | False |
| shapingPolicy\_peakBandwidth | NUMERIC |     | None |
| type | TEXT |     | Standard |
| uplinks | TEXT |     | ACME-Prod-DR-dvSw-DVUplinks-40 |
| vcenter\_address | TEXT |     | 192.168.125.61 |
| vlanId | NUMERIC | Numerical | 0.0 |
| vswitch\_alarms | NUMERIC |     | None |
| vswitch\_name | TEXT |     | vSwitch0 |
| vswitch\_network\_io\_control\_enabled | TEXT | Numerical | True |
| vswitch\_product\_fwd\_class | TEXT |     | etherswitch |
| vswitch\_product\_name | TEXT |     | DVS |
| vswitch\_product\_vendor | TEXT |     | VMware, Inc. |
| vswitch\_product\_version | TEXT | datetimestr | 6.5.0 |

  
  

* * *

## Dataset: imdb-10K-sentimnets-reviews

This Dataset has **10,000 Rows** and **2 Columns**

Download Data: [CSV Format](/data/datasets/imdb-10K-sentimnets-reviews.csv)
 | [Parquet Format](/data/datasets/imdb-10K-sentimnets-reviews.parquet)

View Data: [Table Format](/data/datasets/imdb-10K-sentimnets-reviews.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/imdb-10K-sentimnets-reviews.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='imdb-10K-sentimnets-reviews'`

[Pipeline](#__tabbed_18_1)
[Command Line](#__tabbed_18_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/imdb-10K-sentimnets-reviews.csv'        --> @dm:save              name = 'imdb-10K-sentimnets-reviews'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'imdb-10K-sentimnets-reviews' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/imdb-10K-sentimnets-reviews.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_imdb-10K-sentimnets-reviews)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| review | TEXT |     | Okay, I know this does'nt project India in a good light. But the overall theme of the movie is not India, it's Shakti. The power of a warlord, and the power of a mother. The relationship between Nandini and her husband and son swallow you up in their warmth. Then things go terribly wrong. The interaction between Nandini and her father in law - the power of their dysfunctional relationship - and the lives changed by it are the strengths of this movie. Shah Rukh Khan's performance seems to be a mere cameo compared to the believable desperation of Karisma Kapoor. It is easy to get caught up in the love, violence and redemption of lives in this film, and find yourself heaving a sigh of relief and sadness at the climax. The musical interludes are strengths, believable and well done. |
| sentiment | NUMERIC | Numerical | 1   |

  
  

* * *

## Dataset: incidents-for-analysis

This Dataset has **684 Rows** and **11 Columns**

Download Data: [CSV Format](/data/datasets/incidents-for-analysis.csv)
 | [Parquet Format](/data/datasets/incidents-for-analysis.parquet)

View Data: [Table Format](/data/datasets/incidents-for-analysis.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/incidents-for-analysis.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='incidents-for-analysis'`

[Pipeline](#__tabbed_19_1)
[Command Line](#__tabbed_19_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/incidents-for-analysis.csv'        --> @dm:save              name = 'incidents-for-analysis'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'incidents-for-analysis' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/incidents-for-analysis.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_incidents-for-analysis)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| Unnamed: 0.1 | NUMERIC | Numerical | 0   |
| Ticket  <br>Number | TEXT |     | INC0401467 |
| Priority | TEXT |     | Priority 3 |
| Create  <br>Timestamp | TEXT | datetimestr | 2021-10-01 04:28:00 |
| Resolved  <br>Timestamp | TEXT | datetimestr | 2021-10-01 04:49:49 |
| Duration  <br>(Hours) | TEXT |     | \=(D2-C2)\*24 |
| Summary | TEXT |     | Cannot create cure batches for D-Line of presses |
| Resolved By | TEXT |     | Naresh Chintakindi |
| Resolution Code | TEXT |     | Data Error |
| Resolution Notes | TEXT |     | Updated the D line records |
| created | TEXT | datetimestr | 2021-10-01 04:28:00 |

Pipelines using this Dataset

*   [sample-ml-classification-prediction](/Pipelines/sample-ml-classification-prediction/)
    

  
  

* * *

## Dataset: pagerduty-priority-enrichment-dict

This Dataset has **5 Rows** and **3 Columns**

Download Data: [CSV Format](/data/datasets/pagerduty-priority-enrichment-dict.csv)
 | [Parquet Format](/data/datasets/pagerduty-priority-enrichment-dict.parquet)

View Data: [Table Format](/data/datasets/pagerduty-priority-enrichment-dict.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/pagerduty-priority-enrichment-dict.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='pagerduty-priority-enrichment-dict'`

[Pipeline](#__tabbed_20_1)
[Command Line](#__tabbed_20_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/pagerduty-priority-enrichment-dict.csv'        --> @dm:save              name = 'pagerduty-priority-enrichment-dict'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'pagerduty-priority-enrichment-dict' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/pagerduty-priority-enrichment-dict.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_pagerduty-priority-enrichment-dict)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| priority\_id | TEXT |     | PLSZKS5 |
| rule | TEXT |     | priority starts with '1 - Critical' |
| rule\_id | TEXT |     | A1000 |

Pipelines using this Dataset

*   [ebonding-stream-to-pagerduty](/Pipelines/ebonding-stream-to-pagerduty/)
    

  
  

* * *

## Dataset: pagerduty-svc-enrichment-dict

This Dataset has **1 Row** and **3 Columns**

Download Data: [CSV Format](/data/datasets/pagerduty-svc-enrichment-dict.csv)
 | [Parquet Format](/data/datasets/pagerduty-svc-enrichment-dict.parquet)

View Data: [Table Format](/data/datasets/pagerduty-svc-enrichment-dict.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/pagerduty-svc-enrichment-dict.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='pagerduty-svc-enrichment-dict'`

[Pipeline](#__tabbed_21_1)
[Command Line](#__tabbed_21_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/pagerduty-svc-enrichment-dict.csv'        --> @dm:save              name = 'pagerduty-svc-enrichment-dict'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'pagerduty-svc-enrichment-dict' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/pagerduty-svc-enrichment-dict.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_pagerduty-svc-enrichment-dict)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| rule | TEXT |     | \*  |
| rule\_id | TEXT |     | A1000 |
| service\_id | TEXT |     | P8T85J9 |

Pipelines using this Dataset

*   [ebonding-stream-to-pagerduty](/Pipelines/ebonding-stream-to-pagerduty/)
    

  
  

* * *

## Dataset: pagerduty-urgency-enrichment-dict

This Dataset has **3 Rows** and **3 Columns**

Download Data: [CSV Format](/data/datasets/pagerduty-urgency-enrichment-dict.csv)
 | [Parquet Format](/data/datasets/pagerduty-urgency-enrichment-dict.parquet)

View Data: [Table Format](/data/datasets/pagerduty-urgency-enrichment-dict.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/pagerduty-urgency-enrichment-dict.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='pagerduty-urgency-enrichment-dict'`

[Pipeline](#__tabbed_22_1)
[Command Line](#__tabbed_22_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/pagerduty-urgency-enrichment-dict.csv'        --> @dm:save              name = 'pagerduty-urgency-enrichment-dict'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'pagerduty-urgency-enrichment-dict' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/pagerduty-urgency-enrichment-dict.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_pagerduty-urgency-enrichment-dict)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| rule | TEXT |     | urgency starts with '1 - High' |
| rule\_id | TEXT |     | A1000 |
| urgency\_id | TEXT |     | high |

Pipelines using this Dataset

*   [ebonding-stream-to-pagerduty](/Pipelines/ebonding-stream-to-pagerduty/)
    

  
  

* * *

## Dataset: petclinic-env-dict

This Dataset has **6 Rows** and **3 Columns**

Download Data: [CSV Format](/data/datasets/petclinic-env-dict.csv)
 | [Parquet Format](/data/datasets/petclinic-env-dict.parquet)

View Data: [Table Format](/data/datasets/petclinic-env-dict.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/petclinic-env-dict.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='petclinic-env-dict'`

[Pipeline](#__tabbed_23_1)
[Command Line](#__tabbed_23_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/petclinic-env-dict.csv'        --> @dm:save              name = 'petclinic-env-dict'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'petclinic-env-dict' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/petclinic-env-dict.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_petclinic-env-dict)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| env | TEXT |     | DEV |
| rule | TEXT |     | rda\_gw\_client\_ip is '10.95.131.101' |
| rule\_id | TEXT |     | A1000 |

Pipelines using this Dataset

*   [li-filebeat-events-to-prod-env](/Pipelines/li-filebeat-events-to-prod-env/)
    
*   [li-http-events-to-prod-env](/Pipelines/li-http-events-to-prod-env/)
    
*   [li-replay-logs-to-dev-env](/Pipelines/li-replay-logs-to-dev-env/)
    
*   [li-stream-tcp-syslogs](/Pipelines/li-stream-tcp-syslogs/)
    
*   [li-udp-syslog-events-to-prod-env](/Pipelines/li-udp-syslog-events-to-prod-env/)
    
*   [li-windows-events-to-prod-env](/Pipelines/li-windows-events-to-prod-env/)
    

  
  

* * *

## Dataset: sample-aws-vms

This Dataset has **66 Rows** and **13 Columns**

Download Data: [CSV Format](/data/datasets/sample-aws-vms.csv)
 | [Parquet Format](/data/datasets/sample-aws-vms.parquet)

View Data: [Table Format](/data/datasets/sample-aws-vms.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-aws-vms.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='sample-aws-vms'`

[Pipeline](#__tabbed_24_1)
[Command Line](#__tabbed_24_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-aws-vms.csv'        --> @dm:save              name = 'sample-aws-vms'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'sample-aws-vms' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/sample-aws-vms.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_sample-aws-vms)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| CpuOptions\_CoreCount | NUMERIC | Numerical | 1   |
| CpuOptions\_ThreadsPerCore | NUMERIC | Numerical | 1   |
| EbsOptimized | TEXT | Numerical | False |
| Hypervisor | TEXT |     | xen |
| InstanceType | TEXT |     | t2.micro |
| LaunchTime | TEXT | datetimestr | 2021-05-28T06:01:39+00:00 |
| Placement\_AvailabilityZone | TEXT |     | ap-south-1a |
| RootDeviceName | TEXT |     | /dev/sda1 |
| RootDeviceType | TEXT |     | ebs |
| State\_Code | NUMERIC | Numerical | 16  |
| State\_Name | TEXT |     | running |
| PrivateIpAddress | TEXT |     | 172.161.219.166 |
| InstanceId | TEXT |     | i-47096706649059456 |

Pipelines using this Dataset

*   [sample-vm-analytics](/Pipelines/sample-vm-analytics/)
    

  
  

* * *

## Dataset: sample-classify-predict

This Dataset has **277 Rows** and **11 Columns**

Download Data: [CSV Format](/data/datasets/sample-classify-predict.csv)
 | [Parquet Format](/data/datasets/sample-classify-predict.parquet)

View Data: [Table Format](/data/datasets/sample-classify-predict.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-classify-predict.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='sample-classify-predict'`

[Pipeline](#__tabbed_25_1)
[Command Line](#__tabbed_25_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-classify-predict.csv'        --> @dm:save              name = 'sample-classify-predict'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'sample-classify-predict' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/sample-classify-predict.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_sample-classify-predict)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| Summary | TEXT |     | PrepaidQE \| QuickOpenClose \| QLAB03 \| Not getting Store Capability IS\_DSKT\_TILL\_PILOT as N |
| Issue key | TEXT |     | COCIDG2-2233 |
| Issue id | NUMERIC | Numerical | 445204.0 |
| Issue Type | TEXT |     | Bug |
| Status | TEXT |     | Closed |
| Project type | TEXT |     | software |
| Priority | TEXT |     | Medium |
| Resolution | TEXT |     | Done |
| Creator | TEXT |     | RZaveri@ACME123.org |
| Created | TEXT | datetimestr | 2020-04-03 08:07:00 |
| Updated | TEXT | datetimestr | 2020-04-11 05:02:00 |

  
  

* * *

## Dataset: sample-classify-train

This Dataset has **6,400 Rows** and **11 Columns**

Download Data: [CSV Format](/data/datasets/sample-classify-train.csv)
 | [Parquet Format](/data/datasets/sample-classify-train.parquet)

View Data: [Table Format](/data/datasets/sample-classify-train.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-classify-train.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='sample-classify-train'`

[Pipeline](#__tabbed_26_1)
[Command Line](#__tabbed_26_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-classify-train.csv'        --> @dm:save              name = 'sample-classify-train'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'sample-classify-train' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/sample-classify-train.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_sample-classify-train)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| Summary | TEXT |     | FACT\_MultiPromoP2\_FO \| SAP \| Transaction is not reaching SAP |
| Issue key | TEXT |     | BISFTT2-5356 |
| Issue id | TEXT | Numerical | 748516 |
| Issue Type | TEXT |     | Bug |
| Status | TEXT |     | Closed |
| Project type | TEXT |     | software |
| Priority | TEXT |     | Blocker |
| Resolution | TEXT |     | Canceled |
| Creator | TEXT |     | AChawla3@ACME123.org |
| Created | TEXT | datetimestr | 2020-07-27 21:12:00 |
| Updated | TEXT | datetimestr | 2020-08-22 04:20:00 |

  
  

* * *

## Dataset: sample-cluster-predict

This Dataset has **998 Rows** and **2 Columns**

Download Data: [CSV Format](/data/datasets/sample-cluster-predict.csv)
 | [Parquet Format](/data/datasets/sample-cluster-predict.parquet)

View Data: [Table Format](/data/datasets/sample-cluster-predict.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-cluster-predict.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='sample-cluster-predict'`

[Pipeline](#__tabbed_27_1)
[Command Line](#__tabbed_27_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-cluster-predict.csv'        --> @dm:save              name = 'sample-cluster-predict'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'sample-cluster-predict' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/sample-cluster-predict.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_sample-cluster-predict)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| id  | TEXT |     | 26348437-eabb-4e10-abbc-668d9c4d238a |
| message | TEXT |     | Failed to send set\_hub to spooler (communication error) |

  
  

* * *

## Dataset: sample-cluster-train

This Dataset has **9,000 Rows** and **2 Columns**

Download Data: [CSV Format](/data/datasets/sample-cluster-train.csv)
 | [Parquet Format](/data/datasets/sample-cluster-train.parquet)

View Data: [Table Format](/data/datasets/sample-cluster-train.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-cluster-train.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='sample-cluster-train'`

[Pipeline](#__tabbed_28_1)
[Command Line](#__tabbed_28_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-cluster-train.csv'        --> @dm:save              name = 'sample-cluster-train'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'sample-cluster-train' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/sample-cluster-train.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_sample-cluster-train)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| id  | TEXT |     | 90acd4d4-5b7d-41ec-961a-d83adad83f8d |
| message | TEXT |     | NTP is not configured |

  
  

* * *

## Dataset: sample-ecommerce-data

This Dataset has **4,675 Rows** and **31 Columns**

Download Data: [CSV Format](/data/datasets/sample-ecommerce-data.csv)
 | [Parquet Format](/data/datasets/sample-ecommerce-data.parquet)

View Data: [Table Format](/data/datasets/sample-ecommerce-data.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-ecommerce-data.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='sample-ecommerce-data'`

[Pipeline](#__tabbed_29_1)
[Command Line](#__tabbed_29_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-ecommerce-data.csv'        --> @dm:save              name = 'sample-ecommerce-data'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'sample-ecommerce-data' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/sample-ecommerce-data.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_sample-ecommerce-data)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| \_id | TEXT |     | \--RJgHgBjfKVps-9kmsD |
| \_index | TEXT |     | kibana\_sample\_data\_ecommerce |
| \_type | TEXT |     | \_doc |
| category | TEXT |     | \["Women's Clothing", "Women's Accessories"\] |
| currency | TEXT |     | EUR |
| customer\_first\_name | TEXT |     | Elyssa |
| customer\_full\_name | TEXT |     | Elyssa Stokes |
| customer\_gender | TEXT |     | FEMALE |
| customer\_id | NUMERIC | Numerical | 27  |
| customer\_last\_name | TEXT |     | Stokes |
| customer\_phone | NUMERIC |     | None |
| day\_of\_week | TEXT |     | Monday |
| day\_of\_week\_i | NUMERIC | Numerical | 0   |
| email | TEXT |     | elyssa@stokes-family.zzz |
| geoip.city\_name | TEXT |     | New York |
| geoip.continent\_name | TEXT |     | North America |
| geoip.country\_iso\_code | TEXT |     | US  |
| geoip.location.lat | NUMERIC | Numerical | 40.8 |
| geoip.location.lon | NUMERIC | Numerical | \-74.0 |
| geoip.region\_name | TEXT |     | New York |
| manufacturer | TEXT |     | \['Pyramidustries', 'Tigress Enterprises', 'Gnomehouse'\] |
| order\_date | TEXT | datetimestr | 2021-04-05T22:19:12+00:00 |
| order\_id | NUMERIC | Numerical | 732884 |
| products | TEXT |     | \[{"base\_price": 28.99, "discount\_percentage": 0, "quantity": 1, "manufacturer": "Pyramidustries", "tax\_amount": 0, "product\_id": 16889, "category": "Women's Clothing", "sku": "ZO0177101771", "taxless\_price": 28.99, "unit\_discount\_amount": 0, "min\_price": 15.36, "\_id": "sold\_product\_732884\_16889", "discount\_amount": 0, "created\_on": "2016-12-19T22:19:12+00:00", "product\_name": "Jumper - rose", "price": 28.99, "taxful\_price": 28.99, "base\_unit\_price": 28.99}, {"base\_price": 32.99, "discount\_percentage": 0, "quantity": 1, "manufacturer": "Tigress Enterprises", "tax\_amount": 0, "product\_id": 24253, "category": "Women's Clothing", "sku": "ZO0071100711", "taxless\_price": 32.99, "unit\_discount\_amount": 0, "min\_price": 15.18, "\_id": "sold\_product\_732884\_24253", "discount\_amount": 0, "created\_on": "2016-12-19T22:19:12+00:00", "product\_name": "Cardigan - grey multicolor", "price": 32.99, "taxful\_price": 32.99, "base\_unit\_price": 32.99}, {"base\_price": 30.99, "discount\_percentage": 0, "quantity": 1, "manufacturer": "Pyramidustries", "tax\_amount": 0, "product\_id": 16894, "category": "Women's Accessories", "sku": "ZO0211402114", "taxless\_price": 30.99, "unit\_discount\_amount": 0, "min\_price": 14.88, "\_id": "sold\_product\_732884\_16894", "discount\_amount": 0, "created\_on": "2016-12-19T22:19:12+00:00", "product\_name": "Across body bag - cognac", "price": 30.99, "taxful\_price": 30.99, "base\_unit\_price": 30.99}, {"base\_price": 36.99, "discount\_percentage": 0, "quantity": 1, "manufacturer": "Gnomehouse", "tax\_amount": 0, "product\_id": 19778, "category": "Women's Clothing", "sku": "ZO0347503475", "taxless\_price": 36.99, "unit\_discount\_amount": 0, "min\_price": 17.02, "\_id": "sold\_product\_732884\_19778", "discount\_amount": 0, "created\_on": "2016-12-19T22:19:12+00:00", "product\_name": "Blouse - navy blazer", "price": 36.99, "taxful\_price": 36.99, "base\_unit\_price": 36.99}\] |
| sku | TEXT |     | \['ZO0177101771', 'ZO0071100711', 'ZO0211402114', 'ZO0347503475'\] |
| taxful\_total\_price | NUMERIC | Numerical | 129.96 |
| taxless\_total\_price | NUMERIC | Numerical | 129.96 |
| total\_quantity | NUMERIC | Numerical | 4   |
| total\_unique\_products | NUMERIC | Numerical | 4   |
| type | TEXT |     | order |
| user | TEXT |     | elyssa |

Pipelines using this Dataset

*   [sample-ecommerce-analytics](/Pipelines/sample-ecommerce-analytics/)
    

  
  

* * *

## Dataset: sample-ecommerce-data-with-pii

This Dataset has **4,675 Rows** and **32 Columns**

Download Data: [CSV Format](/data/datasets/sample-ecommerce-data-with-pii.csv)
 | [Parquet Format](/data/datasets/sample-ecommerce-data-with-pii.parquet)

View Data: [Table Format](/data/datasets/sample-ecommerce-data-with-pii.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-ecommerce-data-with-pii.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='sample-ecommerce-data-with-pii'`

[Pipeline](#__tabbed_30_1)
[Command Line](#__tabbed_30_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-ecommerce-data-with-pii.csv'        --> @dm:save              name = 'sample-ecommerce-data-with-pii'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'sample-ecommerce-data-with-pii' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/sample-ecommerce-data-with-pii.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_sample-ecommerce-data-with-pii)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| \_id | TEXT |     | \--RJgHgBjfKVps-9kmsD |
| \_index | TEXT |     | kibana\_sample\_data\_ecommerce |
| \_type | TEXT |     | \_doc |
| category | TEXT |     | \["Women's Clothing", "Women's Accessories"\] |
| currency | TEXT |     | EUR |
| customer\_first\_name | TEXT |     | Elyssa |
| customer\_full\_name | TEXT |     | Elyssa Stokes |
| customer\_gender | TEXT |     | FEMALE |
| customer\_id | NUMERIC | Numerical | 27  |
| customer\_last\_name | TEXT |     | Stokes |
| customer\_phone | NUMERIC |     | None |
| day\_of\_week | TEXT |     | Monday |
| day\_of\_week\_i | NUMERIC | Numerical | 0   |
| email | TEXT |     | elyssa@stokes-family.zzz |
| geoip.city\_name | TEXT |     | New York |
| geoip.continent\_name | TEXT |     | North America |
| geoip.country\_iso\_code | TEXT |     | US  |
| geoip.location.lat | NUMERIC | Numerical | 40.8 |
| geoip.location.lon | NUMERIC | Numerical | \-74.0 |
| geoip.region\_name | TEXT |     | New York |
| manufacturer | TEXT |     | \['Pyramidustries', 'Tigress Enterprises', 'Gnomehouse'\] |
| order\_date | TEXT | datetimestr | 2021-04-05T22:19:12+00:00 |
| order\_id | NUMERIC | Numerical | 732884 |
| products | TEXT |     | \[{"base\_price": 28.99, "discount\_percentage": 0, "quantity": 1, "manufacturer": "Pyramidustries", "tax\_amount": 0, "product\_id": 16889, "category": "Women's Clothing", "sku": "ZO0177101771", "taxless\_price": 28.99, "unit\_discount\_amount": 0, "min\_price": 15.36, "\_id": "sold\_product\_732884\_16889", "discount\_amount": 0, "created\_on": "2016-12-19T22:19:12+00:00", "product\_name": "Jumper - rose", "price": 28.99, "taxful\_price": 28.99, "base\_unit\_price": 28.99}, {"base\_price": 32.99, "discount\_percentage": 0, "quantity": 1, "manufacturer": "Tigress Enterprises", "tax\_amount": 0, "product\_id": 24253, "category": "Women's Clothing", "sku": "ZO0071100711", "taxless\_price": 32.99, "unit\_discount\_amount": 0, "min\_price": 15.18, "\_id": "sold\_product\_732884\_24253", "discount\_amount": 0, "created\_on": "2016-12-19T22:19:12+00:00", "product\_name": "Cardigan - grey multicolor", "price": 32.99, "taxful\_price": 32.99, "base\_unit\_price": 32.99}, {"base\_price": 30.99, "discount\_percentage": 0, "quantity": 1, "manufacturer": "Pyramidustries", "tax\_amount": 0, "product\_id": 16894, "category": "Women's Accessories", "sku": "ZO0211402114", "taxless\_price": 30.99, "unit\_discount\_amount": 0, "min\_price": 14.88, "\_id": "sold\_product\_732884\_16894", "discount\_amount": 0, "created\_on": "2016-12-19T22:19:12+00:00", "product\_name": "Across body bag - cognac", "price": 30.99, "taxful\_price": 30.99, "base\_unit\_price": 30.99}, {"base\_price": 36.99, "discount\_percentage": 0, "quantity": 1, "manufacturer": "Gnomehouse", "tax\_amount": 0, "product\_id": 19778, "category": "Women's Clothing", "sku": "ZO0347503475", "taxless\_price": 36.99, "unit\_discount\_amount": 0, "min\_price": 17.02, "\_id": "sold\_product\_732884\_19778", "discount\_amount": 0, "created\_on": "2016-12-19T22:19:12+00:00", "product\_name": "Blouse - navy blazer", "price": 36.99, "taxful\_price": 36.99, "base\_unit\_price": 36.99}\] |
| sku | TEXT |     | \['ZO0177101771', 'ZO0071100711', 'ZO0211402114', 'ZO0347503475'\] |
| taxful\_total\_price | NUMERIC | Numerical | 129.96 |
| taxless\_total\_price | NUMERIC | Numerical | 129.96 |
| total\_quantity | NUMERIC | Numerical | 4   |
| total\_unique\_products | NUMERIC | Numerical | 4   |
| type | TEXT |     | order |
| user | TEXT |     | elyssa |
| customer\_ssn | TEXT |     | 634-14-2181 |

  
  

* * *

## Dataset: sample-prometheus-timeseries-data

This Dataset has **5,763 Rows** and **3 Columns**

Download Data: [CSV Format](/data/datasets/sample-prometheus-timeseries-data.csv)
 | [Parquet Format](/data/datasets/sample-prometheus-timeseries-data.parquet)

View Data: [Table Format](/data/datasets/sample-prometheus-timeseries-data.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-prometheus-timeseries-data.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='sample-prometheus-timeseries-data'`

[Pipeline](#__tabbed_31_1)
[Command Line](#__tabbed_31_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-prometheus-timeseries-data.csv'        --> @dm:save              name = 'sample-prometheus-timeseries-data'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'sample-prometheus-timeseries-data' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/sample-prometheus-timeseries-data.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_sample-prometheus-timeseries-data)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| instance | TEXT |     | 10.95.125.90:9100 |
| timestamp | TEXT | datetimestr | 2022-02-19 14:38:45 |
| value | NUMERIC | Numerical | 2183816.0 |

  
  

* * *

## Dataset: sample-servicenow-incidents

This Dataset has **66 Rows** and **88 Columns**

Download Data: [CSV Format](/data/datasets/sample-servicenow-incidents.csv)
 | [Parquet Format](/data/datasets/sample-servicenow-incidents.parquet)

View Data: [Table Format](/data/datasets/sample-servicenow-incidents.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-servicenow-incidents.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='sample-servicenow-incidents'`

[Pipeline](#__tabbed_32_1)
[Command Line](#__tabbed_32_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/sample-servicenow-incidents.csv'        --> @dm:save              name = 'sample-servicenow-incidents'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'sample-servicenow-incidents' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/sample-servicenow-incidents.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_sample-servicenow-incidents)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| active | TEXT | Numerical | False |
| activity\_due | TEXT |     | 2016-12-12 17:26:36 |
| additional\_assignee\_list | NUMERIC |     | None |
| approval | TEXT |     | Not Yet Requested |
| approval\_history | NUMERIC |     | None |
| approval\_set | NUMERIC |     | None |
| assigned\_to | TEXT |     | David Loo |
| assignment\_group | TEXT |     | Network |
| business\_duration | TEXT |     | 8 Hours |
| business\_service | TEXT |     | Email |
| business\_stc | TEXT |     | 28,800 |
| calendar\_duration | TEXT |     | 1 Day 4 Hours 23 Minutes |
| calendar\_stc | TEXT |     | 102,197 |
| caller\_id | TEXT |     | Joe Employee |
| category | TEXT |     | Inquiry / Help |
| caused\_by | NUMERIC |     | None |
| child\_incidents | NUMERIC | Numerical | 0.0 |
| close\_code | TEXT |     | Solved (Permanently) |
| close\_notes | TEXT |     | This incident is resolved. |
| closed\_at | TEXT | datetimestr | 2016-12-13 18:46:44 |
| closed\_by | TEXT |     | Joe Employee |
| cmdb\_ci | TEXT |     | Storage Area Network 001 |
| comments | TEXT |     | 2016-12-13 12:30:14 - Joe Employee (Additional comments)  <br>Hi David,  <br>That must be it. I was on phone calls at all three of those times and must not have had any activity on my computer. Please close this incident.  <br>  <br>2016-12-13 10:42:25 - David Loo (Additional comments)  <br>Hi Joe,  <br>I've checked in network logs and you were timed out from the VPN at 9:25AM, 10:42AM and 2:28PM. These three times coincide with entries in the exchange server logs showing you lost connection at those same times. The VPN policy is to time out a connection if it hasn't been active in 30 minutes. Please ensure the next time you lose connectivity you are still connected to the VPN.  <br>  <br>I'm going to update this incident to resolved. Please let me know if you need any more assistance.  <br>  <br>2016-12-13 07:53:01 - Joe Employee (Additional comments)  <br>Hi David,  <br>Thank you! I use the corporate VPN and was also unable to connect to the email server at 9:30AM and 10:45AM.  <br>  <br>2016-12-13 06:43:17 - David Loo (Additional comments)  <br>Hi Joe,  <br>My name is David. I'll be assisting you with this incident. Can you confirm which VPN you have been using today? I also see you were having this issue at 2:30PM. Were there any other times you can recall you had issues connecting to the email?  <br>  <br>2016-12-12 16:56:57 - Beth Anglin (Additional comments)  <br>Hi Joe,  <br>As per discussion on call, Workaround has been provided and it has worked for you. I have verified with the Exchange team we haven't had an issue with the email server today. I'm going to assign this issue to the network team for further investigation.  <br>  <br>2016-12-12 12:43:50 - Joe Employee (Additional comments)  <br>Hi Beth,  <br>Yes, I'm connected to the VPN, although I've had to reconnect to it a couple of times. The last time I was unable to connect was 2:30PM.  <br>  <br>2016-12-12 10:52:42 - Beth Anglin (Additional comments)  <br>Hi Joe,  <br>Are you connected to the VPN when you're having this issue? Can you identify a specific time you were unable to connect to email?  <br>  <br>2016-12-12 08:30:49 - Beth Anglin (Additional comments)  <br>Hi Joe,  <br>My name is Beth and I'll be assisting you with your issue.  <br>  <br>2016-12-12 07:19:57 - Joe Employee (Additional comments)  <br>I am unable to connect to the email server. It appears to be down. |
| comments\_and\_work\_notes | TEXT |     | 2016-12-13 12:30:14 - Joe Employee (Additional comments)  <br>Hi David,  <br>That must be it. I was on phone calls at all three of those times and must not have had any activity on my computer. Please close this incident.  <br>  <br>2016-12-13 10:42:25 - David Loo (Additional comments)  <br>Hi Joe,  <br>I've checked in network logs and you were timed out from the VPN at 9:25AM, 10:42AM and 2:28PM. These three times coincide with entries in the exchange server logs showing you lost connection at those same times. The VPN policy is to time out a connection if it hasn't been active in 30 minutes. Please ensure the next time you lose connectivity you are still connected to the VPN.  <br>  <br>I'm going to update this incident to resolved. Please let me know if you need any more assistance.  <br>  <br>2016-12-13 07:53:01 - Joe Employee (Additional comments)  <br>Hi David,  <br>Thank you! I use the corporate VPN and was also unable to connect to the email server at 9:30AM and 10:45AM.  <br>  <br>2016-12-13 06:43:17 - David Loo (Additional comments)  <br>Hi Joe,  <br>My name is David. I'll be assisting you with this incident. Can you confirm which VPN you have been using today? I also see you were having this issue at 2:30PM. Were there any other times you can recall you had issues connecting to the email?  <br>  <br>2016-12-12 16:56:57 - Beth Anglin (Additional comments)  <br>Hi Joe,  <br>As per discussion on call, Workaround has been provided and it has worked for you. I have verified with the Exchange team we haven't had an issue with the email server today. I'm going to assign this issue to the network team for further investigation.  <br>  <br>2016-12-12 16:56:57 - Beth Anglin (Work notes)  <br>Updating priority as workaround for incident has been provided.  <br>  <br>2016-12-12 12:43:50 - Joe Employee (Additional comments)  <br>Hi Beth,  <br>Yes, I'm connected to the VPN, although I've had to reconnect to it a couple of times. The last time I was unable to connect was 2:30PM.  <br>  <br>2016-12-12 10:52:42 - Beth Anglin (Additional comments)  <br>Hi Joe,  <br>Are you connected to the VPN when you're having this issue? Can you identify a specific time you were unable to connect to email?  <br>  <br>2016-12-12 09:57:00 - Beth Anglin (Work notes)  <br>Increasing priority as this incident is affecting more number of users  <br>  <br>2016-12-12 09:01:24 - Beth Anglin (Work notes)  <br>Updating incident with correct Configuration item  <br>  <br>2016-12-12 08:30:49 - Beth Anglin (Additional comments)  <br>Hi Joe,  <br>My name is Beth and I'll be assisting you with your issue.  <br>  <br>2016-12-12 07:19:57 - Joe Employee (Additional comments)  <br>I am unable to connect to the email server. It appears to be down. |
| company | TEXT |     | ACME North America |
| contact\_type | TEXT |     | Self-service |
| contract | NUMERIC |     | None |
| correlation\_display | NUMERIC |     | None |
| correlation\_id | NUMERIC |     | None |
| delivery\_plan | NUMERIC |     | None |
| delivery\_task | NUMERIC |     | None |
| description | TEXT |     | I am unable to connect to the email server. It appears to be down. |
| due\_date | NUMERIC |     | None |
| escalation | TEXT |     | Normal |
| expected\_start | NUMERIC |     | None |
| follow\_up | NUMERIC |     | None |
| group\_list | NUMERIC |     | None |
| hold\_reason | TEXT |     | Awaiting Caller |
| impact | TEXT |     | 2 - Medium |
| incident\_state | TEXT |     | Closed |
| knowledge | TEXT | Numerical | False |
| location | TEXT |     | San Diego |
| made\_sla | TEXT | Numerical | True |
| notify | TEXT |     | Do Not Notify |
| number | TEXT |     | INC0000060 |
| opened\_at | TEXT | datetimestr | 2016-12-12 07:19:57 |
| opened\_by | TEXT |     | Joe Employee |
| order | NUMERIC |     | None |
| parent | NUMERIC |     | None |
| parent\_incident | TEXT |     | INC0007001 |
| priority | TEXT |     | 3 - Moderate |
| problem\_id | TEXT |     | PRB0000008 |
| reassignment\_count | NUMERIC | Numerical | 2.0 |
| reopen\_count | NUMERIC | Numerical | 0.0 |
| reopened\_by | NUMERIC |     | None |
| reopened\_time | NUMERIC |     | None |
| resolved\_at | TEXT | datetimestr | 2016-12-13 13:43:14 |
| resolved\_by | TEXT |     | David Loo |
| rfc | NUMERIC |     | None |
| route\_reason | NUMERIC |     | None |
| service\_offering | NUMERIC |     | None |
| severity | TEXT |     | 3 - Low |
| short\_description | TEXT |     | Unable to connect to email |
| sla\_due | TEXT |     | UNKNOWN |
| state | TEXT |     | Closed |
| subcategory | TEXT |     | Email |
| sys\_class\_name | TEXT |     | Incident |
| sys\_created\_by | TEXT |     | employee |
| sys\_created\_on | TEXT | datetimestr | 2016-12-12 07:19:57 |
| sys\_domain | TEXT |     | global |
| sys\_domain\_path | TEXT |     | /   |
| sys\_id | TEXT |     | 1c741bd70b2322007518478d83673af3 |
| sys\_mod\_count | NUMERIC | Numerical | 15  |
| sys\_tags | NUMERIC |     | None |
| sys\_updated\_by | TEXT |     | employee |
| sys\_updated\_on | TEXT | datetimestr | 2016-12-13 18:46:44 |
| task\_effective\_number | TEXT |     | INC0000060 |
| time\_worked | NUMERIC |     | None |
| universal\_request | NUMERIC |     | None |
| upon\_approval | TEXT |     | Proceed to Next Task |
| upon\_reject | TEXT |     | Cancel all future Tasks |
| urgency | TEXT |     | 2 - Medium |
| user\_input | NUMERIC |     | None |
| watch\_list | NUMERIC |     | None |
| work\_end | NUMERIC |     | None |
| work\_notes | TEXT |     | 2016-12-12 16:56:57 - Beth Anglin (Work notes)  <br>Updating priority as workaround for incident has been provided.  <br>  <br>2016-12-12 09:57:00 - Beth Anglin (Work notes)  <br>Increasing priority as this incident is affecting more number of users  <br>  <br>2016-12-12 09:01:24 - Beth Anglin (Work notes)  <br>Updating incident with correct Configuration item |
| work\_notes\_list | NUMERIC |     | None |
| work\_start | NUMERIC |     | None |

Pipelines using this Dataset

*   [sample-formatting-template-example](/Pipelines/sample-formatting-template-example/)
    
*   [sample-incident-analytics](/Pipelines/sample-incident-analytics/)
    
*   [sample-incident-clustering](/Pipelines/sample-incident-clustering/)
    

  
  

* * *

## Dataset: synthetic\_syslogs\_dataset

This Dataset has **10,000 Rows** and **2 Columns**

Download Data: [CSV Format](/data/datasets/synthetic_syslogs_dataset.csv)
 | [Parquet Format](/data/datasets/synthetic_syslogs_dataset.parquet)

View Data: [Table Format](/data/datasets/synthetic_syslogs_dataset.html)

To access the dataset in RDA pipeline without converting into a RDA Dataset, you can use this in your pipeline

  `@files:loadfile         filename = 'https://bot-docs.cloudfabrix.io/data/datasets/synthetic_syslogs_dataset.csv'`

Following snippet can be used to load the data as a dataset in your RDA Fabric. Once data is loaded, you can simply use `@dm:recall name='synthetic_syslogs_dataset'`

[Pipeline](#__tabbed_33_1)
[Command Line](#__tabbed_33_2)


```
@files:loadfile             filename = 'https://bot-docs.cloudfabrix.io/data/datasets/synthetic_syslogs_dataset.csv'        --> @dm:save              name = 'synthetic_syslogs_dataset'
```


```
# See 'RDA CLI' guide for instructions to install RDA CLI Tool python3 rdac.py dataset-add \               --name 'synthetic_syslogs_dataset' \               --file 'https://bot-docs.cloudfabrix.io/data/datasets/synthetic_syslogs_dataset.csv'
```

Playground

[Try this in RDA Playground](https://cfxplayground.cloudfabrix.io/rdac/playground/home?snippet=dataset_synthetic_syslogs_dataset)

  

Data Model

| Column | Data Type | Detected Content Type | Sample Value |
| --- | --- | --- | --- |
| device | TEXT |     | 10.10.131.56 |
| message | TEXT |     | %ETHPORT-5-IF\_RX\_FLOW\_CONTROL: Interface Ethernet1/21, operational Receive Flow Control state changed to off |

Pipelines using this Dataset

*   [dli-generate-synthetic-syslogs](/Pipelines/dli-generate-synthetic-syslogs/)
    

  
  

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!