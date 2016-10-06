import zen_utils
from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn

class ZenHandler(BaseRequestHandler):
    def handle(self):
        zen_utils.handle_conversation(self.request,self.client_address)

class ZenServer(ThreadingMixIn,TCPServer):
    allow_reuse_address = 1

if __name__=='__main__':
    address = zen_utils.parse_command_line("single-threaded server")
    server = ZenServer(address, ZenHandler)
    server.serve_forever()

