from flask import Flask,render_template,request,redirect
import sqlite3

app=Flask(__name__)

expenses=[]

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
    
    conn.close()
    
    #合計
    total =sum(e[4] for e in expenses)
    
    return render_template("index.html",expenses=expenses,total=total)
    

if __name__=="__main__":
    app.run(debug=True)