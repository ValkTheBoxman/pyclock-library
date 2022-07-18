import time
from os import *
from tkinter import *
from datetime import datetime, timedelta
from pytz import timezone
from tzlocal import get_localzone

version = "0.4"
FEversion = "2.0"

#holds every function
class pyclock:
    def __init__(self) -> None: ...

    def vp(self):
        if self == 0:
            print("pyclock version:",version)
        if self == 1:
            print("pyclock version:",version)
            print("FE version: ",FEversion)


    #copied off google
    def showDigitalClock() -> None:
        def timing():
            #display current hour,minute,seconds
            current_time = time.strftime("%H : %M : %S")
            #configure the clock
            clock.config(text=current_time)
            #clock will change after every 200 microseconds
            clock.after(200,timing)
 
        #Create a variable that will store our tkinter window
        root=Tk()
        #define size of the window
        root.geometry("600x300")
        #create a variable clock and store label
        #First label will show time, second label will show hour:minute:second, third label will show the top digital clock
        clock=Label(root,font=("times",60,"bold"),bg="cyan")
        clock.grid(row=2,column=2,pady=25,padx=100)
        timing()
        
        #create a variable for digital clock
        digital=Label(root,text="pyclock digital clock",font="times 24 bold")
        digital.grid(row=0,column=2)
        
        nota=Label(root,text="hours        minutes        seconds",font="times 15 bold")
        nota.grid(row=3,column=2)
        
        root.mainloop()
 ###################################################################
    
    def printTime():
        current_time = time.strftime("Year: %Y, Month: %m, Day: %d, Hour: %H, Minute: %M, Second: %S.")
        print(current_time)

    def printTimezone():
        format = "%Y-%m-%d %H:%M:%S %Z%z"
        # prints current utc time
        now_utc = datetime.now(timezone('UTC'))
        print("UTC Timezone: ",now_utc.strftime(format))
        # convert to local time zone
        now_local = now_utc.astimezone(get_localzone())
        print("Your Timezone: ",now_local.strftime(format))

    #holds counters    
    class count:
        def __init__(self) -> None: ...
        
        def countUp(x):
            number = 0
            for i in range(x):
                number += 1
                time.sleep(1)
                print(number)

        def countDown1Num(x,y):
            number = x 
            for i in range(y):
                number -= 1
                time.sleep(1)
                print(number)

        def countDown(x):
            number = x 
            for i in range(number):
               number -= 1
               time.sleep(1)
               print(number) 


    #holds events
    class events:
        def __init__(self) -> None: ...

        def eventOnTime(hour,minute,msg):
            timeHour = time.strftime("%H")
            timeMin = time.strftime("%M")
            print("current time:",timeHour,":",timeMin)
            print("selected time:",hour,":",minute)
            if(hour == timeHour, minute == timeMin):
                print(msg)
            else:
                print("time event conditions not met")

        def eventOnDate(month,date,msg):
            timeHour = time.strftime("%H")
            timeMin = time.strftime("%M")
            print("current time:",timeHour,":",timeMin)
            print("selected time:",month,":",date)
            if(month == timeHour, date == timeMin):
                print(msg)
            else:
                print("date event conditions not met")

        
