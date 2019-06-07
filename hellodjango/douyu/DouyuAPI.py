'''
Created on 2019-06-07

@author: fish
'''

import requests
import time
import hashlib   

aid = 'mmdfish'
key = 'O3jIfLmxPElqq0RHMchBkT4B'
tokenUrl = 'http://openapi.douyu.com/api/thirdPart/token'
class DouyuAPI():
    def __init__(self, aid, key):
        self.aid = aid;
        self.key = key;
    
    def getToken(self):
        timeStamp = str(int(time.time()))
        authSrc = '/api/thirdPart/token?aid='+ aid + '&time=' + timeStamp + 'key'
        print(timeStamp)
        m2 = hashlib.md5()   
        m2.update(authSrc.encode('utf-8'))   
        auth = m2.hexdigest()
        print(auth)
        url = tokenUrl + '?aid='+ aid + '&time=' + timeStamp + '&auth='+auth
        print(url)
        header_dict = {"Content-Type": "application/json"}
        resp = requests.get(url, headers=header_dict)
        print(resp.json())
douyu = DouyuAPI(aid, key)
douyu.getToken()

#curl -X GET "http://openapi.douyu.com/api/thirdPart/token?aid=mmdfish&time=1559840571&auth=76f9b587ea37b593b3855c7fbeff459f" -H "content-type: application/json"