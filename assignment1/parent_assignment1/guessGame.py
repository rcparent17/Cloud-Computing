import sys
import random

rand = random.randint(5,15)
guessed = False
numGuesses = 0

while not guessed:
  guess = 0
  try:
    guess = int(input("Guess a number from 5 to 15: "))
  except Exception:
    print("Guess was not a number")
    sys.exit(1)
  numGuesses = numGuesses + 1
  if rand==guess:
    print("MATCH")
    print("Number found in " + str(numGuesses) + " guesses")
    guessed = True
  elif abs(guess-rand)<3:
    print("HOT")
  else:
    print("COLD")
