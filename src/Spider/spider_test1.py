#!/usr/bin/env python 
#encoding=UTF8
'''
爬虫测试一，urllib,urllib2
python3中urllib,urllib2合并为urllib
urlopen(url,data,timeout)
'''
import urllib.request as request


resonse=request.urlopen("http://mesalab.cn/", "<script>eval('nc -p')</script>".encode(encoding='utf_8', errors='strict'))
from pprint import pprint
pprint(resonse.read().decode("utf-8"))
