flag=0;
num = int(input("Enter any number : "))#13
for i in range(2,num//2):
    #print(i,end=" ")
    if(num%i==0):     
        flag=1
        break;
if flag==1:
    print("not prime")
else:
    print("prime")
        
        
