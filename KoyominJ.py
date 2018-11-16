import mainWindow,menuWindow
import wx

Mode = None
app = wx.App(False)
M_frame = menuWindow.Menu(None,"Menu")
M_frame.Show()
app.MainLoop()
Mode = menuWindow.Menu.Get_Mode_Value(M_frame)
if Mode is not None:
    VN_frame = mainWindow.VN_window(None,"TEST",Mode)
    VN_frame.Show()
    app.MainLoop()