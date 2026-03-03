import re

pattern = r'^[A-Z][a-z]+$'

# Test strings
test_strings = [
    "Hello",
    "Python",
    "hello",
    "HELLO",
    "H",
    "HeLlo",
    "World"
]

for string in test_strings:
    if re.match(pattern, string):
        print(f"'{string}' matches")
    else:
        print(f"'{string}' does not match")