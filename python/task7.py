# ✍️ Task 7: disk usage severity

# File: python/task7.py

# Background: this is what tools like Prometheus Alertmanager or Nagios do with disk checks.

# Steps:

# Ask: Server name: (cleaned with .strip())
# Ask: Disk usage %: (converted with int())
# Decide the severity:
# 90 or more → CRITICAL
# 70 to 89 → WARNING
# below 70 → OK
# Print [<SEVERITY>] <server> disk at <usage>%

# Test cases (the boundaries matter most):

# Server	Disk	Expected output
# db-01	45	[OK] db-01 disk at 45%
# db-01	69	[OK] db-01 disk at 69%
# db-01	70	[WARNING] db-01 disk at 70%
# db-01	89	[WARNING] db-01 disk at 89%
# db-01	90	[CRITICAL] db-01 disk at 90%
# db-01	100	[CRITICAL] db-01 disk at 100%

# 🎯 Bonus 1: if the disk is below 0 or above 100, print Invalid disk value. Check this first.
# 🎯 Bonus 2: store the severity in a variable (severity = "WARNING"), and use one print() at the end instead of three.

# 💡 Hints:

# if / elif / else, most severe first.
# Bonus 1: if disk < 0 or disk > 100:


server_name = input("Server name: ").strip()
disk_usage = int(input("Disk usage %: "))


if disk_usage < 0 or disk_usage > 100 :
    print("Invalid disk value")
elif disk_usage >= 90:
    print(f"[CRITICAL] {server_name} disk at {disk_usage}%")
elif disk_usage >= 70:
    print(f"[WARNING] {server_name} disk at {disk_usage}%")
else:
    print(f"[OK] {server_name} disk at {disk_usage}%")

