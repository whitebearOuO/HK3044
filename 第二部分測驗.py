import json
import os
import bear

#呼叫資料庫
data = "data.json"

#分數初始化
score = 0
#隨機變數
import random 

#提取隨機變數
random_choice = random.choice(data)
questions =list(random_choice.items())

#隨機挑五題
selected_questions = random.sample(questions, 5) 
correct_answer = (random_choice.items()) #這邊我有點不確定要怎麼顯示

#定義題數
number =1 

#用戶回答
user_answers={}

#遊戲開始
print("拼音測驗")
print("本次測驗一共有 5 題，請根據看到的諺語，拚寫出客語音標。 \n")

#迴圈
for _ in range(5):
    print("第 {number} 題，\n")
    print(random_choice)
    print("請輸入該諺語之客語拼音:")
    user_answers=input("問題： {} \n你的答案") #顯示自己的回答
    
    #比對答案
    if user_answers.strip() == correct_answer:
        print("你答對了！\n")
        score += 1  # 答對加一分
        number +=1
    
    elif 
    print("你答錯了！\n")
        number +=1

# 顯示分數
print(f"測驗結束！你獲得了{score}/5 分！\n")
def 
 print("<回到主菜單>")
        print()

# 顯示正確答案
print("以下是正確答案：")
for question ,correct_answer  in selected_questions：
    print(f"諺語：{question}")
    print(f"拼音：{correct_answer[]} \n ")



