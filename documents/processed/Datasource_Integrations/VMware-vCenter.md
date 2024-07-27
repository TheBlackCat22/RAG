 



# VMware vCenter

VMware vCenter is a management software to manage and monitor VMware vSphere virtual infrastructure environments. CloudFabrix's RDA supports integrating with VMware vCenter through it's API interface to collect the inventory on-demand or on schedule basis.

## ****1\. Prerequisites:****

*   Supported VMware vCenter versions are 5.5, 6.x and above.
    
*   User account with **read-only** access permissions for all of the Virtual Infrastructure objects (Datacenter, Cluster, ESXi Host, Virtual Machine, Datastore, Resource Pool etc)
    

## ****2\. Creating an user account with read-only permissions for API access:****

**VMware vCenter infrastructure inventory**

**Step 1**: Login to VMware vCenter web client using a supported web browser with an user account which has enough privileges to create a new account and set the read-only permissions for all Virtual Infrastructure objects.

![VMware_vCenter](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmware/vmware_vmware.png)

**Step 2**: Click on **Menu** and click on **Administration**.

![VMware_vSphere](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmware/vmware_vsphere.png)

Step 3: Click on **Users and Groups** on left menu, click on **Users**, select domain as **vsphere.local** and click on **Add User** button.

![VMware_vCenter_Administration](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmware/vmware_administration.png)

**Step 4**: Enter user account details as shown below and click on **Add** button.

![VMware_vCenter_Add_User](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmware/vmware_adduser.png)

**Step 5**: Click on **Menu** and click on **Home** button.

![VMware_vSphere_Client](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmware/vmware_vsphereclient.png)

**Step 6**: Click on **vSphere Cluster** icon and click on **vCenter** object on left and click on **Permissions** tab and click on **+** button.

![VMware_vSphere_Client](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmware/vmware_vsphereclient1.png)

![VMware_vSphere_User_Group](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmware/vmware_usergroup.png)

**Step 7**: Under **vsphere.local** domain, enter **readonly** user account which was created above and select the **Role** as **Read-only** and click on **OK**.

![VMware_vSphere_Local](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmware/vmware_vspherelocal.png)

## ****3\. Adding VMware vCenter as Datasource/Extension in RDA Studio:****

VMware vCenter or any other datasource/extension's configuration is configured in RDA's user interface. Login into RDA's user interface using a browser.

**https://\[rda-ip-address\]:9998**

Under **Notebook**, click on **CFXDX Python 3** box

![VMware_vCenter_RDA_Studio](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmware/vmware_python.png)

In the **Notebook** command box, type **botadmin()** and **alt (or option) + Enter** to open datasource administration menu.

Click on **Add** menu and under **Type** drop down, select **vmware-vcenter**

![VMware_vCenter_Datasource](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmware/vmware_botadmin.png)

*   **Type**: Datasource/Extension type. In this context, it is **vmware-vcenter-v2**
*   **name** : Datasource/Extension label which should be unique within the RDA
*   **Hostname**: VMware vCenter's IP Address or DNS name
*   **Username**: User account that was created with **read-only** permissions
*   **Password**: User account's password

Click on **Check Connectivity** to verify the network access and credentials validity. Once it is validated, click on **Add** button to add the vCenter as datasource.

## ****4\. VMware vCenter data exploration in RDA Studio:****

Once VMware vCenter integration details are configured in the RDA's as datasource, it will be ready to connect to VMware vCenter instance and explore the data for the analysis.

Run the below command to check and verify network access to VMware vCenter instance using the read-only user account's credentials entered within the RDA's datasource configuration. The **status** output should show as **OK**
```
 check vcenter

```

![VMware_vCenter_Bots](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmware/vmware_vcenter.png)
```
 > tags vcenter 
 
 or 
 
 > bots vcenter

```

\* Run the below command within the **RDA CLI** to list the available **Tags** or **Bots** for VMware vCenter extension. In this example, the VMware vCenter extension is labelled as **vcenter** which will be referenced within each applicable tag name.

Info

Each listed 'tag' starts with a special character (i.e. \* or # or @) and each hints about tag's filtering capability. For more information abut them, please refer to ["**RDA Terminology**"](https://docs.cloudfabrix.io/rda/introduction-to-rda/rda-terminology)

![VMware_vCenter_Bot_Info](https://bot-docs.cloudfabrix.io/images/rda_integrations/vmware/vmware_tagsvcenter.png)

Tags:

*   **vms**: Collects VMware virtual machine inventory
*   **hosts**: Collects VMware ESXi Hosts and Cluster inventory
*   **vswitches**: Collects VMware Standard & Distributed vSwitch inventory
*   **datastores**: Collects VMware datastore storage inventory

Run the below commands to query and collect the VMware virtual machine inventory data.
```
 > bot *vcenter:vms

```

Run the below commands to query and collect the ESXi Hosts and Cluster inventory data.
```
 > bot *vcenter:hosts

```
```
 *vcenter:hosts> data

```

Run the below commands to query and collect the ESXi datastore inventory data.
```
 bot *vcenter:datastores

```
```
 *vcenter:datastores> data

```

## ****5\. VMWare vCenter exploration in RDA Studio:****

Once VMWare vCenter integration details are configured in RDA as a datasource, it will be ready to connect to targe Nagios and explore the data for the analysis.

For the details on vCenter data collection bots, refer [CloudFabrix RDA Bot Documentation](https://bot-docs.cloudfabrix.io/Extensions/extensions_T_Z/#extension-vmware-vcenter-v2 "CloudFabrix RDA Bot Documentation")

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!