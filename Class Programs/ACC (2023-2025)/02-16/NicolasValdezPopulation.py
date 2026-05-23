# Nicolas Valdez Fri Feb 14 13:51:58 2025
# NicolasValdezPopulation
# Predicts the size of a population of organisms after a certain number of days
# of population growth.
# Input(s)
# s, Starting number of organisms, positive int
# r, Average daily percent increase in population, positive float
# t, Total number of days for population growth, positive int
# Output
# Table of the population per day
# Population = s*((1+(r/100))**(nth day while n<=t))

import pyinputplus as pyip

# Welcoming Statement
print("Predicts the approximate size of a population of organisms after a certain number of days of population growth.")

# Required Info
popMin=1
rateMin=0
daysMin=1
daysMax=21

s=pyip.inputInt("Starting population: ",min=popMin)
r=pyip.inputFloat("Average daily percent increase in population: ",min=rateMin)
t=pyip.inputInt("Total number of days for population growth: ",min=daysMin,max=daysMax)

# Calculation and Info Displayed to User Setup Variables
indStart=0
indEnd=t+1
rConv=1+(r/100) # Conversion factor for percent rate to decimal form
popDec=4 # Decides how many decimal spots for population
popWidth=18 # Reserves character spots for population decimal numbers
daysDec=0 # Decides how many decimal spots for days
daysWidth=2 # Reserves character spots for days decimal numbers

# Calculation and Info Displayed to User
print("Day  # | Approx. Population")
print("---------------------------")
for i in range(indStart,indEnd):
    pop=s
    pop*=rConv**i
    print(f"Day {i:{daysWidth}.{daysDec}f} | {pop:{popWidth}.{popDec}f}")
    
# Ending Note
print("Program Ends")