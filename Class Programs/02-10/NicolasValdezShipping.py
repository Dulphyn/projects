# Nicolas Valdez Feb 10 2025
# NicolasValdezShipping
# Calculates shipping charges for a package
# Input(s)
# Weight of a package, pounds (lb), float
# Output
# Shipping charges for the package
# Shipping Cost = Rate * Weight

import pyinputplus as pyip

# Welcoming Statement
print("Calculates shipping charges in US Dollars for a package by the weight of the package in pounds.")

# Rate Table
lowest=2
low=6
high=10

lowestRate=1.5
lowRate=3.0
highRate=4.0
highestRate=4.75

# Required Info
weight=pyip.inputFloat("How many pounds does the package weigh? ",min=0)

# Calculation
if weight<=lowest:
    cost=weight*lowestRate
elif weight<=low:
    cost=weight*lowRate
elif weight<=high:
    cost=weight*highRate
else:
    cost=weight*highestRate

# Info Displayed to User
print(f"The shipping cost of the package is ${cost:.2f}.")

# Ending Note
print("Program Ends")