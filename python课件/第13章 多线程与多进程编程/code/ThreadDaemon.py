import threading
import time

class mythread(threading.Thread):
    def __init__(self, num, threadname):
        threading.Thread.__init__(self, name = threadname)
        self.num = num
        #self.daemon = True
    def run(self):        
        time.sleep(self.num)
        print(self.num)

t1 = mythread(1, 't1')
t2 = mythread(5, 't2')
t2.daemon = True
#t2.setDaemon(False)
print(t1.daemon)
print(t2.daemon)

t1.start()
t2.start()
