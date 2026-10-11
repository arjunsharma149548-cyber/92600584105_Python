#8.	Write a program to demonstrate basic regular expression pattern matching. 

import re

text = "My name is Arjun and my phone number is 9876543210."

# Search for a word
result = re.search("Arjun", text)

if result:
    print("Word found:", result.group())
else:
    print("Word not found.")

# Find all digits
digits = re.findall(r"\d", text)
print("Digits:", digits)

# Check whether the text starts with a word
result = re.match("My", text)

if result:
    print("Text starts with:", result.group())
else:
    print("No match at the beginning.")
