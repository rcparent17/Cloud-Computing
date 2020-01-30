import socket
import sys, os
import threading
import time

address = ("localhost", 9999)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

os.system("clear")
usrname = input("CloudChat v0.0.1\n\nenter a username: ")
sock.connect(address)
connectMsg = usrname + " has connected.\n"
sock.send(connectMsg.encode('ascii'))

def poll():
  msg = sock.recv(2048).decode('ascii')
  if len(msg)>0:
    print("\n"+msg+"\n")

while 1:
  print("looping")
  poll()
  msg = input("message> ")
  sock.send((usrname + ": " + msg).encode('ascii'))

