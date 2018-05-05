def hannoi(num, src, dst, temp=None):
    global times    #声明用来记录移动次数的变量为全局变量
    assert type(num) == int, 'num must be integer'   #确认参数类型和范围
    assert num > 0, 'num must > 0'    
    if num == 1: #只剩最后或只有一个盘子需要移动，这也是函数递归调用的结束条件
        print('The {0} Times move:{1}==>{2}'.format(times, src, dst))
        times += 1
    else:
        #递归调用函数自身，先把除最后一个盘子之外的所有盘子移动到临时柱子上
        hannoi(num-1, src, temp, dst)
        hannoi(1, src, dst)   #把最后一个盘子直接移动到目标柱子上
        #把除最后一个盘子之外的其他盘子从临时柱子上移动到目标柱子上
        hannoi(num-1, temp, dst, src)
times = 1    #用来记录移动次数的变量
hannoi(3, 'A', 'C', 'B') #A表示最初放置盘子的柱子，C是目标柱子，B是临时柱子
