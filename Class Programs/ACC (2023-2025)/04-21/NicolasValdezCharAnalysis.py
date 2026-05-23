# Nicolas Valdez Fri Apr 18 14:00:47 2025
# NicolasValdezCharAnalysis
# Analyzes the distribution of character types in a provided text file
# Input(s)
# Provided text file
# Output
# Number of uppercase letters in the file
# Number of lowercase letters in the file
# Number of digits in the file
# Number of whitespace characters in the file

import tabulate as tabl

# Welcoming Statement
print("Analyzes the distribution of character types in a provided text file.")

# File Name
fileName="text.txt"

# Exception List
zeroDivision="File is empty"
fileNotFound="File not found"
errors=(zeroDivision,fileNotFound)


def empty(data):
    """Test for empty file by the number of lines in the file."""
    1/len(data)
    

def txtToList(fileName):
    """Validates file then puts data into a list"""
    error=False
    data=[]
    try:
        with open(fileName,"r") as infile:
            for line in infile:
                data.append(line.rstrip("\n"))
        empty(data)
    except ZeroDivisionError:
        print(errors[0])
        error=True
    except FileNotFoundError:
        print(errors[1])
        error=True
    finally:
        return(data,error)


def analyze(text):
    """Counts uppercase, lowercase, numeric digits,
    and whitespace characters from a line of text."""
    upper=0
    lower=0
    digits=0
    white=0
    for char in text:
        if char.isupper()==True:
            upper+=1
        elif char.islower()==True:
            lower+=1
        elif char.isdigit()==True:
            digits+=1
        elif char.isspace()==True:
            white+=1
    return(upper,lower,digits,white)

# Create data for a table which counts uppercase, lowercase, numeric digits,
# and whitespace characters from a list
data=txtToList(fileName)
if data[1]==False:
    table=[0,0,0,0]
    for line in data[0]:
        values=analyze(line)
        for i in range(len(values)):
            table[i]+=values[i]
    table=[table]
    header=("Uppercase","Lowercase","Digits","Whitespace")
    tablefmt="grid"
    print("\n",tabl.tabulate(table,header,tablefmt),"\n")
    
# Ending Note
print("Program Ends")