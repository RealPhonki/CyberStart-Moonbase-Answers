#
# Alien Signal API listening on http://127.0.0.1:8082
# Use HTTP GET with x-api-key header to get signal
# We have narrowed down the key to be in the range of 5500 to 5600
# Note: The script can timeout. If this occurs try narrowing
# down your search
#

from urllib.request import Request, urlopen
req = Request('http://127.0.0.1:8082')

for i in range(5500, 5601):
  req.add_header('x-api-key', str(i))
  content = urlopen(req).read()
  print(content)
