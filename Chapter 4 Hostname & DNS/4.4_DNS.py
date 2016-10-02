import argparse, dns.resolver

def lookup(name):
    for qtype in 'A','AAAA','CNAME','MX','NS':
        answer = dns.resolver.query(name,qtype,raise_on_no_answer=False)
        if answer.rrset is not None:
            print(answer.rrset)

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Resolve a name using DNS')
    parser.add_argument('name',help='name that you want to lookup in DNS',nargs='?',default='python.org')
    arg = parser.parse_args()
    lookup(arg.name)