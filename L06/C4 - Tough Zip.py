#
# Zip file found at /tmp/alien-sample-42.zip is password protected
# We have worked out they are using one of the passwords
# in the provided list
# Brute force the Zip file to extract to /tmp
#
# Note: The script can timeout. If this occurs try narrowing
# down your search
#
possiblePasswordList = [
  'pant', 'papa', 'paps', 'para', 'path', 'pats', 'paty',
  'pard', 'pare', 'park', 'parr', 'pars', 'part', 'pase',
  'pash', 'past', 'pate', 'peal', 'pean', 'pear', 'peas',
  'pave', 'pawl', 'pawn', 'paws', 'pays', 'peag', 'peak',
  'peck', 'pele', 'peat', 'pech', 'peke', 'perm', 'perp',
  'pecs', 'peds', 'peed', 'peek', 'peel', 'peen', 'peep',
  'pelf', 'pelt', 'pend', 'pens', 'pent', 'pass', 'pepo',
  'pert', 'phon', 'phot', 'phut', 'peer', 'pegs', 'pehs',
  'pere', 'peri', 'perk', 'phat', 'phew', 'phis', 'phiz',
  'perv', 'peso', 'pest', 'pets', 'pews', 'pfft', 'pfui',
  'pial', 'pian', 'pias', 'pica', 'pice', 'pick', 'pics',
  'pied', 'pier', 'pies', 'pigs', 'plan', 'plat', 'ploy',
  'pika', 'pike', 'piki', 'pint', 'piny', 'pion', 'pith',
  'pile', 'pili', 'pill', 'pily', 'pima', 'pimp', 'pina',
  'pine', 'ping', 'pink', 'pins', 'plug', 'plum', 'pein',
  'poll', 'peps', 'pits', 'pity', 'pixy', 'plop', 'plot',
  'pipe', 'pips', 'pipy', 'pirn', 'pish', 'piso', 'pita',
  'pole', 'plow', 'plod', 'pois', 'poke', 'poky',
  'play', 'plea', 'pleb', 'pled', 'plew', 'plex', 'plie',
  'plus', 'pock', 'poco', 'pods', 'poem', 'poet', 'pogy',
]

import zipfile

def try_password(password):
	try:
		with zipfile.ZipFile('/tmp/alien-sample-42.zip', 'r') as zip_ref:
			zip_ref.extractall(path="/tmp", pwd=password.encode('utf-8'))
		return True
	except Exception:
		return False

def brute_force_zip():
  # for some reason this list comprehension doesn't work
  # return [password for password in possiblePasswordList if try_password(password)][0]
	for password in possiblePasswordList:
		if try_password(password):
			return password

password = brute_force_zip()
