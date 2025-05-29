# Nicolas Valdez Fri May  2 14:39:27 2025
# NicolasValdezCourse
# Let user find course information by course number
# Input(s)
# Course number
# Output
# Course room number
# Instructor
# Meeting time

import pyinputplus as pyip

# Welcoming Statement
print('Discover information about a course.')

# Dictionary key and values
dKeys=('CS101','CS102','CS103','NT110','CM241')
d1Values=('3004', '4501', '6755', '1244', '1411')
d2Values=('Haynes', 'Alvarado', 'Rich', 'Burke', 'Lee')
d3Values=('8:00am', '9:00am', '10:00am', '11:00am', '1:00pm')
d4Values=zip(d1Values,d2Values,d3Values)

# Creates dictionaries
d1=dict(zip(dKeys,d1Values))
d2=dict(zip(dKeys,d2Values))
d3=dict(zip(dKeys,d3Values))
d4=dict(zip(dKeys,d4Values))

# Display course info to user
prompt='View a class:\n'
course=pyip.inputMenu(dKeys,numbered=True,prompt=prompt)
roomNum=d4[course][0]
instr=d4[course][1]
time=d4[course][2]
print(f'\nRoom Number: {roomNum}')
print(f'Instructor: {instr}')
print(f'Meeting Time: {time}')

print('\nProgram Ends')