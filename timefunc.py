import datetime
import wx
import pandas as pd



#run this if a ZID swiped today was swiped again
def GetTimeDif(zid):
    #zid = the zid passed into the function
    #ZID is the ZID colom pulled from the file using pandas
    df = pd.read_csv("test.csv")
    current_time = datetime.datetime.now().strftime("%H:%M %A")

    
    #after student swipes in a second time set the "out time" of that specific student to the current time
    df.loc[df["ZID"] == zid , "Time out"] =  current_time
    
    #look in the file for when he swiped in 
    

    

      
    df.to_csv('test.csv', index=False)
    
    
    #print(ZID)
    #substract 
    
    #print(current_time)



    

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
    #ZID to be pulled from swipe
    GetTimeDif("Z1980556")
