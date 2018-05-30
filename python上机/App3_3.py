import datetime
import wx
class App3_3(wx.Frame):
    def getCurrentTime(self):
        time = datetime.datetime.now()
        showcontent = time.strftime('%Y-%m-%d %H:%M:%S');
        return showcontent

    def __init__(self,supervision):
        wx.Frame.__init__(self,parent = supervision, title = "Lab_App_3_3",size = (400,300))

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('white')

        self.showLabel = wx.StaticText(parent = self.panel,label = 'Show time in 1s',size = (100,30),pos = (150,120),style = wx.ALIGN_CENTER)

        #创建定时器,其中参数owner是实现wx.EvtHandler的实例,故而此处不能用self.showlabel
        self.timer = wx.Timer(self)
        #绑定定时器Hander
        self.Bind(wx.EVT_TIMER,self.onTimer,self.timer)
        #设置间隔时间为1000ms并启动定时器
        self.timer.Start(1000)
    def onTimer(self,event):
        self.showLabel.SetLabel(self.getCurrentTime())
if __name__ == '__main__':
    app = wx.App()
    MyLabApp3_3 = App3_3(None)
    MyLabApp3_3.Show()
    app.MainLoop()