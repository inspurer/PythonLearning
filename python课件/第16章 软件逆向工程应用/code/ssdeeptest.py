import sys
import os

srcFile = sys.argv[1]
desFile = sys.argv[2]

os.popen('ssdeep -b {0} >hash.txt'.format(srcFile))
results = os.popen('ssdeep -bm hash.txt -a "{0}"'.format(desFile))
for result in results.readlines():
    if 'matches' in result:
        start = result.rfind('(')+1
        end = result.rfind(')')
        print('The similarity degree is:'+result[start:end])
        break
