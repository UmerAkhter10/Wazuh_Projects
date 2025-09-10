import ctypes # For system-level operations (e.g., checking if script is run as admin on Windows).

import subprocess # Enables running external system commands and programs from within Python.
                  # Useful for executing shell commands (like 'net accounts', 'gpresult', etc.) and capturing their output.

import re # Provides Regular Expression (regex) support for advanced string searching and pattern matching.
          # Often used to extract specific information from command outputs or text.

def is_admin():
    # Verify whether the script is running with administrator (elevated) privileges
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except: # If not return 'False'
        return False
    
# Functions for matching, verifying, and correcting 'net accounts' configuration values
def net_accounts_config(output, i,r):
        # Search for the targeted string
        match = re.search(r[2], output) # r[2] is the regex pattern for the check, obviously it will be unique for all checks
        # If the regex pattern finds a match in the output
        if match:
            print(f"Check id: {i}") # print check id e.g. 15500
            print(f"title: {r[0]}") # print check title
            print(f"description: {r[1]}", end='\n\n') # print check short description
            # Capture the first matched group (the targeted value) into a variable.
            current_value = match.group(1)
            # if captured group is not like 'None', 'Never', or 'Unlimited', check its value 
            if current_value.isdigit() and r[4](int(current_value)): # r[4] is the condition for the targeted value e.g. current_value == 24, condition is different for all checks
                print(f"Current {r[3]} is {current_value} — compliant with policy.", end="\n\n") #if value is compliant with policy
            else:
                print(f"Current {r[3]} is {current_value} — not compliant with policy requirements.")  #if value is not compliant with policy   
                try:
                        # regulate the targeted value
                        subprocess.run(['net', 'accounts', f'{r[5]}:{r[6]}'], check=True) # r[5] is the command window command and r[6] is the rquired value.
                        print(f"{r[3].capitalize()} is set to {r[6]}.", end="\n\n") # print the new value
                except subprocess.CalledProcessError as e:
                        print(f"Failed to set {r[3]}: {e}") # print the error message if occured
        else:
            print(f"Could not find {r[3]} setting.") # print error message if match is not found
   
def main():

    if not is_admin(): # If return value is False, script will not run further. 
        print("Please run this script as an administrator.")
        return
    
    # Dictionary of checks (keys:IDs and values:Lists)
    '''
            list index 0: Title
            list index 1: Description
            list index 2: Regex Pattern
            list index 3: Unique string for each check
            list index 4: Condition
            list index 5: Unique command to set value
            list index 6: Required value 
    '''
    checks = {
 
         "15500": [ 
              "Ensure 'Enforce password history' is set to 24 or more password(s).",
              """This policy requires users to use at least 24 unique new passwords 
                              before reusing an old one, preventing password cycling.
                              It strengthens security by reducing the risk of brute force attacks 
                              and limiting the impact of compromised accounts.""",
              r'Length of password history maintained:\s+(\w+)',
              "password history length", 
              lambda x: x == 24,
              '/uniquepw', 
              24    
         ],
         "15501":[
               "Ensure 'Maximum password age' is set to '365 or fewer days, but not 0'.",
               """This policy controls how long a password can be used before it must be changed, 
                             with a range of 0–999 days. To reduce the risk of compromise, passwords should 
                             expire regularly (recommended ≤365 days, not 0)""", 
               r'Maximum password age \(days\):\s+(\w+)',
               "maximum password age",
               lambda x: x <= 365 and x > 41,
               '/maxpwage',
               42
         ],
         "15502":[
               "Ensure 'Minimum password age' is set to '1 or more day(s)'.",
               """This policy defines how many days a user must keep a password before 
                             being allowed to change it (0 allows immediate changes, recommended ≥1).
                             It ensures the Enforce Password History setting is effective by stopping users 
                             from cycling through quick password changes to reuse old ones.""" ,
               r'Minimum password age \(days\):\s+(\w+)',
               "minimum password age",
               lambda x: x >= 2,
               '/minpwage',
               2
         ], 
         "15503":[
               "Ensure 'Minimum password length' is set to '14 or more character(s)'.",
               """This policy sets the minimum number of characters required in a password (recommended 14 or more).
                             Longer passwords or passphrases greatly improve resistance against brute force and 
                             dictionary attacks, making accounts more secure.""",
               r'Minimum password length:\s+(\w+)',
               "minimum password length",
               lambda x: x >= 14,
               '/minpwlen',
               14
         ],    
         "15506":[
               "Ensure 'Account lockout duration' is set to '15 or more minute(s)'.",
               """This policy defines how long a locked account stays inaccessible 
                             before automatically unlocking (0 = requires admin unlock).
                             The recommended setting is 15 minutes or more, which balances 
                             security against attacks with usability for legitimate users.""",
               r'Lockout duration \(minutes\):\s+(\w+)',
               "lockout duration",
               lambda x: x >= 15 and x <= 20,
               '/lockoutduration',
               15
         ],          
         "15507":[
               "Ensure 'Account lockout threshold' is set to '5 or fewer invalid logon attempt(s), but not 0'.",
               """This policy specifies the number of failed login attempts allowed before an 
                                account is locked (recommended: 5 or fewer, but not 0).It helps prevent brute force attacks, 
                                though setting it too low may cause accidental or intentional account lockouts.""",
               r'Lockout threshold:\s+(\w+)',
               "lockout threshold",
               lambda x: x == 5,
               '/lockoutthreshold',
               5
         ],
         "15508":[
               "Ensure 'Reset account lockout counter after' is set to '15 or more minute(s)'.",
               """This policy defines how long (in minutes) before the failed login attempt counter resets to zero. 
                                Setting it to 15 minutes or more helps balance security against brute-force attacks while 
                                reducing accidental account lockouts.""",
               r'Lockout observation window \(minutes\):\s+(\w+)',
               "lockout observation window",
               lambda x: x >= 15 and x <= 20,
               '/lockoutwindow',
               15
         ]           
    }
   
    try:
        # Run the 'net accounts' command
        result = subprocess.run(['net', 'accounts'], capture_output=True, text=True)
        result_output = result.stdout

    except Exception as e: # print error message 
        print(f"Error in net accounts command: {e}")
        return
    
    # Pass output of net accounts, check id and list of rule as argument to the function.
    for id, rule in checks.items():
        net_accounts_config(result_output, id, rule)


if __name__ == "__main__":
    main()
