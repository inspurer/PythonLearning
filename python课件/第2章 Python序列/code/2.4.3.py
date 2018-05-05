import random
import time

def RandomNumbers(number, start, end):
    '''使用列表来生成number个介于start和end之间的不重复随机数'''
    data = []
    n = 0
    while True:
        element = random.randint(start, end)
        if element not in data:
            data.append(element)
            n += 1
        if n == number - 1:
            break
    return data

def RandomNumbers1(number, start, end):
    '''使用列表来生成number个介于start和end之间的不重复随机数'''
    data = []
    while True:
        element = random.randint(start, end)
        if element not in data:
            data.append(element)
        if len(data) == number:
            break
    return data

def RandomNumbers2(number, start, end):
    '''使用集合来生成number个介于start和end之间的不重复随机数'''
    data = set()
    while True:
        data.add(random.randint(start, end))
        if len(data) == number:
            break
    return data

start = time.time()
for i in range(10000):
    RandomNumbers(50, 1, 100)
print('Time used:', time.time()-start)

start = time.time()
for i in range(10000):
    RandomNumbers1(50, 1, 100)
print('Time used:', time.time()-start)

start = time.time()
for i in range(10000):
    RandomNumbers2(50, 1, 100)
print('Time used:', time.time()-start)
