x=0
y=1
num=int(input("Enter any number : "))
print(x)
print(y)
for i in range(num-2):
    z=x+y
    print(z)
    x=y
    y=z
