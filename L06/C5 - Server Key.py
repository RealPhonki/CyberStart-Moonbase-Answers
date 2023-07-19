#
# Send server ('localhost', 10000) GET_KEY to retrieve key,
# user needs to reverse and send back to server to get flag.
# It will change each execution so the
# user can not manually achieve this.
#

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 10000))
client.send("GET_KEY".encode())
client.send(client.recv(1024)[::-1])
print(client.recv(1024))
client.close()
