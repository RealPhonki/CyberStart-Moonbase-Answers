#
# Write a script which can connect to the following server
# 'localhost', 10000 over TFP send 'GET_KEY' to download a string.
# The string is compressed with a common algorithm found in many
# websites. Decompress the string and print it to get the flag.
#

import socket
import zlib

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 10000))
print(zlib.decompress(client.recv(1024), 16.zlib+MAX_WBITS)
