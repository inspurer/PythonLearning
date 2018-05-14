#查找输出所有三个字母的单词
import re
s = input('请输入一段英文')
aList = re.findall(r'\b[a-zA-Z]{3}\b',s)
print(aList)
for i in aList:
    print(i)
