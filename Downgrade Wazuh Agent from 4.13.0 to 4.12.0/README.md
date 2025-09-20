## Dongrad Wazuh Agent from 4.13.0 to 4.12.0 in Linux Endpoint
**Remove current version of Wazuh agent**<br> 
`sudo apt-get remove --purge wazuh-agent`<br>
**Download the 4.12.0 version of the Wazuh agent package**<br>
`wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.12.0-1_amd64.deb`<br>
**Install the downloaded version**<br> 
`sudo dpkg -i wazuh-agent_4.12.0-1_amd64.deb`<br>
**Check the installed version**<br> 
`dpkg -l | grep wazuh-agent`<br>
**Set manager ip address in /var/ossec/etc/ossec.conf file in <server> tag**<br>
*<address>MANAGER_IP_ADDRESS</address>*<br>
**Check status of agent**<br> 
`sudo systemctl status wazuh-agent`<br>
*If wazuh-agent is active on endpoint and disconnected on the manager side/dashboard, one possible reason is that the agent enrollment is password protected*<br>
Verify in the Wazuh manager /var/ossec/etc/ossec.conf file <auth> block, <use_password> tag, if yes the enrollment is password protected.<br>
Check password in /var/ossec/etc/authd.pass file of wazuh manager and create a file in the end point with password.<br> 
`echo “YOUR_PASSWORD” > /var/ossec/etc/authd.pass`<br>
**Change its permissions and ownership**<br>
`sudo chmod 640 /var/ossec/etc/authd.pass`<br>
`sudo chown root:wazuh /var/ossec/etc/authd.pass`<br>
**Restart agent** 
