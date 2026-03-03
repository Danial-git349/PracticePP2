import re

pattern = r'^a.*b$'

# Test strings
test_strings = [
    "ab",
    "acb",
    "a123b",
    "a_b",
    "aXYZb",
    "aX",
    "baab",
    "b"
]

for string in test_strings:
    if re.match(pattern, string):
        print(f"'{string}' matches")
    else:
        print(f"'{string}' does not match")