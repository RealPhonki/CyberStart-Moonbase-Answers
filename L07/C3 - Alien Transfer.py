#
# Setup server listening on ('localhost', 10000)
# receive data then send data back after XORing with the key
# attackthehumans
#
# If you get an address already in use error then try again in a few
# moments.
#

# ---------------------- WARNING ----------------------
# For some reason this code only works SOMEIMES. If
# this code doesn't work don't complain about it to me.
# It will constantly say "Incorrect code provided", the
# only solution is to keep submitting the code over and
# over again

import socket

# super compressed xor encrypt function because list comprehension is my lord and savior
def xor_encrypt(message, key):
  return bytes([message[i] ^ key[i % len(key)] for i in range(len(message))])

# connect to the server that induces homicidal thoughts
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 10000))
server.listen(1)

while True:
  # accept the server for who it is (its in the closet)
	connection, address = server.accept()

  # listen to the server's problems
	data = connection.recv(1024)
	if not data:
		continue

  # putting a b infront of a string makes it a bytes string
	encrypted_data = xor_encrypt(b"attackthehumans", key)
	connection.sendall(encrypted_data)

	connection.close()
