import socket
import sys
import os
import select

address = ("localhost", 9999)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

os.system("clear")
usrname = input("CloudChat v0.0.1\n\nenter a username: ")
sock.connect(address)
connectMsg = usrname + " has connected.\n"
sock.send(connectMsg.encode('ascii'))

while 1:
  sockets = [sys.stdin, sock]
  rsocks, wsock, errsock = select.select(sockets, [], [])
  for rsock in rsocks:
    if rsock==sock:
      message = rsock.recv(2048).decode('ascii')
      print(message)
    else:
      message = sys.stdin.readline()
      sock.send((usrname + ": " + message).encode('ascii'))
      sys.stdout.write("YOU: " + message)
      sys.stdout.flush()
