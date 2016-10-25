import getpass, sys, email
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
        print('Login succesfully')
        print_information(c, FOLDERNAME)
    finally:
        c.logout()

def print_information(c,foldername):

    c.select_folder(foldername,readonly=True)
    msgdict = c.fetch('1:*',['BODY.PEEK[]'])

    for message_ID, message in list(msgdict.items()):
        e = email.message_from_bytes(message[b'BODY[]'])
        print(message_ID, e['From'])
        payload = e.get_payload()
        if isinstance(payload,list):
            part_content_types = [part.get_content_type() for part in payload]
            print(' Parts:', ' '.join(part_content_types), '...')
        else:
            print(' ', ' '.join(payload[:60].split()), '...')

if __name__=='__main__':
    main()



