#USING MAP FUNCTION IN LAMBDA

l1 = [10,20,30,40,50]
l2 = [1,2,3,4,5]
val = list(map((lambda x,y:x+y),l1,l2))
print(val)
