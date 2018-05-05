#check and view autoruns in the system

from win32api import *
from win32con import *

def GetValues(fullname):
    name=str.split(fullname,'\\',1)
    try:
        if name[0]=='HKEY_LOCAL_MACHINE':
            key=RegOpenKey(HKEY_LOCAL_MACHINE,name[1],0,KEY_READ)
        elif name[0]=='HKEY_CURRENT_USER':
            key=RegOpenKey(HKEY_CURRENT_USER,name[1],0,KEY_READ)
        elif name[0]=='HKEY_CURRENT_ROOT':
            key=RegOpenKey(HKEY_CURRENT_ROOT,name[1],0,KEY_READ)
        elif name[0]=='HKEY_CURRENT_CONFIG':
            key=RegOpenKey(HKEY_CURRENT_CONFIG,name[1],0,KEY_READ)
        elif name[0]=='HKEY_USERS':
            key=RegOpenKey(HKEY_USERS,name[1],0,KEY_READ)
        else:
            print('Error, no key named ',name[0])
        info = RegQueryInfoKey(key)
        for i in range(0,info[1]):
            ValueName = RegEnumValue(key,i)
            print(str.ljust(ValueName[0],20),ValueName[1])
        RegCloseKey(key)
    except BaseException as e:
        print('Sth is wrong')
        print(e)
if __name__=='__main__':
    KeyNames=['HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run',
              'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce',
              'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx',
              'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run',
              'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce']
    for KeyName in KeyNames:
        print(KeyName)
        GetValues(KeyName)
