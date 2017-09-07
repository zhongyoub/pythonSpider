
import http.cookiejar
import urllib.request
import re 

cj = http.cookiejar.LWPCookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support , urllib.request.HTTPHandler)
urllib.request.install_opener(opener)

def crawl_CSDN(user_name,password):
    para_url="https://passport.csdn.net/account/login"
    post_url="https://passport.csdn.net/account/login"
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
    headers = { 'User-Agent' : user_agent ,'Host': 'passport.csdn.net'}
    request=urllib.request.Request(url=para_url,headers=headers)
    response=urllib.request.urlopen(request)
#     获取包含参数的html
    data=response.read().decode("utf-8")
#     获取参数
    jsessionid=re.findall('jsessionid=(.*)\"', data, flags=0)[0]
#    print(jsessionid)
    lt=re.findall('name="lt" value=\"(.*)\"', data, flags=0)[0]
    execution=re.findall('name="execution" value=\"(.*)\"', data, flags=0)[0]
#     需要提交的参数
    parameters={'username':user_name,'password':password,'lt':lt,'execution':execution,'_eventId':'submit'}
#     把参数变为指定格式
    post_data=urllib.parse.urlencode(parameters).encode(encoding='utf_8', errors='strict')
    post_url=post_url+';jsessionid='+jsessionid
    post_request=urllib.request.Request(post_url,post_data,headers)
    post_response=urllib.request.urlopen(post_request)
#    print(post_response.read().decode("utf-8"))
    #===========================================================================
#    print(execution)
#    print(lt)
#    print(jsessionid)
#    print(data)
    #===========================================================================
    print(get('http://my.csdn.net/'))
 #   print(get('http://www.csdn.net'))

def get(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
    headers = { 'User-Agent':user_agent}
    request=urllib.request.Request(url=url,headers=headers)
    response=urllib.request.urlopen(request)
#     获取包含参数的html
    data=response.read().decode(errors='ignore')
    return data
crawl_CSDN("1143747780@qq.com","youbingzhong")