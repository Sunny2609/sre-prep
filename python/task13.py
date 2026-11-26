# ✍️ Task 13: CPU report (lists + built-ins)

# File: python/task13.py

# Background: monitoring tools (Prometheus, Datadog) collect a CPU sample every few seconds. SREs summarise those samples: the peak, the lowest value, the average, and which samples breached the threshold.

# Use this list (no input needed):

# python
# cpu = [45, 82, 91, 30, 88, 67]

# Print exactly:

# Samples: 6
# Max: 91
# Min: 30
# Average: 67.2
# Above 80%: [82, 91, 88]
# Breaches: 3
# 💡 Thinking steps
# Samples, Max, Min: each is one built-in function (lesson 7, section 10).
# Average = total ÷ count. Which built-in gives the total? Then format it to 1 decimal place.
# Above 80%: the collect pattern again, like Bonus 3 you just did: an empty list, a loop, append if the value is over 80.
# Breaches: how many items are in that new list?
# 🎯 Bonuses
# Bonus 1: print the samples sorted from highest to lowest without changing cpu. (Which sorting tool keeps the original list unchanged?)
# Bonus 2: print the position of each breach, counting from 1:
# Sample 2: 82%
# Sample 3: 91%
# Sample 5: 88%

# 💡 enumerate (lesson 7, section 8).

# Bonus 3: if more than half the samples are above 80, print ALERT: sustained high CPU, otherwise OK: spikes only.

# Test Bonus 3 by changing the list to [85, 90, 95, 40]. That should print the ALERT line.

# Send it 👍

cpu = [45,82,91,30,88,67]

print(f"Samples: {len(cpu)}")
print(f"Max: {max(cpu)}")
print(f"Min: {min(cpu)}")
print(f"Average: {sum(cpu)/len(cpu):.1f}")

high_cpu = []

for value in cpu:
    if value > 80:
        high_cpu.append(value)
print(f"Above 80%: {high_cpu}")

print(f"Breaches: {len(high_cpu)}")

print(f"Sorted: {sorted(cpu, reverse=True)}")

for position , value in enumerate(cpu, start = 1):
    if value > 80:
        print(f"Sample {position}: {value}%")

if len(high_cpu) == 0:
    print("No breaches")

breaches = len(high_cpu) # Here , the high_cpu  = [82,91,88]
total = len(cpu) # Here , the cpu = [45,82,91,30,88,67]]

if breaches > total / 2:
    print("ALERT: sustained high CPU")
else:
    print("OK: spikes only")





