import socket

address = ("localhost", 9999)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(address)

sock.listen(5)

connected = {}

clientsock = ""
addr = ""

while 1:
  if not connected[str(clientsock)] == str(addr[0]):
    clientsock, addr = sock.accept()
    connected[str(clientsock)] = str(addr[0])
  msg = clientsock.recv(2048).decode('ascii')
  clientsock.send(msg.encode('ascii'))
