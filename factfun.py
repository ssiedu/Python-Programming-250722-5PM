def fact(n):
      f=1;
      for i in range(1,n+1):
            f *= i
      return f;

num=int(input("Enter any number : "))
#result = fact(num)
print("factorial of number is : ",fact(num))
