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

# import pyinputplus as pyip
# import numpy as np
# import keyboard as kb
import mouse
from tkinter import *
from threading import Thread
from time import sleep

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

# Start, stop, and hotkey button definitions
def intervalLength(msSpin,secSpin,minSpin):
    '''Get time in milliseconds inbetween key activations. 
    There is a minimum interval length.'''
    msVal=int(msSpin.get())
    secVal=int(secSpin.get())
    minVal=int(minSpin.get())
    secPerMs=1/1000
    secPerMin=60
    length=int(msVal*secPerMs)+secVal+(minVal*secPerMin)
    minLength=1000*secPerMs
    length=max(length,minLength)
    return(length)

def bindKey():
    '''Bind a hotkey to the start button'''
    tempTxt=f'You clicked {hkTxt}.'
    print(tempTxt)

def switch():
    '''Switches the state of the start button.'''
    if startButton['state']=='normal':
        startButton['state']='active'
        stopButton['state']='normal'
    else:
        startButton['state']=='disabled'
        
# Autoclicker functionality
def autoClick(length):
    '''Activate the autoclicker functionality.'''
    print(f'Interval length: {length}sec')
    mouse.click('left')
    print('Click')
    sleep(length)
    

def startAutoClick(length):
    thread=Thread(target=autoClick(length))
    thread.start()
    thread.join()
    
# Create start and stop button frame
stFrame=Frame(root)

# Create start button
startTxt='Start'
startHeight=3
startWidth=25
length=intervalLength(msSpin,secSpin,minSpin)
startCommand=lambda:startAutoClick(length)
startButton=Button(stFrame,
                   text=startTxt,
                   height=startHeight,
                   width=startWidth,
                   command=startCommand)

# Create stop button
stopTxt='Stop'
stopHeight=3
stopWidth=25
stopCommand=switch
stopState='disabled'
stopButton=Button(stFrame,
                   text=stopTxt,
                   height=stopHeight,
                   width=stopWidth,
                   command=stopCommand,
                   state=stopState)

def packStartStop():
    stFrame.pack()
    startButton.pack(side=LEFT)
    stopButton.pack(side=LEFT)
    
# Create set hotkey button
hkTxt='Set hotkey'
hkHeight=3
hkWidth=25
hkCommand=bindKey
hkButton=Button(root,
                text=hkTxt,
                height=hkHeight,
                width=hkWidth,
                command=hkCommand)

# Place widgets
header.pack()

packStartStop()

hkButton.pack()

packAllSpins(msLPadX,msPadX,secLPadX,secPadX,minLPadX,minPadX)

# Run GUI
root.mainloop()

# Ending Note
print('Program Ends')