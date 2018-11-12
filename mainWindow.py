import wx
class VN_window(wx.Frame):
    def __init__(self,parent,title,Mode):
        wx.Frame.__init__(self,parent,title=title)
        self.SetSize(1280,720)
        self.panel = wx.Panel(self,wx.ID_ANY)
        self.Text = wx.StaticText(self.panel,-1,label=Mode)
        self.img_TextBlock = wx.Image("res/TextBlock_Green.png")
        self.bt_TextBlock = self.img_TextBlock.ConvertToBitmap()
        self.st_bt_TextBlock = wx.StaticBitmap(self.panel,-1,self.bt_TextBlock,pos=(0,480))
        self.name_text = wx.StaticText(self.panel,-1,label="[NAME]",pos=(30,500))
        name_text_font = wx.Font(35, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.name_text.SetFont(name_text_font)
        self.serihu_text = wx.StaticText(self.panel,-1,label="sample text...TEXT...TEXT...TEXT",pos=(100,560))
        serihu_text_font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.serihu_text.SetFont(serihu_text_font)
        #print(self.name_text.GetFont)