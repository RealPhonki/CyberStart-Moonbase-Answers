#
# The Tweet Bot API can be found at http://127.0.0.1:8082
#
# GET method sent to that URL:
# ...returns basic info about API
#
# POST method sent to that URL, with:
# - x-api-key:{KEY} in header
# - user={USER} in querystring
# - status-update={TEXT} in querystring
# ...creates a new social media post

from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = 'http://127.0.0.1:8082'
data = {"user": "tweetbotuser", "status-update": "alientest"}
data = urlencode(data).encode('utf-8')

req = Request(url, data=data, headers={'x-api-key': 'tweetbotkeyv1'})

content = urlopen(req).read()
print(content)
