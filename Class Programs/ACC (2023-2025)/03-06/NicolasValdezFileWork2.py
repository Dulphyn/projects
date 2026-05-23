# Nicolas Valdez Thu Mar  6 18:46:21 2025
# NicolasValdezFileWork
# Check if a certain file exists and if there is data in the file
# Input(s)
# The provided text file
# Output
# The total of the numbers in the file as well as their average
# Total = Sum of all numbers
# Average = (Total) / (Number of numbers)

# Provided text file name
fileName="numbers.txt"

# Welcoming Statement
print(f"Calculates the total and average of the data in {fileName}")

# Exception List
valueError="Data must only contain numbers"
zeroDivision="Data is empty"
fileNotFound="File Not Found"
errorList=[valueError,zeroDivision,fileNotFound]

# Validates file and then puts data into a list
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

# Calculations
data=txtToList(fileName)
if data[1]!=True:
    n=len(data[0])
    total=0
    indStart=0
    indEnd=n
    for i in range(indStart,indEnd):
        total+=data[0][i]
        
    average=total/n
    
    # Displayed to User
    print(f"Total is {total}")
    print(f"Average is {average}")
    
    # Ending Note
    print("Program Ends")