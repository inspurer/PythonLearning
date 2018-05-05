#编写程序，至少用两种方法计算100以内所有偶数的和。
sumer = 0
print("First way\n")
for i in range(101):
    if(i%2 ==0):
        sumer+=i
print("sum = %d" %(sumer))
print("\nSecond way\n")
#aList = list(range(0,101,2))
#print(aList)
sumer = sum(range(0,101,2))
print("sum = %d" %(sumer))
#不可将变量名summer改成sum,会覆盖掉sum()函数
