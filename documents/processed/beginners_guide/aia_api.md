 



# RDAF Platform's Asset Intelligence and Analytics (AIA) / Operations Intelligence & Analytics (OIA) RESTful APIs

## 1\. Query the inventory data using RESTful APIs

In RDAF platform, users can use its RESTful API interface to query and get the inventory data from AIA/OIA application. The queried inventory data can be processed for reporting or by the downstream systems.

APIs are RESTful based, supports both GET and POST API calls to RDAF platform, authenticating each request by providing a HTTP **Authentication** header and **Bearer** access token.

Follow the below instructions to generate an API access token, which will be used for authentication while accessing the APIs.

### **1.1** ****API Access Token****

Login into **RDAF UI portal**

![AIA_API Login](https://bot-docs.cloudfabrix.io/images/aia_api/login_page.png)

****API Authentication****

After login into the RDAF UI Portal, click on action icon at the top right corner as shown in the below screen shot go to **My Account** and then on the left side user can find the **Api Access Key** Option.

[![Api Access Key](https://bot-docs.cloudfabrix.io/images/aia_api/api_access_key.png)](/images/aia_api/api_access_key.png)

Click on the **API Access Key** menu and click on **Copy to Clipboard** to copy the **API Access Token**

[![Api Access Token](https://bot-docs.cloudfabrix.io/images/aia_api/api_access_token1.png)](/images/aia_api/api_access_token1.png)

### **1.2** ****Query Inventory data from Pstreams****

`invokeAPI` is the parent API call which supports below two methods to query and get the inventory data.

**queryPstream** - API method to query inventory data from a specified persistent stream that has completely processed inventory data. (Please refer [Persistent Streams](https://bot-docs.cloudfabrix.io/beginners_guide/data_at_rest/?h=pers#7-persistent-streams)
 for more information.)

Tip

AIA/OIA application uses persistent streams with RDAF platform to store the inventory data which is used for dashboard reports and analytics.

*   `invokeAPI` API Request URL
```
 https://<rdaf-aia-platform-ip-address>/api/portal/rdac/invokeAPI

```

Below example provides a sample API request to query the network devices inventory data from persistent stream `aia_network`.

Tip

Users need to copy/store the Bearer token given in the below sample API request from the above 'API Authentication' section

[Sample API Request](#__tabbed_1_1)
```
 curl -k --location --request POST 'https://192.168.108.94/api/portal/rdac/invokeAPI' \ 
 --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTVjYTY2OWEtOTA3My00ZDIwLTgzNTktNDYyNzNiNTEyYmE4IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4Ljk0Ojg4MDgifQ.B64zQTANAqP0InVE6xQl4O5zBx65U51y4M8xosA_6ZY' \ 
 --header 'Content-Type: application/json' \ 
 --data '{ 
     "serviceRequestDescriptor": { 
         "serviceName": "saas-reports", 
         "params": { 
             "params": [ 
                 { 
                     "name": "aia_network", 
                     "max_rows": 2, 
                     "query": "*" 
                 } 
             ] 
         }, 
         "methodName": "queryPstream" 
     } 
 }'

```

| Parameter Name | Description |
| --- | --- |
| serviceName | Name of the service for API request, ex: `saas-reports` |
| params | JSON object with list of API request parameters |
| methodName | Name of the API i.e. `queryPstream` |

**API Request Parameters**

| Parameter | Required | Type | Default value | Description |
| --- | --- | --- | --- | --- |
| name | yes | string |     | Name of the persistent stream to query |
| query | yes | string |     | Provide [CFXQL Query](https://bot-docs.cloudfabrix.io/reference_guides/cfxql/?h=cfxql)<br> to filter the data from the selected persistent stream. To include all of the records, specify the filter as `*` |
| max\_rows | no  | integer | 1000 | API response is paginated. By default each API response limits the number of records to 1000. max supported value is `1000` |
| last\_sort\_results | no  | integer |     | Provides array of values, use these to query next batch of results in the subsequent API and iterate through till the end of the results. |
| sorting | no  | list | Default Sort based on unique keys of Persistent Stream | List of json objects, to sort based on column values and order (ascending / descending) |

*   In **AIA/OIA application**, processed asset inventory data is persisted within the below provided persistent streams.

| Persistent Stream Name | Description |
| --- | --- |
| aia\_network | Asset inventory of network device's `chassis` and sub-component details such as `modules`, `power supplies` etc. |
| aia\_cdp | Asset inventory with `cdp` and `lldp` neighbors data |
| aia\_interface | Asset inventory of network device's interface data |
| aia\_por | Asset inventory of network and other devices with applied `POR` (plan of record) details. |
| aia\_adm | Asset inventory of network devices, connected end-points and application dependency mapping (ADM) details. |
| aia\_iptelephony | Asset inventory of Unified communication device(s) details. |
| oia-alerts-stream | OIA alerts data |
| oia-incidents-stream | OIA incidents data |

[Sample API Response](#__tabbed_2_1)
```
 { 
     "completed": "2022-12-27T08:21:04.808489", 
     "created": "2022-12-27T08:21:04.632261", 
     "serviceError": "none", 
     "serviceResult": { 
         "data": { 
             "hasMoreResults": true, 
             "last_sort_results": [ 
                 1672124935913, 
                 "4fe522a4590115b807844edcc82c88de" 
             ], 
             "offset": null, 
             "results": [ 
                 { 
                     "__mode": "AUTO", 
                     "__rma_new_sn__": "Not Available", 
                     "__rma_old_sn__": "Not Available", 
                     "__state": "ACTIVE", 
                     "__state_updated_time": 1672124308000.0, 
                     "_id": "31affbe3a9b62da78a676b744e2a7319", 
                     "_index": "51f9a6e0711142939f953bec78d7e7bb-stream-2dec0fc9-aia_network-replace-90bafdd7", 
                     "_score": null, 
                     "address": "Not Available", 
                     "admin_down_eth_ports": 125, 
                     "api_status": "Not Applicable", 
                     "apic_node_dn": "Not Applicable", 
                     "apic_pod_id": "Not Applicable", 
                     "apic_role": "Not Applicable", 
                     "asset_id": "e42f38259c3441ca4ae05914144ac23f", 
                     "asset_type": "Hardware", 
                     "bucket_id": "21e31d728718dc98054d6839b124445c", 
                     "cafm_code": "AB22-05", 
                     "cdp_global_deviceId": "dcaabcs14001-2AX52.acme.org(FGE29017ABC)", 
                     "child_devices": 0, 
                     "city": "Pleasanton", 
                     "closet_Id": "RAISEDFLOOR", 
                     "contract_coverage": "Not Available", 
                     "count_": 1, 
                     "country": "Not Available", 
                     "created_time": 1672124323000.0, 
                     "customer_acceptable_sw_version": "Not Available", 
                     "customer_approved_sw_version": "7.0(3)I7(8)", 
                     "customer_category": "DC Fabric LAN", 
                     "customer_certified_replacement": "Not Available", 
                     "customer_equipment_type": "Zone Service Switch", 
                     "customer_por_generation": "N", 
                     "customer_por_generation_Exec": "N", 
                     "customer_topological_tier": "LAN Device", 
                     "customer_zone": "14", 
                     "device_additional_ips": "192.168.188.2,192.168.50.1,", 
                     "device_family_engr": "9508", 
                     "device_family_exec": "9508", 
                     "device_role": "AGGREGATE", 
                     "dns_name": "dcaabcs14001-mgmt.acme.org", 
                     "dot1x_sw_support": "Not Applicable", 
                     "dot1x_system": "Not Applicable", 
                     "down_eth_ports": 140, 
                     "down_ports_categorization": "9+", 
                     "equipment_age": "Not Available", 
                     "equipment_name": "N9K-C9508", 
                     "equipment_type": "CHASSIS", 
                     "fex_description": "Not Available", 
                     "fex_grid": "Not Available", 
                     "fex_model": "Not Available", 
                     "fex_name": "Not Available", 
                     "fex_number": "Not Available", 
                     "fex_serial": "Not Available", 
                     "fex_state": "Not Available", 
                     "first_seen": 1672026693000.0, 
                     "floor_Id": 2, 
                     "grid_Id": "2AX52", 
                     "hostname": "dcaabcs14001-2AX52", 
                     "hw_expiring_qtr": "Not Available", 
                     "hw_expiring_year": "Not Available", 
                     "hw_ldos_string": "No EOL", 
                     "hw_revision": "Missing HW Revision", 
                     "hw_status": "No EOL", 
                     "ip_address": "192.168..163.228", 
                     "is_parent": "Yes", 
                     "is_poe_capable": "No", 
                     "last_qtr_of_support": "Not Available", 
                     "last_seen": 1672026693000.0, 
                     "last_updated_time": 1672124324000.0, 
                     "last_year_of_support": "Not Available", 
                     "latitude": 0.0, 
                     "longitude": 0.0, 
                     "mgmt_ip": "192.168.163.228", 
                     "ntwk_license_name": "Not Available", 
                     "org_id": "c1048ac6-0442-4cd5-a39c-1a98ef2cf1c4", 
                     "org_name": "ACME", 
                     "original_pid": "N9K-C9508-B3-E", 
                     "parent_pid": "N9K-C9508", 
                     "parent_sn": "FGE22789TXV", 
                     "poe_admin_auto": 0, 
                     "poe_admin_off": 0, 
                     "poe_admin_static": 0, 
                     "poe_oper_faulty": 0, 
                     "poe_oper_off": 0, 
                     "poe_oper_on": 0, 
                     "poe_oper_power_deny": 0, 
                     "poe_remaining_watts": 0, 
                     "poe_summary": "Not Available", 
                     "poe_total_watts": 0, 
                     "poe_used_watts": 0, 
                     "postal_code": 94558.0, 
                     "price": 0.0, 
                     "product_category": "Switches", 
                     "product_description": "Nexus 9508 Chassis Bundle with 1Sup, 3 PS, 2SC, 4 FM-E, 3Fan", 
                     "product_family": "Cisco Nexus 9000 Series Switches", 
                     "product_id": "N9K-C9508-B3-E", 
                     "product_name": "Cisco Nexus 9508 Switch", 
                     "product_type": "SWITCH", 
                     "province": "Missing Province", 
                     "region": "CN", 
                     "replacement_cost": 0.0, 
                     "replacement_part_description": "Not Available", 
                     "replacement_part_id": "Not Available", 
                     "serial_num": "FGE22678TXV", 
                     "shipped_city": "Pleasanton", 
                     "site": "AB22-05|02|RAISEDFLOOR|2AX52|4301 Hacienda Dr.|Pleasanton|CA|94558", 
                     "site_code": "ABC", 
                     "site_details": "Not Available", 
                     "site_id": "Not Available", 
                     "site_name": "Not Available", 
                     "site_type": "Data Center", 
                     "site_zone": "ABC-Zone 14(M) - Service", 
                     "snmp_syslocation": "AB22-05|02|RAISEDFLOOR|2AX52|4301 Hacienda Dr.|Pleasanton|CA|94558", 
                     "sort": [ 
                         1672124935913, 
                         "31affbe3a9b62da78a676b744e2a7319" 
                     ], 
                     "source_filename": "acme_consolidated_exportdata_12M26D2022Y_5h30m.zip", 
                     "state": "California", 
                     "state_code": "CA", 
                     "sw_expiring_qtr": "Not Available", 
                     "sw_expiring_year": "Not Available", 
                     "sw_por": "N (Current Standard)", 
                     "sw_status": "Not Available", 
                     "sw_type": "Cisco NX-OS", 
                     "sw_version": "7.0(3)I7(8)", 
                     "sw_version_details": "RELEASE SOFTWARE", 
                     "sys_contact": "VNOC 866-457-4329", 
                     "sys_descr": "Cisco NX-OS(tm) nxos.7.0.3.I7.8.bin, Software (nxos), Version 7.0(3)I7(8), RELEASE SOFTWARE Copyright (c) 2002-2020 by Cisco Systems, Inc. Compiled 3/3/2020 19:00:00", 
                     "sys_objectId": "1.3.6.1.4.1.9.12.3.1.3.1467", 
                     "sys_uptime": 193.0, 
                     "sys_uptime_days": ">180", 
                     "system_vendor_os": "Cisco NX-OS", 
                     "system_vendor_sub_id": "12.3.1.3.1467", 
                     "timestamp": "2022-12-27T07:08:55.913324", 
                     "total_eth_ports": 769, 
                     "up_eth_ports": 629, 
                     "up_ports_categorization": "6+", 
                     "uptime": 193, 
                     "uptime_since": 1655449096135.0, 
                     "vendor": "Cisco", 
                     "vpc_dns": "Not Available", 
                     "vpc_peer_device_ip": "10.0.0.2", 
                     "zone_alias_name": "Acme 14(M) - Service" 
                 }, 
                 { 
                     ... 
                     ... 
                 } 
             ], 
             "results_count": 2, 
             "totalResults": 11581 
         }, 
         "now": "2022-12-27T08:21:04.775442", 
         "reason": "", 
         "status": "ok" 
     } 
 }

```

*   The `last_sort_results` parameter

The response contains the **last\_sort\_results** array of values in data of `serviceResult` for each API query, as shown in above sample API response. Use the **last\_sort\_results** parameter's values from last API response to get next batch of records.

[Sample API Request with last\_sort\_results Parameter](#__tabbed_3_1)
```
 curl -k --location --request POST 'https://192.168.108.94/api/portal/rdac/invokeAPI' \ 
 --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTVjYTY2OWEtOTA3My00ZDIwLTgzNTktNDYyNzNiNTEyYmE4IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4Ljk0Ojg4MDgifQ.B64zQTANAqP0InVE6xQl4O5zBx65U51y4M8xosA_6ZY' \ 
 --header 'Content-Type: application/json' \ 
 --data '{ 
     "serviceRequestDescriptor": { 
         "serviceName": "saas-reports", 
         "params": { 
             "params": [ 
                 { 
                     "name": "aia_network", 
                     "max_rows": 2, 
                     "query": "*", 
                     "last_sort_results": [ 
                 1670392980290, 
                 "288b473baa5b1d47006f7b313b336f3e" 
             ] 
                 } 
             ] 
         }, 
         "methodName": "queryPstream" 
     } 
 }'

```

[Sample API Response](#__tabbed_4_1)
```
 { 
     "completed": "2022-12-27T08:23:15.977406", 
     "created": "2022-12-27T08:23:15.803026", 
     "serviceError": "none", 
     "serviceResult": { 
         "data": { 
             "hasMoreResults": true, 
             "last_sort_results": [ 
                 1672124935912, 
                 "784e454047da8ce16470324a6bc928ce" 
             ], 
             "offset": null, 
             "results": [ 
                 { 
                     "__mode": "AUTO", 
                     "__rma_new_sn__": "Not Available", 
                     "__rma_old_sn__": "Not Available", 
                     "__state": "ACTIVE", 
                     "__state_updated_time": 1672124308000.0, 
                     "_id": "62dc08304dc88fcaebce473e3b7ad5e5", 
                     "_index": "51f9a6e0711142939f953bec78d7e7bb-stream-2dec0fc9-aia_network-replace-90bafdd7", 
                     "_score": null, 
                     "address": "Not Available", 
                     "admin_down_eth_ports": 0, 
                     "api_status": "Success", 
                     "apic_node_dn": "Not Applicable", 
                     "apic_pod_id": "Not Applicable", 
                     "apic_role": "Not Applicable", 
                     "asset_id": "ca01f634b4d80ec5d228e7af52afbacb", 
                     "asset_type": "Hardware", 
                     "bucket_id": "fbe95cc8ed6629939349dd26d6d7f4c5", 
                     "cafm_code": "AB22-05", 
                     "cdp_global_deviceId": "ACMEABCP41908.acme.org(FDO24789AFG)", 
                     "child_devices": 0, 
                     "city": "Pleasanton", 
                     "closet_Id": "RaisedFloor", 
                     "customer_equipment_type": "Acme Production Switch", 
                     "customer_por_generation": "N", 
                     "customer_por_generation_Exec": "N", 
                     ... 
                     ... 
                     "uptime": 388, 
                     "uptime_since": 1638601096076.0, 
                     "vendor": "Cisco", 
                     "vpc_dns": "Not Available", 
                     "vpc_peer_device_ip": "Not Available", 
                     "zone_alias_name": "Acme 10(I) - MSP" 
                 }, 
                 { 
                     ... 
                     ... 
                 } 
             ], 
             "results_count": 2, 
             "totalResults": 11581 
         }, 
         "now": "2022-12-27T08:23:15.951970", 
         "reason": "", 
         "status": "ok" 
     } 
 }

```

[Sample queryPstream API response with results\_count and totalResults parameters](#__tabbed_5_1)

API response contains results\_count and totalResults values in "data" of serviceResult, results\_count represents the number of records that are in the current response data, and totalResults is the total number of records for a given API query (of that persistent stream).
```
 { 
     "completed": "2022-12-27T08:21:04.808489", 
     "created": "2022-12-27T08:21:04.632261", 
     "serviceError": "none", 
     "serviceResult": { 
         "data": { 
             "hasMoreResults": true, 
             "last_sort_results": [ 
                 1672124935913, 
                 "4fe522a4590115b807844edcc82c88de" 
             ], 
             "offset": null, 
             "results": [  
               { 
                     ... 
                     ... 
                 } 
             ], 
             "results_count": 2, 
             "totalResults": 11581 
         }, 
         "now": "2022-12-27T08:21:04.775442", 
         "reason": "", 
         "status": "ok" 
     }

```

Note

For given query, If results\_count in response has less than max\_rows provided or 0 then it means the end of the query results.

**Applying CFXQL query to filter the data:**

Below is a sample API request to query the inventory data of network device using CFXQL query to filter the data.
```
 curl -k --location --request POST 'https://192.168.108.94/api/portal/rdac/invokeAPI' \ 
 --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTVjYTY2OWEtOTA3My00ZDIwLTgzNTktNDYyNzNiNTEyYmE4IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4Ljk0Ojg4MDgifQ.B64zQTANAqP0InVE6xQl4O5zBx65U51y4M8xosA_6ZY' \ 
 --header 'Content-Type: application/json' \ 
 --data '{ 
     "serviceRequestDescriptor": { 
         "serviceName": "saas-reports", 
         "params": { 
             "params": [ 
                 { 
                     "name": "aia_network", 
                     "max_rows": 2, 
                     "query": "ip_address ~ '\''192.168.230'\''", 
                     "last_sort_results": [ 
                 1670392980290, 
                 "288b473baa5b1d47006f7b313b336f3e" 
             ] 
                 } 
             ] 
         }, 
         "methodName": "queryPstream" 
     } 
 }'

```

**Applying Sorting on Columns:**

Below is a sample API request to query the inventory data using Sorting on Columns serial\_num and parent\_sn in ascending order.
```
 curl -k --location --request POST 'https://192.168.108.94/api/portal/rdac/invokeAPI' \ 
 --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTVjYTY2OWEtOTA3My00ZDIwLTgzNTktNDYyNzNiNTEyYmE4IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4Ljk0Ojg4MDgifQ.B64zQTANAqP0InVE6xQl4O5zBx65U51y4M8xosA_6ZY' \ 
 --header 'Content-Type: application/json' \ 
 --data '{ 
     "serviceRequestDescriptor": { 
         "serviceName": "saas-reports", 
         "params": { 
             "params": [ 
                 { 
                     "name": "aia_network", 
                     "max_rows": 500, 
                     "query": "*", 
                     "sorting": [{"serial_num.keyword": "asc"}, {"parent_sn.keyword": "asc"}] 
                 } 
             ] 
         }, 
         "methodName": "queryPstream" 
     } 
 }'

```

Note

Add ‘.keyword’ to columns if column type is text, “asc” for ascending order and “desc” for descending order

Below is a sample Request to query incidents data from oia-incidents-stream Persistent Stream
```
 curl -k --location 'https:///192.168.108.94/api/portal/rdac/invokeAPI' \ 
 --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTVjYTY2OWEtOTA3My00ZDIwLTgzNTktNDYyNzNiNTEyYmE4IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4Ljk0Ojg4MDgifQ.B64zQTANAqP0InVE6xQl4O5zBx65U51y4M8xosA_6ZY' \ 
 --header 'Content-Type: application/json' \ 
 --header 'Cookie: __cfxsession=7be65841-1d40-45ae-95ee-1fb98a600ace; rdafportal=rdaf-portal-1|ZAN/9|ZAN/9' \ 
 --data '{ 
     "serviceRequestDescriptor": { 
         "serviceName": "saas-reports", 
         "params": { 
             "params": [ 
                 { 
                     "name": "oia-incidents-stream", 
                     "max_rows": 20, 
                     "query": "*" 
                 } 
             ] 
         }, 
         "methodName": "queryPstream" 
     } 
 }'

```

Below is a sample Request to query alerts data from oia-alerts-stream Persistent Stream with filter a\_status is 'ACTIVE'
```
 curl -k --location 'https://192.168.108.94/api/portal/rdac/invokeAPI' \ 
 --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTVjYTY2OWEtOTA3My00ZDIwLTgzNTktNDYyNzNiNTEyYmE4IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4Ljk0Ojg4MDgifQ.B64zQTANAqP0InVE6xQl4O5zBx65U51y4M8xosA_6ZY' \ 
 --header 'Content-Type: application/json' \ 
 --header 'Cookie: __cfxsession=7be65841-1d40-45ae-95ee-1fb98a600ace; rdafportal=rdaf-portal-1|ZAOAv|ZAN/9' \ 
 --data '{ 
     "serviceRequestDescriptor": { 
         "serviceName": "saas-reports", 
         "params": { 
             "params": [ 
                 { 
                     "name": "oia-alerts-stream", 
                     "max_rows": 20, 
                     "query": "a_status is 'ACTIVE'" 
                 } 
             ] 
         }, 
         "methodName": "queryPstream" 
     } 
 }'

```

### **1.3** ****Query Inventory data from UI reports****

**getReport** - API method to query the asset inventory data from a given UI widget report within the selected Dashboard.

*   `invokeAPI` **API request URL**
```
 https://<rdaf-aia-platform-ip-address>/api/portal/rdac/invokeAPI

```

[Sample getReport API Request](#__tabbed_6_1)
```
 curl -k --location --request POST 'https://192.168.103.40/api/portal/rdac/invokeAPI' \ 
 --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYjNkN2ExNDQtNDc3NC00MTEwLWEwMzEtZjFmMDhiYTRjYjhiIiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjkwOjg4MDgifQ.cyiMb2Kpi6FDGE8OHIV0zuB4RnK-vy9cbT_ByTeltzA' \ 
 --header 'Content-Type: application/json' \ 
 --data '{ 
     "serviceRequestDescriptor": { 
         "serviceName": "saas-reports", 
         "params": { 
             "params": [ 
                 { 
                     "context": { 
                         "contextInfo": { 
                             "contextIdList": [] 
                         }, 
                         "id": "user-dashboard-aia-network-assetslist", 
                         "name": "aia-network-assetslist", 
                         "view-context": { 
                             "appName": "user-dashboard", 
                             "pageName": "aia-network-assetslist" 
                         } 
                     }, 
                     "dashboardId": "Total Assets Details", 
                     "reportId": "dynamic_v2_tabular_report_0_0", 
                     "properties": {"offset": 0, "maxResults": 2}, 
                     "filters": [] 
                 }]}, 
                 "methodName": "getReport" 
             }}'

```

| Parameter Name | Description |
| --- | --- |
| serviceName | Name of the service for API request, ex: `saas-reports` |
| params | JSON object with list of API request parameters |
| methodName | Name of the API i.e. `getReport` |

**API Request Parameters**

| Parameter | Required | Type | Default value | Description |
| --- | --- | --- | --- | --- |
| context | yes | object |     | Report context details |
| dashboardId | yes | string |     | Unique identifier of user's dashboard |
| reportId | yes | string |     | Unique identifier of a widget / chart within the dashboard |
| filters | no  | list | \[\] | Filters to apply |
| properties | no  | Json object | {}  | To Specify `maxResults` and `last_sort_results` max supported value for `maxResults` is `1000` |

**getReport** API needs id, name, pageName, dashboardId and reportId details as inputs, These values are based on the page where the report resides in UI. Below table gives these details for different reports.

| Report Name | pageName | dashboardId | reportId | appName | id  |
| --- | --- | --- | --- | --- | --- |
| Assets Details | aia-network-assetslist | Total Assets Details | dynamic\_v2\_tabular\_report\_0\_0 | user-dashboard | user-dashboard-aia-network-assetslis |
| Dependent Application Details | aia-adm | ADM Device Details | dynamic\_v2\_tabular\_report\_0\_0 | user-dashboard | user-dashboard-aia-adm |
| CDP Neighbors | aia-network-assetslist | CDP Neighbor Assets | dynamic\_v2\_tabular\_report\_0\_0 | user-dashboard | user-dashboard-aia-network-assetslist |
| IPT Details | aia-ipt-assetslist | IPT Total Assets | dynamic\_v2\_tabular\_report\_0\_0 | user-dashboard | user-dashboard-aia-ipt-assetslist |
| Interfaces Details | aia-network-hardware | Hardware Assets Utilization | dynamic\_v2\_tabular\_report\_0\_25 | user-dashboard | user-dashboard-aia-network-hardware |
| Incidents | oia-incidents-os-template | incidents | dynamic\_v2\_tabular\_report\_0\_0 | user-dashboard | user-dashboard-oia-incidents-os-template |
| Alerts | oia-alerts-os | alerts | dynamic\_v2\_tabular\_report\_0\_0 | user-dashboard | user-dashboard-oia-alerts-os |

Note

**getReport** API is equivalent to old **[getChartData\_v1](https://docs.cloudfabrix.io/cfx-aia/aia-api#native-restful-apis-to-get-inventory-data)
** API for fetching the inventory data from a report in AIA

[Sample getReport API Response](#__tabbed_7_1)
```
 { 
     "completed": "2022-12-27T08:27:14.119707", 
     "created": "2022-12-27T08:27:13.785768", 
     "serviceError": "none", 
     "serviceResult": { 
         "dataResults": [ 
             { 
                 "__mode": "AUTO", 
                 "__rma_new_sn__": "Not Available", 
                 "__rma_old_sn__": "Not Available", 
                 "__state": "ACTIVE", 
                 "__state_updated_time": "12/27/2022 06:58:28 AM ", 
                 "address": "Not Available", 
                 "admin_down_eth_ports": 125, 
                 "api_status": "Not Applicable", 
                 "apic_node_dn": "Not Applicable", 
                 "apic_pod_id": "Not Applicable", 
                 "apic_role": "Not Applicable", 
                 "asset_id": "e42f38259c3441ca4ae05914144ac23f", 
                 "asset_type": "Hardware", 
                 "bucket_id": "21e31d728718dc98054d6839b124445c", 
                 "cafm_code": "AB22-05", 
                 "cdp_global_deviceId": "lcaabcs14001-2AX52.acme.org(FGE29017ABC)", 
                 "child_devices": 0, 
                 "city": "Pleasanton", 
                 "closet_Id": "RAISEDFLOOR", 
                 "contract_coverage": "Not Available", 
                 "count_": 1, 
                 "country": "Not Available", 
                 "created_time": "12/27/2022 06:58:43 AM ", 
                 "customer_acceptable_sw_version": "Not Available", 
                 "customer_approved_sw_version": "7.0(3)I7(8)", 
                 "customer_category": "DC Fabric LAN", 
                 "customer_certified_replacement": "Not Available", 
                 "customer_equipment_type": "Acme Service Switch", 
                 "customer_por_generation": "N", 
                 "customer_por_generation_Exec": "N", 
                 "customer_topological_tier": "LAN Device", 
                 "customer_zone": "14", 
                 "device_additional_ips": "192.168.168.2,192.168.168.1", 
                 "device_family_engr": "9508", 
                 "device_family_exec": "9508", 
                 "device_role": "AGGREGATE", 
                 "dns_name": "lcaabcs14001-mgmt.acme.org", 
                 "dot1x_sw_support": "Not Applicable", 
                 "dot1x_system": "Not Applicable", 
                 "down_eth_ports": 140, 
                 "down_ports_categorization": "9+", 
                 "equipment_age": "Not Available", 
                 "equipment_name": "N9K-C9508", 
                 "equipment_type": "CHASSIS", 
                 "fex_description": "Not Available", 
                 "fex_grid": "Not Available", 
                 "fex_model": "Not Available", 
                 "fex_name": "Not Available", 
                 "fex_number": "Not Available", 
                 "fex_serial": "Not Available", 
                 "fex_state": "Not Available", 
                 "first_seen": "12/26/2022 03:51:33 AM ", 
                 "floor_Id": 2, 
                 "grid_Id": "2AX52", 
                 "hostname": "lcaabcs14001-2AX52", 
                 "hw_expiring_qtr": "Not Available", 
                 "hw_expiring_year": "Not Available", 
                 "hw_ldos_string": "No EOL", 
                 "hw_revision": "Missing HW Revision", 
                 "hw_status": "No EOL", 
                 "id": "user-dashboard-aia-network-drilldown-app", 
                 "ip_address": "192.168.163.228", 
                 "is_parent": "Yes", 
                 "is_poe_capable": "No", 
                 "last_qtr_of_support": "Not Available", 
                 "last_seen": "12/26/2022 03:51:33 AM ", 
                 "last_updated_time": "12/27/2022 06:58:44 AM ", 
                 "last_year_of_support": "Not Available", 
                 "latitude": 0.0, 
                 "longitude": 0.0, 
                 "mgmt_ip": "192.168.163.228", 
                 "ntwk_license_name": "Not Available", 
                 ... 
                 ... 
                 "sys_uptime_days": ">180", 
                 "system_vendor_os": "Cisco NX-OS", 
                 "system_vendor_sub_id": "12.3.1.3.1467", 
                 "timestamp": "2022-12-27T07:08:55.913324", 
                 "total_eth_ports": 769, 
                 "up_eth_ports": 629, 
                 "up_ports_categorization": "6+", 
                 "uptime": 193, 
                 "uptime_since": "06/17/2022", 
                 "vendor": "Cisco", 
                 "vpc_dns": "Not Available", 
                 "vpc_peer_device_ip": "10.0.0.2", 
                 "zone_alias_name": "Acme 14(M) - Service" 
             }, 
             { 
                 ... 
                 ... 
             } 
         ], 
         "hasMoreResults": true, 
         "last_sort_results": [ 
             1672124935913, 
             "4fe522a4590115b807844edcc82c88de" 
         ], 
         "properties": { 
             "maxResults": 2, 
             "offset": 0 
         }, 
         "reportMetaData": { 
             "actions": [ 
                 { 
                     "actionCondition": { 
                         "actionControl": "SHOW_IF", 
                         "conditionalField": [ 
                             { 
                                 "conditionType": "EQUAL", 
                                 "conditionValue": "CHASSIS", 
                                 "fieldId": "equipment_type" 
                             } 
                         ] 
                     }, 
                     "appName": "user-dashboard", 
                     "drillDownContext": "id", 
                     "drillDownLinkField": "dns_name", 
                     "identifier": "dns_name", 
                     "selectionType": "SINGLE", 
                     "stateName": "app.featureapp", 
                     "title": "View Details", 
                     "type": "GO_TO_APP_STATE" 
                 } 
             ], 
             "export": true, 
             "filtering": false, 
             "identifier": "user-dashboard-aia-network-assetslist_0", 
             "paginated": true, 
             "reportColumnDefinitionList": [ 
                 { 
                     "hidden": false, 
                     "id": "org_id", 
                     "identifier": "org_id", 
                     "key": true, 
                     "sortable": true, 
                     "title": "Organization ID", 
                     "type": "TEXT", 
                     "visible": false 
                 }, 
                 { 
                     ... 
                     ... 
                 } 
             ], 
             "sorting": true, 
             "title": "Assets Details" 
         }, 
         "totalResults": 11581 
     } 
 }

```

*   The `last_sort_results` parameter

The response contains the **last\_sort\_results** array of values in data of `serviceResult` for each API query, as shown in above sample API response. Use the **last\_sort\_results** parameter's values from last API response to get next batch of records.

[Sample API Request with last\_sort\_results Parameter](#__tabbed_8_1)
```
 curl -k --location --request POST 'https://192.168.103.40/api/portal/rdac/invokeAPI' \ 
 --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYjNkN2ExNDQtNDc3NC00MTEwLWEwMzEtZjFmMDhiYTRjYjhiIiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjkwOjg4MDgifQ.cyiMb2Kpi6FDGE8OHIV0zuB4RnK-vy9cbT_ByTeltzA' \ 
 --header 'Content-Type: application/json' \ 
 --data '{ 
     "serviceRequestDescriptor": { 
         "serviceName": "saas-reports", 
         "params": { 
             "params": [ 
                 { 
                     "context": { 
                         "contextInfo": { 
                             "contextIdList": [] 
                         }, 
                         "id": "user-dashboard-aia-network-assetslist", 
                         "name": "aia-network-assetslist", 
                         "view-context": { 
                             "appName": "user-dashboard", 
                             "pageName": "aia-network-assetslist" 
                         } 
                     }, 
                     "dashboardId": "Total Assets Details", 
                     "reportId": "dynamic_v2_tabular_report_0_0", 
                     "properties": { "maxResults": 2,  
                                     "last_sort_results": [ 
                                         1670392980290, 
                                         "288b473baa5b1d47006f7b313b336f3e" 
                                     ] 
                                 }, 
                 "filters": [] 
                 }]}, 
                 "methodName": "getReport" 
             }}'

```

**Applying filters to limit the results:**

Below is a sample API request to filter the device's **device\_role** is either `ACCESS` or `AGGREGATE`

[Sample API request with filter](#__tabbed_9_1)
```
 curl -k --location --request POST 'https://192.168.103.40/api/portal/rdac/invokeAPI' \ 
 --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYjNkN2ExNDQtNDc3NC00MTEwLWEwMzEtZjFmMDhiYTRjYjhiIiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjkwOjg4MDgifQ.cyiMb2Kpi6FDGE8OHIV0zuB4RnK-vy9cbT_ByTeltzA' \ 
 --header 'Content-Type: application/json' \ 
 --data '{ 
     "serviceRequestDescriptor": { 
         "serviceName": "saas-reports", 
         "params": { 
             "params": [ 
                 { 
                     "context": { 
                         "contextInfo": { 
                             "contextIdList": [] 
                         }, 
                         "id": "user-dashboard-aia-network-assetslist", 
                         "name": "aia-network-assetslist", 
                         "view-context": { 
                             "appName": "user-dashboard", 
                             "pageName": "aia-network-assetslist" 
                         } 
                     }, 
                     "dashboardId": "Total Assets Details", 
                     "reportId": "dynamic_v2_tabular_report_0_0", 
                     "properties": {}, 
                     "filters": [ 
                         { 
                             "column-id": "device_role", 
                             "column-type": "TEXT", 
                             "condition": "in", 
                             "values": [ 
                                 "ACCESS", 
                                 "AGGREGATE" 
                             ] 
                         } 
                     ]     
                 }]}, 
                 "methodName": "getReport" 
             }}'

```

Below is a sample request to get Incidents report data with filter created time less than 24 hours
```
 curl -k --location 'http://192.168.103.40/rdac/services/invokeJson' \ 
 --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYjNkN2ExNDQtNDc3NC00MTEwLWEwMzEtZjFmMDhiYTRjYjhiIiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjkwOjg4MDgifQ.cyiMb2Kpi6FDGE8OHIV0zuB4RnK-vy9cbT_ByTeltzA' \ 
 --header 'Content-Type: application/json' \ 
 --data '{ 
     "serviceRequestDescriptor": { 
         "serviceName": "saas-reports", 
         "version": "*", 
         "params": { 
             "params": [ 
                 { 
                     "context": { 
                         "contextInfo": { 
                             "contextIdList": [] 
                         }, 
                         "id": "user-dashboard-oia-incidents-os-template", 
                         "name": "user-dashboard-oia-incidents-os-template", 
                         "view-context": { 
                             "appName": "user-dashboard", 
                             "pageName": "oia-incidents-os-template" 
                         } 
                     }, 
                     "dashboardId": "incidents", 
                     "filters": [ 
                         { 
                             "column-id": "i_created_ts", 
                             "column-type": "DATETIME", 
                             "condition": ">", 
                             "timeFilter": true, 
                             "values": [ 
                                 "{\"type\":\"relative\",\"value\":\"-24\",\"units\":\"hours\"}" 
                             ] 
                         } 
                     ], 
                     "reportId": "dynamic_v2_tabular_report_0_0", 
                     "properties": { 
                         "offset": 0, 
                         "maxResults": 100 
                     } 
                 } 
             ] 
         }, 
         "methodName": "getReport", 
         "ignoreCall": true, 
         "parseOutput": true 
     } 
 }'

```

Below is a sample request to get Alerts report data with filters created time less than 24 hours and Severity High
```
 curl -k --location 'http://192.168.103.40/rdac/services/invokeJson' \ 
 --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYjNkN2ExNDQtNDc3NC00MTEwLWEwMzEtZjFmMDhiYTRjYjhiIiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjkwOjg4MDgifQ.cyiMb2Kpi6FDGE8OHIV0zuB4RnK-vy9cbT_ByTeltzA' \ 
 --header 'Content-Type: application/json' \ 
 --data '{ 
     "serviceRequestDescriptor": { 
         "serviceName": "saas-reports", 
         "version": "*", 
         "params": { 
             "params": [ 
                 { 
                     "context": { 
                         "contextInfo": { 
                             "contextIdList": [] 
                         }, 
                         "id": "user-dashboard-oia-alerts-os", 
                         "name": "user-dashboard-oia-alerts-os", 
                         "view-context": { 
                             "appName": "user-dashboard", 
                             "pageName": "oia-alerts-os" 
                         } 
                     }, 
                     "dashboardId": "alerts", 
                     "filters": [ 
                         { 
                             "column-id": "a_updated_ts", 
                             "column-type": "DATETIME", 
                             "condition": ">", 
                             "values": [ 
                                 "{\"type\":\"relative\",\"value\":\"-24\",\"units\":\"hours\"}" 
                             ] 
                         }, 
                         { 
                             "column-id": "a_severity", 
                             "column-type": "TEXT", 
                             "condition": "in", 
                             "values": [ 
                                 "CRITICAL" 
                             ] 
                         } 
                     ], 
                     "reportId": "dynamic_v2_tabular_report_0_0", 
                     "properties": { 
                         "offset": 0, 
                         "maxResults": 100 
                     } 
                 } 
             ] 
         }, 
         "methodName": "getReport", 
         "ignoreCall": true, 
         "parseOutput": true 
     } 
 }'

```

### **1.4** ****PStream data API using offline files****

API to get data from persistent Stream using previously created data files. These data files are created after the ingestion of data into Persistent Stream is complete. The data files that are in csv format, have all columns from Persistent Stream are split and stored as compressed gz files. They are named as data\_1.gz,data\_2.g, etc.

Note: It is recommended to use these new API’s to get larger datasets (e.g. ADM)

The API’s (getExportChunkList and downloadObject) enable users to get the latest file location of a stream and download the data.

**getExportChunkList** - API method to get location of latest chunk files for a stream. Response will have chunk object details in comma separated list

**API Request URL**
```
 https://<rdaf-aia-platform-ip-address>/api/portal/rdac/invokeService/getExportChunkLis

```

[Sample API Request](#__tabbed_10_1)
```
 curl -k --location --request POST 'https://192.168.108.94/api/portal/rdac/invokeService/getExportChunkList' \ 
 --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTlhYzI2YTgtOGMxYy00MzQ3LWFhMTMtM2Y3OWQwNWJkZGM2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjQ1Ojg4MDgifQ.oLAQ2sY87gp3r4MGGG9DlGO3Naa4MbBb7JdYni-a2kg' \ 
 --header 'Content-Type: application/json' \ 
 --data-raw '{ 
     "pstreamName": "aia_adm" 
 }'

```

**API Request Parameters**

| Parameter | Required | Type | Description |
| --- | --- | --- | --- |
| pstreamName | yes | string | Name of the persistent stream to get latest export job details |

[Sample API Response](#__tabbed_11_1)
```
 { 
     "data": { 
         "_id": "4458a6a13c0688f0cd0c6d8a1d4e02c6", 
         "_index": "bc7eec6269c244aa8bc58a725e208a8d-stream-4632cdce-rda_system_collector_export_job_status", 
         "_score": null, 
         "chunk_objects": "aia_adm-f780a9a6/data_1.gz,aia_adm-f780a9a6/data_2.gz,aia_adm-f780a9a6/data_3.gz,aia_adm-f780a9a6/data_4.gz,aia_adm-f780a9a6/data_5.gz,aia_adm-f780a9a6/data_6.gz,aia_adm-f780a9a6/data_7.gz,aia_adm-f780a9a6/data_8.gz,aia_adm-f780a9a6/data_9.gz,aia_adm-f780a9a6/data_10.gz,aia_adm-f780a9a6/data_11.gz,aia_adm-f780a9a6/data_12.gz,aia_adm-f780a9a6/data_13.gz,aia_adm-f780a9a6/data_14.gz,aia_adm-f780a9a6/data_15.gz,aia_adm-f780a9a6/data_16.gz,aia_adm-f780a9a6/data_17.gz,aia_adm-f780a9a6/data_18.gz,aia_adm-f780a9a6/data_19.gz,aia_adm-f780a9a6/data_20.gz,aia_adm-f780a9a6/data_21.gz,aia_adm-f780a9a6/data_22.gz,aia_adm-f780a9a6/data_23.gz,aia_adm-f780a9a6/data_24.gz,aia_adm-f780a9a6/data_25.gz", 
         "count_": 1, 
         "export_job_name": "aia_adm-f780a9a6", 
         "index_name": "bc7eec6269c244aa8bc58a725e208a8d-stream-6467bb64-aia_adm-replace-0ed08cca", 
         "row_count": 13621162, 
         "sort": [ 
             1676279406032, 
             "4458a6a13c0688f0cd0c6d8a1d4e02c6" 
         ], 
         "status": "Completed", 
         "stream": "aia_adm", 
         "timestamp": "2023-02-13T09:10:06.032462" 
     }, 
     "now": "2023-02-15T09:43:12.091051", 
     "reason": "", 
     "status": "ok" 
 }

```

**downloadObject** - API method to download the exported Persistent Stream data chunk objects

This API expects chunk object name received from the response of getExportChunkList API as explained in the previous section ( refer to getExportChunkList API section)

This API response will be a binary output.

*   Redirect the single downloadObject API response via CLI to a .gz file, decompress the .gz file using a gzip to decompress to a csv file. The csv will have data that includes all the columns from Persistent Stream.
    
*   If the Persistent Stream export has more than one chunk object, getExportChunkList API response will have comma separated list of chunk objects.
    

[Example](#__tabbed_12_1)
```
 aia_adm-f780a9a6/data_1.gz, aia_adm-f780a9a6/data_2.gz, aia_adm-f780a9a6/data_3.gz,...

```

Users are expected to download each chunk object (data\_1.gz, data\_2.gz,...) separately and decompress to get the complete data (dataset)

Note

Users can also use API in a programmatic way using Python to get the complete data.

**API Request URL**
```
 https://<rdaf-aia-platform-ip-address>/api/portal/rdac/invokeService/downloadObject

```

[Sample API Request](#__tabbed_13_1)
```
 curl -k --location 'https://192.168.108.94/api/portal/rdac/invokeService/downloadObject' \ 
 --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTlhYzI2YTgtOGMxYy00MzQ3LWFhMTMtM2Y3OWQwNWJkZGM2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjQ1Ojg4MDgifQ.oLAQ2sY87gp3r4MGGG9DlGO3Naa4MbBb7JdYni-a2kg' \ 
 --header 'Content-Type: application/json' \ 
 --header 'Connection: keep-alive' \ 
 --data '{ 
     "objectName": "aia_adm-f780a9a6/data_1.gz" 
 }' --output data_1.gz

```

**API Request Parameters**

| Parameter | Required | Type | Description |
| --- | --- | --- | --- |
| objectName | yes | string | Name of the exported chunk object |

**Example to get a csv data file from .gz file**

*   From command line using gzip tool:
```
  gzip -c -d data_1.gz > data_1.csv
 ```

Note

Users can other tools to decompress the gz files (e.g. 7z, etc)

*   Programmatic (using python) way to retrieve data:
```
 compressed_file = io.BytesIO(api_response) 
 with gzip.open(compressed_file, 'rt') as file: 
    with open("data_1.csv", 'w') as output: 
        output.write(file.read())

```

Users can call above RESTful APIs using get\_pstream\_exported\_data.py python module provided in the [package](https://macaw-amer.s3.amazonaws.com/releases/AIA/7.0.6/cfx_rda_aia_restful_api-v7.0.6.zip "Click Here")
.

API Response will be in compressed csv gzip bytes format and will include all columns from Persistent Stream.

## 2\. Python Module

To call RESTful APIs of RDAF platform's AIA/OIA application, users can create their own python script with the help of **api\_client** python module.

To download the Python package [Click Here](https://macaw-amer.s3.amazonaws.com/releases/AIA/7.0.6/cfx_rda_aia_restful_api-v7.0.6.zip "Click Here")

Note

Once users unzip the package file, it will create scripts directory with python modules.

**Prerequisites for python module:**

*   **requests** python HTTP library
    
*   **Usage of `api_client` python module:**
    

**1.** Import `APIGateway` class from `api_client` module and use `post_getReport` and `post_queryPstream` methods.

**2.** Need to provide the RDAF platform's ip address and `Authorization-Token` details while creating an instance to `APIGateway` class. Below is the example to pass configuration details to `APIGateway`
```
 from api_client import APIGateway 
 
 login_details = {"host": host, "Authorization-Token": token} 
 
 client = APIGateway(**login_details)

```

**3.** Use `post_getReport` method from `APIGateway` to query `getReport` API, below are the inputs needed for `post_getReport` method.
```
 Parameters: 
 
            pageName: str (Name of AIA/OIA page that has the report) 
            dashboardId: str (dashboardId inside the AIA/OIA page) 
            reportId: str (Id of the report within the dashboard of AIA/OIA page) 
            Properties: dict (offset and maxResults to query) —-> {"offset": 0, "maxResults": 20}

```

**4**. Use `post_queryPstream` method from `APIGateway` to query `queryPstream` API, below are the inputs needed for `queryPstream` method.
```
 Parameters: 
 
             name: str (Name of the Persistent Stream) 
             query: str (cfxql query to filter, default value is ‘*’) 
             maxRows: int (maxRows number) 
             last_sort_results: list (last_sort_results from previous query response to get next batch of results, default value is None)

```

**5.** Below are examples to query APIs using `post_getReport` and `post_queryPstream` from APIGateway class
```
 from api_client import APIGateway 
 
 login_details = {"host": host, "Authorization-Token": token} 
 
 client = APIGateway(**login_details) 
 
 response = client.post_queryPstream(name="aia_network", query="site_type is 'Data Center'", maxRows=20, last_sort_results=[1671454183711, "2362c22cfeda287521595c4a1e15a9cf"])

```

Note

It is recommended that users need to retry in case of any error in API response

*   **Usage of get\_report\_api.py and pstream\_query.py**
```
 python get_report_api.py --help

```
```
 usage: get_report_api.py [-h] --host HOST --token TOKEN --page PAGE --dashboard 
                         DASHBOARD --report REPORT [--offset OFFSET] 
                         [--max_rows MAX_ROWS] [--totalresults]

```

*   **Post API Request:**

[Required arguments:](#__tabbed_14_1)
```
   --host HOST           Provide IP Address of the host as input 
   --token TOKEN         Provide Authentication token for authorization 
   --page PAGE           Provide pageName of AIA/OIA app 
   --dashboard DASHBOARD 
                         provide dashboardId of AIA/OIA app page 
   --report REPORT       Provide reportId
 ```

[Optional arguments:](#__tabbed_15_1)
```
   -h, --help            show this help message and exit 
   --offset OFFSET       provide offset number as input 
   --max_rows MAX_ROWS   Provide max_rows number as input 
   --totalresults        Get total rows of the report
 ```

*   **Query for Persistent Stream:**
```
 python pstream_query.py --help

```
```
 usage: pstream_query.py [-h] --host HOST --token TOKEN --name NAME 
                         [--query QUERY] [--offset OFFSET] 
                         [--max_rows MAX_ROWS] [--filename FILENAME]

```

[Required arguments:](#__tabbed_16_1)
```
   --host HOST          Provide IP Address of the host as input 
   --token TOKEN        Provide Authentication token for authorization 
   --name NAME          Provide name of the Persistent Stream as input
 ```

[Optional arguments:](#__tabbed_17_1)
```
   -h, --help           show this help message and exit 
   --query QUERY        Provide cfxql query as input 
   --offset OFFSET      provide offset number as input 
   --max_rows MAX_ROWS  Provide max_rows number as input 
   --filename FILENAME  Provide filename or filepath to save results in csv, 
                        default filename is <stream_name>_query_results.csv
 ```

[Examples](#__tabbed_18_1)

*   Command to query ADM device details report using getReport API with offset 0 and maxResults 500
```
 python get_report_api.pyc --host 192.168.108.50 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiNTk1MWYyZjAtZTdlZi00YWQyLTljYzktZDY1NWFhNzAzNmE2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjU2Ojg4MDgifQ.6bW2L4E_P6cdpmX188vdMLfIDBaTcetm1QBG1cTj1j8" --page aia-adm --report dynamic_v2_tabular_report_0_0 --dashboard "ADM Device Details" --offset 0 --max_rows 500

```

*   Command to query CDP/LLDP neighbors report using getReport API with offset 0 and maxResults 100
```
 python get_report_api.pyc --host 192.168.108.50 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiNTk1MWYyZjAtZTdlZi00YWQyLTljYzktZDY1NWFhNzAzNmE2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjU2Ojg4MDgifQ.6bW2L4E_P6cdpmX188vdMLfIDBaTcetm1QBG1cTj1j8" --page aia-network-assetslist --report dynamic_v2_tabular_report_0_0 --dashboard "CDP Neighbor Assets" --max_rows 100

```

*   Command to query Incidents report using getReport API with offset 0 and maxResults 500
```
 python get_report_api.pyc --host 192.168.108.50 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiNTk1MWYyZjAtZTdlZi00YWQyLTljYzktZDY1NWFhNzAzNmE2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjU2Ojg4MDgifQ.6bW2L4E_P6cdpmX188vdMLfIDBaTcetm1QBG1cTj1j8" --page oia-incidents-os-template --report dynamic_v2_tabular_report_0_0 --dashboard incidents --offset 0 --max_rows 500

```

*   Command to query Alerts report using getReport API with offset 0 and maxResults 500
```
 python get_report_api.pyc --host 192.168.108.50 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiNTk1MWYyZjAtZTdlZi00YWQyLTljYzktZDY1NWFhNzAzNmE2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjU2Ojg4MDgifQ.6bW2L4E_P6cdpmX188vdMLfIDBaTcetm1QBG1cTj1j8" --page ooia-alerts-os --report dynamic_v2_tabular_report_0_0 --dashboard alerts --offset 0 --max_rows 500

```

*   Command to query all the rows from aia\_cdp Persistent Stream with max\_rows 100 per batch
```
 python pstream_query.pyc --host 192.168.108.50 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiNTk1MWYyZjAtZTdlZi00YWQyLTljYzktZDY1NWFhNzAzNmE2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjU2Ojg4MDgifQ.6bW2L4E_P6cdpmX188vdMLfIDBaTcetm1QBG1cTj1j8" --name aia_cdp --max_rows 100

```

*   Command to query all the rows from aia\_network Persistent Stream with max\_rows 500 per batch using filter site\_type is 'Data Center'
```
 python pstream_query.pyc --host 192.168.108.50 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiNTk1MWYyZjAtZTdlZi00YWQyLTljYzktZDY1NWFhNzAzNmE2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjU2Ojg4MDgifQ.6bW2L4E_P6cdpmX188vdMLfIDBaTcetm1QBG1cTj1j8" --name aia_network --query "site_type is 'Data Center'" --max_rows 500

```

*   command to query incidents from oia-incidents-stream Persistent Stream with filter i\_priority\_label in \['Critical', 'High'\] and max\_rows value as 100 to get critical and high in priority incidents
```
 python pstream_query.pyc --host 10.95.107.126 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoiYWNtZUBjZnguY29tIiwid29ya3NwYWNlaWQiOiJiZDRhMTk0NC0zMTEyLTRlMjYtOTE0MC0wM2QwMDFhNTE5MjUiLCJyZGFjX2FwaV9lbmRwb2ludCI6Imh0dHA6Ly8xMC45NS4xMDcuMTI2Ojg4MDgifQ.50yfMTq_ju-nX41i44_gLYm25HTrzuoYmqMWvJHvhTQ" --name oia-incidents-stream --query "i_priority_label in ['Critical', 'High']" --max_rows 100

```

*   command to query alerts from oia-alerts-stream Persistent Stream with filter `a_updated_ts` later than -24 hours to get all alerts updated in last 24 hours

`
```
 python pstream_query.pyc --host 10.95.107.126 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoiYWNtZUBjZnguY29tIiwid29ya3NwYWNlaWQiOiJiZDRhMTk0NC0zMTEyLTRlMjYtOTE0MC0wM2QwMDFhNTE5MjUiLCJyZGFjX2FwaV9lbmRwb2ludCI6Imh0dHA6Ly8xMC45NS4xMDcuMTI2Ojg4MDgifQ.50yfMTq_ju-nX41i44_gLYm25HTrzuoYmqMWvJHvhTQ" --name oia-alerts-stream --query "\`a_updated_ts\` later than -24 hours"`
```

Users can call getExportChunkList, downloadObject RESTful APIs using get\_pstream\_exported\_data.py python module provided in the package. This script will download and save the files in csv format.

*   Usage of get\_pstream\_exported\_data.py
```
 python get_pstream_exported_data.py --help 
 usage: get_pstream_exported_data.py [-h] --host HOST --token TOKEN --name 
                                      NAME [--ssl SSL] [--path PATH]

```

*   Get the latest persistent stream exported chunks data

[Optional arguments:](#__tabbed_19_1)
```
   -h, --help     show this help message and exit 
   --ssl SSL      SSL verification True/False, default value False 
   --path PATH    Provide path to save csv files
 ```

[Required arguments:](#__tabbed_20_1)
```
   --host HOST    Provide IP Address of the host as input 
   --token TOKEN  Provide Authentication token for authorization 
   --name NAME    Provide name of the Persistent Stream as input
 ```

[Examples](#__tabbed_21_1)

**1.** Command to get aia\_adm Persistent Stream exported data in csv files
```
 python get_pstream_exported_data.pyc --host 192.168.108.94 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZ 
 WlkIjoiYTlhYzI2YTgtOGMxYy00MzQ3LWFhMTMtM2Y3OWQwNWJkZGM2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjQ1Ojg4MDgifQ.oLAQ2sY87gp3r4MGGG9DlGO3Naa4MbBb7JdYni-a2kg" --name aia_adm

```

**2.** Command to get aia\_adm Persistent Stream exported data in csv files in /tmp/downloads/ path
```
 python get_pstream_exported_data.pyc --host 192.168.108.94 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZ 
 WlkIjoiYTlhYzI2YTgtOGMxYy00MzQ3LWFhMTMtM2Y3OWQwNWJkZGM2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjQ1Ojg4MDgifQ.oLAQ2sY87gp3r4MGGG9DlGO3Naa4MbBb7JdYni-a2kg" --name aia_adm --path /tmp/downloads/

```

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!