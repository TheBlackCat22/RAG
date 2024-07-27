 



ManageEngine OpManager
======================

**1\. Prerequisites:**
----------------------

This section explains on how to integrate and ingest alerts from ManageEngine OpManager Monitoring tool into CloudFabrix AIOPs platform.

ManageEngine OpManager Monitoring tool supports alert notifications via Email, SMS, Running a Command, Chat, SNMP Traps, invoking a Webhook through HTTP(s) protocol and others. CloudFabrix AIOPs platform uses webhook notification method from ManageEngine OpManager Monitoring tool to receive and ingest the alerts or events.

Supported/Qualified Versions: 12.5.201 or above

Click here for [Alert Sources](https://oiadocs.cloudfabrix.io/features-guide/alert-watch/alert-sources)
 to create a Webhook URL for ManageEngine OpManager Monitoring tool's alert notifications in CloudFabrix OIA application.

**2\. Configure ManageEngine OpManager for Alert notifications over a Webhook:**
--------------------------------------------------------------------------------

**Step 1**: Login into ManageEngine OpManager UI portal with user account which has enough privileges to create and configure Alert/Alarm notifications.

![ManageEngine_OpManager_opmanager](https://bot-docs.cloudfabrix.io/images/rda_integrations/manageengineopmanager/opmanager.png)

**Step 2**: Click on Settings and click on Notifications.

![ManageEngine_OpManager_create owndashboard](https://bot-docs.cloudfabrix.io/images/rda_integrations/manageengineopmanager/create_owndashboard.png)

**Step 3**: Click on Add button to create a new notification profile.

![ManageEngine OpManager_globalprofiles](https://bot-docs.cloudfabrix.io/images/rda_integrations/manageengineopmanager/globalprofiles.png)

**Step 4**: Click on **Invoke a Webhook box.**

![ManageEngine OpManager_create notification profile](https://bot-docs.cloudfabrix.io/images/rda_integrations/manageengineopmanager/create_notification_profile.png)

**Step 5**: Under Hook URL filed, select **POST** and enter the [Webhook URL](https://oiadocs.cloudfabrix.io/features-guide/alert-watch/alert-sources#create-webhook-for-incoming-alerts-from-different-monitoring-tools)
 that was created for ManageEngine OpManager alert notifications under CloudFabrix OIA application. Select **raw** as data type and select **JSON** as payload type. For body content, enter the payload as shown in the code block next to below screen. For request headers, add the below two and set the **Time Out** as 60 seconds. Click **Next**

**Content-Type => application/json**

**Authorization** => Basic username:password in [base64](https://www.base64encode.org)
 format (Optional, this is needed only when Webhook is enabled with HTTP basic authentication)

![ManageEngine_OpManager_invoke_a_webhook](https://bot-docs.cloudfabrix.io/images/rda_integrations/manageengineopmanager/invoke_a_webhook.png)

`[](#__codelineno-0-1) { [](#__codelineno-0-2) "Alert_Id": "$alarmid", [](#__codelineno-0-3) "Alert_Severity": "$stringseverity", [](#__codelineno-0-4) "Alert_AssetName": "$displayName", [](#__codelineno-0-5) "Alert_Message": "$message", [](#__codelineno-0-6) "Alert_AssetType": "$DeviceField(type)", [](#__codelineno-0-7) "Alert_AssetIPAddress": "$DeviceField(ipAddress)", [](#__codelineno-0-8) "Alert_Category": "$category", [](#__codelineno-0-9) "Alert_Time": "$strModTime", [](#__codelineno-0-10) "Alert_Type": "$eventType", [](#__codelineno-0-11) "Alert_AssetEntity": "$entity", [](#__codelineno-0-12) "Alert_LastPolledValue": "$lastPolledValue" [](#__codelineno-0-13) }`

**Step 6**: Select the check boxes that are needed to be notified and make sure **Notify when the alarm is cleared option**. Select all of the **Severity** check boxes. Click **Next**

![ManageEngine_OpManager_choose criteria](https://bot-docs.cloudfabrix.io/images/rda_integrations/manageengineopmanager/choose_criteria.png)

**Step 7**: Under **Available Devices**, add all of the monitored assets that need to be notified whenever there is an alert/alarm is raised or cleared as shown in the below screen and click **Next**.

![ManageEngine_OpManager_associate notification profile](https://bot-docs.cloudfabrix.io/images/rda_integrations/manageengineopmanager/associate_notification_profile.png)

**Step 8**: Select **Apply this profile 24x7** and other appropriate options and click **Next**.

![ManageEngine_OpManager_time window](https://bot-docs.cloudfabrix.io/images/rda_integrations/manageengineopmanager/time_window.png)

**Step 9**: Enter a profile name under **Give profile name to add** filed and click on **Test Action** and make sure it is successful. Once successful, click on **Save** to save the Webhook notification configuration.

Warning

For a successful alert/alarm notification over a Webhook to CloudFabrix AIOps application, make sure to configured it with FQDN and CA Signed certificate. Self-signed SSL certificates will cause a failure.

![ManageEngine_OpManager_monitors](https://bot-docs.cloudfabrix.io/images/rda_integrations/manageengineopmanager/monitors.png)

Info

Additionally, make sure the created **Webhook notification profile** is associated with all of the **monitored assets** for their alerts/alarms to be notified to **CloudFabrix OIA application**. Below screen is for an example on how to associate a **monitored asset** to a **Webhook notification profile.**

![ManageEngine_OpManager_opmanager inventory](https://bot-docs.cloudfabrix.io/images/rda_integrations/manageengineopmanager/opmanager_inventory.png)

**3\. ManageEngine OpManager Alert Field Mappings:**
----------------------------------------------------

| ManageEngine OpManager Alert Field | CFX OIA Field | Mandatory |
| --- | --- | --- |
| Alert\_AssetName + Alert\_AssetEntity | Key | Yes |
| Alert\_Message | message | Yes |
| Alert\_AssetName | assetName | Yes |
| Alert\_AssetIpAddress | assetIpAddress | Yes |
| Alert\_Time | raisedAt / clearedAt | Yes |
| Alert\_AssetType | assetType | Yes |
| Alert\_Type | alertType | Yes |
| Alert\_AssetEntity | componentName | Yes |
| Alert\_Category | alertCategory | Yes |
| Alert\_LastPolledValue | lastPolledValue (Enriched) | No  |
| Alert\_Id | Alert\_Id (Enriched) | No  |
| Alert\_Severity | severity | Yes |

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!