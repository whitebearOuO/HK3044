import json
import random

def second_2():
    # 初始化一個空的列表，用於儲存測試資料
    test_data = []

    # 清空 test_data.json 檔案，確保檔案內容為空
    with open('test_data.json', 'w', encoding='utf-8') as f:
        json.dump(test_data, f)

    # 提示使用者進入自訂考試模式，並說明輸入格式
    print("此為自訂考試模式，需自行輸入諺語及拼音。")
    print("輸入格式為如下：")
    print("請輸入諺語：（諺語）")
    print("請輸入拼音：（拼音）")
    print()

    # 進入無限迴圈，等待使用者輸入
    while 1:
        # 計算當前輸入的諺語數量
        input_counter = len(test_data) + 1
        print("現在正在輸入第" + str(input_counter) + "個諺語。")
        
        # 接收使用者輸入的諺語和拼音
        sentence = input("請輸入諺語： ")
        pinyin = input("請輸入拼音： ")
        
        # 將輸入的資料存入字典並添加到列表中
        entry = {
            "number": input_counter,
            "sentence": sentence,
            "pinyin": pinyin
        }
        test_data.append(entry)
        
        print()
        # 詢問使用者是否繼續輸入
        choose = input("請問要繼續輸入嗎[y/n]：").lower()
        if choose == "y":
            print()
            continue
        else:
            print()
            while True:
                # 顯示已輸入的所有諺語和拼音
                print("您輸入的內容如下：")
                for entry in test_data:
                    print(f"第 {entry['number']} 個\n諺語： {entry['sentence']}\n拼音： {entry['pinyin']}\n")
                
                # 詢問使用者是否需要修改任何內容
                modify = input("是否需要修改任何內容？[y/n]：").lower()
                if modify == 'y':
                    print()
                    modify_number = int(input("請輸入要修改的諺語編號："))
                    for entry in test_data:
                        if entry['number'] == modify_number:
                            entry['sentence'] = input("請輸入新的諺語：")
                            entry['pinyin'] = input("請輸入新的拼音：")
                            break
                else:
                    print()
                    break
                
            
            # 將 test_data 寫入 test_data.json
            with open('test_data.json', 'w', encoding='utf-8') as f:
                json.dump(test_data, f, ensure_ascii=False, indent=4)
            break

    # 開始進行測驗
    print("開始進行測驗，總共有" + str(len(test_data)) + "題。")
    print()

    # 從 test_data.json 讀取資料
    test_data = []
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

    # 顯示測驗結果
    print(f"測驗結束，你答對了 {correct_count} 題，共 {len(test_data)} 題。")
    accuracy = correct_count / (len(test_data)) * 100
    print(f"您的正確率是：{accuracy:.2f}%")
    print()
    print("<回到主菜單>")
    print()