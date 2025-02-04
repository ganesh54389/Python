#----------------------task01:-square of numbers----------------------------
print(list(map(lambda numbers:numbers**2,[2,4,6,8,10,12,14])))
#---------------------task02:filter positinumbers----------------------
print(list(filter(lambda numbers:numbers>0,[1,-1,2,-3,4,-5])))
#--------------------task03:caluculate factorial of n----------------
from functools import reduce
n=int(input("enter your number:"))
print(reduce(lambda x,y:x*y,range(1,n+1)))





    

