#模拟Tim登录界面，账号为‘123456’，密码为‘654321’正确
import wx
class App9_3(wx.Frame):
    #初始化上半部分Bar
    def topPanelInit(self):
        self.timPic = wx.Image("Tim.png", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.timButton = wx.BitmapButton(self.mainPanel, -1, self.timPic, pos=(0,0),size = (420,125))
    #加载头像
    def imageLoader(self,supervison):
        self.pic = wx.Image(self.filename, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button = wx.BitmapButton(supervison, -1, self.pic, pos=(40, 150))
    #初始化下半部分bar
    def bottomPanelInit(self):
        self.imageLoader(self.mainPanel)
        self.accEdit = wx.TextCtrl(parent = self.mainPanel,pos = (120,150),size = (195,30),style = wx.TE_CENTER)
        self.accLab = wx.StaticText(parent = self.mainPanel,label = "注册账号",pos = (320,155),size = (80,30),style = wx.ALIGN_CENTER)
        self.pasEdit = wx.TextCtrl(parent = self.mainPanel,pos = (120,180),size = (195,30),style = wx.TE_CENTER|wx.TE_PASSWORD)
        self.pasLab = wx.StaticText(parent = self.mainPanel,label = "忘记密码",pos = (320,185),size = (80,30),style = wx.ALIGN_CENTER)

        self.logButton = wx.Button(parent = self.mainPanel,label = "登录",pos = (120,230),size = (195,40))
        self.logButton.SetBackgroundColour('red')
        #为登陆按钮注册Handel
        self.Bind(wx.EVT_BUTTON,self.onLoginButtonClicked,self.logButton)
    def onLoginButtonClicked(self,event):
        if self.accEdit.Value == '123456' and self.pasEdit.Value == '654321':
            wx.MessageBox("登陆成功")
            self.DestroyChildren()
            self.imageLoader(self)
        else:
            wx.MessageBox("登陆失败")
    #构造函数
    def __init__(self,filename):
        wx.Frame.__init__(self, None, -1, u'Tim', size=(440,330))
        self.filename=filename
        self.mainPanel=wx.Panel(self,-1)
        self.SetBackgroundColour('white')
        self.topPanelInit()
        self.bottomPanelInit()
app=wx.App()
frame=App9_3('App9_3.jpg')
frame.Show()
app.MainLoop()
