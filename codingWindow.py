import wx
class codingWindow(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title)
        self.SetSize(1200,600)
        self.panel = wx.Panel(self,wx.ID_ANY)
        