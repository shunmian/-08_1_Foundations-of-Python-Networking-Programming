import argparse, email.policy, sys

def main(binary_file):
    policy = email.policy.SMTP
    message = email.message_from_binary_file(binary_file,policy=policy)
    for header in ['From', 'To', 'Date', 'Subject']:                    #header
        print(header + ':', message.get(header,'(none)'))
    print()

    try:                                                                #body
        body = message.get_body(preferencelist=('plain','html'))
    except KeyError:
        print('<This message lacks a printable text or HTML body>')
    else:
        print(body.get_content())


    for part in message.walk():                                         #attachment
        cd = part['Content-Disposition']
        is_attachment = cd and cd.split(';')[0].lower() == 'attachment'
        if not is_attachment:
            continue

        content = part.get_content()
        print('* {} attachment named {!r}: {} object of length {}'.format(part.get_contetn_type().part.get_filename(),type(content).__name__,len(content)))


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Build, print a MIME email')
    parser.add_argument('filename', nargs='?', help='File containing an email')
    args = parser.parse_args()

    if args.filename is None:
        main(sys.sydin.buffer)
    else:
        with open(args.filename,'rb') as f:
            main(f)
