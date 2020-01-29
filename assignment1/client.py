import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ("localhost", 9999)

sendString = ""
sendFile = open("send.txt", "r")
lines = sendFile.readlines()

for line in lines:
  sendString = sendString + line.strip() + " "

sendString = sendString.strip()

sock.connect(address)
socket.send(sendString.encode('ascii'))

msg = sock.recv(1024)
sock.close()

print(msg.decode('ascii') + " words are in the file")
