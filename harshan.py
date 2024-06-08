from utils import *
from main import *
from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def homepage():
    if request.method=="POST":
        student_registration(request.form["Name"],request.form["Age"],request.form["Course"],request.form["Duration"])
    data=read_json()
    return render_template("harshan.html",students=data["student"])

if __name__=="__main__":
    app.run(debug=True)