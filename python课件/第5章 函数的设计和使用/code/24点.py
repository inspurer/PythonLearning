'''24点游戏是指随机选取4张扑克牌（不包括大小王），
然后通过四则运算来构造表达式，如果表达式的值恰好等于24就赢一次。
下面的代码定义了一个函数用来测试随机给定的4个数是否符合24点游戏规则，
如果符合就输出所有可能的表达式。'''

from random import randint
from itertools import permutations

#4个数字和2个运算符可能组成的表达式形式
exps = ('((%s %s %s) %s %s) %s %s',
        '(%s %s %s) %s (%s %s %s)', 
        '(%s %s (%s %s %s)) %s %s',
        '%s %s ((%s %s %s) %s %s)',
        '%s %s (%s %s (%s %s %s))')
ops = r'+-*/'

def test24(v):
    result = []
    #Python允许函数的嵌套定义
    #这个函数对字符串表达式求值并验证是否等于24
    def check(exp):
        try:
            #有可能会出现除0异常，所以放到异常处理结构中
            return int(eval(exp)) == 24
        except:
            return False
    #全排列，枚举4个数的所有可能顺序
    for a in permutations(v):
        #查找4个数的当前排列能实现24的表达式
        t = [exp % (a[0], op1, a[1], op2, a[2], op3, a[3]) for op1 in ops for op2 in ops for op3 in ops for exp in exps if check(exp %(a[0], op1, a[1], op2, a[2], op3, a[3]))]
        if t:
            result.append(t)
    return result

for i in range(20):
    print('='*20)
    #生成随机数字进行测试
    lst = [randint(1, 14) for j in range(4)]
    r = test24(lst)
    if r:
        print(r)
    else:
        print('No answer for ', lst)
