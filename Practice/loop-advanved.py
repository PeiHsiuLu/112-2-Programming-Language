#進階迴圈

# 一、break
#意義：用在迴圈內(for、while)強制結束迴圈
#範例0：
while True:
    break
for x in range(3):
    break
#範例一：
n = 1
while n<5:
    if n==4:
        break #加到四強制中止迴圈
    n+=1
print(n)

# 二、continue 
#強制執行迴圈命令

#範例二 ：
n = 0
for x in [0,1,2,3]:
    if x%2==0:
        continue 
    n+=1
print(n) #印出數字二

#contine 與 #break 的差異：
#continue：強制回到開頭繼續執行迴圈
#break：強制離開迴圈

# 三、else
#迴圈結束前執行該區塊的命令

#範例三：
s = 0
while s<10:
    print(s)
    s+=1
else:
    print("迴圈要結束啦！")#迴圈結束前最後一圈執行此命令

g = 0
for g in range(9): #印出0-8
    print(g)
else:
    print("要結束拉！") #迴圈最後一圈結束前執行此命令
    
for c in "Hello":
    print(c)
else:
    print("hi")
    

#綜合範例：請找到整數平方根
number = int(input("請輸入想要求的數值"))

for i in range(number):
    if i*i == number:
        print(str(number)+"的整數平方根為"+str(i))
        break
else:
    print(str(number)+"沒有整數平方根")
    
#chatgpt協助設計的題目：計算 1 到 100 之間的所有奇數之和，但遇到能被 13 整除的奇數時，跳過該數的計算。
sum = 0
for n in range(1,101):
    if n%13 ==0:
        continue
    else:
        if n%2 ==0:
            continue
        else:
            sum+=n

print(sum)

# 範例
i = 0
while i < 10:
    i = i + 1
    if i %3 != 0:
        continue
    print(i)
    # 輸出3,6,9
i = 0
while i < 10:
 i = i + 1
 if i %5 == 0: #到5脫離迴圈
  break
 print(i) #印出1,2,3,4


# range
range(2) #輸出0,1
range(2,5) #第一位：開頭；第二位：結束
range(10,-10,-2) #第一位：開頭 :第二位：結束；第三位：等差數列
    