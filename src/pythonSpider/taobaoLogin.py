'''
模拟登录淘宝
首先需要了解淘宝的登录流程，有待有时间弄明白登录过程
'''
#!/usr/bin/env python 
#coding:utf-8


import urllib.request as request 
import urllib.parse as parse 
import http.cookiejar as cookiejar
import os 
import re 
import webbrowser
from src.Spider.cookie_v2 import cookie

class Taobao:
    def __init__(self):
        #login url 
        self.loginUrl="https://login.taobao.com/member/login.jhtml"
        #使用代理，防止被封
        self.proxyUrl = "http://120.193.146.97:843"
        self.loginHeader={
            "origin":"https://login.taobao.com",
            "referer":"https://login.taobao.com/member/login.jhtml",
            "upgrade-insecure-requests":1,
            "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
            }
        #username 
        self.username="zhongyoub"
        
        #密码，淘宝对用户的密码进行了加密，256位
        self.password2="426cb0a063f0016c922e70f6f2d4958f221b9468e4d731f9cc406633cf429b9a826bc1757cd3189f014b7dea8616cb80c3bc4aee5f8cbb71dfffc8f2985fcb3b0e587048fe566e8c612748ed1298c94a366e1a1847e09ec8fa97949e430e507f810a467ca4f65d70deb2cacf425d9b1edb8064e1ca15c3dca357ec650580514b"
        
        # ua字符串，经过taobao的ua算法计算得出，包含了时间戳，浏览器，屏幕分辨率，随机数，鼠标信息，键盘信息等
        self.ua="098#E1hvGQvivTUvn9CkvvvvvjiPP2FO0ji2PL5Z0jD24sun1j+afs/x3clhPVKxtjUL4sTHgjYb42ox1jD8fs7Hyot8nLcp3pwCvCeazHi4zTy9XKXDKwdkw6d8Aou/K7Hfmhi8CQhvVXzw7DdNI41ete7tAKEso+dE8dTtOx+UoyIjvpvX5a147r/CU0feXf58g5n8A+yuSdD37Q38o9wCvCeazHi4zzyiXKXDKwdkw6d8Aou/K7Hfmhi8CQhvVXzw7DdN4Liete7tAKEso+dE8dTtOx+UoyIjvpvX5a147rYXa0feXf58g5n8A+yuSdD37Q38oFyCvvpvvvvvCQhvVXzw7Dd"+"NoZHete7tAKEso+dE8dTtOx+UoyItvpvhvvvvvUhCvCuaP2Ef8YMwznsvUl"+"iT7ecjT9FnsXnL8eFjvdwCvCoj3iu4dQPaFw742Qzr5/JVtUjtAqwCvCoj3iu45AcaFw742Qzr5/JVtUjtAsyCvvpvvvvvdphvmpvpOv2V19vG4u6CvvyvhHZv1GwvPHArvpvEvC2BvnPLv29Fdphvmpvp1p2+qvvgEIwCvvpvCvvvRph"+"vCvvvvvvPvpvh6GH03OyCvvOUvvVvay4ivpvUvvmvb1LmUYRtvpvIvvvvCZCvHUUvvUEjphvvTQvv99CvpvAvvvmmvhCv2UvvvUUvphvW9mhCvm/EIiu4g"+"ELYFNdvAw5yk/TjtGyR//JHTUJ51vyjiGd+9JKR2W5yk/TjtGyhvSABtpyCvhQWpjhvCz7x6acEn1vDN+Lva4AxHkpXznshQCOqb64B9W2++fvsxI2hzR9"+"t+FBCAfevD464jomxfaClDBh67GeU+EVJV5EH6b2XSfpAvphvC9v9vvCvp8wCvvpvvUmmdphvmpvp792h1vvGXOhCvCuacmH4fYMwznA/NlIu6948mZFHFjEqmVIEobwCvCoj3tu4u/FaFw742Qzr5/JVtUjtAqwCvCoj3tu4d6qaFw742Qzr5/JVtUjtAqwCvCoj3iu4d6daFw74mSSqkPTB/tMtAsyCvvpvvvvvCQhvVXzw7DdNZOEete7tAKEso+dE8dTtOx+UoyItvpvhvvvvvvwCvCeazHi4zl"+"hqXKXDKwdkw6d8Aou/K7Hfmhi8CQhvVXzw7DdNONrete7tAKEso+dE8dTtOx+UoyIjvpvX5a147rY1f0feXf58g5n8A+yuSdD37Q38o9wCvCeazHi4zgeh"+"XKXDKwdkw6d8Aou/K7Hfmhi8CQhvVXzw7DdNyL1ete7tAKEso+dE8dTtOx+UoyIjvpvX5a147r/BL7feXf58g5n8A+yuSdD37Q38o9=="
        
        self.post={
            "TPL_username":self.username,
            "TPL_password":"",
            "ncoSig":"",
            "ncoSessionid":"",
            "ncoToken":"b6c10ff3ea690be99ab2a844a8e123f9aded994a",
            "slideCodeShow":"false",
            "useMobile":"false",
            "lang":"zh_CN",
            "loginsite":"0",
            "newlogin":"0",
            "TPL_redirect_url":"",
            "from":"tb",
            "fc":"default",
            "style":"default",
            "css_style":"",
            "keyLogin":"false",
            "qrLogin":"true",
            "newMini":"false",
            "newMini2":"false",
            "tid":"",
            "loginType":"3",
            "minititle":"",
            "minipara":"",
            "pstrong":"",
            "sign":"",
            "need_sign":"",
            "isIgnore":"",
            "full_redirect":"",
            "sub_jump":"",
            "popid":"",
            "callback":"",
            "guf":"",
            "not_duplite_str":"",
            "need_user_id":"",
            "poy":"",
            "gvfdcname":"10",
            "gvfdcre":"",
            "from_encoding":"",
            "sub":"",
            "TPL_password_2":self.password2,
            "loginASR":"1",
            "loginASRSuc":"1",
            "allp":"",
            "oslanguage":"zh-CN",
            "sr":"1280*800",
            "osVer":"windows|6.1",
            "naviVer":"chrome|60.03112113",
            "osACN":"Mozilla",
            "osAV":"5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "osPF":"Win32",
            "miserHardInfo":"",
            "appkey":"",
            "nickLoginLink":"",
            "mobileLoginLink":"https://login.taobao.com/member/login.jhtml?useMobile=true",
            "showAssistantLink":"",
            "um_token":"HV01PAAZ0b8709e9ca2b94a659af519c00ec3b84",
            "ua":self.ua
            }
        
        self.poatData=parse.urlencode(self.post)
        #设置代理
        self.proxy = request.ProxyHandler({'http':self.proxyUrl})
        #设置cookie
        self.cookie = cookiejar.LWPCookieJar()
        #设置cookie处理器
        self.cookieHandler = request.HTTPCookieProcessor(self.cookie)
        #设置opener
        self.opener = request.build_opener(self.cookieHandler,self.proxy, request.HTTPHandler)
        
    #是否需要输入验证码，依据请求的情况，不需要的话直接获取J_HToken
    def neeIdenCode(self):
        #首次登陆，验证是否需要验证码
        req = request.Request(self.loginUrl,self.poatData,self.loginHeader)
        response = self.opener.open(req)
        #获取响应内容
        content = response.read().decode('gbk')
        status = response.getcode()
        if status == 200:
            print(u'请求成功')
            pattern = re.compile(u"\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801",re.RegexFlag.S)
            result = re.search(pattern ,content)
            if result :
                print(u'需要输入验证码')
                return content 
            #不需要验证码
            else:
                print(u"安全验证通过，不需要输入验证码")
                #获取J_HToken
                tokenPattern = re.compile('id="J_HToken"')
                tokenMatch = re.search(tokenPattern,content)
                if tokenMatch:
                    return False
        else:
            print(u"请求失败")
            return None 
        
    #得到验证码图片
    def getCheckCodeImg(self,page):
        pattern = re.compile('<img id="J_StandardCode_m.*?data-src="(.*?)"',re.RegexFlag.S)
        matchResult = re.search(pattern,page)
        if matchResult and matchResult.group(1):
            print(matchResult.group(1))
            return matchResult.group(1)
        else:
            print(u'没有找到验证码')
            return False
        
    #输入验证码，重新请求，验证成功，返回J_HToken
    def loginWithCheckCode(self):
        checkCode = input(u'亲输入验证码:')
        self.post['TPL_checkcode'] = checkCode
        self.postData=parse.urlencode(self.post)
        try:
            #再次构建请求，加入验证码后第二次登录尝试
            req = request.Request(self.loginUrl,self.poatData,self.loginHeader)
            response = self.opener.open(req)
            content = response.read().decode('gbk')
            #检测验证码错误  验证码错误：\u9a8c\u8bc1\u7801\u9519\u8bef
            patter = re.compile(u'\u9a8c\u8bc1\u7801\u9519\u8bef', re.RegexFlag.S)
            result = re.search(pattern ,content)
            #如果找到
            if result :
                print(u'验证码错误')
                return False
            else:
                # 验证正确，
                
    
    