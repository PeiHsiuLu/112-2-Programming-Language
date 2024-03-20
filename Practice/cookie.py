#cookie: 存放在瀏覽器的一小段內容
#連線時，放在Request Headers 被送出
#連續抓取頁面實務，可以在一個網頁中，抓取另外一個網頁的內容
#解析頁面的超連結，並結合程式邏輯完成
import urllib.request as req
def getData(url):
    #抓取Headers
    request = req.Request(url,headers = {
        "Cookie":"over18=1", #代表要連線時曾經按過的按鈕
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }) #到NetWork處找User-Agent #要先按檢查再找到Network
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    #print(data)

    #解析 ppt 電影板的原始碼
    import bs4
    root = bs4.BeautifulSoup(data,"html.parser") #讓beautifulsoup解析原始碼
    titles = root.find_all("div",class_="title")
    for title in titles:
        if title.a !=None: #如果聯結有效則輸出 #!=None
            print(title.a.string)
    #抓取下一頁的連結
    nextlink= root.find("a",string="下頁 ›")
    return nextlink ["href"]
#主程序(如下)
count=0
Pageurl = "https://www.ptt.cc/bbs/Gossiping/index2.html"
while count<3: #想要抓幾頁資料就寫多少數字
    Pageurl="https://www.ptt.cc/"+getData(Pageurl)
    count+=1
print(Pageurl)
