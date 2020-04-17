import requests
import json
import re
import os
import sys
import webbrowser
import modle.spd
import time
import modle.gjdip
import bp2
import modle.bash64mabiao
import modle.dlip

os.system("clear")
os.system("cls")

print('               _ _              _     ')
print(' ___ _ __   __| | |_ ___   ___ | |___ ')
print('/ __| \'_ \\ / _` | __/ _ \ / _ \\| / __|')
print('\\__ \\ |_) | (_| | || (_) | (_) | \\__ \\')
print('|___/ .__/ \__,_|\__\___/ \___/|_|___/')
print('    |_|                               ')

print('[1] ip经纬度定位')
print('[2] 经纬度地图定位')
print('[3] 查看本机公网ip')
print('[4] 端口用途查询（第一次使用请先输入0）')
print('[5] 高精度ip经纬度定位（友情提供）')
print('[6] 生成爆破字典')
print('[7] 爆破神器')
print('[8] base64编码/解码')
print('[9] base64码表生成（生成规则请自行改源码）')
print('[10] 爬取国内高匿代理ip')
print('[spider]彩蛋')
print('[exit] 退出')
print()
while True:
    choice = input('spdtools > ')
    if choice == '1':
        ip = input('请输入ip地址：')
        url = 'https://restapi.amap.com/v3/ip?key=3e105e2105fafafb3c52d7fcf75ed5cf&ip=' + ip
        res = requests.get(url)
        json_data = json.loads(res.text)
        print('-----------------------------------------------')
        print('经纬度：',json_data["rectangle"])

        url2 = 'https://restapi.amap.com/v3/geocode/regeo?key=3e105e2105fafafb3c52d7fcf75ed5cf&location=' + json_data["rectangle"]
        res2 = requests.get(url2)
        json_data2 = json.loads(res2.text)
        title = str(json_data2)
        pattern = re.compile(r'[\u4e00-\u9fa5]+')
        result = pattern.findall(title)
        print()
        print("经纬度转地址：",result)
        print('-----------------------------------------------')
    elif choice == '2':
        result2 = input('请输入经纬度(只输入分号左边部分)：')
        url4 = 'https://restapi.amap.com/v3/staticmap?location=' + result2.replace(" ", "") + '&zoom=10&size=1200*550&markers=mid,,A:' + result2.replace(" ", "") + '&key=3e105e2105fafafb3c52d7fcf75ed5cf'
        webbrowser.open(url4, new=0, autoraise=True)
    elif choice == '3':
        url3 = 'http://ifconfig.co/json'
        res3 = requests.get(url3)
        json_data3 = json.loads(res3.text)
        print('-----------------------------------------------')
        print('本机公网ip：',json_data3["ip"])
    elif choice == '4':
        port = input('请输入端口：')
        dkcx = "whatportis " + port
        os.system(dkcx)
    elif choice == '0':
        os.system("pip install whatportis")
    elif choice == '5':
        modle.gjdip.ip()
    elif choice == '6':
        print('[1] 普通字典')
        print('[2] 根据域名生成字典（针对web后台）')
        choice2 = input('spdtools > ')
        if choice2 == '1':
            bp2.bp2()
        if choice2 == '2':
            uu = input('请输入域名：')
            os.system('python bp.py '+uu)
    elif choice == '7':
        print('[1] MySQL爆破')
        print('[2] FTP爆破')
        cc = input('spdtools > ')
        if cc == '1':
            tar = input('请输入目标：')
            usr = input('请输入用户名字典文件：')
            psd = input('请输入密码字典文件：')
            pt = input('请输入端口：')
            os.system('python mysqlbp.py -H '+tar+' --u '+usr+' --p '+psd+' -P '+pt)
        if cc == '2':
            tar = input('请输入目标：')
            usr = input('请输入用户名字典文件：')
            psd = input('请输入密码字典文件：')
            os.system('python ftpbp.py -H '+tar+' -u '+usr+' -p '+psd)
    elif choice == '8':
        os.system('python bash64.py')
    elif choice == '9':
        modle.bash64mabiao.mabiao()
    elif choice == '10':
        modle.dlip.dlip()
    elif choice == 'spider':
        os.system("mode con cols=120 lines=40")
        time.sleep(1)
        modle.spd.spider()
    elif choice == 'exit':
        break