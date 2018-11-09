import wx

class VN_window(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title)
        self.SetSize(1280,720)
        panel = wx.Panel(self,wx.ID_ANY)