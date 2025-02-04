#------------------------if conditions--------------------------------
age=18
if age>=18:
    print(f"youb are eligible to vote ")
    print(f"your age is{age}")
    print(f"so you are eligible to vote ")
print("outside of block of code")    
number=8
if number<=9:
    print(number*number)
print("next line of code ")  
#------------------------else condition--------------------------------------------  
age=16
if age>=18:
    print(f"you are eligible to vote ")
else:
    print(f"you are not eligible to vote ")
    print(f"your age is {age}")   
print(f"this is outline of code ")   
#another example
user_name=input("enter the username:")
password=input("enter the password :")
if user_name=="ganesh" and password=="1234":
    print("login succses")
else:
    print("invalid credentials ")  
# ---------------------------------elif conditions--------------------------------------
#gerade system checking 
marks =int(input("enter the marks:"))
if marks>=90 and marks <=100:
    print(f"you got A grade your obtained marks {marks}")
elif marks>=80:
     print(f"you got B grade your obtained marks {marks}")
elif marks>=70:
      print(f"you got C grade your obtained marks {marks}")   
elif marks>=60:
      print(f"you got D grade your obtained marks {marks}")  
elif marks>=35:
      print(f"you got pass grade your obtained marks {marks}")
else:
     print(f"you are failed ,obtained marks{marks}.better luck next time ") 
#---------------------------------nested if else stm---------------------------------
user_name=input("enter the username:")
password=input("enter the password :")
if user_name=="ganesh":
    if password=="1234":
        print("login succses")
    else:
        print("invalid password")
else:
    print("invalid username ,check the username once")            
#--------------------shorthand if else conditions ----------------------------------------
age=18
print("you are eligible to vote ")if age>=-18 else print("you are not eligible to vote ")
number=int(input("enter the number:"))
print("even number ")if number%2==0 else print("odd number")


          

        

    

        
