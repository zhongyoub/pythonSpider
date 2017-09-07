'''
抓取嗅事百科的内容
'''
#!/usr/bin/env python 

import urllib.request as request
import re


'''
page =1 
url="http://www.qiushibaike.com/hot/page/"+str(page)
header={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        }
try:
    req=request.Request(url,headers=header)
    response=request.urlopen(req)
    content=response.read().decode('utf-8')
    pattern=re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</',
                         re.RegexFlag.S)
    items=re.findall(pattern,content)
    for item in items:
        haveImg=re.search('img',item[2])
        if not haveImg:
            print(item[0],item[1],item[2])
except request.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)
'''
        
'''
通过字符串匹配找出嗅事百科中段子的发布人，发布日期，内容已经点赞数
'''
class QSBK:
    def __init__(self,url):
        self.pageIndex=1
        self.user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
        self.headers={
            'User-Agent':self.user_agent
            }
        self.stories=[]   # 存放段子
        self.url=url
        self.enable=False
    def getPage(self,pageIndex):
        try:
            url=self.url         #此处需要使用正则表达式判断最后是否有个 /   
            if url.endswith(r'/'):
                url+=str(pageIndex)
            else:
                url=url+r'/'+str(pageIndex)
            
            req=request.Request(url,headers=self.headers)
            response=request.urlopen(req)
            pageCode=response.read().decode('utf-8')
            return pageCode
        except request.URLError as e:
            if hasattr(e, 'reason'):
                print(e.reason)
                return None
    
    def getPageItems(self,pageIndex):
        pageCode=self.getPage(pageIndex)
        if not pageCode:
            print("can not get page")
            return None
        pattern=re.compile('<div.*?author clearfix">.*?<a.*?<h2.*?>(.*?)</h2>.*?<div.*?content">.*?<span.*?>(.*?)</span>(.*?)'
            '<div class="stats.*?class="number">(.*?)</i>',re.RegexFlag.S)
        items=re.findall(pattern,pageCode)
        pageStories=[]
        for item in items:
            haveImg=re.search('img',item[1])
            if  not haveImg:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR,"\n",item[1])
                #item[0]是一个段子的发布者，item[1]是内容，item[2]是发布时间,item[4]是点赞数
                pageStories.append([item[0].strip(),text.strip(),item[2].strip(),item[3].strip()])
        return pageStories
    
    # 加载并提取页面的内容，加入到列表中
    def loadPage(self):
        if self.enable==True:
            if len(self.stories) < 2:
                #获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                #将该页的段子存放到全局list中
                if pageStories:
                    self.stories.append(pageStories)
                    #获取完之后页码索引加一，表示下次读取下一页
                    self.pageIndex += 1
    #调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self,pageStories,page):
        for story in pageStories:
            inputs=input("please Enter 'Enter' to continue or q to quit")
            self.loadPage()
            if inputs=='q':
                self.enable=False
                return 
            print(u"第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s" %(page,story[0],story[2],story[3],story[1]))
    #开始方法
    def start(self):
        print(u"正在读取糗事百科,按回车查看新段子，q退出")
        #使变量为True，程序可以正常运行
        self.enable = True
        #先加载一页内容
        self.loadPage()
        #局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                #从全局list中获取一页的段子
                pageStories = self.stories[0]
                #当前读到的页数加一
                nowPage += 1
                #将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                #输出该页的段子
                self.getOneStory(pageStories,nowPage)
 
 
spider = QSBK("http://www.qiushibaike.com/hot/page/")
spider.start()