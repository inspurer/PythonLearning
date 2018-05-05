import win32ui
import win32api
from win32con import *
from pywin.mfc import window

class MyWnd(window.Wnd):
    def __init__(self):
        window.Wnd.__init__(self, win32ui.CreateWnd())
        self._obj_.CreateWindowEx(WS_EX_CLIENTEDGE,
                                  win32ui.RegisterWndClass(0, 0, COLOR_WINDOW+1),
                                  'MFC GUI', WS_OVERLAPPEDWINDOW,
                                  (10,10,800,500), None, 0, None)
        
        self.HookMessage(self.OnRClick, WM_RBUTTONDOWN)
        
        submenu = win32ui.CreateMenu()
        menu = win32ui.CreateMenu()
        submenu.AppendMenu(MF_STRING, 1051, '&Open')
        submenu.AppendMenu(MF_STRING, 1052, '&Close')
        submenu.AppendMenu(MF_STRING, 1053, '&Save')
        menu.AppendMenu(MF_STRING | MF_POPUP, submenu.GetHandle(), '&File')

        submenu = win32ui.CreateMenu()
        submenu.AppendMenu(MF_STRING, 1054, '&Copy')
        submenu.AppendMenu(MF_STRING, 1055, '&Paste')
        submenu.AppendMenu(MF_SEPARATOR, 1056, None)
        submenu.AppendMenu(MF_STRING, 1057, 'C&ut')
        menu.AppendMenu(MF_STRING | MF_POPUP, submenu.GetHandle(), '&Edit')

        submenu = win32ui.CreateMenu()
        submenu.AppendMenu(MF_STRING, 1058, 'Tools')
        submenu.AppendMenu(MF_STRING | MF_GRAYED, 1059, 'Settings')
        m = win32ui.CreateMenu()
        m.AppendMenu(MF_STRING | MF_POPUP | MF_CHECKED, submenu.GetHandle(), 'Option')
        menu.AppendMenu(MF_STRING | MF_POPUP, m.GetHandle(), '&Other')

        self._obj_.SetMenu(menu)
        self.HookCommand(self.MenuClick, 1051)
        self.HookCommand(self.MenuClick, 1052)
        self.HookCommand(self.MenuClick, 1053)
        self.HookCommand(self.MenuClick, 1054)
        self.HookCommand(self.MenuClick, 1060)

    def OnRClick(self,param):
        submenu = win32ui.CreatePopupMenu()
        submenu.AppendMenu(MF_STRING, 1060, 'Copy')
        submenu.AppendMenu(MF_STRING, 1061, 'Paste')
        submenu.AppendMenu(MF_SEPARATOR, 1062, None)
        submenu.AppendMenu(MF_STRING, 1063, 'Cut')
        submenu.TrackPopupMenu(param[5],
                               TPM_LEFTALIGN | TPM_LEFTBUTTON | TPM_RIGHTBUTTON,
                               self)

    def MenuClick(self, lParam, wParam):
        if lParam == 1051:
            self.MessageBox('Open', 'Python', MB_OK)
        elif lParam == 1053:
            self.MessageBox('Save', 'Python', MB_OK)
        elif lParam == 1052:
            self.OnClose()
        elif lParam == 1060 or lParam == 1054:
            self.MessageBox('Copy', 'Python', MB_OK)
        
    def OnClose(self):
        self.EndModalLoop(0)
        
    def OnPaint(self):
        dc, ps = self.BeginPaint()
        dc.DrawText('MFC GUI', self.GetClientRect(),
                    DT_SINGLELINE | DT_CENTER | DT_VCENTER)
        self.EndPaint(ps)
    

w = MyWnd()
w.ShowWindow()
w.UpdateWindow()
w.RunModalLoop(1)
