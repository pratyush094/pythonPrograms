#WITH DEFAULT VALUES

ref = lambda id=0,na=None,sal=0.0:print("Idno: ",id,"\nName: ",na,"\nSal: ",sal)
ref()   #zero argument
print("------------------------")
ref(na="Pratyush")  #with 1 argument
print("------------------------")
ref(id=101,sal=2850000.0)   #with 2 arguments
print("------------------------")
ref(na="Parija",id=103,sal=285000.0)    #with 3 arguments