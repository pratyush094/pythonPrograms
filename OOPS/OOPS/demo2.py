#STATIC VARIABLE PROGRAM

class Employee:
    comp_name = "Sathya"
    comp_cno = 7537975721
    def display(self):
        print("Employee Details")
        print(Employee.comp_name)
        print(Employee.comp_cno)

print("\nEMPLOYEE 1")

e1 = Employee()
e1.display()

#CALLING WITH CLASS NAME
print(Employee.comp_name)
print(Employee.comp_cno)

#CALLING WITH REFERENCE VARIABLE
print(e1.comp_name)
print(e1.comp_cno)

print("\nEMPLOYEE 2")

e2 = Employee()
e2.display()

#CALLING WITH CLASS NAME
print(Employee.comp_name)
print(Employee.comp_cno)

#CALLING WITH REFERENCE VARIABLE
print(e2.comp_name)
print(e2.comp_cno)
