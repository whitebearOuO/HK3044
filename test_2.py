import json
import random

test_data = []

# 清空 test_data.json 的內容
with open('test_data.json', 'w', encoding='utf-8') as f:
    json.dump(test_data, f)

print("此為自訂考試模式，需自行輸入諺語及拼音。")
print("輸入格式為如下：")
print("請輸入諺語：（諺語）")
print("請輸入拼音：（拼音）")
print()

while 1:
    input_counter = len(test_data) + 1
    print("現在正在輸入第" + str(input_counter) + "個諺語。")
    sentence = input("請輸入諺語： ")
    pinyin = input("請輸入拼音： ")
    entry = {
        "number": input_counter,
        "sentence": sentence,
        "pinyin": pinyin
    }
    test_data.append(entry)
    
    print()
    choose = input("請問要繼續輸入嗎[y/n]：").lower()
    if choose == "y":
        print()
        continue
    else:
        while True:
            print("您輸入的內容如下：")
            for entry in test_data:
                print(f"第 {entry['number']} 個\n諺語： {entry['sentence']}\n拼音： {entry['pinyin']}\n")
            
            modify = input("是否需要修改任何內容？[y/n]：").lower()
            if modify == 'y':
                modify_number = int(input("請輸入要修改的諺語編號："))
                for entry in test_data:
                    if entry['number'] == modify_number:
                        entry['sentence'] = input("請輸入新的諺語：")
                        entry['pinyin'] = input("請輸入新的拼音：")
                        break
            else:
                break
        
        # 將 test_data 寫入 test_data.json
        with open('test_data.json', 'w', encoding='utf-8') as f:
            json.dump(test_data, f, ensure_ascii=False, indent=4)
        break

print("開始進行測驗，總共有" + str(len(test_data)) + "題。")
print()

# 從 test_data.json 讀取資料
with open('test_data.json', 'r', encoding='utf-8') as f:
    test_data = json.load(f)

# 隨機打亂 test_data 的順序
random.shuffle(test_data)

# 測驗過程
correct_count = 0
for entry in test_data:
    print(f"請輸入諺語的拼音： {entry['sentence']}")
    user_pinyin = input("拼音： ")
    if user_pinyin == entry['pinyin']:
        print("恭喜答對！")
        print()
        correct_count += 1
    else:
        print(f"錯誤，正確的拼音是： {entry['pinyin']}")
        print()

print(f"測驗結束，你答對了 {correct_count} 題，共 {len(test_data)} 題。")
accuracy = correct_count / (len(test_data)) * 100
print(f"您的正確率是：{accuracy:.2f}%")
print()
print("<回到主菜單>")
print()