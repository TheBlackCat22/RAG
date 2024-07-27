 



Guide to navigate administrative operations in RDA Fabric platform's UI Portal
==============================================================================

**1\. RDA Fabric Platform's UI Portal Introduction**
----------------------------------------------------

The RDAF platform's UI portal is the primary interface for performing various administration operations, including but not limited to.

*   **RDA Fabric Artifact Configuration & Management**
    *   Pipelines
    *   Credentials
    *   Service Blueprints
    *   Formatting Templates
    *   Synthetics
    *   Bundles
*   **RDA Fabric Data Management**
    *   Persistent Streams
    *   Datasets
    *   Log Archives
    *   Dependency Mappings
    *   Data Staging Area
*   **RDA Fabric Applications (OIA/AIA) on-boarding**
*   **RDA Fabric Operational Dashboard**
*   **RDA Fabric User Administration (RBAC)**
*   **RDA Fabric User Dashboard Configuration & Management**

**2\. RDA Fabric User Administration (RBAC)**
---------------------------------------------

As part of the installation of RDAF core platform services, it creates a default tenant admin user called `admin@cfx.com`

In order to access RDAF UI portal, open a web browser and type the RDAF HAProxy server's **IP address or DNS Name** if it is a non-HA deployment or RDAF HAProxy server's **virtual IP address or DNS Name** if it is an HA deployment as shown below.

`[](#__codelineno-0-1) https://<rdaf-haproxy-ip-address>`

The default password for `admin@cfx.com` is **admin1234**

Note

`admin@cfx.com` user is the super admin user for RDA Fabric platform. For production deployment, please make sure to provide strong password and limit the access only to designated administrative users.

On first login onto RDAF UI portal, it prompts for resetting the above default password to user's choice.

![RDAF_Portal_Login_Password](https://bot-docs.cloudfabrix.io/images/rdaf_portal/rdaf_portal_login_password.png)

### **2.1 Local Users**

RDA Fabric platform support local users and remote users integrating with external identity and access management (IAM) tools. Below are supported for user access management.

*   **Local Users**
*   **Active Directory Users**
*   **SSO Users**

**Local Users** are created and managed within the RDAF platform.

Note

Local Users should be used only for POC or Demo or Development environments. For Production deployments, it is recommended to integrate with external identity and access management tools such as Active Directory / LDAP or SSO

The below picture illustrates how the RDAF platform users (local/ or remote) are mapped and roles / permissions are assigned.

![RDAF_Portal_User_Role_Mapping](https://bot-docs.cloudfabrix.io/images/rdaf_portal/rdaf_portal_user_role_mappings.png)

**Adding MSP User Group:**

After login into RDAF platform using **admin@cfx.com** user, go to **Main Menu** --> **Administration** --> **Users**

Under **User Groups** section, click on **Add Group** action button to create a new user group for **MSP Administration**

*   Enter Group Name as **MSP Administrators**
*   Enter Description as **MSP Administration Group**
*   Select Role as **MSP Administrator** ![RDAF_Portal_Tenant_Admin_Group_Add](https://bot-docs.cloudfabrix.io/images/rdaf_portal/rdaf_portal_tenant_admin_group_add.png)

**Adding MSP User:**

Under **Users** section, click on **Add User** action button to create a new MSP user.

*   Enter User First and Last Name
*   Enter User's email address (it is used as login if for the user)
*   Select User Group as **MSP Administrators** (as created above)

![RDAF_Portal_MSP_Admin_User_Add](https://bot-docs.cloudfabrix.io/images/rdaf_portal/rdaf_portal_tenant_admin_user_add.png)

RDAF platform by default comes with the below **User Profiles / Roles** which can be associated to an appropriate user groups as per the requirement.

*   **MSP Administrator:** When MSP Administrator role is associated to an User Group, all the associated users to it will have full MSP Administration privileges and will have access to all of the RDAF platform's Menu items.
*   **MSP User:** When MSP User role is associated to an User Group, all the associated users to it will have limited MSP privileges and will have access to all of the RDAF platform's Menu items.
*   **MSP Read Only User:** When MSP Read Only User role is associated to an User Group, all the associated users to it will have **read-only** MSP privileges and will have access to all of the RDAF platform's Menu items.
*   **Organization Administrator:** When Organization Administrator role is associated to an User Group, all the associated users to it will have Administrative privileges to the resources within the selected Organization.
*   **Organization User:** When Organization User role is associated to an User Group, all the associated users to it will have limited privileges to the resources within the selected Organization.
*   **Organization Read Only User:** When Organization Read Only User role is associated to an User Group, all the associated users to it will have **read-only** privileges to the resources within the selected Organization.
*   **L1 User:** When L1 User role is associated to an User Group, all the associated users to it will have limited privileges and will have ONLY access to RDAF platform's Dashboards Menu.
*   **L3 User:** When L3 User role is associated to an User Group, all the associated users to it will have limited privileges and will have ONLY access to RDAF platform's Dashboards Menu.

### **2.2 Active Directory Users**

RDA Fabric platform supports integrating with Windows Active Directory IAM (Identity and Access Management) system.

For integrating with Windows Active Directory, go to **Main Menu** --> **Administration** --> **Authentication Servers**

Under **Authentication Servers** section, click on **Add** button to add Windows Active Directory server details.

Click on **Test Connectivity** button to validate the Active Directory integration before clicking on **Add** button to save the configuration.

![RDAF_Portal_Windows_AD_Server_Add](https://bot-docs.cloudfabrix.io/images/rdaf_portal/rdaf_add_windows_ad_server.png)

| Parameter Name | Description |
| --- | --- |
| Name | Specify a name or label for Windows Active Directory integration |
| Server IP or Host Name | Enter Active Directory server's IP Address or DNS Name |
| use SSL | Select this check box to use SSL protocol |
| Protocol | Select Active Directory |
| Port | Enter **port 389** for non-SSL or **port 636** for SSL protocol |
| Principal DN Format | Enter domain name in **Distinguished Name (DN) format**. For an example, if domain name is `acme.com`, DN format is `DC=acme,DC=com`. If domain name is `dev.acme.com`, DN format is `DC=dev,DC=acme,DC=com` |
| User Search Filter Format | Enter the value as `(&(objectClass=*))`. This filter is to include all Active Directory objects for searching the **Users & Groups** while importing them into RDA Fabric platform. |
| Username (fully distinguished name) | Enter a valid Active Directory domain user name in **Distinguished Name (DN) format** or in **User Principal format (UPN)**. For an example, `readonlyuser@acme.com` is in **UPN** format which is acceptable. **DN format** for the same user is `CN=readonlyuser,CN=Users,DC=acme,DC=com` |
| Password | Enter User's password for the above specified domain user. |

Tip

Please note that only **one** Active Directory server integration can be added. After adding it successfully, the **Add** button will not appear in the UI. If a new Active Directory server needs to be added, either update the existing configuration or delete the current configuration and add a new one.

#### **2.2.1 Import Active Directory Users**

Tip

Before importing Active Directory users, it is a pre-requisite to create one or more **Local User Groups** and associate them to one of the available **User Role.**

Go to **Main Menu** --> **Administration** --> **Users**. Under **User Groups** section, click on **Add Group** action button to create a new user group.

Before importing Active Directory users, ensure that **Active Directory user groups**, to which the users belong, have been added.

Go to **Main Menu** --> **Administration** --> **Authentication Servers** --> **User Groups**

Click on **Add Group** button to search and import the Active Directory user groups.

In the pop-up window, under **Filter Groups**, enter `*Domain*` (as an example) and click on **Get AD Groups**

Select one or more **User Groups** from the list and click on **Add** button.

Tip

Searching for user groups in Active Directory supports the use of wildcards, such as **'\*'** before and after a user group name. User group filter with a wildcard in the below screenshot is for a reference only.

![RDAF_Portal_Windows_AD_UserGroup_Import](https://bot-docs.cloudfabrix.io/images/rdaf_portal/rdaf_ad_user_group_import.png)

To add the Active Directory users, click on **Users** section.

Click on **Import Users** button to add one or more Active Directory users.

In the pop-up window, below options are available.

*   **From AD Groups:** Select this option to list all of the imported Active Directory user groups in the above step. It allows to select one of the user group from which Active Directory Users can be imported. (**Note:** If the Users are part of **Domain Users** group, please select the below option instead.)
    
*   **From AD Default Group:** Select this option to import the users from default Active Directory group i.e. **Domain Users**
    
*   **AD Group:** Select one of the Active Directory group from the list. (**Note:** This option only available when **From AD Groups** option is selected above.)
    
*   **Filter Group Members:** Enter username string with a wildcard, such as `*acme*` (as an example), and click on **Get AD Users** to retrieve a list of users that match the wildcard filter.
    
*   **User Count:** The default value is 100, and the maximum supported value is 250. This value is set to limit the number of users to be imported from Active Directory.
    
*   **User Group:** Select **Local User Group** that was created with a **User Role** to associate one or more Active Directory users.
    
*   **AD Users:** Select one or more Active Directory users to be imported.
    

Click on **Import** button to import the Active Directory users.

![RDAF_Portal_Windows_AD_Users_Import](https://bot-docs.cloudfabrix.io/images/rdaf_portal/rdaf_ad_users_import.png)

**Delete Imported Active Directory Users & User Groups:**

Go to **Main Menu** --> **Administration** --> **Authentication Servers** --> **User Groups** or **Users**

Select **User Group** and from the action menu, click on **Delete**

Select **User** and from the action menu, click on **Delete**

#### **2.2.2 Add Active Directory Users**

Go to **Main Menu** --> **Administration** --> **Users**

Click on **Add User** action button to add one or more Active Directory users.

Click on **Remote User** check box, under **AD Users** table, select one or more Active Directory users and click on **Submit** button.

![RDAF_Portal_Windows_AD_Add_Users](https://bot-docs.cloudfabrix.io/images/rdaf_portal/rdaf_ad_add_user.png)

**3\. UI Management**
---------------------

### **3.1 Favorites**

RDA Fabric platform allows users to set any user dashboards or administrative / configuration pages as **Favorites**

Select the desired tab which needs to be marked as **Favorite**

Click on the 3 Dot Menu select **Add to Favorites**

![Add_to_Favorites](https://bot-docs.cloudfabrix.io/images/ui_favorites/add_to_favorites.png)

Then a Pop-up appears then we can change the label to the User Defined Label

![Popup](https://bot-docs.cloudfabrix.io/images/ui_favorites/popup.png)

select the Tab that needs to be marked as favorite

![Tab_Selection](https://bot-docs.cloudfabrix.io/images/ui_favorites/tab_selection.png)

Click on the **UI Menu** and select **Favorite Icon** as shown below in the screenshot

Tip

Please click on the pictures below to enlarge and to go back to the page please click on the back arrow button on the top.

User needs to click on the icon as shown in the below screenshot

[![Favorite_icon](https://bot-docs.cloudfabrix.io/images/ui_favorites/favorite_icon.png)](/images/ui_favorites/favorite_icon.png)

Now the user can see the Tabs which they have marked as Favorite, when the user clicks on it, user will get navigated to the respective dashboard

[![NYPD](https://bot-docs.cloudfabrix.io/images/ui_favorites/nypd.png)](/images/ui_favorites/nypd.png)

**4\. Object Store**
--------------------

RDA Fabric platform supports raw files to be added to object store by uploading from the CFX portal UI.

**Object Store** configuration is located at **Menu** → **Configuration** → **RDA Administration** → **Object Store**

### **4.1 Add Objects**

Users can add **Templates/Files**. To add a new file to **Object Store**, click on **Upload** action

![Object Store](https://bot-docs.cloudfabrix.io/images/adding_objects/object_store.png)

![Upload File](https://bot-docs.cloudfabrix.io/images/adding_objects/upload_file.png)

Provide a **Name** for the file and a **Folder Name** to upload the file, then click on the **Add** button to upload the file.

**Supported File Types**

| File Types |     |
| --- | --- |
| **csv** | **html** |
| **pqt** | **txt** |
| **parquet** | **zip** |
| **pa** | **gz** |
| **orc** | **tar** |
| **json** | **yml** |
| **xlsx** |     |

Note

If you need to reupload any template that was already added or stored, click on **Upload** and provide the same inputs for **Name**, **Folder Name**, and upload the new file along with the selection of the checkbox **Enable Overwrite**. Then click on **Save**.

### **4.2 Object Management**

#### **4.2.1 Download**

*   Allows to download the file that was uploaded earlier, The below Screenshots show how thats going to look like

Tip

Please click on the pictures below to enlarge and to go back to the page please click on the back arrow button on the top.

[![Download File](https://bot-docs.cloudfabrix.io/images/adding_objects/download_file.png)](/images/adding_objects/download_file.png)

When the user clicks on to **Download** this is how its going to look like in the below screenshot.

[![Download1](https://bot-docs.cloudfabrix.io/images/adding_objects/download1.png)](/images/adding_objects/download1.png)

#### **4.2.2 Delete**

*   This option allows the user to delete the files that were added earlier as shown in the below screenshot.

[![Delete](https://bot-docs.cloudfabrix.io/images/adding_objects/delete.png)](/images/adding_objects/delete.png)

When the user clicks on to **Delete** this is how its going to look like in the below screenshot.

[![Delete1](https://bot-docs.cloudfabrix.io/images/adding_objects/delete1.png)](/images/adding_objects/delete1.png)

**5\. Pstream Data Archival**
-----------------------------

Data retention supports the ability to backup the data and store it in storage object. It is supported to take backup automatically on a daily basis if archival is enabled on the data.

### **5.1 Enabling Data Archival**

After login into CFX Portal UI go to **Menu** → **Configuration** → **RDA Administration** → **Persistent Streams** → Click **Persistent Streams**

![Pstreams](https://bot-docs.cloudfabrix.io/images/data_retention/pstreams.png)

Feature can also be enabled by passing a flag to a pstream while **adding/editing** the pstream.

![Edit Pstream](https://bot-docs.cloudfabrix.io/images/data_retention/edit_pstream.png)

Adding/Editing the required pstream

![Add Pstream](https://bot-docs.cloudfabrix.io/images/data_retention/add_pstream.png)

Note

As of 3.3 release, the below functionality is not implemented now and is targeted for 3.4

| Parameter Name | Mandatory | Description |
| --- | --- | --- |
| `max_age_in_days` | no  | It expects the input to be in number (days) and it will delete the backed up data from object storage once no of days are passed. |
| `frequency` | yes | Based on the specified interval, data is backed up. |

Note

When data collection happens for the first time it takes backup for the last 7 days.

### **5.2 Backup Collection**

Daily Backup is configured to collect at **12AM UTC Time**.

### **5.3 Backup Status**

Once we have archival enabled for a pstream as it takes a backup, check if the backup is successful and once backup is successful users can see all the backups in CFX UI in the Archives page

Once we have archival enabled for a pstream as it takes a backup and once backup is successful users can see all the backups in CFX UI in the Archives page.

![Archieves](https://bot-docs.cloudfabrix.io/images/data_retention/archieves.png)

### **5.4 Download Archived Backups**

All the successful backups collected/stored will be shown in the Archives page with the name of pstream(s). Click on the action of “View Archives” for a specific pstream user need to download the backup data.

![View Archieves](https://bot-docs.cloudfabrix.io/images/data_retention/view_archives.png)

![Download](https://bot-docs.cloudfabrix.io/images/data_retention/download.png)

Note

Download action gets enabled only when backup data has any update in the last 24 hours (daily schedule). If there is no update in data in the last 24 hours the action will not get enabled

### **5.5 Backup Data Transfer**

Can a user transfer the downloaded, backed up data to a different setup? **Yes**, Once the file is downloaded, user will see a file named

`pstreamName_dateofbackup_time tar.gz downloaded`

`n1_dashboards_data/2023/11/21/all_data_4b4ebde1.tar.gz`

**CFX** supports multiple ways to **Dump/Transfer** backed up data to different setup

### **5.6 Ingest the Backup data to Pstream**

*   As the file is downloaded on your computer you need to extract the `<backupfile>.tar.gz` using standard ‘gunzip’ or other utility. Once the file is extracted, user will see tmp folder in the same location.
    
*   In tmp folder, user will see a file name `<tmp***>.gz`, user is expected to to extract the gz file as well using gunzip or standard utility, Once extracted, user will see `<tmp***>` file
    
*   As the extracted file will not have proper file extension, it will be saved as a document. Users can rename the file with extension as .csv. Ex: `<tmp***>.csv`
    
*   Login to CFX UI go to **Menu** → **Configuration** → **RDA Administration** → **Persistent Streams** → Click **Persistent Streams** and add the dataset using csv file. Click on **Persistent Streams** (below datasets) and make sure the new stream is present where the data needs to be copied or imported. If a stream is not present, create a new stream.
    
*   Click on **Datasets** (Page above to persistent streams) → Click **Datasets** and add the dataset using the csv file extracted in the earlier step.
    
*   On the new dataset that is created click on the action menu and select **Ingest to Stream** and select the stream name in the pop-up and click on **Ingest**. Users can check the status of data ingestion in **rda\_system\_collector\_ingestion\_job\_status** in persistent streams report.
    
*   Data will be shown in the stream once data is ingested successfully to pstream.
    

Note

Timestamp date in pstream will be shown with the date that the backup has taken and with default time filter of Last 24 Hours data will not be shown in the pstream.

### **5.7 Using RDAC Commands**

*   Copy the downloaded file to one of the VM where rdac is running.
    
*   Extract the file using below commands.
    

`[](#__codelineno-1-1) #tar -xvf <pstreamName_dateofbackup_time>tar.gz [](#__codelineno-1-2) #cd tmp/ [](#__codelineno-1-3) #gunzip <tmp***>.gz [](#__codelineno-1-4) #mv <tmp***> <tmp***>.csv`

*   Login to CFX UI go to Menu → Configuration → RDA Administration → Persistent Streams → Click “Persistent Streams” and add the dataset using csv file. Click on the Persistent Streams (below datasets) and make sure the new stream is present where the data needs to be copied. If a stream is not present, create a new stream.
    
*   Using rdac we can copy the data to pstream using the below command.
    

`[](#__codelineno-2-1) #rdac pstream load --name <pstreamName> --data <tmp***>.csv`

Below is the terminal output if data gets copied to stream.

`[](#__codelineno-3-1) Reading input data file... [](#__codelineno-3-2) Input data file has 1714 Rows and 62 Columns [](#__codelineno-3-3) Publishing 1000 rows.. [](#__codelineno-3-4) Publishing 714 rows.. [](#__codelineno-3-5) Completed loading of 1714 rows into stream demo_data in 1.3 seconds`

****6\. Tag Management****
--------------------------

*   Basic functionality of tags is to filter data displayed within dashboards dynamically
    
*   Only user with MSP Administrator role can tag artifacts
    
*   Artifacts that support tags:
    
    a) Dashboards
    
    b) Datasets
    
    c) PStreams
    
    d) Credentials
    
*   All users belonging to a user group with specific tag(s) when they login they see only the artifacts with those particular tag(s)
    
*   Example: If a User Group is assigned **Tag Acme**, all the users in that user group when they login will see only the filtered artifacts that have **Tag Acme**.
    
*   Users with **msp-admin** or **workspace-admin** role can see all the artifacts
    

Tip

Please click on the pictures below to enlarge and to go back to the page please click on the back arrow button on the top.

****6.1 Add Tag****
-------------------

Login as user with **MSP Admin** role and go to **Menu** -> **Administration** -> **Tag Management**

[![Tag Management](https://bot-docs.cloudfabrix.io/images/tag_management/tag_management.png)](/images/tag_management/tag_management.png)

After you click Tag Management user would have the option to **Add Tag** on the top right side as shown in the screenshot below where **Name** and **Description** can be added and saved

[![Add Tag](https://bot-docs.cloudfabrix.io/images/tag_management/add_tag.png)](/images/tag_management/add_tag.png)

****6.2 Edit Tag****
--------------------

If the added tag description needs to be edited, user will have the option on the top right side as shown in the screenshot below to edit the Description

[![Tag Management](https://bot-docs.cloudfabrix.io/images/tag_management/tag_management_edit.png)](/images/tag_management/tag_management_edit.png)

After **Adding Tag** user would have the ability to edit description only for the added tag

[![Tag Management](https://bot-docs.cloudfabrix.io/images/tag_management/tag_management_edit1.png)](/images/tag_management/tag_management_edit1.png)

****6.3 Two Methods to Assign a Tag****
---------------------------------------

### ****6.3.1 Method One****

*   User needs to click on the Row Action and click on **View Artifacts**

[![View_Artifacts](https://bot-docs.cloudfabrix.io/images/tag_management/view_artifacts.png)](/images/tag_management/view_artifacts.png)

**View Artifacts** action shows the artifacts with that particular tag. The following tables are shown:

*   **User Groups** : List of user groups with that particular tag
    
*   **Dashboards** : List of user groups with that particular tag
    
*   **Persistant Streams** : List of pstreams with that particular tag
    
*   **Datasets** : List of datasets with that particular tag
    
*   **Credentials** : List of credentials with that particular tag
    

[![TAG View](https://bot-docs.cloudfabrix.io/images/tag_management/tag_view.png)](/images/tag_management/tag_view.png)

User can pick a name from that particular Artifacts list and Assign a Tag

To assign tag to a user group user can click on **Add Group** and Click on the Group to assign the Tag as Shown below in the screenshot

[![TAG View](https://bot-docs.cloudfabrix.io/images/tag_management/add_group.png)](/images/tag_management/add_group.png)

To delete Tag from user group user can click on **delete**

[![TAG View](https://bot-docs.cloudfabrix.io/images/tag_management/delete.png)](/images/tag_management/delete.png)

Note

We can Follow the same procedure to Add and Delete Tags for other Artifacts such as **Dashboards**, **Persistant Streams**, **Datasets** & **Credentials**

### ****6.3.2 Method Two****

Go to **Menu** -> **Configuration** → **RDA Administration** click on the **Row Action** and select **Manage Tags**

[![TAG View](https://bot-docs.cloudfabrix.io/images/tag_management/manage_tags.png)](/images/tag_management/manage_tags.png)

Click on the Tags which the User wants to Assign

[![TAG View](https://bot-docs.cloudfabrix.io/images/tag_management/added_tag.png)](/images/tag_management/added_tag.png)

The assigned Tag can be seen as shown below in the screenshot

[![TAG View](https://bot-docs.cloudfabrix.io/images/tag_management/assigned_tag.png)](/images/tag_management/assigned_tag.png)

Note

The Method Two can be used only for Datasets , Dashboards & Credentials

****7\. Portal UI - System Default Landing Page****
---------------------------------------------------

### ****7.1 Default Homepage****

When a User logs-in, the first page which shows up is the Landing Page, By default user can start the landing page in different places, User Group Level and User Level

Tip

Please click on the pictures below to enlarge and to go back to the page please click on the back arrow button on the top.

Default Landing Page would look same as shown in the screenshot shown below, when a user logs in for the first time the below home screen will be shown

[![Welcome Page](https://bot-docs.cloudfabrix.io/images/landing_page/welcome_page.png)](/images/landing_page/welcome_page.png)

### ****7.2 User Group Level****

Only **MSP Administrator** can setup home page at **User Group Level**. This step sets a default home page for all users in that user group. Once logged in as MSP Administrator, Go to the top on the left click and go to **Administration** --> **Users** --> **User Groups** and has action then select a dashboard to be the home page and select **Set Homepage** all users within the user group will have the same homepage

[![usergroup_sethompage](https://bot-docs.cloudfabrix.io/images/landing_page/usergroup_sethompage.png)](/images/landing_page/usergroup_sethompage.png)

[![Set Homepage](https://bot-docs.cloudfabrix.io/images/landing_page/sethomepage.png)](/images/landing_page/sethomepage.png)

In the screenshot below user can see the selected homepage showing up when they click on **Home** in the left side Menu Bar.

[![L2L3 Dashboard Homepage](https://bot-docs.cloudfabrix.io/images/landing_page/l2l3_dashboard.png)](/images/landing_page/l2l3_dashboard.png)

### ****7.3 User Level****

In the below screenshot a user by the name **acme@cfx.com** is logged in

[![User](https://bot-docs.cloudfabrix.io/images/landing_page/user.png)](/images/landing_page/user.png)

Note

The Below step is for example purpose only, User can select any Page to set as Homepage

when user logs in, **Menu** --> **Administration** --> **Authentication Servers** --> top right side user has the option to **Set as Home** as shown below in the screenshot.

[![User Homepage](https://bot-docs.cloudfabrix.io/images/landing_page/user_homepage.png)](/images/landing_page/user_homepage.png)

Here in the above screenshot the user selected Authentication Servers page as homepage and the user needs to click on **Set As Home** and then click on **Save**

[![Set As Home](https://bot-docs.cloudfabrix.io/images/landing_page/setashome.png)](/images/landing_page/setashome.png)

Go back to the Main Menu and click on **Home** again, the above updated homepage can be seen here in the Below Screenshot, This way they can select any page as Homepage

[![User Homepage](https://bot-docs.cloudfabrix.io/images/landing_page/userhomepage.png)](/images/landing_page/userhomepage.png)

### ****7.4 Reset Default Home Page****

Note

What ever the Home page user sets in the above section 9.3 will get replaced to default Homepage

if a user wants to go back to the default home page, he needs go to top right menu as shown in the below screenshot and select **My Account**

[![My Account](https://bot-docs.cloudfabrix.io/images/landing_page/my_account.png)](/images/landing_page/my_account.png)

The User would have the option to Reset Homepage and go back to the default Homepage, click on **Reset Homepage** and **Save**

[![Reset Homepage](https://bot-docs.cloudfabrix.io/images/landing_page/reset_homepage.png)](/images/landing_page/reset_homepage.png)

It goes back to the Default Home page which was L2 L3 Dashboard as shown in the one of the above screenshot

[![L2L3 Dashboard](https://bot-docs.cloudfabrix.io/images/landing_page/l2l3_dashboard.png)](/images/landing_page/l2l3_dashboard.png)

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!