import time
from os import *
from tkinter import *

version = "0.2"

#holds every function
class pyclock:
    def __init__(self) -> None: ...

    def vp() -> None:
        print("pyclock version:",version)
    
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
        clock=Label(root,font=("times",60,"bold"),bg="blue")
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

        def countDown(): ...

            

    #holds events
    class events:
        def __init__(self) -> None: ...

        def eventOnTime(): ...

        def eventOnDate(): ...

        