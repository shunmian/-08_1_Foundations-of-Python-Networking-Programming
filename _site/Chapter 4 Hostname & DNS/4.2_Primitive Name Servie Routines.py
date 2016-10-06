import socket

print(socket.gethostname())                     #LALdeMacBook-Pro.local
print(socket.getfqdn())                         #laldemacbook-pro.local

print(socket.gethostbyname('cern.ch'))          #188.184.9.234
print(socket.gethostbyaddr('188.184.9.234'))    #('webrlb01.cern.ch', ['234.9.184.188.in-addr.arpa'], ['188.184.9.234'])

print(socket.getprotobyname('UDP'))             #17
print(socket.getservbyname('www'))              #80
print(socket.getservbyport(80))                 #http

print(socket.gethostbyname(socket.getfqdn()))   #192.168.0.101