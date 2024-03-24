# HW2_視覺化資料分析：鐵達尼號乘客名單推敲生還者資訊
# 請助教批閱時，圖表部分請全畫面檢視

# 零、架設Matplotib與Pandas環境：

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 將中文字體設為微軟正黑體


# 一、先做篩選與計算各個項目的資訊(生還者、死亡人數)

# 00. 讀取資料
df = pd.read_csv("titanic_data_repair.csv")

# 01. 計算各艙等的總乘客數量
passenger_df = df[df['Pclass'].isin(["First","Second","Third"])].groupby('Pclass').size()

# 02. 計算各艙等的總生還者
survival_data = df[(df['Survived'] == 'alive') & (df['Pclass'].isin(["First", "Second", "Third"]))].groupby('Pclass').size()

# 03. 計算各艙等的總死亡人數
death_data = df[(df['Survived'] == 'death') & (df['Pclass'].isin(["First", "Second", "Third"]))].groupby('Pclass').size()

# 04. 計算總生還人數
total_survival_data = (df['Survived'] == 'alive').sum()

# 05. 計算總死亡人數
total_death_data = (df['Survived'] == 'death').sum()

# 06. 將各年齡層依序分組
age_bins = [0, 13, 61, 81] # 0-12歲為一組(兒童)；13-60歲為一組(青壯年)；61-80歲為一組(老人)
age_labels = ['兒童', '青壯年', '老人']
df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)

# 07. 篩選出各年齡層生還人數
Pclass_survival = df[df['Survived'] == 'alive'].groupby(['Age_Group', 'Pclass'], observed=False).size()

# 08. 篩選出各年齡層死亡人數
Pclass_death = df[df['Survived'] == 'death'].groupby(['Age_Group', 'Pclass'], observed=False).size()

Pclass_Survival_dict = Pclass_survival.to_dict()
Survival_values= [value for value in Pclass_Survival_dict.values()]
Pclass_Death_dict = Pclass_death.to_dict()
Death_values= [value for value in Pclass_Death_dict.values()]
list_Pclass=['First','Second','Third']
colors_1 = ['red','yellow','blue']



# 二、Pandas 圖表

# 00. 各艙層乘客人數：
def Pclass_passengers():
    passenger_df_dict = passenger_df.to_dict()
    keys = [key for key in passenger_df_dict.keys()]
    values = [value for value in passenger_df_dict.values()]

    df = pd.DataFrame({'count': values})
    df.index = keys

    df = df.sort_values(by='count', ascending=True)

    df['perc(%)'] = round(df['count']/df['count'].sum()*100,2)

    df['cumperc(%)'] = round(df['count'].cumsum()/df['count'].sum()*100,2)

    print(f'\n各艙層乘客人數如下：\n\n{df}')
    return df


    
# 三、統計圖表

# 00. 柱狀圖    
def bar_plot(x, y, width, color='blue'):
    plt.bar(x, y, width, color=color)
    
# 01. 折線圖
def line_plot(x,y,color="blue"):
    plt.plot(x,y,color=color)
    
# 02. 散佈圖

# 03. 圓餅圖


# 四、問題函式

# 00. 問題零：我想知道，不同艙等階級的人數有多少？(柏拉圖呈現)
def question_0():
    plt.subplots(1, 1)
    plt.subplot(1, 1, 1)
    df = Pclass_passengers()
    bar_plot(df.index, df['count'], width=0.5, color="blue")
    plt.xlabel('Pclass', labelpad=10, fontsize=15, color='black', fontweight='bold')
    plt.ylabel('乘\n客\n人\n數', rotation=0, labelpad=30, fontsize=15, color='black', fontweight='bold')
    plt.title('三個艙等人數', pad=10, fontsize=20, color='black', fontweight='bold')
    plt.twinx()
    line_plot(df.index, df['cumperc(%)'], color='red')
    plt.ylabel('乘\n客\n人\n數\n累\n積\n百\n分\n比', rotation=0, labelpad=30, fontsize=15, color='black', fontweight='bold')
    plt.gca().yaxis.set_major_formatter(PercentFormatter())
    plt.figtext(0.05, 0.95, '問題零', fontsize=20, color='black', fontweight='bold')

# 01. 問題一：我想知道，三個艙等的生還者人數的高低落差，是否會因為社會階級不同而影響到生還率高低？(利用圓餅圖呈現)
def question_1():
    1

# 02. 問題二：我想知道票價是否與艙等有關係 (一張散佈圖)
def question_2():
    1

# 03. 問題三：我想瞭解不同階層不同年齡層是否會影響生存人數？(三張柱狀圖)
def question_3():
    for i in range(3):
        plt.subplots(1,3)
        plt.figtext(0.05, 0.95, f'問題三：不同艙層的{age_labels[i]}存亡概況', fontsize=20, color='black', fontweight='bold')
        for n in range(3):
            plt.subplot(1, 3, n+1)
            if i ==0:
                plt.yticks(np.arange(0, 10, 1))
            elif i ==1:
                plt.yticks(np.arange(0, 150, 10))
            else:
                plt.yticks(np.arange(0, 10, 1))
            bar_plot(['alive','death'],[Survival_values[n+i*3],Death_values[n+i*3]],width=0.5,color={colors_1[n]})
            plt.xlabel(f"{list_Pclass[n]}", labelpad=10, fontsize=15, color='black', fontweight='bold')
            plt.ylabel('乘\n客\n人\n數', rotation=0, labelpad=10, fontsize=15, color='black', fontweight='bold')
            
            
            

# 五、主程式

def main():
    # 問題零-問題三
    question_0()
    question_1()
    question_2()
    question_3()
    # 顯示從問題零-問題三的所有圖表
    plt.show()


# 六、四大問題 & 回答問題

# 00. 問題零：我想知道，不同艙等階級的人數有多少？(柏拉圖呈現)
# 01. 問題一：我想知道，三個艙等的生還者人數的高低落差，是否會因為社會階級不同而影響到生還率高低？(利用圓餅圖呈現)
# 02. 問題二：我想知道票價是否與艙等有關係 (散佈圖)
# 03. 問題三：我想瞭解不同階層不同年齡層是否會影響生存人數？(柱狀圖)


'''以下是四大問題的作答，回答問題 (程式如下)'''
main()
'''以上四大問題回答完畢，感謝助教辛苦批閱'''

