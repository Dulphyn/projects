# Nicolas Valdez Fri Feb 21 13:44:24 2025
# NicolasValdezCookout
# Calculates number of hot dog and hot dog bun packages needed for a cookout
# Input(s)
# Number of people, int
# Number of hot dogs per person, int
# Number of hot dogs per hot dog package, int
# Number of hot dog buns per bun package, int
# Output
# Size of hot dog package
# Size of hot dog bun package
# Minimum number of packages of hot dogs required
# Minimum number of packages of hot dog buns required
# Number of hot dogs that will be left over
# Number of hot dog buns that will be left over

import pyinputplus as pyip # Gets inputs in proper format from user
import math # Calculates ceiling of needed variables
import tabulate as tabl # Tabulate user display information

# Welcoming Statement
print("Calculates number of hot dog and hot dog bun packages needed for a cookout.")

# Required Info
people=pyip.inputInt("Number of people coming to the cookout: ")
perPerson=pyip.inputInt("Number of hot dogs per person: ")
dogsPerPackage=pyip.inputInt("Number of hot dogs per hot dog package: ")
bunsPerPackage=pyip.inputInt("Number of hot dog buns per hot dog bun package: ")

# Calculation
neededDogs=people*perPerson
totalDogsPackages=math.ceil(neededDogs/dogsPerPackage)
totalBunsPackages=math.ceil(neededDogs/bunsPerPackage)
totalDogs=dogsPerPackage*totalDogsPackages
totalBuns=bunsPerPackage*totalBunsPackages
dogsLeftover=totalDogs%neededDogs
bunsLeftover=totalBuns%neededDogs

# Displayed to User
table=[["Hot Dogs",dogsPerPackage,totalDogsPackages,dogsLeftover],["Hot Dog Buns",bunsPerPackage,totalBunsPackages,bunsLeftover]]
print(tabl.tabulate(table,headers=["Item","Size of Package","Number of Packages","Leftovers"],tablefmt="grid"))

# Ending Note
print("Program Ends")