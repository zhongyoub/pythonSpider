'''
csdn登录：http://passport.csdn.net/account/login
输入用户名和密码后，会返回一个jessionid，并从http://passport.csdn.net/account/login;jsessionid="jsessionid"登录
模拟登录csdn，使用cookies,并从中获取jsessionid
'''

import urllib.request as request 
import urllib.parse as parse 
from bs4 import BeautifulSoup as bs 
import http.cookiejar as cookiejar
import re 

def login():
    username ="xxxx"
    password ="xxxxx"
    filename="config.ini"
    header={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        }
    data={
        "username":username,
        "password":password
        }
    loginUrl="https://passport.csdn.net/account/login"
    jsessionid=""
    #保存Cookie，提取jessionid 
    cookies = cookiejar.MozillaCookieJar(filename)
    cookieHandler = request.HTTPCookieProcessor(cookies)
    opener=request.build_opener(cookieHandler)
#    opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36")]
    response = opener.open(loginUrl)
    respondeData = response.read().decode("utf-8")
    '''
    jsessionid=re.findall('jsessionid=(.*)\"', respondeData, flags=0)[0]
    print(jsessionid)
    '''
    #保存cookie到文件
    cookies.save(ignore_discard=True, ignore_expires=True)
    
    soup=bs(respondeData,"lxml")
    for item in soup.form.find_all("input"):
        if item.get("name")=="lt":
            lt=item.get("value").strip()
    #        print(lt)
        if item.get("name")=="execution":
            execution=item.get("value").strip()
    '''
    "lt":lt,
    "execution":execution,
    "_eventId":"submit"
    '''
    data["lt"]=lt
    data["execution"]=execution
    data["_eventId"]="submit"
    print(data)
    cookies.load('config.ini', ignore_discard=True, ignore_expires=True)
    for item in cookies:
        if item.name == "JSESSIONID":
            jsessionid=item.value.strip()
#            print(jsessionid)

    loginUrl=loginUrl+';jsessionid='+jsessionid
    postData=parse.urlencode(data).encode(encoding='utf_8', errors='strict')
    opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36")]
    response = opener.open(loginUrl)
    response = opener.open(loginUrl,postData)
    cookies.save( ignore_discard=True, ignore_expires=True)
    mycsdn_url ="http://my.csdn.net/"
    mycsdn =opener.open(mycsdn_url)
    print(mycsdn.read().decode("utf-8"))

'''
必须包含头部，否则会报错
'''
def get(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
    headers = { 'User-Agent':user_agent}
    req=request.Request(url=url,headers=headers)
    response=request.urlopen(req)
#     获取包含参数的html
    data=response.read().decode(errors='ignore')
    return data

if __name__=='__main__':
    login()
            
