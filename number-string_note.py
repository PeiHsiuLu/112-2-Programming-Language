#0309練習

# 一、數字運算
#加法(+)
5+3
#減法(-)
5-2
#乘法(*)
5*6
#整數除法(//)，除到整數位
print(5//3) #答案為1，因為1...2
#小數除法(/)，直接除盡
print(5/3)
#除法取餘數(%)
print(7%2) #答案為1，因為1...1，取餘數=1
#次方(**)
print(5**3)

#將變數做加法運算(x=x+1 or x+=1)
x=0
x+=1
print(x)

#將變數做減法運算(x-=1)
x-=1
print(x)

#將變數做乘法運算(x*=2)
x=4
x*=3
print(x)

#將變數做小數除法運算(x/=3)
z=8
z/=2
print(z)

#將變數做整數除法運算(x//=3)
z//=2
print(z)

#將變數取餘數
z%=2
print(z)

#將變數做次方運算(y**=1)
y=2
y**=3

print(y)


# 二、字串運算

#使用雙引號或單引號或三引號
print("Hello World")

#字串可用+做連接
print("Hey"+" Bro")

#反斜線\可以寫文字內的雙引號或是引號
print("Hello\"修哥\"")

#也可以直接做字串串接
print("hello""hello")

#換行\n
print("hello\nworld")

#使用三個引號可直接做換行
print('''我是
      
      
      
     修哥''')#換三行

#字串可做乘法運算
handsome="修哥好帥"
print(handsome*4)

#三、字串會對內部的字元編號(索引，由0開始為第一位)
print(handsome[0])
print(handsome[1])
print(handsome[2])
print(handsome[3])

#字串索引從一個位置到一個位置以前(ex.[0:2]只會從第0位到第1位數)
print(handsome[0:2])
#只要從第幾位到第幾位而已，只有開頭標示([0:])
print(handsome[2:])
#只要從第幾位到第幾位而已，只有結尾標示([:5])
print(handsome[:2])