from pymongo import MongoClient
mc = MongoClient()
sa = mc.Sathya
d1 = {"id":101,"name":"Ravi","fees":12500.00}
sa.Student.insert(d1)
print("Data Inserted")
