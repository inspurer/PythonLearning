import os
import sys

def Reduce(targetFile):
    result = {}
    for line in sys.stdin:
        riqi, shuliang = line.strip().split(',')
        result[riqi] = result.get(riqi, 0)+1
    with open(targetFile, 'w') as fp:
        for k,v in result.items():
            fp.write(k + ':' + str(v) + '\n')

if __name__ == '__main__':
    Reduce('result.txt')
