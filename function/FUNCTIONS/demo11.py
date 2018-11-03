a = 10

def sample():
    print("I am Sample")
    print(a)
    print("BYE")

def show():
    print("I am Show")
    print("Hi")

#Using Global Variable
from FUNCTIONS.demo11 import a
print(a)

#Using Function
from FUNCTIONS.demo11 import sample
sample()
