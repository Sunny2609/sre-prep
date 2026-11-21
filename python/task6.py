# ✍️ Task 6: fix the “1 errors” bug

# File: python/task6.py

# Background: your Task 5 printed ALERT: payments has 1 errors. Bad grammar in an alert looks unprofessional, and real tools like PagerDuty or Slack bots handle singular and plural properly.

# Steps:

# Ask: Service name: , cleaned with .strip().
# Ask: Error count: , converted with int().
# Use if / else:
# count is 1 → print ALERT: <service> has 1 error
# any other count → print ALERT: <service> has <count> errors

# Test cases (run all of them):

# Service	Count	Expected output
# payments	1	ALERT: payments has 1 error
# payments	12	ALERT: payments has 12 errors
# auth	2	ALERT: auth has 2 errors

# 🎯 Bonus: if the count is 0, print OK: payments has no errors instead of an alert. Now there are 3 outcomes, so which structure do you need?

# 💡 Hints:

# Compare with ==, not =.
# Bonus: check 0 first, then 1, then everything else.

# ⚠️ Common mistake: if error_count == "1": compares with the text "1", but error_count is an int after int(). Compare with the number 1, no quotes.

service_name = input("Service name: ").strip()
error_count = int(input("Error count: "))

if error_count == 1:
    print(f"ALERT: {service_name} has {error_count} error")
elif error_count == 0:
    print(f"OK: {service_name} has no errors")
else:
    print(f"ALERT: {service_name} has {error_count} errors")

    
