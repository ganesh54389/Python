#sum of squares 
sum=0
for i in range(1,6):
    square=i*i
    sum=sum+square
print(sum)
# countdown 
count=6
while count>0:
    print(count)
    count-=1
#user specified multiplication table by using nested for loop
table_number=int(input("enter the table number:"))
for i in range(table_number):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")
    print("-"*10)
# sum of all even numbers
sum=0
for i in range(0,11,2):
    sum+=i
print(sum)
#sum of all numbers from 1 to given number
given_number=int(input("enter the number:"))
sum=0
for i in range(1,given_number+1):
    sum+=i
print(sum)
#display numbers from list using  loop
list_01=["24","36","45","55","22"]
for i in list_01:
    print(i)
#displaty numbers from -10 to -1 using loops 
for i in range(-10,0):
    print(i)

