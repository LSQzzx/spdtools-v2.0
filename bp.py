# -*-coding:utf-8 -*-
import exrex
import sys

web_filter = ['com', 'cn', 'org', 'edu', 'gov', 'www']


def host_para(host):
    if '://' in host:
        host = host.split('://')[1]
    if '/' in host:
        host = host.replace('/', '.')
    return host


def dic_create(host):
    web_dics = host.split('.')

        # 读取正则规则
    f_rule = open('init/rule.ini', 'r')
    rule = ""
    for i in f_rule:
        if '#' != i[0]:
            rule = i

        # 创建字典文件
    f_dic = open('dic.txt', 'w')
    f_dic.truncate()
    f_dic.close()

    for web_dic in web_dics:
        if web_dic not in web_filter:
                # 读取参考密码进行组合
            f_pass = open('init/psck.txt', 'r')
            for dic_pass in f_pass:
                dics = list(exrex.generate(rule.format(web_dic=web_dic, dic_pass=dic_pass.strip('\n'))))
                for dic in dics:
                        # 过滤过于简单的密码
                    if len(dic) > 4:
                        f_dic = open('dic.txt', 'a+')
                        f_dic.write(dic + "\n")
                        f_dic.close()
                        print(dic.strip('\n'))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        dic_create(host_para(sys.argv[1]))
        print('保存于dic.txt')
        sys.exit()
    else:
        print("[*]Usage:python create_dic.py [URL]")