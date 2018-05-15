import re
x = input("请输入一段英文")
pattern =  re.compile(r"\b[a-zA-Z]{1,3}\b");
result = pattern.findall(x);#返回一个列表
for word in result:
    print(word,end=' ')