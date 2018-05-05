from os.path import isdir, join, splitext
from os import remove, listdir, rmdir
import sys

filetypes = ['.tmp', '.log', '.obj', '.txt']

def delCertainFiles(directory):
    if not isdir(directory):
        return
    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):
            delCertainFiles(temp)
        elif splitext(temp)[1] in filetypes: #检查文件类型
            remove(temp)
            print(temp, ' deleted....')

def main():
    directory = r'E:\old'
    #directory = sys.argv[1]
    delCertainFiles(directory)

main()
