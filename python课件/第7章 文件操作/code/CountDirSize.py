import os

totalSize = 0
fileNum = 0
dirNum = 0

def visitDir(path):
    global totalSize
    global fileNum
    global dirNum
    for lists in os.listdir(path): 
        sub_path = os.path.join(path, lists)
        if os.path.isfile(sub_path):
            fileNum = fileNum+1
            totalSize = totalSize+os.path.getsize(sub_path)
        elif os.path.isdir(sub_path):
            dirNum = dirNum+1
            visitDir(sub_path) 

def main(path):
    if not os.path.isdir(path):
        print('Error:"', path, '" is not a directory or does not exist.')
        return
    visitDir(path)
    
def sizeConvert(size):
    K = 1024
    M = 1024**2
    G = 1024**3
    if size >= G:
        return str(size/G)+'G Bytes'
    elif size >= M:
        return str(size/M)+'M Bytes'
    elif size >= K:
        return str(size/K)+'K Bytes'
    else:
        return str(size)+'Bytes'

def output(path):
    print('The total size of '+path+' is:'+sizeConvert(totalSize)+'('+str(totalSize)+' Bytes)')
    print('The total number of files in '+path+' is:',fileNum)
    print('The total number of directories in '+path+' is:',dirNum)
    
if __name__=='__main__':
    path = r'd:\idapro6.5plus'
    main(path)
    output(path)
