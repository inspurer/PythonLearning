from random import randint

def bubbleSort(lst):
    length = len(lst)
    for i in range(0, length):
        for j in range(0, length-i-1):
            #比较相邻两个元素大小，并根据需要进行交换
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

lst = [randint(1, 100) for i in range(20)]
print('Before sort:\n', lst)
bubbleSort(lst)
print('After sort:\n', lst)
