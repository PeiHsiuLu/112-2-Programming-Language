#類別建立實體物件包裝實體屬性 #要先建立實體物件，才能建立實體屬性
class Point:
    def __init__(self): #定義初始化函式__init__() #建立實體物件self一定要寫
        self.x=3 #括號內的變數.變數名稱x
        self.y=4 #括號內的變數.變數名稱y
#以上是建立實體物件
#此實體物件包含x和y兩個實體屬性
p=Point() #產生實體物件
print(p.x,p.y)

#範例
class Point_1:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
#建立實體物件，並取得實體屬性資料
p=Point_1(1,5)
print(p.x+p.y) #實體物件.實體屬性名稱

#Full Nmae 實體物件的設計
class Name_title:
    def __init__(self,x):
        self.x=x
        
last=Name_title(input("請輸入姓氏： ")) # 變數 = class名稱() #class名稱存入變數

class Name_Name:
    def __init__(self,y):
        self.y=y
        
first = Name_Name(input("請輸入名字： "))

print(last.x + first.y) #輸出變數.程式碼


'''設計一個類別 Book 代表書籍。每本書都有標題、
作者和出版年份等屬性。你的任務是建立 Book 類別，
讓它能夠建立實體物件並包裝這些實體屬性。
然後，建立幾個 Book 物件並存取它們的屬性，以確保你的類別正常運作''' 

class Book:
    def __init__(self, x, y, z, w):
        self.title = x   # 標題
        self.author = y  # 作者
        self.year = z    # 出版年份
        self.edition = w # 版次

# 建立 Book 物件
title_input = input("請輸入標題： ")
author_input = input("請輸入作者： ")
year_input = input("請輸入出版年份： ")
edition_input = input("請輸入版次： ")

my_book = Book(title_input, author_input, year_input, edition_input)

# 印出書籍資訊
print(f"書名：{my_book.title}\n作者：{my_book.author}\n出版年份：{my_book.year}\n版次：{my_book.edition}")


'''設計一個類別 Student 代表學生。
每個學生都有學號、姓名和年齡等屬性。
你的任務是建立 Student 類別，
讓它能夠建立實體物件並包裝這些實體屬性。
然後，建立幾個 Student 物件並存取它們的屬性，
以確保你的類別正常運作。'''

class student:
    def __init__(self,x,y,z):
        self.number = x #x是值的意思 #self.number是變數，回傳值要傳變數
        self.name = y #y是值的意思 #slef.name是變數，回傳值要傳變數
        self.age = z #z是值的意思 #self.age是變數，回傳值要傳變數
        
#建立學生的個別變
number_input = input("請輸入學號")
name_input = input("請輸入姓名")
age_input = input("請輸入年齡")

#將多重變數存入同一個變數
student_list = student(number_input,name_input,age_input)

#輸出變數
print(f"學號：{student_list.number}\n姓名：{student_list.name}\n年齡：{student_list.age}")


'''設計一個類別 Animal 代表動物。
每個動物都有名稱、種類和年齡等屬性。
你的任務是建立 Animal 類別，讓它能夠建立實體物件並包裝這些實體屬性。
然後，建立幾個 Animal 物件並存取它們的屬性，以確保你的類別正常運作。
輸出三種動物'''

class Animal:
    def __init__(self,x,y,z):
        self.name = x
        self.classify = y
        self.age = z
n=1
this_list=[]

while n<4:      
    #建立Animal的變數
    Input_name = input("請輸入是哪一種動物： ")
    Input_classify = input("請輸入動物種類： ")
    Input_age = input("請輸入動物的年齡： ")
    #將動物變數存在一起
    Animal_list =Animal(Input_name,Input_classify,Input_age)
    Animal_print = (f'動物名稱：{Animal_list.name}\n動物種類：{Animal_list.classify}\n動物年齡：{Animal_list.age}\n')
    this_list.append(Animal_print)
    n+=1

for i in range(3):
    print(this_list[i])
    
'''假設你想要建立一個電子商務平台，請設計一個類別 Product 來代表商品。
每個商品都有名稱、價格和庫存等屬性。
你的任務是建立 Product 類別，讓它能夠建立實體物件並包裝這些實體屬性。
然後，建立幾個 Product 物件並存取它們的屬性，以確保你的類別正常運作。'''

class product:
    def __init__(self,x,y,z):
        self.name = x
        self.price = y
        self.quantity = z
items_list = []
for i in range(3):
    print(f"商品{i+1}\n")
    input_name = input("請輸入商品名稱")
    input_price = input("請輸入商品價格")
    input_quantity = input("請輸入商品目前庫存數量\n")
    items = product(input_name,input_price,input_quantity)
    container = (f'商品名稱：{items.name} \n商品價格：{items.price}\n商品目前庫存數量：{items.quantity}\n')
    items_list.append(container)
    if i <2:
        continue
    else:
        for n in range(3):
            print(items_list[n])