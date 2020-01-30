import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ("localhost", 9999)
sock.bind(address)

sock.listen(5)

while True:
  clientSock, addr = sock.accept()
  recvStr = clientSock.recv(1024)
  sendStr = str(len(recvStr.split(" ")))
  clientSock.send(sendStr.encode("ascii"))
  clientSock.close()
