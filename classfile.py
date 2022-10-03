import pickle
class student:
    def __init__(self,name=" ",rollno=0):
        self.name=name;
        self.rollno=rollno
        self.m1,self.m1=0.0,0.0
    def marks(self):
        self.m1=eval(input("Enter subject1 marks : "))
        self.m2=eval(input("Enter subject2 marks : "))
    def display(self):
        print(" Student name : ",self.name)
        print(" Student rollno : ",self.rollno)
        print(" Subject 1 : ",self.m1)
        print(" subject 2 : ", self.m2)

S1=student("shubham",101)
S2=student("Rahul",102)
S1.marks()
S2.marks()
f=open("Record.txt","wb")
pickle.dump(S1,f)
pickle.dump(S2,f)
f.close()
f=open("Record.txt","rb")
S1=pickle.load(f)
S2=pickle.load(f)
print(S1.__dict__)
print(S2.__dict__)
f.close()
