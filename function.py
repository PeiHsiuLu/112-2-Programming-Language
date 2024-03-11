#函式基礎：定義並呼叫函式 
#def 函式名稱(參數的名稱):
    #函式內部的程式碼
#程式範例-1
def sayhello():
    print("hello")
sayhello() #呼叫函式

#可命名變數：括號內的變數可以任意命名
def say(msg):
    print(msg)
    
say("hello")
say('hi') #使用函式的好處：可用相同的程式用在不同變數

#程式範例-2：兩數相加
def add(n1,n2): #命名兩個變數 n1 和 n2 
    result=n1+n2
    print(result)
add(12,17)
add(155,1770)

#return
#return 分為回傳值和呼叫值
#首先，要先寫return回傳值
def recall():
    print("hello") #這只是僅僅用來作為呼叫程式的程式碼
    return("這是回傳值")#呼叫後主要是回傳return的資料

value=recall()#先設立一個變數儲存函式
print(value) #印出來的結果會是return值

#程式範例-3
def saymsg(msg):
    print(msg)
    return
value = saymsg("Hello Function!")
print(value) #回傳None

#程式範例-4
def add(x,y):
    print(x+y)
    return ("hello")

this_add=add(10,11)
print(this_add)

#練習題-1：利用函式算出乘法
n1 = int(input("請輸入數字1"))
n2 = int(input("請輸入數字2"))

def multiply(n1,n2):
    result=n1*n2
    return result

#呼叫multiply
value = multiply(n1,n2)#會分兩次執行，一次執行mulitiply()
print(value) #一次回傳value

#練習題-2：先做次方再做加法
def multiply_plus(N1,N2):
    return N1**N2
value = multiply_plus(3,4)+multiply_plus(10,10) #會先執行(3,4)再執行(10,10)，分別回傳到return，最後做相加
print(value)

#程式的包裝
#因為有些程式必須重複反覆撰寫，所以使用函式
#練習題3：從1加到20
def calculate():
    sum=0
    for x in range(1,21):
        sum+=x
    print(sum)
calculate()

#chatgpt生成練習題：成績評級系統
#成績評級系統：

#設計一個函式，該函式接受一個學生的成績作為輸入（介於0到100之間），然後根據成績給出相對應的評級。評級標準如下：

#90分以上為A等
#80分至89分為B等
#70分至79分為C等
#60分至69分為D等
#60分以下為F等
#然後，函式應該返回該學生的評級。你可以使用if-elif-else語句來實現評級系統，並在函式中使用input函式來接受學生的成績。

def score():
    Score_student= int(input("請輸入該位學生的成績"))
    if Score_student >=90:
        print("A")
    elif Score_student>=80:
        print("B")
    elif Score_student>=70:
        print("C")
    elif Score_student>=60:
        print("D")
    else:
        print("F")
    return

score()

