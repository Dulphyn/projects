# Nicolas Valdez Thu Feb 27 17:50:41 2025
# NicolasValdezMar2
# Contains a function for temperature conversion, sum calculation,
# and a grapevine room calculator
# Input(s)
# Select a function
# Function specific input requests
# Output
# Functions list
# Function specific output

import pyinputplus as pyip # Require good inputs
import math # Special math function
import tabulate as tabl # Display a table

# Welcoming Statement
print("Select a program to use:")



# Converts temperature across units
# Input(s)
# Pick conversion direction from a menu
# Temperature to convert of desired unit, float
# Output
# Converted temperature
# Celsius = (Temperature - 32) * (5 / 9)
# Fahrenheit = (Temperature * (5 / 9)) + 32

def tempConvert(conversion,temperature):
    convList=["Fahrenheit to Celsius", "Celsius to Fahrenheit"]
    if conversion==convList[0]:
        convTemp=(temperature-32)*(5/9)
    else:
        convTemp=(temperature*(9/5))+32
    return(convTemp)

# Calculates the sum of a series
# Input(s)
# N, Chosen number, int
# N <= 50
# Output
# A summation for a chosen number
# Summation = Sum from the range n = 1 to (Chosen Number) of
# n / (Chosen Number + 1 - n)

def seriesSum(bigNumber):
    sumStart=1
    summation=0
    sumEnd=bigNumber+1
    for i in range(sumStart,sumEnd):
        summation+=(i/(sumEnd-i))
    return(summation)

# Calculates how many plants that are able to be grown per row
# Input(s)
# R, the length of the row, in feet, float
# E, the amount of space, in feet, used by an end-post assembly, float
# S, the space, in feet, between plants, float
# R > 0
# E > 0
# E < R / 2
# S > 0
# S <= R - (2 * E)
# Output
# V, the number of plants that will fit in the row
# V = (R - (2 * E)) / S

def grapevines(R,E,S):
    L=R-(2*E)
    numberPlants=math.floor(L/S)
    return(numberPlants)

# Main program
def main():
    # Functions Table Setup
    func1Desc="Converts temperature to a different unit"
    func2Desc="Calculates the sum of a specific series"
    func3Desc="Calculates how many plants that are able to be grown per row"
    funcDesc=[func1Desc,func2Desc,func3Desc]
    
    func1="tempConvert"
    func2="seriesSum"
    func3="grapevines"
    functions=[func1,func2,func3]
    
    column1="Program Purpose"
    column2="Program Name"
    header=[column1,column2]
    
    form="grid"
    
    # Display Available Functions
    funcTable=[[funcDesc[0],functions[0]],[funcDesc[1],functions[1]],[funcDesc[2],functions[2]]]
    print(tabl.tabulate(funcTable,headers=header,tablefmt=form))
    
    # User Selects Program
    programResponse=pyip.inputMenu(functions,numbered=True)
    
    # Function Inputs and Call
    if programResponse==functions[0]:
        print("Convert between celsius and fahrenheit.")
        convList=["Fahrenheit to Celsius", "Celsius to Fahrenheit"]
        givenTempConv=pyip.inputMenu([convList[0],convList[1]],numbered=True)
        if givenTempConv==convList[0]:
            givenTemp=pyip.inputFloat("Temperature in Fahrenheit: ")
        else:
            givenTemp=pyip.inputFloat("Temperature in Celsius: ")
        convertedTemperature=tempConvert(givenTempConv,givenTemp)
    elif programResponse==functions[1]:
        print("Calculates a sum for a given number.")
        minBigNumber=1
        maxBigNumber=50
        givenNumber=pyip.inputInt("Give a big number: ",min=minBigNumber,max=maxBigNumber)
        summedNumber=seriesSum(givenNumber)
    else:
        print("Calculates how many plants that are able to be grown per row.")
        Rlow=0 # Minimum length of R
        givenR=pyip.inputFloat("The length of the row, in feet: ",greaterThan=Rlow)
        
        Elow=0 # Minimum length of E
        Ehigh=givenR/2 # Maximum length of E
        givenE=pyip.inputFloat("The amount of space, in feet, used by an end-post assembly: ",greaterThan=Elow,lessThan=Ehigh)
        
        Slow=0 # Minimum length of S
        Shigh=givenR-(2*givenE) # Maximum length of S
        givenS=pyip.inputFloat("The space, in feet, between plants: ",greaterThan=Slow,max=Shigh)
        
        plantsInRow=grapevines(givenR,givenE,givenS)
        
    # Function Outputs
    if programResponse==functions[0]:
        tempDec=2 # Temperature Decimals
        if givenTempConv==convList[0]:
            print(f"The converted temperature is {convertedTemperature:.{tempDec}f}C")
        else:
            print(f"The converted temperature is {convertedTemperature:.{tempDec}f}F")
    elif programResponse==functions[1]:
        sumDec=4 # Sum Decimals    
        print(f"The result of the sum is {summedNumber:.{sumDec}f}")
    else:
        print(f"The number of plants that can fit in the row is {plantsInRow}.")
    
# Start and loop program
main()
repeatList=["Continue","Exit"]
repeat=pyip.inputMenu([repeatList[0],repeatList[1]],numbered=True)
while repeat==repeatList[0]:
    main()
    repeat=pyip.inputMenu([repeatList[0],repeatList[1]],numbered=True)
    
# Ending Note
print("Program Ends")
