# 如何利用Python下載yt影片
from pytube import YouTube
yt  = YouTube("https://www.youtube.com/watch?v=Udvz99WBEkw&list=RDUdvz99WBEkw&index=1")
print("影片下載中，請等待")
yt.streams.first().download()
print("影片下載完成")