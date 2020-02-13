# file: hangIO.py
# author: Reilly Parent
# I/O module for hangman

import current

global lastGuess # last guessed character
lastGuess = ""

global remaining # remaining attempts
remaining = 6

# method for user to guess a letter
def guess():
    global lastGuess
    global remaining
    guess = ""
    while not len(guess) == 1: # while not 1 character
        guess = input("Enter 1 letter: ")
    lastGuess = guess
    check = current.check(lastGuess) # check current word for character
    if not check:
        remaining = remaining - 1
    if check:
        print(lastGuess + " is in the word.")
    else:
        print(lastGuess + " is not in the word, or has already been guessed.")
    print(str(remaining) + " guesses remaining.\n")

    return check

# reset remaining guesses to 6
def resetCount():
    global remaining
    remaining = 6
