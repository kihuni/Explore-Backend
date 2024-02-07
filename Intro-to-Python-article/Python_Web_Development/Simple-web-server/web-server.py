from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the HTTP request handler class
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Read the HTML content from the file
        with open('index.html', 'rb') as file:
            html_content = file.read()

        # Set the response body with the HTML content
        self.wfile.write(html_content)

    def do_POST(self):
        content_length_str = self.headers.get('Content-Length')
        if content_length_str is None:
            self.send_response(400)  # Bad request
            self.end_headers()
            self.wfile.write(b'Content-Length header is missing')
            return
        
        content_length = int(content_length_str)
        post_data = self.rfile.read(content_length)
        print("Received POST data:", post_data.decode('utf-8'))
        
        # Send a success response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'POST request received successfully')

        return

    def do_PUT(self):
        content_length_str = self.headers.get('Content-Length')
        if content_length_str is None:
            content_length_str = '0'
        
        content_length = int(content_length_str)
        put_data = self.rfile.read(content_length)
        print("Received PUT data:", put_data.decode('utf-8'))

        # Send a success response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'PUT request received successfully')

# Define the main function to start the server
def main():
    # Set the server address and port
    server_address = ('', 8080)

    # Create an instance of the HTTP server
    httpd = HTTPServer(server_address, MyRequestHandler)

    # Start the server
    print('Starting server...')
    httpd.serve_forever()

if __name__ == '__main__':
    main()
