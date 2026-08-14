# Write a program to define and use user-defined functions
# with different types of arguments.

# 1. Positional Arguments
def add(a, b):
    print("Addition :", a + b)

add(10, 20)


# 2. Keyword Arguments
def student(name, age):
    print("Name :", name)
    print("Age :", age)

student(age=22, name="Arjun Sharma")


# 3. Default Arguments
def greet(name="Arjun Sharma"):
    print("Hello", name)

greet()


# 4. Variable Length Arguments
def total(*numbers):
    print("Total :", sum(numbers))

total(10, 20, 30, 40)