# ### TASK 5. an SRE alert message

# ✍️ Task 5: SRE alert message

# File: python/task5.py (empty it first)

# Do this:

# Ask: Service name: , and clean the input with .strip().
# Ask: Error count: , and convert the input to int.
# Print an alert with an f-string.

# Expected output:

# Service name: payments
# Error count: 12
# ALERT: payments has 12 errors

# 🎯 Twist 1: show the service name in UPPERCASE:

# ALERT: PAYMENTS has 12 errors

# 🎯 Twist 2: these 12 errors happened over 5 minutes. Print the rate to 1 decimal place:

# Rate: 2.4 errors/min

# 💡 Syntax you’ll need:

# input("…").strip()
# int(input("…"))
# .upper()
# f"… {variable} …"
# rate = count / 5, then {rate:.1f}

# Send your code and output 


service = input("Service name: ").strip()
error_count = int(input("Error count: "))
print(f"ALERT: {service} has {error_count} errors")
print(f"ALERT: {service.upper()} has {error_count} errors")

rate = error_count / 5
print(f"Rate: {rate:.1f} errors/min")



