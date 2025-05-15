# Nicolas Valdez Fri Apr 11 15:08:49 2025
# NicolasValdezPaint
# Calculates time and money cost information of a paint job
# Input(s)
# W, Square feet of wall space to be painted
# P, Price of the paint per gallon
# Output
# N, Number of gallons of paint required, rounded up to next full gallon
# H, Hours of labor required
# C, Cost of the paint
# L, Labor charges
# T, Total cost of the paint job
# Data table saved to new file
# Formulas:
# N = ceil(W / Square feet of wall space painted per gallon used)
# H = W / Square feet of wall space painted per hour worked
# C = N * P
# L = (Hourly wage * H)
# T = C + L

import pyinputplus as pyip
import math
import tabulate as tabl

# Export file name
fileName="JobEstimate.txt"

# Welcoming Statement
print("Calculates time and money cost information of a paint job. Saves estimate to file.")


# Calculations
def estimator(wallArea,paintCostPerGal,wallPerGal,wallPerHour,wage):
    gallons=math.ceil(wallArea/wallPerGal)
    hours=wallArea/wallPerHour
    totalPaintCost=gallons*paintCostPerGal
    totalLaborCost=wage*hours
    totalCost=totalPaintCost+totalLaborCost
    return(gallons,hours,totalPaintCost,totalLaborCost,totalCost)

def main():
    # Assumptions
    wallPerGal=122
    wallPerHour=122/8
    wage=47

    # Job Information
    wallArea=pyip.inputFloat("Square feet of wall to be painted: ",greaterThan=0)
    paintCostPerGal=pyip.inputFloat("Price of paint per gallon ($): ")
    
    # Form calculations into a table
    table=[estimator(wallArea,paintCostPerGal,wallPerGal,wallPerHour,wage)]
    header=("Gallon(s) of paint","Hour(s) of labor","Cost of paint ($)","Labor charges ($)","Total Cost ($)")
    decimals=(None,".1f",".2f",".2f",".2f")
    print("\n",tabl.tabulate(table,headers=header,floatfmt=decimals))
    
    # Write table to file
    with open(fileName,"w") as infile:
        infile.write(tabl.tabulate(table,headers=header,floatfmt=(None,".1f",".2f",".2f",".2f")))
    print(f"\nTable saved as {fileName}\n")
    
    # Ask to restart program
    choice=["Yes","No"]
    prompt="Make another estimate?\n"
    loop=pyip.inputMenu(choice,prompt,numbered=True)
    return(loop,choice)

# Loop program
restart=main()
while restart[0]==restart[1][0]:
    restart=main()
# Ending Note
print("Program Ends")