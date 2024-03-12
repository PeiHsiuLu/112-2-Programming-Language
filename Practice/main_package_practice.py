#專案檔案配置
#封包：模組進行分類、包裝稱作封包
#專案資料夾
    #主程式.py
    #封包資料夾
       # __init__.py(封包資料夾必備資料夾，否則就是普通資料夾而已) (兩條底線init兩條底線.py)
       #模組一.py
       #模組二.py
#使用封包：
    #import 封包名稱.模組名稱 
    #import 封包名稱.模組名稱 as 模組別名

import Practice.geometry_practtice.line as line
import Practice.geometry_practtice.point as point
result_point = point.distance(58,8)
result_line_1 = line.len(5,6,8,7)
result_line_2 = line.slope(5,0,8,1)

print("距離",result_point)
print("長度",result_line_1)
print("斜率",result_line_2)