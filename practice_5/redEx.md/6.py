import re

text = "Python is great, and powerful. It is easy to learn."

# Replace space, comma, or dot with colon
result = re.sub(r'[ ,.]', ':', text)

print("Original string:")
print(text)

print("\nModified string:")
print(result)