#--------------------------creating a string------------------------------------------ 
single_quoted_string='mangala lakshmi ganesh'
double_quoted_string="mangala gopal"
triple_quoted_string='''hai ganesh how are you '''
print(single_quoted_string)
print(double_quoted_string)
print(triple_quoted_string)
#checking type of data type
print(type(single_quoted_string))
print(type(double_quoted_string))
print(type(triple_quoted_string))
#another way of defining string 
sample=str()
print(type(sample))
print(sample)

my_string="python"
print("positive indexing")
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[4])
print(my_string[5])
print("negative indexing")
my_string="python"
print(my_string[-1])
print(my_string[-2])
print(my_string[-3])
print(my_string[-4])
print(my_string[-5])
print(my_string[-6])
print("slicing")
my_string="python"
print(my_string[1: :1])
print(my_string[ : : ])
print(my_string[-2: :-1])
print(my_string[-2])
user="mahesh ravuri"
print(user[7])
print(user[2:8])
#-----------------------String methods-------------------------
message = "Hello, World!"
upper_case_messge=message.upper()
lower_case_message=message.lower()
print(upper_case_messge)
print(lower_case_message)
sentence = "This is a sample sentence."
count_01=sentence.count("i")
print(count_01)
whitespace_string = " This is a string with leading and trailing whitespace. "
print(len(whitespace_string))
stripped_string=whitespace_string.strip()
print(len(stripped_string))
print(whitespace_string)
data = "Pythonlife,Kiran,123456"
data_01=data.split(",")
print(data_01)
original_string = "Python is fun!"
modified_string=original_string.replace("fun","life")
print(modified_string)
filename = "example.txt"
starts_with = filename.startswith("ex")
ends_with = filename.endswith(".txt")
print(starts_with) # Output: True
print(ends_with) # Output: True
sentence = "This is a sentence."
position_a = sentence.find('a')#return index position if true otherthen return -1
position_i = sentence.index('i')#return index position if true otherthan value error  
print(position_a)
print(position_i)
text = "python programming"
capitalized_text = text.capitalize()
print(capitalized_text)
numeric_string = "12345"
alpha_string = "Python"
is_numeric = numeric_string.isdigit()
is_alpha = alpha_string.isalpha()
print(is_numeric) 
print(is_alpha)
word_list = ['Hello', 'World']
joined_string = ' '.join(word_list)
print(joined_string)






