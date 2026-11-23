# ✍️ Task 9: Countdown before a deploy

# File: python/task9.py

# 📖 Background

# Many deploy tools show a short countdown before a risky action, such as a production deploy, a restart or a database migration. It gives the engineer a few seconds to press Ctrl + C and cancel if they realise something is wrong. It's a small but real safety habit.

# 🎯 What your program must do
# Ask: Seconds:  and convert it to int.
# Count down from that number to 1, printing one line each time:
# Deploying in <n>...
# After the countdown, print: 🚀 Deploying now!
# 🧪 Test cases (run all 4)

# Input 3:

# Deploying in 3...
# Deploying in 2...
# Deploying in 1...
# 🚀 Deploying now!

# Input 5:

# Deploying in 5...
# Deploying in 4...
# Deploying in 3...
# Deploying in 2...
# Deploying in 1...
# 🚀 Deploying now!

# Input 1:

# Deploying in 1...
# 🚀 Deploying now!

# Input 0:

# 🚀 Deploying now!

# (No countdown lines, because there's nothing to count.)

# 💡 Hints
# You know exactly how many times to repeat, so which loop fits best? (Remember the 3-question rule.)
# Look at section 2 of the lesson: there's a range() that counts down.
# ⚠️ Watch the stop value: you want the last line to be 1, not 0, and remember the stop number is never included.
# 🚀 Deploying now! must print only once, so think about its indentation.
# 🎯 Bonus 1: real 1-second pauses

# Make it wait 1 second between each line, like a real countdown.
# (Search: "python sleep 1 second". You'll need an import at the top of the file.)

# 🎯 Bonus 2: write it with while

# Write a second version (task9_while.py) that produces the same output using a while loop instead of for.
# Then answer: which version is cleaner, and why?

# 🎯 Bonus 3: input validation

# If the user types a negative number, print Invalid: seconds can't be negative and nothing else.

# 🎤 Interview angle

# "Why do some tools ask for confirmation or show a countdown before production changes?"
# → To prevent accidents. Many big outages started with someone running a command on the wrong environment. Good SREs build guardrails: confirmations, dry-run modes, countdowns, and clear labels saying which environment you're about to change.

# Send your code and outputs 👍



seconds = int(input("Seconds: "))

if seconds < 0:
        print("Invalid: seconds can't be negative")
else:
      
    for i in range(seconds, 0 , -1):
        print(f"Deploying in {i}...")
        
    print("Deploying now!")


        
        


