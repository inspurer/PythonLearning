import md5
import os

TheFile=input('Please input a filename including the full path:')
if not os.path.exists(TheFile):
    print 'The File ',TheFile,' does not exist.'
else:
    TheFile=open(TheFile,'r')
    FileContent=TheFile.read()
    TheFile.close()
    md5value=md5.md5()
    md5value.update(FileContent)
    print md5value.hexdigest()
