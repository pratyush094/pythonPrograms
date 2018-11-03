#STATIC METHOD

class Employee:
    comp_name = "Sathya"
    comp_cno = 7537975721
    @staticmethod
    def displayCompanyInfo():
        print(Employee.comp_name)
        print(Employee.comp_cno)

Employee.displayCompanyInfo()