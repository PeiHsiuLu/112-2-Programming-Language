# Python Module 模組的載入與使用教學
#被導入的幾何模組
#在 geometry 模組中定義幾何運算功能

#計算兩點的距離
def distance(x1,x2,y1,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

#計算線段的斜率
def slope(x1,x2,y1,y2):
    return(y2-y1)/(x2-x1)