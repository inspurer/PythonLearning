import wx
class wxGUI(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(parent=None, title='wxGUI', size=(640,480))
        self.panel = wx.Panel(self.frame, -1)
        self.image = wx.StaticBitmap(self.panel, size=self.panel.GetSize())
        #bmp = wx.Image(r'h:\1.jpg')
        #self.image.SetBitmap(bmp)

        #create menu
        self.menuBar = wx.MenuBar()
        self.menu = wx.Menu()
        self.menuNew = self.menu.Append(101, 'New')
        self.menuOpen = self.menu.Append(102, 'Open')
        self.menuSave = self.menu.Append(103, 'Save')
        self.menuSaveAs = self.menu.Append(104, 'Save As')
        self.menu.AppendSeparator()
        self.menuClose = self.menu.Append(105, 'Close')
        self.menuBar.Append(self.menu, '&File')
        self.menu = wx.Menu()
        self.menuCopy = self.menu.Append(201, 'Copy')
        self.menuCut = self.menu.Append(202, 'Cut')
        self.menuPaste = self.menu.Append(203, 'Paste')
        self.menuBar.Append(self.menu, '&Edit')
        self.menu = wx.Menu()
        self.menuAbout = self.menu.Append(301, 'About')
        self.menuBar.Append(self.menu, '&Help')
        self.frame.SetMenuBar(self.menuBar)
        wx.EVT_MENU(self, 101, self.OnNew)
        #or specify the event handler in the following way
        #self.Bind(wx.EVT_MENU, self.OnNew, self.menuNew)
        wx.EVT_MENU(self, 102, self.OnOpen)
        wx.EVT_MENU(self, 103, self.OnSave)
        wx.EVT_MENU(self, 104, self.OnSaveAs)
        wx.EVT_MENU(self, 105, self.OnClose)
        wx.EVT_MENU(self, 201, self.OnCopy)
        wx.EVT_MENU(self, 202, self.OnCut)
        wx.EVT_MENU(self, 203, self.OnPaste)
        wx.EVT_MENU(self, 301, self.OnAbout)

        #create popup menu        
        self.popupMenu = wx.Menu()
        self.popupCopy = self.popupMenu.Append(901, 'Copy')
        self.popupCut = self.popupMenu.Append(902, 'Cut')
        self.popupPaste = self.popupMenu.Append(903, 'Paste')
        wx.EVT_MENU(self, 901, self.OnCopy)
        wx.EVT_MENU(self, 902, self.OnCut)
        wx.EVT_MENU(self, 903, self.OnPaste)

        #Bind the popup menu with right click
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick)
        
        self.statusBar = self.frame.CreateStatusBar()

        self.toolbar = self.frame.CreateToolBar()
        self.toolbar.AddSimpleTool(9999,wx.Image('open.png',\
                                                 wx.BITMAP_TYPE_PNG).ConvertToBitmap(),\
                                   'Open', 'Click to Open a file')
        self.toolbar.Realize()
        wx.EVT_TOOL(self, 9999, self.OnOpen)
        
        self.frame.Show()
        return True
    
    def OnRClick(self, event):
        pos = (event.GetX(),event.GetY())
        self.panel.PopupMenu(self.popupMenu, pos)
    def OnNew(self, event):
        self.statusBar.SetStatusText('You clicked the New menu.')
    def OnOpen(self, event):
        self.statusBar.SetStatusText('You clicked the Open menu.')
    def OnSave(self, event):
        self.statusBar.SetStatusText('You clicked the Save menu.')
    def OnSaveAs(self, event):
        pass
    def OnClose(self, event):
        dlg = wx.MessageDialog(self.frame, 'Are you sure to close?', 'MessageDialog',
                               wx.CANCEL|wx.OK|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        if result == wx.ID_OK:
            dlg.Destroy()
            self.frame.Close(True)
    def OnCopy(self, event):
        pass
    def OnCut(self, event):
        pass
    def OnPaste(self, event):
        pass
    def OnAbout(self, event):
        pass
    
app = wxGUI()
app.MainLoop()
