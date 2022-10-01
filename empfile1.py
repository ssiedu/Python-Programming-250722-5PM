f=open("Emp.txt","w+")

for i in range(2):
    name=input("Enter the name :")
    age = int(input("Enter age : "))
    rec= name + " " + str(age)+ "\n"
    f.write(rec)


#f.write(str(age))
f.close()


