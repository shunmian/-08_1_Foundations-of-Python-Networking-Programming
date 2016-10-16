from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

def main():
    server = SimpleJSONRPCServer(('127.0.0.1',7001))    #create JSON Server
    server.register_introspection_functions()           #enable introspection
    server.register_function(lengths)
    print('server in running......')
    server.serve_forever()                              #run forever


def lengths(*args):
    '''Measure the length of each argument'''
    results = []

    for arg in args:
        try:
            arglen = len(arg)
        except TypeError:
            arglen = None
        results.append((arg,arglen))
    return results


if __name__ == '__main__':
    main()





