#-----------------------------creating a  tuple ---------------------
my_tuple=()
print(my_tuple)
my_tuple=(1,2,3)
print(my_tuple)
my_tuple=(1,"hello",3.2)
print(my_tuple)
my_tuple=("mouse",[1,2,4],(1,2,3))
print(len(my_tuple))
my_tuple=(1,2,3,4,5,6,7,8)
my_tuple01=(1,2,3)
print(len(my_tuple))
print(max(my_tuple))
print(min(my_tuple))
my_tuple=(4,2,3,[6,5])
my_tuple[3][0]=9
print(my_tuple)
print((1,2,3)+(4,5,6))#concatenation
print((1,2,3)*2)#repeat in a given number pof times 
my_tuple=(1,2,"a")
print("a" in my_tuple)
for name in ("john","kate"):
    print("hello",name)


