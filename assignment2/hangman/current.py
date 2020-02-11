import sys

currentWord = ""
currentValue = 0
revealed = []
charsInWord = []

def setWord(word, value):
    currentWord = word
    currentValue = value

def set(word, value):
    setWord(word, value)
    charsInWord = []
    for lttr in list(word):
        if not lttr in charsInWord:
            charsInWord.add(lttr)

def display():
    chars = list(currentWord)
    for c in chars:
        if not 
        c in revealed:
            sys.stdout.write(" - ")
        else:
            sys.stdout.write(" " + c + " ")
    sys.stdout.write("\n")
    sys.stdout.flush()

def check(lttr):
    if lttr in charsInWord:
        revealed.add(lttr)
        return True
    return False
