# Nicolas Valdez Feb 10 2025
# NicolasValdezLeapYear
# Checks if a given year is a leap year
# Input(s)
# A year, integer, assumes Gregorian Calendar
# Output
# Number of days in February that year
# If a year is divisible by 100 and 400, it is a leap year.
# If a year is divisible by 100 but not 400, it is not a leap year.
# If a year is not divisible by 100 but divisible by 4, it is a leap year.
# Since it is safe

import pyinputplus as pyip

# Welcoming Statement
print("Checks if a given year is a leap year.")

# Required Info
year=pyip.inputInt("Enter a year: ",min=0)

# Leap Year Conditions
cond1=400
cond2=100
cond3=4

# Calculation
leap=False
if year%cond1==0:
        leap=True
elif year%cond2!=0 and year%cond3==0:
    leap=True

# Info Displayed to User
if leap==False:
    print(f"In the year {year}, February has 28 days.")
else:
    print(f"In the year {year}, February has 29 days.")

# Ending Note
print("Program Ends")