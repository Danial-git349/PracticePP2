import re

def split_at_uppercase(s):
    # Split before each uppercase letter
    return re.split(r'(?=[A-Z])', s)

# Test examples
test_strings = [
    "HelloWorld",
    "PythonProgrammingLanguage",
    "SplitAtUpperCase",
    "CamelCaseExample"
]

for s in test_strings:
    print(f"{s} -> {split_at_uppercase(s)}")