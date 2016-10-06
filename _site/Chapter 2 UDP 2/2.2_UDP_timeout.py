import argparse,socket
from datetime import datetime
import random

MAX_BYTES = 65535

def server(interface, port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((interface,port))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        if random.random()<0.5:
            print('Pretending to drop packet from {}'.format(address))
            continue
        text = data.decode('utf-8')
        print('The client at {} says{!r}'.format(address,text))
        text = 'Your data is {} bytes long'.format(len(text))
        data = text.encode('utf-8')
        sock.sendto(data,address)

def client(hostname, port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.connect((hostname,port))
    text = 'The time is {}'.format(datetime.now())
    data = text.encode('utf-8')
    print('The OS assigned me the address {}'.format(sock.getsockname()))
    delay = 0.1;
    while True:
        sock.send(data)
        sock.settimeout(delay)
        try:
            data= sock.recv(MAX_BYTES)  # Dangerous!
        except socket.timeout as e:
            delay *=2
            print('delay time: {}'.format(delay))
            if delay >=20:
                raise RuntimeError("I think the server is down")
        else:
            break
    text = data.decode('utf-8')
    print('The server replied {!r}'.format(text))

if __name__ == '__main__':
    choices = {'client':client,'server':server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally,'
                                     'pretending packets are often dropped')
    parser.add_argument('role',choices=choices,help='which role to play')
    parser.add_argument('hostname',help='interface the server listens at;'
                        'host the client sends to')
    parser.add_argument('-p',metavar='PORT',type = int, default = 1060,help = 'UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.hostname,args.p)


