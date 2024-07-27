 



# Nagios XI

CloudFabrix supports Nagios XI API integration for fetching asset inventory (host, service data) , relationship data (host & service groups) periodically or on demand. The collected data is primarily used to get additional information for Alert enrichment, correlation to reduce the alert noise & to triage the incident faster. For API integration, it requires only read access permissions. Follow the below given steps to create service account for CloudFabrix AIOps solution with read-only permissions on Nagios XI monitoring tool.

## ****1\. Configure Nagios XI for API Access:****

**Step 1**: Login into Nagios XI monitoring tool with admin privileges.

**Step2**: Click on **Admin** --> Click on **Manage Users** and --> Click on **Add New User** to create new user account.

![Nagios_Users](https://bot-docs.cloudfabrix.io/images/rda_integrations/nagios/nagios_manageusers.png)

**Step 3**: Enter **Username, Password, Name & Email Address**.

Unselect the below items:

*   Force Password Change at Next Login:
*   Email User Account Information:
*   Create as Monitoring Contact

Select the below items:

*   Account Enabled
*   Security Settings
*   Authorization Level: User
*   Can see all hosts and services
*   Read-only access
*   API access

Click on **Add User**

![Nagios_Add_User](https://bot-docs.cloudfabrix.io/images/rda_integrations/nagios/nagios_adduser.png)

*   **Step 4**: Click on newly create user account (i.e. **cfx-readonly**) to view the account settings.

![Nagios_Added_User](https://bot-docs.cloudfabrix.io/images/rda_integrations/nagios/nagios_useradded.png)

*   **Step 5**: Copy the API Key to feed it into CloudFabrix AIOps solution. You can also generate new API key by clicking on **Generate new API key** button.

![Nagios_Edit_User](https://bot-docs.cloudfabrix.io/images/rda_integrations/nagios/nagios_edituser.png)

## ****2\. Adding Nagios XI as Datasource/Extension in RDA Studio:****

Nagios XI or any other datasource/extension's configuration is configured in RDA's user interface. Login into RDA's user interface using a browser.

**https://\[rda-ip-address\]:9998**

Under **Notebook**, click on **CFXDX Python 3** box

![Nagios_RDA_Studio](https://bot-docs.cloudfabrix.io/images/rda_integrations/nagios/nagios_python.png)

In the **Notebook** command box, type botadmin() and **alt (or option) + Enter** to open datasource administration menu.

Click on **Add** menu and under **Type** drop down, select **nagios**

![Nagios_Bot_Admin](https://bot-docs.cloudfabrix.io/images/rda_integrations/nagios/nagios_botadmin.png)

*   **type**: Datasource/Extension type. In this context, it is **nagios**
*   **name**: Datasource/Extension label which should be unique within the RDA
*   **Hostname**: VMware vCenter's IP Address or DNS name
*   **API Key**: API key in Nagios UI that was created with **read-only** permissions

Click on **Check Connectivity** to verify the network access and credentials validity. Once it is validated, click on **Add** button to add the Nagios XI as a datasource.

Below are available data bots for Nagios XI datasource.

![Nagios_Tags](https://bot-docs.cloudfabrix.io/images/rda_integrations/nagios/nagios_tags.png)

## ****3\. Nagios exploration in RDA Studio:****

Once Nagios integration details are configured in RDA as a datasource, it will be ready to connect to targe Nagios and explore the data for the analysis.

For the details on Nagios inventory data collection bots, refer [CloudFabrix RDA Bot Documentation](https://bot-docs.cloudfabrix.io/Extensions/extensions_L_N/#extension-nagios "CloudFabrix RDA Bot Documentation")

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!