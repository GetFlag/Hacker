#coding=gbk
import os
import requests
from bs4 import BeautifulSoup#python֧��html������

def get_picture():
    link_list=[]#�洢ÿҳͷ���ַ
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
            print('���ڽ��յ�ַ'+n.get('href'))
        url_list=[]#�洢ÿ��ͷ���ַ
        for i in link_list:
            r=requests.get(i)
            soup=BeautifulSoup(r.text,'lxml')
            urllist=soup.find_all('li',class_='tx-img')
            for url in urllist:
                newurl=url.a.get('href')
                newurl='https:'+newurl
                url_list.append(newurl)
        path=mkdir()#��ȡ��ǰ�洢·���������ļ���
        for i,v in enumerate(url_list):#emumerate()�������ڱ������ݶ������Ϊһ���������У�ͬʱ�г����ݺ��±꣬һ������forѭ�����
            image=requests.get(v)
            with open(path+ str(i+1)+'.jpg','wb') as file:
                file.write(image.content)
            print(i+1)

def mkdir():
    curpath=os.getcwd()#��ȡ��ǰĿ¼
    path=curpath+'\��ȡͼƬ\\'
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
