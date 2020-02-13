# file: multServer.py
# author: Reilly Parent
# server to multiply 2 integers
from xmlrpc.server import SimpleXMLRPCServer
import socket

# multiply method, returns equation as a string
def multiply(a, b):
    message = (str(a) + " * " + str(b) + " = " + str(a*b))
    return message

hostname = socket.gethostname()

server = SimpleXMLRPCServer((hostname, 8000))
server.register_function(multiply, "multiply")
server.serve_forever()
