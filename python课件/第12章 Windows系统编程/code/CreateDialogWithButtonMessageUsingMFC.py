import win32ui
import win32con
from pywin.mfc import dialog

class MyDialog(dialog.Dialog):
    def OnInitDialog(self):
        dialog.Dialog.OnInitDialog(self)
        self.HookCommand(self.OnButton1,1051)
        self.HookCommand(self.OnButton2,1052)
    def OnButton1(self, wPrarm, lParam):
        win32ui.MessageBox('Button1', 'Python', win32con.MB_OK)
        #self.EndDialog(1)
    def OnButton2(self, wParam, lParam):
        text = self.GetDlgItemText(1054)
        win32ui.MessageBox(text, 'Python', win32con.MB_OK)
        #self.EndDialog(1)

style = win32con.DS_MODALFRAME | win32con.WS_POPUP | win32con.WS_VISIBLE \
        | win32con.WS_CAPTION | win32con.WS_SYSMENU | win32con.DS_SETFONT
childstyle = win32con.WS_CHILD | win32con.WS_VISIBLE
buttonstyle = win32con.WS_TABSTOP | childstyle

di = ['Python', (0,0,300,180), style, None, (8,'MS Sans Serif')]
Button1 = (['Button', 'Button1', 1051, (80, 150, 50, 14),
            buttonstyle | win32con.BS_PUSHBUTTON])
Button2 = (['Button', 'Button2', 1052, (160, 150, 50, 14),
            buttonstyle | win32con.BS_PUSHBUTTON])
Stadic = (['Static', 'Python Dialog', 1053, (130, 50, 60, 14), childstyle])
Edit = (['Edit', '', 1054, (130, 80, 60, 14),
         childstyle | win32con.ES_LEFT | win32con.WS_BORDER | win32con.WS_TABSTOP])

init = []
init.append(di)
init.append(Button1)
init.append(Button2)
init.append(Stadic)
init.append(Edit)

mydialog = MyDialog(init)
mydialog.DoModal()
