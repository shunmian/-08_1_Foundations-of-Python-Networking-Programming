import socket,struct,argparse

header_struct = struct.Struct('!I')


def recvall(sock,length):

    blocks = b''
    while length:
        block = sock.recv(length)
        if not block:
            raise RuntimeError('length of bytes: expected {}, received {}'.format(length,len(block)))
        length -= len(block)
        blocks += block
    return blocks


def get_block(sock):
    block_length = recvall(sock,header_struct.size)
    (block_length,) = header_struct.unpack(block_length)
    block_data = recvall(sock,block_length)
    return block_data


def put_block(sock,message):
    block_length = len(message)
    block_length = header_struct.pack(block_length)
    sock.send(block_length)
    sock.send(message.encode('utf-8'))


def server(address):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind(address)
    print('Server binding at: {}'.format(address))
    sock.listen(1)

    conn, client = sock.accept()
    conn.shutdown(socket.SHUT_WR)

    while True:
        block = get_block(conn)
        if not block:
            print('Server receive data complete')
            break
        print('Block: {}'.format(block.decode('utf-8')))

    conn.close()
    sock.close()


def client(address):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(address)
    print('Client binding at: {}'.format(address))
    print('Client binding to: {}'.format(sock.getpeername()))
    sock.shutdown(socket.SHUT_RD)
    put_block(sock, 'Beautiful is better than ugly.\n')
    put_block(sock, 'Explicit is better than implicit.\n')
    put_block(sock, 'Simple is better than complex.\n')
    put_block(sock, '')
    print('Client send finished')
    sock.close()

if __name__ == '__main__':
    choices = {'server':server,'client':client}
    parser = argparse.ArgumentParser(description="TCP framing: no response")
    parser.add_argument('role',choices=choices,help='choose server or client')
    parser.add_argument('address',help='the server address',nargs='?',default=(('127.0.0.1'),1060))
    args = parser.parse_args()
    function = choices[args.role]
    function(args.address)