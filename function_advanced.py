# 函式參數詳解：參數預設值、名稱對應、任意長度參數
# 一、預設資料：
#def 函式名稱(參數名稱 = 預設資料):
    #函式內部的程式碼
    
def sayhello(msg = "Hello"):
    print(msg)
sayhello("HelloFunction") #會印出HelloFunction，因為更改了變數名稱
sayhello() #只有()會印出預設資料

# 二、呼叫函式，以參數名稱對應資料

def number(n1,n2):
    print(n1)
    print(n2)

number(n2=5,n1=3) #指定參數名稱，即便順序調換也不會有影響 #回傳資料必須是明確的變數資料

#定義一個可以做加法的函式
def divide(n1,n2):
    result = n1/n2
    return result
value=divide(2,4)+divide(n2=2,n1=4)
print(value)

#三、無限參數
#def 函式名稱(*無限參數): 無限參數的參數名稱前必須加入一個星星，代表無限長度的參數
    #無限參數以tuple資料型態處裡
    #函式內部的程式碼
#呼叫函式，可傳入無限數量的參數
#函式名稱(資料一,資料二,資料三...)#無限長度

def say(*msgs):
    #以Tuple的方式做處理
    for msg in msgs:
        print(msg)
        
#呼叫函式，傳入三個參數資料
say("hello","hi","how are you")

def number(*numbers):
    for num in numbers:
        print(num)
        
number(1,2,3,4,5,6,7,8,9,10)

#練習：利用無限參數，印出：
#系級:
#姓名:
#性別：

#印出五位同學

def classmate(*classmates):
    for people in classmates:
        department = input("\n請輸入"+people+"的系級： ")
        sex = input("請輸入"+people+"的性別： ")
        print("\n系級："+department)
        print("姓名："+people)
        print("性別："+sex)

classmate("王大明","李曉華","陳小美","王阿花","林美鳳")
        




#練習題：利用無限參數算出平均數
def average_(*numbers):
    sum=0
    for number in numbers:
        sum+=number
    average = sum/(len(numbers))
    return average

value = average_(52,49,36,78,92)
print(value)
    
        