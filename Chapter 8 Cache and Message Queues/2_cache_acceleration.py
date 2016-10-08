
import memcache,random,timeit,time

def fetch_square(mc,n):
    data = mc.get('sq:{}'.format(n))
    if data is None:
        time.sleep(0.001)
        data = n*n
        mc.set('sq:{}'.format(n),data)
    return data

def main():
    mc = memcache.Client(['127.0.0.1:11211'])

    def make_request():
        fetch_square(mc, random.randint(0, 5000))

    print('Ten successive runs:')
    for i in range(1,11):
        print('{:.2f}s '.format(timeit.timeit(make_request,number=2000)), end ='')

if __name__== "__main__":
    main()

#output:
# Ten successive runs:
# 4.60s 3.13s 2.40s 1.68s 1.30s 1.08s 0.84s 0.75s 0.66s 0.62s
