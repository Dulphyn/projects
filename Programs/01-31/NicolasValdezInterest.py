# Nicolas Valdez Jan 31, 2025
# Calculates the amount of money that will be in a bank account with 
# compounding interest after a specified number of years.

# Input(s)
# Keyboard input of:
# P, the principle amount that was originally deposited into the account
# r, the annual interest rate paid by the account
# n, the number of times per year that the interest is compounded
# t, the specified number of years
# 
# P is some US dollar amount in the format of either a float or integer
# without the currency sign.
# r is some percent with format of a float or integer written without
# the percent sign.
# n is an integer.
# t is an integer.
# 
# Output
# Print of the amount of money in the account
# after the specified number of years rounded to nearest cent
# 
# The formula for calculating compound interest of a principal amount is:
# Final Amount = P*(1+(r/n))**(n*t)

# Required information from the user
prin=float(input("What is the original amount deposited? $"))
interest=float(input("What is the annual interest rate percent paid out? "))/100
number=int(input("How many times per year is the interest rate paid out? "))
time=int(input("How many years will the money stay in the account? "))

# Calculating compound interest
total=prin*(1+(interest/number))**(number*time)

# Info displayed to user
print(f"After interest, the principal deposit will have grown to ${total:.2f}")

# Ending note
print("Program Ends")