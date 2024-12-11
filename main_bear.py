import json
import os
#功能查詢與諺語查詢

#function
def menu():
    wall="="
    print(wall*20)
    print("1. 查詢特定日期諺語（目前僅提供12月份）")
    print("2. 諺語測驗") #由其他人負責，小選項由我提供
    print(wall*20)

def menu_option1():
    data = []
    # 如果檔案存在且不為空，讀取現有資料
    if os.path.exists('data.json') and os.path.getsize('data.json') > 0:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        while True:
            print("功能1： 查詢特定日期諺語")
            date = input("請輸入日期(四位數字，例如1010): ")
                
            # 檢查是否有相同日期的資料
            existing_entry = next((entry for entry in data if entry["date"] == date), None)
            if existing_entry:
                print(date, ": ", existing_entry['sentence'], sep="")
                print("<回到主菜單>")
                print()
                break
            else:
                print("輸入日期錯誤，請重新輸入")
                print()
                continue

def menu2():
    wall="="
    print(wall*20)
    print("測驗目前提供兩種測驗，請選擇：")
    print("1. 考某段期間的諺語")
    print("2. 自訂考試，自行輸入詞與拼音，進行測驗")
    print(wall*20)

#main
while 1:
    print("請參考菜單，選擇您需要的功能")
    menu()
    choose=input("請輸入選項[1/2]：")

    if choose=="1":
        menu_option1()
    elif choose=="2":
        menu2()
        test_choose=input("請輸入選項[1/2]：")
    else:
        print("輸入錯誤，請依照提示進行輸入。")
        print("<回到主菜單>")
        print()
