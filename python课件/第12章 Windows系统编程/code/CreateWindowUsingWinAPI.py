import win32gui
from win32con import *
def WndProc(hwnd,msg,wParam,lParam):
    if msg==WM_PAINT:
        hdc,ps = win32gui.BeginPaint(hwnd)
        rect=win32gui.GetClientRect(hwnd)
        win32gui.DrawText(hdc,'GUI Python',len('GUI Python'),rect,
                          DT_SINGLELINE|DT_CENTER|DT_VCENTER)
        win32gui.EndPaint(hwnd,ps)
    if msg == WM_DESTROY:
        win32gui.PostQuitMessage(0)
    return win32gui.DefWindowProc(hwnd, msg, wParam, lParam)

wc = win32gui.WNDCLASS()
wc.hbrBackground = COLOR_BTNFACE + 1
wc.hCursor = win32gui.LoadCursor(0, IDC_ARROW)
wc.hIcon = win32gui.LoadIcon(0, IDI_APPLICATION)
wc.lpszClassName = 'Python on Windows'
wc.lpfnWndProc = WndProc

reg = win32gui.RegisterClass(wc)

hwnd = win32gui.CreateWindow(
    reg, 'Python', WS_OVERLAPPEDWINDOW, CW_USEDEFAULT, CW_USEDEFAULT,
    CW_USEDEFAULT, CW_USEDEFAULT, 0, 0, 0, None)
win32gui.ShowWindow(hwnd, SW_SHOWNORMAL)
win32gui.UpdateWindow(hwnd)

win32gui.PumpMessages()
