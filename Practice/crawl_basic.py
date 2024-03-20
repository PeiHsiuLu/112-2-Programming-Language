#爬蟲定義：連線到特定網址，抓取特定資料
#解析資料，獲取真正想要的部分
#抓取資料-爬蟲關鍵心法：盡可能讓程式模仿一個普通使用者的樣子
#解析資料：
#JSON格式資料，使用JSON內建模組即可
#大部分是HTML格式資料：使用Beautifulsoup第三方套件進行解析
#必須先安裝beutifulsoup4才能進行分析

#試著爬 ppt 電影板的網頁
import urllib.request as req

url = "https://www.ptt.cc/bbs/movie/index.html"
# Create a Request object and attach Request Headers
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}) #一定要有這個步驟，才會被當正常使用者


with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
#print(data)

#解析 ppt 電影板的原始碼
import bs4
root = bs4.BeautifulSoup(data,"html.parser") #讓beautifulsoup解析原始碼
print(root.title) #root.標籤名稱，可抓到標籤名稱的內容 #root.title 可抓到<title>
print(root.title.string) #可抓到標籤內的字串
div = root.find("div", class_="btn-group btn-group-dir") #尋找class="btn-group btn-group-dir"的div標籤
print(div)
print(div.a.string) #可搜尋文字 #先找到a連結，再抓到文字

link = root.find_all("link", rel="stylesheet") #rel="stylesheet"是條件，link是標籤
print(link)

titles = root.find_all("div",class_="title")
print(titles)

print("\n分野區\n")
for title in titles:
    if title.a !=None: #如果聯結有效則輸出 #!=None
        print(title.a.string)


