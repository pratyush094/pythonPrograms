#print max marks with student no using map function

s1 = [85,84,78,68,80,95]
s2 = [45,57,87,35,58,64]
l = list(map((lambda x,y:"1st Student"+str(x)if x>y else "2nd Student"+str(y)),s1,s2))
print(l)