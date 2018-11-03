class Employee:
    def __init__(self):
        self.idno = 101
        self.name = "Ravi"
    def display(self):
        print(self.idno)
        print(self.name)

class Student:
    def __init__(self,id,na):
        self.idno = id
        self.name = na
    def display(self):
        print(self.idno)
        print(self.name)

e1 = Employee()
e1.display()
print("--------------------------------------")
e2 = Student("120301ElR016","Pratyush")
e2.display()