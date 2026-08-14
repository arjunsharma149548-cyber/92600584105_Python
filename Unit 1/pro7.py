# Write a program to create a dictionary and demonstrate
# dictionary methods and iteration.

student = {
    "name": "Arjun Sharma",
    "age": 22,
    "course": "Python",
    "marks": 85
}

print("Dictionary :", student)

# Dictionary Methods
print("Keys :", student.keys())
print("Values :", student.values())
print("Items :", student.items())
print("Name :", student.get("name"))

# Add and Update
student["city"] = "Bihar"
student["marks"] = 90

print("After Adding and Updating :", student)

# Delete
student.pop("age")
print("After Removing Age :", student)

# Iteration
print("Dictionary Elements:")

for key, value in student.items():
    print(key, ":", value)

