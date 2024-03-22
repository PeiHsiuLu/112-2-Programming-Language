#HW2_視覺化資料分析：鐵達尼號乘客名單推敲生還者資訊

# 零、架設pandas與統計圖表的環境

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
plt.rcParams # 先將圖表設為中文可以解讀


# 一、先做篩選與計算各個項目的資訊(生還者、死亡人數)

# 01. 讀取並用pandas方式列出鐵達尼號部分乘客名單(鐵達尼號乘客總數2200人，但裡頭的資料僅有418筆)
df = pd.read_csv("titanic_data_repair.csv")

# 02. 計算出三個等艙個別的總乘客數量 #頭等艙=1 二等艙=2 三等艙=3
passenger_df = df[df['Pclass'].isin([1,2,3])].groupby('Pclass').size()

# 03. 計算各艙等的總生還者
survival_data = df[(df['Survived'] == 1) & (df['Pclass'].isin([1, 2, 3]))].groupby('Pclass').size()

# 04. 計算各艙等的總死亡人數
death_data = df[(df['Survived'] == 0) & (df['Pclass'].isin([1, 2, 3]))].groupby('Pclass').size()

# 05. 計算總生還人數
total_survival_data = (df['Survived'] == 1).sum()

# 06. 計算總死亡人數
total_death_data = (df['Survived'] ==0).sum()



# 二、統計圖表 (以下是所會用到的統計圖表)

# 01. 折線圖
x=[]
y=[]
def line_plot():
    plt.plot(x,y)

line_plot()
# 02. 柱狀圖
def bar_plot():
    plt.bar(x,y)

# 03. 柏拉圖

# 04. 散佈圖

# 05. 圓餅圖





# 三、三大問題

# 01. 問題一：我想知道，三個艙等的生還者人數的高低落差，是否會因為社會階級不同而影響到生還率高低？(利用柏拉圖呈現)
# 02. 問題一(延伸)：頭、二等艙與三等艙的生還人數比較我想知道 (柱狀圖)
# 03. 問題二：我想知道票價是否與艙等有關係
# 04. 問題三：年齡有影響到生還機率嗎？(柱狀圖)