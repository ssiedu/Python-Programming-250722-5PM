fileobj=open("Employee.txt","a")
name=input("Enter Employee name : ")
age = int(input("Enter Employee age : "))
fileobj.write("\n" + name +"\n"+str(age)+"\n")
#fileobj.write(str(age)+ "\n")
fileobj.close()
