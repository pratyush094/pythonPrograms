#USING MAP FUNCTION DISPLAY HIGHEST MARKS INTO LIST

s1 = [85,84,78,68,80,95]
s2 = [45,57,87,35,58,64]
max = list(map((lambda x,y:x if x>y else y),s1,s2))
print(max)
