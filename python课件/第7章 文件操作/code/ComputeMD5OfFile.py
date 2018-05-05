import hashlib
import os
import sys

#fileName = sys.argv[1]
fileName = r'c:\test.txt'
if os.path.isfile(fileName):
    with open(fileName,'r') as fp:
        lines = fp.readlines()
    data = ''.join(lines)
    print hashlib.md5(data).hexdigest()

