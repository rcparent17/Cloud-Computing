import current

global lastGuess
lastGuess = ""

global remaining
remaining = 6

def guess():
    global lastGuess
    global remaining
    guess = ""
    while not len(guess) == 1:
        guess = input("Enter 1 letter: ")
    lastGuess = guess 
    check = current.check(lastGuess)
    if not check:
        remaining = remaining - 1
    if check:
        print(lastGuess + " is in the word.")
    else:
        print(lastGuess + " is not in the word, or has already been guessed.")
    print(str(remaining) + " guesses remaining.\n")

    return check

def resetCount():
    global remaining
    remaining = 6
