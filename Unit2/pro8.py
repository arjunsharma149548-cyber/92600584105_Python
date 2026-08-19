# Write a program to illustrate variable scope using local global and nonlocal variables.

# Global variable
x = 10

def outer():
    # Nonlocal variable
    y = 20

    def inner():
        # Local variable
        z = 30

        print("Global:", x)
        print("Nonlocal:", y)
        print("Local:", z)

    inner()

outer()