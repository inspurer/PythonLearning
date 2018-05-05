import threading
import time
class mythread(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        global x
        lock.acquire()
        for i in range(3):
            x = x + i
        time.sleep(2)
        print(x)
        lock.release()

#lock = threading.Lock()
lock = threading.RLock()
tl = []
for i in range(10):
    t = mythread()
    tl.append(t)

x = 0

for i in tl:
    i.start()
