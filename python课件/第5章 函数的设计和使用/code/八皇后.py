'''八皇后问题。八皇后问题是高斯先生（就是小时候就把1+2+3+...+100转换成(1+100)*50的那个数学家）在60多年以前提出来的，
是一个经典的回溯算法问题，其核心为：在国际象棋棋盘（8行8列）上摆放8个皇后，
要求8个皇后中任意两个都不能位于同一行、同一列或同一斜线上。'''

def isValid(s, col):
    '''这个函数用来检查最后一个皇后的位置是否合法'''
    #当前皇后的行号
    row = len(s)
    #检查当前的皇后们是否有冲突
    for r, c in enumerate(s):
        #如果这一列已有皇后，或者某个皇后与当前皇后的水平与垂直距离相等
        #就表示当前皇后位置不合法，不允许放置
        if c == col or abs(row - r) == abs(col - c):
            return False
 
    return True
 
def queen(n, s=()):
    '''这个函数返回的结果是每个皇后所在列号'''
    #已是最后一个皇后，保存本次结果
    if len(s) == n:
        return [s]
 
    res = []
    for col in range(n):
        if not isValid(s, col): continue
        for r in queen(n, s + (col,)):
            res.append(r)
 
    return res

#形式转换，最终结果中包含每个皇后所在的行号和列号
result = [[(r, c) for r, c in enumerate(s)] for s in queen(8)]
#输出合法结果的数量
print(len(result))
#输出所有可能的结果，也就是所有皇后的摆放位置
#结果中每个皇后的位置是一个元组，里面两个数分别是行号和列号
for r in result:
    print(r)
