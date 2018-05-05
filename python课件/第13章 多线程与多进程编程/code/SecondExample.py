import threading
import time
def func1(x, y):
    for i in range(x, y):
        print(i, end=' ')
    #time.sleep(10)

t1=threading.Thread(target = func1, args = (15, 20))
t1.start()
t1.join(5)
t2=threading.Thread(target = func1, args = (5, 10))
t2.start()
#t2.join() #the program will not continue until t2 thread finishs

print(t1.isAlive())
time.sleep(2) #try to comment this line to see the different result
print(t2.isAlive())
