#----------------------------for loop-------------------------------------------------
for i in ["ganesh","ravi","vasu","gopal","harish"]:
    print(i)
#another example
fruits=["apple","banana","cherry"]
for i in fruits:
    print("hi")
    print(f"{fruits} stock recived")  
# example 
employee_data=["ganesh","kumar","ram"]
for i in employee_data:
    print(f"{i} salary 5% hike given ")
# range function 
for i  in range(10):
    print(i)
for i in range (2,21):
    print(i)    
for i in range(2,30,2):
    print(i)
table=int(input("enter the table number:"))
for i in range(1,21):
    print(f"{table} X {i} = {table*i}")

#-----------------------nested for loop---------------------------
for i in range(5):
    for j in range(5):
        print(i,j)
for i  in range(1,11):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")
    print("-"*10)
#----------------------------------while loop-------------------------------------
age=18
while age==18:
    print("eligible to vote ")
    break
#----------------------nested while loop --------------------------------------------
age=35
while age>=35:
    print("this is outer loop ")
    while age>=35:
        print("this is inner  loop")
        break
    break





    