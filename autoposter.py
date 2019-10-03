import os
import sys
from getbingbk import getUnsplashPics
import time


def getPicsName():
    files = os.listdir()

    pics = []
    for f in files:
        (fname,fex) = os.path.splitext(f)
        if(fex == '.jpg'):
            pics.append(fname+'.jpg')
    return pics
class mdeditor(object):
    def __init__(self,fileName,title):
        self.name = fileName
        self.title = title
        self.path = os.getcwd()+'\\'+fileName
    def newFile(self):
        print("mkdir"+" "+os.path.splitext(self.name)[0])
        os.system("mkdir"+' '+os.path.splitext(self.name)[0])
        with open(self.path,'w+') as f:
            f.write(
"""---
title: {title}
data: {data}
---
""".format(title = self.title,data =time.asctime(time.localtime(time.time())))
            )
        return self.name
    def image(self,imageDir,deci):
        try:
            with open(self.path,'a') as f:
                f.write('\n![{disc}]({dir})\n'.format(disc = imageDir,dir = imageDir)
                )
        except Exception as e:
            print("写入文件失败！")
            print(e)    
    
def post(path):
    os.chdir(path)
    os.system("hexo g -d")

if __name__ == "__main__":
    myPicsDowner = getUnsplashPics()
    path = os.getcwd()
    print(path)
    try:
        os.chdir(path+"\\source\\pics")#进入post
    except Exception as e:
        print(e)
    print(os.getcwd())
    myEditor = mdeditor("index.md",'pictures')
    dirName = os.path.splitext(myEditor.newFile())[0]#建立index文件夹
    myPicsDowner.fileSaveLocation = os.getcwd()+'\\'+dirName+'\\'
    myPicsDowner.getRandomPics(picCount=3)
    time.sleep(15)
    os.chdir(path+"\\source\\pics"+'\\'+dirName)#进入pics文件夹
    for p in getPicsName():
        myEditor.image(os.path.splitext(myEditor.name)[0]+'/'+p,'')
    post(path)
    
