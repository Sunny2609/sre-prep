server = "db-01"
used_gb = 333
total_gb = 500

usage_percentage = (used_gb)/(total_gb) * 100
print(f"{usage_percentage:.1f}")

print(f"{server} disk: {usage_percentage:.1f}% used")