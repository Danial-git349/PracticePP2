import re

line = "From: user@gmail.com"

if re.search("From:", line):
    print("Found")

import re

text = "My numbers are 19 and 42"
numbers = re.findall('[0-9]+', text)

print(numbers)


x = "From: Using the : character"
y = re.findall('^F.+:', x)
print(y)

y = re.findall('^F.+?:', x)

x = "From stephen@uct.ac.za Sat Jan 5"

