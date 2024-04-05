# 編寫一個程式，檢查一個字符串是否是另一個字符串的子串。
str_1=input("請輸入字串1")
str_2=input("請輸入字串2")

if str_1 in str_2:
    print(f"{str_1}是{str_2}的子串")
else:
    print(f"{str_1}不是{str_2}的子串")