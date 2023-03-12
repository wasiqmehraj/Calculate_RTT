# Sender code:
# to send a single message to the rx

import socket

# Create a UDP socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as msg:
    print("Socket creation failed. ", msg)

# Set the server's address and port
address = ('192.168.56.1', 9911)

# Send data to the server
message = b'#################test message from client#################'

sock.sendto(message, address)
print('Send Success')



