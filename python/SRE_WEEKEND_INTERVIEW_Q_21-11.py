# 🛠️ SRE-1: SLO compliance check ⭐

# File: python/sre1_slo.py

# 📖 Background (a real SRE concept)

# An SLO (Service Level Objective) is a reliability target, for example “99.9% of requests must succeed this month.”

# Availability = the percentage of requests that succeeded
# Error budget = how many failures you’re allowed before you break the SLO

# SREs check this every day. If the SLO is breached, feature releases stop until reliability is fixed. That’s a core SRE practice from the Google SRE book.

# 🎯 What your program must do
# Ask: Total requests: (an int)
# Ask: Failed requests: (an int)
# Calculate the availability %:
# availability = (total - failed) / total * 100
# Print it to 2 decimal places.
# Compare it with an SLO of 99.9:
# availability ≥ 99.9 → ✅ SLO met
# otherwise → ❌ SLO breached
# 🧪 Test cases
# Total	Failed	Expected output
# 100000	50	Availability: 99.95% → ✅ SLO met
# 100000	100	Availability: 99.90% → ✅ SLO met ← boundary!
# 100000	200	Availability: 99.80% → ❌ SLO breached
# 5000	0	Availability: 100.00% → ✅ SLO met
# 🎯 Bonus 1: error budget

# Add this:

# Allowed failures (budget): 100
# Budget used: 50.0%

# 💡 Allowed failures = total * (100 - 99.9) / 100, and budget used % = failed / allowed * 100

# 🎯 Bonus 2: edge cases (Tier B thinking)
# If total is 0, you’d divide by zero and crash 💥 Print No traffic: cannot calculate instead.
# If failed > total, print Invalid input.

# 💡 Check these before doing the maths.

# 🎤 Interview angle

# Questions you should be able to answer out loud after this:

# “What’s the difference between an SLI, an SLO and an SLA?”
# SLI = the measurement (e.g. success rate)
# SLO = the internal target (99.9%)
# SLA = the contract with the customer, with penalties (usually looser, e.g. 99.5%)
# “99.9% monthly: how much downtime is that?” → about 43 minutes a month
# “What happens when the error budget runs out?” → feature releases freeze, and the team focuses on reliability work

# Send your code and output 👍

# total_requests = int(input("Total requests: "))
# failed_requests = int(input("Failed requests: "))

# availability = (total_requests - failed_requests)/(total_requests)*100


# SLO = 99.9

# if availability >= SLO:
#     print(f"Availability: {availability:.2f}% - SLO met ")
# else:
#     print(f"Availability: {availability:.2f}% - SLO breached")




# 🎯 SRE-1 Bonus: full question

# Add both bonuses to your existing SLO file.

# 📖 Background: what is an error budget?

# If your SLO is 99.9%, you’re allowed to fail 0.1% of requests. That allowance is your error budget.

# Example: 100,000 requests × 0.1% = 100 failures allowed this month.

# 50 failed → you’ve used 50% of the budget (still safe)
# 100 failed → 100% used (right at the limit)
# 150 failed → 150% used (budget blown → release freeze 🧊)

# Teams track “budget used %” on dashboards because it tells you how much risk you can still take (deploys, experiments) before breaking the SLO.

# ✍️ What your program must do (final version)

# Step 1: inputs (same as before)

# Total requests: 
# Failed requests:

# Step 2: Bonus 2, validate first (before any maths)

# Condition	Print	Then
# total == 0	No traffic: cannot calculate	stop (nothing else prints)
# failed < 0 or failed > total	Invalid input	stop

# Step 3: availability + SLO (your existing code)

# Availability: 99.95% - SLO met

# Step 4: Bonus 1, error budget

# allowed_failures = total * (100 - SLO) / 100
# budget_used      = failed / allowed_failures * 100

# Print:

# Allowed failures (budget): 100
# Budget used: 50.0%

# Step 5 (extra challenge): budget status

# Budget used	Print
# < 50%	Budget healthy
# 50% – 99.9%	Budget at risk: slow down risky deploys
# ≥ 100%	Budget exhausted: freeze releases
# 🧪 Test cases (run all)
# Total	Failed	Expected output
# 100000	20	99.98% met → budget 100 → used 20.0% → healthy
# 100000	50	99.95% met → budget 100 → used 50.0% → at risk
# 100000	100	99.90% met → budget 100 → used 100.0% → exhausted
# 100000	150	99.85% breached → budget 100 → used 150.0% → exhausted
# 0	0	No traffic: cannot calculate
# 50	80	Invalid input
# 100	-5	Invalid input
    

total_requests = int(input("Total requests: "))
failed_requests = int(input("Failed requests: "))
SLO = 99.9

if total_requests == 0:
    print("No traffic: cannot calculate")
elif failed_requests < 0 or failed_requests > total_requests:
    print("Invalid input")
else:

    availability = (total_requests - failed_requests)/(total_requests)*100



    if availability >= SLO:
        print(f"Availability: {availability:.2f}% - SLO met ")
    else:
        print(f"Availability: {availability:.2f}% - SLO breached")

    allowed_failures = total_requests * (100 - SLO) / 100
    budget_used = failed_requests / allowed_failures * 100

    print(f"Allowed failures (budget): {allowed_failures:.0f}")
    print(f"Budget used: {budget_used:.1f}%")


    if budget_used >= 100:
        print("Budget exhausted: freeze releases")
    elif budget_used >= 50:
        print("Budget at risk: slow down risky deploys")
    else:
        print("Budget healthy")






