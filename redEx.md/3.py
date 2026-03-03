import re

pattern = r'^[a-z]+_[a-z]+$'

# Test strings
test_strings = [
    "hello_world",
    "python_program",
    "Hello_world",
    "hello_World",
    "helloWorld",
    "hello__world",
    "hello_world_test"
]

for string in test_strings:
    if re.match(pattern, string):
        print(f"'{string}' matches")
    else:
        print(f"'{string}' does not match")