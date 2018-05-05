from ctypes import *
from time import sleep
from datetime import datetime

#方便调用Windows底层API函数
user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi

#实时查看当前窗口
def getProcessInfo():
    global windows
    #获取当前位于桌面最顶端的窗口句柄
    hwnd = user32.GetForegroundWindow()
    pid = c_ulong(0)
    #获取进程ID
    user32.GetWindowThreadProcessId(hwnd, byref(pid))
    processId = str(pid.value)
    #获取可执行文件名称
    executable = create_string_buffer(512)
    h_process = kernel32.OpenProcess(0x400|0x10, False, pid)
    psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)
    #获取窗口标题
    windowTitle = create_string_buffer(512)
    user32.GetWindowTextA(hwnd, byref(windowTitle), 512)
    #关闭句柄
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)
    #更新最近两个窗口列表
    windows.pop(0)
    windows.append([executable.value.decode('gbk'),windowTitle.value.decode('gbk')])

def main():
    global windows
    windows = [None, None]
    while True:
        getProcessInfo()
        #如果用户切换窗口则进行提示
        if windows[0] != windows[1]:
            print('='*30)
            print(str(datetime.now())[:19],windows[0],'==>',windows[1])
        sleep(0.2)
if __name__ == '__main__':
    main()
