# Nicolas Valdez Feb 10 2025
# NicolasValdezAge
# Checks whether a person is an infant, child, teenager, or adult
# Input(s)
# Age, float
# Output
# Age classification

import pyinputplus as pyip

# Welcoming Statement
print("Input your age to check whether you are an infant, child, teenager, or adult")

# Assumptions
adult=20
teen=13
child=1

# Required Info
age=pyip.inputFloat("Input your age: ")

# Classification
if age>=adult:
    print("You are an adult.")
elif age>=teen:
    print("You are a teenager.")
elif age>child:
    print("You are a child.")
else:
    print("You are an infant.")
    
# Ending Note
print("Program Ends")