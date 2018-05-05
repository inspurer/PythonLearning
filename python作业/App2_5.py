#sample input:1,2,3,4,5 回车 1 回车 3
#sample output:1,2,3
aStr = input('请输入一个列表(以，间隔)')
aStr = aStr.split(",")
aList = [int(aStr[i]) for i in range(len(aStr))]
begin = int(input('请输入起始下标'))
end = int(input('请输入结束下标'))
print(aList[begin:end+1])
