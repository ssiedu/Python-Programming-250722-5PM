num=int(input("Enter Number : "))#1234
rev=0;
sod=0;
tod=0
temp = num
while num!=0:
    rev = rev*10+num%10  #0+4  rev=4   // 40+3=43   // 430+2 = 432//  4320+1 = 4321
    sod=sod+num%10 # 0+4=4 = 4+3 =7 // 7+2 =9 // 9 +1 =10
    tod=tod+1
    num=num//10  #1234//10    num =123    num=12  num=1//10  =0
print("reverse Number :",rev)
print("sum of digit : ",sod)
print("Total Number of digit : ",tod)
if temp == rev:
    print("Number is pallindrome")
else:
    print("Number is not pallindrom")
