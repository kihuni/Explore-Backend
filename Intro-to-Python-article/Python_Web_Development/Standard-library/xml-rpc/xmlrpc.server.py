from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create an XML-RPC server
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Define a function to be exposed via XML-RPC
    def add(x, y):
        return x + y

    # Register the function with the server
    server.register_function(add, 'add')

    print("XML-RPC server is running on http://localhost:8000")

    # Run the server indefinitely
    server.serve_forever()
