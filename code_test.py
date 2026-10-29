import csv
from collections import Counter
from pathlib import Path
 
# Locate the CSV file
folder = Path(__file__).parent
csv_file = folder / "sef_logs.csv"
report_file = folder / "security_report.txt"
 
# Start counting login results
successful = 0
failed = 0
unknown = 0
failed_ips = Counter()
 
# Read the login records
with open(csv_file, "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
 
    for row in reader:
        ip = row["Source_IP"].strip()
        result = row["Result"].strip().lower()
 
        if result in ("successful", "sucessful"):
            successful += 1
 
        elif result == "failed":
            failed += 1
            failed_ips[ip] += 1
 
        else:
            unknown += 1
 
# Prepare the security report
report = "=== SECURITY ANALYSIS REPORT ===\n"
report += f"Successful logins: {successful}\n"
report += f"Failed logins: {failed}\n"
report += f"Unknown results: {unknown}\n"
 
report += "\n=== FAILED LOGIN ANALYSIS ===\n"
 
for ip, count in failed_ips.items():
    report += f"\nIP Address: {ip}\n"
    report += f"Failed Attempts: {count}\n"
 
    if count >= 3:
        report += "SECURITY ALERT: Repeated failed logins!\n"
 
# Save the report to a separate file
with open(report_file, "w", encoding="utf-8") as file:
    file.write(report)
 
# Display the report in the terminal
print(report)
print("Report saved to security_report.txt")