#----------------------defining dictonary---------------------------
sample={ }
print(type(sample))

sample_01={
    1:1234,
    2:4536,
    3:7891
}
print(type(sample_01))

sample_2= dict()    #by using dictonary class
print(type(sample_2))
#---------------------dictonary methods-----------------------------
dictonary_01={
    "user01":"user1001",
    "user02":"user1002",
    "user03":"user1003",
    "user04":"user1004"
}
print(dictonary_01)
dictonary_01.clear()
print(dictonary_01)
dictonary_01={
    "user01":"user1001",
    "user02":"user1002",
    "user03":"user1003",
    "user04":"user1004"
}
sample_1=dictonary_01.copy()
print(sample_1)
sample_1.clear()
print(sample_1)
print(dictonary_01)
dictonary_01={
    "user01":"user1001",
    "user02":"user1002",
    "user03":"user1003",
    "user04":"user1004"
}
print(dictonary_01.get("user01"))
print(dictonary_01.get("user02"))
print(dictonary_01.get("user03"))
print("square bracket notation")
print(dictonary_01["user01"])
dictonary_01.pop("user01")
print(dictonary_01)
print(dictonary_01.keys())
print(dictonary_01.values())
print(dictonary_01.items())
dictonary_01={
    "user01":"user1001",
    "user02":"user1002",
    "user03":"user1003",
    "user04":"user1004"
}
emp_id= {"emp01":2121,"emp02":3214}
dictonary_01.update(emp_id)
print(dictonary_01)
dictonary_01={
    "user01":"user1001",
    "user02":"user1002",
    "user03":"user1003",
    "user04":"user1004"
}
print(dictonary_01["user02"])
dictonary_01["user05"]="vasukumar"
print(dictonary_01)
sample={

}
sample[1]="vasu"
print(sample)
