# file: current.py
# author: Reilly Parent
# a hangman module to change and display the current word
import sys

global currentWord
currentWord = ""

global currentValue
currentValue = 0

global revealed
revealed = []

global charsInWord
charsInWord = []

# sets current word and point value, called by set
def setWord(word, value):
    global currentWord
    global currentValue
    currentWord = word
    currentValue = value

# (re)initializes current word and value, an array of all of the characters in the current word, and resets revealed when called
def set(word, value):
    global charsInWord
    global revealed
    setWord(word, value)
    charsInWord = []
    revealed = []
    #store characters in current word
    for lttr in list(word):
        if not lttr in charsInWord:
            charsInWord.append(lttr)

# displays word based on what has been revealed
def display():
    global currentWord
    global revealed
    chars = list(currentWord)
    sys.stdout.write("Current guess:")
    # display each character individually, and " - " if the character is not revealed
    for c in chars:
        if not c in revealed:
            sys.stdout.write(" - ")
        else:
            sys.stdout.write(" " + c + " ")
    sys.stdout.write("\n")
    sys.stdout.flush()

# returns whether or not a character is in the word and not revealed, appends character to revealed if true
def check(lttr):
    global charsInWord
    global revealed
    if lttr in charsInWord and not lttr in revealed:
        revealed.append(lttr)
        return True
    return False

# returns whether or not all characters in the word have been revealed
def wordSolved():
    global charsInWord
    global revealed
    solved = True
    for c in charsInWord:
        if not c in revealed:
            solved = False
            break
    return solved

# getters

def getValue():
    global currentValue
    return currentValue

def getWord():
    global currentWord
    return currentWord
