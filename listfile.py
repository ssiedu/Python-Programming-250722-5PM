file=open("listfile","w")
list1=[]
for i in range(5):
    name=input("Enter Name of student : ")
    list1.append(name+"\n")

file.writelines(list1)
file.close()
f=open("listfile","r")
print(f.readlines())
f.close()
