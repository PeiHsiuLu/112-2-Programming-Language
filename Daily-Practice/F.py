# 編寫一個程式，輸入一個整數 n，輸出費波納契數列的前 n 項。
n = int(input("請輸入欲輸出的項目數(前n項)"))
sum = 0
number_1=0
number_2=1
for i in range(n+1):
    if i ==0:
        print(number_1)
    elif i==1:
        print(number_2)
    else:
        current_number=number_1+number_2
        print(current_number)
        number_1 = number_2
        number_2 = current_number