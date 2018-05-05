import threading
class mythread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)
    def run(self):
        global myevent
        if myevent.isSet():
            myevent.clear()
            myevent.wait()
            print(self.getName())
        else:
            print(self.getName())
            myevent.set()

myevent = threading.Event()
myevent.set()
tl = []
for i in range(10):
    t = mythread(str(i))
    tl.append(t)

for i in tl:
    i.start()
