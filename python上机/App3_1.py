import re
with open("App3_1.cpp","r") as fp:
    data = fp.readlines();
count = 0;
suitabledata = [];
flag = False  #是否是形如“/*...*/”的注释
for line in data:
    #print(line)
    line.strip()
    #line = re.sub('\s','',line)   #最好不要用这句，会把字符串中间的也去掉
    #line.replace("\t","").replace("\n",""),很好奇为什么这句不起作用
    line = line.replace("\t","").replace("\r","").replace("\n","")#因为不是原地操作。。。
    #print(line)
    #print(len(line))
    if(line.startswith(r"//")):
        continue
    if(line.startswith(r"/*")):
        flag = True;
        continue
    if(line.endswith(r"*/")):
        flag = False
        continue
    if(flag):    #不能放在前面
        continue
    if(line=='}' or line =='{'):
        count += 1
        continue
    if line in suitabledata:
        continue
    count += 1 
    suitabledata.append(line)
print("总代码行数",len(data))
print("不重复代码行数:",count)
    
    
