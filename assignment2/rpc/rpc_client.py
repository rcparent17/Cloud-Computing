import sys
import xmlrpc.client

problems = []

add  = xmlrpc.client.ServerProxy("http://localhost:8000/")
mult = xmlrpc.client.ServerProxy("http://localhost:8001/")


probFile = open("calculator.txt")
lines = probFile.readlines()

for line in lines:
    parts = line.split()
    problems.append((parts[0], int(parts[1]), int(parts[1])))

for problem in problems:
    add.add(problem[1], problem[2]) if (problem[0]=="A") else mult.multiply(problem[1], problem[2])
