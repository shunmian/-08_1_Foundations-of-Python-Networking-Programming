import zen_utils,socket,random,argparse

def client(address, cause_error=False):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.connect(address)
    print('client binding at: {}, to: {}'.format(sock.getsockname(),sock.getpeername()))
    aphorisms = list(zen_utils.aphorisms)
    if cause_error:
        sock.sendall(aphorisms[0][:-1])
        return

    for aphorism in random.sample(aphorisms,3):
        sock.sendall(aphorism)
        print(aphorism,zen_utils.recv_until(sock,b'.'))

    sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='client')
    parser.add_argument('host',help='hostname or IP')
    parser.add_argument('-p',metavar='port',type=int,default=1060,help='the port number')
    args = parser.parse_args()
    address = (args.host,args.p)
    client(address)
