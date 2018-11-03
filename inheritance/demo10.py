#SINGLE INHERITANCE USING STATIC VARIABLES

class A:
    comp_name = "SATHYA"
    def display(self):
        print("This is Display")

class B(A):
    def show(self):
        print("This is Show")

print("class A  :",A.comp_name)
print("class B  :",B.comp_name)
a1 = A()
a1.display()

b1 = B()
b1.show()
b1.display()
