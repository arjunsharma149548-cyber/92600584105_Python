#Write a program to generate a sequence of numbers using generator functions and yield keyword.

def numbers():
    for i in range(1, 6):
        yield i

for num in numbers():
    print(num)