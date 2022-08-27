x=10
y=20

print("Logical and : ", ((x>y) and (y==20)))      # false
print("Logical or  : ", ((x>y) or (y!=20)))         #false
print("Logical not  : ", (not(x)))              #false
print("Logical and/not : ",((x>=10) or (not(y))))   #true
print("Logical or/not  : ", (not(x) or not(y)))         #false
print("Logical and/or/not : ", (not((x==y) or (x>=y))) and (x<=y))  #false#true
