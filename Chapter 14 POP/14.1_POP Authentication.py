import getpass, poplib, sys

def main():
    # if len(sys.argv) !=3:
    #     print("usage: {} hostname username".format(sys.argv[0]))
    #     sys.exit(2)
    #
    # hostname, username = sys.argv[1:]
    # p = poplib.POP3_SSL(hostname)
    # try:
    #     p.user(username)
    #     p.pass_(getpass.getpass())
    #
    # except poplib.error_proto as e:
    #     print("Login fail: {}".format(e))
    #
    # else:
    #     print("Your message: {}".format(p.stat()))
    # finally:
    #     p.quit()
    import poplib
    from email import parser

    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user('shunmian@gmail.com')
    pop_conn.pass_('Fzyr.3513.198822')
    # Get messages from server:
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    # Concat message pieces:
    messages = ["\n".join(mssg[1]) for mssg in messages]
    # Parse message intom an email object:
    messages = [parser.Parser().parsestr(mssg) for mssg in messages]
    for message in messages:
        print
        message['subject']
    pop_conn.quit()

if __name__=="__main__":
    main()

