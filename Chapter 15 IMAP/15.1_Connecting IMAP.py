import getpass, imaplib, sys

def main():
    if len(sys.argv) !=3:
        print("usage: {} hostname, username".format(sys.argv[0]))
        sys.exit(2)

    SERVER, USERNAME = sys.argv[1:]
    m = imaplib.IMAP4_SSL(SERVER)
    m.login(USERNAME,getpass.getpass())

    try:
        print('Capabilities {}'.format(m.capability()))
        print('Listing mailboxes ')
        status, data = m.list()
        print('Status: {}'.format(status))
        print('Data:')
        for datum in data:
            print(repr(datum))
    finally:
        m.logout()

if __name__=='__main__':
    main()

"""
Capabilities: ('IMAP4REV1', 'UNSELECT', 'IDLE', 'NAMESPACE', 'QUOTA',
 'XLIST', 'CHILDREN', 'XYZZY', 'SASL-IR', 'AUTH=XOAUTH')
Listing mailboxes
Status: 'OK'
Data:
b'(\\HasNoChildren) "/" "INBOX"'
b'(\\HasNoChildren) "/" "Personal"'
b'(\\HasNoChildren) "/" "Receipts"'

"""