import threading
class mythread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        print('I am {0}'.format(self.num))

t1 = mythread(1)
t2 = mythread(2)
t3 = mythread(3)
t1.start()
t2.start()
t3.start()
