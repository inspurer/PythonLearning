import time

def Insert():
    a = []
    for i in range(10000):
        a.insert(0,i)

def Append():
    a = []
    for i in range(10000):
        a.append(i)

start = time.time()
for i in range(10):
    Insert()
print 'Insert:',time.time()-start

start = time.time()
for i in range(10):
    Append()
print 'Append:',time.time()-start
