#6.	Write a program to perform file and directory operations using os and sys modules.
import os
import sys

# Display the current working directory
print("Current Directory:", os.getcwd())

# Create a new directory
folder = "MyFolder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Directory created successfully.")
else:
    print("Directory already exists.")

# Create a file inside the directory
file_path = os.path.join(folder, "sample.txt")

with open(file_path, "w") as file:
    file.write("Hello, Python!")

print("File created successfully.")

# Display files and directories
print("Directory Contents:", os.listdir("."))

# Display Python version
print("Python Version:", sys.version)

# Display command-line arguments
print("Command-Line Arguments:", sys.argv)
