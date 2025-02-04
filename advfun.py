# #--------------------------labda function-----------------------------------
def add(a,b):#addition
    return a+b
obj=add(10,10)
print(obj)
result=lambda a,b:a+b
print(result(10,10))
def sub(a,b):#another example
    return a-b
obj=sub(20,10)
print(obj)
result=lambda a,b:a-b
print(result(20,1))
print(result(5,3))
print(result(15,10))

# #--------------filter function-----------------------------------------
list_1=[1,2,3,4,5]
def even(a):
    return a%2==0
obj=filter(even,list_1)
print(list(obj))
 
result=filter(lambda a:a%2==0,list_1)
print(list(result))# explicit converstion is mandatory 
  
print(list(filter(lambda a:a%2==0,[1,2,3,4,5])))

#-----------------------------map function ------------------------------
list_1=[1,2,3,4,5,6,7,8,9]
def square(i):
    return i**2
obj=map(square,list_1)
print(list(obj))

result=map(lambda i:i**2,[1,2,3,4,5,6,7,8,9] )
print(list(result))

print(list(map(lambda i:i**2,[1,2,3,4,5,6,7,8,9] )))
#map function multiple iterables
def myfunc(a, b):
  return a * b
x = map(myfunc, (5, 5, 2), (2, 2, 2))
print(list(x))

def myfunc(a, b):
  return a * b
x = map(myfunc, [5, 5, 2], [2, 2, 2])
print(tuple(x))
#--------------------------reuce function---------------------------------
from functools import reduce
def add(a,b):
    return a+b
obj=reduce(add,[1,2,3,4,5])
print(obj)

result=reduce(lambda a,b:a+b, [1,2,3,4,5,6])
print(result)
#----------------------------generator function -----------------------
def my_function():
    yield 1
    yield 2
    yield 3
obj=my_function()  
print(obj.__next__())  
print(obj.__next__())  
print(obj.__next__())  








   




