# #---------------------function defination------------------------------
def greet():
    print("hello welcome to python life ")
greet()    
def add():
    num1=10
    num2=20
    result=num1+num2
    print(result)
add()  
def details(user,id):
    print(f"{user}\t{id}")
details("ganesh",24)  
details("charan",1234)
details(["vasu","kumar"],1223)  
#-------------------parameters and arguments----------------
def mul(x,y):
    print(x*y)
mul(4,4)    
def add(a,b):
    print(a+b)
add(4040,1010) 
# ---------------------retun statement---------------------
def add(x,y):
    return x+y
obj=add(2222,1111)  
print(obj+789+89) 
#----------------------default parameters-------------------
def details(user=None,age=None,id=None):
    print(f"{user}\t{age}\t{id}")
details("charan",24,1234)
details("ganesh",22)
details("ram")    
details()
#------------------------arbitary argument------------------
def myfun(*a):#return tuple formart
    print(a)
myfun(1,"vasu","kumar")   
#-------------------------keyword argumrnt ---------------------
def myfun(**a):
    print(a)
myfun(a=1,b=2,c=3) 
#---------module-----------------
from math import *
print(sqrt(16))
print(pi)
print(pow(3,2))
import random
print(random.randint(1,10))
print(random.choice(["apple","banana","orange"]))
from datetime import datetime
now=datetime.now()
# print(now)
import os
print(os.getcwd())




  