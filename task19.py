#-----task01 reverse order of a list-----------------------------

my_list = [10, 20, 30, 40, 50, 11]
my_list.reverse()# one way 
print(my_list)
my_list = [10, 20, 30, 40, 50, 11]
print(my_list[6::-1])# another way
my_list = [10, 20, 30, 40, 50, 11]
print(my_list[-1: :-1])# another way

#--------task02- common elemenst -------------------

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
new_list=[]
for i in list1:
    for j in list2:
        if i==j:
            new_list.append(i)
print(new_list)    

#-------------------task03 unique elements--------------------
original_list = [1, 2, 2, 3, 4, 4, 5]  
unique_list=[]
for i  in original_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)        
#--------------removing dupilcate elements ---------------------
original_list = [1, 2, 2, 3, 4, 4, 5]  
duplicates_free_list=[]
for i  in original_list:
    if i not in duplicates_free_list:
        duplicates_free_list.append(i)
duplicates_free_list.sort()        
print(duplicates_free_list)
#-----------------list concarenation--------------------------
li_01=[1,2,3,4,5,6,7,8]
li_02=["sukanya","roopa","maheswari"]
results=li_01+li_02
print(results)#one way
li_01=[1,2,3,4,5,6,7,8]
li_02=["sukanya","roopa","maheswari"]
li_01.extend(li_02)
print(li_01)#another way
# #---------------------------list repettions-------------------
ori_list=[4,5,6]
emplty_list=[]
for i in ori_list:
    for j in range(3):
        emplty_list.append(i)
print(emplty_list)
#----------------------list removal------------------------------
test_list=[10,20,30,40,50,60,70]
len=len(test_list)
for i in range(len):
    if i%2!=0:
        print(test_list[i])
#----------list insertion --------------------
listt_01=[4,5,6]
listt_01.insert(0,10)
listt_01.insert(1,11)
listt_01.insert(2,12)
print(listt_01)
#-----------list comprehenshion excecises--------------
em_li=[]
for i in range(11):
    result=i**2
    em_li.append(result)
print(em_li)
#----------even numbers in the list -----------------
list_emp=[]
for i in range(21):
    if i%2==0:
        list_emp.append(i)
print(list_emp)   
#-----------------words legth------------------------
em_list=[]
words=["apple","banana","cherry","date"]  
for i in words:
    result=len(i)
    em_list.append(result)
print(em_list)       
    
    
