# file: rpc_client.py
# author: Reilly Parent
# client for add and multiply servers

import sys
import xmlrpc.client

problems = []

add  = xmlrpc.client.ServerProxy("http://ip-172-31-41-36.us-east-2.compute.internal:8000/")
mult = xmlrpc.client.ServerProxy("http://ip-172-31-27-3.us-east-2.compute.internal:8000/")


probFile = open("calculator.txt")
lines = probFile.readlines()

# store problems as tuples
for line in lines:
    parts = line.split()
    problems.append((parts[0], int(parts[1]), int(parts[1])))

for problem in problems:
    # call add server if line starts with A, else multiply
    print(add.add(problem[1], problem[2])) if (problem[0]=="A") else print(mult.multiply(problem[1], problem[2]))
