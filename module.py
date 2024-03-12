#module
#import 模組名稱 或是 # import 模組名稱 as 模組別名
import sys as s #更改別名稱為s

s.path.append("modules")
#從geometry.py 模組載入使用
import geometry #在模組的搜尋列表中新增路徑

#算出兩點距離
result = geometry.distance(1,4,3,8)# 計算兩點距離：(1,3) (4,8)
print(result)

#算出斜率
result = geometry.slope(1,4,3,8)
print(result)



print(s.platform) #印出作業系統
print(s.maxsize) #印出整數型態的最大值 
print(s.path) #印出搜尋模組的路徑
print(s.version) #印出當前使用的 python 版本
