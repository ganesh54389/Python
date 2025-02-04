#----------------fstring for username and their age ------------------------------------
username=input("enter the user name :")
age=int(input("enter the age of user name:"))
print(f"welcome to {username},the age is {age}")
#product name display in a readble format 
my_dict={
    "name_of_the_product":"vivo v25 pro ",
    "price":"20000",
    "quantity":"5"
}
print(my_dict)
print(f"product details" )
print(f"name of the product is {my_dict['name_of_the_product']}, their price {my_dict['price']} and quantity is {my_dict['quantity']}")
#create a list "numbers" contain 1to 10 and check the values present or not 
numbers=[1,2,3,4,5,6,7,8,9,10]
print(5 in numbers)
print(15 not in numbers)
# to caluculate area of rectangle 
length=int(input("enter the length of rectangles:"))
width=int(input("enter the width of rectangles:"))
area=length*width
print(f"the length of rectangle is {length} and the width of rectangle is {width},the the area of rectangle is {area}")
#increamenting and decrementing 
varible01=40
varible01+=1
print(varible01)
varible02=20
varible02-=1
print(varible02)
#--------celsius to fahrenheit----------------------
celsius=int(input("enter the celsius value:"))
fahrenheit=(celsius*(9/5))+32
print(f"celsius after conversion fahrenheit,the temparture in fahrenheit is {fahrenheit}")
#caluculating simple intrest formula 
principal=int(input("enter the principal value :"))
rate_of_int=int(input("enter the rate of intrest value:"))
time=int(input("emter the time :"))
simple_intrest=(principal*rate_of_int*time)/100
print(f"the principal is {principal},the rate of intrest is {rate_of_int},and the time is {time} then the simple intrest is {simple_intrest}")
#concatenation 
msg_01=input("enter the string value:")
msg_02=input("enter the string vale :")
conc=msg_01+msg_02
print(conc)
#kilometers to miles 
number_of_kilometers=int(input("enter the kilometers:"))
number_of_miles=(number_of_kilometers)/1.609344
print(f"number of kilometers is {number_of_kilometers} is converted into miles is{number_of_miles}")
