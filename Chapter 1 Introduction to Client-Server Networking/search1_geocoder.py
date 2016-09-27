from pygeocoder import Geocoder

if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'
    print(type(Geocoder.geocode(address)[0]))
    print(Geocoder.geocode(address)[0].coordinates)


