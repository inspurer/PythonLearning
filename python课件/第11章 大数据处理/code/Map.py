'''
功能：提取文件中日期出现次数
作者：董付国
日期：2014-11-11，2015-12-26更新
QQ：306467355
Email：dongfuguo2005@126.com
'''
import os
import re
import threading
import time

def Map(sourceFile):
    if not os.path.exists(sourceFile):
        print(sourceFile, ' does not exist.')
        return    
    pattern = re.compile(r'[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}')
    result = {}
    with open(sourceFile, 'r') as srcFile:
        for dataLine in srcFile:
            r = pattern.findall(dataLine)
            if r:
                t = result.get(r[0], 0)
                t += 1
                result[r[0]] = t
    desFile = sourceFile[0:-4] + '_map.txt'
    with open(desFile, 'a+') as fp:
        for k, v in result.items():
            fp.write(k + ':' + str(v) + '\n')

if __name__ == '__main__':
    desFolder = 'test'
    files = os.listdir(desFolder)
    
    #如果不使用多线程，可以直接这样写
    '''for f in files:
        Map(desFolder + '\\' + f)'''
    
    #使用多线程
    def Main(i):
        Map(desFolder + '\\' + files[i])
    fileNumber = len(files)
    for i in range(fileNumber):
        t = threading.Thread(target = Main, args =(i,))
        t.start()
    
