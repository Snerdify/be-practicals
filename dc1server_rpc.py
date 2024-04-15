from xmlrpc.server import SimpleXMLRPCServer
import math


def factorial(n: int):
    return math.factorial(n)


server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(factorial, "factorial")
server.serve_forever()   
