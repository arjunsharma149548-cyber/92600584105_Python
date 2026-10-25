#Q6.Write a program to demonstrate method overriding and polymorphism.
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")


d = Dog()
c = Cat()

d.sound()
c.sound()