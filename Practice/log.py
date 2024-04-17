# selinium
#Selinium：用來做瀏覽器自動化的套件
# 根據標籤的ID去搜尋
"""driver.find_element(By.ID,"搜尋條件")"""
# 根據標籤的任意屬性去搜尋
"""driver.find_element(By.CSS_SELECTOR,"[屬性名稱 = 屬性的值]")"""
# 載入 Selinium 相關模組
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.chrome_executable_path = "C:\Users\Paul2\Downloads\chromedriver_win32.zip"
