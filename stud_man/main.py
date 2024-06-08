from oper import *
from flask import Flask, render_template, request


app=Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method=="POST":
        registration(request.form["name"],request.form["age"],request.form["course"],request.form["duration"])
    return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True)

# from flask