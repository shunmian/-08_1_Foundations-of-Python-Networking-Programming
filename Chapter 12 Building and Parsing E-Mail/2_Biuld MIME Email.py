import email.message, email.policy, email.utils, mimetypes, argparse, sys

plain = """Hello,
This is a MiME Message from Chapter 12.
= Anonymous """

html = """<p>Hello,</p>
<p>This is a <b> test message</b> from Chapter 12.</p>
<p>- <i>Anonymous</i></p>"""

img = """<p> This is the smallest possible blue GIF:</p>
<img src ="cid:{}" height = "80" width = "80">"""



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