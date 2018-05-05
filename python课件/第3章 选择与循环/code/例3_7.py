for i in range(100, 1000):
    #这里是序列解包的用法
    bai, shi, ge = map(int, str(i))
    if ge**3 + shi**3 + bai**3 == i:
        print(i)
