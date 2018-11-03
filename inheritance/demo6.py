class A:
    def m1(self):
        print("M1 of class A")

class B(A):
    def m2(self):
        print("M2 of class B")

class C(B):
    def m3(self):
        print("M3 of class C")

#calling class A method
a1 = A()
a1.m1()
print("--------------------------")

#calling class B method
b1 = B()
b1.m2()
b1.m1()
print("--------------------------")


#calling class C method
c1 = C()
c1.m3()
c1.m1()
c1.m2()
