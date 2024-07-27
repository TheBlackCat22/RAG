 



Infoblox NetMRI
===============

**Network device Inventory and topology**

Infoblox NetMRI is a network management product that delivers comprehensive network change and configuration management (NCCM). NetMRI enables users to automate network change, see the impact of changes on network health, manage network configurations, and meet a variety of compliance requirements. It supports multi-vendor network infrastructure.

CloudFabrix RDA provides out of the box integration for Infoblox NetMRI through it's API interface. As part of the integration, it collects multi-vendor network device inventory, MAC & ARP tables, CDP & LLDP neighbors and the network topology information.

****1\. Configure Infoblox NetMRI for API Access:****
-----------------------------------------------------

**Step 1**: Login into **Infoblox NetMRI** using an user account which has privileges to create new user account and assign **read-only** permissions.

**Step 2**: Click on **Settings** button, click on **Users** under **User Admin** menu, and click on **Add User** button to create new user and assign **View Role** for **read-only** permissions.

![Infoblox_Settings](https://bot-docs.cloudfabrix.io/images/rda_integrations/infobloxnetmri/infobloxnetmri_infoblox1.png)

****2\. Adding Infoblox NetMRI as Datasource/Extension in RDA Studio:****
-------------------------------------------------------------------------

Infoblox NetMRI or any other datasource/extension's configuration is configured in RDA's user interface. Login into RDA's user interface using a browser.

https://\[rda-ip-address\]:9998

Info

Default username and password of standalone **RDA Studio** is **rdademo** and **rdademo1234**

Under **Notebook**, click on **CFXDX Python 3** box

![Infoblox_RDA_Studio](https://bot-docs.cloudfabrix.io/images/rda_integrations/infobloxnetmri/infobloxnetmri_launcher3.png)

In the **Notebook** command box, type **botadmin()** and **alt (or option) + Enter** to open datasource administration menu.

Click on **Add** menu and under **Type** drop down, select **infoblox-netmri**

![Infoblox_RDA_Datasource](https://bot-docs.cloudfabrix.io/images/rda_integrations/infobloxnetmri/infobloxnetmri_infobloxnetmri.png)

*   **Type**: Datasource/Extension type. In this context, it is 'infoblox-netmri'
*   **name**: Datasource/Extension label which should be unique within the RDA
*   **Hostname**: Infoblox NetMRI's IP Address or DNS name
*   **Username**: Username that was created in Infoblox NetMRI with 'read-only' permissions
*   **Password**: User account's password
*   **api\_version**: Leave default value as 'auto'
*   **Protocol**: API integration over HTTP/HTTPs protocol

Click on **Check Connectivity** to verify the network access and credentials validity. Once it is validated, click on **Add** button to add the Infoblox NetMRI as a datasource.

For the details on Infoblox NetMRI inventory data collection bots, refer [CloudFabrix RDA Bot Documentation](https://bot-docs.cloudfabrix.io/Extensions/extensions_F_K/#extension-infoblox-netmri "CloudFabrix RDA Bot Documentation")

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!