import datetime
import wx



#run this if a ZID swiped today was swiped again
def GetTimeDif(ZID):
    #look in the file for when he swiped in 
    #substract 
    current_time = datetime.datetime.now()
    print(current_time)



    

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)

        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        my_btn = wx.Button(panel, label='Press Me', pos=(5, 55))

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
