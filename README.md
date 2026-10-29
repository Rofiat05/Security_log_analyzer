Security Log Analyser
Project Overview
This project uses Python to analyse authentication logs and identify potentially suspicious login activities.
The program reads login records stored in a CSV file and examines successful, failed and unknown login attempts.
Project Objectives
Count successful and failed login attempts.
Identify IP addresses associated with repeated failed logins.
Generate security alerts when an IP address records three or more failed attempts.
Support security monitoring and investigation.
Technologies Used
Python
Visual Studio Code
CSV files
Git and GitHub
How the Program Works
Python reads the authentication records from sef_logs.csv.
It examines each login result.
It counts successful, failed and unknown results.
It groups failed attempts by source IP address.
It displays a security alert when an IP address has three or more failed attempts.
How to Run
Open the project folder in VS Code and run:
py read_logs.py
Alternatively, use python read_logs.py if that command works on your computer.
Security Significance
Repeated failed login attempts can indicate incorrect passwords, account access problems or potentially suspicious authentication activity.
The program helps identify events requiring further investigation. An alert alone does not prove that an attack occurred.
Project Status
Initial security log analysis implemented. Further testing and improvements are planned.
