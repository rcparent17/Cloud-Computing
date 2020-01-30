import sys

args = sys.argv
numArgs = len(args)
print("Number of args: " + str(numArgs))
if numArgs>=3:
  print("There are 3 or more arguments")
else:
  print("There are less than 3 arguments")
