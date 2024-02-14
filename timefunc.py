#import datetime
from datetime import datetime
import wx
import pandas as pd

# main function
def main():
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
    #ZID to be pulled from swipe


    #Need to create control structure such that :
    enterDate("Z1980556") #runs omly on first swipe
    enterStartTime("Z1980556") # runs only on first swipe
    GetTimeDif("Z1980556")  #runs only on second swipe


def enterDate(zid):
    df = pd.read_csv("test.csv")
    current_date = datetime.now().date()
    df.loc[df["ZID"] == zid , "Date"] = current_date
    df.to_csv('test.csv', index=False)


def enterStartTime(zid):
    df = pd.read_csv("test.csv")
    #pulling current time from local machine
    CurrentTime = datetime.now().strftime("%H:%M")
    #converting to datetime obj
    CurrentTime = datetime.strptime(CurrentTime, "%H:%M").time()
    

    df.loc[df["ZID"] == zid , "Time in"] =  CurrentTime.strftime("%H:%M")
    df.to_csv('test.csv', index=False)


    


#run this if a ZID swiped today was swiped again
def GetTimeDif(zid):
    #zid = the zid passed into the function
    #ZID is the header name for the colomn that has all the ZID's
    df = pd.read_csv("test.csv")



    #pulling current time from local machine
    CurrentTime = datetime.now().strftime("%H:%M")
    
    #converting to datetime obj
    CurrentTime = datetime.strptime(CurrentTime, "%H:%M").time()
    

    
    #after student swipes in a second time set the "out time" of that specific student to the current time
    df.loc[df["ZID"] == zid , "Time out"] =  CurrentTime.strftime("%H:%M")#(to lose the seconds attribute )

    TimeIn = df.loc[df["ZID"] == zid, "Time in"].iloc[0] #pulling 'time in' from the  data frame

    TimeIn = datetime.strptime(TimeIn, "%H:%M").time() #converting to datetime obj

   

    #had to add the day to each time stamp to get the substract working, idk why...
    TimeIn = datetime.combine(datetime.today(), TimeIn)
    CurrentTime = datetime.combine(datetime.today(), CurrentTime)


    #finding the time difference 
    TimeDiff = CurrentTime - TimeIn

    
    #slap time diff into the dataframe
    df.loc[df["ZID"] == zid , "Time Stayed For"] =  TimeDiff#.strftime("%H:%M")
    

    #save dataframe into file
    df.to_csv('test.csv', index=False)
    
    


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