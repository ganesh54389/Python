#------------------list------------------------------------------------------------------
list_1=[1,2,3,"ganesh","vasu sir ",[4,5,6,7]]
print(type(list_1))
print(list_1)
#operations on list 
#indexing 
my_list=[1,2,3,"apple","banana"]
print(my_list)
my_list = [10, 20, 30, 40, 50]
print("negative indexing ")
print(my_list[0])
print(my_list[1])
print(my_list[2])     
print(my_list[3])
print(my_list[4])
print("negative indexing ")
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])
print(my_list[-5])
#slicing
my_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(my_list[1:7])#extraxt 20 to 70
print(my_list[0:4])#extraxt 10 to 40
print(my_list[0:8])#extraxt 10 to 80
print(my_list[ :8])#extraxt 10 to 80
print(my_list[ : ])#extraxt 10 to 80
print(my_list[2: ])#extraxt 30 to 80
print(my_list[: :2 ])#alternate values
print(my_list[: :3 ])#alternate values
print("using negative indexing values:")
my_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(my_list[ : :1])
print(my_list[ : :-1])
print(my_list[8:0:-1])
print(my_list[-6: :1])
print(my_list[8: :-1])
print(my_list[3: :-1])
#-------list methods -------------------------
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
num=["ganesh","ramesh","mahesh"]
numbers.append("ganesh")
numbers.append(1234)
numbers.append(23.6)
numbers.append([1,2,3,4])
numbers.extend(num)
print(numbers)
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]# copy function 
copy_1=numbers.copy()
numbers.clear()
print(copy_1)
print(numbers)
numbers = [3, 1, 4, 1, 5, 9, 2, 6,]
print(numbers.count(1))
print(numbers.index(3))
numbers.remove(1)
print(numbers)
numbers = [3, 1, 4, 1, 5, 9, 2, 6,]
obj=numbers.pop(3)
print(numbers)
print(obj)
numbers.insert(3,5060)
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
numbers = [3, 1, 4, 1, 5, 9, 2, 6,]
numbers.sort(reverse=True)
print(numbers)
#---------------------------------------------------------------
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][1])
print(matrix[1][2])
print(matrix[2][0])
#------------------list comprenhesion----------------------------------
print([i**2 for i in range(5)])
print([i for i in range(9) if i!=1])







