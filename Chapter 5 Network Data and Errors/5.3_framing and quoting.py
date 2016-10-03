import socket,argparse

def server(address):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind(address)
    print('Server binding at: {}'.format(address))
    sock.listen(1)
    while True:
        conn, client = sock.accept()
        print('Accept client from: {}'.format(conn.getpeername()))
        conn.shutdown(socket.SHUT_WR)
        data = b''
        while True:
            more = conn.recv(8192) #8K
            if not more:
                print('Reach the end of incoming data')
                break
            data += more
        print('Message is:\n{}'.format(data.decode('ascii')))
        conn.close()
    sock.close()

def client(address):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(address)
    sock.shutdown(socket.SHUT_RD)
    print('Client binding at:{}'.format(sock.getsockname()))
    print('Client sending to:{}'.format(sock.getpeername()))
    sock.sendall(b'Beautiful is better than ugly.\n')
    sock.sendall(b'Explicit is better than implicit.\n')
    sock.sendall(b'Simple is better than complex.\n')
    print('Client sending data finished')
    sock.close()

if __name__ == '__main__':
    choices = {'server':server,'client':client}
    parser = argparse.ArgumentParser(description="TCP framing: no response")
    parser.add_argument('role',choices=choices,help='choose server or client')
    parser.add_argument('address',help='the server address',nargs='?',default=(('127.0.0.1'),1060))
    args = parser.parse_args()
    function = choices[args.role]
    function(args.address)



