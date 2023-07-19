#
# Write a script that connects to 'localhost' port 10000
# You then need to send a command to list the files in the /tmp directory
#

# another easy challenge
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("127.0.0.1", 10000))
clientsocket.send("ls -al /tmp\n".encode())
print(clientsocket.recv(1024).decode())
