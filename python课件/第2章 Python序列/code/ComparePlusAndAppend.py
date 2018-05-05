import time

result = []
start = time.time()
for i in range(10000):
    result = result + [i]
print(len(result), time.time()-start)
print(result)
result = []
start = time.time()
for i in range(10000):
    result.append(i)
print(len(result), time.time()-start)
