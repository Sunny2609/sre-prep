# ✍️ Task 12: Server name generator (loops)

# File: python/task12.py

# Background: when scaling out (Terraform count, Ansible inventories, Kubernetes StatefulSets), servers get predictable names. Zero-padding keeps them sorted correctly.

# Steps

# Ask Prefix: (.strip().lower())
# Ask Count: (int)
# Print one name per line, from 01, always 2 digits
# Prefix	Count	Expected
# web	3	web-01, web-02, web-03
# DB	12	db-01 … db-12
# cache	0	prints nothing

# 🎯 Bonus 1: ask for the environment → web-01.prod
# 🎯 Bonus 2: if count > 99, use 3 digits → web-001 … web-150
# 🎯 Bonus 3: collect the names in a list, then print Generated 3 hostnames: web-01 to web-03

# 💡 Search: "python f-string zero padding"

prefix = input("Prefix: ").strip().lower()
count = int(input("Count: "))
environment = input("Environment: ").strip().lower()


if count > 99:
        width = 3
else:
        width = 2

names = []

for i in range(1,count+1):
        name = f"{prefix}-{i:0{width}d}.{environment}"
        print(name)
        names.append(name)
        
if len(names) == 0:
        print("Generated 0 hostnames")
elif len(names) == 1:
        print(f"Generated 1 hostname: {names[0]}")
else:
        print(f"Generated {len(names)} hostnames: {names[0]} to {names[-1]}")
          



   
          
          




    
   

