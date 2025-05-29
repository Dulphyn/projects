# Nicolas Valdez Sat May 17 17:42:40 2025
# AutoKeyClicker
# Allow user to toggle the automation of the 
# clicking of a desired keyboard or mouse key
# Input(s)
# Desired key to be automated
# Period or frequency of key clicks
# Output
# A GUI for easy user input
# Autoclicking

import time
import threading
from pynput.mouse import Button as pynBtn
from pynput.mouse import Controller
from pynput.keyboard import Listener, KeyCode
from pynput.keyboard import Controller
from tkinter import *


# Welcoming Statement
welcome='Toggle the automation of the clicking of a desired keyboard key.'
print(welcome)

# Create main window
root=Tk()
title='Auto Clicker'
root.title(title)
rootWidth=450
rootHeight=370
rootDim=f'{rootWidth}x{rootHeight}'
root.geometry(rootDim)

# Create welcome label
headerTxt=welcome
header=Label(root,text=headerTxt)

# Create spinboxes frame
msFrame=Frame(root)
secFrame=Frame(root)
minFrame=Frame(root)

# Create millisecond label
msTxt='Milliseconds'
msLabel=Label(msFrame,text=msTxt)
msLPadX=0

# Create second label
secTxt='Seconds'
secLabel=Label(secFrame,text=secTxt)
secLPadX=0

# Create minute label
minTxt='Minutes'
minLabel=Label(minFrame,text=minTxt)
minLPadX=0

# Create millisecond spinbox
msMin=0
msMax=9999
msWidth=5
msPadX=30
msSpin=Spinbox(msFrame,
               from_=msMin,
               to=msMax,
               width=msWidth)

# Create second spinbox
secMin=0
secMax=9999
secWidth=5
secPadX=30
secSpin=Spinbox(secFrame,
                from_=secMin,
                to=secMax,
                width=secWidth)

# Create minute spinbox
minMin=0
minMax=9999
minWidth=5
minPadX=30
minSpin=Spinbox(minFrame,
                from_=minMin,
                to=minMax,
                width=minWidth)

# Commands

# Start Button
def intervalLength(msSpin,secSpin,minSpin):
    '''Get time in seconds inbetween key activations. 
    There is a minimum interval length.'''
    msVal=int(msSpin.get())
    secVal=int(secSpin.get())
    minVal=int(minSpin.get())
    secPerMs=1/1000
    secPerMin=60
    length=(msVal*secPerMs)+secVal+(minVal*secPerMin)
    minLength=50*secPerMs
    length=max(length,minLength)
    print(f'Interval length: {length}sec')
    return(length)

# Thank you @ https://www.geeksforgeeks.org/how-to-make-a-python-auto-clicker/
# for this next section of code slightly modified due to conflict with tkinter
# as well as some customization due to the GUI integration

# Config variables
d = intervalLength(msSpin,secSpin,minSpin)             # Delay between clicks
btn = pynBtn.left     # Mouse button to click

# Hotkeys
stChar='a'
start_key = KeyCode(char=stChar)  # Start/stop key
exChar='b'
exit_key = KeyCode(char=exChar)   # Exit key

class AutoClicker(threading.Thread):
    def __init__(self, d, btn):
        super().__init__()
        self.d = d
        self.btn = btn
        self.clicking = False
        self.active = True

    def start_click(self):
        self.clicking = True

    def stop_click(self):
        self.clicking = False

    def exit(self):
        self.stop_click()
        self.active = False

    def run(self):
        while self.active:
            while self.clicking:
                mouse.click(self.btn)
                time.sleep(self.d)

# instance of keyboard controller is created
keyboard=Controller()

def stHotkey(stChar):
    keyboard.press(stChar)
    keyboard.release(stChar)
    
# instance of mouse controller is created
mouse = Controller()

# Create and start the auto-clicker thread
clicker = AutoClicker(d, btn)
clicker.start()

def on_press(k):
    if k == start_key:
        if clicker.clicking:
            clicker.stop_click()
            print("[INFO] Clicker Stopped.")
        else:
            clicker.start_click()
            print("[INFO] Clicker Started.")
    elif k == exit_key:
        clicker.exit()
        print("[INFO] Exiting.")
        return False  # Stop listener
    
with Listener(on_press=on_press) as listener:
    listener.join()

        
# Stop Button

# Set Hotkey

# Create start and stop button frame
stFrame=Frame(root)

# Create start button
startTxt='Start'
startHeight=3
startWidth=25
startCommand=lambda:stHotkey(stChar)
startButton=Button(stFrame,
                   text=startTxt,
                   height=startHeight,
                   width=startWidth,
                   command=startCommand)

# Create stop button
stopTxt='Stop'
stopHeight=3
stopWidth=25
stopCommand=None
stopState='disabled'
stopButton=Button(stFrame,
                   text=stopTxt,
                   height=stopHeight,
                   width=stopWidth,
                   command=stopCommand,
                   state=stopState)

# Create set hotkey button
hkTxt='Set hotkey'
hkHeight=3
hkWidth=25
hkCommand=None
hkButton=Button(root,
                text=hkTxt,
                height=hkHeight,
                width=hkWidth,
                command=hkCommand)

# Spinbox packing
def msPack(msLPadX,msPadx):
    '''Pack millisecond frame, label, and spinbox.'''
    msFrame.pack(side=LEFT)
    msLabel.pack(padx=msLPadX,side=TOP)
    msSpin.pack(padx=msPadX,side=LEFT)
    
def secPack(secLPadX,secPadX):
    '''Pack second frame, label, and spinbox.'''
    secFrame.pack(side=LEFT)
    secLabel.pack(padx=secLPadX,side=TOP)
    secSpin.pack(padx=secPadX,side=LEFT)
    
def minPack(minLPadX,minPadX):
    '''Pack minute frame, label, and spinbox.'''
    minFrame.pack(side=LEFT)
    minLabel.pack(padx=minLPadX,side=TOP)
    minSpin.pack(padx=minPadX,side=LEFT)
    
def packAllSpins(msLPadX,msPadX,secLPadX,secPadX,minLPadX,minPadX):
    '''Packs the millisecond, second, and minute spinbox/labels.'''
    msPack(msLPadX,msPadX)
    secPack(secLPadX,secPadX)
    minPack(minLPadX,minPadX)
    
# Start/Stop packing
def packStartStop():
    stFrame.pack()
    startButton.pack(side=LEFT)
    stopButton.pack(side=LEFT)
    
# Place widgets
header.pack()

packStartStop()

hkButton.pack()

packAllSpins(msLPadX,msPadX,secLPadX,secPadX,minLPadX,minPadX)

# Run GUI
root.mainloop()

# Ending Note
print('Program Ends')