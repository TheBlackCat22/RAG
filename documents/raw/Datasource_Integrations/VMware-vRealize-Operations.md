 



VMware vRealize Operations
==========================

VMware vRealize supports alert notifications via Email, SNMP Traps, Webhook through Rest Notification plugin and others. CloudFabrix AIOPs platform uses webhook notification method from VMware vRealize Operations to receive and ingest the alerts or events. Additionally, it provides inventory and relationship data of virtual infrastructure elements along with their operations data (metrics).

****1\. Prerequisites:****
--------------------------

This section explains on how to integrate with VMware vRealize Operations monitoring tool into CloudFabrix AIOPs platform.

****2\. Configure VMware vRealize Operations for API Access:****
----------------------------------------------------------------

**Virtual Infrastructure Monitoring**

CloudFabrix supports VMware vRealize Operations API integration for fetching asset inventory, relationship data, metrics and historical alerts periodically or on demand. For API integration, it requires only read access permissions. Follow the below given steps to create service account for CloudFabrix AIOps solution with read-only permissions on VMware vRealize Operations monitoring tool.

**Step 1**: Login into VMware vRealize Operations using an user account which has privileges to create new user account and assign read-only permissions.

**Step 2**: Go to **Administration**, expand **Access** on left menu and click on **Access Control**, and under **User Accounts** tab, click on **Add** button.

![vRealize_Admin](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmwarevrealize/vmwarevrealize_administration.png)

**Step 3**: Enter the below details as shown in the below screen and click **Next**

*   User Name
*   Password
*   First Name & Last Name
*   Email Address (Optional)
*   Description (Optional)

![vRealize_Users](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmwarevrealize/vmwarevrealize_user.png)

**Step 4**: Under **Assign Groups and Permissions** Click on **Objects**, select Role as **ReadOnly**, select checkbox for **Assign this role to the user**, under Select Object Hierarchies, select checkbox for **Allow access to all objects in the system** and click on **Finish** to save the settings.

![vRealize_Objects](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmwarevrealize/vmwarevrealize_userobjects.png)

****3\. Adding VMware vRealize Operations as Datasource/Extension in RDA Studio:****
------------------------------------------------------------------------------------

VMware vRealize Operations or any other datasource/extension's configuration is configured in RDA's user interface. Login into RDA's user interface using a browser.

**https://\[rda-ip-address\]:9998**

Under **Notebook**, click on **CFXDX Python 3** box

![vRealize_RDA_Studio](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmwarevrealize/vmwarevrealize_python.png)

In the **Notebook** command box, type **botadmin()** and **alt (or option) + Enter** to open datasource administration menu.

Click on **Add** menu and under Type drop down, select **vrops**

![vRealize_Bot_Admin](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmwarevrealize/vmwarevrealize_botadmin.png)

*   **Type**: Datasource/Extension type. In this context, it is '**vrops**'
*   **name**: Datasource/Extension label which should be unique within the RDA
*   **Hostname**: VMware vCenter's IP Address or DNS name
*   **Username**: User account that was created with 'read-only' permissions
*   **Password**: User account's password

Click on **Check Connectivity** to verify the network access and credentials validity. Once it is validated, click on **Add** button to add the VMware vRealize Operations as a datasource.

****4\. MWare vRealize exploration RDA Studio:****
--------------------------------------------------

Once VMWare vRealize integration details are configured in RDA as a datasource, it will be ready to connect to targe Nagios and explore the data for the analysis.

For the details on vCenter data collection bots, refer [CloudFabrix RDA Bot Documentation](https://bot-docs.cloudfabrix.io/Extensions/extensions_T_Z/#extension-vrops "CloudFabrix RDA Bot Documentation")

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!