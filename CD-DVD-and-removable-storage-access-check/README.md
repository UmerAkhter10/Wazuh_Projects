## Goal

The goal of this project is security configuration assessment of all removable storage devices (such as USB drives and CD/DVDs) on endpoints using Wazuh. This includes detecting any read, write, or execution configuration enabled from such devices and monitoring at SCA module of Wazuh dashboard.

## Setup Instructions 

1. To apply this check only on Windows 10 systems, you need to define a rule within the requirement block of the .yml file. On Windows, you can verify the product name by querying the registry using the following command:<br>
`reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v ProductName`<br><br>
![reg query for targeted OS](CD-DVD-and-removable-storage-access-check-screenshots/2.png) <br><br>
You can also verify this manually using the Registry Editor: press Windows key + R, type regedit, and navigate to
*HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion*.<br>
![regedit to check targeted OS](CD-DVD-and-removable-storage-access-check-screenshots/1.png) <br><br>
So, the rule for requirement block will be `'r:HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion -> ProductName -> r:^Windows 10'`


