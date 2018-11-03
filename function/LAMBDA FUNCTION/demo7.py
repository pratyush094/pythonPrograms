#USING CONDITIONAL CONTROL STATEMENTS (IF ELSE) IN LAMBDA FUNCTION
#HIGHEST NUMBER BETWEEN 2 NOS

ref = lambda no1,no2:no1 if no1>no2 else no2
a = int(input("Enter no1: "))
b = int(input("Enter no2: "))
print("Ans: ",ref(a,b))
