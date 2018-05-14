#编写程序，生成包含20个各不相同的随机数的列表，
#然后将前10个元素按降序排列，后10个元素按升序排列。输出结果
import random
aList = [random.randint(0,100) for i in range(20)]
print('生成的随机数为:')
print(aList)
front = sorted(aList[0:10],reverse = True)
print('前十个数降序排列为:')
print(front)
back = sorted(aList[10:20])
print('后十个数升序排列为:')
print(back)
#print(front.extend(back)) output None consider WHY???
front.extend(back)
print(front)
