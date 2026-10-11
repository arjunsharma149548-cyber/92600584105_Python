#9.	Write a program to use re module functions such as match search and findall.

import re

text = "Python is easy. Python is powerful. My marks are 85."

# 1. Using match()
result1 = re.match("Python", text)
print("Match:", result1.group() if result1 else "Not found")

# 2. Using search()
result2 = re.search("easy", text)
print("Search:", result2.group() if result2 else "Not found")

# 3. Using findall()
result3 = re.findall("Python", text)
print("Findall:", result3)

# Find all digits
digits = re.findall(r"\d+", text)
print("Digits:", digits)
