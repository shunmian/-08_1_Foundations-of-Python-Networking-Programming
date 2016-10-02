import argparse,socket,sys

def connect_to(hostname_or_IP):

    try:
        infolist=socket.getaddrinfo(hostname_or_IP,'www',0,socket.SOCK_STREAM,0,socket.AI_ADDRCONFIG|socket.AI_V4MAPPED|socket.AI_CANONNAME)
    except socket.gaierror as e:
        print("Name service failure:",e.args[1])
        sys.exit(1)
    else:
        print("infolist get successful: {}".format(infolist))


    info = infolist[0]
    sock = socket.socket(*info[0:3])
    try:
        sock.connect(*info[4:])
    except socket.error as e:
        print('client connectio error: {}'.format(e))
    else:
        print('{} is listening on port 80'.format(info[4:]))

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('hostname',help='the hostname or IP for connection')
    arg = parser.parse_args()
    connect_to(arg.hostname)
