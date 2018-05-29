import wx
class App9_1(wx.Frame):
    def __init__(self,superion):
        wx.Frame.__init__(self,parent = superion,title = "Colors Selector",size = (400,300))
        #添加主面板
        self.mainPanel = wx.Panel(self)
        self.mainPanel.SetBackgroundColour('purple')
        #添加按钮
        self.hitButton = wx.Button(parent = self.mainPanel,label = "请选择背景颜色",pos=(160,130))
        #为按钮绑定Hander
        self.Bind(wx.EVT_BUTTON,self.onButtonHited,self.hitButton)
        #添加颜色对话框
        self.colDialog = wx.ColourDialog(parent = self)
    def onButtonHited(self,event):
        self.colDialog.ShowModal()
        #进程在此阻塞，其他窗体disabled
        color = self.colDialog.GetColourData().GetColour()
        wx.MessageBox(str(color))
        self.mainPanel.SetBackgroundColour(color)
if __name__ =='__main__':
    app = wx.App()
    MySelector = App9_1(None)
    MySelector.Show()
    app.MainLoop()
