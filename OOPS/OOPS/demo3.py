#INSTANCE VARIABLE PROGRAM to hold same values for both objects

class Employee:
    def assign(self):
        self.idno = 101
        self.name = "PRATYUSH"
    def display(self):
        print(self.idno)
        print(self.name)

print("\nEMPLOYEE 1")
e1 = Employee()
#e1.display()
e1.assign()
e1.display()

print("\nEMPLOYEE 2")
e2 = Employee()
e2.assign()
e2.display()
