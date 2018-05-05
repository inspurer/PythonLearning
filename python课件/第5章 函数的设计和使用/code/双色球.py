'''双色球是一种比较常见的彩票玩法，
每一注彩票由6个介于1到33之间的不重复数字和1个介于1到16之间的数字组成。
下面的代码用来随机生成一注双色球彩票，结果是完全随机的，
如果买了不中的话，我是不会负责赔钱的，嘿嘿。'''

import random

def doubleColor():
    red = random.sample(range(1,34), 6)
    blue = random.choice(range(1, 17))
    return str(red)+'-'+str(blue)

print(doubleColor())
