# Nicolas Valdez Fri Apr 11 17:25:38 2025
# NicolasValdezSaveRecords
# For each player in a golf game, records their name and score to a text file.
# Input(s)
# Player names
# Player scores
# Output
# Names and scores recorded to a file 

import pyinputplus as pyip

# Welcoming Statement
print("Save each player's names and respective scores.")

# Output file
fileName="golf.txt"

# Grab name and score of a player
def grabInfo():
    """Asks user to enter a player's name and that player's score."""
    name=pyip.inputStr("\nEnter player's name: ")
    score=pyip.inputInt(f"Enter the score of the player {name}: ")
    return(name,score)

def main():
    minPlayer=1
    count=pyip.inputInt("How many players are there? ",min=minPlayer)
    with open(fileName,"w") as newfile:
        for player in range(count):
            data=str(grabInfo())
            newfile.write(data)
            newfile.write("\n")
            
main()
print(f"\nInformation has been saved as {fileName}.\n")
# Ending Note
print("Program Ends")