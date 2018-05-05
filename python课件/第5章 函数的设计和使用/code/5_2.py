def demo(*para):
    avg = sum(para)/len(para) #注意Python 2.x与Python 3.x对除法运算符“/”的解释不同
    g = [i for i in para if i>avg]
return (avg,)+tuple(g)

print(demo(1, 2, 3, 4))
