import wx
class wxGUI(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(parent=None, title='wxGUI', size=(300,280))
        self.panel = wx.Panel(self.frame, -1)

        self.radioButtonSexM = wx.RadioButton(self.panel, -1, 'Male', pos=(80,60))
        self.radioButtonSexF = wx.RadioButton(self.panel, -1, 'Female', pos=(80,80))
        self.checkBoxAdmin = wx.CheckBox(self.panel, -1, 'Aministrator', pos=(150,80))

        self.label1 = wx.StaticText(self.panel, -1, 'UserName:', pos=(0,110), style=wx.ALIGN_RIGHT)
        self.label2 = wx.StaticText(self.panel, -1, 'Password:', pos=(0,130), style=wx.ALIGN_RIGHT)

        self.textName = wx.TextCtrl(self.panel, -1, pos=(70,110), size=(160,20))
        self.textPwd = wx.TextCtrl(self.panel, -1, pos=(70,130), size=(160,20),style=wx.TE_PASSWORD)
        
        self.buttonOK = wx.Button(self.panel, -1, 'OK', pos=(30,160))
        self.Bind(wx.EVT_BUTTON, self.OnButtonOK, self.buttonOK)
        self.buttonCancel = wx.Button(self.panel, -1, 'Cancel', pos=(120,160))
        self.Bind(wx.EVT_BUTTON, self.OnButtonCancel, self.buttonCancel)
        self.buttonOK.SetDefault()
        

        self.frame.Show()
        return True
    
    def OnButtonOK(self, event):
        finalStr = ''
        if self.radioButtonSexM.GetValue() == True:
            finalStr += 'Sex:Male\n'
        elif self.radioButtonSexF.GetValue() == True:
            finalStr += 'Sex:Female\n'
        if self.checkBoxAdmin.GetValue() == True:
            finalStr += 'Administrator\n'
        if self.textName.GetValue()=='dongfuguo' and self.textPwd.GetValue()=='dongfuguo':
            finalStr += 'user name and password are correct\n'
        else:
            finalStr += 'user name or password is incorrect\n'
        wx.MessageBox(finalStr)
    def OnButtonCancel(self, event):
        self.radioButtonSexM.SetValue(True)
        self.radioButtonSexF.SetValue(False)
        self.checkBoxAdmin.SetValue(True)
        self.textName.SetValue('')
        self.textPwd.SetValue('')

app = wxGUI()
app.MainLoop()
