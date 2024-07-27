 



RDAF Platform's Asset Intelligence and Analytics (AIA) / Operations Intelligence & Analytics (OIA) RESTful APIs
===============================================================================================================

1\. Query the inventory data using RESTful APIs
-----------------------------------------------

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

`[](#__codelineno-0-1) https://<rdaf-aia-platform-ip-address>/api/portal/rdac/invokeAPI`

Below example provides a sample API request to query the network devices inventory data from persistent stream `aia_network`.

Tip

Users need to copy/store the Bearer token given in the below sample API request from the above 'API Authentication' section

[Sample API Request](#__tabbed_1_1)

`[](#__codelineno-1-1) curl -k --location --request POST 'https://192.168.108.94/api/portal/rdac/invokeAPI' \ [](#__codelineno-1-2) --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTVjYTY2OWEtOTA3My00ZDIwLTgzNTktNDYyNzNiNTEyYmE4IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4Ljk0Ojg4MDgifQ.B64zQTANAqP0InVE6xQl4O5zBx65U51y4M8xosA_6ZY' \ [](#__codelineno-1-3) --header 'Content-Type: application/json' \ [](#__codelineno-1-4) --data '{ [](#__codelineno-1-5)     "serviceRequestDescriptor": { [](#__codelineno-1-6)         "serviceName": "saas-reports", [](#__codelineno-1-7)         "params": { [](#__codelineno-1-8)             "params": [ [](#__codelineno-1-9)                 { [](#__codelineno-1-10)                     "name": "aia_network", [](#__codelineno-1-11)                     "max_rows": 2, [](#__codelineno-1-12)                     "query": "*" [](#__codelineno-1-13)                 } [](#__codelineno-1-14)             ] [](#__codelineno-1-15)         }, [](#__codelineno-1-16)         "methodName": "queryPstream" [](#__codelineno-1-17)     } [](#__codelineno-1-18) }'`

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

`[](#__codelineno-2-1) { [](#__codelineno-2-2)     "completed": "2022-12-27T08:21:04.808489", [](#__codelineno-2-3)     "created": "2022-12-27T08:21:04.632261", [](#__codelineno-2-4)     "serviceError": "none", [](#__codelineno-2-5)     "serviceResult": { [](#__codelineno-2-6)         "data": { [](#__codelineno-2-7)             "hasMoreResults": true, [](#__codelineno-2-8)             "last_sort_results": [ [](#__codelineno-2-9)                 1672124935913, [](#__codelineno-2-10)                 "4fe522a4590115b807844edcc82c88de" [](#__codelineno-2-11)             ], [](#__codelineno-2-12)             "offset": null, [](#__codelineno-2-13)             "results": [ [](#__codelineno-2-14)                 { [](#__codelineno-2-15)                     "__mode": "AUTO", [](#__codelineno-2-16)                     "__rma_new_sn__": "Not Available", [](#__codelineno-2-17)                     "__rma_old_sn__": "Not Available", [](#__codelineno-2-18)                     "__state": "ACTIVE", [](#__codelineno-2-19)                     "__state_updated_time": 1672124308000.0, [](#__codelineno-2-20)                     "_id": "31affbe3a9b62da78a676b744e2a7319", [](#__codelineno-2-21)                     "_index": "51f9a6e0711142939f953bec78d7e7bb-stream-2dec0fc9-aia_network-replace-90bafdd7", [](#__codelineno-2-22)                     "_score": null, [](#__codelineno-2-23)                     "address": "Not Available", [](#__codelineno-2-24)                     "admin_down_eth_ports": 125, [](#__codelineno-2-25)                     "api_status": "Not Applicable", [](#__codelineno-2-26)                     "apic_node_dn": "Not Applicable", [](#__codelineno-2-27)                     "apic_pod_id": "Not Applicable", [](#__codelineno-2-28)                     "apic_role": "Not Applicable", [](#__codelineno-2-29)                     "asset_id": "e42f38259c3441ca4ae05914144ac23f", [](#__codelineno-2-30)                     "asset_type": "Hardware", [](#__codelineno-2-31)                     "bucket_id": "21e31d728718dc98054d6839b124445c", [](#__codelineno-2-32)                     "cafm_code": "AB22-05", [](#__codelineno-2-33)                     "cdp_global_deviceId": "dcaabcs14001-2AX52.acme.org(FGE29017ABC)", [](#__codelineno-2-34)                     "child_devices": 0, [](#__codelineno-2-35)                     "city": "Pleasanton", [](#__codelineno-2-36)                     "closet_Id": "RAISEDFLOOR", [](#__codelineno-2-37)                     "contract_coverage": "Not Available", [](#__codelineno-2-38)                     "count_": 1, [](#__codelineno-2-39)                     "country": "Not Available", [](#__codelineno-2-40)                     "created_time": 1672124323000.0, [](#__codelineno-2-41)                     "customer_acceptable_sw_version": "Not Available", [](#__codelineno-2-42)                     "customer_approved_sw_version": "7.0(3)I7(8)", [](#__codelineno-2-43)                     "customer_category": "DC Fabric LAN", [](#__codelineno-2-44)                     "customer_certified_replacement": "Not Available", [](#__codelineno-2-45)                     "customer_equipment_type": "Zone Service Switch", [](#__codelineno-2-46)                     "customer_por_generation": "N", [](#__codelineno-2-47)                     "customer_por_generation_Exec": "N", [](#__codelineno-2-48)                     "customer_topological_tier": "LAN Device", [](#__codelineno-2-49)                     "customer_zone": "14", [](#__codelineno-2-50)                     "device_additional_ips": "192.168.188.2,192.168.50.1,", [](#__codelineno-2-51)                     "device_family_engr": "9508", [](#__codelineno-2-52)                     "device_family_exec": "9508", [](#__codelineno-2-53)                     "device_role": "AGGREGATE", [](#__codelineno-2-54)                     "dns_name": "dcaabcs14001-mgmt.acme.org", [](#__codelineno-2-55)                     "dot1x_sw_support": "Not Applicable", [](#__codelineno-2-56)                     "dot1x_system": "Not Applicable", [](#__codelineno-2-57)                     "down_eth_ports": 140, [](#__codelineno-2-58)                     "down_ports_categorization": "9+", [](#__codelineno-2-59)                     "equipment_age": "Not Available", [](#__codelineno-2-60)                     "equipment_name": "N9K-C9508", [](#__codelineno-2-61)                     "equipment_type": "CHASSIS", [](#__codelineno-2-62)                     "fex_description": "Not Available", [](#__codelineno-2-63)                     "fex_grid": "Not Available", [](#__codelineno-2-64)                     "fex_model": "Not Available", [](#__codelineno-2-65)                     "fex_name": "Not Available", [](#__codelineno-2-66)                     "fex_number": "Not Available", [](#__codelineno-2-67)                     "fex_serial": "Not Available", [](#__codelineno-2-68)                     "fex_state": "Not Available", [](#__codelineno-2-69)                     "first_seen": 1672026693000.0, [](#__codelineno-2-70)                     "floor_Id": 2, [](#__codelineno-2-71)                     "grid_Id": "2AX52", [](#__codelineno-2-72)                     "hostname": "dcaabcs14001-2AX52", [](#__codelineno-2-73)                     "hw_expiring_qtr": "Not Available", [](#__codelineno-2-74)                     "hw_expiring_year": "Not Available", [](#__codelineno-2-75)                     "hw_ldos_string": "No EOL", [](#__codelineno-2-76)                     "hw_revision": "Missing HW Revision", [](#__codelineno-2-77)                     "hw_status": "No EOL", [](#__codelineno-2-78)                     "ip_address": "192.168..163.228", [](#__codelineno-2-79)                     "is_parent": "Yes", [](#__codelineno-2-80)                     "is_poe_capable": "No", [](#__codelineno-2-81)                     "last_qtr_of_support": "Not Available", [](#__codelineno-2-82)                     "last_seen": 1672026693000.0, [](#__codelineno-2-83)                     "last_updated_time": 1672124324000.0, [](#__codelineno-2-84)                     "last_year_of_support": "Not Available", [](#__codelineno-2-85)                     "latitude": 0.0, [](#__codelineno-2-86)                     "longitude": 0.0, [](#__codelineno-2-87)                     "mgmt_ip": "192.168.163.228", [](#__codelineno-2-88)                     "ntwk_license_name": "Not Available", [](#__codelineno-2-89)                     "org_id": "c1048ac6-0442-4cd5-a39c-1a98ef2cf1c4", [](#__codelineno-2-90)                     "org_name": "ACME", [](#__codelineno-2-91)                     "original_pid": "N9K-C9508-B3-E", [](#__codelineno-2-92)                     "parent_pid": "N9K-C9508", [](#__codelineno-2-93)                     "parent_sn": "FGE22789TXV", [](#__codelineno-2-94)                     "poe_admin_auto": 0, [](#__codelineno-2-95)                     "poe_admin_off": 0, [](#__codelineno-2-96)                     "poe_admin_static": 0, [](#__codelineno-2-97)                     "poe_oper_faulty": 0, [](#__codelineno-2-98)                     "poe_oper_off": 0, [](#__codelineno-2-99)                     "poe_oper_on": 0, [](#__codelineno-2-100)                     "poe_oper_power_deny": 0, [](#__codelineno-2-101)                     "poe_remaining_watts": 0, [](#__codelineno-2-102)                     "poe_summary": "Not Available", [](#__codelineno-2-103)                     "poe_total_watts": 0, [](#__codelineno-2-104)                     "poe_used_watts": 0, [](#__codelineno-2-105)                     "postal_code": 94558.0, [](#__codelineno-2-106)                     "price": 0.0, [](#__codelineno-2-107)                     "product_category": "Switches", [](#__codelineno-2-108)                     "product_description": "Nexus 9508 Chassis Bundle with 1Sup, 3 PS, 2SC, 4 FM-E, 3Fan", [](#__codelineno-2-109)                     "product_family": "Cisco Nexus 9000 Series Switches", [](#__codelineno-2-110)                     "product_id": "N9K-C9508-B3-E", [](#__codelineno-2-111)                     "product_name": "Cisco Nexus 9508 Switch", [](#__codelineno-2-112)                     "product_type": "SWITCH", [](#__codelineno-2-113)                     "province": "Missing Province", [](#__codelineno-2-114)                     "region": "CN", [](#__codelineno-2-115)                     "replacement_cost": 0.0, [](#__codelineno-2-116)                     "replacement_part_description": "Not Available", [](#__codelineno-2-117)                     "replacement_part_id": "Not Available", [](#__codelineno-2-118)                     "serial_num": "FGE22678TXV", [](#__codelineno-2-119)                     "shipped_city": "Pleasanton", [](#__codelineno-2-120)                     "site": "AB22-05|02|RAISEDFLOOR|2AX52|4301 Hacienda Dr.|Pleasanton|CA|94558", [](#__codelineno-2-121)                     "site_code": "ABC", [](#__codelineno-2-122)                     "site_details": "Not Available", [](#__codelineno-2-123)                     "site_id": "Not Available", [](#__codelineno-2-124)                     "site_name": "Not Available", [](#__codelineno-2-125)                     "site_type": "Data Center", [](#__codelineno-2-126)                     "site_zone": "ABC-Zone 14(M) - Service", [](#__codelineno-2-127)                     "snmp_syslocation": "AB22-05|02|RAISEDFLOOR|2AX52|4301 Hacienda Dr.|Pleasanton|CA|94558", [](#__codelineno-2-128)                     "sort": [ [](#__codelineno-2-129)                         1672124935913, [](#__codelineno-2-130)                         "31affbe3a9b62da78a676b744e2a7319" [](#__codelineno-2-131)                     ], [](#__codelineno-2-132)                     "source_filename": "acme_consolidated_exportdata_12M26D2022Y_5h30m.zip", [](#__codelineno-2-133)                     "state": "California", [](#__codelineno-2-134)                     "state_code": "CA", [](#__codelineno-2-135)                     "sw_expiring_qtr": "Not Available", [](#__codelineno-2-136)                     "sw_expiring_year": "Not Available", [](#__codelineno-2-137)                     "sw_por": "N (Current Standard)", [](#__codelineno-2-138)                     "sw_status": "Not Available", [](#__codelineno-2-139)                     "sw_type": "Cisco NX-OS", [](#__codelineno-2-140)                     "sw_version": "7.0(3)I7(8)", [](#__codelineno-2-141)                     "sw_version_details": "RELEASE SOFTWARE", [](#__codelineno-2-142)                     "sys_contact": "VNOC 866-457-4329", [](#__codelineno-2-143)                     "sys_descr": "Cisco NX-OS(tm) nxos.7.0.3.I7.8.bin, Software (nxos), Version 7.0(3)I7(8), RELEASE SOFTWARE Copyright (c) 2002-2020 by Cisco Systems, Inc. Compiled 3/3/2020 19:00:00", [](#__codelineno-2-144)                     "sys_objectId": "1.3.6.1.4.1.9.12.3.1.3.1467", [](#__codelineno-2-145)                     "sys_uptime": 193.0, [](#__codelineno-2-146)                     "sys_uptime_days": ">180", [](#__codelineno-2-147)                     "system_vendor_os": "Cisco NX-OS", [](#__codelineno-2-148)                     "system_vendor_sub_id": "12.3.1.3.1467", [](#__codelineno-2-149)                     "timestamp": "2022-12-27T07:08:55.913324", [](#__codelineno-2-150)                     "total_eth_ports": 769, [](#__codelineno-2-151)                     "up_eth_ports": 629, [](#__codelineno-2-152)                     "up_ports_categorization": "6+", [](#__codelineno-2-153)                     "uptime": 193, [](#__codelineno-2-154)                     "uptime_since": 1655449096135.0, [](#__codelineno-2-155)                     "vendor": "Cisco", [](#__codelineno-2-156)                     "vpc_dns": "Not Available", [](#__codelineno-2-157)                     "vpc_peer_device_ip": "10.0.0.2", [](#__codelineno-2-158)                     "zone_alias_name": "Acme 14(M) - Service" [](#__codelineno-2-159)                 }, [](#__codelineno-2-160)                 { [](#__codelineno-2-161)                     ... [](#__codelineno-2-162)                     ... [](#__codelineno-2-163)                 } [](#__codelineno-2-164)             ], [](#__codelineno-2-165)             "results_count": 2, [](#__codelineno-2-166)             "totalResults": 11581 [](#__codelineno-2-167)         }, [](#__codelineno-2-168)         "now": "2022-12-27T08:21:04.775442", [](#__codelineno-2-169)         "reason": "", [](#__codelineno-2-170)         "status": "ok" [](#__codelineno-2-171)     } [](#__codelineno-2-172) }`

*   The `last_sort_results` parameter

The response contains the **last\_sort\_results** array of values in data of `serviceResult` for each API query, as shown in above sample API response. Use the **last\_sort\_results** parameter's values from last API response to get next batch of records.

[Sample API Request with last\_sort\_results Parameter](#__tabbed_3_1)

`[](#__codelineno-3-1) curl -k --location --request POST 'https://192.168.108.94/api/portal/rdac/invokeAPI' \ [](#__codelineno-3-2) --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTVjYTY2OWEtOTA3My00ZDIwLTgzNTktNDYyNzNiNTEyYmE4IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4Ljk0Ojg4MDgifQ.B64zQTANAqP0InVE6xQl4O5zBx65U51y4M8xosA_6ZY' \ [](#__codelineno-3-3) --header 'Content-Type: application/json' \ [](#__codelineno-3-4) --data '{ [](#__codelineno-3-5)     "serviceRequestDescriptor": { [](#__codelineno-3-6)         "serviceName": "saas-reports", [](#__codelineno-3-7)         "params": { [](#__codelineno-3-8)             "params": [ [](#__codelineno-3-9)                 { [](#__codelineno-3-10)                     "name": "aia_network", [](#__codelineno-3-11)                     "max_rows": 2, [](#__codelineno-3-12)                     "query": "*", [](#__codelineno-3-13)                     "last_sort_results": [ [](#__codelineno-3-14)                 1670392980290, [](#__codelineno-3-15)                 "288b473baa5b1d47006f7b313b336f3e" [](#__codelineno-3-16)             ] [](#__codelineno-3-17)                 } [](#__codelineno-3-18)             ] [](#__codelineno-3-19)         }, [](#__codelineno-3-20)         "methodName": "queryPstream" [](#__codelineno-3-21)     } [](#__codelineno-3-22) }'`

[Sample API Response](#__tabbed_4_1)

`[](#__codelineno-4-1) { [](#__codelineno-4-2)     "completed": "2022-12-27T08:23:15.977406", [](#__codelineno-4-3)     "created": "2022-12-27T08:23:15.803026", [](#__codelineno-4-4)     "serviceError": "none", [](#__codelineno-4-5)     "serviceResult": { [](#__codelineno-4-6)         "data": { [](#__codelineno-4-7)             "hasMoreResults": true, [](#__codelineno-4-8)             "last_sort_results": [ [](#__codelineno-4-9)                 1672124935912, [](#__codelineno-4-10)                 "784e454047da8ce16470324a6bc928ce" [](#__codelineno-4-11)             ], [](#__codelineno-4-12)             "offset": null, [](#__codelineno-4-13)             "results": [ [](#__codelineno-4-14)                 { [](#__codelineno-4-15)                     "__mode": "AUTO", [](#__codelineno-4-16)                     "__rma_new_sn__": "Not Available", [](#__codelineno-4-17)                     "__rma_old_sn__": "Not Available", [](#__codelineno-4-18)                     "__state": "ACTIVE", [](#__codelineno-4-19)                     "__state_updated_time": 1672124308000.0, [](#__codelineno-4-20)                     "_id": "62dc08304dc88fcaebce473e3b7ad5e5", [](#__codelineno-4-21)                     "_index": "51f9a6e0711142939f953bec78d7e7bb-stream-2dec0fc9-aia_network-replace-90bafdd7", [](#__codelineno-4-22)                     "_score": null, [](#__codelineno-4-23)                     "address": "Not Available", [](#__codelineno-4-24)                     "admin_down_eth_ports": 0, [](#__codelineno-4-25)                     "api_status": "Success", [](#__codelineno-4-26)                     "apic_node_dn": "Not Applicable", [](#__codelineno-4-27)                     "apic_pod_id": "Not Applicable", [](#__codelineno-4-28)                     "apic_role": "Not Applicable", [](#__codelineno-4-29)                     "asset_id": "ca01f634b4d80ec5d228e7af52afbacb", [](#__codelineno-4-30)                     "asset_type": "Hardware", [](#__codelineno-4-31)                     "bucket_id": "fbe95cc8ed6629939349dd26d6d7f4c5", [](#__codelineno-4-32)                     "cafm_code": "AB22-05", [](#__codelineno-4-33)                     "cdp_global_deviceId": "ACMEABCP41908.acme.org(FDO24789AFG)", [](#__codelineno-4-34)                     "child_devices": 0, [](#__codelineno-4-35)                     "city": "Pleasanton", [](#__codelineno-4-36)                     "closet_Id": "RaisedFloor", [](#__codelineno-4-37)                     "customer_equipment_type": "Acme Production Switch", [](#__codelineno-4-38)                     "customer_por_generation": "N", [](#__codelineno-4-39)                     "customer_por_generation_Exec": "N", [](#__codelineno-4-40)                     ... [](#__codelineno-4-41)                     ... [](#__codelineno-4-42)                     "uptime": 388, [](#__codelineno-4-43)                     "uptime_since": 1638601096076.0, [](#__codelineno-4-44)                     "vendor": "Cisco", [](#__codelineno-4-45)                     "vpc_dns": "Not Available", [](#__codelineno-4-46)                     "vpc_peer_device_ip": "Not Available", [](#__codelineno-4-47)                     "zone_alias_name": "Acme 10(I) - MSP" [](#__codelineno-4-48)                 }, [](#__codelineno-4-49)                 { [](#__codelineno-4-50)                     ... [](#__codelineno-4-51)                     ... [](#__codelineno-4-52)                 } [](#__codelineno-4-53)             ], [](#__codelineno-4-54)             "results_count": 2, [](#__codelineno-4-55)             "totalResults": 11581 [](#__codelineno-4-56)         }, [](#__codelineno-4-57)         "now": "2022-12-27T08:23:15.951970", [](#__codelineno-4-58)         "reason": "", [](#__codelineno-4-59)         "status": "ok" [](#__codelineno-4-60)     } [](#__codelineno-4-61) }`

[Sample queryPstream API response with results\_count and totalResults parameters](#__tabbed_5_1)

API response contains results\_count and totalResults values in "data" of serviceResult, results\_count represents the number of records that are in the current response data, and totalResults is the total number of records for a given API query (of that persistent stream).

`[](#__codelineno-5-1) { [](#__codelineno-5-2)     "completed": "2022-12-27T08:21:04.808489", [](#__codelineno-5-3)     "created": "2022-12-27T08:21:04.632261", [](#__codelineno-5-4)     "serviceError": "none", [](#__codelineno-5-5)     "serviceResult": { [](#__codelineno-5-6)         "data": { [](#__codelineno-5-7)             "hasMoreResults": true, [](#__codelineno-5-8)             "last_sort_results": [ [](#__codelineno-5-9)                 1672124935913, [](#__codelineno-5-10)                 "4fe522a4590115b807844edcc82c88de" [](#__codelineno-5-11)             ], [](#__codelineno-5-12)             "offset": null, [](#__codelineno-5-13)             "results": [  [](#__codelineno-5-14)               { [](#__codelineno-5-15)                     ... [](#__codelineno-5-16)                     ... [](#__codelineno-5-17)                 } [](#__codelineno-5-18)             ], [](#__codelineno-5-19)             "results_count": 2, [](#__codelineno-5-20)             "totalResults": 11581 [](#__codelineno-5-21)         }, [](#__codelineno-5-22)         "now": "2022-12-27T08:21:04.775442", [](#__codelineno-5-23)         "reason": "", [](#__codelineno-5-24)         "status": "ok" [](#__codelineno-5-25)     }`

Note

For given query, If results\_count in response has less than max\_rows provided or 0 then it means the end of the query results.

**Applying CFXQL query to filter the data:**

Below is a sample API request to query the inventory data of network device using CFXQL query to filter the data.

`[](#__codelineno-6-1) curl -k --location --request POST 'https://192.168.108.94/api/portal/rdac/invokeAPI' \ [](#__codelineno-6-2) --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTVjYTY2OWEtOTA3My00ZDIwLTgzNTktNDYyNzNiNTEyYmE4IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4Ljk0Ojg4MDgifQ.B64zQTANAqP0InVE6xQl4O5zBx65U51y4M8xosA_6ZY' \ [](#__codelineno-6-3) --header 'Content-Type: application/json' \ [](#__codelineno-6-4) --data '{ [](#__codelineno-6-5)     "serviceRequestDescriptor": { [](#__codelineno-6-6)         "serviceName": "saas-reports", [](#__codelineno-6-7)         "params": { [](#__codelineno-6-8)             "params": [ [](#__codelineno-6-9)                 { [](#__codelineno-6-10)                     "name": "aia_network", [](#__codelineno-6-11)                     "max_rows": 2, [](#__codelineno-6-12)                     "query": "ip_address ~ '\''192.168.230'\''", [](#__codelineno-6-13)                     "last_sort_results": [ [](#__codelineno-6-14)                 1670392980290, [](#__codelineno-6-15)                 "288b473baa5b1d47006f7b313b336f3e" [](#__codelineno-6-16)             ] [](#__codelineno-6-17)                 } [](#__codelineno-6-18)             ] [](#__codelineno-6-19)         }, [](#__codelineno-6-20)         "methodName": "queryPstream" [](#__codelineno-6-21)     } [](#__codelineno-6-22) }'`

**Applying Sorting on Columns:**

Below is a sample API request to query the inventory data using Sorting on Columns serial\_num and parent\_sn in ascending order.

`[](#__codelineno-7-1) curl -k --location --request POST 'https://192.168.108.94/api/portal/rdac/invokeAPI' \ [](#__codelineno-7-2) --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTVjYTY2OWEtOTA3My00ZDIwLTgzNTktNDYyNzNiNTEyYmE4IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4Ljk0Ojg4MDgifQ.B64zQTANAqP0InVE6xQl4O5zBx65U51y4M8xosA_6ZY' \ [](#__codelineno-7-3) --header 'Content-Type: application/json' \ [](#__codelineno-7-4) --data '{ [](#__codelineno-7-5)     "serviceRequestDescriptor": { [](#__codelineno-7-6)         "serviceName": "saas-reports", [](#__codelineno-7-7)         "params": { [](#__codelineno-7-8)             "params": [ [](#__codelineno-7-9)                 { [](#__codelineno-7-10)                     "name": "aia_network", [](#__codelineno-7-11)                     "max_rows": 500, [](#__codelineno-7-12)                     "query": "*", [](#__codelineno-7-13)                     "sorting": [{"serial_num.keyword": "asc"}, {"parent_sn.keyword": "asc"}] [](#__codelineno-7-14)                 } [](#__codelineno-7-15)             ] [](#__codelineno-7-16)         }, [](#__codelineno-7-17)         "methodName": "queryPstream" [](#__codelineno-7-18)     } [](#__codelineno-7-19) }'`

Note

Add ‘.keyword’ to columns if column type is text, “asc” for ascending order and “desc” for descending order

Below is a sample Request to query incidents data from oia-incidents-stream Persistent Stream

`[](#__codelineno-8-1) curl -k --location 'https:///192.168.108.94/api/portal/rdac/invokeAPI' \ [](#__codelineno-8-2) --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTVjYTY2OWEtOTA3My00ZDIwLTgzNTktNDYyNzNiNTEyYmE4IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4Ljk0Ojg4MDgifQ.B64zQTANAqP0InVE6xQl4O5zBx65U51y4M8xosA_6ZY' \ [](#__codelineno-8-3) --header 'Content-Type: application/json' \ [](#__codelineno-8-4) --header 'Cookie: __cfxsession=7be65841-1d40-45ae-95ee-1fb98a600ace; rdafportal=rdaf-portal-1|ZAN/9|ZAN/9' \ [](#__codelineno-8-5) --data '{ [](#__codelineno-8-6)     "serviceRequestDescriptor": { [](#__codelineno-8-7)         "serviceName": "saas-reports", [](#__codelineno-8-8)         "params": { [](#__codelineno-8-9)             "params": [ [](#__codelineno-8-10)                 { [](#__codelineno-8-11)                     "name": "oia-incidents-stream", [](#__codelineno-8-12)                     "max_rows": 20, [](#__codelineno-8-13)                     "query": "*" [](#__codelineno-8-14)                 } [](#__codelineno-8-15)             ] [](#__codelineno-8-16)         }, [](#__codelineno-8-17)         "methodName": "queryPstream" [](#__codelineno-8-18)     } [](#__codelineno-8-19) }'`

Below is a sample Request to query alerts data from oia-alerts-stream Persistent Stream with filter a\_status is 'ACTIVE'

`[](#__codelineno-9-1) curl -k --location 'https://192.168.108.94/api/portal/rdac/invokeAPI' \ [](#__codelineno-9-2) --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTVjYTY2OWEtOTA3My00ZDIwLTgzNTktNDYyNzNiNTEyYmE4IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4Ljk0Ojg4MDgifQ.B64zQTANAqP0InVE6xQl4O5zBx65U51y4M8xosA_6ZY' \ [](#__codelineno-9-3) --header 'Content-Type: application/json' \ [](#__codelineno-9-4) --header 'Cookie: __cfxsession=7be65841-1d40-45ae-95ee-1fb98a600ace; rdafportal=rdaf-portal-1|ZAOAv|ZAN/9' \ [](#__codelineno-9-5) --data '{ [](#__codelineno-9-6)     "serviceRequestDescriptor": { [](#__codelineno-9-7)         "serviceName": "saas-reports", [](#__codelineno-9-8)         "params": { [](#__codelineno-9-9)             "params": [ [](#__codelineno-9-10)                 { [](#__codelineno-9-11)                     "name": "oia-alerts-stream", [](#__codelineno-9-12)                     "max_rows": 20, [](#__codelineno-9-13)                     "query": "a_status is 'ACTIVE'" [](#__codelineno-9-14)                 } [](#__codelineno-9-15)             ] [](#__codelineno-9-16)         }, [](#__codelineno-9-17)         "methodName": "queryPstream" [](#__codelineno-9-18)     } [](#__codelineno-9-19) }'`

### **1.3** ****Query Inventory data from UI reports****

**getReport** - API method to query the asset inventory data from a given UI widget report within the selected Dashboard.

*   `invokeAPI` **API request URL**

`[](#__codelineno-10-1) https://<rdaf-aia-platform-ip-address>/api/portal/rdac/invokeAPI`

[Sample getReport API Request](#__tabbed_6_1)

`[](#__codelineno-11-1) curl -k --location --request POST 'https://192.168.103.40/api/portal/rdac/invokeAPI' \ [](#__codelineno-11-2) --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYjNkN2ExNDQtNDc3NC00MTEwLWEwMzEtZjFmMDhiYTRjYjhiIiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjkwOjg4MDgifQ.cyiMb2Kpi6FDGE8OHIV0zuB4RnK-vy9cbT_ByTeltzA' \ [](#__codelineno-11-3) --header 'Content-Type: application/json' \ [](#__codelineno-11-4) --data '{ [](#__codelineno-11-5)     "serviceRequestDescriptor": { [](#__codelineno-11-6)         "serviceName": "saas-reports", [](#__codelineno-11-7)         "params": { [](#__codelineno-11-8)             "params": [ [](#__codelineno-11-9)                 { [](#__codelineno-11-10)                     "context": { [](#__codelineno-11-11)                         "contextInfo": { [](#__codelineno-11-12)                             "contextIdList": [] [](#__codelineno-11-13)                         }, [](#__codelineno-11-14)                         "id": "user-dashboard-aia-network-assetslist", [](#__codelineno-11-15)                         "name": "aia-network-assetslist", [](#__codelineno-11-16)                         "view-context": { [](#__codelineno-11-17)                             "appName": "user-dashboard", [](#__codelineno-11-18)                             "pageName": "aia-network-assetslist" [](#__codelineno-11-19)                         } [](#__codelineno-11-20)                     }, [](#__codelineno-11-21)                     "dashboardId": "Total Assets Details", [](#__codelineno-11-22)                     "reportId": "dynamic_v2_tabular_report_0_0", [](#__codelineno-11-23)                     "properties": {"offset": 0, "maxResults": 2}, [](#__codelineno-11-24)                     "filters": [] [](#__codelineno-11-25)                 }]}, [](#__codelineno-11-26)                 "methodName": "getReport" [](#__codelineno-11-27)             }}'`

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

`[](#__codelineno-12-1) { [](#__codelineno-12-2)     "completed": "2022-12-27T08:27:14.119707", [](#__codelineno-12-3)     "created": "2022-12-27T08:27:13.785768", [](#__codelineno-12-4)     "serviceError": "none", [](#__codelineno-12-5)     "serviceResult": { [](#__codelineno-12-6)         "dataResults": [ [](#__codelineno-12-7)             { [](#__codelineno-12-8)                 "__mode": "AUTO", [](#__codelineno-12-9)                 "__rma_new_sn__": "Not Available", [](#__codelineno-12-10)                 "__rma_old_sn__": "Not Available", [](#__codelineno-12-11)                 "__state": "ACTIVE", [](#__codelineno-12-12)                 "__state_updated_time": "12/27/2022 06:58:28 AM ", [](#__codelineno-12-13)                 "address": "Not Available", [](#__codelineno-12-14)                 "admin_down_eth_ports": 125, [](#__codelineno-12-15)                 "api_status": "Not Applicable", [](#__codelineno-12-16)                 "apic_node_dn": "Not Applicable", [](#__codelineno-12-17)                 "apic_pod_id": "Not Applicable", [](#__codelineno-12-18)                 "apic_role": "Not Applicable", [](#__codelineno-12-19)                 "asset_id": "e42f38259c3441ca4ae05914144ac23f", [](#__codelineno-12-20)                 "asset_type": "Hardware", [](#__codelineno-12-21)                 "bucket_id": "21e31d728718dc98054d6839b124445c", [](#__codelineno-12-22)                 "cafm_code": "AB22-05", [](#__codelineno-12-23)                 "cdp_global_deviceId": "lcaabcs14001-2AX52.acme.org(FGE29017ABC)", [](#__codelineno-12-24)                 "child_devices": 0, [](#__codelineno-12-25)                 "city": "Pleasanton", [](#__codelineno-12-26)                 "closet_Id": "RAISEDFLOOR", [](#__codelineno-12-27)                 "contract_coverage": "Not Available", [](#__codelineno-12-28)                 "count_": 1, [](#__codelineno-12-29)                 "country": "Not Available", [](#__codelineno-12-30)                 "created_time": "12/27/2022 06:58:43 AM ", [](#__codelineno-12-31)                 "customer_acceptable_sw_version": "Not Available", [](#__codelineno-12-32)                 "customer_approved_sw_version": "7.0(3)I7(8)", [](#__codelineno-12-33)                 "customer_category": "DC Fabric LAN", [](#__codelineno-12-34)                 "customer_certified_replacement": "Not Available", [](#__codelineno-12-35)                 "customer_equipment_type": "Acme Service Switch", [](#__codelineno-12-36)                 "customer_por_generation": "N", [](#__codelineno-12-37)                 "customer_por_generation_Exec": "N", [](#__codelineno-12-38)                 "customer_topological_tier": "LAN Device", [](#__codelineno-12-39)                 "customer_zone": "14", [](#__codelineno-12-40)                 "device_additional_ips": "192.168.168.2,192.168.168.1", [](#__codelineno-12-41)                 "device_family_engr": "9508", [](#__codelineno-12-42)                 "device_family_exec": "9508", [](#__codelineno-12-43)                 "device_role": "AGGREGATE", [](#__codelineno-12-44)                 "dns_name": "lcaabcs14001-mgmt.acme.org", [](#__codelineno-12-45)                 "dot1x_sw_support": "Not Applicable", [](#__codelineno-12-46)                 "dot1x_system": "Not Applicable", [](#__codelineno-12-47)                 "down_eth_ports": 140, [](#__codelineno-12-48)                 "down_ports_categorization": "9+", [](#__codelineno-12-49)                 "equipment_age": "Not Available", [](#__codelineno-12-50)                 "equipment_name": "N9K-C9508", [](#__codelineno-12-51)                 "equipment_type": "CHASSIS", [](#__codelineno-12-52)                 "fex_description": "Not Available", [](#__codelineno-12-53)                 "fex_grid": "Not Available", [](#__codelineno-12-54)                 "fex_model": "Not Available", [](#__codelineno-12-55)                 "fex_name": "Not Available", [](#__codelineno-12-56)                 "fex_number": "Not Available", [](#__codelineno-12-57)                 "fex_serial": "Not Available", [](#__codelineno-12-58)                 "fex_state": "Not Available", [](#__codelineno-12-59)                 "first_seen": "12/26/2022 03:51:33 AM ", [](#__codelineno-12-60)                 "floor_Id": 2, [](#__codelineno-12-61)                 "grid_Id": "2AX52", [](#__codelineno-12-62)                 "hostname": "lcaabcs14001-2AX52", [](#__codelineno-12-63)                 "hw_expiring_qtr": "Not Available", [](#__codelineno-12-64)                 "hw_expiring_year": "Not Available", [](#__codelineno-12-65)                 "hw_ldos_string": "No EOL", [](#__codelineno-12-66)                 "hw_revision": "Missing HW Revision", [](#__codelineno-12-67)                 "hw_status": "No EOL", [](#__codelineno-12-68)                 "id": "user-dashboard-aia-network-drilldown-app", [](#__codelineno-12-69)                 "ip_address": "192.168.163.228", [](#__codelineno-12-70)                 "is_parent": "Yes", [](#__codelineno-12-71)                 "is_poe_capable": "No", [](#__codelineno-12-72)                 "last_qtr_of_support": "Not Available", [](#__codelineno-12-73)                 "last_seen": "12/26/2022 03:51:33 AM ", [](#__codelineno-12-74)                 "last_updated_time": "12/27/2022 06:58:44 AM ", [](#__codelineno-12-75)                 "last_year_of_support": "Not Available", [](#__codelineno-12-76)                 "latitude": 0.0, [](#__codelineno-12-77)                 "longitude": 0.0, [](#__codelineno-12-78)                 "mgmt_ip": "192.168.163.228", [](#__codelineno-12-79)                 "ntwk_license_name": "Not Available", [](#__codelineno-12-80)                 ... [](#__codelineno-12-81)                 ... [](#__codelineno-12-82)                 "sys_uptime_days": ">180", [](#__codelineno-12-83)                 "system_vendor_os": "Cisco NX-OS", [](#__codelineno-12-84)                 "system_vendor_sub_id": "12.3.1.3.1467", [](#__codelineno-12-85)                 "timestamp": "2022-12-27T07:08:55.913324", [](#__codelineno-12-86)                 "total_eth_ports": 769, [](#__codelineno-12-87)                 "up_eth_ports": 629, [](#__codelineno-12-88)                 "up_ports_categorization": "6+", [](#__codelineno-12-89)                 "uptime": 193, [](#__codelineno-12-90)                 "uptime_since": "06/17/2022", [](#__codelineno-12-91)                 "vendor": "Cisco", [](#__codelineno-12-92)                 "vpc_dns": "Not Available", [](#__codelineno-12-93)                 "vpc_peer_device_ip": "10.0.0.2", [](#__codelineno-12-94)                 "zone_alias_name": "Acme 14(M) - Service" [](#__codelineno-12-95)             }, [](#__codelineno-12-96)             { [](#__codelineno-12-97)                 ... [](#__codelineno-12-98)                 ... [](#__codelineno-12-99)             } [](#__codelineno-12-100)         ], [](#__codelineno-12-101)         "hasMoreResults": true, [](#__codelineno-12-102)         "last_sort_results": [ [](#__codelineno-12-103)             1672124935913, [](#__codelineno-12-104)             "4fe522a4590115b807844edcc82c88de" [](#__codelineno-12-105)         ], [](#__codelineno-12-106)         "properties": { [](#__codelineno-12-107)             "maxResults": 2, [](#__codelineno-12-108)             "offset": 0 [](#__codelineno-12-109)         }, [](#__codelineno-12-110)         "reportMetaData": { [](#__codelineno-12-111)             "actions": [ [](#__codelineno-12-112)                 { [](#__codelineno-12-113)                     "actionCondition": { [](#__codelineno-12-114)                         "actionControl": "SHOW_IF", [](#__codelineno-12-115)                         "conditionalField": [ [](#__codelineno-12-116)                             { [](#__codelineno-12-117)                                 "conditionType": "EQUAL", [](#__codelineno-12-118)                                 "conditionValue": "CHASSIS", [](#__codelineno-12-119)                                 "fieldId": "equipment_type" [](#__codelineno-12-120)                             } [](#__codelineno-12-121)                         ] [](#__codelineno-12-122)                     }, [](#__codelineno-12-123)                     "appName": "user-dashboard", [](#__codelineno-12-124)                     "drillDownContext": "id", [](#__codelineno-12-125)                     "drillDownLinkField": "dns_name", [](#__codelineno-12-126)                     "identifier": "dns_name", [](#__codelineno-12-127)                     "selectionType": "SINGLE", [](#__codelineno-12-128)                     "stateName": "app.featureapp", [](#__codelineno-12-129)                     "title": "View Details", [](#__codelineno-12-130)                     "type": "GO_TO_APP_STATE" [](#__codelineno-12-131)                 } [](#__codelineno-12-132)             ], [](#__codelineno-12-133)             "export": true, [](#__codelineno-12-134)             "filtering": false, [](#__codelineno-12-135)             "identifier": "user-dashboard-aia-network-assetslist_0", [](#__codelineno-12-136)             "paginated": true, [](#__codelineno-12-137)             "reportColumnDefinitionList": [ [](#__codelineno-12-138)                 { [](#__codelineno-12-139)                     "hidden": false, [](#__codelineno-12-140)                     "id": "org_id", [](#__codelineno-12-141)                     "identifier": "org_id", [](#__codelineno-12-142)                     "key": true, [](#__codelineno-12-143)                     "sortable": true, [](#__codelineno-12-144)                     "title": "Organization ID", [](#__codelineno-12-145)                     "type": "TEXT", [](#__codelineno-12-146)                     "visible": false [](#__codelineno-12-147)                 }, [](#__codelineno-12-148)                 { [](#__codelineno-12-149)                     ... [](#__codelineno-12-150)                     ... [](#__codelineno-12-151)                 } [](#__codelineno-12-152)             ], [](#__codelineno-12-153)             "sorting": true, [](#__codelineno-12-154)             "title": "Assets Details" [](#__codelineno-12-155)         }, [](#__codelineno-12-156)         "totalResults": 11581 [](#__codelineno-12-157)     } [](#__codelineno-12-158) }`

*   The `last_sort_results` parameter

The response contains the **last\_sort\_results** array of values in data of `serviceResult` for each API query, as shown in above sample API response. Use the **last\_sort\_results** parameter's values from last API response to get next batch of records.

[Sample API Request with last\_sort\_results Parameter](#__tabbed_8_1)

`[](#__codelineno-13-1) curl -k --location --request POST 'https://192.168.103.40/api/portal/rdac/invokeAPI' \ [](#__codelineno-13-2) --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYjNkN2ExNDQtNDc3NC00MTEwLWEwMzEtZjFmMDhiYTRjYjhiIiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjkwOjg4MDgifQ.cyiMb2Kpi6FDGE8OHIV0zuB4RnK-vy9cbT_ByTeltzA' \ [](#__codelineno-13-3) --header 'Content-Type: application/json' \ [](#__codelineno-13-4) --data '{ [](#__codelineno-13-5)     "serviceRequestDescriptor": { [](#__codelineno-13-6)         "serviceName": "saas-reports", [](#__codelineno-13-7)         "params": { [](#__codelineno-13-8)             "params": [ [](#__codelineno-13-9)                 { [](#__codelineno-13-10)                     "context": { [](#__codelineno-13-11)                         "contextInfo": { [](#__codelineno-13-12)                             "contextIdList": [] [](#__codelineno-13-13)                         }, [](#__codelineno-13-14)                         "id": "user-dashboard-aia-network-assetslist", [](#__codelineno-13-15)                         "name": "aia-network-assetslist", [](#__codelineno-13-16)                         "view-context": { [](#__codelineno-13-17)                             "appName": "user-dashboard", [](#__codelineno-13-18)                             "pageName": "aia-network-assetslist" [](#__codelineno-13-19)                         } [](#__codelineno-13-20)                     }, [](#__codelineno-13-21)                     "dashboardId": "Total Assets Details", [](#__codelineno-13-22)                     "reportId": "dynamic_v2_tabular_report_0_0", [](#__codelineno-13-23)                     "properties": { "maxResults": 2,  [](#__codelineno-13-24)                                     "last_sort_results": [ [](#__codelineno-13-25)                                         1670392980290, [](#__codelineno-13-26)                                         "288b473baa5b1d47006f7b313b336f3e" [](#__codelineno-13-27)                                     ] [](#__codelineno-13-28)                                 }, [](#__codelineno-13-29)                 "filters": [] [](#__codelineno-13-30)                 }]}, [](#__codelineno-13-31)                 "methodName": "getReport" [](#__codelineno-13-32)             }}'`

**Applying filters to limit the results:**

Below is a sample API request to filter the device's **device\_role** is either `ACCESS` or `AGGREGATE`

[Sample API request with filter](#__tabbed_9_1)

`[](#__codelineno-14-1) curl -k --location --request POST 'https://192.168.103.40/api/portal/rdac/invokeAPI' \ [](#__codelineno-14-2) --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYjNkN2ExNDQtNDc3NC00MTEwLWEwMzEtZjFmMDhiYTRjYjhiIiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjkwOjg4MDgifQ.cyiMb2Kpi6FDGE8OHIV0zuB4RnK-vy9cbT_ByTeltzA' \ [](#__codelineno-14-3) --header 'Content-Type: application/json' \ [](#__codelineno-14-4) --data '{ [](#__codelineno-14-5)     "serviceRequestDescriptor": { [](#__codelineno-14-6)         "serviceName": "saas-reports", [](#__codelineno-14-7)         "params": { [](#__codelineno-14-8)             "params": [ [](#__codelineno-14-9)                 { [](#__codelineno-14-10)                     "context": { [](#__codelineno-14-11)                         "contextInfo": { [](#__codelineno-14-12)                             "contextIdList": [] [](#__codelineno-14-13)                         }, [](#__codelineno-14-14)                         "id": "user-dashboard-aia-network-assetslist", [](#__codelineno-14-15)                         "name": "aia-network-assetslist", [](#__codelineno-14-16)                         "view-context": { [](#__codelineno-14-17)                             "appName": "user-dashboard", [](#__codelineno-14-18)                             "pageName": "aia-network-assetslist" [](#__codelineno-14-19)                         } [](#__codelineno-14-20)                     }, [](#__codelineno-14-21)                     "dashboardId": "Total Assets Details", [](#__codelineno-14-22)                     "reportId": "dynamic_v2_tabular_report_0_0", [](#__codelineno-14-23)                     "properties": {}, [](#__codelineno-14-24)                     "filters": [ [](#__codelineno-14-25)                         { [](#__codelineno-14-26)                             "column-id": "device_role", [](#__codelineno-14-27)                             "column-type": "TEXT", [](#__codelineno-14-28)                             "condition": "in", [](#__codelineno-14-29)                             "values": [ [](#__codelineno-14-30)                                 "ACCESS", [](#__codelineno-14-31)                                 "AGGREGATE" [](#__codelineno-14-32)                             ] [](#__codelineno-14-33)                         } [](#__codelineno-14-34)                     ]     [](#__codelineno-14-35)                 }]}, [](#__codelineno-14-36)                 "methodName": "getReport" [](#__codelineno-14-37)             }}'`

Below is a sample request to get Incidents report data with filter created time less than 24 hours

`[](#__codelineno-15-1) curl -k --location 'http://192.168.103.40/rdac/services/invokeJson' \ [](#__codelineno-15-2) --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYjNkN2ExNDQtNDc3NC00MTEwLWEwMzEtZjFmMDhiYTRjYjhiIiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjkwOjg4MDgifQ.cyiMb2Kpi6FDGE8OHIV0zuB4RnK-vy9cbT_ByTeltzA' \ [](#__codelineno-15-3) --header 'Content-Type: application/json' \ [](#__codelineno-15-4) --data '{ [](#__codelineno-15-5)     "serviceRequestDescriptor": { [](#__codelineno-15-6)         "serviceName": "saas-reports", [](#__codelineno-15-7)         "version": "*", [](#__codelineno-15-8)         "params": { [](#__codelineno-15-9)             "params": [ [](#__codelineno-15-10)                 { [](#__codelineno-15-11)                     "context": { [](#__codelineno-15-12)                         "contextInfo": { [](#__codelineno-15-13)                             "contextIdList": [] [](#__codelineno-15-14)                         }, [](#__codelineno-15-15)                         "id": "user-dashboard-oia-incidents-os-template", [](#__codelineno-15-16)                         "name": "user-dashboard-oia-incidents-os-template", [](#__codelineno-15-17)                         "view-context": { [](#__codelineno-15-18)                             "appName": "user-dashboard", [](#__codelineno-15-19)                             "pageName": "oia-incidents-os-template" [](#__codelineno-15-20)                         } [](#__codelineno-15-21)                     }, [](#__codelineno-15-22)                     "dashboardId": "incidents", [](#__codelineno-15-23)                     "filters": [ [](#__codelineno-15-24)                         { [](#__codelineno-15-25)                             "column-id": "i_created_ts", [](#__codelineno-15-26)                             "column-type": "DATETIME", [](#__codelineno-15-27)                             "condition": ">", [](#__codelineno-15-28)                             "timeFilter": true, [](#__codelineno-15-29)                             "values": [ [](#__codelineno-15-30)                                 "{\"type\":\"relative\",\"value\":\"-24\",\"units\":\"hours\"}" [](#__codelineno-15-31)                             ] [](#__codelineno-15-32)                         } [](#__codelineno-15-33)                     ], [](#__codelineno-15-34)                     "reportId": "dynamic_v2_tabular_report_0_0", [](#__codelineno-15-35)                     "properties": { [](#__codelineno-15-36)                         "offset": 0, [](#__codelineno-15-37)                         "maxResults": 100 [](#__codelineno-15-38)                     } [](#__codelineno-15-39)                 } [](#__codelineno-15-40)             ] [](#__codelineno-15-41)         }, [](#__codelineno-15-42)         "methodName": "getReport", [](#__codelineno-15-43)         "ignoreCall": true, [](#__codelineno-15-44)         "parseOutput": true [](#__codelineno-15-45)     } [](#__codelineno-15-46) }'`

Below is a sample request to get Alerts report data with filters created time less than 24 hours and Severity High

`[](#__codelineno-16-1) curl -k --location 'http://192.168.103.40/rdac/services/invokeJson' \ [](#__codelineno-16-2) --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYjNkN2ExNDQtNDc3NC00MTEwLWEwMzEtZjFmMDhiYTRjYjhiIiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjkwOjg4MDgifQ.cyiMb2Kpi6FDGE8OHIV0zuB4RnK-vy9cbT_ByTeltzA' \ [](#__codelineno-16-3) --header 'Content-Type: application/json' \ [](#__codelineno-16-4) --data '{ [](#__codelineno-16-5)     "serviceRequestDescriptor": { [](#__codelineno-16-6)         "serviceName": "saas-reports", [](#__codelineno-16-7)         "version": "*", [](#__codelineno-16-8)         "params": { [](#__codelineno-16-9)             "params": [ [](#__codelineno-16-10)                 { [](#__codelineno-16-11)                     "context": { [](#__codelineno-16-12)                         "contextInfo": { [](#__codelineno-16-13)                             "contextIdList": [] [](#__codelineno-16-14)                         }, [](#__codelineno-16-15)                         "id": "user-dashboard-oia-alerts-os", [](#__codelineno-16-16)                         "name": "user-dashboard-oia-alerts-os", [](#__codelineno-16-17)                         "view-context": { [](#__codelineno-16-18)                             "appName": "user-dashboard", [](#__codelineno-16-19)                             "pageName": "oia-alerts-os" [](#__codelineno-16-20)                         } [](#__codelineno-16-21)                     }, [](#__codelineno-16-22)                     "dashboardId": "alerts", [](#__codelineno-16-23)                     "filters": [ [](#__codelineno-16-24)                         { [](#__codelineno-16-25)                             "column-id": "a_updated_ts", [](#__codelineno-16-26)                             "column-type": "DATETIME", [](#__codelineno-16-27)                             "condition": ">", [](#__codelineno-16-28)                             "values": [ [](#__codelineno-16-29)                                 "{\"type\":\"relative\",\"value\":\"-24\",\"units\":\"hours\"}" [](#__codelineno-16-30)                             ] [](#__codelineno-16-31)                         }, [](#__codelineno-16-32)                         { [](#__codelineno-16-33)                             "column-id": "a_severity", [](#__codelineno-16-34)                             "column-type": "TEXT", [](#__codelineno-16-35)                             "condition": "in", [](#__codelineno-16-36)                             "values": [ [](#__codelineno-16-37)                                 "CRITICAL" [](#__codelineno-16-38)                             ] [](#__codelineno-16-39)                         } [](#__codelineno-16-40)                     ], [](#__codelineno-16-41)                     "reportId": "dynamic_v2_tabular_report_0_0", [](#__codelineno-16-42)                     "properties": { [](#__codelineno-16-43)                         "offset": 0, [](#__codelineno-16-44)                         "maxResults": 100 [](#__codelineno-16-45)                     } [](#__codelineno-16-46)                 } [](#__codelineno-16-47)             ] [](#__codelineno-16-48)         }, [](#__codelineno-16-49)         "methodName": "getReport", [](#__codelineno-16-50)         "ignoreCall": true, [](#__codelineno-16-51)         "parseOutput": true [](#__codelineno-16-52)     } [](#__codelineno-16-53) }'`

### **1.4** ****PStream data API using offline files****

API to get data from persistent Stream using previously created data files. These data files are created after the ingestion of data into Persistent Stream is complete. The data files that are in csv format, have all columns from Persistent Stream are split and stored as compressed gz files. They are named as data\_1.gz,data\_2.g, etc.

Note: It is recommended to use these new API’s to get larger datasets (e.g. ADM)

The API’s (getExportChunkList and downloadObject) enable users to get the latest file location of a stream and download the data.

**getExportChunkList** - API method to get location of latest chunk files for a stream. Response will have chunk object details in comma separated list

**API Request URL**

`[](#__codelineno-17-1) https://<rdaf-aia-platform-ip-address>/api/portal/rdac/invokeService/getExportChunkLis`

[Sample API Request](#__tabbed_10_1)

`[](#__codelineno-18-1) curl -k --location --request POST 'https://192.168.108.94/api/portal/rdac/invokeService/getExportChunkList' \ [](#__codelineno-18-2) --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTlhYzI2YTgtOGMxYy00MzQ3LWFhMTMtM2Y3OWQwNWJkZGM2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjQ1Ojg4MDgifQ.oLAQ2sY87gp3r4MGGG9DlGO3Naa4MbBb7JdYni-a2kg' \ [](#__codelineno-18-3) --header 'Content-Type: application/json' \ [](#__codelineno-18-4) --data-raw '{ [](#__codelineno-18-5)     "pstreamName": "aia_adm" [](#__codelineno-18-6) }'`

**API Request Parameters**

| Parameter | Required | Type | Description |
| --- | --- | --- | --- |
| pstreamName | yes | string | Name of the persistent stream to get latest export job details |

[Sample API Response](#__tabbed_11_1)

`[](#__codelineno-19-1) { [](#__codelineno-19-2)     "data": { [](#__codelineno-19-3)         "_id": "4458a6a13c0688f0cd0c6d8a1d4e02c6", [](#__codelineno-19-4)         "_index": "bc7eec6269c244aa8bc58a725e208a8d-stream-4632cdce-rda_system_collector_export_job_status", [](#__codelineno-19-5)         "_score": null, [](#__codelineno-19-6)         "chunk_objects": "aia_adm-f780a9a6/data_1.gz,aia_adm-f780a9a6/data_2.gz,aia_adm-f780a9a6/data_3.gz,aia_adm-f780a9a6/data_4.gz,aia_adm-f780a9a6/data_5.gz,aia_adm-f780a9a6/data_6.gz,aia_adm-f780a9a6/data_7.gz,aia_adm-f780a9a6/data_8.gz,aia_adm-f780a9a6/data_9.gz,aia_adm-f780a9a6/data_10.gz,aia_adm-f780a9a6/data_11.gz,aia_adm-f780a9a6/data_12.gz,aia_adm-f780a9a6/data_13.gz,aia_adm-f780a9a6/data_14.gz,aia_adm-f780a9a6/data_15.gz,aia_adm-f780a9a6/data_16.gz,aia_adm-f780a9a6/data_17.gz,aia_adm-f780a9a6/data_18.gz,aia_adm-f780a9a6/data_19.gz,aia_adm-f780a9a6/data_20.gz,aia_adm-f780a9a6/data_21.gz,aia_adm-f780a9a6/data_22.gz,aia_adm-f780a9a6/data_23.gz,aia_adm-f780a9a6/data_24.gz,aia_adm-f780a9a6/data_25.gz", [](#__codelineno-19-7)         "count_": 1, [](#__codelineno-19-8)         "export_job_name": "aia_adm-f780a9a6", [](#__codelineno-19-9)         "index_name": "bc7eec6269c244aa8bc58a725e208a8d-stream-6467bb64-aia_adm-replace-0ed08cca", [](#__codelineno-19-10)         "row_count": 13621162, [](#__codelineno-19-11)         "sort": [ [](#__codelineno-19-12)             1676279406032, [](#__codelineno-19-13)             "4458a6a13c0688f0cd0c6d8a1d4e02c6" [](#__codelineno-19-14)         ], [](#__codelineno-19-15)         "status": "Completed", [](#__codelineno-19-16)         "stream": "aia_adm", [](#__codelineno-19-17)         "timestamp": "2023-02-13T09:10:06.032462" [](#__codelineno-19-18)     }, [](#__codelineno-19-19)     "now": "2023-02-15T09:43:12.091051", [](#__codelineno-19-20)     "reason": "", [](#__codelineno-19-21)     "status": "ok" [](#__codelineno-19-22) }`

**downloadObject** - API method to download the exported Persistent Stream data chunk objects

This API expects chunk object name received from the response of getExportChunkList API as explained in the previous section ( refer to getExportChunkList API section)

This API response will be a binary output.

*   Redirect the single downloadObject API response via CLI to a .gz file, decompress the .gz file using a gzip to decompress to a csv file. The csv will have data that includes all the columns from Persistent Stream.
    
*   If the Persistent Stream export has more than one chunk object, getExportChunkList API response will have comma separated list of chunk objects.
    

[Example](#__tabbed_12_1)

`[](#__codelineno-20-1) aia_adm-f780a9a6/data_1.gz, aia_adm-f780a9a6/data_2.gz, aia_adm-f780a9a6/data_3.gz,...`

Users are expected to download each chunk object (data\_1.gz, data\_2.gz,...) separately and decompress to get the complete data (dataset)

Note

Users can also use API in a programmatic way using Python to get the complete data.

**API Request URL**

`[](#__codelineno-21-1) https://<rdaf-aia-platform-ip-address>/api/portal/rdac/invokeService/downloadObject`

[Sample API Request](#__tabbed_13_1)

`[](#__codelineno-22-1) curl -k --location 'https://192.168.108.94/api/portal/rdac/invokeService/downloadObject' \ [](#__codelineno-22-2) --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiYTlhYzI2YTgtOGMxYy00MzQ3LWFhMTMtM2Y3OWQwNWJkZGM2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjQ1Ojg4MDgifQ.oLAQ2sY87gp3r4MGGG9DlGO3Naa4MbBb7JdYni-a2kg' \ [](#__codelineno-22-3) --header 'Content-Type: application/json' \ [](#__codelineno-22-4) --header 'Connection: keep-alive' \ [](#__codelineno-22-5) --data '{ [](#__codelineno-22-6)     "objectName": "aia_adm-f780a9a6/data_1.gz" [](#__codelineno-22-7) }' --output data_1.gz`

**API Request Parameters**

| Parameter | Required | Type | Description |
| --- | --- | --- | --- |
| objectName | yes | string | Name of the exported chunk object |

**Example to get a csv data file from .gz file**

*   From command line using gzip tool:

 `[](#__codelineno-23-1)  gzip -c -d data_1.gz > data_1.csv`

Note

Users can other tools to decompress the gz files (e.g. 7z, etc)

*   Programmatic (using python) way to retrieve data:

`[](#__codelineno-24-1) compressed_file = io.BytesIO(api_response) [](#__codelineno-24-2) with gzip.open(compressed_file, 'rt') as file: [](#__codelineno-24-3)    with open("data_1.csv", 'w') as output: [](#__codelineno-24-4)        output.write(file.read())`

Users can call above RESTful APIs using get\_pstream\_exported\_data.py python module provided in the [package](https://macaw-amer.s3.amazonaws.com/releases/AIA/7.0.6/cfx_rda_aia_restful_api-v7.0.6.zip "Click Here")
.

API Response will be in compressed csv gzip bytes format and will include all columns from Persistent Stream.

2\. Python Module
-----------------

To call RESTful APIs of RDAF platform's AIA/OIA application, users can create their own python script with the help of **api\_client** python module.

To download the Python package [Click Here](https://macaw-amer.s3.amazonaws.com/releases/AIA/7.0.6/cfx_rda_aia_restful_api-v7.0.6.zip "Click Here")

Note

Once users unzip the package file, it will create scripts directory with python modules.

**Prerequisites for python module:**

*   **requests** python HTTP library
    
*   **Usage of `api_client` python module:**
    

**1.** Import `APIGateway` class from `api_client` module and use `post_getReport` and `post_queryPstream` methods.

**2.** Need to provide the RDAF platform's ip address and `Authorization-Token` details while creating an instance to `APIGateway` class. Below is the example to pass configuration details to `APIGateway`

`[](#__codelineno-25-1) from api_client import APIGateway [](#__codelineno-25-2) [](#__codelineno-25-3) login_details = {"host": host, "Authorization-Token": token} [](#__codelineno-25-4) [](#__codelineno-25-5) client = APIGateway(**login_details)`

**3.** Use `post_getReport` method from `APIGateway` to query `getReport` API, below are the inputs needed for `post_getReport` method.

`[](#__codelineno-26-1) Parameters: [](#__codelineno-26-2) [](#__codelineno-26-3)            pageName: str (Name of AIA/OIA page that has the report) [](#__codelineno-26-4)            dashboardId: str (dashboardId inside the AIA/OIA page) [](#__codelineno-26-5)            reportId: str (Id of the report within the dashboard of AIA/OIA page) [](#__codelineno-26-6)            Properties: dict (offset and maxResults to query) —-> {"offset": 0, "maxResults": 20}`

**4**. Use `post_queryPstream` method from `APIGateway` to query `queryPstream` API, below are the inputs needed for `queryPstream` method.

`[](#__codelineno-27-1) Parameters: [](#__codelineno-27-2) [](#__codelineno-27-3)             name: str (Name of the Persistent Stream) [](#__codelineno-27-4)             query: str (cfxql query to filter, default value is ‘*’) [](#__codelineno-27-5)             maxRows: int (maxRows number) [](#__codelineno-27-6)             last_sort_results: list (last_sort_results from previous query response to get next batch of results, default value is None)`

**5.** Below are examples to query APIs using `post_getReport` and `post_queryPstream` from APIGateway class

`[](#__codelineno-28-1) from api_client import APIGateway [](#__codelineno-28-2) [](#__codelineno-28-3) login_details = {"host": host, "Authorization-Token": token} [](#__codelineno-28-4) [](#__codelineno-28-5) client = APIGateway(**login_details) [](#__codelineno-28-6) [](#__codelineno-28-7) response = client.post_queryPstream(name="aia_network", query="site_type is 'Data Center'", maxRows=20, last_sort_results=[1671454183711, "2362c22cfeda287521595c4a1e15a9cf"])`

Note

It is recommended that users need to retry in case of any error in API response

*   **Usage of get\_report\_api.py and pstream\_query.py**

`[](#__codelineno-29-1) python get_report_api.py --help`

`[](#__codelineno-30-1) usage: get_report_api.py [-h] --host HOST --token TOKEN --page PAGE --dashboard [](#__codelineno-30-2)                         DASHBOARD --report REPORT [--offset OFFSET] [](#__codelineno-30-3)                         [--max_rows MAX_ROWS] [--totalresults]`

*   **Post API Request:**

[Required arguments:](#__tabbed_14_1)

  `[](#__codelineno-31-1)   --host HOST           Provide IP Address of the host as input [](#__codelineno-31-2)   --token TOKEN         Provide Authentication token for authorization [](#__codelineno-31-3)   --page PAGE           Provide pageName of AIA/OIA app [](#__codelineno-31-4)   --dashboard DASHBOARD [](#__codelineno-31-5)                         provide dashboardId of AIA/OIA app page [](#__codelineno-31-6)   --report REPORT       Provide reportId`

[Optional arguments:](#__tabbed_15_1)

  `[](#__codelineno-32-1)   -h, --help            show this help message and exit [](#__codelineno-32-2)   --offset OFFSET       provide offset number as input [](#__codelineno-32-3)   --max_rows MAX_ROWS   Provide max_rows number as input [](#__codelineno-32-4)   --totalresults        Get total rows of the report`

*   **Query for Persistent Stream:**

`[](#__codelineno-33-1) python pstream_query.py --help`

`[](#__codelineno-34-1) usage: pstream_query.py [-h] --host HOST --token TOKEN --name NAME [](#__codelineno-34-2)                         [--query QUERY] [--offset OFFSET] [](#__codelineno-34-3)                         [--max_rows MAX_ROWS] [--filename FILENAME]`

[Required arguments:](#__tabbed_16_1)

  `[](#__codelineno-35-1)   --host HOST          Provide IP Address of the host as input [](#__codelineno-35-2)   --token TOKEN        Provide Authentication token for authorization [](#__codelineno-35-3)   --name NAME          Provide name of the Persistent Stream as input`

[Optional arguments:](#__tabbed_17_1)

  `[](#__codelineno-36-1)   -h, --help           show this help message and exit [](#__codelineno-36-2)   --query QUERY        Provide cfxql query as input [](#__codelineno-36-3)   --offset OFFSET      provide offset number as input [](#__codelineno-36-4)   --max_rows MAX_ROWS  Provide max_rows number as input [](#__codelineno-36-5)   --filename FILENAME  Provide filename or filepath to save results in csv, [](#__codelineno-36-6)                        default filename is <stream_name>_query_results.csv`

[Examples](#__tabbed_18_1)

*   Command to query ADM device details report using getReport API with offset 0 and maxResults 500

`[](#__codelineno-37-1) python get_report_api.pyc --host 192.168.108.50 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiNTk1MWYyZjAtZTdlZi00YWQyLTljYzktZDY1NWFhNzAzNmE2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjU2Ojg4MDgifQ.6bW2L4E_P6cdpmX188vdMLfIDBaTcetm1QBG1cTj1j8" --page aia-adm --report dynamic_v2_tabular_report_0_0 --dashboard "ADM Device Details" --offset 0 --max_rows 500`

*   Command to query CDP/LLDP neighbors report using getReport API with offset 0 and maxResults 100

`[](#__codelineno-38-1) python get_report_api.pyc --host 192.168.108.50 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiNTk1MWYyZjAtZTdlZi00YWQyLTljYzktZDY1NWFhNzAzNmE2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjU2Ojg4MDgifQ.6bW2L4E_P6cdpmX188vdMLfIDBaTcetm1QBG1cTj1j8" --page aia-network-assetslist --report dynamic_v2_tabular_report_0_0 --dashboard "CDP Neighbor Assets" --max_rows 100`

*   Command to query Incidents report using getReport API with offset 0 and maxResults 500

`[](#__codelineno-39-1) python get_report_api.pyc --host 192.168.108.50 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiNTk1MWYyZjAtZTdlZi00YWQyLTljYzktZDY1NWFhNzAzNmE2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjU2Ojg4MDgifQ.6bW2L4E_P6cdpmX188vdMLfIDBaTcetm1QBG1cTj1j8" --page oia-incidents-os-template --report dynamic_v2_tabular_report_0_0 --dashboard incidents --offset 0 --max_rows 500`

*   Command to query Alerts report using getReport API with offset 0 and maxResults 500

`[](#__codelineno-40-1) python get_report_api.pyc --host 192.168.108.50 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiNTk1MWYyZjAtZTdlZi00YWQyLTljYzktZDY1NWFhNzAzNmE2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjU2Ojg4MDgifQ.6bW2L4E_P6cdpmX188vdMLfIDBaTcetm1QBG1cTj1j8" --page ooia-alerts-os --report dynamic_v2_tabular_report_0_0 --dashboard alerts --offset 0 --max_rows 500`

*   Command to query all the rows from aia\_cdp Persistent Stream with max\_rows 100 per batch

`[](#__codelineno-41-1) python pstream_query.pyc --host 192.168.108.50 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiNTk1MWYyZjAtZTdlZi00YWQyLTljYzktZDY1NWFhNzAzNmE2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjU2Ojg4MDgifQ.6bW2L4E_P6cdpmX188vdMLfIDBaTcetm1QBG1cTj1j8" --name aia_cdp --max_rows 100`

*   Command to query all the rows from aia\_network Persistent Stream with max\_rows 500 per batch using filter site\_type is 'Data Center'

`[](#__codelineno-42-1) python pstream_query.pyc --host 192.168.108.50 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZWlkIjoiNTk1MWYyZjAtZTdlZi00YWQyLTljYzktZDY1NWFhNzAzNmE2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjU2Ojg4MDgifQ.6bW2L4E_P6cdpmX188vdMLfIDBaTcetm1QBG1cTj1j8" --name aia_network --query "site_type is 'Data Center'" --max_rows 500`

*   command to query incidents from oia-incidents-stream Persistent Stream with filter i\_priority\_label in \['Critical', 'High'\] and max\_rows value as 100 to get critical and high in priority incidents

`[](#__codelineno-43-1) python pstream_query.pyc --host 10.95.107.126 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoiYWNtZUBjZnguY29tIiwid29ya3NwYWNlaWQiOiJiZDRhMTk0NC0zMTEyLTRlMjYtOTE0MC0wM2QwMDFhNTE5MjUiLCJyZGFjX2FwaV9lbmRwb2ludCI6Imh0dHA6Ly8xMC45NS4xMDcuMTI2Ojg4MDgifQ.50yfMTq_ju-nX41i44_gLYm25HTrzuoYmqMWvJHvhTQ" --name oia-incidents-stream --query "i_priority_label in ['Critical', 'High']" --max_rows 100`

*   command to query alerts from oia-alerts-stream Persistent Stream with filter `a_updated_ts` later than -24 hours to get all alerts updated in last 24 hours

``[](#__codelineno-44-1) python pstream_query.pyc --host 10.95.107.126 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoiYWNtZUBjZnguY29tIiwid29ya3NwYWNlaWQiOiJiZDRhMTk0NC0zMTEyLTRlMjYtOTE0MC0wM2QwMDFhNTE5MjUiLCJyZGFjX2FwaV9lbmRwb2ludCI6Imh0dHA6Ly8xMC45NS4xMDcuMTI2Ojg4MDgifQ.50yfMTq_ju-nX41i44_gLYm25HTrzuoYmqMWvJHvhTQ" --name oia-alerts-stream --query "\`a_updated_ts\` later than -24 hours"``

Users can call getExportChunkList, downloadObject RESTful APIs using get\_pstream\_exported\_data.py python module provided in the package. This script will download and save the files in csv format.

*   Usage of get\_pstream\_exported\_data.py

`[](#__codelineno-45-1) python get_pstream_exported_data.py --help [](#__codelineno-45-2) usage: get_pstream_exported_data.py [-h] --host HOST --token TOKEN --name [](#__codelineno-45-3)                                      NAME [--ssl SSL] [--path PATH]`

*   Get the latest persistent stream exported chunks data

[Optional arguments:](#__tabbed_19_1)

  `[](#__codelineno-46-1)   -h, --help     show this help message and exit [](#__codelineno-46-2)   --ssl SSL      SSL verification True/False, default value False [](#__codelineno-46-3)   --path PATH    Provide path to save csv files`

[Required arguments:](#__tabbed_20_1)

  `[](#__codelineno-47-1)   --host HOST    Provide IP Address of the host as input [](#__codelineno-47-2)   --token TOKEN  Provide Authentication token for authorization [](#__codelineno-47-3)   --name NAME    Provide name of the Persistent Stream as input`

[Examples](#__tabbed_21_1)

**1.** Command to get aia\_adm Persistent Stream exported data in csv files

`[](#__codelineno-48-1) python get_pstream_exported_data.pyc --host 192.168.108.94 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZ [](#__codelineno-48-2) WlkIjoiYTlhYzI2YTgtOGMxYy00MzQ3LWFhMTMtM2Y3OWQwNWJkZGM2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjQ1Ojg4MDgifQ.oLAQ2sY87gp3r4MGGG9DlGO3Naa4MbBb7JdYni-a2kg" --name aia_adm`

**2.** Command to get aia\_adm Persistent Stream exported data in csv files in /tmp/downloads/ path

`[](#__codelineno-49-1) python get_pstream_exported_data.pyc --host 192.168.108.94 --token "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoia3BAY2Z4LmNvbSIsIndvcmtzcGFjZ [](#__codelineno-49-2) WlkIjoiYTlhYzI2YTgtOGMxYy00MzQ3LWFhMTMtM2Y3OWQwNWJkZGM2IiwicmRhY19hcGlfZW5kcG9pbnQiOiJodHRwOi8vMTAuOTUuMTA4LjQ1Ojg4MDgifQ.oLAQ2sY87gp3r4MGGG9DlGO3Naa4MbBb7JdYni-a2kg" --name aia_adm --path /tmp/downloads/`

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!