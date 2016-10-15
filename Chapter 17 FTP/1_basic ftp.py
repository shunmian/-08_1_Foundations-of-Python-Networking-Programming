from ftplib import FTP

def main():

    ftp = FTP('ftp.ibiblio.org')
    print("Welcome: {}".format(ftp.getwelcome()))
    ftp.login()                                     # login anonymously
    print("Current working directory:",ftp.pwd())   #just like pwd in terminal
    ftp.quit()

if __name__=='__main__':
    main()