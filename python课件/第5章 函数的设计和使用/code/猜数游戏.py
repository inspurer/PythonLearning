'''系统随机产生一个数，玩家最多可以猜5次，系统会根据玩家的猜测进行提示，
玩家则可以根据系统的提示对下一次的猜测进行适当调整。'''

from random import randint

def guess():
    #随机生成一个整数
    value = randint(1,1000)
    #最多允许猜5次
    maxTimes = 5
    for i in range(maxTimes):
        prompt = 'Start to GUESS:' if i==0 else 'Guess again:'
        #使用异常处理结构，防止输入不是数字的情况
        try:
            x = int(input(prompt))
            #猜对了
            if x == value:
                print('Congratulations!')
                break
            elif x > value:
                print('Too big')
            else:
                print('Too little')
        except:
            print('Must input an integer between 1 and 999')
    else:
        #次数用完还没猜对，游戏结束，提示正确答案
        print('Game over. FAIL.')
        print('The value is ', value)

guess()
