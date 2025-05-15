# Nicolas Valdez Thu Apr 10 18:03:36 2025
# NicolasValdezGuess
# Generates a random number, has user make attempts to guess the number
# Input(s)
# An integer guess
# Output
# Displays if guess is too high, too low, or correct
# Asks user to play again

import pyinputplus as pyip
import random as rand

# Welcoming Statement
print("Try to guess a secret number.")

# Generate a secret number
def randNum(low,high):
    """Generates and returns random integer between set bounds, inclusive."""
    num=round(rand.triangular(low,high))
    return(num)

# Prompt user to make a guess
def guess(low,high):
    """Prompts user to guess an integer between set bounds, inclusive."""
    guess=pyip.inputInt(f"Guess a number from {low} to {high}: ",min=low,max=high)
    return(guess)

# Game statements
def answer(tries,maxTries):
    """Includes all statements about the user's guess printed to user."""
    correct=f"\nCongratulations, you guessed the secret number after {tries} attempts!"
    tooLow="Too low, try again."
    tooHigh="Too high, try again."
    triesLimit=f"\nGuess limit of {maxTries} reached."
    choice=["Yes","No"]
    prompt="Would you like to play again?\n"
    return(correct,tooLow,tooHigh,triesLimit,choice,prompt)

# The guessing game
def game():
    """Generates a random number, has user make attempts to guess the number. Returns if user wants to play again."""
    low=1
    high=600
    maxTries=8
    secret=randNum(low,high)
    tries=1
    for attempt in range(maxTries):
        attempt=guess(low,high)
        if attempt==secret:
            print(answer(tries,maxTries)[0])
            break
        elif attempt<secret:
            print(answer(tries,maxTries)[1])
            tries+=1
        else:
            print(answer(tries,maxTries)[2])
            tries+=1
        if tries>maxTries:
            print(answer(tries,maxTries)[3])
    play=pyip.inputMenu(answer(tries,maxTries)[4],prompt=answer(tries,maxTries)[5],numbered=True)
    return(play,answer(tries,maxTries)[4])

# Initiates the game
replay=game()
while replay[0]==replay[1][0]:
    replay=game()

# Ending Note
print("Program Ends")