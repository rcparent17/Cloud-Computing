import current

lastGuess = ""

def guess():
    guess = ""
    while not len(guess) == 1:
        guess = input("Enter 1 letter: ")
    lastGuess = guess
    check = current.check(lastGuess)
    current.display()
    if check:
        print(lastGuess + " is in the word.")
    else:
        print(lastGuess + " is not in the word.")
