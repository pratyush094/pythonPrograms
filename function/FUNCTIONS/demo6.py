def add():
    sub()
    print("I am Add")
def mul():
    sub()
    print("I am Mul")
def sub():
    print("I am Sub")
def div():
    print("I am Div")
    add()
    mul()
print("CALC EXAMPLE")
mul()
sub()
add()
