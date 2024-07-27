 



CloudFabrix RDA Releases
========================

This document captures Release Notes for RDA, AIOPs, AIA releases.

RDAF 3.4.2 Release Notes
------------------------

**__Release Date: 31-May-2024__**

Release-artifacts

**Infra Services tag - 1.0.3.2 (Haproxy)**

**Platform Services and RDA Worker tag - 3.4.2**

**OIA (AIOps) Application - 7.4.2**

**RDAF Deployment CLI - 1.2.2**

**RDA Studio - 3.4.2**

### ****1\. Compatibility****

#### ****1.1 Infra - 1.0.2,1.0.2.1****

#### ****1.2 RDAF - 3.4.1****

#### ****1.3 AIOps - 7.4.1****

### ****2\. New Features****

#### ****2.1 RDAF Platform****

*   **Added support to use swagger API document with API Token**.
    
*   **User role permission validation is added for Swagger APIs**.
    
    Only MSP-admin users are permitted to execute **POST**, **PUT**, and **DELETE** APIs. Other user roles are only permitted to execute GET APIs.
    
*   **Support added for Snapshot feature**.
    
    Admins are able to create, import, export, review and delete Snapshots
    
*   **Added New APIs to Swagger Document**
    
    Added reset password and add organization apis to swagger document
    
*   **Asset Navigator is now populated using graphdb**
    
*   **Ability to add missing columns to Pivot Tables whose 'pivot\_type' is 'extended'**
    
    The values in the pivot column are assessed to determine if there are any missing values, which are then added as columns of the pivot table, with row values 0.
    
*   **New extensions for Inventory and metric collection from Hitachi Ops Center Administrator and Analyzer**.
    
    New extension is added for SSO and non-SSO Ops Center Administrator for collecting inventory information. New extension also added for inventory and metrics collection from Ops Center Analyzer and Analyzer Detailed-View.
    
*   **Support added to optionally store and manage any particular persistent stream data on external Opensearch Cluster**.
    
*   **Logging agent is moved from fluentbit to filebeat**
    
*   **FSM now consumes incident and alert updates from Kafka. Topics: oia-processed-alerts and incidents-master.**
    
*   **Object store page was taking longer time to load**
    
    The process of reading object files from Minio was taking too long. To improve the performance of obtaining RDA object lists, a new pstream is introduced to create meta entries for RDA objects. Additionally, to ensure that the RDA objects' meta pstream is always in sync with Minio, it was added to the sync\_artifact process.
    
*   **Changed http/s proxy configuration to read from minio objects instead of environment to make it easier to change**
    
*   **ITSM ticket added in alerts report for all outbounds.**
    
    The FSM Create Ticket pipeline sends a request to the alert processor to update alerts with the corresponding ITSM ticket number. The Alerts tabular report under the incident drill-down will now display the ITSM ticket number.
    

#### ****2.2 UI****

*   **For time series charts, time slicer options Zoom In and Add Time Filter are set as default**.
    
    If the user wants prior behavior of zooming in by default upon selecting a time range with the mouse, they can set the following in the chartProperties of time series widget mode="**zoom**" in the widget definition of the dashboard.
    
*   **UI Tabular Report Enhancement for Pagination Control**.
    
    Added user input for the page number in paginated tabular report.
    
*   **Audit logs are added for operations on mappers, endpoints, policies, teams and configuration settings.**.
    
    Audit log will be published for create, update and delete operations performed on mappers, endpoints, policies, teams and configuration settings.
    
*   **Topology UI Control Panel Enhancement**
    
    Dashboard widget definition has a new option `inMultiviewContainer` which enables `New View` action button to add a new tab for the additional views.
    
*   **UI Form Framework Enhancement (Table Field)**
    
    UI form field involving display of reports (SELECTOR\_TABLE, SELECTOR\_DIALOG, etc) has additional control property of `table-size` which determines the height of the table field. Possible values can be `small`, `medium`, `large` default value is `medium`
    
*   **Topology UI Feature on save / load data to / from a file**
    
    Topology UI gets new action **Download Data** and **Load Data** with which user can save the current topology & View data to a file and also can load from previously saved file.
    
*   **UI Feature - User Preference on disabling Session Timeout**
    
    User Preference has a new option to turn off session timeout and automatic logout on idle
    
*   **Support for control panel in GeoMap**
    
    Support for the new control panel has been added for GeoMap which shows all the markers and edges from the map in tables. The user can click on markers or edges to select their respected rows in table, select a row from table and zoom to it on map and do much more.
    
*   **For tabular reports, by default local (UI) search is not performed**.
    
    Changed the default search behavior to perform remote search, i.e. `remote_searchable` is set to true by default. If users want local search, they can set it to false in the tabular widget definition. If `remote_searchable_cols` is set, we will honor the fields in here for remote search. If it is not set, we will use up-to 10 TEXT visible columns defined in the table. This number can be configured via `remote_search_columns_count`.
    
*   **Support added for pins on x-axis for time series widget**.
    
    These pins are special markers which can be circle, triangle, square etc. and can be annotated with a single letter inside the shape and also can have a specific color.
    
*   **Browser title will reflect active app tab title**
    
    The browser tab title will be updated to whichever application tab is currently focused
    
*   **Introducing new user preference: Main Navigation Menu tab behavior**
    
    When enabled, this opens the menu selection in a tab appended to the existing opened tabs. When disabled (the default), menu selection replaces opened tabs.
    
*   **UI Feature - Copied to clipboard message**
    
    Copied to clipboard message is shown if a user clicks copy icon button in Code Block.
    
*   **UI Feature - My Downloads button in In-App Notifications**
    
    My Downloads button is added to **In-App Notifications** if the export has huge amount of rows.
    
*   **Slim scrollbar for chart legend**
    
    Chart legend in windows operating system have a slim scrollbar now
    

#### ****2.3 AIOps/Assurance****

*   **3 new policy related fields are added to Incidents and sent to ITSM.**
    
    Policy\_name, correlation\_startat, correlation\_exipresat are added to incident and sent to ITSM. Extend support for customizing Timestamp fields.
    
*   **Support is added to skip ITSM Ticket**.
    
    Support is added to skip ITSM Ticket as specified using the incident-mapping properties `notify-itsm-action-fields` and `notify-itsm-action-stream`. For Resuming ITSM ticket, in itsm-ticket=false cases, the pipeline stream should be read using RDA pipeline and build a pipeline to process it
    
*   **`reviveSuppressedAlerts` Bot support is added to revive suppressed alert or alerts on-demand**.
    
    Ability to revive suppressed alerts on demand is added using the BOT in alert-processor through pipeline. This takes alert Id as input and revives SUPPRESSED alerts. **Revive Suppressed Alerts** property defined in policy will be ignored while reviving alerts. Already CLEARED alerts are not revived using the BOT.
    
*   **View Source Payload Action in Events tabular report of Alert Tracking**.
    
    Source payload of an Event can be viewed using **View Source Payload** action in Events tabular report of Alert Tracking. If size of an source payload is greater than 256kb, it needs to be download using **Download Source Payload** action
    
*   **FSM now consumes incident and alert updates from Kafka. Topics: oia-processed-alerts and incidents-master**.
    
*   **Audit logs for operations on mappers,endpoints,policies,teams and configuration settings**.
    
    Audit log will be published for create, update and delete operations performed on mappers, endpoints, policies, teams and configuration settings.
    
*   **Merged View Alerts and View Details actions in Alert Groups tabular report**.
    
    Merged **View Alerts** and **View Details** actions in Alert Groups tabular report to **View Details** Action. View Details action will have two tabs **Alerts & Alert Group Analytics**.
    
    **1**. **Alerts** - Will show list of alerts correlated to the group.
    
    **2**. **Alert Group Analytics** - Gives analytics data for the group.
    
*   **A New Alert RDA Agent API is introduced which will be used for retrieving all alerts for a given incident source Key**.
    
*   **Enhanced** Alert Details **action in Alerts Tabular report**.
    
    Alert Details action will launch a new dashboard with below pages
    
*   **Alert summary report added on drill down of an alert using Alert Details Action**.
    
    Alert summary report added on drill down of an alert using Alert Details Action. Alert summary report is shown in Alert Detail, Alert Trail and Alert Delta pages
    

Known-issue

Column Selector/Ordering is not supported in Alert Trail and Source Events List Tabular Report of Alert Trail Page.

*   **Added `Correlate` Option to `Revive Suppressed Alerts` to revive and correlate Suppressed Alerts**
    
    Added **Correlate** Option to **Revive Suppressed Alerts** to revive and correlate Suppressed Alerts. When a policy is defined with the option alerts for which suppression window is expired and it will skip applying Suppression/Suppress\_Flapping on reviving and incidents will be created respectively based on the applied correlation policy.
    
*   **Remove references of incident share action from tabular report row level action or from incident summary in incident drill down report**.
    
*   **Policy Name is added as additional filter option in incident tabular report's**.
    
*   **Few columns are removed from remote\_search list, their content can still be searched using advanced filter**.
    
    Columns i\_cluster, i\_correlation\_id, i\_service\_names, i\_priority\_label, i\_config\_items, i\_description, i\_tags, i\_cfx\_incident\_type, i\_comments are removed from remote searchable columns because they were causing high CPU on collector container hence removed these less frequently used fields from it.
    
*   **Retention filter is added to OIA Incident Stream to purge only resolved/closed/cancelled incidents**.
    
    For upgrade setups, the following line should be manually added to the oia-incidents-stream definition from UI: "retention\_purge\_extra\_filter": "i\_state == 'Resolved' OR i\_state == 'Cancelled' OR i\_state == 'Closed'" This will ensure that even after retention-days, incidents are purged from this pstream only if they are resolved, closed or cancelled.
    

#### ****2.4 BOTS****

*   **New extensions for Inventory and metric collection from Hitachi Ops Center Administrator and Analyzer.**
    
    New extension is added for SSO and non-SSO Ops Center Administrator for collecting inventory information. New extension also added for inventory and metrics collection from Ops Center Analyzer and Analyzer Detailed-View.
    
*   **New Extension for inventory collection from Huawei Dorado.**
    
*   **Added option to disable SSL verification check when AppDynamics is configured with custom signed certificates.**
    
*   **Added support for SSH key based authentication for network device extension.**
    
*   **A new extension 'cfxdx-ext-cisco-vmanage' is added to support vManage APIs.**
    
*   **Elasticsearch v2 extension: added option for case insensitive search and delete**
    
    `read-index` bot will perform case-insensitive search by default. `delete-data-by-query` will perform case-sensitive search and delete by default.
    
    Optional parameter `case_insensitive` can be used to change the default behaviour
    
*   **Added enhancement in zabbix-metrics-data bot, to accept the history\_column parameter.**
    
    This enhancement accepts the `history_column` parameter along with `itemid_column` from incoming dataset, by mapping, grouping and batching with `itemid_column` values.
    
*   **HEC support to add-to-index bot in Splunkv2 extension for performance improvements**.
    
    Optional HEC credentials are now accepted which will enable Splunk HEC for add-to-index bot
    

#### ****2.5 Others****

*   NA

### ****3\. Bug Fixes****

#### ****3.1 RDAF Platform****

*   **Issue with converting data type from float to integer when exporting the dashboard to PDF has been fixed. Additionally, datetime values are now converted to the user-selected time zone**.
    
*   **Issue with filters in Global search issue for Service Blueprints widget is fixed**.
    
*   **Sorting fix for Group Counters in Counter Chart**
    
    Group Counters can now be sorted in ascending or descending order, and by Title or Value
    
*   **Delete dashboard action will show list of dashboard groups associated with that dashboard**.
    
    Delete dashboard action will show if any dashboard groups are associated with the dashboard and will allow deletion only if it is not associated with any dashboard group
    
*   **Add support to show dynamic stack in studio**.
    
    Studio used to show static stacks. Added support to show dynamic stack by reading data from pstream
    
*   **When an aggregate value for a group results is null (example: when there is no data in the agg field for a group), the whole timeseries chart used to be broken**.
    
*   **The header of "Pull from Git" report is not showing any data**.
    
*   **Adding layer and node\_type in nodes tabular report for topology control panel**.
    
*   **Fixed issue with dataset creation and update failing when data contains special characters**.
    

#### ****3.2 UI****

*   **Label in timeseries widget no longer gets trimmed because of colon(:) character**.
    
*   **UI gives "503 Service Unavailable" error after successful logout**.
    
*   **Resolved the issue of the missing profile icon for SAML SSO users**
    
*   **Expand neighbor selection dialog no longer shows group nodes**.
    
    The expand neighbor selection dialog will not display nodes of type group node since that is an invalid choice.
    
*   **Display error message when a new pipeline is being creates with an existing pipeline name**.
    
    When creating a new pipeline, if draft pipeline is already existing, it will throw error. If pipeline is edited, it can be saved with same version or a new version.
    

#### ****3.3 AIOps/Assurance****

*   **Fixes an issue wherein a mapper needs to handle both valid as well as invalid JSON**
    
    Added handling in mapper for both valid and invalid JSONs as input. When a valid JSON is provided, the payload is not extracted from the body; instead the body itself is treated as payload.
    
*   **Security vulnerabilities**.
    
    Security vulnerabilities are fixed in TLS cookie, Cacheable HTTPS response & Cookie without HttpOnly flag.
    

#### ****3.4 BOTS****

*   **Fix enrich bots caching temp datasets by default**
    
    Temp datasets will no longer be cached. All normal datasets will be cached by default and will be refreshed every 120 seconds if there was an update
    
*   **Chunked datasets created from pipelines with 'dm:save' bot will appear on the datasets page in the portal**.
    
    Only View data action is supported for chunked datasets other actions like manage data, export and ingest stream are not supported
    
*   **Add generic bot for NDFC**
    

#### ****3.5 Others****

*   NA

### ****4\. Known Issues, Caveats****

*   NA

#### ****4.1 RDAF Platform****

*   **Clicking on "diff preview" button in git dashboard is not showing any data.**
    
*   **Sorting of non TEXT fields in tabular reports don't work as expected when they are not defined in the column filters of the dashboard definition**.
    
*   **Actions on datasets with special characters are not working**.
    
    It is recommended to avoid using any special characters in dataset names while creating them
    
*   **Wrong UserID displayed in audit logs when draft pipeline is added**.
    
    When a draft pipeline is added, the userID column is displayed as `SERVICE` in audit logs instead of the actual userid
    
*   **Snapshot feature skips draft pipelines with special characters**.
    
*   **There may be a discrepancy between the number of draft pipelines shown in the snapshot report and the actual count if any draft pipelines have special characters in their names**.
    
*   **Widgets use a default significant digits**
    
*   **PDF Export feature**.
    
    Pages that have HTML templates not being exported correctly
    
*   **Add filter by list option tabular widget**
    
*   **Support scheduling and email for dashboard export**
    

#### ****4.2 UI****

*   NA

#### ****4.3 AIOps/Assurance****

*   NA

#### ****4.4 Others****

RDAF 3.4.1.1 Release Notes
--------------------------

**__Release Date: 3-Apr-2024__**

Release-artifacts

**Infra Services tag - 1.0.3 & (1.0.3.1 Haproxy)**

**Platform Services and RDA Worker tag - 3.4.1/3.4.1.1**

**OIA (AIOps) Application - 7.4.1/7.4.1.1**

**RDAF Deployment CLI - 1.2.1**

****1\. Compatibility****

****1.1 Infra - 1.0.2,1.0.2.1**** ****1.2 RDAF - 3.4**** ****1.3 AIOps - 7.4****

****2\. New Features****

*   NA

****2.1 RDAF Platform****

*   NA

****2.2 UI****

*   NA  
    ****2.3 AIOps/Assurance****
    
*   NA
    

****2.4 BOTS****

*   NA

****2.5 Others**** \* NA

****3\. Bug Fixes****

*   NA

****3.1 RDAF Platform****

*   **Reflected cross-site scripting vulnerability in webhook server.**
    
    Reflected cross-site scripting vulnerabilities arise when data is copied from a request and echoed into the application's immediate response in an unsafe way.
    

****3.2 UI****

*   **In Topology - Node details were not showing when a user clicks on a node.**
    
    This was specific to nodes that were moved out of a group node.
    

****3.3 AIOps/Assurance****

*   **Enriched and Key Alert Attributes are now sorted in Ascending order by default.**
    
*   **Maximum message size limit was increased for Kafka producer clients.**
    
    There was no explicit max message size limit added for Kafka producer clients, hence the default value of 1 MB was provided. It was observed that for very large messages, the producer was failing with `MSG_SIZE_TOO_LARGE` error. The maximum message size limit is now increased to 64 MB.
    

****3.4 BOTS**** \* NA ****3.5 Others**** \* NA

****4\. Known Issues, Caveats**** \* NA ****4.1 RDAF Platform**** \* NA ****4.2 UI**** \* NA ****4.3 AIOps/Assurance**** \* NA ****4.4 Others**** \* NA

RDAF 3.4.1 Release Notes
------------------------

**__Release Date: 22 March 2024__**

Release-artifacts

**Infra Services tag - 1.0.3 & (1.0.3.1 Haproxy)**

**Platform Services and RDA Worker tag - 3.4.1**

**OIA (AIOps) Application - 7.4.1**

**RDAF Deployment CLI - 1.2.1**

****1\. Compatibility****

****1.1 Infra - 1.0.2,1.0.2.1**** ****1.2 RDAF - 3.4**** ****1.3 AIOps - 7.4****

****2\. New Features****

****2.1 RDAF Infra****

Following is the RDAF Infra service that is upgraded as a part of 3.4.1 release using the tag 1.0.3.1

*   **HAProxy**

****2.2 RDAF Platform****

*   **Added Support to Include CSV Files in Dashboard Export.**
    
    The data from Tabular and Pivot widgets will be exported as CSV files within the Exported Zip file if the 'Include CSV files' option is selected during dashboard export. The maximum number of rows for export is 100,000.
    
*   **Enhanced support to receive SNMP v3 Traps to configure different privacy modes for different IP addresses.**
    
    NA
    

****2.3 UI****

*   NA

****2.4 AIOps/Assurance****

*   **Expose short URL for incidents.**
    
    Instead of exposing long URLs for incidents which get passed to external ticketing system, emails etc., a short URL will be passed for incidents. This will prevent exposure of internal details/context etc.
    
*   **Changed the retention\_days policy to be 365 days for some system created pstreams.**
    
    NA
    
*   **Retaining MinIO configuration changes across upgrades for incident room via pipeline.**
    
    A new IRM agent bot (updateOiaConfigFile) was added which allows updating Incident room specific MinIO based configuration JSON files and also enables retaining the changes when version/release upgrades are done.
    
*   **Enhance match function of JSON mapper to support multiple match conditions.**
    
    Currently `match` function of JSON mapper only returns the first match for a group expression. This is a limitation when there is a need to have multiple match conditions separated by OR condition (`|`). The solution is to pick the first non-null (allows empty string) value among the list of returned matching groups.
    

****2.5 BOTS****

*   **Optional checkbox is added in Zabbix extension to skip SSL verification.**
    
    NA
    

****2.6 Others****

*   NA

****3\. Bug Fixes****

****3.1 RDAF Platform****

*   **Global search is not working for dashboard report in Add/Edit dashboard groups action pop up form.**
    
    In some of the upgrade setups Global search in dashboard report is not working because of realtime column included in search query, which existed in pstream metadata as datetime type column in those setups. Removed that column from search query.
    
*   **Dataset, schema, formatting templates and rda-objects created with leading or trailing tab or spaces has caused the issue for few actions or in enrichment process as its empty.**
    
    Few actions and enrichment process were failing, if dataset, schema, formatting templates and rda-objects name contains leading or trailing tab or spaces. Handled such cases while saving artifacts.
    
*   **If one of the assigned dashboards to the group was deleted, none of the dashboards were loading after that.**
    
    NA
    
*   **Bug fixes in Export to PDF Report.**
    
    Missing some bars in export for mixed bucket charts. Values in piecharts are overlapping
    
*   **Users were unable to view the forecasting graph and insight report.**
    
    ML Dashboards permission issue due to which users were unable to view the forecasting graph and insight report was fixed.
    
*   **Tables in popup report showed up empty.**
    
    Tables in popup report showed up empty and the data was filled only when a manual table refresh was performed.
    
*   **When organizations were updated in user groups, those user groups were not showing up as pre-selections in the Edit Dashboard Groups action form.**
    
    When organizations were added/removed from user groups, those user groups, if they were already assigned in dashboard groups, were not showing up as pre-selections in the Edit Dashboard Groups action form.
    
*   **Minio connectivity failure in proxy setups.**
    
    Worker and Bots failed to connect to Minio, in case http proxy was set and the Minio host was included in NO proxy. Fix was added to check the NO proxy list in such scenario.
    

****3.2 UI****

*   **Removed home page white label settings.**
    
    Since home page is now replaced by landing page, white label settings for the home page have been removed.
    
*   **Datetime columns are not showing in readable format and labels alignment issues in export report.**
    
    Datetime columns are now displayed in a readable format, and labels in time series and bar charts no longer overlap the chart data
    
*   **Tables in popup report showed up empty.**
    
    Tables in popup report showed up empty and the data was filled only when a manual table refresh was performed.
    

****3.3 AIOps/Assurance****

*   **Collab service restarting on HA setup.**
    
    NA
    
*   **Fixed issue with L1, L2/L3 Dashboards where bulk actions like Assign are broken.**
    
    NA
    
*   **Issue in inline enrichment with payload comprising multiple events and not all events have enriched data.**
    
    The issue was observed when inline enrichment, specifically stream enrichment was used against an input payload containing a batch of events. Not all the events were getting enriched, causing an issue when consolidating the enriched data.
    
*   **Fix for issue with Kafka pstreams when adding for external topic.**
    
    When using multiple Kafka pstreams, it is observed that adding a new pstream causes a consumer re-balance across all consumers. This resulted in a situation where a consumer would crash and restart and not have any topic-partitions assigned thereafter. The consumers need to use a different consumer-group to avoid this issue.
    
*   **Revive At time stamp is not getting cleared when an alert gets revived on suppression window expiry.**
    
    When alert is getting revived once the suppression policy window is expired, revived timestamp is staying with the old value. Hence we are seeing old value revived for the alert. Due to this alert is getting picked on every run of Revival job.
    
*   **Some errors were seen when Teams List Cache is getting refreshed.**
    
    Errors were seen during refresh, only when there was no team and was fixed appropriately.
    

****3.4 BOTS****

*   **Bug fixes for CIMC extension BOT.**
    
    When the device doesn't have any data for the BOT, it currently returns empty dataset. With this fix. BOT will now return additional row for the device IP that has no data.
    
*   **Linux Extension bug fixes.**
    
    Fix status event timeout was not running the fallback command when command waits for user input, which is now fixed.
    

****3.5 Others**** \* NA

****4\. Known Issues, Caveats**** \* NA ****4.1 RDAF Platform**** \* NA ****4.2 UI**** \* NA ****4.3 AIOps/Assurance**** \* NA ****4.4 Others**** \* NA

RDAF 3.4/AIOps 7.4 – Release Notes
----------------------------------

**__Release Date: Feb 28 2024__**

**1\. Compatibility**

**1.1 Infra - 1.0.2,1.0.2.1** **1.2 RDAF - 3.3** **1.3 AIOps - 7.3,7.3.0.1**

**2\. New Features**

**2.1 RDAF Infra**

Following are the RDAF Infra services that are upgraded as part of 3.4 release using the tag 1.0.3

*   **NATS**
    
*   **MinIO**
    
*   **MariaDB**
    
*   **OpenSearch**
    
*   **Kafka**
    
*   **Redis**
    
*   **GraphDB**
    

Note

After upgrading the **Kafka Service**, the **Zookeeper** service is no longer needed and will be removed after the upgrade.

**2.2 RDAF Platform**

*   FSM: Provide out of the box models for ITSM ticketing
    
*   FSM Model - Minor Enhancements
    
*   Domain rules based alerting -- Rules were attached as per the requirement
    
*   Conditional purging of data from p-stream
    
*   Added support to Edit dashboard definition within the dashboard
    
*   Scheduled Jobs: Log the activity of cronjobs
    
*   kpi-workbench enhancement and issues
    
*   Manage Scheduler's web server with gunicorn
    
*   Support template for dashboard export
    
*   Add support for Dataset Bounded PStreams
    

Important

With this feature, when the system does not have any pstreams linked to a dataset, we are making unreasonable amount of calls to sync, which results in filling up the logs and also potentially cause collector service to have CPU/memory issues that will eventually cause timeout issues.

**Workaround**: Create an internal pstream that is bounded to the dataset the following way: From the pstreams dashboard, add the following pstream:

**Name**: `rda_system_internal_pstream` In the attributes section, add the following:

`[](#__codelineno-0-1) { [](#__codelineno-0-2) "source_dataset": "rda_system_internal_dataset", [](#__codelineno-0-3) "system_defined": "yes" [](#__codelineno-0-4) }`

*   Support template for dashboard export
    
*   Add multiple markers on a timeseries chart
    
*   Connectivity Chart support
    
*   Showing user globally selected timezone in the date and time fields
    
*   Add back partition identifier field for inbound endpoints
    

**2.3 UI**

*   Visual status feedback provided for certain UI operations
    
*   Increase UI timeout from 30 mins to 60 mins
    
*   UI search filter provided to search across and not just the first selected set of pages
    
*   White label upload image type 'ico
    
*   Topology view enhancements
    
*   Show delete icon on favourite list item hove
    

**2.4 AIOps/Assurance**

*   oia-incident-stream: set default fields with preconfigured datatypes
    
*   Should show only incidents which have ITSM ticket while click on bulk actions on Incidents with External Ticket dashboard report
    
*   Add Show Alert Key or Mapping Logic as an action to Alerts tabular report
    
*   Incident metrics page to show metrics with anomalies using timeseries\_multisource widget
    
*   Enhancement to display the block that is causing error in JSON mapper
    
*   Alerts & Incidents Data Retention default value changed to 30 days instead of 365 days
    
*   Migrate all pages from Incident details to new dashboard
    
*   sqlalchemy 2.0 and latest mysqlclient library to AIOps services
    

**2.5 BOTS**

*   getbackup list bot in NDFC
    
*   DNAC - DR Bot
    

**2.6 Others**

*   NA

**3\. Bug Fixes**

**3.1 RDAF Platform**

*   Schedules are not triggered properly for Service Blueprints with ID containing '('
    
*   ITSM ticketing is missing randomly for some Incidents
    
*   Metrics Analysis and Insights Workbench Dashboard has no data
    
*   MariaDB & APP services restarted
    
*   Service pipeline gets terminates while restarting one of the IRM service instance in HA
    
*   Prometheus alerts intermittently are failing to process at in-line enrichment
    
*   Collector is hanging intermittently and does not process any more nats messages
    
*   Removed py2neo graphDB library
    
*   For SSO user logins added audit log for user activities
    
*   multi-proc-eval is not throwing error but returning original dataframe
    
*   Fixed file browser service errors while adding Organizations
    
*   Removed unnecessary logs from api server
    
*   Blueprint: Scheduled Job not getting executed for some cron expressions
    
*   Webhook server one instance in HA is failing to accept any payload
    
*   Time stamp values should be converted to readable format in some places
    
*   Update enriched attribute with latest value if a value with the same key is already added
    
*   Update inline stream enrichment to handle multiple events in a single payload with some events without enriched data
    
*   Run dataset and stream updates in a fixed length threadpool
    
*   Purge settings values not retained in DB as part of upgrade path
    
*   MariaDB schema update performance issue
    
*   When user is logged in with "organization administrator", the data for "View Dependencies" action is showing incorrectly in the datasets report
    

**3.2 UI**

*   Time filter is not working in "Artifact Dependencies"
    
*   Sorting on row count not working Archives report
    
*   Existing column width is changing, after adding new column from column selector
    
*   Sorting is not working for an 'Enabled' column in Dashboards and Service Blueprints
    
*   Sorting is not working for few of the columns in "view artifacts" action of Tag Management
    

**3.3 AIOps/Assurance**

*   Bulk incident actions data is showing across the organizations
    
*   Manage data action getting error for alert-model dataset
    
*   Noise reduction showing wrong not accounting CLEARED alerts
    
*   Fix issues with OIA config items
    
*   Update enriched attribute with latest value if a value with the same key is already added
    
*   Update inline stream enrichment to handle multiple events in a single payload with some events without enriched data
    

**3.4 BOTS**

*   NA

**3.5 Others**

*   DNAC - Disable filtering in Summary page for Client Count by SSID report
    
*   Network Device Inventory table search for some of the fields is not working when coloring is applied
    
*   DNAC Adoption: wired and wireless clients count do not add up
    
*   DNAC - “Not Applicable” in CLLI list of “Client Counts by Location” Widget
    
*   DNAC - cisco\_dnac\_wireless\_profile pipeline failures
    
*   DNAC - Retail Wireless -> Client count showing 0
    
*   Some specific time filters in Prime dashboards is not working, Need to change timezones in data
    
*   DNAC is getting deleted from stream despite of failure in the collection
    
*   Adoption Dashboard coloring Green and Red based on DNAC reachability status.
    

**4\. Known Issues, Caveats**

*   NA

**4.1 RDAF Platform**

*   NA

**4.2 UI**

*   NA

**4.3 AIOps/Assurance**

*   NA

**4.4 Others**

*   DNAC - Location related fields are being parsed wrongly in RTO page

RDA 3.3/AIOps/AIA 7.3 – Release Notes
-------------------------------------

**__Release Date: Nov 23 2023__**

**RDA/AIOps/AIA New Features/Enhancements**

*   Platform: Data Retention/Archival functionality
*   Platform: Github integration for managing artifacts
*   Platform: Portal UI Menu Management - System Default Landing Page
*   Platform: Portal UI - Add to Favorites
*   Platform: Tag management for rda artifacts
*   Platform: Support from UI to add HTML Templates
*   Platform: Added Live Persistent Stream Stats functionality under Persistent Streams
*   Platform: Added Current Usage stats functionality under Persistent Streams
*   Platform: Support for NDFC Bots
*   Platform: Support for CIMC Bots
*   AIOps: Configurations Report added under Administration to update different configurations at global level for MSP Admin
*   AIOPs: Suppression policy enhancement: Disable revival for sources that don't have clear alerts
*   AIA: HPNA Integration

**System Level Optimization**

*   Platform: FSM HA Enhancements
*   Platform: Context based prefixing of kafka topics
*   Platform: KPI workbench enhancements

**CFDs / Bug Fixes- Resolved**

*   Platform: RBAC Issue - end-user able to see admin artifacts
*   Platform: Health Data and Report Enhancements
*   Platform: Support for Group Label in Mixed Chart Buckets
*   Platform: Campus and Retails Dashboard empty reports issues.
*   Platform: Site Location Issues in Inventory data.
*   Platform: Time zone change from ART to CST in RTO1 & 2 dashboard
*   Platform: Enable scroll bar for Bar and Multi bar charts
*   Platform: Data off for few seconds on when data deletion happening from streams.
*   Platform: Show float values with decimals in multi bar charts
*   Platform: Formatting options for Bar and Multi Bar charts
*   Platform: Share Link to share the all/single tab.
*   Platform: Info icon to be shown when description is added to reports.
*   Platform: Some of the streams are not populated with dnac\_name and dnac\_category columns
*   Platform: Adoption Dashboard to show unique count of Hostnames
*   Platform: Formatting options to be applied on Y axis instead of series columns.
*   Platform: Audit log Ingestion failure on writing data to stream
*   Platform: Clients Dashboard to be fixed with filtering issues.
*   Platform: Advanced Pivots to show more than 1000 rows
*   Platform: Location parsing to needs to be handled differently based in DNACs
*   Platform: X-axis and Secondary Y axis values are not visible properly in dark mode
*   Platform: Adoption Dashboard not to show Not Available for Switch
*   Platform: Adding colors to SSID across the dashboards
*   Platform: Counts in Inventory and Insights pages are not matching.
*   Platform: Some of the Misconfigured APs are showing Device Name as Not Available.
*   Platform: Client Count By SSID Pie charts are showing Not Available
*   Platform: Segment filter option to not allow filtering on report segments
*   Platform: Duplicates Switch data in Wired Dashboard when inventory data is merged with Images
*   Platform: DNAC Pipeline failure fixes
*   Platform: Fix for Https Token/Auth Errors
*   Platform: Security scan issue sysctl configuration fix for multinic
*   Platform: FSM - Use assigned partitions for load distribution of events scheduled for future
*   Platform: FSM now uses DN prefixed topics for events. This is to align with the dn bot that uses DN prefixed topic by default
*   Platform: BMC Bot - Fix Update and Resolve APIs to utilize the multi-threading feature. Fix the corresponding pipelines
*   Platform: BMC - Close the ticket only if it is in the Queued state; otherwise, move tickets in other states to Autofix
*   Platform: BMC - Additional Pipeline, Dataset, Ticketing fixes
*   AIOps: Minutes field in suppression policy
*   AIOps: Support for dependency analysis and reports for all artifacts (pipelines, datasets, dashboards, credentials etc)
*   AIOps: Column filter is not working in dashboard groups
*   AIOps: Column filter is not working in datasets, pipelines and pstreams
*   AIOps: Time filter is not working in datasets
*   AIOps: Suppress flapping alerts policy not working
*   AIOps: Add to Incident feature is not working
*   AIOps: Collab page is timing out
*   AIOps: Add Alert summary to FSM-Collab Activity Page while updating ticket
*   AIOps: Collab page is timing out
*   AIOps: Add alert-key as a searchable column in alerts table
*   AIOps: User click on alert actions row level alert - action popup not aligned
*   AIOps: IP address not updating while update message in correlation parent incident

**Known Issues/Caveats**

*   Platform: Info Icon will not be shown for counter reports
*   Platform: Dashboard export PDF is missing with few of the reports in exported PDF
*   Platform: Dashboard Export showing up with each widget in a single page.
*   AIA: LEP for asset ingester service is not working properly, some times both instances behaving as leaders
*   AIA: SNMP ingestion values overwriting APIC data. Workaround: Ingest APIC files at the end after SNMP ingestions are complete
*   AIA: Smart sorting on interfaces, IP addresses
*   AIA: Customization of dashboards
*   AIA: Notifications support for file downloads, user creation and deletion, file deletion
*   AIA: Edge collector reports (This is not working in macaw based platform release also)
*   AIA: Settings on charts not supporting changing to different charts
*   AIA: No counter filters at the top (Counter charts)
*   AIA: No default sorting for Tabular report - Workaround: Users can sort after opening the report
*   AIA: Manual state transition UI for assets & IPT data (Workaround: Manually update the pipeline with the required Serial Numbers and run the pipeline).
*   AIA: Filter cannot be removed/hidden for POR page
*   AIA: Snapshots are supported only in AIA app (No support at portal level) Workaround: Pipelines can be provided to backup data as needed.
*   AIA: Export for large datasets working up to 200K records

RDA 3.2.2.2/AIOps/AIA 7.2.2.2 – Release Notes
---------------------------------------------

**__Release Date: Oct 8 2023__**

**RDA/AIOps/AIA New Features/Enhancements**

*   Platform: Added url prefix support to Haproxy and portal frontend (support added via environment to values.yaml)
*   Platform: API support for User Groups, Users and Role mappings
*   Platform: Prime Client Sessions Dashboards
*   Platform: Support added for Customer facing portal integration
*   Platform: Dashboard Export for non tabbed view
*   Platform: Dashboard support for User group name as context and use it as filter with in the published Dashboard(s)
*   Platform: Others should be hidden from Bar and Multi Bar charts
*   Platform: Formatting issues of decimal points and Units in Timeseries and Multi Bar and Bar Charts
*   Platform: Fixed Multi Bar chart with scroll bar enabled
*   Platform: Timeseries report enhancement for missing data points to join data points with gap\_interval
*   Platform: Secondary axis support for Multi Bar chart
*   Platform: Added DNAC Category Quick/Group filters in Overall (Global), Wireless, Wired, Health and Insights pages
*   Platform: Coloring support for timeseries series intervals
*   Platform: Group Label support for Timeseries and Secondary Axis reports
*   Platform: Retention Days change to 180 days from 7 days to timeseries pstreams

**System Level Optimization**

*   NA

**CFDs / Bug Fixes- Resolved**

*   Platform: Topology / stack definition support added to User groups context
*   Platform: UI - Fixed User preferences / Save filters
*   Platform: UI - Fixed User preferences / Set as defaults
*   Platform: Topology dashboard fixes
*   Platform: Dark Mode issue for Adoption Dashboard
*   Platform : Fixed issue - searching with IP, search filter showing all records if match is not found
*   AIOps: Highlight more important fields and group fields in the Alert Payload view
*   AIOps: Fixed the issue where alerts not getting resolved when an incident is resolved from the ITSM ticket
*   AIOps: Event Type status showing wrong on View Trail report for repeated alerts
*   AIOps: asset\_ip\_address column is added to remote searchable columns of all the alert dashboards
*   AIOps: Fixed issue for inline pstream base alert enrichment failing due to timeout error
*   AIOps: Update dataset when notification is sent via system audit log stream
*   AIOps: Disable hostname verification for Kafka client on collector
*   AIOps: Ability to resize columns in incident and alert tables

**Known Issues/Caveats**

*   Platform: Row background coloring in Unclaimed Devices report in Overall Page.
*   Platform: Multi Bar secondary axis report x-axis values and secondary axis values are not showing properly in dark mode.
*   Platform: Dashboard Export showing up with each widget in a single page.
*   Platform: Row background coloring in Unclaimed Devices report in Overall Page.
*   Platform: Dashboard export PDF is missing with few of the reports in exported PDF option
*   AIOps: Suppress flapping alerts policy is not working as expected
*   AIOps: Remove team configuration is not properly saving
*   AIOps: UI\_Prefix setup is redirecting to home page after opening an existing dashboard from favorites
*   AIOps: When a new column is added the existing column width is changing
*   AIOps: Resizable column is overlapping on row level actions of all tabular reports
*   AIOps: Unable to resize a column till user comes out of the report, reloads the same report after enabling a column
*   AIOps: Repeat count not increasing properly if the alerts are coming in same batch with same alert key
*   AIops: Alert actions row level popup is not aligned properly at the top level

RDA 3.2.2/AIOps/AIA 7.2.2 – Release Notes
-----------------------------------------

**__Release Date: Aug 23 2023__**

**RDA/AIOps/AIA New Features**

*   Platform: UI support for dark mode
*   Platform: White label - Add brand image to App Page
*   Platform: Add API support for Administrative Operations such as User creation, assigning roles, etc.
*   Platform: Download report using APIs (DNAC)
*   Platform: Enhancements to System Health APIs (DNAC)
*   Platform: Restore existing FSM instances from database
*   Platform: Enhanced opensearch security index purge policy
*   Platform: Making kafka Max message size as 8Mb and kafka automatic topic creation
*   Platform: FSM changes for AOTS and ServiceNow
*   AIOps: Integrating alert\_processor\_companion service
*   AIOps: UI Enhancements
*   AIOps: Support Pstream based suppression policy
*   AIOps: OpsGenie bot changes to support proxy environment
*   AIOps: New OIA service added (alert-processor-companion) as part OIA installation
*   AIOps: Export and import draft pipelines from UI
*   AIOps: Topology dashboard Enhancements

**System Level Optimization**

*   NA

**CFDs - Resolved**

*   Platform: DNAC Version in Adoption Dashboard
*   Platform: Site/Location details for devices and clients
*   Platform: Support for SSID along with Sites
*   Platform: Reorganized reports in order to avoid empty widgets when filters are applied
*   Platform: Banners in dashboards
*   Platform: Region, State, City additional group filters in all dashboards
*   Platform: Non-compliance (pie-chart), Non-Compliance reports in wired dashboard
*   Platform: Not Available for WLC and APs in Adoption Dashboard
*   Platform: SSID timeseries Graph issues
*   Platform: Portal UI - Top level application menu
*   Platform: Portal UI - Set as Landing Page
*   Platform: Convert PStream dashboard into an App with pages (data preview, stats, metadata etc)
*   Platform: Bulk alert clear from Alerts Dashboard not clear all alerts
*   AIOps: Suppression policy not working for dataset based enrichment attributes
*   AIOps: Groupby query for numeric fields does not work
*   AIOps: In dashboards, METADATA was showing only a few columns (Pagination does not work)
*   AIOps: Incident cross launch from SNOW showing empty alerts
*   AIOps: Suppression policy did not apply for a few alert occurrences
*   AIOps: Not able to add formatting templates
*   AIOps: Not updating clear alert status in OpsGenie
*   AIOps: Pipeline verification is failing while publishing even though there is nothing wrong with the pipeline
*   AIOps: Scheduling in suppression policies is not working

**Known Issues/Caveats**

*   Platform: While opening a dashboards from Favorites, dashboard report loading taking time
*   Platform: Blueprints> Audit Report> Verify Source Credentials Issue
*   Platform: Users are created with non-existing group through 'Add' user api
*   AIOps: Burst Policy not working when single event contains multiple alerts

RDA 3.2.1.3/AIOps/AIA 7.2.1.1 – Release Notes
---------------------------------------------

**__Release Date: July 7 2023__**

**RDA/AIOps/AIA New Features**

*   Platform: New rdafk8s infra down/up cmds for k8s environment
*   Platform: Added support for data plane policy generation
*   Platform: Restore existing FSM instances from database
*   AIOps: Added support to post the incoming events to Pstream
*   AIOps: Enhanced UI search filter to search across all the pages and not just the first selected set of pages
*   AIOps: Suppression policy revival enhancements

**System Level Optimization**

*   NA

**CFDs - Resolved**

*   Platform : Mysql errors while purging resolved incident object in FSM service
*   AIOps: In dashboards, METADATA was showing only a few columns (Pagination does not work)
*   AIOps: Incident cross launch from SNOW showing empty alerts
*   AIOps: Suppression policy did not apply for a few alert occurrences
*   AIOps: Not able to add formatting templates
*   AIOps: Not updating clear alert status in OpsGenie
*   AIOps: Pipeline verification is failing while publishing even though there is nothing wrong with the pipeline
*   AIOps: Scheduling in suppression policies is not working

**Known Issues/Caveats**

*   Platform: FSM receiving multiple closure successful notifications while clear alerts with bulk clear from alerts report
*   Platform: When a user opens a dashboards using 'Favorites' dashboard report, loading is taking more time
*   AIOps: No need to specify hours while create weekly suppression policies

RDA 3.2.1/AIOps/AIA 7.2.1 – Release Notes
-----------------------------------------

**__Release Date: June 30 2023__**

**RDA/AIOps/AIA New Features**

*   Platform: FSO edge deployment
*   Platform: New FSM platform service added to both k8s, non-k8s setups (HA and non-HA mode)
*   Platform: FSM bidirectional integration support with BMC Remedy Ticketing
*   Platform: In-Service Software Upgrade (ISSU)
*   Platform: Kafka config changes in k8s(fresh install), non-k8s setups
*   Platform: New rdafk8s infra management commands support added to k8s setups
*   Platform: Added support for data plane policy generation and dataplane configuration to collector service
*   Platform: New "Add to Favorite" feature added to GUI
*   Platform : Enhancements for flattening json and continue\_on\_failure (sink) bots
*   Platform : Retry Support for DNAC bots in case of API failure
*   AIOps: Alerts support for OpsGenie
*   AIOps: Added support to choose icon from icon library
*   AIA: Enabled Bounded Datasets

**System Level Optimization**

*   NA

**CFDs - Resolved**

*   Platform: User deletion failing with 504 error
*   Platform: File browser functionality moved to platform from app level
*   Platform: Fixed file downloads when user login with case sensitivity
*   Platform: Fixed advanced filters at dashboards level
*   Platform: Export of dashboards
*   AIOps: Fixed child pipeline loading issue
*   AIOps: Fixed event consumer service in order to not to stop consuming the messages from Kafka in maintenance mode
*   AIOps: Fixed clearing of child alerts intermittently getting into a loop for bulk alerts clear action(via GUI)

**Known Issues/Caveats**

*   Platform: Settings on charts not supporting changing to different charts (GUI)
*   Platform: No default sorting for Tabular reports (Workaround - users can sort after opening the report)
*   Platform: rdaf infra healthcheck cmd is throwing error in nats port connection line, for non-k8s standalone setups - No impact on functionality
*   AIA: Smart sorting on interfaces, IP Addresses (no workaround)
*   AIA: Edge Collector report issue (no workaround)
*   AIA: Filter cannot be removed/hidden for POR page (no workaround)
*   AIA: SNMP ingestion values overwriting APIC data (Workaround: Ingest APIC files at the end after SNMP ingestions are completed)

RDA 3.2/AIOps 7.2 – Release Notes
---------------------------------

**__Release Date: May 15th 2023__**

**RDA/AIOps New Features**

*   Platform: Support added for two redis masters in k8s setup for HA cases
*   Platform: Replication factor in kafka config changed to 2, to support HA cases
*   Platform: In-Service Software Upgrade (ISSU)
*   Platform: New version of library (rework done) for Kafkav2/Data network
*   AIOps: Drill-down option on a policy from policies report
*   AIOps: Fixes to stream sync pipelines
*   AIOps: Removed project-id filter from alerts and alert-groups dashboards
*   AIOps: Rabbitmq support for lazy commit
*   AIOps: Ml dashboard migration

**System Level Optimization**

*   NA

**Enhancements**

*   Platform: Support added for two redis masters in k8s setup for HA cases.
*   Platform: Nats image is upgraded from 1.0.2 to 1.0.2.1
*   Platform: For AWS setups, ‘rdafk8s status’ and ‘rdafk8s log\_monitoring status’ cmds were fixed
*   Platform: Support for complete Wired and Wireless dashboards

**CFDs - Resolved**

*   NA

**Known Issues/Caveats**

*   Platform: rdafk8s platform status not showing properly
*   Platform: rdafk8s/rdaf platform reset-admin-user cmd is not working
*   Platform: rdaf infra healthcheck cmd is throwing error in nats port connection line, for non-k8s standalone setups - No impact on functionality
*   Platform: UI may throw intermittent 504 timeout errors when an infra VM is ungracefully powered off. It stabilizes after 3-4 minutes.
*   AIOps: When a worker node/VM is restarted abruptly (negative test case), service pipeline is not migrated to other working worker node
*   Compliance bot fix to get complete data using pagination support (DNAC)
*   Client counts for APs report (DNAC)
*   Sorting on Health columns (DNAC)

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!