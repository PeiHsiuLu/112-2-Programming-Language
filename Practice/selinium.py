#Selinium：用來做瀏覽器自動化的套件
# 1. 網頁截圖
# 2. 爬蟲
# 3. 自動化測試

"""今日待辦事項"""
# Step1 下載 Chrome Driver 驅動程式
# Step2 安裝 Selinium 套件
# Step3 撰寫程式，完成網頁截圖

#載入Selinium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 設定 Chrome Driver 的可執行檔路徑
options = Options()
options.chrome_executable_path = "C:\\path\\to\\chromedriver.exe"

# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/") #想打開的網址
driver.close()
