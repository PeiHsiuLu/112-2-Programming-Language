#文字檔案的讀取和儲存
#檔案操作流程：1. 開啟檔案 > 2. 讀取或寫入 > 3. 關閉檔案
# Step1. 開啟檔案(open file)
    # 檔案物件=open(檔案路徑,mode=開啟模式(開啟、讀取或是讀寫))
    #讀取：r #寫入(儲存)：w #讀寫：r+
    #讀取全部檔案：檔案物件.read()
    # 一行一行讀取：for 變數 in 檔案物件：從檔案中依序讀取每行文字到變數中
    #讀取JSON格式 import json 
    #讀取到的資料=json.load(檔案物件)

#Step2. 寫入(儲存檔案)
    #寫入文字：檔案物件.write(字串)
    #寫入換行符號：檔案物件.write("這是範例文字\n")
    #寫入JSON格式：
    #Import json
    #json.dump(要寫入的資料,檔案物件)

#Step3. 關閉檔案
    #檔案物件.close()
    #最佳關閉檔案的方法：with open(檔案路徑,mode=開啟模式) as 檔案物件：
    #讀取或寫入檔案的程式
    #以上區塊會自動且安全地關閉檔案
    
#儲存檔案
#file = open("data.txt", mode="w",encoding="UTF-8")#"mode="w"(儲存檔案) #開啟 #中文檔案必須寫入encoding="UTF-8"
with open("data.txt", mode="w",encoding="UTF-8") as file: #利用with open打開檔案
    file.write("Hello File\nSecond Hello\n哈囉！") #操作 (寫入或讀取) #寫入下一行 #新資料會直接覆蓋舊資料
    file.close() #關閉 #可加可不加，因為會自動關閉
with open("data_number.txt",mode="w",encoding="utf-8") as file:
    file.write('5\n3\n5\n6')
#讀取檔案 #只能讀取已存在的檔案
with open("data.txt",mode = "r",encoding = "utf-8") as file:
    data = file.read() #一定要加入括號，否則會出錯誤
print(data)

sum = 0
with open("data_number.txt",mode = "r",encoding = "utf-8") as file:
    for line in file:
        sum+=int(line)
print(sum)
import json
#從檔案中讀取 JSON 資料，放入變數 data 裡面
with open("config.json",mode="r") as file:
    data=json.load(file)
#把最新的資料複寫回檔案
data["name"]="My Name"
print(data) #data是一個字典
print("name：",data["name"]) #印出"name"的值
print("version：",data["version"]) #印出"version"的值

# 從檔案中讀取 JSON 資料，放入變數 data 裡面
with open("config.json", mode="r") as file:
    data = json.load(file)

# 修改變數中的資料
data["name"] = "Pei-Hsiu Lu" #用中文會出現亂碼
print(data['name'])
# 把最新的資料寫回檔案
with open("config.json", mode="w") as file:
    json.dump(data, file)
