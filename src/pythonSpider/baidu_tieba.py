'''
爬取百度贴吧
'''
#!/usr/bin/env python 
#coding=utf-8

import urllib.request as request
import re 

class BDTB(object):
    
    def __init__(self,baseUrl,param,indexPage,floorTag):
        #基础URL
        self.baseUrl=baseUrl
        #是否只看楼主
        self.param='?see_lz='+str(param)
        #页码
        self.indexPage=indexPage
        #将HTML标签剔除工具类对象
        self.tool=Tool()
        #file,文件写入对象
        self.file=None
        self.floor=1
        #默认标题，如果没有获取标题，则使用默认标题
        self.defaultTitle=u'百度贴吧'
        #是否写入楼分隔符标记
        self.floorTag=floorTag  
         
    # 获取页面
    def getPage(self,pageIndex=None):
        try:   
            if pageIndex is None:
                pageIndex=self.indexPage
            url=self.baseUrl+self.param+'&pn='+str(pageIndex)
            req=request.Request(url)
            response=request.urlopen(req)
            print(response.geturl())
            print(response.getcode())
            response=response.read().decode('utf-8')     #此处有编码问题
            return response
    #        return response.read().decode('utf-8')
    #        print(response.read().decode('utf-8'))
        except request.URLError as e:
            if hasattr(e, 'reason'):
                print(u'连接百度贴吧失败，',e.reson)
                return None
            
    # 获取帖子标题
    def getTitle(self,pageIndex):
        page=self.getPage(pageIndex)
        pattern=re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.RegexFlag.S)
        result=re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None
            
    #提取帖子总页数
    def getPageCount(self,pageIndex):
        page=self.getPage(pageIndex)
        pattern=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.RegexFlag.S)
        result=re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None 
    #获取帖子正文内容,每一页有很多层楼
    def getContent(self,page):
        pattern=re.compile('<div id="post_content_.*?>(.*?)</div>',re.RegexFlag.S)
        items=re.findall(pattern, page)
        contents=[]
        for item in items:
         #   print(floors,u'楼----')
         #   print(self.tool.replace(item))
            content='\n'+self.tool.replace(item)+'\n'
            contents.append(content.encode('utf-8'))
        return contents
    
    def setFileName(self,title):
        if title is not None:
            self.file=open(title+'.txt','w+')
        else:
            self.file=open(self.defaultTitle+'.txt','w+')
    
    def writeData(self,contents):
        for item in contents:
            if self.floorTag==1:
                floorline="\n"+str(self.floor)+u"---------\n"
                self.file.write(floorline)
            self.file.write(item)
            self.floor+=1    
            
    def start(self):
        page=self.getPage()
        pageCount=self.getContent(page)
        title=self.getTitle(page)
        self.setFileName(title)
        if pageCount == None:
            print(u'URL无效，try again')
            return 
        try:
            print(u'该帖子共有'+str(pageCount)+'页')
            for i in range(1,range(pageCount)+1):
                print('正写入第'+str(i)+'页数据')
                page=self.getPage(i)
                contents=self.getContent(page)
                self.writeData(contents)
        except IOError as e:
            print(u'写入失败:'+e.message)
        finally:
            print(u'写入完成')  
            
'''
Tool类，替换各种标签
'''          
class Tool(object):
    #去除img标签
    removeImg=re.compile('<img.*?>| {7}|')
    #去除超链接
    removeAddr=re.compile('<a.*?></a>')
    #将换行符标签换为<\n>
    replaceLine=re.compile('<tr>|<div>|</div></p>')
    #将制表符换成\t
    replaceTd=re.compile('<td>')
    #将段落开头换成\n加空格
    replacePara=re.compile('<p.*?>')
    #将换行符或双换行符换为\n
    replaceBR=re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag=re.compile('<.*?>')
    
    def replace(self,x):
        x=re.sub(self.removeImg, "",x)
        x=re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTd,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()
             
baseUrl='https://tieba.baidu.com/p/3138733512'
see_lz=input(u'是否只看楼主,是输入1，否输入0:')
pageIndex=input(u'请输入页码:')
floorTag=input(u'是否写入楼层信息，是输入1，否输入0:')
bdtb=BDTB(baseUrl,see_lz,int(pageIndex),floorTag)
bdtb.start()