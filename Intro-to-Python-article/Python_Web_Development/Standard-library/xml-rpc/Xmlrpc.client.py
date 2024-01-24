import xmlrpc.client

# Create an XML-RPC server proxy
proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

# Call a remote method
result = proxy.add(2, 3)

# Print the result
print("Result:", result)
