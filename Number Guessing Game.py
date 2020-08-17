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
def comp_guess_num(input_num, guess):
    score = 100
    if input_num > guess:
        print(f"OPPS.. TRY AGAIN\nHint! Guess number is less than {guess + randint(1,10)}..")
        score -= 1
    else: 
        print(f"OPPS.. TRY AGAIN\nHint! Guess number is greater {randint(90,100) - guess}..")
        score -= 1

def diff_guess_num(input_num, guess):
    diff = input_num - guess
    print(f"guess {diff} number less then input number")

def check_actual_num():
    pass

def guess_num(guess):
    
    flag = True
    while flag:
        user_num = int(input("Guess the number: "))
        if user_num != guess:
            comp_guess_num(user_num, guess)
        else:
            print(f"Congratulations! You won the game...\nYour Score: {score}")
            flag = False

guess_num(num)