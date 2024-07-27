 



NodePing
========

**1\. Prerequisites:**
----------------------

This section explains on how to integrate and ingest alerts from NodePing monitoring tool into CloudFabrix AIOPs platform.

NodePing supports alert notifications via email, sms, webhook, slack, pagerduty and others. CloudFabrix AIOPs platform uses webhook notification method from NodePing to receive and ingest the alerts or events.

Click here for [Alert Sources](https://oiadocs.cloudfabrix.io/features-guide/alert-watch/alert-sources)
 to create a Webhook URL for NodePing alert notifications in CloudFabrix OIA application.

**2.Configure NodePing for Alert notifications over a Webhook:**
----------------------------------------------------------------

**Step 1**: Login into your **NodePing SaaS account** which has privileges to create alert notifications

![NodePing_User_Login](https://bot-docs.cloudfabrix.io/images/rda_integrations/nodeping/userlogin.png)

**Step 2**: Under **Checks & Contacts**, click on **Contacts** and click on **Add new contact**

![NodePing_Contacts](https://bot-docs.cloudfabrix.io/images/rda_integrations/nodeping/contacts.png)

**Step 3**: Enter a name for Webhook, select HTTP method as **POST**, copy & paste the Webhook URL that was created in CloudFabrix OIA application (refer [Alert Sources](https://oiadocs.cloudfabrix.io/features-guide/alert-watch/alert-sources)
 section), select notification type as **Webhook**.

Click on **Headers** and add Key Value pair as shown in the below screen. Key name as **Content-Type** and value as **application/json**. Select **Account Access Level** as **Notifications Only**.

Click on **Body** and click on **RAW** as shown in the below screen.

![NodePing_Add_Contact](https://bot-docs.cloudfabrix.io/images/rda_integrations/nodeping/addacontact.png)

`[](#__codelineno-0-1) { [](#__codelineno-0-2)   "alert_check_id":"{_id}", [](#__codelineno-0-3)   "alert_event":"{event}", [](#__codelineno-0-4)   "alert_label":"{label}", [](#__codelineno-0-5)   "alert_message":"{m}", [](#__codelineno-0-6)   "alert_uuid":"{uuid}", [](#__codelineno-0-7)   "alert_customer_id":"{ci}", [](#__codelineno-0-8)   "alert_check_type":"{t}", [](#__codelineno-0-9)   "alert_target":"{tg}", [](#__codelineno-0-10)   "alert_interval":"{i}", [](#__codelineno-0-11)   "alert_start_time":"{s}", [](#__codelineno-0-12)   "alert_end_time":"{e}", [](#__codelineno-0-13)   "alert_runtime":"{rt}", [](#__codelineno-0-14)   "alert_resultcode":"{sc}", [](#__codelineno-0-15)   "alert_resultupadte":"{su}", [](#__codelineno-0-16)   "alert_additional_message":"{m}" [](#__codelineno-0-17) }`

**Step 4**: Under **Headers** tab, add **Authorization** header as shown in the below screen when Webhook was created in OIA Application with Username & Password. This step is not needed if **Username & Password** was not set for Webhook URL.

The **Authorization** header value should be in **Basic \[username:password encoded in base64\]** format

Ex: Webhook Username & Password is **cfxuser** & **cfxpassword**, convert it to base64 encoded value as shown below ([https://www.base64encode.org](https://www.base64encode.org/)
) cfxuser:cfxpassword => Y2Z4dXNlcjpjZnhwYXNzd29yZA==

![Node_Ping_Headers](https://bot-docs.cloudfabrix.io/images/rda_integrations/nodeping/headers.png)

**Step 5**: Under **Checks and Contacts**, click on **Checks**, edit one or more monitored objects and under **Notify** section, add the new Webhook that was created above to forward the alert notifications to CloudFabrix OIA application.

![NodePing_Check_Status](https://bot-docs.cloudfabrix.io/images/rda_integrations/nodeping/checkstatus.png)

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!