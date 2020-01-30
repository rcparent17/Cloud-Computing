import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()

address = (hostname, 9999)
sock.bind(address)

sock.listen(5)

while True:
  clientSock, addr = sock.accept()
  print("Got connection with host " + str(addr))
  recvStr = clientSock.recv(1024).decode('ascii')
  lines = recvStr.split("#")
  numLines = str(len(lines))
  words = 0
  chars = 0
  for line in lines:
    words = words + len(line.split())
    chars = chars + len(line)
  sendStr = numLines + "/" + str(words) + "/" + str(chars)
  clientSock.send(sendStr.encode('ascii'))
  clientSock.close()
