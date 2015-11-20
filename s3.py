# author: Sharon Jerop Kipruto 
# email: jerop@mit.edu
# version Thursday, January 22nd, 2015 0325

import json
import requests

# POSTing a JSON dictionary with the key token to fetch the prefix and array
keys = {'token':"b52GtaejQD"}
info = json.dumps(keys)
response = requests.post("http://challenge.code2040.org/api/prefix", info)
print response.text

# generating an array of strings that do not start with a particular prefix
array = response.json().values()[0]['array']
prefix = response.json().values()[0]['prefix']
array = [string for string in array if string.startswith(prefix, 0, len(string)) == False]

# POSTing a JSON dictionary to return the generated array
data = {'token':"b52GtaejQD",'array': array}
data = json.dumps(data)
result = requests.post('http://challenge.code2040.org/api/validateprefix', data)
print result.text
