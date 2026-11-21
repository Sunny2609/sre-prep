# ✍️ Task 8: HTTP status code classifier

# File: python/task8.py

# 📖 Background (why SREs care)

# Every request to a website or API returns a 3-digit status code. During an incident, the first thing an SRE checks is which kind of codes are rising, because:

# 4xx means the client sent something wrong (a bad URL, no login). Usually that’s not our fault.
# 5xx means our server failed. Someone gets paged 🚨
# 🎯 What your program must do
# Ask: HTTP status code: and convert it to int.
# Classify it using this table:
# Code range	Print
# 200 – 299	Success
# 300 – 399	Redirect
# 400 – 499	Client error
# 500 – 599	Server error: investigate!
# anything else	Invalid code
# 🧪 Test cases (run all 8)
# Input	Expected output
# 200	Success
# 301	Redirect
# 404	Client error
# 499	Client error
# 500	Server error: investigate!
# 503	Server error: investigate!
# 600	Invalid code
# 99	Invalid code
# 💡 Hints
# A range check in one line: if 200 <= code <= 299:
# Use if / elif / elif / elif / else.
# Here the ranges don’t overlap, so does the order matter? Think about it 😉
# 🎯 Bonus 1: add the meaning of common codes

# For these codes, add the name in brackets:

# Code	Meaning
# 200	OK
# 404	Not Found
# 500	Internal Server Error
# 502	Bad Gateway
# 503	Service Unavailable
# 504	Gateway Timeout

# Example output:

# HTTP status code: 503
# Server error: investigate! (Service Unavailable)

# 💡 That needs a second if / elif chain that uses ==.

# 🎯 Bonus 2: the // trick

# Find the code’s class with floor division:

# python
# 503 // 100   # → 5
# 404 // 100   # → 4

# Rewrite your classifier to compare the class (== 2, == 3, == 4, == 5) instead of ranges.


status_code = int(input("HTTP status code: "))

if status_code <=199 or status_code >= 600:
    print("Invalid code")
elif status_code >=200 and status_code <=299:
    print("Success")
elif status_code >=300 and status_code <=399:
    print("Redirect")
elif status_code >=400 and status_code <=499:
    print("Client error")
elif status_code >=500 and status_code <=599:
    print("Server error:investigate!")