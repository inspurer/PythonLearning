import os

def searchZeroFiles(directory):
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isfile(path):
            if (os.path.getsize(path) == 0) and (os.path.split(path)[1] != '__init__.py'):
                print(path)
        elif os.path.isdir(path):
            searchZeroFiles(path)
searchZeroFiles('c:\\python35')
