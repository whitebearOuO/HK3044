import os
import json

def third():
    # 如果檔案存在且不為空，讀取現有資料
    if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

    print("進行諺語測驗，可以選擇一段期間的諺語進行測驗。")
    print("並且選擇您需要的腔調。")
    print()

    while 1:
        print("請注意，開始日期必須小於結束日期，僅提供12月份諺語，日期格式1201。")
        print()
        date_start = input("請輸入開始日期： ")
        date_end = input("請輸入結束日期： ")
        if (date_start >= "1201" and date_end <= "1231" and (int(date_end) - int(date_start) >= 0)):
            correct_counter=0
            total=int(date_end)-int(date_start)+1
            speak = input("請輸入您要測驗的腔調:\n1.四縣\n2.海陸\n請輸入數字[1/2]: ")
            if (speak == "1" or speak == "2"):
                for date in range(int(date_start), int(date_end) + 1):
                    date_str = str(date)
                    for entry in data:
                        if entry["date"] == date_str:
                            print(f"{date_str}: {entry['sentence']}")
                            user_input = input("請輸入拼音： ")
                            correct_pinyin = entry['xi-ien'] if speak == "1" else entry['hoi-liug']
                            if user_input == correct_pinyin:
                                print("拼音正確！")
                                print()
                                correct_counter+=1
                            else:
                                print(f"拼音錯誤，正確拼音是：{correct_pinyin}")
                            break
                    else:
                        print(f"{date_str}: 無資料")
                accuracy = correct_counter / total * 100
                print(f"測驗完成，您的正確率是：{accuracy:.2f}%")
                print("<回到主菜單>")
                print()
                break
            else:
                print("輸入錯誤，請重新輸入。")
                print()
        else:
                print("輸入錯誤，請重新輸入。")
                print()