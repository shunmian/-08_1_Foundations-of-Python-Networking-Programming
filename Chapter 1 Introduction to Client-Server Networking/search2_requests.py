import requests

def geocode(address):
    parameters = {'address':address,'sensor':'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base,params=parameters) # construct a Request object with get method, the return is Response object
    answer = response.json() #编码json,返回dict,json是一种特殊的dict。
    print(answer)

if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'
    geocode(address)