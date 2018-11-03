#CLASS METHOD

class Employee:
    comp_name = "Sathya"    #static variable
    @classmethod
    def display(cls):
        print("CLASS METHOD")
        print(cls)
        print(cls.comp_name)    #calling static variable using cls

Employee.display()  #calling class method