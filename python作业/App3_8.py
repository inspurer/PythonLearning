#编写程序，输出所有由1、2、3、4这四个数字组成的素数，
#并且每个在素数中每个数字只用一次
import math
a = {1,2,3,4}
aSet = set()
for i in a:
    ii = i*1000
    for j in a - {i}:
        jj = j*100
        for k in a-{i,j}:
            kk = k*10
            for l in a-{i,j,k}:
                aSet.add(ii+jj+kk+l)
print(aSet)
aList = list(aSet)
#aSet在迭代过程中不允许修改
for i in range(len(aList)-1,-1,-1):
    n = aList[i]
    t = math.sqrt(n)
    j = 2
    while j<t:
        if(n%j == 0):
            del aList[i]
            break
        j +=1
print(aList)
