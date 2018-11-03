#CALLING STATIC METHOD INSIDE CLASS METHOD USING "cls"

class Employee:

    @staticmethod
    def show():
        print("I am Static Method")

    @classmethod
    def display(cls):
        print("I am Class Method")
        #calling static method using "cls"
        cls.show()

#calling class method
Employee.display()
