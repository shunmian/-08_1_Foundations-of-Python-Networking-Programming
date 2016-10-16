from jsonrpclib import Server

def main():
    proxy = Server('http://127.0.0.1:7001')
    print(proxy.lengths(*['hi',27,'itsgoodday']))

if __name__ == '__main__':
    main()


