#
# Write a script that makes HTTP requests to the server
# http://127.0.0.1:8082/selfdestruct until the numbers match
# and read the response to get the flag.
# You can easily run out of execution time in this challenge.
# You will need to check the response and stop your attack
# once you see the flag.
#

# import request module
from urllib.request import Request, urlopen

# make a request instance
req = Request("http://127.0.0.1:8082/selfdestruct")

# repeat a bunch of times
for i in range(100):
  
  # get the content
  content = urlopen(req).read().decode()
 	
  # split the content by newlines
  split_data = content.splitlines()
  
  # get the numbers on the page and print them
  num_1, num_2 = split_data[21], split_data[24]
  print(f"Numbers: {num_1}, {num_2}")
  
  # if the criteria is met then print the flag and stop the loop
  if num_1 == num_2:
    print(f"Flag: {split_data[28]}")
    break
