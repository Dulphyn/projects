# Nicolas Valdez Fri Feb 14 12:31:20 2025
# NicolasValdezSoftSales
# Calculates discount savings and total cost of package(s) after discount.
# Input(s)
# Number of packages purchased, int
# Output
# Discount savings
# Total cost of package after discount
# --------------------------------------
# For quantities 1<=q<=9, 0% discount
# For quantities 10<=q<=19, 10% discount
# For quantities 20<=q<=49, 20% discount
# For quantities 50<=q<=99, 30% discount
# For quantities q>=100, 40% discount
# --------------------------------------

import pyinputplus as pyip

# Welcoming Statement
print("Calculates discount savings and total cost of package(s) after discount (in USD).")

# Table and Conversion
price=99 # Cost of individual package

max0=9 # Max purchased quantities per discount tier
max1=19
max2=49
max3=99

disc0=0.0 # Discount taken off purchase for each tier
disc1=0.1
disc2=0.2
disc3=0.3
disc4=0.4

discConv=100 # Conversion factor for decimal discount to percent form

# Required Info
count=pyip.inputInt("How many packages did you buy? ",min=1)

# Calculation
if count<=max0:
    discount=disc0
elif count<=max1:
    discount=disc1
elif count<=max2:
    discount=disc2
elif count<=max3:
    discount=disc3
else:
    discount=disc4

cost=price*count
savings=cost*discount
total=cost-savings
percent=discount*discConv

# Info Displayed to User
print(f"The {percent}% discount saved ${savings:.2f} off your ${cost:.2f} purchase of {count} package(s).")
print(f"After savings, your total comes out to ${total:.2f}.")

# Ending Note
print("Program Ends")