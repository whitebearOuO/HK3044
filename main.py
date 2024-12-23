import json
import os
import bear
from for_main import first
from for_main import third

'''
此程式總共分配四個章節。
為求整合方便，還有避免變數名稱重複，將不同段的內容變成function呼叫。
如果需要看完全沒改過的原code，請至根目錄查看。

1. 偵測日期提供諺語.py - 陶芷鈺
2. 功能查詢與諺語查詢.py - 陳湘雯
3. 測驗程式.ipynb - 鄭程遠
4. 第二部分測驗.py - 張家綺 (此部分為原預計測驗3-1)

'''

#偵測日期提供諺語 陶芷鈺
first.first()
print()

#功能查詢與諺語查詢 陳湘雯
while 1: #需要讓程式一直執行，回到選單。使用while迴圈
    print("請參考菜單，選擇您需要的功能")
    bear.menu()
    choose=input("請輸入選項[1/2]：")

    if choose=="1": #查詢特定日期諺語
        print()
        bear.menu_option1()
    elif choose=="2": #諺語測驗
        print()
        bear.menu2()
        test_choose=input("請輸入選項[1/2]：")
        if(test_choose=="1"):
            print()
            third.third()

    else: #輸入不在菜單裡的選擇
        print("輸入錯誤，請依照提示進行輸入。")
        print("<回到主菜單>")
        print()
