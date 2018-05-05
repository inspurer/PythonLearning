def conv(lst1, lst2):
    '''用来计算两个列表所表示的信号的卷积，返回一个列表'''
    result = []
    #翻转第一个列表
    lst1.reverse()
    length1 = len(lst1)
    length2 = len(lst2)
    #移动翻转后的第一个列表，直到“完全移入”
    for i in range(1, length1+1):
        t = lst1[length1-i:]
        #计算重叠“面积”
        v = sum((item1*item2 for item1, item2 in zip(t,lst2)))
        result.append(v)
    #继续移动翻转后的第一个列表，直到“完全移出”
    for i in range(1, length2):
        t = lst2[i:]
        v = sum((item1*item2 for item1, item2 in zip(lst1,t)))
        result.append(v)
    return result

def mul(lst):
    '''把列表中的数字转换为普通整数的形式'''
    result = ''
    c = 0
    for item in lst[::-1]:
        item = item + c
        #计算当前位的余数和向前一位进位的数字
        n, c = str(item%10), item //10
        #使用字符串记录临时结果
        result += n
    if c:
        result += str(c)
    return eval(result[::-1])

def main(num1, num2):
    lst1 = list(map(int, str(num1)))
    lst2 = list(map(int, str(num2)))
    result = conv(lst1, lst2)
    print(mul(result)==num1*num2)

from random import randint
for i in range(100):
    num1 = randint(1, 99999999)
    num2 = randint(1, 99999999999)
    main(num1, num2)
