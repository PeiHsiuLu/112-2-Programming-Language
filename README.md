# 112-2 師大科技系程式語言 
授課教師：蔡芸琤教授  
姓名：呂沛修  
系級：科技系二年級

# 一、入門自主學習筆記區
這是我自主學習的紀錄，期望可以透過紀錄自己學習python的過程，讓自己變得更好！ 
  
[01. 自主學習：變數與資料型態 2024/03/09](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/datatype_note.py)  
[02. 自主學習：數字、字串的基本運算 2024/03/09](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/number-string_note.py)  
[03. 自主學習：有序列表的基本運算 - List、Tuple 2024/03/09](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/list-tuple.py)  
[04. 自主學習：集合、字典的基本運算 - Set、Dictionary 2024/03/09](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/set-dict.py)  
[05. 自主學習：流程控制：if 判斷式 2024/03/10](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/if.py)  
[06. 自主學習：流程控制：迴圈基礎，while 迴圈、for 迴圈 2024/03/10](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/loop.py)  
[07. 自主學習：流程控制：迴圈進階控制，break、continue、else 命令 2024/03/11](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/loop-advanved.py)  
[08. 自主學習：函式基礎：定義並呼叫函式 2024/03/11](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/function.py)  
[09. 自主學習：函式參數詳解：參數預設值、名稱對應、任意長度參數 2024/03/12](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/function_advanced.py)  
[10. 自主學習：Module 模組的載入與使用 2024/03/12](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/module.py)  
[11. 自主學習：Package 封包的設計與使用 2024/03/12](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/main_package_practice.py)  
[12. 自主學習：文字檔案的讀取和儲存 2024/03/15](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/file.py)  
[13. 自主學習：亂數與統計模組 2024/03/15](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/random_statistic_module.py)  
[14. 自主學習：網路連線程式、公開資料串接 2024/03/17](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/internet.py)  
[15. 自主學習：類別的定義與使用 - Class Attributes 2024/03/17](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/class.py)  
[16. 自主學習：實體物件的建立與使用 - 上篇 - 實體屬性 2024/03/19](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/classify-1.py)  
[17. 自主學習：實體物件的建立與使用 - 下篇 - 實體方法 - Instance Methods 2024/03/19](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/classify-2.py)  
[18. 自主學習：網路爬蟲 Web Crawler 基本教學 2024/03/20](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/crawl_basic.py)  
[19. 自主學習：網路爬蟲 Web Crawler 教學 - Cookie 操作實務 2024/03/20](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Practice/cookie.py)  

# 二、期末專題 - AI人臉情緒辨識
主要是導入模型訓練 ai 辨識人臉的六大情緒(AI影像辨識) ："Happy","Angry","Sad","Surprise","Neutral","Fear"  
## 所使用到的技術
1. tensorflow
2. numpy
3. keras
4. gradio  
## 關於我們的AI期末專題
### 為甚麼想要做AI人臉情緒辨識的專題
有些人不會管理自己的表情，常常讓人覺得是在擺著一張臭臉或心情不好，導致社交困難。

透過臉部城管家，可以開始管理自己的表情，讓人隨時看起來都是開心的。

### 鎖定受眾
1. 大眾層面 – 面部表情控制：協助進行表情控制
2. 企業層面 – 人力資源徵才：內心：開心 >>> 表現：憤怒

### 技術上如何實現這樣的服務
1. Gradio 網頁展示：利用上傳的照片或是影片轉換成偵測的情緒，進行輸出
2. 深度學習：自主運用Tensorflow套件訓練AI模型(桌機)、Kaggle資料集：FER-2013 (10000多張照片)
3. 運行的程式環境 - Jupyter Notebook：可用記憶體較大，沒有像是colab的記憶體用量限制


## 各次進度
[0423-0501 第一次提案成果展示](https://www.youtube.com/watch?v=_fisrHrd9S4)  
[0502-0515 第二次提案成果展示](https://www.youtube.com/watch?v=7CXz_LF7uAY)  
[0516-0606 期末成果展示](https://www.youtube.com/watch?v=2kOsxPXWxgI)  

## 訓練模型與檔案
[訓練的模型](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Final_Project/model%20.h5)  
[AI 情緒模型訓練檔](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/emodetect%20(3).ipynb)  
[使用模型來輸出影片或即時辨識](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/emooutput_.ipynb)  
[Gradio 成果展示](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/gradio.ipynb)  

## 這次的 AI 模型訓練心得
這次挑選AI影像辨識來做為我們的期末專題，主要是因為想要對AI有更深一層的了解。在做專題的同時，也發現到訓練AI模型的不易：如果電腦性能不夠好(GPU規格不夠)，就難以進行模型訓練，因為AI模型訓練非常需要有強大的GPU做後援。












# 三、視覺化自主學習區
Matplotlib資料視覺化  
  
[ 01. 自主學習：折線圖 2024/03/22](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Visuallisation_study/line.py)  
[ 02. 自主學習：長條圖 2024/03/22](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Visuallisation_study/bar.py)  
[ 03. 自主學習：圓餅圖 2024/03/25](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Visuallisation_study/pie.py)  
[ 04. 自主學習：散佈圖 2024/03/26](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Visuallisation_study/scatter.py)  


# 四、課堂作業連結區
[HW1：利用Pandas讀取CSV檔進行資料分析 — 112年與102年二類組分科排行前10名比較](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Homework/HW1-112%E5%B9%B4%E8%88%87102%E5%B9%B4%E4%BA%8C%E9%A1%9E%E7%B5%84%E5%88%86%E7%A7%91%E6%8E%92%E8%A1%8C%E5%89%8D10%E5%90%8D%E6%AF%94%E8%BC%83_%E9%87%8D%E5%81%9A.py)  
[HW1：分析報告](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Homework/HW1%EF%BC%9A%E5%88%86%E6%9E%90112%E8%87%B3102%E5%B9%B410%E5%B9%B4%E4%B9%8B%E9%96%93%E7%9A%84%E4%BA%8C%E9%A1%9E%E7%B5%84%E7%86%B1%E9%96%80%E7%A7%91%E7%B3%BB%E5%89%8D%E5%8D%81%E5%90%8D.pdf)  

[HW2：利用Matplotlib進行各項資料分析(柱狀圖、圓餅圖、柏拉圖、散佈圖) — 鐵達尼號乘客名單推敲生還者資訊](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Homework/HW2_%E8%A6%96%E8%A6%BA%E5%8C%96%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%EF%BC%9A%E9%90%B5%E9%81%94%E5%B0%BC%E8%99%9F%E4%B9%98%E5%AE%A2%E5%90%8D%E5%96%AE%E6%8E%A8%E6%95%B2%E7%94%9F%E9%82%84%E8%80%85%E8%B3%87%E8%A8%8A.py)  
[HW2：分析報告](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Homework/HW2%5E7%E8%A6%96%E8%A6%BA%E5%8C%96%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%5E7%E9%90%B5%E9%81%94%E5%B0%BC%E8%99%9F%E4%B9%98%E5%AE%A2%E5%90%8D%E5%96%AE%E6%8E%A8%E6%95%B2%E7%94%9F%E9%82%84%E8%80%85%E8%B3%87%E8%A8%8A.pdf)  
[HW2：圖表(四大問題DataFrame&Matplotlib圖表)](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Homework/HW2-Matplotlib%20%E5%9C%96%E8%A1%A8(%E6%9F%B1%E7%8B%80%E5%9C%96%E3%80%81%E5%9C%93%E9%A4%85%E5%9C%96%E3%80%81%E6%9F%8F%E6%8B%89%E5%9C%96%E3%80%81DataFrame)%20(1).pdf) 
  
[HW3：練習爬蟲(PTT軍事版)](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Homework/HW3-crawl.py)  
[HW3_CSV](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Homework/military.csv)  
[HW3_JSON](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Homework/military.json)  
[HW3_程式碼執行結果](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/%E7%B5%90%E6%9E%9C.png)  
[HW3_YT解說影片](https://www.youtube.com/watch?v=kuLXT4rfXcE)

[HW4_LLM&Jieba關聯圖生成](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Homework/HW4.ipynb)  


# 五、Markdown 語法說明
Markdown 語法說明：https://markdown.tw/
# 六、python 小專題  
有時太忙沒有自主學習，就利用20-30分鐘的零星時間做些小專案，訓練手感  
  
[1. 師大本部人的三餐選擇器 2024/03/16](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/folio/choose_food.py)  
[2. 下載 YT MP4格式影片 2024/04/28](https://colab.research.google.com/drive/1ufR0NN8A3fwTDEYdncKc4PMP5wcVeUBW#scrollTo=EZMkT6MhBpJ) 

# 七、python 7 日小專題訓練  
感謝chatgpt協助設計題目 - 7日計畫：  


[ Day01 實現一個計算器程序，接受用戶輸入兩個數字和一個操作符（例如+、-、*、/），並輸出計算結果。 2024/03/29](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Daily-Practice/calculate.py)  
[ Day02 實現一個程式，判斷給定的整數是否為質數 2024/03/30](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Daily-Practice/prime.py)  
[ Day03 編寫一個程式，輸入一個整數 n，輸出費波納契數列的前 n 項 2024/03/31](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Daily-Practice/F.py)  
[ Day04 編寫一個程式，輸入一個字符串，判斷它是不是迴文字符串](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Daily-Practice/text.py)  
[ Day05 將兩個列表合併為一個，並按升序](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Daily-Practice/list.py)  
[ Day06 編寫一個程式，計算給定列表中所有元素的平均值](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Daily-Practice/average.py)  
[ Day07 編寫一個程式，檢查一個字符串是否是另一個字符串的子串。](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Daily-Practice/same-text.py)

# 八、利用python下載youtube  
為了個人需求，寫了代碼方便自己從yt下載影片  
[下載YT影片程式碼_pytube的使用](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Video-Download/video_download.py)  


