from ftplib import FTP
import os,sys

def main():

    fname = 'linux-1.0.tar.gz'
    if os.path.exists(fname):
        raise IOError('refusing to overwrite your {} file'.format(fname))

    ftp = FTP('ftp.kernel.org')
    ftp.login()
    ftp.cwd('/pub/linux/kernel/v1.0')
    ftp.voidcmd('TYPE I')

    socket, size = ftp.ntransfercmd('RETR linux-1.0.tar.gz')
    nbytes = 0

    f = open(fname,'wb')

    while True:
        data = socket.recv(4096)
        if not data:
            break
        f.write(data)
        nbytes +=len(data)
        print('\rdownloading: {:.2%}'.format(nbytes/size), end='')
        sys.stdout.flush()

    f.close()
    socket.close()
    ftp.voidresp()
    ftp.quit()

if __name__=='__main__':
    main()