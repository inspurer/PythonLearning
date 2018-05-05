from random import randint

def selectSort(lst, reverse=False):
    length = len(lst)
    for i in range(0, length):
        m = i  #假设剩余元素中第一个最小或最大        
        for j in range(i+1, length):  #扫描剩余元素
            #如果有更小或更大的，就记录下它的位置
            exp = 'lst[j] < lst[m]'
            if reverse:
                exp = 'lst[j] > lst[m]'
            #内置函数eval()用来对字符串进行求值
            if eval(exp):
                m = j        
        if m!=i:  #如果发现更小或更大的，就交换值
            lst[i], lst[m] = lst[m], lst[i]


lst = [randint(1, 100) for i in range(20)]
print('Before sort:\n', lst)
selectSort(lst)
print('After sort:\n', lst)
