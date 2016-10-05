import socket, ssl,argparse

def client(host,port,cafile=None):
    purpose = ssl.Purpose.SERVER_AUTH
    context = ssl.create_default_context(purpose,cafile=cafile)

    raw_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    raw_sock.connect((host, port))

    ssl_sock = context.wrap_socket(raw_sock,server_hostname=host)
    print('SSL client binding at: {}, connecting to: {}'.format(ssl_sock.getsockname(),ssl_sock.getpeername()))

    data = b''
    while True:
        more = ssl_sock.recv(4096)
        if not more:
            break;
        data += more
    ssl_sock.recv()
    print('SSL client receive message: {}'.format(data.decode('utf-8')))
    ssl_sock.close()
    print('SSL client closed')

def server(host,port,certificate,cafile=None):
    purpose = ssl.Purpose.CLIENT_AUTH
    context = ssl.create_default_context(purpose,cafile=cafile)
    context.load_cert_chain(certificate)

    raw_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    raw_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    raw_sock.bind((host,port))
    raw_sock.listen(1)
    print('server listen at: {}'.format(raw_sock.getsockname()))

    raw_conn, client = raw_sock.accept()
    ssl_sock = context.wrap_socket(raw_conn,server_side=True)
    print('SSL server bindigg at: {}'.format(ssl_sock.getsockname()))
    ssl_sock.sendall(('Beatiful is better than ugly').encode('utf-8'))
    ssl_sock.close()
    print('SSL server closed')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SSL demonstration')
    choices = ('server','client')
    parser.add_argument('role',choices=choices,help='the server or client role')
    parser.add_argument('host',help='the server\'s interface or client\'s host)')
    parser.add_argument('port',help='port number',default=1060,type=int)
    parser.add_argument('-ca',help='the Certificate Authorities')
    parser.add_argument('-c',help='server\'s certificate')

    args = parser.parse_args()

    if args.role == 'server':
        server(args.host,args.port,args.c,args.ca)
    else:
        client(args.host,args.port,args.ca)



