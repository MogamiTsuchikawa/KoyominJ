import wx
class VN_window(wx.Frame):
    def __init__(self,parent,title,Mode):
        wx.Frame.__init__(self,parent,title=title)
        self.SetSize(1280,720)
        self.panel = wx.Panel(self,wx.ID_ANY)
        self.Text = wx.StaticText(self.panel,-1,label=Mode)