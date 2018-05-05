import wx

class ListBoxDemo(wx.Frame):
    def __init__(self, superion):
        wx.Frame.__init__(self, parent=superion, title='ListBox demo', size=(200,200))
        panel = wx.Panel(self)
        self.buttonQuit = wx.Button(parent=panel, label='Quit', pos=(60,120))
        self.Bind(wx.EVT_BUTTON, self.OnButtonQuit, self.buttonQuit)
        li = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        self.listBox = wx.ListBox(panel, choices=li)

        self.Bind(wx.EVT_LISTBOX, self.OnClick, self.listBox)

    def OnClick(self, event):
        #t = self.listBox.GetSelection()
        #s = self.listBox.GetString(t)
        s = self.listBox.GetStringSelection()
        wx.MessageBox(s)

    def OnButtonQuit(self, event):
        dlg=wx.MessageDialog(self,'Really Quit?','Caution',\
                             wx.CANCEL|wx.OK|wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_OK:
            self.Destroy()
if __name__ == '__main__':
    app = wx.App()
    frame = ListBoxDemo(None)
    frame.Show()
    app.MainLoop()
