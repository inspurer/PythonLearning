import sys
import os
#路径不区分大小写，\  \\  / 均可做分隔符
direcotry = input('请输入路径')
filename = input('请输入文件名')
#direcotry = r'E:\JAVA Src' just for test
#filename = r'test.txt'
#error
#os.walk returns an iterator that yields three-tuples, not a three-tuple:
#You need to iterate over os.walk():
#for root_o, dir_o, files_o in os.walk(top):
#from stackoverflow
'''pathlist,direcotrylist,filelist=os.walk(direcotry)
if filename in filelist:
    print('Exsits!')
else:
    print('Can not find!')'''
#这是深度优先遍历，第一次迭代，得到一个filelist,包含当前目录下的所有文件
#第二次迭代，这是filelist是当前目录下第一个文件夹下的所有文件
#以此类推
for pathlist,direcotrylist,filelist in os.walk(direcotry):
    print(filelist)
    if filename in filelist:
        print('Exsits!')
        break;
    else:
        print('Can not find!')

