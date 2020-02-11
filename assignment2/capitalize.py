sentence = input("Enter some words: ")
words = sentence.split()
outString = ""

for word in words:
	newWord = ""
	newWord = newWord + word[0].upper()
	newWord = newWord + word[1:]
	outString = outString + newWord + " "

print(outString)
