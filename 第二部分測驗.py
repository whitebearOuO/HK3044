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

# 定義日期選擇變數
date = list(data.keys())  # 範圍根據資料庫中的鍵
print(f"資料庫中共有 {len(date)} 個題目範圍。")

# 顯示可選的題目範圍
for i, key in enumerate(date, 1):
    print(f"{i}: {key}")

# 用戶選擇範圍
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

# 根據範圍過濾資料
selected_data_keys = date[start - 1:end]
filtered_data = {key: data[key] for key in selected_data_keys}

# 計算題目總數
total_questions = len(filtered_data)
print(f"範圍內共有 {total_questions} 題目。")

# 用戶選擇題數
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
selected_questions = random.sample(list(filtered_data.values()), num_questions)

# 初始化分數與記錄回答
score = 0
results = []  # 用於記錄題目與答案

# 開始遊戲提示
print("\n拼寫測驗")
print(f"本次測驗共有 {num_questions} 題，請根據看到的句子，輸入正確的拼音。\n")

# 測驗迴圈
for i, question_data in enumerate(selected_questions, 1):
    sentence = question_data.get("sentence", "題目缺失")
    xi_ien = question_data.get("xi-ien", "無正確答案")
    hoi_liug = question_data.get("hoi-liug", "無正確答案")

    # 顯示題目
    print(f"第 {i} 題：{sentence}")
    user_answer = input("請輸入答案：").strip()

    # 判斷答案正確性
    is_correct = user_answer == xi_ien or user_answer == hoi_liug
    if is_correct:
        print("答對了！\n")
        score += 1
    else:
        print(f"答錯了！正確答案可能是：{xi_ien} 或 {hoi_liug}\n")

    # 記錄結果
    results.append({
        "sentence": sentence,
        "xi-ien": xi_ien,
        "hoi-liug": hoi_liug,
        "user_answer": user_answer,
        "correct": is_correct
    })

# 顯示測驗結果
print(f"測驗結束！你獲得了 {score}/{num_questions} 分！\n")

# 顯示所有正確答案
print("以下是題目與正確答案：")
for result in results:
    print(f"題目：{result['sentence']}")
    print(f"正確答案：四縣 {result['xi-ien']} \n 海陸 {result['hoi-liug']}")
    print(f"你的答案：{result['user_answer']}")
    print(f"是否正確：{'正確' if result['correct'] else '錯誤'}\n")
