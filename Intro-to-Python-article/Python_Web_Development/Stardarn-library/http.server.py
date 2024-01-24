import http.server
import socketserver

# Define the request handler class
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Customize the response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World!')

# Create an HTTP server instance
server_address = ('', 8000)
httpd = socketserver.TCPServer(server_address, MyHTTPRequestHandler)

# Start the server
print('Server running on port 8000...')
httpd.serve_forever()
