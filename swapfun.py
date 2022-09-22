def swap(x,y):
      print("value of x : ",x)
      print("value of y : ",y)
      temp=x
      x=y
      y=temp
      print("value of x : ",x)
      print("value of y : ",y)

a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
print("Before function call")
print("value of a : ",a)
print("value of b : ",b)
swap(a,b)
print("After function call")
print("value of a : ",a)
print("value of b : ",b)
