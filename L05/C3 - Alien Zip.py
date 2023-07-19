#
# Sample Alien Zip file found at /tmp/alien-zip-2092.zip is password protected
# We have worked out they are using three digit code
# Brute force the Zip file to extract to /tmp
#
# Note: The script can timeout if this occurs try narrowing
# down your search

import zipfile

def try_password(password):
	try:
		with zipfile.ZipFile('/tmp/alien-zip-2092.zip', 'r') as zip_ref:
			zip_ref.extractall(path="/tmp", pwd=password.encode('utf-8'))
		return True
	except Exception:
		return

def brute_force_zip():
  # for some reason this list comprehension doesn't work even though its the same thing???
  # return [str(i).zfill(3) for i in range(1000) if try_password(str(i).zfill(3))][0]
	for i in range(1000):  # password range from 100 to 999
		if try_password(str(i).zfill(3)):
			return str(i).zfill(3)

brute_force_zip()
