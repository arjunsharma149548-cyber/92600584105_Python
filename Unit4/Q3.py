#Q3.Write a program to illustrate instance variables and class variables
class Student:
    # Class variable
    college = "Marwadi University"

    def __init__(self, name, marks):
        # Instance variables
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("College:", self.college)


# Creating objects
s1 = Student("Arjun", 85)
s2 = Student("Rahul", 90)

# Displaying student details
s1.display()
print("-----------")
s2.display()
