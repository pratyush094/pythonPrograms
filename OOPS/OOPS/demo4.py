#INSTANCE VARIABLE to hold different values for every object

class Employee:
    def assign(self,id,name):
        self.idno = id
        self.name = name
    def display(self):
        print(self.idno)
        print(self.name)

print("\nEMPLOYEE 1")
e1 = Employee()
e1.assign(101,"Pratyush")
e1.display()

print("\nEMPLOYEE 2")
e2 = Employee()
e2.assign(102,"Parija")
e2.display()