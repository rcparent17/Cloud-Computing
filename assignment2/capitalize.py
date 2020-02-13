# file: capitalize.py
# author: Reilly Parent

sentence = input("Enter some words: ")
words = sentence.split() # word array
outString = ""

for word in words:
	newWord = ""
	newWord = newWord + word[0].upper() # capitalize first letter
	newWord = newWord + word[1:] # add the rest of the word
	outString = outString + newWord + " "

print(outString)
