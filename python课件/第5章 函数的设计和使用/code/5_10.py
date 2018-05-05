import random

def demo(x, n):
    if n not in x:
        print(n, ' is not an element of ', x)
        return

    i = x.index(n) #获取指定元素在列表中的索引
    x[0], x[i] = x[i], x[0] #将指定元素与第0个元素交换
    key = x[0]
    
    i = 0
    j = len(x) - 1
    while i<j:
        while i<j and x[j]>=key: #从后向前寻找第一个比指定元素小的元素
            j -= 1
        x[i] = x[j] 
        
        while i<j and x[i]<=key: #从前向后寻找第一个比指定元素大的元素
            i += 1
        x[j] = x[i]
        
    x[i] = key

x =list(range(1, 10))
random.shuffle(x)

print(x)
demo(x, 4)
print(x)
