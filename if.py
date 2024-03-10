#if 判斷式
#if 布林值 Boolean if=True 則會執行，否則若是False，則執行else

#判斷式 在 if 中，唯有 True 才會執行
if True:
    print("True")
    
#判斷式if，若是False就不會執行
if False:
    print("True") #False就不會執行 #裡面的內容必須使用Tab鍵
    
#else 執行if!=True的情況 or if=False
x=True

if x:
    print("True")
else:
    print("執行 False")

y=False

if y:
    print("不執行")
else:
    print("執行False")
    
#input 輸入 (裡面的字串文字是提示文字)
z = int(input("請輸入數字(整數)")) #必須將字串轉為數字，因為input一定是字串 #int可將字串轉換成整數，float可將字串轉換成浮點數

#if elif else:(多重判斷)

if z>200:
    print("z大於200")
elif z == 200:
    print("z等於200") #兩個==，代表等於的意思。一個等於是設定變數
else:
    print("z小於200")

#簡單的四則運算(依舊遵循先乘除後加減，有括號要先算的規律)
n1 = int(input('請輸入數字1 '))
n2 = int(input("請輸入數字2 "))
print(n1+n2)

#利用if製作簡易的計算器
number_1 = int(input('請輸入數字1 '))
number_2 = int(input('請輸入數字2 '))
op = input("請輸入運算符號(+,-,*,/,%,//,**) ")

if op == "+":
    print(number_1 + number_2)
elif op =="-":
    print(number_1 - number_2)
elif op == "*":
    print(number_1*number_2)
elif op == "/":
    print(number_1/number_2)
elif op == '//':
    print(number_1//number_2)
elif op == "%":
    print(number_1%number_2)
else:
    print("不支援運算")
