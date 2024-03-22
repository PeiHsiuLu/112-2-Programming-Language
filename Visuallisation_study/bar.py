import matplotlib as plt
#(x1,y1)(x2,y2)(x3,y3)
#呈現方式：([x1,x2,x3],[y1,y2,y3])
#x軸為數字，具有連續性
plt.bar([1,4,3],[2,5,6])
#但若x軸為字串，則具有離散性
plt.bar(["B","A","R"],[2,5,6])
#圖表樣式