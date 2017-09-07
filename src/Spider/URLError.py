'''
URLError异常
'''

#！/usr/bin/env python 
#coding:utf-8


import urllib.request as request
import urllib.parse as parse 

req=request.Request("http://blog.csdn.net/acq")
try:
    response=request.urlopen(req)
    print(response.read().decode("utf-8"))
except request.HTTPError as e:
    print(e.code)
except request.URLError as e:
    if hasattr(e, "reason"):
        print(e.reason)
else:
    print("ok")