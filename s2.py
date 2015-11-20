# author: Sharon Jerop Kipruto 
# email: jerop@mit.edu
# version Thursday, January 22nd, 2015 0325

import json
import requests

# POSTing a JSON dictionary with the key token to fetch haystack
keys = {'token':"b52GtaejQD"}
info = json.dumps(keys)
response = requests.post("http://challenge.code2040.org/api/haystack", info)
print response.text

# identifying the needle and the haystack 
needle = response.json().values()[0]['needle']
haystack = response.json().values()[0]['haystack']

# locating the index of the needle in the haystack
index = None
if needle in haystack:
    index = haystack.index(needle)
print 'The index is: ' + str(index)

# POSTing a JSON dictionary to return the index of the needle in the haystack
data = {'token':"b52GtaejQD",'needle': index}
data = json.dumps(data)
result = requests.post('http://challenge.code2040.org/api/validateneedle', data)
print result.text
