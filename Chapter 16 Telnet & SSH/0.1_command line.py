import subprocess

def test1():
    args = ['echo', 'Sometimes', '*', 'is just an asterisk']
    subprocess.call(args)

def test2():
    while True:
        args = input('[ ').strip().split()
        if args is None:
            continue
        elif args == ['exit']:
            break
        elif args[0] == 'show':
            print(args[1:])
        else:
            try:
                subprocess.call(args)
            except Exception as e:
                print(e)

if __name__=='__main__':
    test2()


