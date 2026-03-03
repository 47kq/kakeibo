import csv
import os
import datetime

expenses=[]

#==実行時にcsvを読み込む==
if os.path.exists("kakeibo.csv"):
    with open("kakeibo.csv",newline="",encoding="utf-8") as f:
        reader=csv.reader(f)
        for row in reader:
            date=row[0]
            item=row[1]
            category =row[2]
            amount=int(row[3])
            expenses.append((date,item,category,amount))
        for e in expenses:
            print(e)
        print("=============")

#==追加==
def add_expense():
    today=datetime.date.today().isoformat()
    item=input("内容: ")
    category=input("カテゴリ: ")
    
    while True:
        try:
            amount=int(input("金額: "))
            break
        except ValueError:
            print("数字を入力してください")
            
    expenses.append((today,item,category,amount))
        
    #csvに保存
    with open("kakeibo.csv",mode="a",newline="",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow([today,item,category,amount])
        
    print("追加しました")
        
#==一覧==
def show_expenses():
    total=0
    category_totals={}
    
    for i,(date,item,category,amount) in enumerate(expenses):
        print(i,date,item,category,amount)
        total += amount
        
        if category in category_totals:
            category_totals[category]+=amount
        else:
            category_totals[category]=amount
    
    print("\n--- カテゴリ別合計 ---")
    for category,amount in category_totals.items():
        print(category,":",amount)
    
    print("\n合計:",total)
    
#==削除==
def delete_expense():
    delete_index=int(input("削除する番号を入力: "))
        
    if 0<=delete_index<len(expenses):
        expenses.pop(delete_index)
            
        #csvを書き直す
        with open("kakeibo.csv",mode="w",newline="",encoding="utf-8") as f:
            writer=csv.writer(f)
            for date,item,category,amount in expenses:
                writer.writerow([date,item,category,amount])
                    
        print("削除しました")
            
    else:
        print("無効な値です")

def show_this_month_total():
    today=datetime.date.today()
    this_year=today.year
    this_month=today.month
    
    total=0
    
    for date,item,category,amount in expenses:
        year,month,day=map(int,date.split("-"))
        
        if year==this_year and month==this_month:
            total+=amount
            
    print("今月の合計:",total)

#==メインループ==
def main():
    while True:
        print("\n1: 追加 2: 一覧  3: 削除 4: 今月合計 5: 終了")
        choice = input("選択: ")
        
        
        if choice=="1":
            add_expense()
        elif choice=="2":
            show_expenses()
        elif choice=="3":
            delete_expense()
        elif choice=="4":
            show_this_month_total()
        elif choice=="5":
            break
        else:
            print("無効な選択")
        
#==実行==
if __name__ =="__main__":
    main()