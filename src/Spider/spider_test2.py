'''
登录测试
'''
#!/usr/bin/env python 
#encoding=UTF8

import urllib.request as request
import urllib.parse as parse

values={"username":"1143747780@qq.com","password":"youbingzhong"}
data=parse.urlencode(values).encode(encoding='utf-8', errors='strict')
url="http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    'Referer':"http://www.zhihu.com/articles"
    }

'''
Get method :
url=url+"?"+data
req=request.Request(url)
'''
req=request.Request(url,data,headers)
response=request.urlopen(req)
print(response.read().decode("utf-8"))

