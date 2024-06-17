from utils import *
from main import *
from flask import Flask,render_template,request,redirect,session
from flask_session import Session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
                                                               
app=Flask(__name__)
@app.route("/<name>")
@app.route("/",methods=["GET","POST"])
def homepage(name=""):
    print(name)
    if request.method=="POST":
        student_registration(request.form["Name"],request.form["Age"],request.form["Course"],request.form["Duration"])
    data=read_json()
    return render_template("harshan.html",students=data["student"])

@app.route("/delete/<id>",methods=["GET","POST"])
def delete(id):
    name=delete_stud(int(id))
    # return render_template("harshan.html",students=data["student"],name=name)
    return redirect("/"+name)

@app.route("/update/<id>",methods=["GET","POST"])
def update(id):
    if request.method=="GET":
        data=read_json()
        for i in data["student"]:
          if i["sno"]==(int(id)):
              
                return render_template("harshan_2.html",std=i)
    else:
            
        update_stud(int(id),request.form["Name"],request.form["Age"],request.form["Course"],request.form["Duration"])
        return redirect("/")
        
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")