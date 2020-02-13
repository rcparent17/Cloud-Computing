from xmlrpc.server import SimpleXMLRPCServer
import socket

def multiply(a, b):
    message = (str(a) + " * " + str(b) + " = " + str(a*b))
    return message

hostname = socket.gethostname()

server = SimpleXMLRPCServer((hostname, 8000))
server.register_function(multiply, "multiply")
server.serve_forever()
