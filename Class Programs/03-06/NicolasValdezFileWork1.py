# Nicolas Valdez Thu Mar  6 18:46:21 2025
# NicolasValdezFileWork
# Calculates the total and average of the data in the provided text file
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
except FileNotFoundError:
    print(errorList[2])

else:
    if error!=True:
        n=len(values)
        total=0
        indStart=0
        indEnd=n
        for i in range(indStart,indEnd):
            total+=values[i]
            
        average=total/n
    
        # Displayed to User
        print(f"Total is {total}")
        print(f"Average is {average}")
    
        # Ending Note
        print("Program Ends")