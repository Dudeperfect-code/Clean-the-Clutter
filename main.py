import os
import shutil
f = os.listdir()
f.remove("main.py")     #removing main.py from the list
files=[i.lower() for i in f]    # lowering all elements

docExt = [".doc",".docx",".docm",".pdf",".ppt",".ppt",".dot",".dotx",".dotm",".xml",".xlsx",".txt"]
vidExt = ['.webm','.ogg','.mpeg','.mpg','.mp2','.mpe','.mpv','.mp4','.m4p','.m4v','.avi','.wmv','.mov','.qt','.avchd','.flv','.swf']
musExt = ['.mp3',".whl"]
imgExt = ['.jpeg','.jpg','.png','.gif','.raw','.bmp','.tif','.tiff']
comp = [".rar","zip",".torrent"]
code = [".html",".sql",".py",".php",".css","js",".c",".c++",".c#",".htm"]

def check(word,list):   #checks for extension present in presets
    for i in list:
        if i in word:
            return True
    else:
        False

def Createfolder(name):          #Create folder if not exist
    if not os.path.exists(name):
        os.mkdir(name)

def move(folder,file):           #Move Files
    shutil.move(file,f"{folder}/{file}")

for i in files:
    if check(i,docExt):
        Createfolder("Documents")
        move("Documents",i)
    elif check(i,vidExt):
        Createfolder("Videos")
        move("Videos",i)
    elif check(i,imgExt):
        Createfolder("Images")
        move("Images",i)
    elif check(i,comp):
        Createfolder("Compressed")
        move("Compressed",i)
    elif check(i,code):
        Createfolder("Code Files")
        move("Code Files",i)
    elif check(i,musExt):
        Createfolder("Music")
        move("Music",i)
    elif os.path.isdir(i):
        Createfolder("Folders")
        move("Folders",i)

