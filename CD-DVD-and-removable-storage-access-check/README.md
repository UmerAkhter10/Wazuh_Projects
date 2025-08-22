## Goal

The goal of this project is security configuration assessment of all removable storage devices (such as USB drives and CD/DVDs) on endpoints using Wazuh. This includes detecting any read, write, or execution configuration enabled from such devices and monitoring at SCA module of Wazuh dashboard.

1. To apply this check for Windows 10 only, we have to define rule for requirement block of .yml file. In Windows we can check product name from following reg query,<br>
`reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v ProductName`<br>
![reg query for targeted OS](CD-DVD-and-removable-storage-access-check/2.png)
