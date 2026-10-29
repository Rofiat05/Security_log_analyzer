import csv
from collections import Counter
 
failed_ips = Counter()
successful = 0
failed = 0
unknown = 0
 
with open("sef_logs.csv", "r", encoding="utf-8-sig") as file:
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
 
print("=== SECURITY LOG ANALYSIS ===")
print("Successful logins:", successful)
print("Failed logins:", failed)
print("Unknown results:", unknown)
 
print("\n=== FAILED LOGIN ANALYSIS ===")
 
for ip, count in failed_ips.items():
    print("IP Address:", ip)
    print("Failed Attempts:", count)
 
    if count >= 3:
        print("SECURITY ALERT: Repeated failed logins!")
 
    print("------------------------")