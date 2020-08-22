# 4. Dice Rolling Simulator

# As the name of the program suggests, we will be imitating a rolling dice. 
# The program will generate a random number each dice the program runs, and the users can use the dice repeatedly for as long as he wants.  
# When the user rolls the dice, the program will generate a random number between 1 and 6 (as on a standard dice).
# The number will then be displayed to the user. 
# It will also ask users if they would like to roll the dice again. 
# The program should also include a function that can randomly grab a number within 1 to 6 and print it. 
# This beginner-level project will help build a strong foundation for fundamental programming concepts.

from random import randint

def dice_rolls():
    dice_no = randint(1,6)
    print(dice_no)

while True:
    user = input("\nRolling Dice! roll | quit : ").lower()
    if user == 'roll':
        dice_rolls()
        user = input("\nWanna play again? yes | no : ")
        if user == 'no':
            print("\nGame Over!\nThank you for playing.")
            break
    else:
         print("\nGame Over!\nThank You for playing.")
         break