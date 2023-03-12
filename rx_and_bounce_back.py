# receiver code: This receives data and bounces it back to sender
import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server's address and port
address_n_port = ('192.168.56.1', 9911)
sock.bind(address_n_port)
data = 'start'
while len(data) != 0:
    # Wait for a client to send data
    data, client_address = sock.recvfrom(4096)  # where 4096 is the amount of data in bytes
    # recvfrom gets the address as well as the data
    sock.sendto(data, client_address)  # sendto sends the data to the extracted address
    print(data)
