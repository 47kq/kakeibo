import csv
import os

expenses=[]

#==実行時にcsvを読み込む==
if os.path.exists("kakeibo.csv"):
    with open("kakeibo.csv",newline="",encoding="utf-8") as f:
        reader=csv.reader(f)
        for row in reader:
            item=row[0]
            amount =int(row[1])
            expenses.append((item,amount))

#==メインループ==
while True:
    print("\n1: 追加 2: 一覧 3: 終了")
    choice = input("選択: ")
    
    if choice=="1":
        item=input("内容: ")
        amount=int(input("金額: "))
        expenses.append((item,amount))
        
        #csvに保存
        with open("kakeibo.csv",mode="a",newline="",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerow([item,amount])
        
        print("追加しました")
        
    elif choice=="2":
        total=0
        for item,amount in expenses:
            print(item,amount)
            total += amount
        print("合計:",total)
        
    elif choice=="3":
        break
    
    else:
        print("無効な選択")