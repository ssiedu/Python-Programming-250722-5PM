num=int(input("Enter number :"))
if num==0:
    print("Zero")
elif num>0:
    print("Positive")
    if num%2==0:
        print("Even")
    else:
        print("Odd")
else:
    print("Negative")
    if num%2==0:
        print("Even")
    else:
        print("odd")
