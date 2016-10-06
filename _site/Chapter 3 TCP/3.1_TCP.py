import argparse,socket

def recvall(socket, length):
    data = b''
    while len(data)<length:
        more = socket.recv(length-len(data))
        if not more:
            raise EOFError("expected data length:{}; received data length: {}.".format(length,len(more)))
        data += more
    return data

def server(interface, port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    sock.bind((interface,port))
    print('passive socket: {}'.format(sock.getsockname()))
    sock.listen(1)
    while True:
        conn, sockname = sock.accept()
        print('conn: {}'.format(repr(conn)))
        print('sock: {}'.format(repr(sock)))
        print('we\'have receive a connection from {}'.format(sockname))
        print('active socket:{}, client socket:{}'.format(conn.getsockname(),conn.getpeername()))
        data = recvall(conn, 16)
        print('client text: {}'.format(data.decode('utf-8')))
        text = data.decode('utf-8')
        data = text.encode('utf-8')
        conn.sendall(data)
        print('Farewell')
        conn.close()

def client(host, port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((host,port))
    print('client socket:{}'.format(sock.getsockname()))
    text = "Hi,there,goodman"
    data = text.encode('utf-8')
    sock.sendall(data)
    reply = recvall(sock,16)
    print('The server said {}'.format(reply.decode('utf-8')))
    sock.sendto()
    sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    choices = {"server":server,"client":client}
    parser.add_argument("role",choices=choices,help="chose role:server or client")
    parser.add_argument("host",help="the server's interface; client's host")
    parser.add_argument("-p",help="the port number",default="1060",type=int)
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host,args.p)