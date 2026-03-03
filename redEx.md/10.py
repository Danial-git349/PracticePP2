import re

def camel_to_snake(camel_str):
    # Insert underscore before uppercase letters (except the first) and convert to lowercase
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_str

# Test examples
test_strings = [
    "CamelCaseExample",
    "PythonProgrammingLanguage",
    "HelloWorld",
    "ConvertCamelToSnake"
]

for s in test_strings:
    print(f"{s} -> {camel_to_snake(s)}")