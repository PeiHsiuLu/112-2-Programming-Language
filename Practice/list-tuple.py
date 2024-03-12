# 一、有序可變動列表list []
grades=[50,69,100,89,76]
print(grades)
#取得列表位置資料[索引數字]
print(grades[0])
#更改列表位置資料
grades[0]=60 #更改第0位的資料
print(grades)
#選擇範圍輸出(ex. [0:4] 會出現到第4位，[0:]會從第0位開始輸出到結束 [:3]會輸出到第二位)
print(grades[0:4])
print(grades[:4])
print(grades[0:])
#更改列表(可直接在列表值的範圍上做更動)
grades[0:]=[80,89,100,99,98]
print(grades)
#空列表
empty=[]
print(empty)
#刪除列表資料
grades[1:4]=[] #直接賦予一個空值，就可以刪除列表資料了
print(grades)
#額外新增列表資料
grades[2:10]=[88,79,76,54,63,20,21,22]
print(grades)
#列表的加法
grades=grades+[2,3]
print(grades)
#列表的長度(len)
print(len(grades))
#巢狀列表：列表內還有列表
nest=[[5,[56,34,[65,[71,73,[74]]]],20],[32,20,17],[53,68,90]]
#找到巢狀列表的位置，用索引符號旁邊再加索引
print(nest[0][1][2][1][2][0])
# 二、有序不可變動列表tuple ()
#tuple可用索引值，但不可變更位置
this_tuple=(5,4,3.5)
print(this_tuple)
#強制變更tuple
chage_tuple=list(this_tuple) #(先將原先的tuple轉換成list)
chage_tuple[0:]=[60,71,78,96,74]
this_tuple=tuple(chage_tuple) #再將被改正的list轉回tuple
print(this_tuple)

