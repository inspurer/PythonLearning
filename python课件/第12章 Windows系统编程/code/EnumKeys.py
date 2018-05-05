import _winreg 
key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer") 
try: 
    i = 0 
    while 1:
        Name, Value, Type = _winreg.EnumValue(key, i)
        print repr(Name),':',repr(Value),':',Type
        i += 1
except WindowsError:
    pass
