from flask import Flask,render_template,request,redirect
import sqlite3

app=Flask(__name__)


def init_db():
    conn=sqlite3.connect("kakeibo.db")

    conn.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    item TEXT,
    category TEXT,
    amount INTEGER
    )             
    """)

    conn.close()

init_db()

@app.route("/",methods=["GET","POST"])
def index():    
    
    if request.method == "POST" and "delete" in request.form:
        delete_index = int(request.form["delete"])
        
        conn=sqlite3.connect("kakeibo.db")
        
        conn.execute("DELETE FROM expenses WHERE id=?", (delete_index,))
        
        conn.commit()
        conn.close()
        
        return redirect("/")
    
    
    
    if request.method=="POST":
        date=request.form["date"]
        item=request.form["item"]
        category=request.form["category"]
        amount=request.form["amount"]
        
        conn=sqlite3.connect("kakeibo.db")
        
        conn.execute(
            "INSERT INTO expenses(date,item,category,amount) VALUES(?,?,?,?)",
            (date,item,category,amount)
        )
        conn.commit()
        conn.close()
        
        return redirect("/")
    
    #データ取得
    conn=sqlite3.connect("kakeibo.db")
    
    cursor = conn.execute("SELECT*FROM expenses")
    
    expenses=cursor.fetchall()
    
    
    #合計
    total =sum(e[4] for e in expenses)
    
    #カテゴリ別合計
    cursor=conn.execute("""
    SELECT category ,SUM(amount)
    FROM expenses                    
    GROUP BY category
    """)
    
    category_totals=cursor.fetchall()
    
    cursor=conn.execute("""
    SELECT date,SUM(amount)
    FROM expenses
    GROUP BY date
    ORDER BY date DESC                                        
    """)
    day_data=cursor.fetchall()
    
    cursor=conn.execute("""
    SELECT strftime('%Y-%m',date),SUM(amount)
    FROM expenses 
    GROUP BY strftime('%Y-%m',date)
    ORDER BY strftime('%Y-%m',date) DESC
    """)
    month_data=cursor.fetchall()
    
    cursor=conn.execute("""
    SELECT strftime('%Y',date),SUM(amount)
    FROM expenses
    GROUP BY strftime('%Y',date)
    ORDER BY strftime('%Y',date) DESC
    """)
    year_data=cursor.fetchall()
    
    
    
    conn.close()
    
    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        category_totals=category_totals,
        day_data=day_data,
        month_data=month_data,
        year_data=year_data
    )
    
@app.route("/edit/<int:id>")
def edit(id):
    conn=sqlite3.connect("kakeibo.db")
    cursor=conn.execute("SELECT * FROM expenses WHERE id=?",(id,))
    expense=cursor.fetchone()
    conn.close()
    
    return render_template("edit.html",expense=expense)

@app.route("/update/<int:id>",methods=["POST"])
def update(id):
    date=request.form["date"]
    item=request.form["item"]
    category=request.form["category"]
    amount=int(request.form["amount"])
    
    conn=sqlite3.connect("kakeibo.db")
    
    conn.execute("""
        UPDATE expenses
        SET date=?,item=?,category=?,amount=?
        WHERE id=?            
    """,(date,item,category,amount,id))
    
    conn.commit()
    conn.close()
    
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)