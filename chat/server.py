import socket
import select
import sys
import threading
from threading import *

hostname = socket.gethostname()

address = (hostname, 9999)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(address)

sock.listen(100)

connected = []

clientsock = ""
addr = ""

def clientthr(csock, addr):
  csock.send(("connected to CloudChat server at " + address[0]).encode("ascii"))
  while 1:
    try:
      msg = csock.recv(2048).decode('ascii')
      if msg:
        sys.stdout.write(msg)
        sys.stdout.flush()
        broadcast(msg.encode('ascii'), csock)
      else:
        remove(csock)
    except:
      continue

def broadcast(msg, csock):
  for client in connected:
    if client != csock:
      try:
        client.send(msg)
      except:
        client.close()
        remove(client)

def remove(csock):
  if csock in connected:
    connected.remove(csock)

while 1:
  csock, addr = sock.accept()
  connected.append(csock)
  threading.Thread(target=clientthr, args=(csock, addr)).start()

csock.close()
sock.close()
