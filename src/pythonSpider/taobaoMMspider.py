'''
抓取mm.taobao.com上面mm的姓名，年龄和居住地，以及mm的个人详情页面地址
'''
#!/usr/bin/env python 
#coding=utf-8

import urllib.request as request 
import re 
import os 

class MMtaobao:
    def __init__(self,url,pageIndex):
        self.url=url 
        self.pageIndex=pageIndex
        self.tool=Tool()
    
    def getPage(self,pageIndex):
        if pageIndex is None:
            pageIndex=self.pageIndex
        url=self.url+"?page="+str(pageIndex)
        print(url)
        req=request.Request(url)
        response=request.urlopen(req)
        return response.read().decode('gbk')
    
    def getContent(self,pageIndex):
        page=self.getPage(pageIndex)
        pattern=re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?'+
                           '<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
                           re.RegexFlag.S)
        items=re.findall(pattern,page)
        print("items:",items)
        contents=[]
        for item in items:
            # item[0]:个人详情  item[1]:图片Icon  item[2]:名字 item[3]：年龄，item[4]：城市
            contents.append([item[0],item[1],item[2],item[3],item[4]])  
        return contents  
    
    #获取个人详情
    def getDetailPage(self,infoUrl):
        response = request.urlopen(infoUrl)
        response=response.read().decode('gbk')
        return response
    
    #获取个人文字介绍
    def getBrief(self,page):
        pattern=re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.RegexFlag.S)
        result=re.search(pattern, page)
        return self.tool.replace(result.group(1))
    
    #获取页面中所有图片
    def getAllImg(self,page):
        pattern=re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.RegexFlag.S)
        #个人信息页面所有代码
        content=re.search(pattern,page)
        #从代码中提取图片
        patternImg= re.compile('<img.*?src="(.*?)"',re.RegexFlag.S)
        images=re.findall(patternImg,content.group(1))    #
        print('images:',images)
        return images             #返回的是图片对应的超链接
            
    #保存多张图片
    def saveImgs(self,images,name):
        count=1
        print(u'发现', count,u'共有',len(images),u'张照片')
        for imageUrl in images:
            splitpath=imageUrl.split('.')
            fTail=splitpath.pop()    #一处list列表中最后一个元素list[-1]
            if len(fTail)>3:
                fTail="jpg"
            fileName = name+"\\"+str(count)+"."+fTail
            imageUrl = "http:"+imageUrl
            try:
                self.saveImg(imageUrl,fileName)
            except request.HTTPError as e:
                print(e.reason)
                continue
            count+=1
    
    #保存头像
    def saveIcon(self,iconUrl, name):
        splitPath = iconUrl.split('.')
        fTail = splitPath.pop()
        fileName = name +"\\"+"icon." +fTail
        self.saveImg(iconUrl, fileName)
    
    #传入图片地址，文件名，保存单张图片
    def saveImg(self,imageUrl,fileName):
        response = request.urlopen(imageUrl)
        data=response.read()
        f=open(fileName,'wb')     # 此处应该使用 try --- except
        if f is not None:
            f.write(data)
        print(u'正在保存图片',fileName)
        f.close()
    
    #保存个人文本信息,注意乱码问题
    def saveBrief(self,content,name):
        fileName=name+'\\'+name+'.txt'
        f=open(fileName,"wb+")
        print(u"正在保存"+name+"的个人信息",fileName)
        f.write(content.encode('utf-8'))      
        
    #创建目录
    def mkdir(self,path):
        path=path.strip()
        #判断路径存在与否
        isExist = os.path.exists(path)
        if not isExist:
            print(u'可以新建文件夹',path)
            os.mkdir(path)
            return True
        else:
            print(u'已经存在文件夹',path)
            return False
    
    #将各种信息保存起来
    def savePageInfo(self,pageIndex):
        contents = self.getContent(pageIndex)
        for item in contents:
            print(u'名字:',item[2],",年龄:",item[3],",居住城市:",item[4])
            print(u'个人详情页:',item[0])
            detailUrl="http:"+item[0]
            #获取个人详情页信息
            detailPage =self.getDetailPage(detailUrl)
            brief = self.getBrief(detailPage)     
            
            images = self.getAllImg(detailPage)
            self.mkdir(item[2])   
            #保存个人简介
            self.saveBrief(brief, item[2])
            #保存Icon
            iconUrl="http:"+item[1]
            self.saveIcon(iconUrl, item[2])
            #保存图片
            self.saveImgs(images, item[2])
    
    #设置起始页和结束页
    def savePagesInfo(self,start,end):
        for i in range(start,end+1):
            self.savePageInfo(i)     

class Tool:
    #去除img标签,1-7位空格,&nbsp;
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    #将多行空行删除
    removeNoneLine = re.compile('\n+')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        x = re.sub(self.removeNoneLine,"\n",x)
        #strip()将前后多余内容删除
        return x.strip()

url='http://mm.taobao.com/json/request_top_list.htm'
mm =MMtaobao(url,1)
mm.savePagesInfo(mm.pageIndex, mm.pageIndex)
        
        