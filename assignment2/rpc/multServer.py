from xmlrpc.server import SimpleXMLRPCServer

def multiply(a, b):
    print(str(a) + " * " + str(b) + " = " + str(a*b))
    return a*b

server = SimpleXMLRPCServer(("localhost", 8001))
server.register_function(multiply, "multiply")
server.serve_forever()
