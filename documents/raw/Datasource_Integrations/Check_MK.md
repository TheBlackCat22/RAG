 



Check MK
========

**1\. Prerequisites:**
----------------------

This section explains on how to integrate and ingest alerts from Check MK monitoring tool into CloudFabrix AIOPs platform.

Check MK (derived from Nagios Core) is a monitoring tool which supports alert notifications via email, slack, pagerduty, victorops or a script executing a command. CloudFabrix AIOPs platform uses webhook notification method using a script from Check MK monitoring tool to receive and ingest the alerts or events.

Click here for [Alert Sources](https://oiadocs.cloudfabrix.io/features-guide/alert-watch/alert-sources)
 to create a Webhook URL for Check MK alert notifications in CloudFabrix OIA application.

Note: Under Alert Mapping section, use Nagios alert mapping configuration for Check MK alerts.

**2.Configure Check MK for Alert notifications over a Webhook:**
----------------------------------------------------------------

**Step 1**: Download the below scripts for both **Host** and **Service** type of alerts

For **Host** type alerts:

[https://macaw-amer.s3.amazonaws.com/releases/OIA/scripts/webhook/cfx-host-webhook-notification.sh](https://macaw-amer.s3.amazonaws.com/releases/OIA/scripts/webhook/cfx-host-webhook-notification.sh)

For **Service** type alerts:

[https://macaw-amer.s3.amazonaws.com/releases/OIA/scripts/webhook/cfx-service-webhook-notification.sh](https://macaw-amer.s3.amazonaws.com/releases/OIA/scripts/webhook/cfx-service-webhook-notification.sh)

**Step 2**: Copy the **cfx-host-webhook-notification.sh** and **cfx-service-webhook-notification.sh** script to Check MK system into the folder **/omd/sites//local/share/check\_mk/notifications**

**Step 3**: Login into Check MK monitoring tool's machine using SSH CLI as **root** user and execute the below commands.

`[](#__codelineno-0-1) ssh root@<checkmk-ip-address>`

`[](#__codelineno-1-1) cd /omd/sites/<Site_Name>/local/share/check_mk/notifications`

`[](#__codelineno-2-1) chmod 755 cfx-host-webhook-notification.sh [](#__codelineno-2-2) chmod 755 cfx-service-webhook-notification.sh`

**Step 4**: Edit the scripts **cfx-host-webhook-notification.sh** & **cfx-service-webhook-notification.sh** and configure the below variables. Configure the **CFX\_WEBHOOK\_URL** variable with **Webhook URL** that was created under [Alert Sources](https://oiadocs.cloudfabrix.io/features-guide/alert-watch/alert-sources)
 section in CloudFabrix OIA application.

Configure **CFX\_WEBHOOK\_USERNAME** and **CFX\_WEBHOOK\_PASSWORD** variables if the Webhook is configured with HTTP authentication, otherwise, leave them empty.

`[](#__codelineno-3-1) CFX_WEBHOOK_URL="<cfx-webhook-url>" [](#__codelineno-3-2) CFX_WEBHOOK_USERNAME="<cfx-webhook-username-Optional>" [](#__codelineno-3-3) CFX_WEBHOOK_PASSWORD="<cfx-webhook-username-Optional>"`

**Step 5**: Login into Check MK monitoring tool UI as a user which has admin privileges to configure the alert notifications.

![Check_MK_login](https://bot-docs.cloudfabrix.io/images/rda_integrations/checkmk/checkmk_login.png)

**Step 6**: Under **Setup** menu, click on **Users** menu to create a new user for Check MK alert notifications.

![Check_MK_maindashboard](https://bot-docs.cloudfabrix.io/images/rda_integrations/checkmk/maindashboard.png)

**Step 7**: Click on **Add** button

![Check_MK_users](https://bot-docs.cloudfabrix.io/images/rda_integrations/checkmk/checkmk_users.png)

**Step 8**: Enter username as **cfx\_notifications**. Select appropriate sites under **Authorized sites**. Under **Security** section, select **Automatic secret for machine accounts** and generate a secret.

Select **Disable password** option to disable the login to this account. Select the roles as **Normal monitoring user**

![Check_MK_adduser](https://bot-docs.cloudfabrix.io/images/rda_integrations/checkmk/checkmk_adduser.png)

**Step 9**: Commit the changes.

**Step 10**: Under **Setup** menu, click on **Notifications** menu to create configure alert notifications for both Host and Service type problems.

![Check_MK_activate pending changes](https://bot-docs.cloudfabrix.io/images/rda_integrations/checkmk/activate_pending_changes.png)

**Step 11**: Configure alert notifications for **Host** type problems.

Click on **Add rule** button.

![Check_MK_notification configuration](https://bot-docs.cloudfabrix.io/images/rda_integrations/checkmk/notification_configuration.png)

**Step 12**: Enter the **Description** as **cfx\_host\_notification**.

Select **Notification Method** as **cfx-host-webhook-notification.sh** from the drop down menu.

Under Contact selection section, select cfx\_notifications user that was created to enable the alert notification.

Select appropriate **Sites** to enable the alert notification.

![Check MK_add notification rule](https://bot-docs.cloudfabrix.io/images/rda_integrations/checkmk/add_notification_rule.png)

**Step 13**: For **Match host event type** option, select appropriate options as shown below. Click on Save button to save the alert notification rule.

![Check MK_match host](https://bot-docs.cloudfabrix.io/images/rda_integrations/checkmk/match_host.png)

**Step 14**: Configure alert notifications for **Service** type problems.

Click on **Add rule** button.

Enter the **Description** as **cfx\_service\_notification**.

Select **Notification Method** as **cfx-service-webhook-notification.sh** from the drop down menu.

Under Contact selection section, select cfx\_notifications user that was created to enable the alert notification.

Select appropriate **Sites** to enable the alert notification.

![Check_MK_add notification](https://bot-docs.cloudfabrix.io/images/rda_integrations/checkmk/add_notification.png)

**Step 15**: For **Match service event type** option, select appropriate options as shown below. Click on Save button to save the alert notification rule.

![Check_MK_match service event](https://bot-docs.cloudfabrix.io/images/rda_integrations/checkmk/match_service_event.png)

Below is the Alert Filed mapping table (for information only) between Check MK alert notification fields and CloudFabrix OIA's common data model fields for Alerts.

| Check MK Alert Field | CloudFabrix OIA Alert Field |
| --- | --- |
| Alert\_NotificationType | alertType |
| Alert\_Nagios\_SourceType | Determines whether source alert is from Host or Service type |
| Alert\_ServiceNotificationId / Alert\_HostNotificationId | key (Service/Host) |
| Alert\_ServiceDescription /Alert\_ServiceOutput | message (Service) |
| Alert\_HostName | assetName |
| Alert\_HostAddress | assetIpAddress |
| Alert\_Nagios\_SourceType | assetType |
| Alert\_HostState /Alert\_HostAddress (or) Alert\_HostOutput | message (Host) |
| Alert\_DateTime | raisedAt / clearedAt |
| Alert\_ServiceState/Alert\_HostState | severity (Service/Host) |

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!