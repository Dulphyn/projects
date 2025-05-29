# Nicolas Valdez Thu May 29 16:38:50 2025
# MyServer
# Host an iterative server
# Input(s)
# Client connection
# Output
# Display "Hello World" to client's stdout

import socket

# Welcoming Statement
print('Host an iterative server')

# Server IP and port number
server_ip=''
server_port=12345
server_address=(server_ip,server_port)

# Max queue size
max_queue_size=5

# Handle client connection request
def handle_connection(client_connection):
    recv_size=1024
    request=client_connection.recv(recv_size) # Taken from https://ruslanspivak.com/lsbaws-part3/#fn:1, not fully sure how its relevant
    print(request.decode())
    response=b'Hello, world!'
    client_connection.sendall(response)

# Serve client
def serve_client(server_address,max_queue_size):
    sock=socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Used options from https://ruslanspivak.com/lsbaws-part3/#fn:1
    sock.bind(server_address)
    sock.listen(max_queue_size)
    print(f'Serving on port {server_address[1]}.')

    # Loop server
    while True:
        client_connection,client_address=sock.accept()
        handle_connection(client_connection)
        client_connection.close()
    
if __name__=='__main__':
    serve_client(server_address,max_queue_size)

# Ending Note
print('Program Ends')