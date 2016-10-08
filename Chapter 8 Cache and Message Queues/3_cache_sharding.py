import hashlib

def alpha_shard(word):
    """Do a poor job of assigning data to servers by using first letters."""
    if word[0] < 'g':       # abcdef
        return 'server0'
    elif word[0] < 'n':     # ghijklm
        return 'server1'
    elif word[0] < 't':     # nopqrs
        return 'server2'
    else:                   # tuvwxyz
        return 'server3'

def hash_shard(word):
    '''Assign data to servers using Python's built-in hash() function.'''
    return 'server{}'.format(hash(word)%4)

def md5_shard(word):
    """Assign data to servers using a public hash algorithm."""
    data = word.encode('utf-8')
    return 'server{}'.format(hashlib.md5(data).digest()[-1] % 4)


def main():
    words = open('words.txt').read().split()

    for function in alpha_shard, hash_shard, md5_shard:
        shardingDict = {"server0": 0, "server1": 1, "server2": 2, "server3": 3}
        for word in words:
            server = function(word)
            shardingDict[server] +=1

        print("function: {}".format(function.__name__))
        for k,v in shardingDict.items():
            print('{}: {:.0f}% '.format(k, 100*v/len(words)))
        print('')

if __name__== "__main__":
    main()

# output:
# function: alpha_shard
# server1: 20%
# server2: 32%
# server0: 33%
# server3: 15%
#
# function: hash_shard
# server1: 25%
# server2: 25%
# server0: 25%
# server3: 25%
#
# function: md5_shard
# server1: 25%
# server2: 25%
# server0: 25%
# server3: 25%