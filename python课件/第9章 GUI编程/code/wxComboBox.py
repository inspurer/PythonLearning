import wx
class wxGUI(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(parent=None, title='wxGUI', size=(300,200))
        self.panel = wx.Panel(self.frame, -1)

        self.names = {'First Class':['Zhang San', 'Li Si', 'Wang Wu'],
                 'Second Class':['Zhao Liu', 'Zhou Qi']}

        #ComboBox1
        self.comboBox1 = wx.ComboBox(self.panel, value='Click here',\
                                    choices=self.names.keys(),\
                                    pos=(0,50), size=(100,30))
        self.Bind(wx.EVT_COMBOBOX, self.OnCombo1, self.comboBox1)

        #ComboBox2
        self.comboBox2 = wx.ComboBox(self.panel, value='Click here',\
                                    choices=[],\
                                    pos=(0,100), size=(100,30))
        self.Bind(wx.EVT_COMBOBOX, self.OnCombo2, self.comboBox2)

        self.frame.Show()
        return True
    
    def OnCombo1(self, event):
        banji = self.comboBox1.GetValue()
        self.comboBox2.Set(self.names[banji])

    def OnCombo2(self, event):
        wx.MessageBox(self.comboBox2.GetValue())

app = wxGUI()
app.MainLoop()
