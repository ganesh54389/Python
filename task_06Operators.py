# -------------arithmetic operator---------------------------------------------
# additions operations 
num_1=int(input("enter the number01:"))
num_2=int(input("enter the number02:"))
results=num_1+num_2
print(f"number01 is {num_1} and number02 is {num_2} performed addition then the results is {results}")
#substarction operator
number_01=int(input("enter the number01:"))
number_02=int(input("enter the number02:"))
results_s=number_01-number_02
print(f"number01 is {number_01} and number02 is {number_02} performed substraction then the results is {results_s}")
 #multiplication operatoion
numm_01=int(input("enter the number01:"))
numm_02=int(input("enter the number02:"))
results_m=numm_01*numm_02
print(f"number01 is {numm_01} and number02 is {numm_02} performed multiplication operations then the result is {results_m}")
#divison operations
nummm_1=int(input("enter the number01:"))
nummm_2=int(input("enter the number02:"))
results_d=nummm_1/nummm_2
floor_divison=nummm_1//nummm_2
modulo_div=nummm_1%nummm_2
print(f"number01 is {nummm_1} and number02 is {nummm_2} perform divisons operations then the results is {results_d}")
print(f"number01 is {nummm_1} and number02 is {nummm_2} perform floor divisons operations then the results is {floor_divison}")
print(f"number01 is {nummm_1} and number02 is {nummm_2} perform floor divisons operations then the results is {modulo_div}")
#exponentiation operator
number01=int(input("enter the number 01:"))
number02=int(input("enter the number 02:"))
exp=number01**number02
print(f"number 01 is {number01} and number 02 is {number02} perform exponentation operation then the results is {exp}")
# --------------------------------assignment operators -------------------------------
f_number=int(input("enter the number:"))
f_number+=20 
print(f_number)
# --------------------comparison opearators--------------------------------------
one_value=int(input("enter the number :"))
second_value=int(input("emter the number :"))
print(one_value==second_value)
print(one_value!=second_value)
print(one_value>second_value)
print(one_value<second_value)
print(one_value<=second_value)
print(one_value>=second_value)
# ----------------------logical operator ---------------------------------------
one_bool_value=6
print(one_bool_value>3 and one_bool_value<10)
print(one_bool_value>10 or one_bool_value>2)
print(not(one_bool_value>10 or one_bool_value>2))
#-----------------identity opearators----------------------------------------
list_1=[1,2,3,4]
list_2=[1,2,3,4]
print(list_1 is list_2)
print(list_1 is list_1)
print(list_2 is not list_1)
#----------------------membership operators -------------------------------------
list_01=["apples","grapse","mango"]
print("strawberry" in list_01)
print("strawberry" not in list_01)
print("apples" in list_01)
#----------------------output formatting------------------------------------------
name="ganesh"
age=21
print(f"name {name}, the age is {age} so he is eligible to vote ") 


