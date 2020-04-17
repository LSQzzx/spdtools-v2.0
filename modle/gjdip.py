def ip():
    import requests
    import re
    from requests.adapters import HTTPAdapter
    
    host = 'https://ips.market.alicloudapi.com'
        #host2 = 'https://market.console.aliyun.com/?#/orders?_k=mncont'
    path = '/iplocaltion'
    method = 'GET'
    appcode = '6c5b80a59e0243bd8556b3b9a4c1bf33'
    headers = {'Authorization': 'APPCODE ' + appcode}
    ip = input("请输入ip:")
    url = host + path + '?ip=' + ip
    
    result = None
    try:
        result = requests.get(url, headers=headers, timeout=30, verify=False)
        result = result.json()
    except Exception as e:
        print('%s throw exception: %s'%(ip, str(e)))
    title = str(result)
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    result2 = pattern.findall(title)
    print('地址:',result2)
    print('经纬度：',result['result']['lng'],',',result['result']['lat'])