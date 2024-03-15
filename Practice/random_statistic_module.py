import random #載入亂數模組
#從列表中隨機選取一個資料
data=random.choice([1,2,5,8])
print(data)
#從列表中隨機選取兩筆資料 #或是兩筆以上資料
data=random.sample([2,3,1,6],2)
print(data)

#隨機調換變數資料
data=[0,1,5,8]
random.shuffle(data) #shuffle：推開
print(data)

#隨機亂數

#取得0.0-1.0之間的隨機亂數 #出現機率相同
data=random.random() #相當於下面的隨機亂數 #指0到1之間的隨機亂數
print(data)
data=random.uniform(0.0,1.0) #uniform意思是機率相同 #可取數值1以上的數值
print(data)

#常態分配亂數

#取得平均數=100，標準差=10 #得到的資料多數會在90-110之間
data=random.normalvariate(100,10) #alvariate：方差分析 #第一個數值是平均數，第二個數值是標準差 
print(data)

#常態分配亂數：取得平均數=0,標準差=5 #得到的資料多會在-5～5之間
data=random.normalvariate(0,5)
print(data)
#載入統計模組
import statistics
#計算列表中數值的平均數
data=statistics.mean([5,2,3,9]) #用列表將數值包起來
print(data)

#計算列表中數值的中位數
data=statistics.median([9,4,1,3])
print(data)
#計算列表中數值的樣本標準差
data=statistics.stdev([1,4,9,3,8])
print(data)

#練習小專案：選擇今日晚餐：
dinner=random.choice(['義肥','牛老大','鮮魚湯',"大台北滷味",'楓月女僕咖啡廳'])
print("今天的晚餐就吃"+dinner+"!")