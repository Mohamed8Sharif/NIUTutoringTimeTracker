import datetime
import wx
import pandas as pd

# main function
def main():
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
    #ZID to be pulled from swipe
    GetTimeDif("Z1980556")


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

# GUI for the application
class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)        
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.CENTER, 5)        
        my_btn = wx.Button(panel, label='Press Me')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        panel.SetSizer(my_sizer)        
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("Error I guess")
        else:
            GetTimeDif(value)


# Calls main function
if __name__ == '__main__':
    main()