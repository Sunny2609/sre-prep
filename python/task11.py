# ✍️ Task 11: Character report for a hostname

# File: python/task11.py

# 📖 Background

# Hostnames follow rules: letters, digits, hyphens and dots only. Before creating DNS records, servers or Kubernetes resources, automation scripts often check what a name contains, because a bad character (like an underscore or a space) can break DNS or a deployment.

# 🎯 What your program must do
# Ask: Hostname: and remove extra spaces at both ends.
# Go through the hostname one character at a time.
# Count three things:
# letters (a–z, A–Z)
# digits (0–9)
# other characters (everything else, such as - or .)
# Print one line in this exact format:
# Letters: <X>, Digits: <Y>, Other: <Z>
# 🧪 Test cases (run all 5)
# Hostname typed	Expected output
# web-01.prod	Letters: 7, Digits: 2, Other: 2
# db01	Letters: 2, Digits: 2, Other: 0
# api-gateway-eu-west-1	Letters: 15, Digits: 1, Other: 5
# 12345	Letters: 0, Digits: 5, Other: 0
# web01 (spaces around)	Letters: 3, Digits: 2, Other: 0
# 💡 Hints
# Lesson 6, section 4: the digits example you dry-ran. This is the same pattern, with three counters.
# String methods: .isalpha() checks for a letter, .isdigit() checks for a digit.
# Each character is exactly one of the three types, so think if / elif / else.
# 🎯 Bonus 1: total check

# Also print the total length, and confirm the counts add up:

# Letters: 7, Digits: 2, Other: 2
# Total: 11 (matches length: True)
# 🎯 Bonus 2: hostname validation

# After the counts, print Valid hostname if the name contains only letters, digits, - and .; otherwise print Invalid hostname.

# Hostname	Expected 2nd line
# web-01.prod	Valid hostname
# web_01	Invalid hostname (underscore)
# web 01	Invalid hostname (space in the middle)
# db@01	Invalid hostname
# 🎯 Bonus 3: uppercase warning

# DNS names are case-insensitive, but the convention is lowercase. If the hostname contains any uppercase letter, print:
# Warning: hostname contains uppercase letters

# Hostname	Expected extra line
# Web-01	Warning: hostname contains uppercase letters
# web-01	(no warning)
# 🎤 Interview questions (answer out loud afterwards)
# "Name two rules a valid DNS hostname must follow."
# "Why do underscores in hostnames cause problems?"
# "Your script counts characters in a 10 GB log file the same way. What's the problem, and what would you change?"

# Send your code and all outputs 👍


hostname = input("Hostname: ").strip()
letters = 0
digits = 0
other = 0
valid = True
has_upper = False
for ch in hostname:
    if ch.isalpha():
        letters += 1
        if ch.isupper():
            has_upper = True
        

    elif ch.isdigit():
        digits += 1
    else:
        other += 1
        if ch != "-" and ch != ".":
            valid = False
        
print(f"Letters: {letters}, Digits: {digits}, Other: {other}")
total = letters + digits + other
print(f"Total : {total} (matches length: {total == len(hostname)}) ")

if valid:
    print("Valid hostname")
else:
    print("Invalid hostname")

if has_upper:
    print("Warning: hostname contains uppercase letters")