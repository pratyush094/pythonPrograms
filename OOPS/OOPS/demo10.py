class Employee:
    def __init__(self,id,na):
        self.idno = id
        self.name = na
    def display(self):
        print(self.idno)
        print(self.name)
    def __init_subclass__(Employee,sal,comp_name):
        self.salary = sal
        self.company = comp_name
    def show(self):
        print(self.salary)
        print(self.company)
e1 = Employee(101,"ravi")
e1.display()
e2 = Employee(125000.00,"TechM")
e2.show()
