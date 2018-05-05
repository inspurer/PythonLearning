import threading
import time
import queue

class Producer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)
    def run(self):
        global myqueue
        myqueue.put(self.getName())
        print(self.getName(), ' put ', self.getName(), ' to queue.')

class Consumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)
    def run(self):
        global myqueue        
        print(self.getName(), ' get ', myqueue.get(), ' from queue.')

myqueue = queue.Queue()
plist = []
clist = []

for i in range(10):
    p = Producer('Producer' + str(i))
    plist.append(p)
    c = Consumer('Consumer' + str(i))
    clist.append(c)

for i in plist:
    i.start()
    i.join()
for i in clist:
    i.start()
    i.join()
