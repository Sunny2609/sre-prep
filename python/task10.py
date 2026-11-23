# ✍️ Task 10: Retry with limits ⭐

# File: python/task10.py

# 📖 Background

# Real health checks often fail once or twice due to network blips. So monitoring tools retry a few times before declaring a service down, but never forever. If it still fails after the maximum attempts, they page on-call.

# 🎯 What your program must do
# Allow a maximum of 5 attempts.
# On each attempt, ask: Attempt <N> - healthy? (yes/no): (clean with .strip().lower())
# If the answer is yes:
# print Service healthy after <N> attempt(s)
# stop asking
# If all 5 answers are no, print:
# FAILED: service unhealthy after 5 attempts - paging on-call
# 🧪 Test cases

# Test 1: healthy at once

# Attempt 1 - healthy? (yes/no): yes
# Service healthy after 1 attempt(s)

# Test 2: healthy on the 3rd try

# Attempt 1 - healthy? (yes/no): no
# Attempt 2 - healthy? (yes/no): no
# Attempt 3 - healthy? (yes/no): YES
# Service healthy after 3 attempt(s)

# Test 3: never healthy

# Attempt 1 - healthy? (yes/no): no
# Attempt 2 - healthy? (yes/no): no
# Attempt 3 - healthy? (yes/no): no
# Attempt 4 - healthy? (yes/no): no
# Attempt 5 - healthy? (yes/no): no
# FAILED: service unhealthy after 5 attempts - paging on-call

# ⚠️ In Test 1 and 2, the FAILED line must not appear.

# 🎯 Bonus 1

# Print 1 attempt vs 3 attempts properly (like Task 6 / C2), instead of attempt(s).

# 🎯 Bonus 2

# Ask the user for the max attempts at the start, instead of fixing it at 5.

# 🎯 Bonus 3

# If the user types anything other than yes/no (e.g. maybe), print Invalid answer, counting as failure 

# 🎤 Interview angle

# "Why limit retries? Why not keep trying until it works?"



MAX_ATTEMPTS = int(input("Max attempts: "))
healthy = False



for attempt in range (1, MAX_ATTEMPTS+1):
    answer = input(f"Attempt {attempt} - healthy? (yes/no): ").strip().lower()
    if answer == "yes":
        if attempt == 1:
            word = "attempt"
        else:
            word = "attempts"
        print(f"Service healthy after {attempt} {word}")
        healthy = True
        break
    elif answer != "no":
        print("Invalid answer, counting as failure")
if not healthy:
    print(f"FAILED: service unhealthy after {MAX_ATTEMPTS} attempts - paging on-call")


