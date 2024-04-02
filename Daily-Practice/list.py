# 將兩個列表合併為一個，並按升序
import random


def random_num(*containers ): #可設定為任意變數
    container=[]
    for i in range (5):
        number = random.randint(0,100)
        container.append(number)
    return container

    
def merge_and_sort(list_1,list_2):
    merge_list=list_1+list_2 #合併列表
    merge_list.sort() #sort可由小到大排列
    return merge_list

def main():
    x=[]
    y=[]
    value_1=random_num(x)
    value_2=random_num(y)
    Merge_Sort_List = merge_and_sort(value_1,value_2)
    print(Merge_Sort_List)
    return Merge_Sort_List
    
    
    
main()


        
