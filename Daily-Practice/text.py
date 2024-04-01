# 編寫一個程式，輸入一個字符串，判斷它是不是迴文字符串
text=list(input("請輸入欲判定的字符"))
container_text = tuple(text)
judge = []
    
while len(text)!=0:
    judge.append(text.pop(len(text)-1))

    
if list(container_text)==judge:
    print("這是迴文字符")
else:
    print("這不是迴文字符")
