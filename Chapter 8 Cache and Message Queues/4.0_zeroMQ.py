import zmq,argparse

def server():
    context = zmq.Context()
    sock = context.socket(zmq.REP)
    sock.bind('tcp://127.0.0.1:1061')

    while True:
        data = sock.recv()
        sock.send(data)

def client():
    context = zmq.Context()
    sock = context.socket(zmq.REQ)
    sock.connect('tcp://127.0.0.1:1061')

    message = b'Hello, world!'
    sock.send(message)
    reply = sock.recv()
    print("received: {}".format(reply))


if __name__== "__main__":
    parser = argparse.ArgumentParser(description="zero message queue echo")
    choices = {"server":server,"client":client}
    parser.add_argument("role",choices=choices,help='the role, either server or client')

    args = parser.parse_args()
    function = choices[args.role]
    function()
