import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #將中文字體設為微軟正黑體
#(x1,y1)(x2,y2)(x3,y3)
#呈現方式：([x1,x2,x3],[y1,y2,y3])
#x軸為數字，具有連續性
plt.subplot(3,1,1)
plt.bar([1,4,3],[2,5,6])
plt.xlabel("x-test_1")
plt.ylabel("y-test_1")
#但若x軸為字串，則具有離散性
plt.subplot(3,1,2)
plt.bar(["B","A","R"],[2,5,6])
plt.xlabel("x-test_2")
plt.ylabel("y-test_2")


#樣式與軸線
#圖表樣式
#使用wid參數設定寬度，color參數設定顏色
plt.subplot(3,1,3)
plt.bar(
    ["b",'a','r'],
    [2,4,7],
    color = "red",
    width = 0.5
)
plt.xlabel("x-test_3")
plt.ylabel("y-test_3")
#載入CSV格式的檔案
import csv
def salary(human):
    x = []
    y = []
    z = []
    with open("data.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)  #讀取標題(因為是下一個元素)
        for row in reader:
            x.append(str(row[0]))
            y.append(int(row[1]))
            z.append(int(row[2]))
    return x, y, z

# 創建子圖布局
fig, ax = plt.subplots(2,1)
ax[0].set_yticks(np.arange(0, 70000, 10000)) #要記住，結束的那一個永遠不會顯示(80000不會顯示) #10000指的是刻度，0是起始點，800000是結束點(但不會顯示)
ax[1].set_yticks(np.arange(0, 70000, 10000)) #0是指第0個子圖，1是指第一個子圖的意思
# 子圖1
plt.subplot(2,1,1)
x, y, z = salary("小王")
plt.bar(x, y)
plt.xlabel("年度")
plt.ylabel("小王薪水")


# 子圖2
plt.subplot(2,1,2)
x, y, z = salary("小美")
plt.bar(x, z)
plt.xlabel("年度")
plt.ylabel("小美薪水")

plt.show()