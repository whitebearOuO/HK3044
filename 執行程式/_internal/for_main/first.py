import json
import datetime

def first():
    today = datetime.date.today() # 獲取今天的日期
    print("今天是", today)  # 顯示今日日期
    today = datetime.date.today().strftime("%m%d") # 獲取今天的日期，並格式化為 "MMdd" 格式
    # 開啟並讀取 JSON 檔案
    with open('data.json', 'r', encoding="utf-8") as file:
        data = json.load(file)

        sen = next((entry for entry in data if entry['date'] == today), None)  # 查找符合今天日期的資料

        # 判斷是否找到對應資料
        if sen:
            print("今日每日一句：", sen['sentence'])
            print("意義 1：", sen['meaning-1'])

            # 僅當 'meaning-2' 有值時才輸出
            if sen.get('meaning-2'):
                print("意義 2：", sen['meaning-2'])

            print("音標（四縣腔）：", sen['xi-ien'])
            print("音標（海陸腔）：", sen['hoi-liug'])
        else:
            print("查無資料")
