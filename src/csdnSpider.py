'''
模拟登录csdn,需要考虑jessionId,从文件夹中读取jsessionid，可实现登录一次
'''
#!/usr/bin/python env 
#encoding=utf8

import lxml
from bs4 import BeautifulSoup
import configparser
import urllib.request as request
import urllib.parse as parse

def login():
    cf=configparser.ConfigParser()
    cf.read("config.ini")
    cookies=cf.items("cookies")
    cookies=dict(cookies)
    jessionid=cookies['jsessionid']
    from pprint import pprint
    pprint(cookies)
    username=cf.get('info', 'username')
    password=cf.get('info', 'password')
    
    header={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "Host":"passport.csdn.net",
        "Referer":"http://passport.csdn.net"
        }
    loginurl="http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
    response=request.urlopen(loginurl)
    soup=BeautifulSoup(response.read().decode('utf-8'),"lxml")
    for input in soup.form.find_all("input"):
        if input.get("name")=="lt":
            lt=input.get("value")
        if input.get("name")=="execution":
            execution=input.get("value")
    
    
    login_data={'username':username,
                'password':password,
                "lt":lt,
                "execution":execution,
                "_eventId":"submit"
                }
    loginurl = "http://passport.csdn.net/account/login;jsessionid="+jessionid
    postdata=parse.urlencode(login_data).encode(encoding='utf-8', errors='strict')
    req=request.Request(loginurl,data=postdata,headers=header)
    response=request.urlopen(req)
    print(response.read().decode("utf-8"))
    
    
if __name__=='__main__':
    login()
