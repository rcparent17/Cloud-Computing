import sys

global currentWord
currentWord = ""

global currentValue
currentValue = 0

global revealed
revealed = []

global charsInWord
charsInWord = []

def setWord(word, value):
    global currentWord
    global currentValue
    currentWord = word
    currentValue = value

def set(word, value):
    global charsInWord
    global revealed
    setWord(word, value)
    charsInWord = []
    revealed = []
    for lttr in list(word):
        if not lttr in charsInWord:
            charsInWord.append(lttr)

def display():
    global currentWord
    global revealed
    chars = list(currentWord)
    sys.stdout.write("Current guess:")
    for c in chars:
        if not c in revealed:
            sys.stdout.write(" - ")
        else:
            sys.stdout.write(" " + c + " ")
    sys.stdout.write("\n")
    sys.stdout.flush()

def check(lttr):
    global charsInWord
    global revealed
    if lttr in charsInWord and not lttr in revealed:
        revealed.append(lttr)
        return True
    return False

def wordSolved():
    global charsInWord
    global revealed
    solved = True
    for c in charsInWord:
        if not c in revealed:
            solved = False
            break
    return solved

def getValue():
    global currentValue
    return currentValue

def getWord():
    global currentWord
    return currentWord
