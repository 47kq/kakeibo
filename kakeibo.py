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

#==追加==
def add_expense():
    item=input("内容: ")
    amount=int(input("金額: "))
    expenses.append((item,amount))
        
    #csvに保存
    with open("kakeibo.csv",mode="a",newline="",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow([item,amount])
        
    print("追加しました")
        
#==一覧==
def show_expenses():
    total=0
    for i,(item,amount) in enumerate(expenses):
        print(i,item,amount)
        total += amount
    print("合計:",total)
    
#==削除==
def delete_expense():
    delete_index=int(input("削除する番号を入力: "))
        
    if 0<=delete_index<len(expenses):
        expenses.pop(delete_index)
            
        #csvを書き直す
        with open("kakeibo.csv",mode="w",newline="",encoding="utf-8") as f:
            writer=csv.writer(f)
            for item,amount in expenses:
                writer.writerow([item,amount])
                    
        print("削除しました")
            
    else:
        print("無効な値です")

#==メインループ==
def main():
    while True:
        print("\n1: 追加 2: 一覧  3: 削除 4: 終了")
        choice = input("選択: ")
    
        if choice=="1":
            add_expense()
        elif choice=="2":
            show_expenses()
        elif choice=="3":
            delete_expense()
        elif choice=="4":
            break
        else:
            print("無効な選択")
        
#==実行==
main()