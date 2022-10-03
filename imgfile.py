f=open("Image.png","rb")
f1=open("Image1.png","wb")
'''str=f.read()
for i in str:
    print(i,end= " ")'''
f1.write(f.read())

f.close()
f1.close()
