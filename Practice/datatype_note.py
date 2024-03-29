#2024/03/09 練習
#資料：程式的基本單位

#數字：
12345 #整數 int
1.5 #浮點數 float
#eval 可將字串轉為數值
print(type(eval('1.5')))

#字串：
#必須用文字來表示
"修哥好帥"
"你好啊"

#布林值(Boolean)：
True
False

#有順序，可變動的列表：
#內部可以是集合(set)、字典(dict)、數字(整數或小數)、字串(str)、布林值(True or False)、元組
this_list=[1,2.5,True,False,"Hi",{"數學":"Math","國文":"Chinese"},(1,2,3),{5,4,3}]#列表內的值中的字典或是列表也會在輸出時，變成由小到大排列

# 01. list 串列(列表)
#使用中括號[A,B,C]
#由左往右第一個數值是0，由右往左第一個數值是-1
print(f'這是列表：{this_list[-3:-1]}') #一般來說都是從左往右看，所以-3也自然是擺在前頭
# 使用 len() 函數來計算長度
print(len(this_list))

# 列表新增一個值：
this_list.append(9) #新增數值9於尾端
del this_list[-3:-1] #刪除倒數第三和倒數第二位
# 列表插入新的值：
this_list.insert(0,[29,28,37]) #在第幾位插入
this_list.pop(0) #指清除第幾位的意思
print(this_list)
#集合(set)
#無順序概念
#主要用於聯集、交集、差集 #用大括號表示
A={1,3,5,7,9}
B={2,4,6,8,10}
C={2,3,5,7}
#聯集：
print(A|B|C) #有重複數值也不會重複出現，僅僅會出現一次
#交集
print(A&C)
print(B&C)
#差集
print(B-C)
print(A-C)

#利用add和remove來新增或刪除資料
print(A.add(11)) #添加11這個值於末尾
print("這是移除"+str(B.remove(8))) #移除8數值
print(A|B)
#字典(dict)：
#使用引號和半形的冒號
Apple_dict={"Apple":"蘋果"}
{'有':"ji3"}
Apple_dict["Banana"]="香蕉"
del Apple_dict['Apple']
print(f'新字典{Apple_dict}')

#字典的key值不可變動，但是value可變動
#遍歷尋找key和value
key = {key for key in Apple_dict}
print(key) 
value = {value for value in Apple_dict.values()}
print("值",value) #逗號有空格含義

#元組(tuple)：
T=(5,4,3)
A=(T,{"國文":95,"數學":90})
print(A[0][0])#找出變數A中第0位元組中第0位的數值：5

#變數(variable)：
#用來儲存資料的名稱
#變數名稱=資料名稱
#變數 (存資料的記憶體)
#常用一個有意義的名稱，來存放值(可為數值、文字…)，值可以重新設定或經運算修改
#第一個字元可以是英文、中文、或底線(_) 像是__init__，但不可以是數字，第二個字元以後就可用數字
#不可以有空白、特殊符號
#例如：item 2, box@name
#英文字元有區分大小寫
#有些關鍵字、內建函數等保留字不可使用 (例如 class)
x=3
y=5

#判斷變數型態可用type
print(type(x))

#變數刪除可用 del 變數
# 例子：del x



#輸出(print)：
print(x)
print(y)

#逐行輸出結果

#變數有可被替換性

x=5
y=3

#輸出的結果會不同

print(x)
print(y)

# 反斜線的功用(反斜線本身有轉譯的作用，所以先加\，再加入要加入的符號，便可成功轉譯)
# 01.換行：
print('\n我是\n修哥')
# 02. tab鍵
print('\t這是tab鍵')
# 03. 表示引號
print('My\'name\'is \'Billy\'')
# 04. 表示反斜線
print("這是反斜線：\\")


