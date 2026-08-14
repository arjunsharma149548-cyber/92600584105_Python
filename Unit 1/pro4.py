# Write a program to demonstrate string operations including
# slicing, formatting and built-in string functions.

name = "Python Programming"

# String Operations
print("String :", name)
print("Length :", len(name))
print("First Character :", name[0])
print("Last Character :", name[-1])

# String Slicing
print("Slicing :", name[0:6])
print("Reverse :", name[::-1])

# String Formatting
age = 21
print("My name is {} and my age is {}".format(name, age))

# Built-in String Functions
print("Uppercase :", name.upper())
print("Lowercase :", name.lower())
print("Replace :", name.replace("Python", "Java"))
print("Count :", name.count("m"))
print("Find :", name.find("Programming"))

