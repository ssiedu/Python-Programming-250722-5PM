f= open("Student.txt","w")
count=int(input("Enter Number of student : "))
for i in range(count):
    name=input("Enter name of student : ")
    rollno=int(input("Enter Roll no :"))
    per = eval(input("Enter percentage :"))
    rec= name + "," + str(rollno) + "," + str(per) + "\n"
    f.write(rec)
f.close()
