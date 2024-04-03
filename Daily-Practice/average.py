#  編寫一個程式，計算給定列表中所有元素的平均值。

def average(*numbers):
    this_list = []
    sum=0
    n=0
    while True:
        number = int(input('請輸入數值(輸入0即為停止)'))
        if number==0:
            break
        else:
            this_list.append(number)
    print(f"列表：{this_list}")
            
    for i in this_list:
        sum+=i
        n+=1
        this_average = round(sum/n,2)
        
        
    print(this_average)
        
average()