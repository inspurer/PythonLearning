import matplotlib.pyplot as plt
with open ("data.txt") as fp:
    lines = fp.readlines()
x = list()
y = list()
for line in lines:
    data = ''.join(line)
    data = data.split(',')
    data = [float(item) for item in data]
    x.append(data[0])
    y.append(data[1])
fig = plt.figure()
#1行一列第一个活动区域
ax1 = fig.add_subplot(111)
#设置标题
ax1.set_title('locations')
#设置X轴标签
plt.xlabel('X')
#设置Y轴标签
plt.ylabel('Y')
#画散点图
cValue = []
color = ['r','g','b','k','y']
for item in color:
    item = list(item)
    cValue.extend(item*12)
sValue = []
size = [1+3*i for i in range(0,84,1)]
for i in size:
    j = list()
    j.append(i)
    sValue.extend(j*12)
ax1.scatter(x,y,s=sValue,c=cValue,marker='.')
#设置图标
#plt.legend('x1')
#显示所画的图
plt.show()


