# Nicolas Valdez Jan 31, 2025
# Converts celsius temperature to a fahrenheit temperature
# 
# Input(s)
# Keyboard input of a celsius temperature in the format of a 
# float or integer value without the associated unit.
# For example, the user inputs the float "0.00" or the integer "100".
# 
# Output
# Print of the converted temperature
# 
# The formula for converting celsius temperature to fahrenheit is:
# Fahrenheit = (9/5) * Celsius + 32

# Given temp in Celsius
Cels=float(input("Give a temperature in celsius: "))

# Conversion Factor
Fahr=(9/5)*Cels+32

# Info displayed to user
print(f"The temperature in fahrenheit is {Fahr}")

# Ending note
print("Program Ends")
