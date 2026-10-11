#10.Write a program to extract specific information from a text file using regular expressions


import re

# Create a text file
with open("data.txt", "w") as file:
    file.write("Name: Arjun\n")
    file.write("Phone: 9876543210\n")
    file.write("Email: arjun@gmail.com\n")

# Read the text file
with open("data.txt", "r") as file:
    text = file.read()

# Extract name
name = re.search(r"Name:\s*(.*)", text)

# Extract phone number
phone = re.search(r"Phone:\s*(\d{10})", text)

# Extract email
email = re.search(r"Email:\s*([\w.-]+@[\w.-]+\.\w+)", text)

# Display extracted information
print("Name:", name.group(1) if name else "Not found")
print("Phone:", phone.group(1) if phone else "Not found")
print("Email:", email.group(1) if email else "Not found")
