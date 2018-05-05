'''编写函数计算任意位数的黑洞数。
黑洞数是指这样的整数：
由这个数字每位数字组成的最大数减去每位数字组成的最小数仍然得到这个数自身。
例如3位黑洞数是495，因为954-459=495，4位数字是6174，因为7641-1467=6174。'''

def main(n):
    '''参数n表示数字的位数，例如n=3时，返回495'''
    #待测试数范围的起点和结束值
    start = 10**(n-1)+2
    end = start*10-20
    #依次测试每个数
    for i in range(start, end):
        i = str(i)
        #由这几个数字组成的最大的数
        big = ''.join(sorted(i,reverse=True))
        big = int(big)
        #由这几个数字组成的最小的数
        little = ''.join(sorted(i))
        little = int(little)
        if big-little==int(i):
            print(i)
n = 4
main(n)
