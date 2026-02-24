# Code #4: Date Examples

from datetime import datetime

print("=== Date Examples ===")

# Example 1: Current date and time
now = datetime.now()
print("Example 1 - Current date & time:", now)

# Example 2: Format date
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Example 2 - Formatted date:", formatted)

# Example 3: Specific date
birthday = datetime(2008, 5, 14)
print("Example 3 - Birthday:", birthday)

# Example 4: Date difference
date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 1, 10)
difference = date2 - date1
print("Example 4 - Difference in days:", difference.days)