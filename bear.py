import json
import os

def wall(): # 菜單的牆壁
    wall="="
    print(wall*20)

def menu(): # 主菜單
    wall()
    print("1. 查詢特定日期諺語（目前僅提供12月份）")
    print("2. 諺語測驗") # 由其他人負責，小選項由我提供
    print("3. 結束程式")
    wall()

def menu_option1(): # 諺語查詢功能
    data = []
    # 如果檔案存在且不為空，讀取現有資料
    if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        while True:
            print("功能1： 查詢特定日期諺語")
            date = input("請輸入日期(四位數字，例如1201): ")
                
            # 檢查是否有相同日期的資料
            existing_entry = next((entry for entry in data if entry["date"] == date), None)
            if existing_entry:
                print(date, ": ", existing_entry["sentence"], sep="") #輸出查詢的諺語
                choose=input("想查看諺語詳細內容嗎？[y/n]： ").lower()
                print()
                if(choose=="y"): # 提供諺語詳細資料
                    if(len(existing_entry["sentence_diff"])>1): # 如果有其他寫法再輸出
                        print("其他寫法：", existing_entry["sentence_diff"])
                    print("意義1 ：", existing_entry["meaning-1"])
                    if(len(existing_entry["meaning-2"])>1): # 如果有其他意義再輸出
                        print("意義2 ：", existing_entry["meaning-2"])
                    print("音標（四縣腔）：", existing_entry["xi-ien"])
                    print("音標（海陸腔）：", existing_entry["hoi-liug"])
                print("<回到主菜單>")
                print()
                break
            else: # 輸入錯誤，讓使用者重新輸入
                print("輸入日期錯誤，請重新輸入")
                print()
                continue

def menu2(): # 測驗用菜單
    wall()
    print("測驗目前提供兩種測驗，請選擇：")
    print("1. 考某段期間的諺語")
    print("2. 自訂考試，自行輸入詞與拼音，進行測驗")
    wall()