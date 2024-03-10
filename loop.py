#迴圈運算

#while 若布林值 = True 執行命令，回到上方，做下一次的迴圈運算 (也就是說可以做無限多次)。直到False才會結束迴圈。
#範例程式：
n=1
while n<10:
    print(n)
    n+=1 #加總直到n=10，因為當n==10時，則為False
    #ctrl+C 可以強制關閉程式
#小練習：練習從1加到10累加==55

N=1
Sum=0
while N<=10:
    Sum+=N
    N+=1
print(Sum)


#for
#for 後面加變數名稱 in 列表或字串
#將列表中的項目或字串中的字元逐一取出，逐一處裡
#範例程式(數字)：
for x in [4,2,1]:
    print("逐一取得列表中的資料",x) #會逐一輸出4,2,1
    
#範例程式(字串)：
for y in "hello":
    print("逐一生成字元：",y)
    
#for迴圈也可搭配 range()
#for 變數名稱 in range(n) 基本上 == for 變數名稱 in [0,1,2,...,n-1](基本上不會包含n)
for w in range (9):
    print(str(w)+"\n")
#for 變數名稱 in range (範圍) 相當於 for 變數名稱 in [範圍中的所有數字，但不包含最尾端的]
for z in range (1,6): #從1開始，但不會包含6在內
    print(z)
#用在列表上[]
for thislist in [1,2,6,5,1,1,3,5,4,7,8,9,10]: #會依序生成所有列表內的值
    print(thislist)
    
#利用for做1累加到10，變成55
sum=0
for s in range(1,11):
    sum+=s
print(sum)