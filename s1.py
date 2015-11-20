# author: Sharon Jerop Kipruto 
# email: jerop@mit.edu
# version Thursday, January 22nd, 2015 0316

import json
import requests

# POSTing a JSON dictionary with the key token to fetch the string
keys = {'token':"b52GtaejQD"}
info = json.dumps(keys)
response = requests.post("http://challenge.code2040.org/api/getstring", info)
string = response.json().values()[0]
print 'The string is: ' + string # printing the given string

# reversing the string 
inv_string = string[::-1]
print 'The reversed string is: ' + inv_string # printing the reversed string

# POSTing a JSON dictionary to return the reversed string
data = {'token':"b52GtaejQD", 'string': inv_string}
data = json.dumps(data)
result = requests.post('http://challenge.code2040.org/api/validatestring', data)
print result.text
