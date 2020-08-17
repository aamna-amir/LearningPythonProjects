# Create a number guessing program

# This is a simple yet exciting idea. You can even call it a mini-game. 
# Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range. 
# Then give users a hint to guess the number. 
# Every time the user guesses wrong, he gets another clue, and his score gets reduced. 
# The clue can be multiples, divisible, greater or smaller, or a combination of all.
# You will also need functions to compare the inputted number with the guessed number, 
# to compute the difference between the two, and to check whether an actual number was inputted or not.

from random import randint

num = randint(1, 100)
print(num)
def guess_num(guess):
    
    flag = True
    while flag:
        user_num = int(input("Guess the number: "))
        if user_num != guess:
            if user_num > guess:
                print(f"OPPS.. TRY AGAIN\nHint! Guess number is less than {guess + randint(1,10)}..")
            else: 
                print(f"OPPS.. TRY AGAIN\nHint! Guess number is greater {randint(100,110) - guess}..")
        else:
            print("Congratulations! You won the game...")
            flag = False

guess_num(num)