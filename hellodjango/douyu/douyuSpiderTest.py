'''
Created on 2019-06-07

@author: fish
'''

import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

def getClassify():
    r = http.request('GET', "https://www.douyu.com/directory")
    plain_text = r.data.decode("utf-8")
    file = open("content.html", "w", encoding='utf-8')
    file.write(plain_text);
    soup = BeautifulSoup(plain_text, "html5lib")
    classify_list = soup.findAll(attrs={'class':'layout-Classify-item'})
    for classify in classify_list:
        link_info = classify.find('a')
        link = link_info.get('href')
        name_info = classify.find('strong')
        classify_name = name_info.text
        print(classify_name + ":" + link)

def getLOL():
    r = http.request('GET', "https://www.douyu.com/g_LOL")
    plain_text = r.data.decode("utf-8")
    file = open("content_lol.html", "w", encoding='utf-8')
    file.write(plain_text);
    soup = BeautifulSoup(plain_text, "html5lib")
    classify_list = soup.findAll('li', {'class':'layout-Cover-item'})
    for classify in classify_list:
        link_info = classify.find('a')
        link = link_info.get('href')
        name_info = classify.find(attrs={'class':'DyListCover-user'})
        user_name = name_info.text
        print(user_name + ":" + link)

getLOL()