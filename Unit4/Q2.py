#Q2.Write a program to demonstrate constructor and destructor usage. 

class student:
    def __init__(self):
        print("constructor is called")

    def __del__(self):
        print("destructor is called")

s1=student()

del s1