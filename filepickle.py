import pickle
def write():
    f=open("binarylist","wb")
    list1=[1,"Hello","Welcome"]
    pickle.dump(list1,f)
    f.close()

def read():
    f1=open("binarylist","rb")
    data=pickle.load(f1)
    print(data)
    f1.close()

write()
read()
