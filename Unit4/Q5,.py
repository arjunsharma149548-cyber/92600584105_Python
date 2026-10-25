#Q5.Write a program to implement single multilevel and multiple inheritance.
#single inheratance
class A:
    def show(self):
        print("This is class A")

class B(A):
    pass

obj = B()
obj.show()

#multilevel inheratance
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(B):
    pass

obj = C()
obj.showA()
obj.showB()

#multiple inhetratance 
class A:
    def showA(self):
        print("Class A")

class B:
    def showB(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.showA()
obj.showB()