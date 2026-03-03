import re

def insert_spaces(text):
    # Insert space before each uppercase letter (except the first one)
    result = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    return result

# Test examples
test_strings = [
    "HelloWorld",
    "PythonProgrammingLanguage",
    "CamelCaseExample",
    "SplitAtUpperCase"
]

for s in test_strings:
    print(f"{s} -> {insert_spaces(s)}")