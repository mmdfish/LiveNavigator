'''
Created on 2019-06-10

@author: fish
'''

import urllib3
import json
from hellodjango.models import LiveRoom

import os
import django
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")#website可以更改为自己的项目名称
django.setup()

typeNum = 1000
http = urllib3.PoolManager()
url = 'https://www.douyu.com/gapi/rkc/directory/2_'
roomUrl = 'https://www.douyu.com'
def analysisJSON():
    print("json")
    
def getJSON(typeIndex):
    for typeIndex in range(1, typeNum):
        firstPageUrl = url + typeIndex + '/1'
        http.request('GET', firstPageUrl)
        
def getAllPagesJSON(typeIndex):
    pageNum = getFirstPageJSON(typeIndex)
#     for pageIndex in range(2, pageNum):
#         pageUrl = url + str(typeIndex) + '/' + str(pageIndex)
#         jsonContent = getJSONFromUrl(pageUrl)
#         analysisPageJSON(jsonContent)

def getJSONFromUrl(pageUrl):
    request = http.request('GET', pageUrl)
    content = request.data.decode("utf-8")
    jsonContent = json.loads(content)
    return jsonContent      

def getFirstPageJSON(typeIndex):
    firstPageUrl = url + str(typeIndex) + '/1'
    jsonContent = getJSONFromUrl(firstPageUrl)
    analysisPageJSON(jsonContent)
    return jsonContent['data']['pgcnt']

def analysisPageJSON(jsonContent):
    a=LiveRoom.objects
    for room in jsonContent['data']['rl']:
        roomid = room['rid']
        roomname = room['rn']
        userid = room['uid']
        username = room['nn']
        url = room['url']
        kind = room['c2name']
        onlineNumber = room['ol']
        userTag = room['od']
        
        a.create(room_home = 'douyu',
                 room_id = roomid,
                 room_name = roomname,
                 user_id = userid,
                 user_name = username,
                 room_kind = kind,
                 room_url = roomUrl + url,
                 room_olnum = onlineNumber,
                 room_usertag = userTag)
                 
                 
getFirstPageJSON(1)
    