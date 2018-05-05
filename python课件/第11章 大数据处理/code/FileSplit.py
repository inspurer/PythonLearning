'''
功能：切分文件
作者：董付国
日期：2014-11-11，2015-12-26更新
QQ：306467355
Email：dongfuguo2005@126.com
'''
import os
import os.path
import time

def FileSplit(sourceFile, targetFolder):
    if not os.path.isfile(sourceFile):
        print(sourceFile, ' does not exist.')
        return
    if not os.path.isdir(targetFolder):
        os.mkdir(targetFolder)
    tempData = []
    number = 1000
    fileNum = 1
    linesRead = 0    
    with open(sourceFile, 'r') as srcFile:
        dataLine = srcFile.readline().strip()
        while dataLine:
            for i in range(number):
                tempData.append(dataLine)                
                dataLine = srcFile.readline()                
                if not dataLine:
                    break
            desFile = os.path.join(targetFolder, sourceFile[0:-4] + str(fileNum) + '.txt')
            with open(desFile, 'a+') as f:
                f.writelines(tempData)
            tempData = []
            fileNum = fileNum + 1       

if __name__ == '__main__':
    #sourceFile = input('Input the source file to split:')
    #targetFolder = input('Input the target folder you want to place the split files:')
    sourceFile = 'test.txt'
    targetFolder = 'test'
    FileSplit(sourceFile, targetFolder)
