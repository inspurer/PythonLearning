# This program or framework only considers the difference of print in Python2 and Python3.
# Of course you can consider and convert other rules.
import sys
import os

def Usage():
    print("Usage:\n%s anotherPython2Program"%sys.argv[0])
    
def main():
    if len(sys.argv) != 2:
        Usage()
        return
    pyFileName = sys.argv[1]
    if not os.path.isfile(pyFileName):
        Usage()
        return
    if not pyFileName.endswith('.py'):
        Usage()
        return
    newFileName = pyFileName[0:-3]+'_3.py'
    desFP = open(newFileName, 'w')
    with open(pyFileName, 'r') as fp:
        for line in fp.readlines():
            if 'print ' in line:
                if '#' not in line:
                    line = line.rstrip().replace('print ', 'print(')+')\n'
                else:
                    position = line.index('#')
                    line_before = line[0:position].rstrip()
                    line_after = line[position:]
                    line = line_before.replace('print ', 'print(')+') '+line_after
            desFP.write(line)
    desFP.close()

main()
        
    
