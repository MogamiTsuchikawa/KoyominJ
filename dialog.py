import wx
class ErorrDialog(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title)
        self.SetSize(1280,720)
        self.panel = wx.Panel(self,wx.ID_ANY)
