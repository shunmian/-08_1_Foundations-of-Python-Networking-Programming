import rpyc

def main():
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port = 18861)
    t.start()

class MyService(rpyc.Service):
    def exposed_line_counter(self, fileobj, function):      # let client call the exposed_method
        print('Client has invoked exposed_line_counter()')  # pass the filobj ID back to client to call the function.
        for linenum, line in enumerate(fileobj.readlines()):
            function(line)
        return linenum+1

if __name__ == '__main__':
    main()





