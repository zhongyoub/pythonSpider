'''
将爬取的内容以一定的格式保存到数据库中
'''

#!/usr/bin/env python 
#coding:utf-8

import time 
import xlutils
import twisted

print(twisted.__version__)

# 获取当前时间
def getCurrentTime():
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))