class A:
    def __init__(self):
        print("Default constructor of class A")

class B(A):
    def show(self):
        print("Show of class B")

b1 = B()
b1.show()
