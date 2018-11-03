#STATIC AND INSTANCE VARIABLE

class Employee():
    comp_name = "Sathya"
    comp_cno = 7537975721
    def assign(self,id,name):
        self.idno = id
        self.name = name
    def display(self):
        print(Employee.comp_name)
        print(Employee.comp_cno)
        print(self.idno)
        print(self.name)

print("\nEMPLOYEE 1")
e1 = Employee()
e1.assign(101,"Pratyush")
e1.display()

print("\nEMPLOYEE 2")
e2 = Employee()
e2.assign(102,"Kumar")
e2.display()

print("\nEMPLOYEE 3")
e3 = Employee()
e3.assign(103,"Parija")
e3.display()