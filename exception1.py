try :
    a=int(input("Enter the value of a : "))
    b=int(input("Enter the value of b : "))
    #res=0

    res=a/b

    
#except ValueError:
    #print("No")

except Exception as e:
    print(e)
