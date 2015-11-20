# author: Sharon Jerop Kipruto 
# email: jerop@mit.edu

import json
import requests
import datetime

# POSTing a JSON dictionary with the key token to fetch the datestamp
keys = {'token':"b52GtaejQD"}
info = json.dumps(keys)
response = requests.post("http://challenge.code2040.org/api/time", info)
print response.text

# calculating the new timestamp usint the datetime module
datestamp = response.json().values()[0]['datestamp']
interval = response.json().values()[0]['interval']
date = datetime.datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
print date
new_date = datetime.timedelta(seconds=interval) + date
print new_date
iso_date = new_date.isoformat()
print iso_date

# POSTing a JSON dictionary to return the new date in ISO format
data = {'token':"b52GtaejQD",'datestamp': iso_date}
data = json.dumps(data)
result = requests.post('http://challenge.code2040.org/api/validatetime', data)
print result.text
