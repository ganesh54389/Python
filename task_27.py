#--------------adding function-----------------------
def add(a,b):
    sum=a+b
    return sum
print(add(25,75))
#------------------square function -------------------
def square(x):
    return x*x
x=int(input("enter the number:"))
print(square(x))
#-----------------factorial function--------------
def factorial(n):
    if n < 0:
        print("Input must be a positive integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(3))
#--------------maximum function---------------------
def maximum(numbers):
    max_value=numbers[0]
    for num in numbers:
        if num>max_value:
            max_value=num
    return max_value
print(maximum([1,2,3,4]))    
#----------------------reverese a function---------------
def reverse(s):
    print(s[-1: :-1])
reverse("kishor")   
#----------------------prime number---------------------------
def is_prime(n):
    if n>=2:
        for i in range(2,n):
            n%i==0
            return "not a prime"
        return "prime"
print(is_prime(2))    

#-----------------sum of squares ----------------
def sum_of_squares(numbers):
    sum=0
    for x in numbers:
        sum=sum+(x**2)
        return sum
print(sum_of_squares([1,2,3]))    








    


        

    