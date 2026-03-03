import re

pattern = r"^ab*$"

# Test strings
test_strings = ["a", "ab", "abb", "abbb", "b", "aa", "ba", "aab"]

for string in test_strings:
    if re.match(pattern, string):
        print(f"'{string}' matches")
    else:
        print(f"'{string}' does not match")