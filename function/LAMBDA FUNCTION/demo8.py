#READ 3 NOS AND PRINT THE BIGGEST AMONG THE 3

res = lambda no1,no2,no3:no1 if no1>no2 and no1>no3 else no2 if no2>no1 and no2>no3 else no3
a = int(input("Enter no1:   "))
b = int(input("Enter no2:   "))
c = int(input("Enter no3:   "))
print("BIGGEST: ",res(a,b,c))
