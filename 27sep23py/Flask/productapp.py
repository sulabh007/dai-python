from flask import Flask,render_template,redirect,request,url_for


import sqlite3
con=sqlite3.connect(r'db.sqlite3',check_same_thread=False)
if con!=None:
    print("Connection done")
    
cursor=con.cursor()

app=Flask(__name__)

@app.route('/')

def home():
    #return "hello world"
    return render_template('helloworld.html')

@app.route('/products')
def displayProduct():
    cursor.execute("select * from product")
    rows=cursor.fetchall()
    return render_template("displayproduct.html",data=rows)

@app.route('/acceptproduct')
def displayform():
    return render_template("productdata.html")

@app.route('/product/addproduct',methods=['POST'])
def addproduct():
    #id=request.form.get("pid")
    pname=request.form.get("pname")
    qty=request.form.get("qty")
    price=request.form.get("price")
    cursor.execute("insert into product (pname,qty,price) values(:pname,:qty,:pr)",(pname,qty,price))
    con.commit()
    #return "product"+pname+"  "+pid
    return redirect('/products')
    
@app.route("/delete/<id>")
def deleteprod():
    


if __name__=="__main__":
    app.run(debug=True)
    
