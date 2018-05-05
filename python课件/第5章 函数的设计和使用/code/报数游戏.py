'''有n个人围成一圈，顺序排号。
从第一个人开始从1到k（假设k=3）报数，报到k的人退出圈子，然后圈子缩小，
从下一个人继续游戏，问最后留下的是原来的第几号。'''

from itertools import cycle

def demo(lst, k):
    #切片，以免影响原来的数据
    t_lst = lst[:]
    #游戏一直进行到只剩下最后一个人
    while len(t_lst)>1:
        #创建cycle对象
        c = cycle(t_lst)
        #从1到k报数
        for i in range(k):
            t = next(c)
        #一个人出局，圈子缩小
        index = t_lst.index(t)
        t_lst = t_lst[index+1:] + t_lst[:index]
        #测试用，查看每次一个人出局之后剩余人的编号
        print(t_lst)
    #游戏结束
    return t_lst[0]

lst = list(range(1,11))
print(demo(lst, 3))
