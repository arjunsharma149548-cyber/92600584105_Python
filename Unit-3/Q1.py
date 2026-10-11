#write a program to create and import a user define module.

import mainQ1

student=mainQ1.greeting("Arjun")
print(student)

import mainQ1

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

addition=mainQ1.add(a,b)
print("Addition:",addition)