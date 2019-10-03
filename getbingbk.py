#coding:utf-8
"""
待更新：每周自动删除
       搜索功能
       用户系统结合raspberrpi
"""

import win32gui
import win32con
import requests
import time
import urllib3
import socket
import json
import os
import random
import threading

class bingbgdowner(object):
    def __init__(self,fileSaveLocation,fileName = time.asctime(time.localtime(time.time()))):
        """
        fileSaveLocation示例："C:\\dir\\"
        """
        self.fileSaveLocation = fileSaveLocation
        self.url = "https://cn.bing.com"
        self.fileName = fileName+'.jpg'
    def getbingbk(self):
        try:
            result = requests.get(self.url)
            resource = result.content.decode()
            #处理html代码并获取backgroundPic地址
            bgLink = resource.find("bgLink")
            resource = resource[bgLink:]
            href = resource.find('href="')
            resource = resource[href+6:]
            end = resource.find("&")
            resource = resource[:end]
            url = self.url + resource
            #下载图片
            pics = requests.get(url).content
            #print(str(time.time()))
            with open(self.fileSaveLocation+self.fileName,"wb+") as f:
                f.write(pics)
                f.close()
            print("succeed") 
        except Exception as e :
            print(e)

class thread_download(threading.Thread):
    def __init__(self,picUrl,fileSaveLocation,headers,name,count):
        threading.Thread.__init__(self)  
        self.picUrl = picUrl
        self.fileSaveLocation = fileSaveLocation
        self.headers = headers
        self.count = count
        self.name = name
    def run(self):
        try:
            print("下载第{}张图片...\n".format(self.count))
            response = requests.get(self.picUrl,headers = self.headers).json()
            downUrl = response['url']
            response = requests.get(downUrl,headers = self.headers).content
            self.saveToFile(response,name = self.name)
            print("第{}张图片 ✔ :)".format(self.count))
        except Exception as e:
            print("下载第{}张图片 ✖ :(，错误信息如下：".format(self.count))
            print(e)



    def saveToFile(self,content,name = None):
        if name != None:
            pass
        else:
            name = str(time.time())
        with open(self.fileSaveLocation+name+'.jpg','ab+') as f:
            f.write(content)


class getUnsplashPics(object):
    def __init__(self):
        self.basicUrl = "https://api.unsplash.com/"
        self.fileSaveLocation = 'C:\\Users\\Fseven\\Pictures\\bing\\'
        self.pubKey = 'fa60305aa82e74134cabc7093ef54c8e2c370c47e73152f72371c828daedfcd7'
        self.myKey="2c5ca66c14d8b971510a5693112e276630aac16aeaab0ff9600e446c46104732"
        self.headers = {
                "Accept-Version": "v1",
                "Authorization" :'Client-ID '+self.pubKey
            }
    def setWallPaper(self,paperName,ramdon = False):
        if ramdon:
            fileNames = os.listdir(self.fileSaveLocation)
            paperName = random.choice(fileNames)
            print(paperName)
            
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,self.fileSaveLocation+paperName,1+2)
        print("set succeed")

    def getRandomPics(self,picCount = 30):
        response = None
        params = {
            'orientation':'landscape',
            'count':picCount
        }
        linkarr = []
        try:

            specialUrl = "photos/random"
            response = requests.get(self.basicUrl+specialUrl,headers = self.headers,params= params)
            
            response = response.json()
            print("获取图片信息 ✔ :)，共得到了{}条信息！".format(picCount))
            #print(response)
            for re in response:
                linkarr.append({'url':re['links']['download_location'],'name':re['id']})
        except requests.exceptions.ConnectionError as e:
            print("获取图片信息 ✖ :(，错误信息如下：")
            print(type(e))
            print(e)
        count = 1
        for downUrl in linkarr:

            downer = thread_download(downUrl['url'],self.fileSaveLocation,self.headers,downUrl['name'],count)
            downer.start()
            count += 1

    def search(self,query,page = 1,perPage = 10,collection = None,orientation = 'landscape'):
        """
        param Description
        query
            Search terms.
        page
            Page number to retrieve. (Optional; default: 1)
        per_page
            Number of items per page. (Optional; default: 10)
        collections
            Collection ID(‘s) to narrow search. If multiple, comma-separated.
        orientation
            Filter search results by photo orientation. Valid values are landscape, portrait, and squarish.
        """
        specialUrl = 'search/photos'
        response = requests.get(self.basicUrl+specialUrl,headers = self.headers,params = {
            'query':query,
            'page':page,
            'per_page':perPage,
            'collection':collection,
            'orientation':orientation
        }).json()
        count =1
        for re in response['results']:
            downLoader = thread_download(re['links']['download_location'],self.fileSaveLocation,self.headers,name = query+' '+re['id'],count = count)
            count += 1
            downLoader.start()
        

"""             except Exception as e :
                print(type(e))
                print(e)
            
 """

#getbingbk()
if (__name__ == '__main__'):
    pass
