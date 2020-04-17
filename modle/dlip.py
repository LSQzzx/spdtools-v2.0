#coding:utf-8
import requests
from lxml import etree
from urllib import request

def dlip():
    _headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'www.xicidaili.com',
        'If-None-Match':'W/"b077743016dc54409ebe6b86ba7a869b"',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
    }
    _cookies = None


    def getHtml(page):
        url = "https://www.xicidaili.com/nn/"+str(page)
        result = requests.get(url,headers=_headers).text
        html = etree.HTML(result)
        return html

    file = open('ip.txt', 'w', encoding='utf-8')
    for j in range(1,10):
        print("正在爬取第"+str(j)+"页IP")
        try:
            for html in getHtml(j):
                ips = html.xpath('(//tr[@class="odd"]|//tr[@class=""])/td[2]/text()')
                duans = html.xpath('(//tr[@class="odd"]|//tr[@class=""])/td[3]/text()')
                gaodi = html.xpath('(//tr[@class="odd"]|//tr[@class=""])/td[5]/text()')
                types = html.xpath('(//tr[@class="odd"]|//tr[@class=""])/td[6]/text()')
                for i in range(0,len(ips)):
                        file.write(types[i])
                        file.write(' , ')
                        file.write(duans[i])
                        file.write(' , ')
                        file.write(gaodi[i])
                        file.write(' , ')
                        file.write(ips[i])
                        file.write('\n')
                        print(types[i],duans[i],gaodi[i],ips[i])

        except:
            pass

    file.close()
    print('保存于ip.txt')

