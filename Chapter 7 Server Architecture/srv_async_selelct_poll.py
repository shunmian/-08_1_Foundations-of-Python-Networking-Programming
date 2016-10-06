import zen_utils, select

def all_events_forever(poll_object):
    while True:
        for fd,event in poll_object.poll():
            yield fd,event


def serve(listener):
    sockets = {listener.fileno(): listener}
    addresses = {}
    bytes_received = {}
    bytes_to_send = {}

    poll_object = select.poll()
    poll_object.register(listener,select.POLLIN)

    for fd, event in all_events_forever(poll_object):
        sock = sockets[fd]

        # Socket closed: remove it from our data structures.

        if event & (select.POLLHUP|select.POLLERR|select.POLLNVAL):
            address = addresses.pop(sock)
            rb = bytes_received.pop(sock,b'')
            wb = bytes_to_send.pop(sock,b'')

            if rb:
                print('Client {} sent {} but then closed'.format(address,rb))
            elif wb:
                print('Client {} closed before we send {}'.format(address,wb))
            else:
                print('Client {} closed socket normally'.format(address))
            poll_object.unregister(fd)
            del sockets[fd]

        # New socket: add it to our structures.

        elif sock is listener:
            sock, address = sock.accept()
            print('Accepted connection from {}'.format(address))
            sock.setblocking(False)
            sockets[sock.fileno()] = sock
            addresses[sock] = address
            poll_object.register(sock,select.POLLIN)

        # Incoming data: keep receiving until we see the suffix.

        elif event & select.POLLIN:
            more = sock.recv(4096)
            if not more:
                sock.close()
                continue
            data = bytes_received.pop(sock,b'') + more
            if data.endswith(b'?'):
                bytes_to_send[sock] = zen_utils.get_answer(data)
                poll_object.modify(sock, select.POLLOUT)
            else:
                bytes_received[sock] = data

        # Socket ready to send: keep sending until all bytes are delivered.

        elif event & select.POLLOUT:
            data = bytes_to_send.pop(sock)
            n = sock.send(data)
            if n < len(data):
                bytes_to_send[sock] = data[n:]
            else:
                poll_object.modify(sock,select.POLLIN)


if __name__=='__main__':
    address = zen_utils.parse_command_line(('low-level async server'))
    listener = zen_utils.create_srv_socket(address)
    serve(listener)
