import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocode(address):

     path = '{}?address={}&sensor=false'.format(base,quote_plus(address))
     connection = http.client.HTTPConnection('maps.google.com')
     connection.request('GET', path)
     rawreply = connection.getresponse().read()  # bytes
     print(type(rawreply))
     reply = json.loads(rawreply.decode('utf-8')) # byte to string to dict
     print(type(reply))
     print(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'
    geocode(address)