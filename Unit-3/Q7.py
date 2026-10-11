#7.	Write a program to copy move and delete files using shutil module. 


import shutil
import os

# Create a sample file
with open("sample.txt", "w") as file:
    file.write("Hello, Python!")

# 1. Copy the file
shutil.copy("sample.txt", "copy.txt")
print("File copied successfully.")

# 2. Move the file
shutil.move("copy.txt", "moved.txt")
print("File moved successfully.")

# 3. Delete the file
if os.path.exists("moved.txt"):
    os.remove("moved.txt")
    print("File deleted successfully.")
