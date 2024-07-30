import wx

class MyPaintApp(wx.Frame):
    def __init__(self):
        super().__init__(None, title="WXPaint", size=(1200, 800), style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        
        self.Bind(wx.EVT_CHAR_HOOK, self.ControlZ)

        self.InitUI()
        self.Centre()
        self.Show()

        self.color = 'black'
        self.tcolor = 'black'
        self.width = 2
        self.pen_width = 2
        self.eraser_width = 10
        self.evar = False
        self.pen_size_png = 1
        self.eraser_size_jpeg = 1
        self.style_var = 1

    """V КРУТОЙ БЛОК V"""

    def on_undo(self):
        # Здесь можно реализовать логику отмены действия
        print("Отмена действия")

    def ControlZ(self, event):
        keycode = event.GetKeyCode()
        modifiers = event.GetModifiers()
        if modifiers == wx.MOD_CONTROL and keycode == ord('Z'):
            self.on_undo()
        else:
            event.Skip()

    """^ КРУТОЙ БЛОК ^"""

    def OnKeyDown(self, evt):
        keycode = evt.GetKeyCode()
        print(keycode)

    def InitUI(self):
        self.panel = wx.Panel(self)

        self.panel.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.panel.Bind(wx.EVT_MOTION, self.OnMouseMotion)
        self.panel.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.panel.Bind(wx.EVT_LEAVE_WINDOW, self.OnMouseLeave) #EVT_LEAVE_WINDOW - при выходе из окна; EVT_ENTER_WINDOW - при выходе в окно

        self.SetBackgroundColour("gray")
        self.drawing = False
        self.last_pos = (0, 0)
        self.current_pos = (0, 0)
        self.SetSize((1200, 700))

    def OnMouseDown(self, event):
        self.drawing = True
        self.current_pos = event.GetPosition()

    def OnMouseMotion(self, event):
        if self.drawing:
            dc = wx.ClientDC(self.panel)
            dc.SetPen(wx.Pen(self.color, self.width)) #, wx.PENSTYLE_SOLID
            dc.SetFont(wx.Font(self.width, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT))
            self.last_pos = self.current_pos
            self.current_pos = event.GetPosition()
            if self.style_var == 1:
                dc.DrawLine(self.last_pos[0], self.last_pos[1], self.current_pos[0], self.current_pos[1])
            if self.style_var == 2:
                dc.DrawPoint(self.current_pos[0], self.current_pos[1])
            if self.style_var == 3:
                dc.DrawArc(self.last_pos[0], self.last_pos[1], self.current_pos[0], self.current_pos[1], self.current_pos[0], self.current_pos[1])
            if self.style_var == 4:
                dc.SetTextForeground(self.color)
                dc.DrawRotatedText(str(self.current_pos[0] - self.current_pos[1]), self.current_pos[0], self.current_pos[1], self.current_pos[1]-self.current_pos[0])
            
    def OnMouseUp(self, event):
        if self.drawing:
            self.drawing = False

    def OnMouseLeave(self, event):
        pass #self.drawing = False

def main():
    app = wx.App()
    MyPaintApp().SetIcon(wx.Icon('clear_all.png'))
    app.MainLoop()

main()