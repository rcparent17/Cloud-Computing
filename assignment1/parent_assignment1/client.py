import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = (sys.argv[1], int(sys.argv[2])) #(host, address)

sendString = ""
sendFile = open(sys.argv[3], "r")
lines = sendFile.readlines()

for line in lines:
  sendString = sendString + line.strip() + "#"

sendString = sendString[:-1]

sock.connect(address)
sock.send(sendString.encode('ascii'))

msg = sock.recv(1024)
sock.close()

answer = msg.decode('ascii').split("/")
lines = answer[0]
words = answer[1]
chars = answer[2]

print(lines + " lines, " + words + " words, and " + chars + " characters in " + sys.argv[3])
