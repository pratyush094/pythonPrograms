name = input("Enter Employee Name: ")
desig = input("Enter Designation,m/a/c: ")
salary = float(input("Enter Salary: "))

if desig=='m' or desig=='M':
    bonus = 0.20*salary
    total_sal = salary + bonus


elif desig=='a' or desig=='A':
    bonus = 0.10*salary
    total_sal = salary + bonus

elif desig=='c' or desig=='C':
    bonus = 0.05*salary
    total_sal = salary + bonus

else:
    print("No Bonus")
    print(salary)

print("Bonus: ",bonus)
print("Total Salary: ",total_sal)
