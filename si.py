principal = eval(input("Enter the value of principal amount : "))
rate   = eval(input("Enter the value of rate of interest : "))
time = eval(input("Enter the time in year/month : "))
Simple_interest = (principal *rate *time)/100
print("simpal interest is : ",Simple_interest)
total_amount = principal + Simple_interest
print("Total amount with interest : ",total_amount)
