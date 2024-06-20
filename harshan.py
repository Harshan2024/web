from utils import *
from main import *
from flask import Flask,render_template,request,redirect,session
from flask_session import Session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["secret_key "] = "SECRET KEY"
Session(app)
app=Flask(__name__)
def session_valid():
     try:
        if  session["name"]:
            return True
        else:
            return False
     except:
         return False

# @app.route("/")
# def index():
#     if not session.get("name"):
#         return redirect("/login")
#     return render_template("harshan.html")
      
            
@app.route("/login",methods=["GET","POST"])
def login():
    print(request.method)
    data=read_json(FILE="json/mail.json")
    if request.method=="POST":
        session["name"] = request.form.get("name")
        print(session["name"])
        return redirect("/")
    write_json(data,FILE="json/mail.json")
    
    return render_template("harshan_2.html")
    

 
@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

@app.route("/",methods=["GET","POST"])
def homepage():
 if  session_valid():
    print("session valid")
    if request.method=="POST":
        student_registration(request.form["Name"],request.form["Age"],request.form["Course"],request.form["Duration"])
    data=read_json()
    return render_template("harshan.html",students=data["student"])
 else:
     return redirect("/login")
 
@app.route("/delete/<id>",methods=["GET","POST"])
def delete(id):
   if  session_valid(): 
    name=delete_stud(int(id))
    # return render_template("harshan.html",students=data["student"],name=name)
    return redirect("/"+name)
   else:
     return redirect("/login")

@app.route("/update/<id>",methods=["GET","POST"])
def update(id):
  if  session_valid():   
    if request.method=="GET":
        data=read_json()
        for i in data["student"]:
          if i["sno"]==(int(id)):
              
                return render_template("harshan_2.html",std=i)
    else:
            
        update_stud(int(id),request.form["Name"],request.form["Age"],request.form["Course"],request.form["Duration"])
        return redirect("/")
  else:
     return redirect("/login")  
        
if __name__=="__main__":
    app.secret_key = 'SECRET KEY'
    app.run(debug=True,host="0.0.0.0")