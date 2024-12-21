import json
import os
import random 
#呼叫資料庫
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # 讀取 JSON 資料

#分數初始化
score = 0



#隨機五題
selected_questions = random.sample(list(data.items()), 5)

#定義題數
number =1 

#用戶回答
user_answers={}

#遊戲開始
print("拼寫測驗")
print("本次測驗一共有 5 題，請根據看到的諺語，拼寫出客語音標。 \n")

#迴圈
for i, (question, correct_answer) in enumerate(selected_questions, 1):
    print(f"第 {i} 題：{question}")
    user_answer = input("請輸入該諺語的客語拼音：").strip()

    # 判斷答案正確
    if user_answer == correct_answer:
        print("你答對了！\n")
        score += 1
    # 判斷答案錯誤
    else:
        print("你答錯了！\n")

# 顯示分數
print(f"測驗結束！你獲得了{score}/5 分！\n")
# 顯示正確答案
print("以下是正確答案：")
for question ,correct_answer  in selected_questions ：
    print(f"諺語：{question}")
    print(f"拼音：{correct_answer} \n ")



