#------------------------exercise01--------------------------
my_tuple=("ganesh",24,"green")
print(my_tuple)
#----------------------exercise02-----------------------------
my_tuple=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
print(my_tuple[3])
#-----------------------exercise03---------------------------
print((1,3,5)+(2,4,6))
#-----------------------exercise04--------------------------
rectangle_dimension=(10,5)
length,width=rectangle_dimension
area=length*width
print(area)
#-----------------------------exercise05----------------------
my_tuple=("ganesh",24,"green")
print("ganesh"in my_tuple)
#----------------------------exercise06-----------------------
items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
print("item\t\tprice")
totalcost=0
for item,price in items: 
    totalcost+=price
    print(f"{items}\t\t{price}")
print(f"total\t\t{totalcost}")    
items = [("apple", 99), ("banana", 99), ("milk", 99)]
total = 0

# Print the header
print('Item   \t  Price')
print('-' * 15)

# Iterate through the tuple
for i, j in items:
    total = total + j
    print(f"{i} \t  {j}")

# Print the total
print('-' * 15)
print(f'Total:      {total}')

    