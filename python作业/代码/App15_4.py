import os
import pygame
import random
import wx

musicUrlList = []
#加载工作目录下的所有.mp3文件
def musicUrlLoader():
    fileList = os.listdir(".")
    for filename in fileList:
        if filename.endswith(".mp3"):
            print("找到音频文件",filename)
            musicUrlList.append(filename)

class MyMusicPlayer(wx.Frame):
    def __init__(self,superion):
        wx.Frame.__init__(self,parent = superion, title = 'Xinspurer Player',size = (400,300))

        musicUrlLoader()

        MainPanel = wx.Panel(self)
        MainPanel.SetBackgroundColour('pink')

        self.ShowInfoText = wx.StaticText(parent = MainPanel, label = '播放未开始', pos = (100,100)
                                          ,size = (185,25),style = wx.ALIGN_CENTER_VERTICAL)
        self.ShowInfoText.SetBackgroundColour('white')

        self.isPaused = False   #是否被暂停
        self.StartPlayButton = wx.Button(parent = MainPanel, label = '随机播放', pos = (100,150))
        self.Bind(wx.EVT_BUTTON, self.OnStartClicked, self.StartPlayButton)

        self.PauseOrContinueButton = wx.Button(parent = MainPanel, label = '暂停播放', pos = (200,150))
        self.Bind(wx.EVT_BUTTON, self.OnPauseOrContinueClicked, self.PauseOrContinueButton)
        self.PauseOrContinueButton.Enable(False)

        pygame.mixer.init()



    def OnStartClicked(self,event):
        self.isPaused = False
        self.PauseOrContinueButton.Enable(True)

        self.willPlayMusic = random.choice(musicUrlList)
        pygame.mixer.music.load(self.willPlayMusic.encode())
        pygame.mixer.music.play()

        self.ShowInfoText.SetLabel("当前播放:"+self.willPlayMusic)


    def OnPauseOrContinueClicked(self,event):
        if not self.isPaused:
            self.isPaused = True
            pygame.mixer.music.pause()
            self.PauseOrContinueButton.SetLabel('继续播放')

            self.ShowInfoText.SetLabel('播放已暂停')
        else:
            self.isPaused = False
            pygame.mixer.music.unpause()
            self.PauseOrContinueButton.SetLabel('暂停播放')

            self.ShowInfoText.SetLabel("当前播放:" + self.willPlayMusic)


if __name__ == "__main__":
    app = wx.App()
    myMusicPlayer = MyMusicPlayer(None)
    myMusicPlayer.Show()
    app.MainLoop()

#需要pip install pygame
#需要在当前目录上放几首.mp3歌曲,点击随机播放，开始播放某一首
#@author:通信1602班肖涛
