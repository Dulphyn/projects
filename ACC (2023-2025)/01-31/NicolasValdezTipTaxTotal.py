# Nicolas Valdez Jan 31, 2025
# Calculates the total amount of a meal purchased at a restaurant
# 
# Input(s)
# Keyboard input of the charge for the food in US dollars in the format of a
# float or integer without the currency sign. This assumes tip is calculated
# before sales tax.
# For example, the user inputs the float "9.99" or the integer "10".
# 
# Output
# Print of the charge of the food
# Print of the amount of the 18% tip
# Print of the amount of the 7% sales tax
# Print of the amount of the charge of the food plus the tip plus the sales tax
# All outputs rounded to nearest cent

# Constants
tip=0.18
sales_tax=0.07

# Charge of the food
charge=float(input("The meal costed: $"))

# Tip cost
tip_cost=charge*tip

# Sales tax cost
sales_tax_cost=charge*sales_tax

# Total cost
total=charge+tip_cost+sales_tax_cost

# Info displayed to user
print(f"You were charged ${charge} for the food")
print(f"The 18% tip costed you ${tip_cost:.2f}")
print(f"The 7% sales tax costed you ${sales_tax_cost:.2f}")
print(f"The total cost of the food is ${total:.2f}")

# Ending note
print("Program Ends")