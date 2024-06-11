from utils import *
from main import *
from flask import Flask,render_template,request,redirect

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
    data=read_json()
    route="/"+name
    # return render_template("harshan.html",students=data["student"],name=name)
    return redirect(route)



if __name__=="__main__":
    app.run(debug=True)