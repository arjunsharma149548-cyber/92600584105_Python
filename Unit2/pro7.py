#Write a program to demonstrate list dictionary and set comprehensions.

# List Comprehension
numbers = [1, 2, 3, 4, 5]
square = [x * x for x in numbers]
print("List:", square)


# Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
square_dict = {x: x * x for x in numbers}
print("Dictionary:", square_dict)


# Set Comprehension
numbers = [1, 2, 3, 4, 5]
square_set = {x * x for x in numbers}
print("Set:", square_set)