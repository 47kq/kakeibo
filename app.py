from flask import Flask,render_template,request,redirect

app=Flask(__name__)

expenses=[]

@app.route("/",methods=["GET","POST"])
def index():    
    
    
    if request.method=="POST":
        date=request.form["date"]
        item=request.form["item"]
        category=request.form["category"]
        amount=request.form["amount"]
        
        expenses.append({
            "date":date,
            "item":item,
            "category":category,
            "amount":amount
        })
        
    return render_template("index.html",expenses=expenses)
    

if __name__=="__main__":
    app.run(debug=True)