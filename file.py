#=====================file handling============================
file=open("temple.txt",mode='r')
read_data=file.read()# return the data present in file
print(read_data)
file.close()

file=open("temple.txt",mode='r')
read_data=file.readline()# return the first line of file
print(read_data)
file.close()

file=open("temple.txt",mode='r')
read_data=file.readlines()#return of list of substrings
print(read_data)
file.close()

file=open("temple.txt",mode='a')
append_data=file.write("\nby using append operations we can add the data")
file.close()#data added to the existing data in the file 


file=open("temple.txt",mode='w')
write_data=file.write("this is new data")
file.close()#added to the file as a new data

list_1=["\nhema","\nkishor","\nkumar"]
file=open("temple.txt",mode='w')
write_data=file.writelines(list_1)
file.close()

#seek ---set pointer positions and tell---find pointer locations
file=open("temple.txt",mode='w+')
write_data=file.write("sample test")
print(file.tell())
file.seek(0)
read_data=file.read()
print(read_data)
file.close
#rename the file by using os module
import os
filename="temple.txt"
new_name="classic.txt"
os.rename(filename,new_name)
#------------------------completed---------------------------------------






