from functools import reduce
from math import gcd

def isCoPrime(p):
    '''判断p中每个元组的第1个数（即mi）之间是否互素'''
    for index, item1 in enumerate(p):
        for item2 in p[index+1:]:
            if gcd(item1[0], item2[0])!=1:
                return False
    return True

def extEuclid(Mi, mi):
    '''暴力穷举，求Mi对mi的乘法逆元，也可以使用扩展欧几里得算法快速求解'''
    for i in range(1, mi):
        if i*Mi % mi == 1:
            return i

def chineseRemainder(p):
    '''p为[(3, 2), (7, 1), (13, 5),(mi, ai) ...]形式的参数，其中3/7/13为商，2/1/5为余数'''
    #先判断所给数据中的mi是否互素，如果不是则提示数据错误并退出
    if not isCoPrime(p):
        return 'Data error.'        
    #切片浅复制，临时变量，防止修改实参中的数据
    pp = p[:]
    #求M=m1*m2*m3*...*mn
    ppp = [item[0] for item in pp]
    M = reduce(lambda x,y: x*y, ppp)
    for index, item in enumerate(pp):
        Mi = int(M/item[0])
        bi = extEuclid(Mi, item[0])
        pp[index] = item+(Mi, bi)
    #求解最终结果，sum(ai*bi*Mi) mod M
    result = sum([item[1]*item[2]*item[3] for item in pp])
    result = result % M
    #考虑特殊情况，不允许结果为1
    if result==1:
        result = result+M
    return result

data = [[(3,2), (5,3), (7,2)],
        [(5,1), (3,2)],
        [(5,1), (3,1)],
        [(5,4), (3,2)],
        [(7,2), (8,4), (9,3)],
        [(5,2), (6,4), (7,4)],
        [(3,2), (5,3), (7,4)]]
for p in data:
    print(p)
    print(chineseRemainder(p))
