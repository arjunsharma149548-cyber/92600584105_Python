# Write a program to illustrate the use of tuples and sets
# with basic operations.

# Tuple
numbers = (10, 20, 30, 40, 50)

print("Tuple :", numbers)
print("First Element :", numbers[0])
print("Last Element :", numbers[-1])
print("Length of Tuple :", len(numbers))

# Tuple Operations
print("Count of 20 :", numbers.count(20))
print("Index of 30 :", numbers.index(30))

# Set
myset = {10, 20, 30, 40}

print("Set :", myset)

# Set Operations
myset.add(50)
print("After Adding :", myset)

myset.remove(20)
print("After Removing :", myset)

set2 = {30, 40, 50, 60}

print("Union :", myset.union(set2))
print("Intersection :", myset.intersection(set2))

