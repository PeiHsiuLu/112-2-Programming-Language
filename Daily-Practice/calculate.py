# 實現一個計算器程序，接受用戶輸入兩個數字和一個操作符（例如+、-、*、/），並輸出計算結果。
n1 = eval(input("請輸入數字1\n"))
n2 = eval(input("請輸入數字2\n"))
op = input("請輸入運算子(+,-,*,/)\n")


if op == "+":
    print(n1+n2)
elif op =="-":
    print(n1-n2)
elif op =="*":  
    print(n1*n2)
elif op =="/":
    if n2 ==0:
        print("除數不能為0！")
    else:
        print(f"計算結果：{n1/n2}")
else:
    print("不合法的運算")