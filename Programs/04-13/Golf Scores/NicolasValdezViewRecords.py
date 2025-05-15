# Nicolas Valdez Fri Apr 11 18:54:18 2025
# NicolasValdezViewRecords
# View saved record of player names and their respective scores
# Input(s)
# Text file name and score record
# Output
# Table of player names and their respective scores

from tabulate import tabulate
import ast

# Welcoming Statement
print("View your previously saved record of golf game player names and their respective scores.")

# Record file name
fileName="golf.txt"

# Exception List
zeroDivision="Data is empty"
fileNotFound="File Not Found"
errorList=[zeroDivision,fileNotFound]

# Validates file and then puts data into a list
def txtToList(fileName):
    """Validates file and then puts data into a list"""
    error=False
    values=[]
    try:
        with open(fileName,"r") as infile:
            for line in infile:      
                values.append(line.rstrip("\n"))
        fileLength=len(values)
        1/fileLength # Tests for ZeroDivisionError
    except ZeroDivisionError:
        print(errorList[0])
        error=True
    except FileNotFoundError:
        print(errorList[1])
        error=True
    finally:
        return(values,error)

def listToTuple(badList):
    """Converts a list with string elements in the format of a tuple into an actual tuple."""
    newList=[]
    for i in badList:
        newList.append(ast.literal_eval(i))
    return(newList)

data=txtToList(fileName)
if data[1]==False:
    table=listToTuple(data[0])
    headers=["Player Name","Score"]
    tablefmt="grid"
    print(tabulate(table,headers,tablefmt))
# Ending Note
print("Program Ends")