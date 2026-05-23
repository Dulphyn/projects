# Nicolas Valdez Thu May  8 11:28:04 2025
# NicolasValdez8Ball
# Simulates a Magic 8 Ball. This is displays a random response 
# to a yes or no question
# Input(s)
# 8 Ball responses file
# A yes or no question
# Restart program choice
# Output
# A random 8 Ball response
# [Main Formula]

import pyinputplus as pyip
from numpy import random

# File Names
fileName='8_ball_responses.txt'


# Exception List
zeroDivision='File is empty'
fileNotFound='File not found'
errors=(zeroDivision,fileNotFound)

# Welcoming Statement
print('Simulates a Magic 8 Ball. This is displays a random response to a yes or no question.')

def empty(data):
    '''Test for empty file by the number of lines in the file.'''
    1/len(data)
    
def txtToList(fileName):
    '''Validates file then puts data into a list'''
    error=False
    data=[]
    try:
        with open(fileName,'r') as infile:
            for line in infile:
                data.append(line.rstrip('\n'))
        empty(data)
    except ZeroDivisionError:
        print(errors[0])
        error=True
    except FileNotFoundError:
        print(errors[1])
        error=True
    finally:
        return(data,error)

def answer(data):
    choices=len(data)
    randNum=random.randint(0,choices)
    response=data[randNum]
    return(response)


def main(data):
        pyip.inputStr('Ask a yes or no question: ')
        response=answer(data[0])
        print(f'{response}\n')
        choices=['Ask another question','Exit']
        choice=pyip.inputMenu(choices,numbered=True)
        return(choice,choices)
data=txtToList(fileName)
if data[1]==False:
    restart=main(data)
    while restart[0]==restart[1][0]:
        restart=main(data)
        
# Ending Note
print('Program Ends')