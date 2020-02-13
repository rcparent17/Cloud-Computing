# file: hangman.py
# author: Reilly Parent
# main module for hangman

import words
import hangIO
import current
import sys
import random

global running # if the game is running
running = True

global wordDict # words from dictionary file
wordDict = words.init()

global score
score = 500

# select and set random word to current
def init():
    global wordDict
    select = random.randint(0, len(wordDict)-1)
    current.set(list(wordDict.keys())[select], list(wordDict.values())[select])

# main method to run game
def run():
    global score
    global running
    guess = False
    running = True
    numWrong = 0
    while running:
        if current.wordSolved(): # if solved
            print("You got this word!\n")
            del wordDict[current.getWord()] # remove from dict
            score = score + current.getValue()
            running = False
        if running:
            current.display()
            guess = hangIO.guess()
        if not guess and running:
            numWrong = numWrong + 1
        if numWrong == 6 and running: # lose condition
            print("You didn't get this word. The word was: " + current.getWord() + "\n")
            del wordDict[current.getWord()] # remove from dict
            running = False

while len(wordDict) > 0: # while words are left
    init() # set word
    hangIO.resetCount() # set remaining guesses to 6
    run() # run word
print("Your score: " + str(score))
