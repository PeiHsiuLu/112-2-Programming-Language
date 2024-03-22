#HW2_視覺化資料分析：鐵達尼號乘客名單推敲生還者資訊

# 零、架設pandas與統計圖表的環境

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


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

# 07. 計算男性總生還人數
ms_data = ((df['Survived'] == 1) & (df['Sex'] == 'male')).sum()

# 08. 計算男性總死亡人數
md_data = ((df['Survived'] == 0) & (df['Sex'] == 'male')).sum()

# 09. 計算女性總生還人數
fs_data = ((df['Survived'] == 1) & (df['Sex'] == 'female')).sum()

# 10. 計算女性總死亡人數
fd_data = ((df['Survived'] == 0) & (df['Sex'] == 'female')).sum()

# 11. 計算頭等艙男性生還人數
ms_1_data = ((df['Survived'] == 1) & (df['Sex'] == 'male') &(df['Pclass']==1)).sum()

# 12. 計算頭等艙男性死亡人數
md_1_data = ((df['Survived'] == 0) & (df['Sex'] == 'male') &(df['Pclass']==1)).sum()

# 13. 計算二等艙男性生還人數
ms_2_data = ((df['Survived'] == 1) & (df['Sex'] == 'male') &(df['Pclass']==2)).sum()

# 14. 計算二等艙男性死亡人數
md_2_data = ((df['Survived'] == 0) & (df['Sex'] == 'male') &(df['Pclass']==2)).sum()

# 15. 計算三等艙男性生還人數
ms_3_data = ((df['Survived'] == 1) & (df['Sex'] == 'male') &(df['Pclass']==3)).sum()

# 16. 計算三等艙男性死亡人數
md_3_data = ((df['Survived'] == 0) & (df['Sex'] == 'male') &(df['Pclass']==3)).sum()

# 17. 計算頭等艙女性生還人數
fs_1_data = ((df['Survived'] == 1) & (df['Sex'] == 'female') &(df['Pclass']==1)).sum()

# 18. 計算頭等艙女性死亡人數
fd_1_data = ((df['Survived'] == 0) & (df['Sex'] == 'female') &(df['Pclass']==1)).sum()

# 19. 計算二等艙女性生還人數
fs_2_data = ((df['Survived'] == 1) & (df['Sex'] == 'female') &(df['Pclass']==2)).sum()

# 20. 計算二等艙女性死亡人數
fd_2_data = ((df['Survived'] == 0) & (df['Sex'] == 'female') &(df['Pclass']==2)).sum()

# 21. 計算三等艙女性生還人數
fs_3_data = ((df['Survived'] == 1) & (df['Sex'] == 'female') &(df['Pclass']==3)).sum()

# 22. 計算三等艙女性死亡人數
fd_3_data = ((df['Survived'] == 0) & (df['Sex'] == 'female') &(df['Pclass']==3)).sum()


# 二、統計圖表 (以下是所會用到的統計圖表)

# 01. 柏拉圖

# (1) 先將生還者人數轉為集合
n=1
ps_survival_list = []
while n<4:
    ps_survival_list.append(survival_data.to_dict().get(n,0))
    n+=1

# (2) 創建DataFrame
pc_s_list = pd.DataFrame({'count': ps_survival_list})
pc_s_list.index = ['First class', 'Second class', 'Third class']

# (3) 將數值由小到大排列
pc_s_list = pc_s_list.sort_values(by='count', ascending=True)

# (4) 具體計算每個count值的累積
pc_s_list['cumperc'] = pc_s_list['count'].cumsum()/pc_s_list['count'].sum()*100

# (5) 設計柏拉圖的美觀
color1 = 'steelblue'
color2 = 'red'       
line_size = 4
fig, ax = plt.subplots()
ax.bar(pc_s_list.index, pc_s_list['count'], color=color1)

# (6) 增加折線圖
ax2 = ax.twinx()
ax2.plot(pc_s_list.index, pc_s_list['cumperc'], color=color2, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())

# (7) 設置左右兩側y軸的刻度顏色
ax.tick_params(axis='y', colors=color1)
ax2.tick_params(axis='y', colors=color2)

# (8) 設定柏拉圖的標題
plt.title('The survival of each class\n')

# 02. 柱狀圖





# 三、三大問題

# 01. 問題一：我想知道，三個艙等的生還者人數的高低落差，是否會因為社會階級不同而影響到生還率高低？(利用柏拉圖呈現)
# 02. 問題一(延伸)：頭、二等艙與三等艙的生還人數比較我想知道 (柱狀圖)
# 03. 問題二：有關於男女生還比例，我想要知道；並且，我想知道其他三個艙等男女生還比例各是多少 (圓餅圖)
# 04. 問題三：年齡有影響到生還機率嗎？(柱狀圖)