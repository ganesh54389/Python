#============================exception Handling===========================================
#-----------------------------zero divison error------------------------------
num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
print(num1+num2)
try:
    print(num1/num2)
except:
    print("divison by zero error")
print(num1-num2)
#another example
try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")
#------------------index out of bound error-----------------
list_01=[0,1,2,3,4,5]
print(list_01[0])
print(list_01[1])
try:
   print(list_01[6])
except:
    print("index out of range")   
print(list_01[2])
print(list_01[3])
print(list_01[4])
#another example
num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
print(num1+num2)
try:
    print(num1/num2)
except:
    print("divison by zero error")
else:
    print("normal flow of programme excution")
print(num1-num2)
#------------------------finally block example--------------------------
try:  
    div = 4 // 0    
    print( div )   
except ZeroDivisionError:  
    print( "Atepting to divide by zero" )   
finally:  
    print( 'This is code of finally clause' )  
#-----------------------value error -------------------------------
try:
    num1=int(input("enter the number:"))
    num2=int(input("enter the number"))
except ValueError as e:
       print(e) #checking the value error


#-----------------------key error------------------------------- 
subjects = {'Sree': 'Maths', 
			'Ram': 'Biology', 
			'Shyam': 'Science', 
			'Abdul': 'Hindi'} # this is key error example
print(subjects['Fharan']) 
#handling key error 
subjects = {'Sree': 'Maths', 
			'Ram': 'Biology', 
			'Shyam': 'Science', 
			'Abdul': 'Hindi'}  
try: 
	print('subject of Fharan is:', 
		subjects['Fharan']) 
except KeyError: 
	print("Fharan's records doesn't exist") 








