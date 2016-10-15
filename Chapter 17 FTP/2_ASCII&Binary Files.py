from ftplib import FTP
import os

def main_ASCII():
    if os.path.exists('README'):
        raise IOError('refusing to overwrite your README file')

    ftp = FTP('ftp.kernel.org')
    ftp.login()
    ftp.cwd('/pub/linux/kernel')

    with open('README','w') as f:
        def writeline(data):
            f.write(data)
            f.write(os.linesep)
        ftp.retrlines('RETR README',writeline) #Retrieve data in line mode

    ftp.quit()


def main_byte():

    if os.path.exists("patch8.gz"):
        raise IOError('refusing to overwrite your patch8.gz file')

    ftp = FTP('ftp.kernel.org')
    ftp.login()
    ftp.cwd('/pub/linux/kernel/v1.0')

    with open('patch8.gz', 'wb') as f:
        ftp.retrbinary('RETR patch8.gz',f.write) #Retrieve data in binary mode

    ftp.quit()

if __name__ == '__main__':
    main_byte()

