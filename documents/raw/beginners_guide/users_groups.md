 



Users & Groups
==============

This Document provides instructions on User Onboarding (various roles), The changes introduced to support MSP Functionality & Data Filtering across Various Organizations

****User Onboarding****
-----------------------

To support MSP functionality we added new roles. Here are the following roles

### ****Workspace Administrator****

**Description:** This is the role given to the default user (admin@cfx.com). This user is super user who can on board all the different user roles and also has permissions to do both administration and configuration of users and organizations.

### ****MSP Administrator****

**Description:** This user has administrator permissions to add, edit, delete, configure, administer multiple organizations and to onboard users across multiple organizations and assign different roles to the users.

### ****MSP User****

**Description:** This user has permissions to see dashboards assigned to them and also, can perform certain actions (please capture what actions???) This user can be associated with one or more organizations. This user will not have any administrator or configuration privileges.

### ****Organization (Tenant) Administrator****

**Description:** This user is assigned to a specific organization by either Workspace Administrator or MSP Administrator. This user has privilege to configure the assigned organization. Also, this user can onboard users with either Organization Admin, Organization User, L1, L3, Organization Read Only Users as well for the assigned organization.

### ****Organization User****

**Description:** This user has permissions to see dashboards assigned and also can perform certain actions. This user can be associated with only one organization. No administrator or configuration privileges.

### ****MSP Read Only User****

**Description:** This user has only read only access to see dashboards assigned and cannot perform any actions. This user can be associated with more than one organization. No administrator or configuration privileges (Difference between MSP user and MSP RO user is that, this user will not have any associated actions).

### ****Organization Read Only User****

**Description:** This user has read only permission to see dashboards assigned and also cannot perform any actions. This user can be associated with only one organization. No administrator or configuration privileges (Difference between Or Organization user and Organization RO user is that, this user will not have any associated actions).

### ****L3 User****

**Description:** This user is the same as the Organization User with different privileges. This user can be associated with only one organization.

### ****L1 User****

**Description:** This user is the same as the Organization User with even less privileges. This user can be associated with only one organization.

### ****User Roles and Permissions****

**RDA Permissions for Dashboards**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| View | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Enable | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Disable | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Dashboards Groups**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| View | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Enable | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Disable | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Datasets**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| View | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Ingest | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Manage | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Clone | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Export | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Schemas**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Pstreams**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| View | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Pipelines**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| View | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Verify | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Run | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Publish | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Formatting Templates**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Stacks**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| View | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Service Blueprints**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| View | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Enable | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Disable | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Deploy | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Alert Rules**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| View | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Bundles**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Compare | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Deploy | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Credentials**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| View | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Verify | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Site Profiles**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| View | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Staging Areas**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| View | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Log Archives**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| View | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Fabric Health**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| View | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Users**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |
| Reset Password | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |
| Activate | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |
| Deactivate | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |
| Manage | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |
| View | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |

**RDA Permissions for User Groups**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Organizations**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |
| Configure | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for MSP Details**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Update | Yes | Yes | No  | No  | No  | No  | No  | No  | No  |

**RDA Permissions for Authentication Severs**

| RDA Permissions | Workspace Admin | MSP Admin | Organization Admin | MSP User | Organization User | MSP RO User | Organization RO User | L1 User | L3 User |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Add | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |
| Edit | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |
| Delete | Yes | Yes | Yes | No  | No  | No  | No  | No  | No  |

### ****Steps to onboard user****

Login as workspace administrator(admin@cfx.com)

![msp_login](https://bot-docs.cloudfabrix.io/images/users_groups/login.png)

After Login on the left side the user can find Menu for Workspace administrator, The user needs to select Administration

![msp_administration](https://bot-docs.cloudfabrix.io/images/users_groups/administration.png)

Select Organizations section form the the left side Menu Bar to add new Organization

Note

Workspace Administrator can add Multiple Organizations

![msp_Organizations](https://bot-docs.cloudfabrix.io/images/users_groups/organizations.png)

After selecting Organizations here as shown below the user can Add New Organization

![msp_Add_Organization](https://bot-docs.cloudfabrix.io/images/users_groups/add_organization.png)

Note

Workspace administrator can add multiple organizations

Select Users Section on the left side Menu Bar to on-board users. select the User Groups tab above

![msp_Users_Usergroups](https://bot-docs.cloudfabrix.io/images/users_groups/users_usergroups.png)

Here after selecting User Groups on the right side you will find Add Group click on that and Add a New User Group

![msp_Adduser_Usergroups](https://bot-docs.cloudfabrix.io/images/users_groups/adduser_usergroups.png)

![msp_Dropdown](https://bot-docs.cloudfabrix.io/images/users_groups/dropdown.png)

![msp_Adding_Usergroups](https://bot-docs.cloudfabrix.io/images/users_groups/adding_usergroups.png)

In the above Screenshot, **User1** has **MSP Administrator** role and is associated with organizations ‘ACME’ and ‘Coke’ (two organizations/tenants)

Note

Each User Group is associated with a particular role. Based on the role selected administrators can assign one or more organizations. If the selected role is MSP Administrator, MSP User or MSP Read Only User then this user group can be associated with one or more organizations. Any other role (except for Workspace Administrator) only one organization can be associated.

Select the Users Tab to add New user, New user is on boarded by adding the user details and assigning the user to a User Group. All the users will have the same role that is associated with the User Group and across all the organizations within the User Group.

![msp_Adduser_users](https://bot-docs.cloudfabrix.io/images/users_groups/adduser_users.png)

In the below Screenshot, `cfx_admin@cfx.com` user is added to MSP Admin Group. Meaning, this `cfx_admin@cfx.com` user will have an MSP Administrator role across organizations

![msp_Adduser_user1](https://bot-docs.cloudfabrix.io/images/users_groups/adduser_user1.png)

Here in the below Screenshot the added user can be seen

![msp_Addeduser](https://bot-docs.cloudfabrix.io/images/users_groups/addeduser.png)

To view the permissions associated with each role select View Permissions action, users can select this action by selecting three dots which is at the right side of each user as shown in the below screenshot

![msp_Userid](https://bot-docs.cloudfabrix.io/images/users_groups/userid.png)

Once a user is On-boarded, appropriate dashboards need to be assigned to that User Group. Dashboards that are assigned to the User Group will be visible to all the users within that group

Note

Except for Workspace Administrator and MSP Administrator who have access to all the dashboards

*   **Adding a new Dashboard Group**

Home -> Configuration -> RDA Administration -> Dashboards -> Dashboard Groups

![msp_RDA](https://bot-docs.cloudfabrix.io/images/users_groups/rda.png)

![msp_Dashboards](https://bot-docs.cloudfabrix.io/images/users_groups/dashboards.png)

Each Dashboard Group is associated with one or more User Groups and one or more dashboards.

![msp_Add_Dashboard](https://bot-docs.cloudfabrix.io/images/users_groups/add_dashboard.png)

Added Dashboard group can be seen in the screenshot below

![msp_Added_Dashboard](https://bot-docs.cloudfabrix.io/images/users_groups/added_dashboard.png)

Login with cfx\_admin@cfx.com with default password “changeme” and then will ask for reset password

![msp_Changeme](https://bot-docs.cloudfabrix.io/images/users_groups/changeme.png)

![msp_resetpassword](https://bot-docs.cloudfabrix.io/images/users_groups/resetpassword.png)

*   **Changes to support MSP Functionality**

Only **Workspace Administrators** and **MSP Administrators** have privileges to administer and configure various organizations. These roles can on board users across different organizations with different roles

**Organization Administrators** can be associated with only one organization and can configure that organization only. Also, this user can on board users with roles at the same level that is Organization Administrator, Organization Read Only User, L1 User and L3 User for that organization. In addition, this user has access to only dashboards that are assigned and associated to this user group.

*   Menu for Organization Administrator

![msp_Menu](https://bot-docs.cloudfabrix.io/images/users_groups/menu.png)

All the RDA related administration have been moved under '**RDA Administration**' and '**RDA Integrations**' options that are visible only for Workspace Administrator and MSP Administrator

Some of the diagnostic related UI are moved under '**Fabric Health**' and can be accessed only by Workspace Administrator and MSP Administrator

### ****Data filtering across various organizations****

Users are associated to the organizations based on the user groups they belong to. If they have any '**MSP**' related roles then they can have access to the organization(s) that are associated within the user group. The users cannot have access to organizations which they are not associated with.

**Example:**

A setup has 3 organizations Org1, Org2, Org3 with the following users and the associated roles

| User | Role | Organizations | Dashboards |
| --- | --- | --- | --- |
| User1 | MSP Admin | Org1, Org2 | Incidents, Alerts |
| User2 | MSP Admin | Org2, Org3 | Incidents, Alerts |
| User3 | MSP User | Org2, Org3 | Incidents |
| User4 | Organization Admin | Org1 | Incidents, Alerts |
| User5 | Organization User | Org1 | Incidents, Alerts |
| User6 | MSP Read Only User | Org2, Org3 | Incidents, Alerts |
| User7 | Organization Read Only User | Org1 | Incidents, Alerts |
| User8 | L1 User | Org1 | Incidents, Alerts |
| User9 | L3 User | Org1 | Incidents, Alerts |

*   **User1** is ‘MSP Admin’ for organizations Org1 and Org2. That user will be able to perform all the actions within the dashboards Incidents and Alerts. User1 shouldn’t be able to see data from Org3.
    
*   **User2** is ‘MSP Admin’ for organizations Org2 and Org3. That user will be able to perform all the actions within the dashboards Incidents and Alerts. User2 shouldn’t be able to see data from Org1.
    
*   **User3** is ‘MSP User’ for Org2 and Org3. User3 can see only the dashboard ‘Incidents’. User3 cannot see Org1 data and also ‘Alerts’ dashboard. The actions that User3 can perform within the ‘Incidents’ dashboard are a subset of the MSP Admin role.
    
*   **User4** is Organization Admin for only Org1. User4 shouldn’t be able to see data from Org2 and Org3. User4 can perform all the actions within Incidents and Alerts dashboards
    
*   **User5** is Organization User for only Org1. User5 shouldn’t be able to see data from Org2 and Org3. User5 can perform only subset of actions within Incidents and Alerts dashboards
    
*   **User6** is ‘MSP Read Only User’ for Org2 and Org3. User6 can see the dashboards ‘Incidents’ and ‘Alerts’. User6 cannot see Org1 data. User6 cannot perform any actions with the dashboards.
    
*   **User7** is ‘Organization Read Only User’ for Org1. User7 can see the dashboards ‘Incidents’ and ‘Alerts’. User7 cannot see Org2 and Org3 data. User7 cannot perform any actions with the dashboards.
    
*   **User8** is L1 User for only Org1. User8 shouldn’t be able to see data from Org2 and Org3. User8 can perform only subset of actions within Incidents and Alerts dashboards
    
*   **User9** is L3 User for only Org1. User9 shouldn’t be able to see data from Org2 and Org3. User9 can perform only subset of actions within Incidents and Alerts dashboards
    
*   **Migration**
    
    Current setups on boarded only tenant admin and tenant users. The corresponding roles are renamed as "**Organization Admin** and "**Organization User**". Also all screens related to RDA have been moved under "**Configuration**" and "**Fabric Health**" menus which can be accessible only to MSP Admin or Workspace Admin roles. If the current tenant admin needs to access those screens that user role has to be changed to msp admin. The following steps need to be performed to migrate those users from tenant admin to msp admin
    

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!