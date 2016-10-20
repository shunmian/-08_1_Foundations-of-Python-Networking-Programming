import email.message, email.policy, email.utils

text = '''Hello,
This is a basic message from Chapter 12 - Anonymouse'''

def main():
    message = email.message.EmailMessage(email.policy.SMTP)
    message['To'] = 'shunmian@gmail.com'
    message['From'] = 'Test Sender<sender@example.com>'
    message['Subject'] = 'Text Message, Chapter 12'
    message['Date'] = email.utils.formatdate(localtime=True)
    message['Message-ID'] = email.utils.make_msgid()
    message.set_content(text)
    print(message.as_string())

if __name__=='__main__':
    main()