# 使用plot方法，根據資料點畫出折線圖
import matplotlib.pyplot as plt
# 兩組資料點
# 假如我們要使用兩組資料點，x軸的點要放在同一側；y軸的點要放在同一側(用中括號包起來中括號)(依此類推)
# 一組資料點
plt.subplot(2,2,2)
plt.plot([2,3,4],[4,6,8])

# 兩組資料點
plt.subplot(2,2,1)
plt.plot([2,3,4],[[4,2],[6,3],[8,4]]) #第一組：(2,4)(3,6)(4,8);第二組：(2,2)(3,3)(4,4)
# 圖例與軸線標題
# 圖表中的中文 #設定支援中文的字型 #rc
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
# 標籤與圖例
# 使用label參數設定標籤
# 使用legend 方法產生圖例
plt.subplot(2,2,1)
plt.plot(
    [2,3,4],
    [[4,2],[6,3],[8,4]],
    label = ["第一組","第二組"]
)

# 設定標籤後，呼叫legend產生圖例
plt.legend()

# 軸線的標題
plt.xlabel('x 軸')  # x軸的標題
plt.ylabel('y 軸')  # y軸的標題


# 導入CSV檔
import csv
file = open ("data.csv",encoding="utf-8")
reader = csv.reader(file)
header = next(reader)
print("標頭",header) #csv檔的第一筆資料

x=[] # 預期[2010,2011,2012]
y=[] # 預期[40000,41100],[40200,60000],[60000,50000]
for row in reader:
    print("每列的資料：",row)
    x.append(int(row[0]))
    y.append([int(row[1]),int(row[2])])
plt.subplot(2,2,3)
plt.plot(x,y,label = header[1:3])
plt.legend()
plt.xlabel(header[0])
plt.ylabel('薪資')
plt.show()