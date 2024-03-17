#封裝變數或函式
#封裝的變數或函式，統稱類別的屬性
#Step1. 定義類別
class test: #定義類別名稱 #類別名稱的規則與變數名稱的規則相同
    x=3 #定義變數
    def say(): #定義函式
        print("Hello!") 
#Step2. 使用類別中的封裝的屬性
#基本語法：類別名稱.屬性名稱
test.say() #抓到類別中的函式
print(test.x+3) #抓到類別中的變數+3

#應用一：從網路上抓取資料並放入類別中讀取出來 #動態
import urllib.request as request
import json

class Internet:
    def fetch_data(self,url):
        with request.urlopen(url) as response:
            data = json.load(response)
        return data

    def write_to_file(self,data, filename):
        operation_date = data["result"]["results"]
        with open(filename, mode="w", encoding="utf-8") as file:
            for x in operation_date:
                operate_date = x["營運日"]
                quantity = x['總運量']
                file.write(f"營運日：{operate_date}，總運量：{quantity}\n")

# 創建 Internet 的實例
internet = Internet()

# 從網路上抓取資料
url = 'https://data.taipei/api/v1/dataset/d9621706-cbaf-48cb-8d85-ac062c1dc2d9?scope=resourceAquire'
data = internet.fetch_data(url)

# 寫入文件
internet.write_to_file(data, "臺北捷運全系統旅運量統計.txt")

#上課範例：
class IO:
    supportedSrcs= ["console","file"] #設定變數
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print('Read from',src) 
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")