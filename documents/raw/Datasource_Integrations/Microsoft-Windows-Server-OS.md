 



Microsoft Windows Server OS
===========================

CloudFabrix RDA provides out of the box agent-less integration for inventory data collection from Microsoft Windows server editions using WinRM protocol. Using this integration, inventory data like Windows OS version, server make & model, running services and processes and TCP/UDP network connections will be collected.

Using RDA's integration with Windows Server OS, below are the two primary use cases that are supported and consumed within the CloudFabrix Asset Intelligence and AIOps platforms.

*   Windows Server OS inventory &
*   Application Dependency

****1\. Prerequisites:****
--------------------------

**Windows Server OS inventory**

Below are prerequisites which need to be configured on target Windows Server hosts.

*   PowerShell 3.0 or above
*   Operating system: Windows 2008 & R2, Windows 2012 & R2, Windows 2016 or above
*   Configure WinRM for remote management (refer WinRM configuration section)

WinRM OutofMemmory Hotfix is recommended - When running on PowerShell v3.0, there is a bug with the WinRM service that limits the amount of memory available to WinRM. KB2842230 [("Out of memory" error on a computer that has a customized MaxMemoryPerShellMB quota set and has WMF 3.0 installed (microsoft.com)](https://support.microsoft.com/en-us/topic/-out-of-memory-error-on-a-computer-that-has-a-customized-maxmemorypershellmb-quota-set-and-has-wmf-3-0-installed-9700d191-0033-d0c9-fb80-9761bbc1ab03)
 Lack of this fix on host, RDA may fail to execute certain commands on target host.

*   User Credentials

Note

Cloudfbarix recommends providing the local administrator privileges of the target server for the user account which is created for data collection (domain or local). However, In the absence of elevated privileges, discovery requires a user account that has enough privileges (read & execute) for WinRM remote management (WS-Man) and respective commands used in discovery. Refer the sections 2 & 3 for more information.

**WinRM configuration**:

CloudFabrix supports both WinRM configuration over HTTP/HTTPS and authentication protocols using Basic/NTLM .

Info

We recommend referring to the Microsoft document to configure WinRM over HTTP/HTTPS. The following configuration steps are for reference only.

**Configure WinRM over HTTP:**

Open command shell in windows and run the following command to quickly enable the WinRM with default configuration

`[](#__codelineno-0-1) winrm quickconfig`

*   Make sure to allow WinRM TCP port 5985 in Windows Firewall if it's enabled.
*   Similar configuration can be done from PowerShell console by executing following command.

`[](#__codelineno-1-1) Enable-PSRemoting -force`

**Configure WinRM over HTTPS:**

Info

Microsoft has published detailed information on how to configure WinRM over HTTPS @ [How to configure WINRM for HTTPS - Windows Client | Microsoft Docs](https://learn.microsoft.com/en-US/troubleshoot/windows-client/system-management-components/configure-winrm-for-https)

*   WinRM over HTTPS requires a certificate with CN matching the hostname.
*   Install/import the certificate on Windows Host Certificate --> Personal --> Certificates
*   Open command shell and execute the following command. It will create WinRM configuration and HTTPS listener

`[](#__codelineno-2-1) winrm quickconfig -transport:https`

*   Modify WinRM configuration
    
    The following parameters are required to modify apart from the default configuration.
    
*   Add CloudFabrix RDA’s IP address to TrustedHosts parameter or use “\*” to accept remote connections from any source. Following command helps to modify the TrustedHosts value.
    

`[](#__codelineno-3-1) winrm set winrm/config/client '@{TrustedHosts="*"}'`

*   Configure WinRM based on authentication method. CloudFabrix support both Basic/NTLM

`[](#__codelineno-4-1) winrm set winrm/config/service/auth '@{Negotiate="true"}'`

`[](#__codelineno-5-1) winrm set winrm/config/service/auth '@{Kerberos="true"}'`

Note

If you wanted to use **Basic** auth method then **AllowUnencrypted** parameter value should be set to **true**

`[](#__codelineno-6-1) winrm set winrm/config/service '@{AllowUnencrypted="true"}'`

*   CbtHardeningLevel value should be **Relaxed**

`[](#__codelineno-7-1) winrm set winrm/config/service/auth '@{CbtHardeningLevel="relaxed"}'`

**Configuring WinRM with Group Policy:**

Please refer the document from Microsoft to [configure WinRM using Group Policies.](https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management)

Info

We recommend to provide the elevated or local administrator privileges for the user account which is created for data collection (domain or local) for deep discovery. However, In the absence of elevated privileges, discovery requires an user account which has enough privileges (read & execute) for WinRM remote management (WS-Man). Refer the following Microsoft documentation for more information on user privileges @[https://docs.microsoft.com/en-us/windows/win32/winrm/authentication-for-remote-connections](https://learn.microsoft.com/en-us/windows/win32/winrm/authentication-for-remote-connections)

****2\. Assigning User Permissions for data collection****
----------------------------------------------------------

The following actions are required to get least read/execute privileges to **non-admin** users. These items are for reference only and providing the privileges depends on the customer infrastructure environment.

*   Create a local / domain user service account
*   Add the user account (which is created for data collection) to the following local group.

**WinRMRemoteWMIUsers\_\_ OR Remote Management Users**

*   Configure **execute**, **remote enable**, **read security**, and **enable account** permissions for the **Remote Management Users** group on the root WMI namespace and subnamespaces.

![Windows_WMI](https://bot-docs.cloudfabrix.io/images/rda_integrations/microsoft/microsoft_wmi.png)

![Windows_Administrators](https://bot-docs.cloudfabrix.io/images/rda_integrations/microsoft/microsoft_administrators.png)

![Windows_Remote_Management](https://bot-docs.cloudfabrix.io/images/rda_integrations/microsoft/microsoft_remotemanagement.png)

*   Provide explicit **read** & **execute** permissions to the user in WinRM SDDL configuration. Following command helps to configure the privileges.

`[](#__codelineno-8-1) winrm configSDDL default`

*   Provide explicit read/execute permissions to the user account (which is created for data collection) in powershell session configuration.

Following command helps to configure the privileges.

`[](#__codelineno-9-1) Set-PSSessionConfiguration -Name Microsoft.PowerShell -ShowSecurityDescriptorUI`

*   Grant **SC\_MANAGER\_CONNECT** and **GENERIC\_READ** permissions for `scmanager` (Service Control Manager) to the **service account** which is going to be used for data collection using the `sc.exe` command utility.

Execute the below script in a **powershell** CLI interface as an `Administrator` to list currently configured remote access permissions for built-in users / groups for `scmanager`.

`[](#__codelineno-10-1) Add-Type -TypeDefinition @' [](#__codelineno-10-2) using System; [](#__codelineno-10-3) namespace SCManager [](#__codelineno-10-4) { [](#__codelineno-10-5)     [Flags] [](#__codelineno-10-6)     public enum AccessMask [](#__codelineno-10-7)     { [](#__codelineno-10-8)         SC_MANAGER_CONNECT = 0x0001, [](#__codelineno-10-9)         SC_MANAGER_CREATE_SERVICE = 0x0002, [](#__codelineno-10-10)         SC_MANAGER_ENUMERATE_SERVICE = 0x0004, [](#__codelineno-10-11)         SC_MANAGER_LOCK = 0x0008, [](#__codelineno-10-12)         SC_MANAGER_QUERY_LOCK_STATUS = 0x0010, [](#__codelineno-10-13)         SC_MANAGER_MODIFY_BOOT_CONFIG = 0x0020, [](#__codelineno-10-14)         STANDARD_RIGHTS_REQUIRED = 0xF0000, [](#__codelineno-10-15)         STANDARD_RIGHTS_READ = 0x20000, [](#__codelineno-10-16)         STANDARD_RIGHTS_WRITE = 0x20000, [](#__codelineno-10-17)         STANDARD_RIGHTS_EXECUTE = 0x20000, [](#__codelineno-10-18)         SC_MANAGER_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED | [](#__codelineno-10-19)             SC_MANAGER_CONNECT | [](#__codelineno-10-20)             SC_MANAGER_CREATE_SERVICE | [](#__codelineno-10-21)             SC_MANAGER_ENUMERATE_SERVICE | [](#__codelineno-10-22)             SC_MANAGER_LOCK | [](#__codelineno-10-23)             SC_MANAGER_QUERY_LOCK_STATUS | [](#__codelineno-10-24)             SC_MANAGER_MODIFY_BOOT_CONFIG, [](#__codelineno-10-25)         GENERIC_READ = STANDARD_RIGHTS_READ | [](#__codelineno-10-26)             SC_MANAGER_ENUMERATE_SERVICE | [](#__codelineno-10-27)             SC_MANAGER_QUERY_LOCK_STATUS, [](#__codelineno-10-28)         GENERIC_WRITE = STANDARD_RIGHTS_WRITE | [](#__codelineno-10-29)             SC_MANAGER_CREATE_SERVICE | [](#__codelineno-10-30)             SC_MANAGER_MODIFY_BOOT_CONFIG, [](#__codelineno-10-31)         GENERIC_EXECUTE = STANDARD_RIGHTS_EXECUTE | [](#__codelineno-10-32)             SC_MANAGER_CONNECT | [](#__codelineno-10-33)             SC_MANAGER_LOCK, [](#__codelineno-10-34)         GENERIC_ALL = SC_MANAGER_ALL_ACCESS, [](#__codelineno-10-35)     } [](#__codelineno-10-36) } [](#__codelineno-10-37) '@ [](#__codelineno-10-38) $sddl = ((sc.exe sdshow scmanager) -join "").Trim() [](#__codelineno-10-39) $sd = ConvertFrom-SddlString -Sddl $sddl [](#__codelineno-10-40) $sd.RawDescriptor.DiscretionaryAcl | ForEach-Object { [](#__codelineno-10-41)     $sid = $_.SecurityIdentifier [](#__codelineno-10-42)     try { [](#__codelineno-10-43)         $account = $sid.Translate([Security.Principal.NTAccount]) [](#__codelineno-10-44)     } catch [Security.Principal.IdentityNotMappedException] { [](#__codelineno-10-45)         $account = $sid [](#__codelineno-10-46)     } [](#__codelineno-10-47)     [PSCustomObject]@{ [](#__codelineno-10-48)         Account = $account [](#__codelineno-10-49)         Access = [SCManager.AccessMask]$_.AccessMask [](#__codelineno-10-50)         AccessMask = '0x{0:X8}' -f $_.AccessMask [](#__codelineno-10-51)         AceType = $_.AceType [](#__codelineno-10-52)     } [](#__codelineno-10-53) } | Format-List`

[Example Output](#__tabbed_1_1)

`Account    : NT AUTHORITY\INTERACTIVE Access     : SC_MANAGER_CONNECT, GENERIC_READ AccessMask : 0x00020015 AceType    : AccessAllowed  Account    : NT AUTHORITY\SERVICE Access     : SC_MANAGER_CONNECT, GENERIC_READ AccessMask : 0x00020015 AceType    : AccessAllowed  Account    : NT AUTHORITY\Authenticated Users Access     : SC_MANAGER_CONNECT AccessMask : 0x00000001 AceType    : AccessAllowed  Account    : NT AUTHORITY\SYSTEM Access     : SC_MANAGER_CONNECT, SC_MANAGER_MODIFY_BOOT_CONFIG, GENERIC_READ AccessMask : 0x00020035 AceType    : AccessAllowed  Account    : BUILTIN\Administrators Access     : GENERIC_ALL AccessMask : 0x000F003F AceType    : AccessAllowed  Account    : BUILTIN\Hyper-V Administrators Access     : GENERIC_READ AccessMask : 0x00020014 AceType    : AccessAllowed`

In the above example output, `NT AUTHORITY\INTERACTIVE` and `NT AUTHORITY\SERVICE` accounts has both `SC_MANAGER_CONNECT` and `GENERIC_READ` permissions.

Run the below command in `cmd.exe` CLI interface as an `Administrator` to get the currently configured user access permission settings (a.k.a **SDDL** string) for **scmanager** (Service Control Manager) service.

`[](#__codelineno-11-1) sc.exe sdshow scmanager`

[Example Output](#__tabbed_2_1)

`D:(A;;LCRPRC;;;HA)(A;;CC;;;AU)(A;;CCLCRPRC;;;IU)(A;;CCLCRPRC;;;SU)(A;;CCLCRPWPRC;;;SY)(A;;KA;;;BA)(A;;CC;;;AC)S:(AU;FA;KA;;;WD)(AU;OIIOFA;GA;;;WD)`

**Syntax of above SDDL string:**

**Permission Code** for `NT AUTHORITY\SERVICE` account: A;;CCLCRPRC;;;

`NT AUTHORITY\SERVICE` account's short code: SU

Get SID of the service account user to whom the `SC_MANAGER_CONNECT` and `GENERIC_READ` permissions to be granted.

**Note:** Please run the below commands in `cmd.exe` CLI interface. `cfxuser` is used just for a reference.

`[](#__codelineno-12-1) wmic useraccount where name='cfxuser' get sid`

[Example Output](#__tabbed_3_1)

`SID S-1-5-21-93897503-1393288148-4093635276-1002`

Assign the `SC_MANAGER_CONNECT` and `GENERIC_READ` permissions to the service account user using the below command. In the above user permissions output for `scmanager`, `NT AUTHORITY\SERVICE` account has `SC_MANAGER_CONNECT` and `GENERIC_READ` permissions. Please apply the same permission codes to the **service account**.

Note

Please run the below command in `cmd.exe` CLI interface. The highlighted settings are the permission codes to configure `SC_MANAGER_CONNECT` and `GENERIC_READ` permissions for the SID of the service account user.

**sc.exe sdset scmanager D:(A;;LCRPRC;;;HA)(A;;CC;;;AU)(A;;CCLCRPRC;;;IU)(A;;CCLCRPRC;;;SU)(A;;CCLCRPWPRC;;;SY)(A;;KA;;;BA)(A;;CC;;;AC)(A;;CCLCRPRC;;;S-1-5-21-93897503-1393288148-4093635276-1002)S:(AU;FA;KA;;;WD)(AU;OIIOFA;GA;;;WD)**

*   Restart **Windows Remote Management** service (WS-Man)

****3\. Windows Commands used for data collection:****
------------------------------------------------------

*   Windows OS System Inventory

`[](#__codelineno-13-1) systeminfo /fo csv [](#__codelineno-13-2) (Get-WmiObject -Class win32_computersystemproduct).UUID [](#__codelineno-13-3) Get-WmiObject -Class Win32_Processor | Select-Object -Property Manufacturer,Name, NumberOfCores,NumberOfLogicalProcessors,SocketDesignation,CurrentClockSpeed,SystemName,Status" [](#__codelineno-13-4) [](#__codelineno-13-5) BIOS Details: [](#__codelineno-13-6) [](#__codelineno-13-7) $bios = @{};  [](#__codelineno-13-8) (Get-WmiObject -Class win32_computersystemproduct |  [](#__codelineno-13-9) select IdentifyingNumber, SKUNumber, UUID, Vendor).psobject.properties |  [](#__codelineno-13-10) % {$bios.Add($_.Name, $_.Value)};  [](#__codelineno-13-11) (Get-WmiObject -Class  win32_bios |  [](#__codelineno-13-12) select BIOSVersion, SerialNumber, ReleaseDate, Description, Manufacturer, Version).psobject.properties |  [](#__codelineno-13-13) % {$bios.Add($_.Name, $_.Value)}; new-object psobject -Property $bios`

*   Windows Service & Process Inventory

`[](#__codelineno-14-1) Get-WmiObject -Class Win32_Process [](#__codelineno-14-2) Get-WmiObject -Class Win32_Service`

*   Windows Application TCP/UDP Connections

`[](#__codelineno-15-1) nestat -ano [](#__codelineno-15-2) nestat -anob (Optional)`

*   Windows Network Configuration

`[](#__codelineno-16-1) Get-WmiObject -Class Win32_NetworkAdapterConfiguration | Select-Object -Property * [](#__codelineno-16-2) Get-WmiObject -Class Win32_NetworkAdapter | Select-Object -Property Index, NetConnectionStatus`

*   Windows installed Software Applications

`[](#__codelineno-17-1) Get-WmiObject Win32_Product |select-object Name,Version,Description,InstallDate,InstallDate2,InstallLocation,InstallSource,ProductID,RegCompany,RegOwner,Vendor`

**Test WinRM Connection:**

To verify the WinRM configuration, use winrs.exe command which helps to test the remote connection to target Windows server using WinRM protocol.

Below are the sample commands to verify:

`[](#__codelineno-18-1) winrs -r:http://<Target_Win_IPaddress>:5985 -u:username -p:password hostname [](#__codelineno-18-2) winrs -r:https://<Target_Win_IPaddress>:5986 -u:username -p:password hostname`

To verify WinRM port(s) 5985 or 5986 access check from a remote Windows system:

`[](#__codelineno-19-1) Test-NetConnection -computername "<Target_Win_IPaddress>" -P "5985" [](#__codelineno-19-2) Test-NetConnection -computername "<Target_Win_IPaddress>" -P "5986"`

****4\. Adding Microsoft Windows OS as Datasource/Extension in RDA Studio:****
------------------------------------------------------------------------------

Microsoft Windows OS or any other datasource/extension's configuration is configured in RDA's user interface. Login into RDA's user interface using a browser.

**https://\[rda-ip-address\]:9998**

Under **Notebook**, click on **CFXDX Python 3** box ![Windows_RDA_Studio](https://bot-docs.cloudfabrix.io/images/rda_integrations/microsoft/microsoft_python.png)

In the '**Notebook**' command box, type botadmin() and **alt (or option) + Enter** to open datasource administration menu. Click on '**Add**' menu and under **Type** drop down, select **windows-inventory** ![Windows_RDA_Datasource](https://bot-docs.cloudfabrix.io/images/rda_integrations/microsoft/microsoft_inventory.png)

*   **Type**: Datasource/Extension type. In this context, it is **windows-inventory**
*   **name**: Datasource/Extension label which should be unique within the RDA
*   **Hostname**: IP Address / DNS name of Windows host
*   **Username**: Windows username
*   **Password**: Windows password
*   **Port**: 5985 / 5986
*   **Transport Protocol**: http / https
*   **Auth Protocol**: basic / ntlm / kerberos
*   **Provider**: wsman (default value)

Info

**Hostname** field is only used for a quick network access and authentication access check against any one of the valid Window server host while adding the windows-inventory as a datasource. For actual data collection from Windows servers, it expects IP or IP subnet range as an input during runtime. Please refer the following sections for an example.

Click on **Check Connectivity** to verify the network access and credentials validity. Once it is validated, click on **Add** button to add the windows-inventory as a datasource.

****5\. Windows Server OS data exploration in RDA Studio:****
-------------------------------------------------------------

Once Windows OS integration details are configured in RDA as a datasource, it will be ready to connect to targe Windows servers and explore the data for the analysis.

For the details on Windows OS inventory data collection bots, refer [CloudFabrix RDA Bot Documentation](https://bot-docs.cloudfabrix.io/Extensions/extensions_T_Z/#extension-windows-inventory "CloudFabrix RDA Bot Documentation")

Was this page helpful?

Thanks for your feedback!

Thanks for your feedback!