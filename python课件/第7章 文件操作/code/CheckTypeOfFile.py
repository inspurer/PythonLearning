'''Check the type of given file.
   You need install python-magic and libmagic,
   you'd better run this program on linux platform.
   '''
import magic
ms = magic.magic_open(magic.MAGIC_NONE)
ms.load()
fileName = r'c:\windows\notepad.exe'
data = open(fileName,'rb').read()
print ms.buffer(data)
