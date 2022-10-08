import threading
import time
def square(num):
    #print("Square of numbers : ")
    for n in num:
        time.sleep(0.3)
        print("square is : ",n*n)

def cube(num):
    #print("cube of numbers " )
    for n in num:
        time.sleep(0.3)
        print("cube is : ",n*n*n)

arr=[4,5,6,7]

'''t1=time.time()
square(arr)
cube(arr)
print("Total time taken by thread : ", time.time()-t1)'''
t1=threading.Thread(target=square, args=(arr,))
t2=threading.Thread(target=cube,args=(arr,))
t1.start()
time.sleep(0.4)
t2.start()
t1.join()
t2.join()
print("Thread 1 and Thread 2 executed")
