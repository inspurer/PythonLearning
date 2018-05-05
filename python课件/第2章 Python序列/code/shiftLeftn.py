import time
from random import randint as randint

def shiftLeftn_1(myList, n):
    if (not isinstance(n, int)) or (not isinstance(myList, list)):
        print('Parameter wrong')
        return
    for i in range(n):
        myList.append(myList.pop(0))

def shiftLeftn_2(myList, n):
    first = myList[0:n]
    second = myList[n:]
    first.reverse()
    second.reverse()
    myList = first+second
    myList.reverse()
    return myList

timesWin = 0
for j in range(1000):
    print('='*30)
    listSize = randint(100, 1000)
    repeatTimes = randint(1000, 10000)
    shiftTimes = randint(1, listSize)
    print('listSize:', listSize, 'repeatTimes:', repeatTimes, 'shiftTimes:', shiftTimes)
    x = list(range(listSize))
    #print('First method(More straightforward):')
    start = time.time()
    for i in range(repeatTimes):
        shiftLeftn_1(x, shiftTimes)
    delta1 = time.time()-start
    print('First method(More straightforward):', delta1)

    #print('Second method(Classic algorithm):')
    start = time.time()
    for i in range(repeatTimes):
        shiftLeftn_2(x, shiftTimes)
    delta2 = time.time()-start
    print('Second method(Classic algorithm):', delta2)

    if delta1 < delta2:
        timesWin += 1
print(timesWin)
