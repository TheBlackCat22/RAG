 



# Dell EMC Unity

Dell EMC Unity is an unified storage array model that comes in hybrid and all-flash configuration, designed for performance, efficiency and built for multi-cloud. It provides both file (NFS, CIFS) and block (FCP, iSCSI) based storage services to end hosts and applications. CloudFabrix's RDA supports integrating with Unity storage arrays through their API interface to collect inventory data on-demand or on schedule basis.

## ****1\. Prerequisites****

Follow the below steps to create a service user account with read-only permissions to integrate with EMC Unity storage arrays.

**Step-1:** Create an user-account with readonly permissions in Unisphere management UI. Login to Unisphere management UI as **admin** privileged user

![DellEMC_Unishere](https://bot-docs.cloudfabrix.io/images/rda_integrations/dellemcunity/dellemcunity_unisphere.png)

**Step-2:** Click on **Settings**.

![DellEMC_VSA](https://bot-docs.cloudfabrix.io/images/rda_integrations/dellemcunity/dellemcunity_vsaunity01.png)

**Step-3:** Under **Users and Groups** section, click on **User Management** and click on **Add**

![DellEMC_User](https://bot-docs.cloudfabrix.io/images/rda_integrations/dellemcunity/dellemcunity_usermanagement.png)

**Step-4:** Select **Local User**

**Note:** **LDAP User** is also supported.

![DellEMC_LocalUser](https://bot-docs.cloudfabrix.io/images/rda_integrations/dellemcunity/dellemcunity_localuser.png)

**Step-5:** Enter service user account name as shown below and enter the password.

![DellEMC_User_Info](https://bot-docs.cloudfabrix.io/images/rda_integrations/dellemcunity/dellemcunity_userinformation.png)

**Step-6:** Select **Operator** as a role which provides read-only access permissions.

![DellEMC_Role](https://bot-docs.cloudfabrix.io/images/rda_integrations/dellemcunity/dellemcunity_role.png)

**Step-7:** Click on **Finish** to create the service user account.

![DellEMC_Summary](https://bot-docs.cloudfabrix.io/images/rda_integrations/dellemcunity/dellemcunity_summary.png)

## ****2\. Adding Dell EMC Unity storage array as Datasource/Extension in RDA Studio:****

Dell EMC Unity storage array or any other datasource/extension's configuration is configured in RDA's user interface. Login into RDA's user interface using a browser.

https://\[rda-ip-address\]:9998

Info

Default username and password of standalone **RDA Studio** is **rdademo** and **rdademo1234**

Under **Notebook**, click on **CFXDX Python 3** box

![DellEMC_RDA_Studio](https://bot-docs.cloudfabrix.io/images/rda_integrations/dellemcunity/dellemcunity_launcher1.png)

In the **'Notebook'** command box, type **botadmin()** and **alt (or option) + Enter** to open datasource administration menu.

Click on **'Add'** menu and under **Type** drop down, select **emc-unity**

![DellEMC_Datasource](https://bot-docs.cloudfabrix.io/images/rda_integrations/dellemcunity/dellemcunity_emcunity.png)

**Enter the below details to add Dell EMC Unity storage array as a datasource:**

*   Name
    
*   Storage IP (IP Address or DNS name of Dell EMC Unity storage array)
    
*   Username and Password
    
*   Protocol (http or https)
    
*   Port (API access port, ex: 443)
    

For the details on Dell EMC Unity storage array's inventory data collection bots, refer [CloudFabrix RDA Bot Documentation](https://bot-docs.cloudfabrix.io/Extensions/extensions_D_E/#extension-emc-unity "CloudFabrix RDA Bot Documentation")

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!