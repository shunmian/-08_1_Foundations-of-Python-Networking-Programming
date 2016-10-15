from ftplib import FTP
import os,sys

def main_list1():
    ftp = FTP('ftp.ibiblio.org')
    ftp.login()
    ftp.cwd('/pub/academic/astronomy/')
    entries = ftp.nlst()        #nlst just list the file name, no other information
    ftp.quit()

    print(len(entries),"entries:")
    for entry in entries:
        print(entry)

def main_list2():
    ftp = FTP('ftp.ibiblio.org')
    ftp.login()
    ftp.cwd('/pub/academic/astronomy/')
    entries = []
    ftp.dir(entries.append)     #dir has more information
    ftp.quit()

    print(len(entries),"entries:")
    for entry in entries:
        print(entry)

if __name__=='__main__':
    main_list2()