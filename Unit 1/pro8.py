# Write a program to explain mutable and immutable objects in Python.

# Immutable Object - String
name = "Arjun Sharma"

print("Original String :", name)

name = name + " Python"
print("After Modification :", name)

# Mutable Object - List
student = ["Arjun Sharma", 21, "Python"]

print("Original List :", student)

student[1] = 22
print("After Modification :", student)