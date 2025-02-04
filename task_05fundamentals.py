#print is a function to display information on the screen
print("hello python life ")
print(10+50)
print("welcome to day two of python session")
#----------------comments -------------------------------
#comments are non excutable statements that describe about lines of code 
num_1=10 #value 10 assigned to number 01--->inline comments 
num_2=30 #value 30 assigned to number 02
results=num_1+num_2
''' here the results can store the addition  of num_01 and num_02 
later i display the result by using print function  '''
print(results) 
#----------------variable-------------------------------


# variable is a container to store values 
roll_number=1234
print(roll_number)
#id is used to identify memory location 
print("memory address is:")
print(id(roll_number))
school_name="vivekananda english medium high school "
School_name="avr english medium high school "
_school_name="ganesh englsih medium high school "
first_student_01="Lakshmi Ganesh "
print(school_name)
print(School_name)
print(_school_name)
print(first_student_01)
#varibles are case sensitive 
#camel case
firstName="David kishor kumar "
print(firstName)
#snake case
first_name="mangala lakshmi ganesh "
print(first_name)
#pascal case 
First_Name="indusri"
print(First_Name)


#-------------------data types ---------------------------------------------
#data type is type of the data that can store in variable 
#int ---class
sample_number=1234
print(sample_number)
print("it can print the type of data type")
print(type(sample_number))
#float
float_number=2.10
print(float_number)
print("it can print the type of data type")
print(type(float_number))
#str --string is a class ,sequence of characters 
user_name="ramakrishna123@gmail.com"#it can allow both alpha-numeric-special  characters 
print('kiran kumar sir ')
print("ganesh wake up at 6'0clock ")
print('''he complete "MCA "in "gates institute of technology " ''')

#------------------------------------type converstion ----------------------------------
#integer to float 
height=5
print(height)
print(type(height))
heighttt=float(height)
print(heighttt)
print(type(heighttt))

#floatto int
weight=5.8
print(weight)
print(type(weight))
weighttt=int(weight)
print(weighttt)
print(type(weighttt))

#str to int
roll_num=1234
print(roll_number)
print(type(roll_number))
rolll_numm=int(roll_number)
print(rolll_numm)
print(type(rolll_numm))



#--------------------complex data type --------------------------------
complex_data_type=4+6j
print(type(complex_data_type))
#performing operations using complex number 
complex_number_01=2+6j
complex_number_02=8+6j
result=complex_number_01+complex_number_02
print("result of complex number:")
print(result)

#---------------------List---------------------------------------------------------
list_01=[26,54.8,"kishor kumar",[25,78.9,"lakshmi ganesh "],[65,76.9,"gopal"],54.8]
print(list_01)
print(type(list_01))
print(id(list_01))
list_01.append("nagamma")
print(id(list_01))

#---------------------tuple----------------------------------------------------
tuple_01=(25,34.6,"ganesh",[12,12.5,"kishor"],(24,24.5,"savitri"),25)
print(tuple_01)
print(type(tuple_01))

#-----------------set-----------------------------------------------------------
set_01={"vasu","mahesh",12,12.7}
print(set_01)
print(type(set_01))

#-------------------dictonarty------------------------------------------
my_dict={"02":"kishor","01":"ramesh","username":"1234","(1,2)":"nagamurty","rama":"krishna"},
print(my_dict)
print(type(my_dict))
#------------------boolean---------------------------------------------
print(bool(1))
print(bool(0))
sample=True
sample_01=False
print(type(sample))
print(type(sample_01))


#----------------input function ----------------------------------------
first_number=input("enter the number:")
second_number=input("enter the number:")
result=first_number+second_number#concatenation is done 
print(result)#input function take defualt data type as string

no_1=int(input("enter the number:"))
no_2=int(input("enter the number:"))
result=no_1+no_2
print(f"number01 value is{no_1}and number02 value is{no_2},the result is {result}")








