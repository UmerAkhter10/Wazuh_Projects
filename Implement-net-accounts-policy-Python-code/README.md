## Goal

The objective of this task is to develop a Python-based solution (packaged as an executable) that automates the verification and remediation of `net accounts` settings in alignment with the CIS Windows 10 Benchmark. This will reduce reliance on manual UI-based corrections suggested by the Wazuh SCA module, thereby saving time and effort while ensuring consistent compliance.

## Setup Instructions 
### 1. Development of Python Code and Executable file
[Python Code](cis_win10_benchmark_net_accounts_remediations.py) is developed and [.exe file](cis_win10_benchmark_net_accounts_remediations.exe) is created using pyinstaller.

### 2. Execute the .exe on a fresh, unconfigured Windows 10 system
#### Before execution 'net accounts' result
![Preview Failed](Implement-net-accounts-policy-Python-code-screenshots/1.png)<br><br>
#### Execution 
![Preview Failed](Implement-net-accounts-policy-Python-code-screenshots/2.png)<br><br>
![Preview Failed](Implement-net-accounts-policy-Python-code-screenshots/3.png)<br><br>
![Preview Failed](Implement-net-accounts-policy-Python-code-screenshots/4.png)<br><br>
![Preview Failed](Implement-net-accounts-policy-Python-code-screenshots/5.png)<br><br>
#### After execution 'net accounts' result
Executing the program enforces the configured net accounts policies on the target Windows 10 system.<br>
![Preview Failed](Implement-net-accounts-policy-Python-code-screenshots/6.png)<br><br>
#### Again execute the file
![Preview Failed](Implement-net-accounts-policy-Python-code-screenshots/7.png)<br><br>


