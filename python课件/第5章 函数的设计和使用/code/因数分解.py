from random import randint
from math import sqrt

def factoring(n):
    '''对大数进行因数分解'''
    if not isinstance(n, int):
        print('You must give me an integer')
        return
    #开始分解，把所有因数都添加到result列表中
    result = []
    for p in primes:
        while n!=1:
            if n%p == 0:
                n = n/p
                result.append(p)
            else:
                break
        else:
            result = map(str, result)
            result = '*'.join(result)
            return result
    #考虑参数本身就是素数的情况
    if not result:
        return n

testData = [randint(10, 100000) for i in range(50)]
#随机数中的最大数
maxData = max(testData)
#小于maxData的所有素数
primes = [ p for p in range(2, maxData) if 0 not in 
        [ p% d for d in range(2, int(sqrt(p))+1)] ]

for data in testData:
    r = factoring(data)
    print(data, '=', r)
    #测试分解结果是否正确
    print(data==eval(r))
