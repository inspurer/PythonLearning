sList = []
while True:
    x = input("请输入成绩")
    sList.append(float(x))
    print('当前平均成绩为:',sum(sList)/len(sList))
    y = input("是否继续输入,(yes继续，no中止)")
    if y == 'no':
        break
