# Nicolas Valdez Fri Apr 18 13:04:04 2025
# NicolasValdezDate
# Converts a date to another format and then prints that date
# Input(s)
# A date in the format of mm/dd/yyyy
# Output
# A date in the format of [Month] [Day], [Year]

import pyinputplus as pyip

# Welcoming Statement
print("Convert a date from mm/dd/yyyy to [Month] [Day], [Year].")

# Get date
inpDate=pyip.inputDate("Enter a date: ")

# Format date
newDate=inpDate.strftime("%B %d, %Y")

# Print date
print(newDate)

# Ending Note
print("Program Ends")