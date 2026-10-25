#Q4.Write a program to demonstrate instance methods class methods and static methods.
class Student:
    college = "Marwadi University"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Instance method
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    # Class method
    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    # Static method
    @staticmethod
    def welcome():
        print("Welcome to the Student Management System!")


# Creating an object
s1 = Student("Arjun", 85)

# Calling methods
s1.display()
Student.show_college()
Student.welcome()
