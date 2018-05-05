#这个循环用来保证必须输入大于2的整数作为评委人数
while True:
    try:
        n = int(input('请输入评委人数：'))
        if n <= 2:
            print('评委人数太少,必须多于2个人。')
        else:
            #如果输入大于2的整数，就结束循环
            break
    except:
        Pass

#用来保存所有评委的打分
scores = []
for i in range(n):
    #这个while循环用来保证用户必须输入0到100之间的数字
    while True:
        try:
            score = input('请输入第{0}个评委的分数：'.format(i+1))
            #把字符串转换为实数
            score = float(score)
            #用来保证输入的数字在0到100之间
            assert 0<=score<=100
            scores.append(score)
            #如果数据合法，跳出while循环，继续输入下一个评委的得分
            break
        except:
            print('分数错误')

#计算并删除最高分与最低分
highest = max(scores)
lowest = min(scores)
scores.remove(highest)
scores.remove(lowest)
#计算平均分，保留2位小数
finalScore = round(sum(scores)/len(scores), 2)

formatter = '去掉一个最高分{0}\n去掉一个最低分{1}\n最后得分{2}'
print(formatter.format(highest, lowest, finalScore))
