a = 1000
def fun1():
    global a
    a = 50
    print("GLOBAL VARIABLE  ")
    print(a)
print(a)
fun1()
print(a)
