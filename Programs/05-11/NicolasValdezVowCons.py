# Nicolas Valdez Thu May  8 12:55:34 2025
# NicolasValdezVowCons
# Counts number of vowels or consonants in a string. Y is considered a vowel.
# Does not count letters with accents.
# Input(s)
# A string
# Output
# Number of vowels or number of consonants

import pyinputplus as pyip

# Welcoming Statement
print('Counts number of vowels or consonants in a string. The letter, y is considered a consonant. Does not count characters with accents.')

def vowels(string):
    '''Counts number of vowels. The letter, 'y' is not considered a vowel.'''
    vowels=('a','e','i','o','u')
    count=0
    for i in string:
        if i.lower() in vowels:
            count+=1
    return(count)

def cons(string):
    '''Counts the number of consonants. The letter, 'y' is considered a consonant.'''
    cons=('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')
    count=0
    for i in string:
        if i.lower() in cons:
           count+=1
    return(count)

# User inputs
string=pyip.inputStr('Enter a string: ')
countVow=vowels(string)
countCons=cons(string)

# Display results
print(f'The number of vowels is {countVow}.')
print(f'The number of consonants is {countCons}.')

# Ending Note
print('Program Ends')