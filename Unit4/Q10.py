#Q10.Write a program to perform file pointer operations using seek and tell methods.
# Create and write data into a file
f = open("demo.txt", "w+")
f.write("Hello Python Programming")

# tell() returns the current file pointer position
print("Position after writing:", f.tell())

# seek() moves the file pointer
f.seek(0)
print("Position after seek(0):", f.tell())

# Read first 5 characters
print("Data:", f.read(5))
print("Position after reading:", f.tell())

# Move pointer to position 6
f.seek(6)
print("Position after seek(6):", f.tell())

# Read remaining data
print("Remaining data:", f.read())

f.close()
