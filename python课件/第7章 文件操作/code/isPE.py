# -*- coding:utf-8 -*-

import sys
import os

if len(sys.argv)!=2:
    print('Usage: {0} anotherFile'.format(sys.argv[0]))
    sys.exit()
    
filename = sys.argv[1] #获取要检测的文件名
if not os.path.isfile(filename): #判断是否为文件
    print(filename + ' is not file.')
    sys.exit()

with open(filename, 'rb') as fp:
    flag1 = fp.read(2) #读取文件前两个字节
    fp.seek(0x3c) #获取PE头偏移
    offset = ord(fp.read(1))
    fp.seek(offset)
    flag2 = fp.read(4) #获取PE头签名
if flag1==b'MZ' and flag2==b'PE\x00\x00': #判断是否为PE文件的典型特征签名
    print(filename + ' is a PE file.')
else:
    print(filename + ' is not a PE file.')
