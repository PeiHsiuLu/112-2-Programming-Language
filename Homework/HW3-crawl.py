import urllib.request as req
import pandas as pd
import bs4
import numpy as np
import json
# HW3:解析 ppt 軍事板的原始碼

def getData(url):
    #抓取Headers
    request = req.Request(url,headers = {
        "Cookie":"over18=1", 
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }) 
    
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")


    root = bs4.BeautifulSoup(data,"html.parser") 
    titles = root.find_all("div",class_="title")
    date = root.find_all("div",class_="date")
    t=[]
    d=[]
    for title in titles:
        if title.a !=None: 
            t.append(title.a.string)
    df = pd.DataFrame({'Title': t})
    
    
    for date_ in date:
        d.append(date_.string)
    df['dates']=d
    print(df)
    
    # CSV存檔
    df.to_csv("military.csv", index=False)
    # JSON存檔
    df.to_json("military.json", orient="records", force_ascii=False, lines=True)
    print("\n\n\n")
    
    
    


#主程序(如下)
count=0
Pageurl = "https://ptt-info.tw/bbs/Military/index.html"
getData(Pageurl)
for i in range(10):
    print("CSV 和 JSON 皆已存檔成功囉！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")


