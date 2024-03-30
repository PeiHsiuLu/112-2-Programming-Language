# 實現一個程式，判斷給定的整數是否為質數。
n = eval(input("請輸入欲判斷的數值"))

# 我寫的程式碼：
if n<=0 or type(n)==float:
    print("對不起，請重新輸入數值！")
elif n==1:
    print(f"{n}既不是質數，也不是合數")
else:
    for i in range (n):
        i+=1
        n2=n%i
        if i==1:
            continue
        elif n2==0 and (n!=i):
            print(f"{n}是合數")
            break
        else:
            if n-i !=0:
                continue
            else:
                print(f"{n}是質數")
                
# chatgpt 協助修正後的程式碼：
n = eval(input("請輸入欲判斷的數值："))

if n <= 0 or type(n) == float:
    print("對不起，請重新輸入正整數！")
elif n == 1:
    print(f"{n}既不是質數，也不是合數")
elif n == 2:
    print(f"{n}是質數") #2是最小的質數，要做另外處理
else:
    for i in range(2, int(n**0.5) + 1):  # 修正迴圈範圍 #因為最大的因數除了自己以外，一定是平方根
        if n % i == 0:
            print(f"{n}是合數")
            break
    else:
        print(f"{n}是質數")
