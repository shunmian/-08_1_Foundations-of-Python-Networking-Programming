import argparse,socket,sys

def server(interface, port, bytecount):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    sock.bind((interface,port))
    print('passive socket: {}'.format(sock.getsockname()))
    sock.listen(1)
    while True:
        conn, sockname = sock.accept()
        byte_received = 0
        bytecount = (bytecount + 15) // 16 * 16
        data = b''
        while byte_received < bytecount:

            more = conn.recv(1024)
            if not more:
                break;
            data += more
            byte_received += len(more)
            print('server receive: {}; progress: {:.2f}%'.format(data.decode('utf-8'), byte_received/bytecount * 100))
            data = data.decode('utf-8').upper().encode('utf-8')
            conn.sendall(data)
            print('server send   : {}; progress: {:.2f}%'.format(data.decode('utf-8'), byte_received/bytecount * 100))
            sys.stdout.flush()
        print('Farewell')
        f = conn.makefile()
        print('file read: {}'.format(f.read()))

        conn.close()

def client(host, port, bytecount):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((host,port))
    bytecount = (bytecount+15)//16*16
    print('client is going to send {} bytes'.format(bytecount))
    byte_sent = 0
    text = 'Hello my friend '
    while byte_sent < bytecount:
        sock.sendall(text.encode('utf-8'))
        byte_sent += len(text)
        print('client send   : {}; progress: {:.2f}%'.format(text,byte_sent/bytecount*100))
        sys.stdout.flush()
    print('client send finished')
    sock.shutdown(socket.SHUT_WR)

    byte_received = 0
    while byte_received < bytecount:
        reply = sock.recv(1024)
        if not reply:
            break
        byte_received += len(reply)
        print('client receive: {}; progress: {:.2f}%'.format(reply.decode('utf-8'),byte_received/bytecount*100))
        sys.stdout.flush()
    print('client receive finished')
    sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    choices = {"server":server,"client":client}
    parser.add_argument("role",choices=choices,help="chose role:server or client")
    parser.add_argument("host",help="the server's interface; client's host")
    parser.add_argument("bytecount",help='the communicating bytenumber between sever and client',nargs='?',default=16,type=int)
    parser.add_argument("-p",help="the port number",default="1060",type=int)
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host,args.p,args.bytecount)