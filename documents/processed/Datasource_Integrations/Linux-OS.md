 



# Linux OS

CloudFabrix RDA provides out of the box agent-less integration for inventory data collection from Linux server OS editions using SSH protocol. Using this integration, inventory data like Linux OS version, server make & model, running services and processes and TCP/UDP network connections will be collected.

Using RDA's integration with Linux Server OS, below are the two primary use cases that are supported and consumed within the CloudFabrix Asset Intelligence and AIOps platforms.

*   Linux Server OS inventory &
    
*   Application Dependency
    

## ****1\. Prerequisites:****

**Linux OS inventory**

Supported Linux server OS distributions are, CentOS, RHEL and Ubuntu. SSH user account that is used to connect and collect the data should have sudo privileges for the below commands.

*   dmidecode
*   netstat
*   ss
*   nsenter\*\*
*   docker ps\*\*
*   docker ps -a\*\*
*   docker inspect\*\*

\*\*Applicable only for docker container environments

On CentOS, RHEL & Ubuntu, edit **/etc/sudoers** file and add the above commands for the user account that is used for data collection.
```
 <user_name> ALL=(root) NOPASSWD: /usr/sbin/dmidecode,/usr/bin/netstat,/usr/sbin/ss,/usr/bin/nsenter,/usr/bin/docker ps *,/usr/bin/docker inspect *,/usr/bin/docker top *

```

Note

In some of the Linux OS versions, above commands may be under /bin directory instead of /usr/bin, please verify the location path of these commands and configure them appropriately in **/etc/sudoers** file.

**Test SSH Connection with CLI access:**

To verify the SSH configuration, use ssh command which helps to test the remote connection to target Linux server over SSH protocol and an ability to execute a command.
```
 ssh [user-name]@[ip-address] [command] 
 
 ssh cfxuser@192.168.10.10 hostname

```

## ****2\. Adding Linux OS as Datasource/Extension in 'RDA':****

Linux OS or any other datasource/extension's configuration is configured in RDA's user interface. Login into RDA's user interface using a browser.

**https://\[rda-ip-address\]:9998**

Under **Notebook**, click on **CFXDX Python 3** box

![Linux_RDA_Studio](https://bot-docs.cloudfabrix.io/images/rda_integrations/linux/linux_linuxpython.png)

In the **Notebook** command box, type botadmin() and **alt (or option) + Enter** to open datasource administration menu.

Click on **Add** menu and under **Type** drop down, select **linux-inventory**

![Linux_RDA_Datasource](https://bot-docs.cloudfabrix.io/images/rda_integrations/linux/linux_linuxbotadmin.png)

*   **Type**: Datasource/Extension type. In this context, it is **linux-inventory**
*   **name**: Datasource/Extension label which should be unique within the RDA
*   **Hostname**: IP Address / DNS name of Linux host
*   **Username**: Linux username
*   **Password**: Linux password
*   **Private Key Passphrase**: SSH private key passphrase (optional)
*   **SSH Private Key**: SSH private key (optional)
*   **Port**: 22

Note

Hostname field is only used for a quick network access and authentication access check against any one of the valid Linux server host while adding the linux-inventory as a datasource. For actual data collection from Linux servers, it expects IP or IP subnet range as an input during runtime. Please refer the following sections for an example.

Click on **Check Connectivity** to verify the network access and credentials. Once it is validated, click on **Add** button to add the linux-inventory as a datasource.

## ****3\. Linux OS data exploration in RDA Studio:****

Once Linux OS integration details are configured in RDA as a datasource, it will be ready to connect to targe Linux servers and explore the data for the analysis.

For the details on Linux OS inventory data collection bots, refer [CloudFabrix RDA Bot Documentation](https://bot-docs.cloudfabrix.io/Extensions/extensions_L_N/#extension-linux-inventory "CloudFabrix RDA Bot Documentation")

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!