import json
import random

def third():
    # 呼叫資料庫
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)  # 讀取 JSON 資料
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"讀取資料庫時出錯: {e}")
        exit()

    # 確保資料庫格式正確
    if not isinstance(data, list):
        print("資料庫格式錯誤，應該是題目列表格式！")
        exit()

    # 獲取所有日期範圍
    dates = [int(item["date"]) for item in data]  # 將日期轉為整數
    min_date, max_date = min(dates), max(dates)
    print(f"資料庫中共有 {len(dates)} 個諺語，日期範圍為：{min_date} 至 {max_date}。\n")

    # 用戶選擇日期範圍
    while True:
        try:
            start_date = int(input(f"請輸入起始日期（格式如 {min_date}）：").strip())
            end_date = int(input(f"請輸入結束日期（格式如 {max_date}）：").strip())

            # 範圍檢查
            if start_date < min_date or end_date > max_date or start_date > end_date:
                print("日期範圍錯誤，請確保起始日期和結束日期在正確範圍內且順序正確！\n")
                continue

            # 篩選範圍內的資料
            selected_data = [
                item for item in data if start_date <= int(item["date"]) <= end_date
            ]

            if selected_data:
                print(f"範圍內共有 {len(selected_data)} 題。\n")
                break
            else:
                print("範圍內無題目，請重新輸入日期範圍！")
        except ValueError:
            print("請輸入有效的日期數字！\n")

    # 用戶選擇題數
    while True:
        try:
            num_questions = int(input(f"請輸入想測驗的題數（最多 {len(selected_data)} 題）："))
            if 1 <= num_questions <= len(selected_data):
                break
            else:
                print(f"請輸入 1 到 {len(selected_data)} 之間的數字！")
        except ValueError:
            print("請輸入有效的整數！")

    # 隨機選取題目
    selected_questions = random.sample(selected_data, num_questions)

    # 初始化分數與記錄回答
    score = 0
    results = []  # 用於記錄題目與答案

    # 開始遊戲提示
    print("\n拼寫測驗\n")
    print(f"本次測驗共有 {num_questions} 題，請根據看到的句子，輸入正確的拼音(四縣腔與海陸腔均可。\n")

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
        print(f"正確答案：{result['xi-ien']} 或 {result['hoi-liug']}")
        print(f"你的答案：{result['user_answer']}")
        print(f"是否正確：{'正確' if result['correct'] else '錯誤'}\n")
