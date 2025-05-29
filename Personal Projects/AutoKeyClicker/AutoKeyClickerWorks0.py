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
import pygame as pg
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

# Create millisecond label
msTxt='Milliseconds'
msLabel=Label(root,text=msTxt)

# Create second label
secTxt='Seconds'
secLabel=Label(root,text=secTxt)

# Create minute label
minTxt='Minutes'
minLabel=Label(root,text=minTxt)

# Create millisecond spinbox
msMin=0
msMax=9999
msWidth=5
msPadX=35
msPadY=10
msSpin=Spinbox(root,
               from_=msMin,
               to=msMax,
               width=msWidth)

# Create second spinbox
secMin=0
secMax=9999
secWidth=5
secPadX=35
secPadY=10
secSpin=Spinbox(root,
                from_=secMin,
                to=secMax,
                width=secWidth)

# Create minute spinbox
minMin=0
minMax=9999
minWidth=5
minPadX=35
minPadY=10
minSpin=Spinbox(root,
                from_=minMin,
                to=minMax,
                width=minWidth)

# Get time in milliseconds inbetween key activations
def intervalLength(msSpin,secSpin,minSpin):
    '''Get time in milliseconds inbetween key activations.'''
    msVal=int(msSpin.get())
    secVal=int(secSpin.get())
    minVal=int(minSpin.get())
    msPerSec=1000
    msPerMin=60*msPerSec
    length=msVal+(secVal*msPerSec)+(minVal*msPerMin)
    print(f'Interval length: {length}ms')
    length=int(length)
    return(length)

def bindKey():
    '''Bind a hotkey to the start button'''
    tempTxt=f'You clicked {hkTxt}.'
    print(tempTxt)

# Activate the autoclicker functionality
def autoClick(length):
    '''Activate the autoclicker functionality.'''
    clicks=5 # Temporary 5 clicks until I make the user able
    # to start and stop when they want
    pause=1000 # Temporary initial hold before clicking begins   
    pg.time.wait(pause)
    for i in range(clicks):
        mouse.click('left')
        print(f'Click {i}')
        pg.time.wait(length)
    
# Create start button
startTxt='Start'
startHeight=3
startWidth=25
startCommand=lambda:autoClick(intervalLength(msSpin,secSpin,minSpin))
startButton=Button(root,
                   text=startTxt,
                   height=startHeight,
                   width=startWidth,
                   command=startCommand)

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

startButton.pack()

msLabel.pack()
msSpin.pack(padx=msPadX,
            pady=msPadY)

secLabel.pack()
secSpin.pack(padx=secPadX,
             pady=secPadY)

minLabel.pack()
minSpin.pack(padx=minPadX,
             pady=minPadY)

hkButton.pack()

# Run GUI
root.mainloop()

# Ending Note
print('Program Ends')