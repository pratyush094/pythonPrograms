#METHOD OVERLOADING

class Employee:
    def assign(self,id="Not Assigned",name="No Name",sal="No Salary"):
        self.idno = id
        self.name = name
        self.salary = sal
    def display(self):
        print("IDNO =",self.idno)
        print("NAME =",self.name)
        print("SALARY   =",self.salary)

#without any parameters
e1 = Employee()
e1.assign()
e1.display()

print("--------------------------")

#with 1 parameter
e2 = Employee()
e2.assign(101)
e2.display()

print("--------------------------")

#with all parameters
e3 = Employee()
e3.assign(name="PRATYUSH",id=101,sal=1250000.00)
e3.display()