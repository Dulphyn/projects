# Nicolas Valdez Fri Apr 11 12:58:49 2025
# NicolasValdezFileRead
# Pair and write line separated values from two text files into a new text file.
# Input(s)
# Two text files containing line separated values
# Number of lines to be read from the two separate files 
# Output
# A new text file containing matched 

import pyinputplus as pyip

# Welcoming Statement
print("Pair and write values from two text files into a new text file.")

# Input files
firstFile=pyip.inputFilename("Input name of the first file: ")
secondFile=pyip.inputFilename("Input name of the second file: ")
inFile=(firstFile,secondFile)

# Output file
outFile="combined.txt"

# Exception List
valueError="Data must only contain numbers"
zeroDivision="Data is empty"
fileNotFound="File Not Found"
errorList=[valueError,zeroDivision,fileNotFound]

# Validates file and then puts data into a list
def txtToList(fileName):
    """Validates file and then puts data into a list"""
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

def combine(first,second):
    """Takes two lists, combines them into a new tuple, then converts each
    element of the combined tuple into a string. If the length of the
    two lists is unequal, only combines the number of elements equivalent 
    to the length of the shorter list."""
    zipped=tuple(zip(first,second))
    combined=[]
    for tup in zipped:
        combined.append(f"{tup[0]} {tup[1]}")
    return(combined)
# Write to new file
first=txtToList(inFile[0])
second=txtToList(inFile[1])
if first[1]!=True and second[1]!=True:
    combined=combine(first[0],second[0])
    minLines=1
    maxLines=len(combined)
    numLines=pyip.inputInt("How many values do you want to pair up? ",min=minLines,max=maxLines)
    indEnd=numLines+1
    with open(outFile,"w") as newfile:
        for column in combined[minLines:indEnd]:
            newfile.write(column)
            newfile.write("\n")
    print(f"\nThe text file, {outFile}, has been created and has paired the values the first {numLines} values of your two text files.\n")
# Ending Note
print("Program Ends")