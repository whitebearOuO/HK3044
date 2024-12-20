import json
import os
import bear
from for_main import first

'''
此程式總共分配四個章節，為求整合方便直接將不同段的內容變成function。
如果看完全沒改過的原code，請至根目錄查看。

1. 偵測日期提供諺語.py - 陶芷鈺
2. 功能查詢與諺語查詢.py - 陳湘雯
3. 測驗程式.ipynb - 鄭程遠

程式整合：陳湘雯
簡報製作：陶芷鈺
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
        bear.menu_option1()
    elif choose=="2": #諺語測驗
        bear.menu2()
        test_choose=input("請輸入選項[1/2]：")

    else: #輸入不在菜單裡的選擇
        print("輸入錯誤，請依照提示進行輸入。")
        print("<回到主菜單>")
        print()
