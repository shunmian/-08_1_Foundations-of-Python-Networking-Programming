import operator, math
from xmlrpc.server import SimpleXMLRPCServer
from functools import reduce

def main():
    server = SimpleXMLRPCServer(('127.0.0.1',7001))  #create ROC Server
    server.register_introspection_functions()        #enable introspection
    server.register_multicall_functions()            #enable mutlcall
    server.register_function(addtogether)            #register 3 functions
    server.register_function(quadratic)
    server.register_function(remote_repr)
    print("Server ready")
    server.serve_forever()                           #server run forever


def addtogether(*things):
    '''Add together everying in the list `things`.'''
    return reduce(operator.add,things)

def quadratic(a,b,c):
    '''Determing `x` values satisfying `a` *x*x + `b`*x + c == 0 '''
    b24ac = math.sqrt(b*b-4.0*a*c)
    return list(set([(-b-b24ac)/2.0*a, (-b+b24ac)/2.0*a]))  #RPC function can only return 1 argument or list

def remote_repr(arg):
    '''Return the `repr()` rendering of the supplied `arg`.'''
    return  arg

if __name__ == '__main__':
    main()





