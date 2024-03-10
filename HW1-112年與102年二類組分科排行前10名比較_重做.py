#因為有極高的完美主義，加上第一次繳的作業我覺得做得太爛，所以我決定重新繳過一份
#首先先讀取要分析的兩個檔案
import pandas as pd
df1 = pd.read_csv('102年二類組分科排名比較.csv')
df2 = pd.read_csv('112年二類組分科排名比較.csv')

# 將兩檔案進行合併
merged_df = pd.merge(df1, df2, on='排名', suffixes=('_112', '_102'))

# 刪除Unnamed列
merged_df.drop(columns=['Unnamed: 2'], inplace=True)

# 將結果寫入新的CSV文件
merged_df.to_csv('merged_file.csv', index=False, encoding='utf-8')

#輸出112年與102年二類組的分科排名前十名結果
print("\n"+str(merged_df))

#將兩CSV檔的科系資料轉換成列表形式

#將df1轉換成列表
second_column_df1 = df1.iloc[:,1]
second_column_set_df1 = set(second_column_df1)

#將df2轉換成列表
second_column_df2 = df2.iloc[:,1]
second_column_set_df2 = set(second_column_df2)

#輸出聯集結果：在過去10年曾經出現過的熱門校系
print("\n聯集結果："+str(second_column_set_df2 | second_column_set_df1))

#輸出交集結果：在過去10年都是二類組考生心目中的熱門校系
print("\n交集結果："+str(second_column_set_df1&second_column_set_df2))

#輸出差集結果：在112年將102年的熱門校系取而代之的新校系
print("\n差集結果："+str(second_column_set_df2 - second_column_set_df1))