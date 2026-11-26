# 📘 Lesson 7: Lists

# A list holds many values in one variable, in order. Almost all SRE data comes as collections: servers, log lines, IPs, pods, error codes. Lists are how Python holds them.

# Run the examples in demo.py and compare with the # comments.

# 1. Creating a list

servers = ["web-01", "web-02", "db-01"]
cpu = [45, 82, 91, 30]
empty = []

print(servers)        # ['web-01', 'web-02', 'db-01']
print(len(servers))   # 3
print(type(cpu))      # <class 'list'>

# Square brackets [ ], items separated by commas.

# 2. Indexing: get one item

servers = ["web-01", "web-02", "db-01"]

print(servers[0])     # web-01   ← first item is index 0
print(servers[2])     # db-01
print(servers[-1])    # db-01    ← -1 = last item
print(servers[-2])    # web-02   ← second from the end

# ⚠️ servers[3] crashes with IndexError: list index out of range. With 3 items, valid indexes are 0, 1, 2.

# 3. Slicing: get a part of the list

nums = [10, 20, 30, 40, 50]
print(nums[1:3]) # [20,30]
print(nums[:2]) # [10,20]
print(nums[2:]) # [30,40,50]
print(nums[-2:]) # [40, 50]
print(nums[::-1]) # [ 50,40,30,20,20] #reversed

# Same rule as range: the stop is never included. Slicing works on strings too: "web-01"[:3] → "web".

# 4. Lists can be changed (strings can't)

servers = ["web-01","web-02","db-01"]
servers[1] = "web-99"
print(servers) # ["web-01","web-99","db-01"]

name = "web"
# name [0] = "W" ❌ TypeError: strings are immutable

# Lists are mutable ( changeable in place). Strings are immutable.

# 5. Adding items

servers = ["web-01"]
servers.append("web-02")
print(servers)    # ["web-01","web-02"]

servers.insert(0, "lb-01") 
print(servers)   #["lb-01","web-01","web-02"]

servers.extend(["db-01","db-02"])
print(servers)   #["lb-01","web-01","web-02","db-01","db-02"]

# Use extend to add each item separately.

# 6. Removing items 

servers = ["lb-01","web-01","web-02","db-01"]
servers.remove("web-02")
print(servers) # ["lb-01","web-01","db-01"]

last = servers.pop() # remove + return the LAST item
print(last) # db-01
print(servers) # ["lb-01","web-01"]

# pop removes an item by index and hands it back to you. With no index it removes and returns the last item, which is handy for draining a list one item at a time:
first = servers.pop(0) # remove + return by INDEX
print(first) # lb-01

# 7. Checking and counting

codes = [200,500,200,404,500,500]
print(500 in codes) # True
print(301 in codes) # False
print(codes.count(500)) # 3
print(codes.index(404)) # 3

# in is the safe way to ask "is it there?" before remove() or index()

# 8. Loopimng over a list

servers = ["web-01","web-02","db-01"]
for server in servers:
    print(f"Checking {server} ...")

# Need the position too ? Use enumerate:

for i, server in enumerate(servers, start=1):
    print(f"{i}. {server}")

# 1. web-01
# 2. web-02
# 3. db-01

# enumerate gives you two values each round: the counter and the item


#  9. Building a list inside a loop ( the collect pattern)

cpu = {"web-01":0} 

usage = [45,82,91,30,88]
high = []

for value in usage:
    if value > 80:
        high.append(value)  

print(high) #[82, 91, 88] 
print(f"{len(high)} readings above 80%")

# 10. Built-in helpers: min, max, sum, sorted

latency = [120,340,95,410,200]

print(min(latency)) # 95
print(max(latency)) # 410
print(sum(latency)) # 1165
print(sum(latency) / len(latency)) # 233.0

print(sorted(latency)) # [95,120,200,340,410]
print(sorted(latency, reverse = True)) #[410,340,200,120,95]
print(latency) # unchanged

# sorted(x) returns a new sorted list. x.sort() sorts the same list in place and returns None:
 
latency.sort()
print(latency) #[95,120,200,340,410]

result = latency.sort()
print(result) # None

# 11. Strings ↔ lists: split() and join() ⭐

line = "2026-11-25 ERROR db-01 timeout"
parts = line.split() # split on spaces
print(parts) # ['2026-11-25', 'ERROR', 'db-01', 'timeout']
print(parts[1]) # ERROR
print(parts[2]) # db-01

host = "web-01.prod.hsbc"
print(host.split(".")) # ['web-01', 'prod', 'hsbc']

names = ["web-01","web-02","db-01"]
print(", ".join(names)) # web-01, web-02, db-01
print("\n".join(names)) # one per line

# split() turns a log line into fields. join() builds output from a list. You'll use both in almost every log parsing question.


# 12 . The copy trap (Tier A favourite)

a = ["web-01","web-02"]
b = a
b.append("db-01")
print(a) # ["web-01","web-02","db-01"]

c = a.copy() # a real copy (or a[:])
c.append("cache-01")
print(a) # unchanged
print(c)  # ['web-01','web-02','db-01','cache-01']

# b = a doesn't copy anything. It gives the same list a second name. This causes real bugs, e.g. a function that "filters" a server list and silently changes the original inventory.


# Quick check (predict, then run)

x = [5, 10, 15, 20, 25]
print(x[1:4])          # [10,15,20]
print(x[-1])           # 25
print(x[::-1][0])      # 25

y = [3, 1, 2]
z = y.sort()
print(z)               # None

a = [1, 2]
b = a
b.append(3)
print(a)               # [1,2,3]

print("a,b,,c".split(","))   # ['a','b','','c']