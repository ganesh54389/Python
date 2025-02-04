#--------------------vowel checker----------------------------------------------------
charcter=input("enter the charcter:")
vowels=["a","e","i","o","u","A","E","I","O","U"]
if charcter in vowels:
    print("entered charcter is vowel ")
else:
    print("entered charcater is consonents ")    
#-----------------------age classification -----------------------------------
age=int(input("enter the age of a person:"))
if age<=12:
    print("your child ")
elif age>=13 and age<=17:
    print("your teenagers ")
elif age>=18 and age <=64:
    print("your adult ")
else:
    print("yopur senior ")
#----------------------number classifiear -----------------------------------------
number=int(input("ente the number:"))
if number>0:
    print("positive number" )
elif number<0:
    print("negative numbers ")
else:
    print("zero")    
# ----------------------leap year progrm----------------------------------
year=int(input("enter the year:"))
if year%4==0:
    print("leap year")
else:
    print("not a leap year")       
#----------------------caluculator------------------------------------------
number_01=int(input("enter the number :"))
number_02=int(input("enter the number :"))
addition=number_01+number_02
print(f"addition operations:{addition}")
addition=number_01-number_02
print(f"addition operations:{addition}")
addition=number_01*number_02
print(f"addition operations:{addition}")
addition=number_01/number_02
print(f"addition operations:{addition}")
#----------------shorthand if statement-------------------------------------------
x=8
print(f"result is even")if x%2==0 else print(f"result is odd")
#--------------------discount percentage--------------------------------------------
original_price=float(input("enter the price:"))
discount=float(input("enter the discount:"))
cal_dis=original_price*(discount/100)
print(cal_dis)
original_price-=cal_dis
print(original_price)
#---------------------------------------BMI caluculator --------------------------------
weight=float(input("enter the weight:"))
height=float(input("enter the height:"))
body_mass_index=weight/(height**2)
print(body_mass_index)

