class A:
    def __init__(self):
        print("Constructor of A")
    def __del__(self):
        print("Destructor of A")

class B(A):
    def show(self):
        print("Show of A")

b1 = B()
b1.show()
