# Write a program to create and manipulate lists
# using indexing, slicing and list comprehensions.

# Creating a list
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

# Indexing
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Slicing
print("Slicing:", numbers[1:4])
print("First Three Elements:", numbers[:3])

# Manipulating List
numbers.append(60)
print("After Append:", numbers)

numbers.remove(20)
print("After Remove:", numbers)

# List Comprehension
squares = [x * x for x in numbers]
print("Squares:", squares)