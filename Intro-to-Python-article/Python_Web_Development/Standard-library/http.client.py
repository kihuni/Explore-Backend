import http.client

# Create an HTTP connection
conn = http.client.HTTPSConnection("www.example.com")

# Send a GET request
conn.request("GET", "/")

# Get the response from the server
response = conn.getresponse()

# Print the response status code
print("Status:", response.status)

# Print the response headers
print("Headers:", response.getheaders())

# Print the response body
print("Body:", response.read().decode())

# Close the connection
conn.close()
