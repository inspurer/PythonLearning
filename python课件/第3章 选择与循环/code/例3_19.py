def binarySearch(lst, value):
    start = 0
    end = len(lst)
    while start < end:
        print(lst[start:end])
        middle = (start + end) // 2      #计算中间位置        
        if value == lst[middle]:         #查找成功，返回元素对应的位置
            return middle        
        elif value > lst[middle]:        #在后面一半元素中继续查找
            start = middle + 1        
        elif value < lst[middle]:        #在前面一半元素中继续查找
            end = middle  
    return False                         #查找不成功，返回False

from random import randint

lst = [5, 5, 20, 21, 21, 23, 23, 23, 28, 28, 29, 30, 31, 32, 33, 36, 41, 45, 46, 47]
lst.sort()
print(lst)
result = binarySearch(lst, 30)
if result!=False:
    print('Success, its position is:',result)
else:
    print('Fail. Not exist.')
