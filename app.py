from flask import Flask,render_template,request,redirect

app=Flask(__name__)

expenses=[]

@app.route("/",methods=["GET","POST"])
def index():    
    
    if request.method == "POST" and "delete" in request.form:
        delete_index = int(request.form["delete"])
        if 0<=delete_index < len(expenses):
            expenses.pop(delete_index)
        return redirect("/")
    
    
    
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
        return redirect("/")
    
    total =sum(int(e["amount"]) for e in expenses)
    return render_template("index.html",expenses=expenses,total=total)
    

if __name__=="__main__":
    app.run(debug=True)