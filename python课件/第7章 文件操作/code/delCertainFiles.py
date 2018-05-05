# delete files of certain types in current directory and its all sub directories recursively
from os.path import isdir, join, splitext
from os import remove, listdir, getcwd
filetypes = []
def delCertainFiles(directory):
    for filename in listdir(directory):
        temp = join(directory, filename)       
        if isdir(temp):
            delCertainFiles(temp)
        elif splitext(temp)[1][1:] in filetypes: # check file extension name
            remove(temp)
            print(temp, ' deleted....')

def readFileTypes():
    global filetypes
    with open('filetypes.txt', 'r') as fp:
        filetypes = fp.readlines()
    filetypes = [ext.strip() for ext in filetypes]

def main():
    readFileTypes()
    print(filetypes)
    delCertainFiles(getcwd())

main()
