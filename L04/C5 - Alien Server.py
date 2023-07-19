#
# Connect to alien server ('localhost', 10000)
#
# Then send each of these values...
# USER
# aliensignal
# PASS
# unlockserver
# SEND
# moonbase
# END
# ...and receive the response from each.
#
# Note: You must receive data back from the server after you send each value
#
import socket

messages = ["USER", "aliensignal", "PASS", "unlockserver", "SEND", "moonbase", "END"]

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 10000))

for message in messages:
  clientsocket.send(message.encode())
  print(clientsocket.recv(1024))
