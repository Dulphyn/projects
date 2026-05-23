# Nicolas Valdez Tue Apr  1 15:05:17 2025
# NicolasValdezPieChart
# Creates a pie chart of expenses
# Input(s)
# File with information of the following expenses in this order:
# Rent
# Gas
# Food
# Clothing
# Car payment
# Misc
# Output
# Pie chart of expenses
# [Main Formula]

import matplotlib.pyplot as plt

# Welcoming Statement
print("Chart your expenses in a pie chart.")

# Provided text file name
fileName="expenses.txt"

# Exception List
valueError="Data must only contain numbers"
zeroDivision="Data is empty"
fileNotFound="File Not Found"
errorList=(valueError,zeroDivision,fileNotFound)

def txtToList(fileName):
    error=False
    values=[]
    try:
        with open(fileName,"r") as infile:
            for line in infile:      
                try:
                    values.append(float(line.rstrip("\n")))
                except ValueError:
                    print(errorList[0])
                    error=True
        fileLength=len(values)
        1/fileLength # Tests for ZeroDivisionError
    except ZeroDivisionError:
        print(errorList[1])
        error=True
    except FileNotFoundError:
        print(errorList[2])
        error=True
    finally:
        return(values,error)

# Make pie chart
legend=("Rent","Gas","Food","Clothing","Car Payment","Misc")
data=(txtToList(fileName),legend)
if data[0][1]!=True:
    x=data[0][0]
    plt.pie(x,labels=data[1])

plt.show()
# Ending Note
print("Program Ends")