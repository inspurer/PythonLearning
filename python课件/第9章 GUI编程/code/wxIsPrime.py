import wx
from math import sqrt

class IsPrimeFrame(wx.Frame):
    def __init__(self, superion):
        wx.Frame.__init__(self, parent=superion, title='Check Prime', size=(400,200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('Yellow')
        wx.StaticText(parent=panel, label='Input a integer:', pos=(10,10))
        self.inputN = wx.TextCtrl(parent=panel, pos=(120,10))
        self.result = wx.StaticText(parent=panel, label='', pos=(10,50))
        self.buttonCheck = wx.Button(parent=panel, label='Check', pos=(70,90))
        self.Bind(wx.EVT_BUTTON, self.OnButtonCheck, self.buttonCheck)
        self.buttonQuit = wx.Button(parent=panel, label='Quit', pos=(150,90))
        self.Bind(wx.EVT_BUTTON, self.OnButtonQuit, self.buttonQuit)

    def OnButtonCheck(self, event):
        self.result.SetLabel('')
        try:
            num = int(self.inputN.GetValue())
        except BaseException,e:
            self.result.SetLabel('not a integer')
            return
        n = int(sqrt(num))
        for i in range(2,n+1):
            if num%i == 0:
                self.result.SetLabel('No')
                break
        else:
            self.result.SetLabel('Yes')
        #self.buttonCheck.SetLabelText('test')

    def OnButtonQuit(self, event):
        dlg=wx.MessageDialog(self,'Really Quit?','Caution',\
                             wx.CANCEL|wx.OK|wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_OK:
            self.Destroy()
if __name__ == '__main__':
    app = wx.App()
    frame = IsPrimeFrame(None)
    frame.Show()
    app.MainLoop()
