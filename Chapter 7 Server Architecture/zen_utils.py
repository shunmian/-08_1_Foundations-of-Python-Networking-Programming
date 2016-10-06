import socket,time,argparse

aphorisms = {b'Beautiful is better than?': b'ugly.',
             b'Explicit is better than?': b'implicit.',
             b'Simple is better than?': b'complex.'}


def get_answer(question):
    """Return the string response to a particular Zen-of-Python aphorism"""
    time.sleep(5.0)
    return aphorisms.get(question,b'Error: unknown aphorism')


def parse_command_line(description):
    '''Parse command line and return a socket address.'''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('host',help='the server interface')
    parser.add_argument('-p',help='the port number',type=int,default=1060)
    args = parser.parse_args()
    address = (args.host,args.p)
    return address


def create_srv_socket(address):
    """Build and reuturn a listener server socket."""
    listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    listener.bind(address)
    print('server binding at: {}'.format(address))
    listener.listen(1)
    return listener

def accept_connection_forever(listener):
    """Forever accepting client socket."""
    while True:
        sock, address = listener.accept()
        print('client binding from: {}'.format(address))
        handle_conversation(sock,address)


def handle_conversation(sock,address):
    """Converse with a client over `sock` until they are done talking."""
    try:
        while True:
            handle_requests(sock)
    except EOFError:
        print('client binding fron: {} is closed'.format(address))
    except Exception as e:
        print('client {} error: {}'.format(address,e))
    finally:
        sock.close()

def handle_requests(sock):
    """Recieve a single client request on `sock` and send the answer."""
    question = recv_until(sock, b'?')
    answer = get_answer(question)
    sock.sendall(answer)

def recv_until(sock,suffix):
    """Receive bytes over socket `sock` until we receive the 'suffix'."""
    data = b''
    data += sock.recv(4096)
    if not data:
        raise EOFError('socket closed')
    while not data.endswith(suffix):
        more = sock.recv(4096)
        if not more:
            raise IOError('received {!r}, then socket closed'.format(more))
        data += more
    return data