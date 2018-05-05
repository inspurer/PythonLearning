import wx

class TreeCtrlFrame(wx.Frame):
    def __init__(self, superion):
        wx.Frame.__init__(self, parent=superion, title='TreeCtrl demo', size=(300,400))
        panel = wx.Panel(self)
        self.tree = wx.TreeCtrl(parent=panel, pos=(5,5), size=(120,200))
        self.inputString = wx.TextCtrl(parent=panel, pos=(150,10))
        self.buttonAddChild = wx.Button(parent=panel, label='AddChild', pos=(150,90))
        self.Bind(wx.EVT_BUTTON, self.OnButtonAddChild, self.buttonAddChild)
        self.buttonDeleteNode = wx.Button(parent=panel, label='DeleteNode', pos=(150,120))
        self.Bind(wx.EVT_BUTTON, self.OnButtonDeleteNode, self.buttonDeleteNode)
        self.buttonAddRoot = wx.Button(parent=panel, label='AddRoot', pos=(150,150))
        self.Bind(wx.EVT_BUTTON, self.OnButtonAddRoot, self.buttonAddRoot)

    def OnButtonAddChild(self, event):
        itemSelected = self.tree.GetSelection()
        if not itemSelected:
            wx.MessageBox('Select a Node first.')
            return
        itemString = self.inputString.GetValue()
        self.tree.AppendItem(itemSelected, itemString)
        

    def OnButtonDeleteNode(self, event):
        itemSelected = self.tree.GetSelection()
        if not itemSelected:
            wx.MessageBox('Select a Node first.')
            return
        self.tree.Delete(itemSelected)
    def OnButtonAddRoot(self, event):
        rootItem = self.tree.GetRootItem()
        if rootItem:
            wx.MessageBox('The tree has already a root.')
        else:
            itemString = self.inputString.GetValue()
            self.tree.AddRoot(itemString)
        
if __name__ == '__main__':
    app = wx.App()
    frame = TreeCtrlFrame(None)
    frame.Show()
    app.MainLoop()
