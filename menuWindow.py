import wx

class Menu(wx.Frame):
    def __init__(self,parent,title):
        self.Mode = None


        wx.Frame.__init__(self,parent,title=title)
        self.SetSize(400,200)
        self.panel = wx.Panel(self,wx.ID_ANY)
        self.NewStudy_Btn = wx.Button(self.panel,-1,label="New",pos=(280,20))
        self.NewStudy_Btn.SetSize(100,50)
        self.NewStudy_Btn.Bind(wx.EVT_LEFT_DOWN,self.NewStudy_Clicked)
        self.Load_Btn = wx.Button(self.panel,-1,label="Load",pos=(280,50))
        self.Load_Btn.SetSize(100,50)
        self.Load_Btn.Bind(wx.EVT_LEFT_DOWN,self.Load_Clicked)
    def NewStudy_Clicked(self,event):
        self.Mode = "New"
        self.Close()
    def Load_Clicked(self,event):
        self.Mode = "Load"
        self.Close()       
    def Get_Mode_Value(self):
        
        return self.Mode