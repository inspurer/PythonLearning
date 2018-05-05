import threading

class Producer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
        global x
        con.acquire()
        if x == 20:
            con.wait()
        else:
            print('\nProducer:', end=' ')
            for i in range(20):                
                print(x, end=' ')
                x = x + 1
            print(x)
            con.notify()
        con.release()

class Consumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name =threadname)
    def run(self):
        global x
        con.acquire()
        if x == 0:
            con.wait()
        else:
            print('\nConsumer:', end=' ')
            for i in range(20):                
                print (x, end=' ')
                x = x - 1
            print(x)
            con.notify()
        con.release()

con = threading.Condition()
x = 0
p = Producer('Producer')
c = Consumer('Consumer')
p.start()
c.start()
p.join()
c.join()
print('\nAfter Producer and Consumer all done:',x)
