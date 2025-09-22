## Goal

Set up alerts to monitor when execute permissions are granted to shell scripts, ensuring that potentially harmful scripts are flagged before execution to prevent data loss or system damage.

## Setup Instructions 
## At Ubuntu Endpoint
1. Create a directory e.g. `/testdir`<br>
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/1.png)<br>
2. Create a script file in the directory e.g. `testscript.sh` and check its permissions<br>
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/2.png)<br>
3. Put this script file on monitoring from */var/ossec/etc/ossec.conf* file of Ubuntu agent.<br>
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/3.png)<br>
4. Verify that monitoring is started by checking this file in the **Inventory** of FIM module in Wazuh dashboard.<br> 
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/4.png)<br>
5. Modify file (add some text) and check alert is generated or not.<br>
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/5.png)<br>
Check this in the **Events** of FIM module,<br>
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/6.png)<br>
7. Now cheange the permissions of file and analyze what alert is generated,<br> 
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/7.png)<br>
Check this in the **Events** of FIM module, Integrity Check rule is triggered again (id 550), not specific rule for permission change<br>
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/8.png)<br>
That's why we need to write a custom rule.<br>
But before, revert the changes,<br>
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/9.png)<br>
## At Wazuh Manager
8. Create a file for custom FIM rule */var/ossec/etc/rules/fim_custom_rules.xml*, add the custom rule to generate alert for change in execution permissions for scipt files,<br>
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/10.png)
9. Restart wazuh manager `sudo systemctl restart wazuh-manager`
10. Again change the permissions of script file (at Ubuntu endpoint) and observe custom rule is triggered,<br>
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/11.png)
Check this in the **Events** of FIM module,<br>
![Error](Alert-on-Execution-Permission-Grant-for-script-Files-in-Ubuntu-Screenshots/12.png)
Now the custom permission check rule is triggered. 
