import  xmlrpc.client

def main():
    proxy = xmlrpc.client.ServerProxy('http://127.0.0.1:7001')
    multicall = xmlrpc.client.MultiCall(proxy)
    multicall.addtogether('x','y','z')
    multicall.addtogether(20,30,4,1)
    multicall.quadratic(2,-4,0)
    multicall.remote_repr({'name': 'Arthur',
                             'data':{'age':42,'sex':'M'}})

    for answer in multicall():
        print(answer)

if __name__ == '__main__':
    main()


