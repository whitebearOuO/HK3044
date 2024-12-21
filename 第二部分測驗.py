# 測驗system 1 拼音
import json
import random

# 呼叫資料庫
try:
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)  # 讀取 JSON 資料
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"讀取資料庫時出錯: {e}")
    exit()

# 確保資料庫格式正確
if not isinstance(data, dict):
    print("資料庫格式錯誤，應該是題目對應答案的字典格式！")
    exit()

# 定義範圍選擇變數
date = list(data.keys())  # 假設範圍根據題目的鍵來選擇
print(f"資料庫中共有 {len(date)} 題目範圍。")

# 顯示題目範圍
for i, key in enumerate(date, 1):
    print(f"{i}: {key}")

# 用戶選擇題目範圍
while True:
    try:
        start = int(input("請輸入起始範圍的編號："))
        end = int(input("請輸入結束範圍的編號："))
        if 1 <= start <= len(date) and 1 <= end <= len(date) and start <= end:
            break
        else:
            print("請確保範圍有效，且起始值小於等於結束值！")
    except ValueError:
        print("請輸入有效的整數範圍！")

# 根據選擇的範圍過濾資料
selected_data_keys = date[start - 1:end]
filtered_data = {key: data[key] for key in selected_data_keys}

# 用戶選擇題目數量
total_questions = len(filtered_data)
print(f"範圍內共有 {total_questions} 題目。")
while True:
    try:
        num_questions = int(input(f"請輸入想測驗的題數（最多 {total_questions} 題）："))
        if 1 <= num_questions <= total_questions:
            break
        else:
            print(f"請輸入 1 到 {total_questions} 之間的數字！")
    except ValueError:
        print("請輸入有效的整數！")

# 隨機選取題目
selected_questions = random.sample(list(filtered_data.items()), num_questions)

# 初始化分數
score = 0

# 開始遊戲提示
print("\n拼寫測驗")
print(f"本次測驗共有 {num_questions} 題，請根據看到的諺語，拼寫出客語音標。\n")

# 測驗迴圈
for i, (question, correct_answer) in enumerate(selected_questions, 1):
    print(f"第 {i} 題：{question}")
    user_answer = input("請輸入該諺語的客語拼音：").strip().lower()

    # 判斷答案正確性
    if user_answer == correct_answer.strip().lower():
        print("你答對了！\n")
        score += 1
    else:
        print(f"你答錯了！正確答案是：{correct_answer}\n")

# 顯示總分
print(f"測驗結束！你獲得了 {score}/{num_questions} 分！\n")

# 顯示正確答案
print("以下是正確答案：")
for question, correct_answer in selected_questions:
    print(f"諺語：{question}")
    print(f"拼音：{correct_answer}\n")
