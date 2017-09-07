'''
Proxy的使用
timeout设置

'''

import urllib.request as request
import urllib.parse as parse 

enable_proxy=True
proxy_handler=request.ProxyHandler({"http":"http://some-proxy.com:8080"})
null_proxy_handler=request.ProxyHandler({})
if enable_proxy:
    opener=request.build_opener(proxy_handler)
else:
    opener=request.build_opener(proxy_handler)


values={
    'usernmae':"1143747780@qq.com",
    'password':"xxxxx"
    }
url="http://www.baidu.com"
data=parse.urlencode(values).encode(encoding='utf-8', errors='strict')
response=request.urlopen(url, data, 1000)
req=request.Request(url,data=data)
req.get_method=lambda:"PUT"
httphandler = request.HTTPHandler(debuglevel=1)
httpshandler = request.HTTPSHandler(debuglevel=1)
opener = request.build_opener(httphandler,httpshandler)    #挂载opener
request.install_opener(opener)      #安装opener
response=request.urlopen(req)
