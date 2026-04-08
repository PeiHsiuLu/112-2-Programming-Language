# 112-2 師大科技系程式語言 
授課教師：蔡芸琤教授  
姓名：呂沛修  
系級：科技系二年級


# 一、期末專題 - AI人臉情緒辨識
主要是導入模型訓練 ai 辨識人臉的六大情緒(AI影像辨識) ："Happy","Angry","Sad","Surprise","Neutral","Fear"  
## 所使用到的技術
1. tensorflow
2. numpy
3. keras
4. gradio  
## 關於我們的AI期末專題
### 為甚麼想要做AI人臉情緒辨識的專題
有些人不會管理自己的表情，常常讓人覺得是在擺著一張臭臉或心情不好，導致社交困難。

透過臉部城管家，可以開始管理自己的表情，笑臉迎人過每一天！  

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


# 二、課堂作業連結區
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

[HW4_LLM&Jieba關聯圖生成](https://colab.research.google.com/drive/1qytVBIjxypYkJBfhDik-zeqobz55WzRx?usp=sharing)  


# 三、python 小專題  
  
[1. 師大本部人的三餐選擇器 2024/03/16](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/folio/choose_food.py)  
[2. 下載 YT MP4格式影片 2024/04/28](https://colab.research.google.com/drive/1ufR0NN8A3fwTDEYdncKc4PMP5wcVeUBW#scrollTo=EZMkT6MhBpJ) 



# 四、利用python下載youtube  
為了個人需求，寫了代碼方便自己從yt下載影片  
[下載YT影片程式碼_pytube的使用](https://github.com/PeiHsiuLu/112-2-Programming-Language/blob/main/Video-Download/video_download.py)  


