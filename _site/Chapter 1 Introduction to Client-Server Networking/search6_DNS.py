import socket

if __name__ == '__main__':
    host = "www.shunmian.me"
    add = socket.gethostbyname(host)
    print("the host:{}'s IP is: {}".format(host,add))
