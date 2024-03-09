# 一、集合的運算

#集合並無順序性
#判斷值是否出現在集合(in or not in)
A={5,4,3}
print(4 in A) #True
print(6 not in A) #True
print(5 not in A) #False
B={5,4,54,36,78}
#交集& 取兩個集合中共同的資料
print(A&B)
#聯集| 取兩個集合中所有的資料，但不重複取
C=A|B
print(C)
#差集 - 從一集合中，減去另一集合重疊之處
C= A-B #3 只會出現A集合，但消除與B集合重疊之處
print(C)
C=B-A
print(C) #78,36,54 只會出現B集合，但消除與A集合重疊之處
#反交集^ 取兩個集合中，不重疊的部分
C=A^B
print(C)
#字串會拆解成集合
s=set("apple")
print(s)

# 二、字典的運算：key-value
dic={"apple":"蘋果","banana":"香蕉","orange":"橘子"}
#找值(直接 dic[key] )
print(dic["apple"]) #該key的值
#可修改字典的值
dic["apple"]="小蘋果"
print(dic)
#可用 in 或 not in 判斷字典中的值是否存在 (但是是判斷 key 不是 value)
print("test" in dic)
#刪除字典中的key
del dic["apple"]
print(dic)
#字典中的變數運算
dic={x:x*2 for x in [6,7,8]} #for是迭代遍歷結構，會將列表的值代入x執行運算
print(dic)
