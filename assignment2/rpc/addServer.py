# file: addServer.py
# author: Reilly Parent
# server to add 2 integers
from xmlrpc.server import SimpleXMLRPCServer
import socket

# add method, returns equation as a string
def add(a, b):
    message = (str(a) + " + " + str(b) + " = " + str(a+b))
    return message

hostname = socket.gethostname()

server = SimpleXMLRPCServer((hostname, 8000))
server.register_function(add, "add")
server.serve_forever()
