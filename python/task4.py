## Lesson for Task 4: Working with Strings"

# 1. Changing case
host = "Web-01.Prod"
print(host.upper()) # WEB-01.PROD
print(host.lower()) # web-01.prod

# 2. Methods don't change the original
host = "Web-01.Prod"
print(host.upper()) # WEB-01.PROD
print(host) # Web-01.Prod

host = host.upper() # store the result to keep it
print(host) # WEB-01.PROD

## 3. Length with len()
print(len("web-01")) # 6
print(len("web-01.prod")) # 11
print(len("db 01")) # 5 -> spaces count too

# Note: len() is a function , not a method , so you write len(host), not host.len()

## 4. Repeating a string with * ####
print("-" * 5) # -----
print("=" * 20) # ====================
print("ab" * 3) # ababab

### 5. An underline that matches a word's length ####
word = "ALERT"
print(word) # ALERT
print("-" * len(word)) # -----

### 6. Everyday methods ( these will come up a lot in SRE scripts)
print("  web-01  ".strip())                     # web-01
print("web-01.prod".replace("prod", "dev"))     # web-01.dev
print("web-01.prod".startswith("web"))          # True
print("web-01.prod".endswith(".prod"))         # True

# Note:  .strip() is very useful with input(), because users often type extra spaces by accident.


### 7. Splitting a string into parts #####
host = "web-01.prod.hsbc"
parts = host.split(".")

print(parts) # ['web-01', 'prod', 'hsbc']
print(parts[0]) # web-01
print(parts[1]) # prod
print(parts[2]) # hsbc

### 8. Methods inside f-strings ###
env = "prod"
print(f"Deploying to {env.upper()}") # Deploying to PROD

name = "web-01"
print(f"{name} has {len(name)} chars") # web-01 has 6 chars


#### 9. Combining input() with string methods ####
host = input("Enter hostname: ").strip()
print(f"You typed: {host}")

##### TASK 4.
#1. ask the user: Enter hostname: , and clean the input with .strip().
#2. print it in UPPERCASE
#3. print its length , with a label , eg. Length: 11
#4. Print a line of - exactly as long as the hostnames


hostname = input("Enter hostname: ").strip()
result = hostname.upper()
print(result)

d = len(result)
print(f"Length: {d}")
print("-" * d)






 