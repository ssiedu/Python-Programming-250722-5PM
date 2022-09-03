num = int(input("Enter Number :"))
if num%5==0 and num%7==0:
    print("divisible by both")
elif num%7==0:
    print("divisible by 7")
elif num%5==0:
    print("divisible by 5")
else:
    print("not divisible by both")
