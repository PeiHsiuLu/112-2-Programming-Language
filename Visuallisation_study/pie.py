# 圓餅圖繪製
import matplotlib.pyplot as plt
import csv
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 將中文字體設為微軟正黑體
# 一、資料點的呈現
# 01. 使用pie方法，根據一個為度的資料點畫出圓餅圖
# 資料點x的範例如下：
# 20,30,40
# 標籤、圖例與標題
# 01. 使用labels參數設定標籤，使用legends方法產生圖例
# 02. 使用labeldistance參數設定標籤位置，0代表圓心，1代表圓周
# 03. 使用title方法設定圖表標題
def pie_plot(x, labels=None, labeldistance=0.5, title=None):
    total = sum(x)
    plt.title(title)
    plt.pie(x, labels=[f'{round((val/total)*100,2)}%' for val in x], labeldistance=labeldistance)
    plt.legend()
plt.subplots(1,3)
plt.subplot(1,3,1)
pie_plot([20,30,40],labeldistance=0.5, title='這是一個圓餅圖')
plt.subplot(1,3,2)
pie_plot([40,50,40],labeldistance=0.5, title='這是第二個圓餅圖')


# 04. 開啟CSV讀取檔案
file = open("pie-chart.csv",encoding="utf-8")
reader = csv.reader(file)
header = next(reader)
x=[]
y=[]
for row in reader:
    x.append(int(row[1]))
plt.subplot(1,3,3)
pie_plot(x,labeldistance=0.5,title='瀏覽器市佔率')
plt.show()
