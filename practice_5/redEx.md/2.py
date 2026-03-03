import re

pattern = r"^ab{2,3}$"

# Test strings
test_strings = ["ab", "abb", "abbb", "abbbb", "a", "b", "aabbb"]

for string in test_strings:
    if re.match(pattern, string):
        print(f"'{string}' matches")
    else:
        print(f"'{string}' does not match")