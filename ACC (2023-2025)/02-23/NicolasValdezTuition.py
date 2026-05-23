# Nicolas Valdez Fri Feb 21 15:36:05 2025
# NicolasValdezTuition
# Calculates the projected tuition by year for a certain number of years
# Input(s)
# P, Starting tuition cost, positive int
# N, Times per year tuition increases, positive int
# r, Percent increase in tuition, positive float
# t, Total number of years for tuition cost increase, positive int
# Output
# Table of the tuition cost by year for the designated number of years
# Tuition (nth year) = P * (1 + ((r / 100)/ N)) ** (N * (nth year while n<=t))

import pyinputplus as pyip

# Welcoming Statement
print("Calculates the projected tuition by year for a certain number of years.")

# Required Info and Restrictions
pMin=0
nMin=0
rMin=0
tMin=0

p=pyip.inputFloat("Starting tuition cost in US Dollars: ",greaterThan=pMin)
n=pyip.inputFloat("Number of times tuition increases per year: ",greaterThan=nMin)
r=pyip.inputFloat("By what percent does tuition increase each time? ",greaterThan=rMin)
t=pyip.inputInt("Total number of years to project tuition for: ",greaterThan=tMin)

# Calculation Setup and Display Setup
indStart=0
indEnd=t+1
increase=1+((r/100)/n) # Tuition increase rate
tuitionDec=2 # Decides how many decimal spots for tuition
tuitionWidth=16 # Reserves character spots for tuition decimal numbers
yearsDec=0 # Decides how many decimal spots for years
yearsWidth=3 # Reserves character spots for years decimal numbers

# Calculation and Info Displayed to User
print("Year   # | Tuition Cost ($)")
print("---------------------------")
for i in range(indStart,indEnd):
    tuition=p
    tuition*=increase**(n*i)
    print(f"Year {i:{yearsWidth}.{yearsDec}f} | {tuition:{tuitionWidth}.{tuitionDec}f}")

# Ending Note
print("Program Ends")