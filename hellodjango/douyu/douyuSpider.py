'''
Created on 2019-06-07

@author: fish
'''
import urllib3
from bs4 import BeautifulSoup

url_directory = 'https://www.douyu.com/directory';
class DouyuSpider():
    def __init__(self):
        self.http = urllib3.PoolManager()
    
    def getClassifyInfo(self):
        r = self.http.request('GET', url_directory)
        plain_text = r.data.decode("utf-8")
        soup = BeautifulSoup(plain_text, "html5lib")
        classify_list=soup.findAll('li',{'class':'layout-Classify-item'})
        for classify in classify_list:
            link_info = classify.find('a')
            link = link_info.get('href')
            name_info = classify.find('strong')
            classify_name = name_info.text
            print(classify_name + ":" +link)
            
spider = DouyuSpider()
spider.getClassifyInfo();