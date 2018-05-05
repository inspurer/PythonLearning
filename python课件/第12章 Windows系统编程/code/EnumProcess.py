from ctypes.wintypes import *
from ctypes import  *
import collections

kernel32 = windll.kernel32

class tagPROCESSENTRY32(Structure):
    _fields_ = [('dwSize',              DWORD),
                ('cntUsage',            DWORD),
                ('th32ProcessID',       DWORD),
                ('th32DefaultHeapID',   POINTER(ULONG)),
                ('th32ModuleID',        DWORD),
                ('cntThreads',          DWORD),
                ('th32ParentProcessID', DWORD),
                ('pcPriClassBase',      LONG),
                ('dwFlags',             DWORD),
                ('szExeFile',           c_char * 260)]

def enumProcess():
    hSnapshot = kernel32.CreateToolhelp32Snapshot(15, 0)
    fProcessEntry32 = tagPROCESSENTRY32()
    processClass = collections.namedtuple("processInfo","processName processID")
    processSet = []
    if hSnapshot:
        fProcessEntry32.dwSize = sizeof(fProcessEntry32)
        listloop = kernel32.Process32First(hSnapshot, byref(fProcessEntry32))
        while listloop:
            processName = (fProcessEntry32.szExeFile)
            processID = fProcessEntry32.th32ProcessID
            processSet.append(processClass(processName, processID))
            listloop = kernel32.Process32Next(hSnapshot, byref(fProcessEntry32))
    return processSet
for i in enumProcess():
    print(i.processName,i.processID)
