from pprint import pprint
import socket

#1.基本用法
infolist = socket.getaddrinfo('gatech.edu','www')
pprint(infolist)

info = infolist[0]
sock = socket.socket(*info[0:3])
pprint(info[4])
sock.connect(info[4])

#1_Bind Your Server to a Port--------------------------------------------

info = socket.getaddrinfo(None,'smtp',0,socket.SOCK_STREAM,0,socket.AI_PASSIVE)
print(info)
info = socket.getaddrinfo(None,53,0,socket.SOCK_DGRAM,0,socket.AI_PASSIVE)
print(info)
info = socket.getaddrinfo('127.0.0.1','smtp',0,socket.SOCK_STREAM,0)
print(info)
info = socket.getaddrinfo('localhost','smtp',0,socket.SOCK_STREAM,0)
print(info)

#2_Connect to a Service---------------------------------------------------
info = socket.getaddrinfo('iana.org','www',0,socket.SOCK_STREAM,0,socket.AI_ADDRCONFIG|socket.AI_V4MAPPED)
print(info)
#output: [(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('192.0.43.8', 80))]
info = socket.getaddrinfo('iana.org','www',0,socket.SOCK_STREAM,0)
print(info)
#output:[(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('192.0.43.8', 80)), (<AddressFamily.AF_INET6: 30>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('2001:500:88:200::8', 80, 0, 0))]

#3_Canonical Hostname-----------------------------------------------------
info = socket.getaddrinfo('iana.org','www',0,socket.SOCK_STREAM,0,socket.AI_CANONNAME)
print(info)

#output:[(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, 'iana.org', ('192.0.43.8', 80)), (<AddressFamily.AF_INET6: 30>, <SocketKind.SOCK_STREAM: 1>, 6, 'iana.org', ('2001:500:88:200::8', 80, 0, 0))]