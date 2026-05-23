# Nicolas Valdez Tue Apr  1 14:43:49 2025
# NicolasValdezDriversExam
# Grades a given driver's license exam
# Input(s)
# Every applicant's exam
# Output
# For each applicant:
# Display pass or fail
# Display total correct and incorrect answers
# Display a list showing question numbers of incorrectly answered questions

import tabulate as tabl

# Welcoming Statement
print("Returns the grade of each applicant's exam with details.")

# Applicant's exam file names and exam information
fileName=("bob_ans.txt","carol_ans.txt","lynn_ans.txt","george_ans.txt","harvey_ans.txt")
names=("Bob","Carol","Lynn","George","Harvey")
passing=15

# Exception List
zeroDivision="Data is empty"
fileNotFound="A file was not found"
errorList=(zeroDivision,fileNotFound)

# Validates file and then puts data into a list
def txtToList(fileName):
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

# Match applicant answers to the key
def matchToKey(answers):
    key=("a","c","a","a","d","b","c","a","c","b","a","d","c","a","d","c","b","b","d","a")
    correct=[]
    incorrect=[]
    ansOffset=1
    for ans in range(len(answers)):
        if answers[ans]==key[ans]:
            correct.append((ans+ansOffset,answers[ans]))
        else:
            incorrect.append((ans+ansOffset,answers[ans]))
    return(correct,incorrect)
    
# Main
table=[]
header=["Applicant","Pass?","Total Correct","Total Incorrect","Questions Incorrect"]
style="grid"
for file in range(len(fileName)):
    data=txtToList(fileName[file])
    if data[1]!=True:
        matched=matchToKey(data[0])
        numCorrect=len(matched[0])
        numIncorrect=len(matched[1])
        incorrect=[]
        name=names[file]
        if numCorrect>=passing:
            passed="Passed"
        else:
            passed="Did not pass"
        for ans in matched[1]:
            incorrect.append(f"#{ans[0]}")
        table.append([name,passed,numCorrect,numIncorrect,incorrect])
print(tabl.tabulate(table,headers=header,tablefmt=style,stralign="right"))

# Save results
results="exam_results.txt"
with open(results,"w") as infile:
    for row in table:
        for column in row:
            infile.write(str(column))
            infile.write("\n")
        infile.write("\n")

# Ending Note
print("Program Ends")
