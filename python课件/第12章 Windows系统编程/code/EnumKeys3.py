import winreg 
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer") 
try: 
    i = 0 
    while 1:
        Name, Value, Type = winreg.EnumValue(key, i)
        print (Name,':',Value,':',Type)
        i += 1
except WindowsError:
    pass
