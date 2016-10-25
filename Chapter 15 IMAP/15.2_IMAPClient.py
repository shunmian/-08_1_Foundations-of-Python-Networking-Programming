import getpass, sys
from imapclient import IMAPClient


def main():
    if len(sys.argv) !=3:
        print("usage: {} hostname, username".format(sys.argv[0]))
        sys.exit(2)

    SERVER, USERNAME = sys.argv[1:]
    c = IMAPClient(SERVER,ssl=True)

    try:
        c.login(USERNAME, getpass.getpass())
    except c.Error as e:
        print('Could not log in:', e)
    else:
        print('Capabilities {}'.format(c.capabilities()))
        print('Listing mailboxes ')
        data = c.xlist_folders()
        for flags, delimiter, folder_name in data:
            print('{:30s} {} {}'.format(''.join(str(flags)), delimiter, folder_name))
    finally:
        c.logout()

if __name__=='__main__':
    main()

"""
输出
Capabilities: ('IMAP4REV1', 'UNSELECT', 'IDLE', 'NAMESPACE', 'QUOTA', 'XLIST', 'CHILDREN', 'XYZZY',
'SASL-IR', 'AUTH=XOAUTH')
Listing mailboxes:
\HasNoChildren					/ INBOX
\HasNoChildren					/ Personal
\HasNoChildren					/ Receipts
\HasNoChildren					/ Travel
\HasNoChildren					/ Work
\Noselect \HasNoChildren        / [Gmail]
\HasChildren \HasNoChildren		/ [Gmail]/All Mail
\HasNoChildren					/ [Gmail]/Drafts
\HasChildren \HasNoChildren		/ [Gmail]/Sent Mail
\HasNoChildren					/ [Gmail]/Spam
\HasNoChildren					/ [Gmail]/Starred
\HasChildren \HasNoChildren		/ [Gmail]/Trash
"""

