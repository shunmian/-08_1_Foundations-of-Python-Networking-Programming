import zen_utils, asyncio

@asyncio.coroutine
def handle_conversation(reader,writer):
    address = writer.get_extra_info('peername')
    print('Accepted connection form {}'.format(address))
    while True:
        data = b''
        while not data.endswith(b'?'):
            more_data = yield from reader.read(4096)
            if not more_data:
                if data:
                    print('Client {} send {!r} but then closed',format(address,data))
                else:
                    print('Client {} closed socket normally'.format(address))
                return
            data += more_data
        answer = zen_utils.get_answer(data)
        writer.write(answer)


if __name__=='__main__':
    address = zen_utils.parse_command_line(('asyncio server using callbacks'))
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_conversation,*address)
    server = loop.run_until_complete(coro)
    print('Listening at {}'.format(address))
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()