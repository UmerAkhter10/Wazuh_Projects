## Dongrad Wazuh Agent from 4.13.0 to 4.12.0 in Linux Endpoint
**Remove current version of Wazuh agent**<br> 
`sudo apt-get remove --purge wazuh-agent`
Download the desired 4.12.0 version of the Wazuh agent package:
wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.12.0-1_amd64.deb
install the downloaded version 
sudo dpkg -i wazuh-agent_4.12.0-1_amd64.deb
check installed version 
dpkg -l | grep wazuh-agent
add manager ip address in /var/ossec/etc/ossec.conf file in <server> tag
<address>MANAGER_IP_ADDRESS</address>
check status of agent 
sudo systemctl status wazuh-agent
if active on endpoint and disconnected on the manager side/dashboard, one possible reason is the agent is password protected
verify in the Wazuh server /var/ossec/etc/ossec.conf file <auth> block, <use_password> tag, if yes the enrollment is password protected
check password in /var/ossec/etc/authd.pass file of wazuh manager
and create a file in the end point with password 
echo “YOUR_PASSWORD” > /var/ossec/etc/authd.pass
change its permissions and ownership
sudo chmod 640 /var/ossec/etc/authd.pass
sudo chown root:wazuh /var/ossec/etc/authd.pass
restart agent 
