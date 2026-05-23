# Nicolas Valdez Fri Feb 21 14:44:14 2025
# NicolasValdezGrapevines
# Calculates how many plants that are able to be grown per row
# Input(s)
# R, the length of the row, in feet, float
# E, the amount of space, in feet, used by an end-post assembly, float
# S, the space, in feet, between plants, float
# S<=R
# 
# Output
# V, the number of plants that will fit in the row
# V = (R - (2 * E))/S

import pyinputplus as pyip # Gets inputs in proper format and allows for restrictions
import math # Calculates floor of needed variable

# Welcoming Statement
print("Calculates how many plants that are able to be grown per row.")

# Required Info and Restrictions
Rlow=0 # Minimum length of R
R=pyip.inputFloat("The length of the row, in feet: ",greaterThan=Rlow)

Elow=0 # Minimum length of E
Ehigh=R/2 # Maximum length of E
E=pyip.inputFloat("The amount of space, in feet, used by an end-post assembly: ",greaterThan=Elow,lessThan=Ehigh)

Shigh=R-(2*E) # Maximum length of S
S=pyip.inputFloat("The space, in feet, between plants: ",max=Shigh)

# Setup Variables
L=R-(2*E)

# Calculation
V=math.floor(L/S)

# Displayed Info
print(f"There is room for {V} plant(s) in the row.")

# Ending Note
print("Program Ends") 

