# 5. Hangman
# This is more of a “guess the word” game. 
# The core concepts you have to use while developing this project are variables, random, integer, strings, char, input and output, and boolean. 
# In the game, users have to enter letter guesses, and each user will have a limited number of guesses 
# (a counter variable is needed for limiting the guesses).
# You can create a pre-organized list of words that users can grab words from. 
# Also, you must include specific functions to check whether or not a user has entered a single letter or 
# if the input letter is in the hidden word, to if the user has actually inputted a single letter, 
# and to print the correct outcomes (letters).

from random import choice
words = ['apple','computer','chair','book','unicorn']
hidden_word = choice(words)
count = 0
limit = 0
print(hidden_word)

def check_letter(letter):
    for word in words:
        if letter in word and len(letter)==1:
            print("\nYou Won!\nword found: ", word)
            return 'found'
            break
    else:
        print("\nTry Again")

flag = True
while flag:
    if limit < 3:
        count += 1
        limit += 1
        user_input = input("\nEnter a letter: ")
        if check_letter(user_input) == 'found':
            print("\nGame Over!")
            break
    else:
        print("\nGame Over!")
        flag = False
print("\nTries: ", count)