#Write a program to illustrate the use of different data types and type casting.

student_name = "Arjun"
roll_no = 92600584105
age = 22
height = 5.7
is_student = True

print("Student Name:",student_name,"Type:",type(student_name))
print("Age:",age,"Type:",type(age))
print("Height:",height,"Type:",type(height))
print("IS student:",is_student,"Type:",type(is_student))

num1 = "44"
num2 = int(num1)
num3 = float(num2)
num4 = str(num3)

print("String to integer:",num2)
print("Integer to flost:",num3)
print("Integer to string:",num4)