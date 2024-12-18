import json
import os
import bear
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
