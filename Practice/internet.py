import urllib.request as request #導入urllibrary，抓取網路公開資料
# Step 1 下載特定網址資料
# Step 2 尋找合適的資料來源
# Step 3 確認資料格式(Json CSV 或其他格式)

#網路連線
#src = "https://www.ntnu.edu.tw"
#with request.urlopen(src) as response: #括號要輸入網址 #取得師範大學的網站原始碼(HTML、CSS、JS)
    #data = response.read().decode("utf-8") #用decode("utf-8")解碼
#print(data)

#串接、擷取公開資料
#利用Json格式處理公開資料
import json
src="https://od.moi.gov.tw/api/v1/rest/datastore/301210000T-002243-002"
with request.urlopen(src) as response:
    data = json.load(response) #利用json模組處裡json格式
#print(data)

this_list=data["result"]["records"] #從字典中搜索出一個值
#enumerate函式可被用於一個可遍歷的數據對象
#將資料裝進檔案中
with open("opendata.txt",mode="w",encoding="utf-8") as file:#檔案名稱,模式,encoding="utf-8"
    for index,x in enumerate (this_list): #利用index變數來記錄目前的變數索引值
        if index == 0:
            continue
        name=x["Name"]
        position=x["Position"]
        file.write(f'姓名：{name},職稱：{position}'+"\n")


    
    
    