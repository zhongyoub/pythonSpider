'''
使用cookie登录,使用多线程的方式请求资源
'''

import urllib.request as request
import http.cookiejar as cookiejar
import urllib.parse as parse 
import threading


'''
filename="mesa.ini"
cookie=cookiejar.MozillaCookieJar(filename)  # 声明一个cookie对象保存Cookie，然后写入文件
opener= request.build_opener(request.HTTPCookieProcessor(cookie))
postdata={
    'username':"chengyixuan",
    'password':"chengyixuan"
    }
loginUrl = 'https://mesalab.cn/login'
# 模拟登录，并保存Cookie
data=parse.urlencode(postdata).encode(encoding='utf_8', errors='strict')
result = opener.open(loginUrl, data)
cookie.save( ignore_discard=True, ignore_expires=True)
# 利用cookie请求另一url
gradeurl='https://mesalab.cn/nis/index'
result=opener.open(gradeurl)
print(result.read().decode("utf-8"))
'''

class ThreadClass(threading.Thread):
    def __init__(self,threaname,opener,url):
        threading.Thread.__init__(self)
        self.threadname=threaname
        self.opener=opener
        self.url=url
    
    def run(self):
        try:
            opener.open(url)
            print(self.threadname," start")
        except request.HTTPError as e:
            print(e.code)
        except request.URLError as e:
            if hasattr(e, "reason"):
                print(e.reason)
                
# 从文件中读取cookie
thread_list=[]
cookie = cookiejar.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('mesa.ini', ignore_discard=True, ignore_expires=True)
url='https://mesalab.cn/nis/index'
#req = request.Request(url)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
while True:
    for i in range(100):
        thread=ThreadClass('thread{}'.format(i),opener,url)
        thread_list.append(thread)
        thread.start()
        



