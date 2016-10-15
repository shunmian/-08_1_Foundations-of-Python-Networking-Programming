from ftplib import FTP

def walk_dir(ftp, target_dir):
    source_dir = ftp.pwd()
    try:
        ftp.cwd(target_dir)
    except Exception as e:
        return

    print("{}".format(target_dir))
    names = ftp.nlst()
    for name in names:
        walk_dir(ftp,'{}/{}'.format(target_dir,name))
    ftp.cwd(source_dir)

def main():
    ftp = FTP('ftp.kernel.org')
    ftp.login()
    walk_dir(ftp,'/pub/linux/kernel/Historic/old-versions')
    ftp.quit()

if __name__=='__main__':
    main()