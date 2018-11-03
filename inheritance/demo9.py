#SINGLE INHERITANCE

class A:
    def display(self):
        print("I am Display")

class B(A):
    def show(self):
        print("I am Show")

a1 = A()
a1.display()
#a1.show >>> ERROR

b1 = B()
b1.show()
b1.display()