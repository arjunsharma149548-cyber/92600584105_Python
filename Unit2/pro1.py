# Demonstrate if, if-else and if-elif-else

num = int(input("Enter a number: "))

# 1. if statement
if num > 0:
    print("Number is Positive")


# 2. if-else statement
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


# 3. if-elif-else statement
if num > 0:
    print("Number is greater than Zero")
elif num < 0:
    print("Number is less than Zero")
else:
    print("Number is Zero")