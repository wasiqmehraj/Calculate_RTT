import time
import socket

# Create a UDP socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create the socket
except socket.error as msg:
    print("Socket creation failed. ", msg)  # error handling

# Set the server's address and port
rx_address = ('192.168.56.1', 9911)

n = 5  # no. of times, you want to send the message
t = n
time_sent = time.time()     # record the time you sent the message

while n != 0:
    # Send data to the rx
    message = b'<<<<<<<<<<<<<<<<<<  test message from sender  >>>>>>>>>>>>>>>>>>'
    sock.sendto(message, rx_address)
    print('Send Success')

    # Wait for the rx to send the data back
    data = sock.recv(4096)
    print('Receive Success')

    n -= 1
time_received = time.time()

# Calculate the round trip time (RTT)
rtt = time_received - time_sent
rtt = rtt / t
# Print the RTT
print(" Average Round trip time client: {} seconds".format(rtt))
