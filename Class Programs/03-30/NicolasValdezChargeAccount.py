# Nicolas Valdez Thu Mar 27 18:03:53 2025
# NicolasValdezChargeAccount
# Checks if the user's charge account number exists in the given file
# Input(s)
# The provided text file
# Charge account number
# Output
# States if inputted charge account number exists in file

import pyinputplus as pyip

# Provided text file name
fileName="charge_accounts.txt"

# Welcoming Statement
print("Check if your charge account exists.")

# Exception List
valueError="Data must only contain integers"
zeroDivision="Data is empty"
fileNotFound="File not found"
accountDigits=7
faultyData=f"Data must only contain numbers with {accountDigits} digits"
errorList=(valueError,zeroDivision,fileNotFound,faultyData)

def txtToList(fileName):
    error=False
    badData=False
    values=[]
    try:
        with open(fileName,"r") as infile:
            for line in infile:      
                try:
                    values.append(int(line.rstrip("\n")))
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
        for i in values:
            dataLength=len(str(i))
            badData=False
            if dataLength!=accountDigits:
                badData=True
                error=True
        if badData==True:
            print(errorList[3])    
        return(values,error)
    
# Calculations
data=txtToList(fileName)
if data[1]!=True:
    accountNum=pyip.inputInt("Input charge account number: ")
    accountExists=False
    for i in data[0]:
        if accountNum==i:
            accountExists=True
            print("Charge account number is valid.")
            break
    if accountExists==False:
        print("Charge account number is not valid.")
        
# Ending Note
print("Program Ends")