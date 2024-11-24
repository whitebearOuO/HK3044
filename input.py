import json
import sys
import os

data = []

# 如果檔案存在，讀取現有資料
if os.path.exists('data.json'):
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

try:
    while True:
        date = input("請輸入日期(四位數字，例如1010): ")
        
        # 檢查是否有相同日期的資料
        existing_entry = next((entry for entry in data if entry["date"] == date), None)
        
        if existing_entry:
            print(f"已存在的句子: {existing_entry['sentence']}")
            update = input("是否更改資料[y/n]: ").strip().lower()
            if update == 'y':
                print("正在更改已有的資料...")
                data.remove(existing_entry)
            else:
                print("正在新增資料...")
                continue
        
        sentence = input("請輸入句子: ")
        meaning_1 = input("請輸入第一個意思: ")
        meaning_2 = input("請輸入第二個意思: ")
        xi_ien = input("請輸入句子的四縣拼音: ")
        hoi_liug = input("請輸入句子的海陸拼音: ")

        entry = {
            "date": date,
            "sentence": sentence,
            "meaning-1": meaning_1,
            "meaning-2": meaning_2,
            "xi-ien": xi_ien,
            "hoi-liug": hoi_liug
        }

        data.append(entry)
except EOFError:
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("\n資料已儲存到 data.json 檔案中")