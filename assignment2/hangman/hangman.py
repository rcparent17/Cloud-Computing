import words
import hangIO
import current
import sys
import random

global running
running = True

global wordDict
wordDict = words.init()

global score
score = 500

def init():
    global wordDict
    select = random.randint(0, len(wordDict)-1)
    current.set(list(wordDict.keys())[select], list(wordDict.values())[select])

def run():
    global score
    global running
    guess = False
    running = True
    numWrong = 0
    while running:
        if current.wordSolved():
            print("You got this word!\n")
            del wordDict[current.getWord()]
            score = score + current.getValue()
            running = False
        if running:
            current.display()
            guess = hangIO.guess()
        if not guess and running:
            numWrong = numWrong + 1
        if numWrong == 6 and running:
            print("You didn't get this word. The word was: " + current.getWord() + "\n")
            del wordDict[current.getWord()]
            running = False

while len(wordDict) > 0:
    init()
    hangIO.resetCount()
    run()
print("Your score: " + str(score))
