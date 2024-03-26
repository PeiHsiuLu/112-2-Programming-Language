import matplotlib.pyplot as plt
import csv
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
# 使用scatter方法繪製散佈圖
def scatter_plot(x,y,c=None,s=None,label=None):
    plt.scatter(x,y,c=c,s=s,label=label)
plt.subplots(1,1)
plt.subplot(1,1,1)  
scatter_plot([2,4,3],[10,20,15],c="green",s=50,label="第一組")
scatter_plot([3,5,8],[1,1.67,2.2],c='black',s=100,label='第二組') # c: 設定顏色 # s: 設定參數：點的大小 # label:組別
plt.legend()
file = open("data.csv",encoding='utf-8')
reader = csv.reader(file)
header = next(reader)
x=[]
y=[]
z=[]
for row in reader:
    x.append(str(row[0]))
    y.append(int(row[1]))
    z.append(int(row[2]))


plt.subplots(1,1)
plt.subplot(1,1,1)
scatter_plot(x,y,c='green',s=50,label='小王')
scatter_plot(x,z,c='grey',s=80,label='小美')
plt.legend()
plt.show()