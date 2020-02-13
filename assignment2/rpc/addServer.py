from xmlrpc.server import SimpleXMLRPCServer

def add(a, b):
    print(str(a) + " + " + str(b) + " = " + str(a+b))
    return a+b

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(add, "add")
server.serve_forever()
