## Goal

Set up alerts to monitor when execute permissions are granted to shell scripts, ensuring that potentially harmful scripts are flagged before execution to prevent data loss or system damage.

## Setup Instructions 
## At Ubuntu Endpoint
1. Create a directory e.g. `/testdir`<br>
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/1.png)<br>
2. Create a script file in the directory e.g. `testscript.sh`<br>
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/2.png)<br>
3. Put this script file on monitoring from */var/ossec/etc/ossec.conf* file of Ubuntu agent.<br>
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/3.png)<br>
4. Verify that monitoring is started by checking this file in the **Inventory** of FIM module in Wazuh dashboard.<br> 
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/4.png)<br>
5. 
