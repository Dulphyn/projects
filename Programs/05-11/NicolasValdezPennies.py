# Nicolas Valdez Thu May  8 09:33:58 2025
# NicolasValdezPennies
# Calculates money earned per day if salary was doubled each day 
# as well as the total money earned at the end of the period
# Input(s)
# S, Initial salary per day
# L, Period length
# Output
# Salary for each day of the period
# Total money earned from all days of the period
# (Day n salary) = S * ((Rate of increase per day) ** n)

import pyinputplus as pyip
from tabulate import tabulate

# Welcoming Statement
print('Calculates money earned if a daily salary was doubled each day. Shows grand total earnings.\n')

# Inputs
prompt=('Choose a starting daily salary:\n')
choices=('Penny','Nickel','Dime','Quarter')
minL=0
maxL=100
S=pyip.inputMenu(choices,prompt,numbered=True) # Initial salary given for the day
L=pyip.inputInt('Number of days to multiply salary: ',greaterThan=minL,max=maxL) # Period length for which salary will increase

# Assumptions
R=2 # Rate at which salary increases per day

def coinToValue(S,choices):
    values=(0.01,0.05,0.10,0.25)
    if S==choices[0]:
        S=values[0]
    elif S==choices[1]:
        S=values[1]
    elif S==choices[2]:
        S=values[2]
    else:
        S=values[3]
    return(S)
        

def salaryIncrease(S,L,R):
    '''Calculate the salary for each day of a period and put it into a list
    S(0) = Initial salary given for the day
    L = Period length for which salary will increase
    R = Rate at which salary increases per day
    S(n)= S(0) * (R ** n)
    sum of S(n) from n=0 to n=L
    '''
    salPerDay=[]
    for day in range(L+1):
        sal=S*(R**day)
        salPerDay.append(sal)
    return(salPerDay)

def grandTotal(data):
    """Sum all values of a column."""
    total=['Total Earned',0]
    for sal in data:
        total[1]+=sal[1]
    return(total)

# Form table
precision=2
coinValue=coinToValue(S,choices)
columns=('Day #','Salary ($)')
salaries=salaryIncrease(coinValue,L,R)
days=range(L+1)
data=list(zip(days,salaries))
total=grandTotal(data)
data.append(total)

# Print table
table=tabulate(data,headers=columns,floatfmt=f'.{precision}f')
print(table)

# Ending Note
print('\nProgram Ends')