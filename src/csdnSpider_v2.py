'''
模拟登录csdn网站，从Cookie中读取jessionid
'''
#!/usr/bin/env python 
#encoding:utf-8


import requests
import os
from bs4 import BeautifulSoup as bs
from http.cookiejar import LWPCookieJar


def toJson(str):
    '''
    提取lt流水号，将数据化为一个字典
    '''
    soup = bs(str,"lxml")
    tt = {}
    for inp in soup.form.find_all('input'):
        if inp.get('name') != None:
            tt[inp.get('name')] =inp.get('value')
    return tt

# cookie setting
s = requests.Session()
s.cookies = LWPCookieJar('cookiejar')
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
if not os.path.exists('cookiejar'):
    print("there is no cookie,setting")
    r = s.get("http://passport.csdn.net/account/login")
    s.cookies.save(ignore_discard=True)
    '''
    cookies=s.cookies 
    jsessionid = dict(cookies)["jsessionid"]
    '''
    soup = toJson(r.text)
    payload ={'username':'1143747780@qq.com','password':'youbingzhong','lt':soup["lt"],'execution':'e1s1','_eventId':'submit'}
    r = s.post("http://passport.csdn.net/account/login",data=payload,headers=header)
    s.cookies.save(ignore_discard=True)
    print(r.text)
else:
    print("cookie exists,restore")
    s.cookies.load(ignore_discard=True)
 #   cookies = dict(s.cookies)
 #   jessionid=cookies["jsessionid"]

r = s.get("http://write.blog.csdn.net/postlist",headers=header)
print(r.text)