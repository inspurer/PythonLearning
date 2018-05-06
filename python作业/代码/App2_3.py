#编写程序，生成1000个0~1000之间的随机整数
#并统计每个元素的出现次数
import random
aList = [random.randint(0,100) for i in range(1000)]
aSet = set(aList)
for j in aSet:
    print(j,':',aList.count(j))
