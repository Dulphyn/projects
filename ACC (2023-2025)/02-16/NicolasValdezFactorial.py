# Nicolas Valdez Fri Feb 14 13:24:26 2025
# NicolasValdezFactorial
# Calculates the factorial of any positive integer number.
# Input(s)
# Any integer>=0
# Output
# The factorial result of the given number
# A factorial takes a positive integer n and calculates the product of all numbers
# from 1 to n. For example, 5 factorial (5!) is equivalent to 5*4*3*2*1 or 120.

import pyinputplus as pyip
import math

# Welcoming Statement
print("Calculates the factorial of any positive integer number.")

# Required Info
n=pyip.inputInt("Find the factorial of what number? ",min=0)

# Calculation Setup Variables
loopFact=1
indStart=1
indEnd=n+1

# Calculation by Loop
for i in range(indStart,indEnd):
    loopFact*=i

# Calculation by Math Library
mathFact=math.factorial(n)

# Info Displayed to User
print(f"By method of loop, {n}! is equivalent to {loopFact}.")
print(f"By method of math library, {n}! is equivalent to {mathFact}.")

# Ending Note
print("Program Ends")