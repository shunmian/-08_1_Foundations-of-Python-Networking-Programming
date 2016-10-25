import getpass, sys
from imapclient import IMAPClient

def main():
    if len(sys.argv) !=4:
        print("usage: {} hostname, username foldername".format(sys.argv[0]))
        sys.exit(2)

    SERVER, USERNAME, FOLDERNAME = sys.argv[1:]
    c = IMAPClient(SERVER,ssl=False)

    try:
        c.login(USERNAME, getpass.getpass())
    except c.Error as e:
        print('Could not log in:', e)
    else:
        select_dict = c.select_folder(FOLDERNAME,readonly=True)
        for k,v in sorted(select_dict.items()):
            print('%s: %r' % (k,v))
    finally:
        c.logout()

if __name__=='__main__':
    main()

"""
输出
EXISTS: 3
PERMANENTFLAGS: ('\\Answered', '\\Flagged', '\\Draft', '\\Deleted',
                 '\\Seen', '\\*')
READ-WRITE: True
UIDNEXT: 2626
FLAGS: ('\\Answered', '\\Flagged', '\\Draft', '\\Deleted', '\\Seen')
UIDVALIDITY: 1
RECENT: 0
"""

