import os
import re
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
                print(r[0], ',', 1)

if __name__ == '__main__':
    Map('test.txt')    
