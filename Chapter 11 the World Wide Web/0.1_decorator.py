

def hello(func):

    def __decorator():
        print('Hello, {}'.format(func.__name__))
        func()
        print('goodbye, {}'.format(func.__name__))
    return __decorator()

@hello
def sing():
    print('I am singing')


if __name__=='__main__':
    sing
