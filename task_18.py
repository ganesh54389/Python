#---------------------------nested list -----------------------------
list_1=[[1,2,3],[4,5,6],[7,8,9]]
print(list_1[0][1])
print(list_1[0][2])
print(list_1[0][0])
print("accesing second list")
print(list_1[1][0])
print(list_1[1][1])
print(list_1[1][2])
print("accessing third list:")
print(list_1[2][0])
print(list_1[2][1])
print(list_1[2][2])
#------------------------------list comprehension--------------
fruits=["apple","mango","banana","cherry","kiwi"]
new_list=[]
for i in fruits:
    if "a" in i:
        new_list.append(i)
print(new_list)    
#code compression by using list comprehension
fruits=["apple","mango","banana","cherry","kiwi"]
new_list=[i for i in fruits if "a" in i]
print(new_list)
#--------------------single line compression -------------------
fruits=["apple","mango","banana","cherry","kiwi"]
print([i for i in fruits if "a" in i])
    