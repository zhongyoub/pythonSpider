'''
cookie的使用
CookieJar —-派生—->FileCookieJar  —-派生—–>MozillaCookieJar和LWPCookieJar
'''

#!/usr/bin/env python 
#coding:utf-8

import http.cookiejar as cookiejar
import urllib.request as request 

# 获取Cookie
# 声明一个cookiejar实例来保存Cookie
cookie = cookiejar.CookieJar()
# 利用urllib.request的HTTPCookieProcessor()对象来创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
# 此处的opener()方法也可以传入request
response=opener.open("http://www.baidu.com")
for item in cookie:
    print('Name='+item.name)
    print('Value='+item.value)
 
    
# 将cookies写入文件
filename="cookie.ini"
cookie = cookiejar.MozillaCookieJar(filename)
handler=request.HTTPCookieProcessor(cookie)
opener=request.build_opener(handler)
response = opener.open("http://www.baidu.com")
# 保存Cookie文件
cookie.save( ignore_discard=True, ignore_expires=True)



# 从文件中读取cookie
cookie = cookiejar.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.ini', ignore_discard=True, ignore_expires=True)
req = request.Request("http://www.baidu.com")
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
response= opener.open(req)
print(response.read())




    