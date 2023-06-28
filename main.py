from pywhatkit import *
from pytube import YouTube
from pafy import new
def search():
    topic=input("enter the topic:")
    playonyt(topic)
    link()

def video_download():
    url = input("enter the link:")
    yt = YouTube(url)
    print("the description of video :")
    print("title:",yt.title)
    print("length",yt.length,"sec")
    yt.streams.filter(only_video=True)
    yt.streams.filter(progressive=True)
    pix=input("need to download maximum resolution (max) or minimum resolution (min) : ")
    if pix=="max":
        dow=yt.streams.get_highest_resolution()
    elif pix=="min":
        dow=yt.streams.get_lowest_resolution()
    print("download started...................")
    dow.download("D:")
    print("download completed :):)")

def audoi_download():
    ur=input("enter the link:")
    mu=new(ur)
    print("the description of video :")
    print("title:", mu.title)
    print("length", mu.length, "sec")
    do=mu.getbestaudio()
    print("download started...................")
    do.download()
    print("download completed :):)")
def link():
    fil=input("need to download audio (audio) or video (video)")
    if fil=="audio":
        audoi_download()
    elif fil=="video":
        video_download()

com=input("need to search a video for download enter 'video' or having link enter 'link' : ")
if com=="video":
    search()
elif com=="link":
    link()