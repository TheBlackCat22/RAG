 



# Zabbix

## **1.Prerequisites:**

This section explains on how to integrate and ingest alerts from Zabbix monitoring tool into CloudFabrix AIOPs platform.

Zabbix supports alert notifications via email, sms, script or webhook. CloudFabrix AIOPs platform uses webhook notification method from Zabbix to receive and ingest the alerts or events.

Click here for [Alert Sources](https://oiadocs.cloudfabrix.io/features-guide/alert-watch/alert-sources)
 to create a Webhook URL for Zabbix alert notifications in CloudFabrix OIA application.

## **2.Configure Zabbix for Alert notifications over a Webhook:**

**Step 1**: Login to Zabbix monitoring tool through web-browser UI

![Zabbix_userlogin](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/userlogin.png)

**Step 2**: On left menu, expand **Administration** and click on **Media types**

![Zabbix_administration](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/administration.png)

**Step 3**: Click on **Create media type**

![Zabbix_createmedia](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/createmedia.png)

**Step 4**: Click on **Media type**, Enter name for the Webhook and select **Type** as **Webhook** from the drop down.

![Zabbix_webhook](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/webhook.png)

**Step 5**: As highlighted in the above screen, add the below parameters.

`Alert_Date => {EVENT.DATE}`

`Alert_HostAddress => {HOST.IP}`

`Alert_Hostname => {HOST.NAME}`

`Alert_RecoveryDate => {EVENT.RECOVERY.DATE}`

`Alert_RecoveryTime => {EVENT.RECOVERY.TIME}`

`Alert_RecoveryName => {EVENT.RECOVERY.NAME}`

`Alert_RecoveryTags => {EVENT.RECOVERY.TAGSJSON}`

`Alert_ServiceDescription => {EVENT.NAME}`

`Alert_ServiceEventId => {EVENT.ID}`

`Alert_ServiceOutput => {EVENT.OPDATA}`

`Alert_ServiceSeverity => {EVENT.SEVERITY}`

`Alert_Time => {EVENT.TIME}`

`Alert_Status => {EVENT.STATUS}`

`Alert_Message => {ALERT.MESSAGE}`

`Alert_HostGroup => {TRIGGER.HOSTGROUP.NAME}`

`Alert_Tags => {EVENT.TAGSJSON}`

`Alert_Template => {TRIGGER.TEMPLATE.NAME}`

`Alert_WebHookURL => {ALERT.SENDTO}`

**Step 6**: Edit the **Script** field and add the below **Java script**
```
 var params = JSON.parse(value), 
 req = new CurlHttpRequest(), 
 resp; 
 req.AddHeader('Content-Type: application/json'); 
 //req.AddHeader('Authorization: Basic <base64encoded - username:password>'); 
 //Below example when HTTP Basic authentication is used for Webhook,  
 //Username: cfxuser, Password: cfxuser 
 //req.AddHeader('Authorization: Basic Y2Z4dXNlcjpjZnh1c2Vy'); 
 
 var params = JSON.parse(value); 
 payload = {}; 
 payload.Alert_ServiceEventId = params.Alert_ServiceEventId; 
 payload.Alert_HostName = params.Alert_HostName; 
 payload.Alert_HostAddress = params.Alert_HostAddress; 
 payload.Alert_Date = params.Alert_Date; 
 payload.Alert_Time = params.Alert_Time; 
 payload.Alert_ServiceSeverity = params.Alert_ServiceSeverity; 
 payload.Alert_ServiceDescription = params.Alert_ServiceDescription; 
 payload.Alert_ServiceOutput = params.Alert_ServiceOutput; 
 payload.Alert_Message = params.Alert_Message; 
 payload.Alert_RecoveryDate = params.Alert_RecoveryDate; 
 payload.Alert_RecoveryTime = params.Alert_RecoveryTime; 
 payload.Alert_RecoveryName = params.Alert_RecoveryName; 
 payload.Alert_RecoveryTags = params.Alert_RecoveryTags; 
 payload.Alert_Status = params.Alert_Status; 
 payload.Alert_HostGroup = params.Alert_HostGroup; 
 payload.Alert_Tags = params.Alert_Tags; 
 payload.Alert_Template = params.Alert_Template; 
 resp = req.Post(params.Alert_WebHookURL, 
 JSON.stringify(payload) 
     ); 
 return resp;

```

**Step 7**: Click on **Apply** to save the Script

**Step 8**: Make sure **Enabled** is check-box is checked.

**Step 9**: Click on **Message Templates** tab and click on **Add** as show in the below screen

![Zabbix_mediatypes](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/mediatypes.png)

**Step 10**: From **Message Type** drop down menu, select **Problem**, Enter Subject as **Problem: {EVENT.NAME}**, leave **Message** as blank and click on **Add**

![Zabbix_messagetemplateproblem](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/messagetemplateproblem.png)

**Step 11**: Click on **Add** to add another Message Template. From **Message Type** drop down menu, select **Problem recovery**, Enter Subject as Resolved in {EVENT.DURATION}: {EVENT.NAME}, leave **Message** as blank and click on **Add**

**Step 12**: Click on **Add** to save the Webhook Media Type.

![Zabbix_problemrecovery](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/problemrecovery.png)

**Step 12**: Click on **Add** to save the Webhook Media Type.

![Zabbix_messagetemplate](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/messagetemplate.png)

**Step 13**: On left menu, expand **Administration** and click on **User groups** to add a new user group with read-only permissions.

![Zabbix_usergroups](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/usergroups.png)

**Step 14**: Click on **Create user group**

![Zabbix_createusergroup](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/createusergroup.png)

**Step 15**: Click on **User group** tab, enter **Group name** as **cfx\_notifications\_group**

![Zabbix_cfxnotificationgroup](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/cfxnotificationgroup.png)

**Step 16**: Click on **Permissions** tab, and click on **Select** to select all groups

![Zabbix_permissions](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/permissions.png)

**Step 17**: Select all **Host Groups** as shown below and click **Select**.

![Zabbix_hostgroups](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/hostgroups.png)

**Step 18**: Select **Read** permission, select **Include subgroups** check-box and click on **Add** button

![Zabbix_permissions hostgroup](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/permissions_hostgroup.png)

**Step 19**: On left menu, expand **Administration** and click on **Users** to add a new user with Read-only permissions.

![Zabbix_administration users](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/administration_users.png)

**Step 20**: Click on **Create user**.

![Zabbix_usergroup createuser](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/usergroup_createuser.png)

**Step 21**: Click on **User** tab, enter Alias as **cfx\_notification\_user**. Click on **Select** to select the **cfx\_notifications\_group** that was create above (Step 15). Enter user password.

![Zabbix_cfx notifications user](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/cfx_notifications_user.png)

**Step 22**: Click on **Media** tab and click on **Add** button as show in the below screen to add Webhook details.

![Zabbix_media type add](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/media_type_add.png)

**Step 23**: Select **CloudFabrix-Webhook** that was created in one of the step above (Step 4), and for **Send to** field add the Webhook URL (created under [Alert Sources](https://oiadocs.cloudfabrix.io/features-guide/alert-watch/alert-sources)
 section), leave the rest of fields as shown in below screen and Click **Add**

![Zabbix_cloudfabrix webhook](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/cloudfabrix_webhook.png)

**Step 24**: Click **Add** button to complete in adding the Webhook notification in Zabbix.

![Zabbix_cloudfabrix webhook media](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/cloudfabrix_webhook_media.png)

Info

**Testing the Webhook notification**: Under **Media Type** section of the menu, select the **Webhook** that was created above and click on **Test**

Tip

If there is a test failure with error message cannot get URL: Couln't resolve hostname, httprequest.c.323 internal ,edit the **Webhook media type** and enter the Webhook URL as a value for **Alert\_WebHookURL** attribute, save it and try the **Test** connection again.

Warning

Zabbix Triggers Please make sure to select **PROBLEM event generation mode** as **single** for sending Alert notifications to CloudFabrix AIOPs system. When **multiple** option is selected, Zabbix generates a new event ID everytime it evaluates the condition of the trigger. CloudFabrix AIOps system uses the event ID to track the lifecycle of an event from open to closure. Below is the same screen for a reference.

![Zabbix_triggers](https://bot-docs.cloudfabrix.io/images/rda_integrations/zabbix/triggers.png)

## **3\. Zabbix Alert Field Mappings**:

| Zabbix Field | CFX OIA Field | Mandatory |
| --- | --- | --- |
| Alert\_ServiceEventId | key | Yes |
| Alert\_ServiceDescription/ Alert\_ServiceOutput | message | Yes |
| Alert\_HostName | assetName | Yes |
| Alert\_HostAddress | assetIpAddress | Yes |
| Alert\_Status | status (=OPEN if PROBLEM else CLEARED) | Yes |
| Alert\_Date / Alert\_Time | raisedAt | Yes |
| Alert\_RecoveryDate / Alert\_RecoveryTime | clearedAt | Yes |
| Alert\_Tags / Alert\_RecoveryTags | Tags (additional attributes) | No  |
| Alert\_Template | alertType | Yes |
| Alert\_HostGroup | Customer\_name (for enrichment) | No  |
| Alert\_ServiceState | severity | Yes |

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!