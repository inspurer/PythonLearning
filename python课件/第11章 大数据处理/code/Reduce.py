'''
功能：合并Map以后的结果成为一个结果文件
作者：董付国
日期：2014-11-12
QQ：306467355
Email：dongfuguo2005@126.com
'''
import os

def Reduce(sourceFolder, targetFile):
    if not os.path.isdir(sourceFolder):
        print(sourceFolder, ' does not exist.')
        return
    result = {}
    #Deal only with the mapped files
    allFiles = [sourceFolder+'\\'+f for f in os.listdir(sourceFolder) if f.endswith('_map.txt')]
    for f in allFiles:
        with open(f, 'r') as fp:
            for line in fp:
                line = line.strip()
                if not line:
                    continue
                position = line.index(':')
                key = line[0:position]
                value = int(line[position + 1:])
                result[key] = result.get(key,0) + value
    with open(targetFile, 'w') as fp:
        for k,v in result.items():
            fp.write(k + ':' + str(v) + '\n')

if __name__ == '__main__':
    Reduce('test', 'test\\result.txt')
