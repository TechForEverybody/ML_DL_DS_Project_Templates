from flask import Flask,render_template,request,jsonify

App=Flask(__name__)

@App.route("/")
def index():
    return render_template("index.html")