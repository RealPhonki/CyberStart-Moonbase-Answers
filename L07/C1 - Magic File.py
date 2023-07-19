#
# Find the valid png file in the /tmp directory using magic bytes.
# The code is hidden in this file.
#

import os

def is_valid_png(filepath):
	with open(filepath, 'rb') as file:
		header = file.read(8)

	return header == b'\x89PNG\r\n\x1a\n'

def find_valid_png():
	for filename in os.listdir('/tmp'):
		filepath = os.path.join('/tmp', filename)

		if is_valid_png(filepath):
			with open(filepath, 'rb') as f:
				[print(line) for line in f]

find_valid_png()
