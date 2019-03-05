#coding=gbk
import os
import requests
from bs4 import BeautifulSoup#python支持html解析器

def get_picture():
    link_list=[]#存储每页头像地址
    for i in range(1,2):
        if i==1:
            tp='https://www.woyaogexing.com/touxiang/index.html'
        else:
            tp='https://www.woyaogexing.com/touxiang/index_'+str(i)+'.html'
        r=requests.get(tp)
        soup=BeautifulSoup(r.text,'lxml')
        linklist=soup.find_all('a',class_='img')
        for n in linklist:
            link_list.append('https://www.woyaogexing.com'+n.get('href'))
            print('正在接收地址'+n.get('href'))
        url_list=[]#存储每张头像地址
        for i in link_list:
            r=requests.get(i)
            soup=BeautifulSoup(r.text,'lxml')
            urllist=soup.find_all('li',class_='tx-img')
            for url in urllist:
                newurl=url.a.get('href')
                newurl='https:'+newurl
                url_list.append(newurl)
        path=mkdir()#获取当前存储路径并创建文件夹
        for i,v in enumerate(url_list):#emumerate()函数用于遍历数据对象组合为一个索引序列，同时列出数据和下标，一般用于for循环语句
            image=requests.get(v)
            with open(path+ str(i+1)+'.jpg','wb') as file:
                file.write(image.content)
            print(i+1)

def mkdir():
    curpath=os.getcwd()#获取当前目录
    path=curpath+'\爬取图片\\'
    folder=os.path.exists(path)
    if not folder:
        os.mkdirs(path)
        print("--- new folder ...---")
        print("--- OK ---")
    else:
        print("--- There is this folder! ---")
    return path

if __name__=='__main__':
    get_picture()
