# file: words.py
# author: Reilly Parent
# dictionary module for hangman

wordDict = {}

dFile = open("dictionary.txt", "r")
lines = dFile.readlines()

# initialize and return word dictionary from file
def init():
    for line in lines:
        word_value = line.split()
        wordDict[word_value[0]] = int(word_value[1])
    return wordDict
