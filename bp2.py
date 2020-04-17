# -*-coding:utf-8 -*-

def bp2():
    print('[1] 0-9')
    print('[2] A-Z')
    print('[3] a-z')
    print('[4] 0-9,A-z')
    print('[5] 0-9,a-z')
    print('[6] A-Z,a-z')
    print('[7] 0-9,A-Z,a-z')
    aaa = input('spdtools > ')

    a = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        ]
    b = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
    c = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

    if aaa == '1':
        chars = a
    if aaa == '2':
        chars = b
    if aaa == '3':
        chars = c
    if aaa == '4':
        chars = a + b
    if aaa == '5':
        chars = a + c
    if aaa == '6':
        chars = b + c
    if aaa == '7':
        chars = a + b + c

    print('[1] 4位')
    print('[2] 5位')
    print('[3] 6位')
    bbb = input('spdtools > ')

    if bbb == '1':
        f = open("dic2.txt", 'w')
        f.truncate()
        base = len(chars)
        end = len(chars) ** 4
        for i in range(0, end):
            n = i
            ch0 = chars[int(n % base)]
            n /= base
            ch1 = chars[int(n % base)]
            n /= base
            ch2 = chars[int(n % base)]
            n /= base
            ch3 = chars[int(n % base)]
            f.write(ch3 + ch2 + ch1 + ch0 + '\n')
        f.close()
        print('保存于dic2.txt')
    if bbb == '2':
        f = open("dic2.txt", 'w')
        f.truncate()
        base = len(chars)
        end = len(chars) ** 4
        for i in range(0, end):
            n = i
            ch0 = chars[int(n % base)]
            n /= base
            ch1 = chars[int(n % base)]
            n /= base
            ch2 = chars[int(n % base)]
            n /= base
            ch3 = chars[int(n % base)]
            n /= base
            ch4 = chars[int(n % base)]
            f.write(ch4 + ch3 + ch2 + ch1 + ch0 + '\n')
        f.close()
        print('保存于dic2.txt')
    if bbb == '3':
        f = open("dic2.txt", 'w')
        f.truncate()
        base = len(chars)
        end = len(chars) ** 4
        for i in range(0, end):
            n = i
            ch0 = chars[int(n % base)]
            n /= base
            ch1 = chars[int(n % base)]
            n /= base
            ch2 = chars[int(n % base)]
            n /= base
            ch3 = chars[int(n % base)]
            n /= base
            ch4 = chars[int(n % base)]
            n /= base
            ch5 = chars[int(n % base)]
            f.write(ch5 + ch4 + ch3 + ch2 + ch1 + ch0 + '\n')
        f.close()
        print('保存于dic2.txt')
