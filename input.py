import json
import sys

data = []

try:
    while True:
        date = input("請輸入日期(四位數字，例如1010): ")
        sentence = input("請輸入句子: ")
        pinyin1 = input("請輸入句子的第一個拼音: ")
        pinyin2 = input("請輸入句子的第二個拼音: ")

        entry = {
            "date": date,
            "sentence": sentence,
            "pinyin1": pinyin1,
            "pinyin2": pinyin2
        }

        data.append(entry)
except EOFError:
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("\n資料已儲存到 data.json 檔案中")