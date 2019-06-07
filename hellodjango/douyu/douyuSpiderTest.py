'''
Created on 2019-06-07

@author: fish
'''

import urllib3

http = urllib3.PoolManager()
r = http.request('GET', "https://www.douyu.com/directory")
plain_text = r.data.decode("utf-8")
file = open("content.html", "w", encoding='utf-8')
file.write(plain_text);