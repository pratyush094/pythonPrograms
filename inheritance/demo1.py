class A:
    @staticmethod
    def show():
        print("A class static method")
class B(A):
    def display(self):
        print("B class instance method")

#calling static method
A.show()

#calling static method using class B
B.show()
