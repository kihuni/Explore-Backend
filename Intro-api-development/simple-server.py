from socket import *

def server():
    # Create a socket object
    mysock = socket(AF_INET, SOCK_STREAM)

    # Bind the socket object to a port
    mysock.bind(('localhost', 9000))

    # Listen for incoming connections
    mysock.listen(5)

    while True:
        # Accept incoming connections
        conn, addr = mysock.accept()
        print('Connected to', addr)

        # Receive and print the request from the client
        data = conn.recv(1000)
        print(data.decode())

        # Send a response to the client
        conn.sendall('HTTP/1.1 200 OK\n'.encode())
        conn.sendall('Content-Type: text/html\n'.encode())
        conn.sendall('\n'.encode())
        conn.sendall('<html><body><h1>Hello, world!</h1></body></html>\n'.encode())

        # Close the connection
        conn.close()

    # Close the socket
    mysock.close()