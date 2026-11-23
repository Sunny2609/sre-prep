# 🟢 C1: Service health decision

# File: python/c1_health.py

# Where this style shows up: bank GCC SRE rounds (JPMorgan, Barclays, Citi, Goldman), and the scripting part of Tier B rounds (Walmart, PayPal). They love “given these metrics, decide the state” questions.

# 📖 Background

# Load balancers, Kubernetes probes and uptime monitors don’t look at one signal. They combine several to decide whether a service is healthy. A service can return HTTP 200 and still be slow or failing for some users.

# 🎯 What your program must do
# Ask: HTTP status code: → int
# Ask: Latency (ms): → int
# Ask: Error rate (%): → float (it can be 0.5)
# Decide, most severe first:
# Condition	Print
# status is 5xx (500–599) or error rate > 5	DOWN
# latency > 1000 or error rate > 1	DEGRADED
# otherwise	HEALTHY
# 🧪 Test cases (run all 6)
# Status	Latency	Error %	Expected
# 200	120	0.2	HEALTHY
# 200	1500	0.2	DEGRADED (slow)
# 200	300	2.5	DEGRADED (some errors)
# 503	100	0.1	DOWN (server error)
# 200	200	7	DOWN (too many errors)
# 200	1000	1	HEALTHY ← boundary! (> not >=)
# 💡 Hints
# float(input(...)) for the error rate.
# or joins two conditions in one if.
# 5xx: 500 <= status <= 599 (or status // 100 == 5).
# 🎯 Bonus

# Print the reason too, e.g. DEGRADED (latency 1500 ms > 1000 ms).
# 💡 You’ll need separate checks to know which condition fired.

# 🎤 Interview angle

# “Why check error rate and not just the status code?” → One request returning 200 tells you nothing about the other 10,000. SREs alert on rates over time, not single responses.



status_code = int(input("HTTP status code: "))
latency = int(input("Latency (ms): "))
error_rate = float(input("Error rate (%): "))

if 500 <= status_code <= 599:
    print(f"DOWN (server error {status_code})")
elif error_rate > 5:
    print(f"DOWN (error rate {error_rate}% > 5%)")
elif latency > 1000:
    print(f"DEGRADED (latency {latency} ms > 1000 ms)")
elif error_rate > 1:
    print(f"DEGRADED (error rate {error_rate}% > 1%)")
else:
    print("HEALTHY")


# 🟢 C2: TLS certificate expiry check

# File: python/c2_cert.py

# Where this style shows up: bank GCCs (JPMorgan, Barclays, Citi, Goldman, HSBC), payments and fintech (Visa, Mastercard, PayPal, Razorpay, PhonePe). Certificate expiry is a top outage and audit risk in these companies.

# 📖 Background

# Every HTTPS website has a TLS certificate with an expiry date. When it expires, browsers and API clients refuse to connect, so the service goes down for every user at once, even though the servers are perfectly healthy. SRE teams monitor every certificate and alert well before expiry.

# 🎯 Main task
# Ask: Domain:  and normalise it to lowercase with no extra spaces.
# Ask: Days until expiry:  as a whole number. It can be 0 or negative if the certificate has already expired.
# Print one line based on the days left:
# Days left	Output
# 0 or less	EXPIRED: <domain> — site is down for users!
# 1 to 7	CRITICAL: renew <domain> now (<days> days left)
# 8 to 30	WARNING: renew <domain> soon (<days> days left)
# more than 30	OK: <domain> valid for <days> days
# 🧪 Main test cases (run all 8)
# Domain typed	Days	Expected output
# pay.hsbc.com	-2	EXPIRED: pay.hsbc.com — site is down for users!
# pay.hsbc.com	0	EXPIRED: pay.hsbc.com — site is down for users!
# pay.hsbc.com	1	CRITICAL: renew pay.hsbc.com now (1 days left)
# pay.hsbc.com	7	CRITICAL: renew pay.hsbc.com now (7 days left)
# pay.hsbc.com	8	WARNING: renew pay.hsbc.com soon (8 days left)
# pay.hsbc.com	30	WARNING: renew pay.hsbc.com soon (30 days left)
# pay.hsbc.com	31	OK: pay.hsbc.com valid for 31 days
#  PAY.HSBC.COM 	200	OK: pay.hsbc.com valid for 200 days
# 🎯 Bonus 1: grammar

# 1 days left looks unprofessional in an alert. When exactly 1 day is left, print 1 day left; otherwise days.

# Days	Expected
# 1	CRITICAL: renew pay.hsbc.com now (1 day left)
# 5	CRITICAL: renew pay.hsbc.com now (5 days left)
# 🎯 Bonus 2: renewal deadline

# Company policy: certificates must be renewed at least 14 days before expiry. For every certificate that has not expired, print a second line:

# If more than 14 days are left: Renew within <X> days (where X = days left minus 14)
# If 14 days or fewer are left: Past renewal deadline — escalate!
# Days	Line 1	Line 2
# 20	WARNING: … (20 days left)	Renew within 6 days
# 15	WARNING: … (15 days left)	Renew within 1 days (or 1 day if you combine with Bonus 1)
# 14	WARNING: … (14 days left)	Past renewal deadline — escalate!
# 5	CRITICAL: … (5 days left)	Past renewal deadline — escalate!
# 200	OK: pay.hsbc.com valid for 200 days	Renew within 186 days
# -2	EXPIRED: …	(no second line)
# 🎯 Bonus 3: input validation
# If the domain is empty (the user just pressed Enter), print Invalid domain and nothing else.
# If days is more than 825, print Invalid: certificates can't be valid that long and nothing else.
# Domain	Days	Expected
# (empty)	30	Invalid domain
# pay.hsbc.com	900	Invalid: certificates can't be valid that long
# 🎤 Interview questions to answer out loud afterwards
# “How do you prevent certificate-expiry outages?”
# “Automatic renewal is set up. Why do you still need monitoring?”
# “How would you check the expiry date of a live site from the Linux command line?”

# Write the code, run every test case, then send your code, the outputs, and your 3 answers 👍

domain = input("Domain: ").strip().lower()

days_left = int(input("Days until expiry: "))

if days_left == 1:
    day_word = "day"
else:
    day_word = "days"


if domain == "":
    print("Invalid domain and nothing else")
elif days_left > 825 :
    print("Invalid: certificates can't be valid that long and nothing else.")
elif days_left <= 0:
    print(f"EXPIRED: {domain} - site is down for users!")
elif days_left <= 7:
    print(f"CRITICAL: renew {domain} now ({days_left} {day_word} left)")
elif days_left <= 30:
    print(f"WARNING: renew {domain} soon ({days_left} {day_word} left)")
else:
    print(f"OK: {domain} valid for {days_left} {day_word}")



# 🟢 C3: Change-freeze check

# File: python/c3_change_window.py

# Where this style shows up: banks above all (JPMorgan, Barclays, Citi, Deutsche Bank, HSBC, Goldman), where production changes are allowed only in approved change windows (ITIL / change management).

# 📖 Background

# Banks can't risk breaking payments during business hours. So production deploys are only allowed in a change window, at low-traffic times, with an approved change request and a rollback plan.

# 🎯 Main task
# Ask: Day (mon/tue/wed/thu/fri/sat/sun): and normalise it (lowercase, no extra spaces).
# Ask: Hour (0-23): as a whole number.
# First, if the hour is outside 0–23, print Invalid hour and nothing else.
# Deploys are allowed only when both are true:
# the day is Saturday or Sunday, and
# the time is from 22:00 to 05:59 (hour 22, 23, 0, 1, 2, 3, 4 or 5)
# Print Deploy allowed or Blocked: outside change window.
# 🧪 Main test cases (run all 9)
# Day	Hour	Expected
# sat	23	Deploy allowed
# sun	2	Deploy allowed
# sat	22	Deploy allowed
# sun	5	Deploy allowed
# sun	6	Blocked: outside change window
# sat	21	Blocked: outside change window
# sat	14	Blocked: outside change window
# wed	23	Blocked: outside change window
# SAT	25	Invalid hour
# 🎯 Bonus 1: day validation

# If the day isn't one of the 7 valid values, print Invalid day and nothing else.

# Day	Hour	Expected
# funday	23	Invalid day
# Saturday	23	Invalid day
# 🎯 Bonus 2: emergency change

# Ask a third question: Emergency change? (yes/no): . An approved emergency change (e.g. a security fix or an outage fix) is allowed at any time on any day, and prints:
# Deploy allowed (EMERGENCY - post-change review required)

# Day	Hour	Emergency	Expected
# wed	14	yes	Deploy allowed (EMERGENCY - post-change review required)
# wed	14	no	Blocked: outside change window
# sat	23	no	Deploy allowed
# wed	30	yes	Invalid hour
# 🎯 Bonus 3: helpful block message

# When blocked, tell the user when the next window opens:

# Weekday (mon–fri) → Blocked: next window opens Saturday 22:00
# Weekend daytime (6–21) → Blocked: window opens today at 22:00
# Day	Hour	Expected
# wed	23	Blocked: next window opens Saturday 22:00
# sat	14	Blocked: window opens today at 22:00

















