# 用實體物件設計：平面座標上的點距離
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)
    def distance(self,targetX,targetY):
        return (((self.x-targetX)**2+(self.y-targetY)**2)**0.5)
P1 = Point(3,4)
P2 = Point(0,0)
P1.show()
result = P1.distance(0,0)
print(result)

#file 實體物件的設計
class file:
    def __init__(self,name):
        self.name=name
        self.file=None #尚未開啟檔案：初期是 None
    #實體方法
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
    
#讀取第一個檔案
f1=file("data.txt")
f1.open()

data = f1.read()
print(data)

#讀取第二個檔案
f2=file("if.py") #不論檔案名為何，一樣都是會印出裡面的檔案內容
f2.open()

data_2=f2.read()
print(data_2) 
