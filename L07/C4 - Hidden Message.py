#
# One of the agents has intercepted a file from the aliens
# The flag is hidden in large amount of non alphanumeric characters.
# The file lives at /tmp/destroymoonbase.gif
#

with open("/tmp/destroymoonbase.gif", "r") as f:
  contents = f.read().replace("$", '').replace("#", '')
  print(contents)
