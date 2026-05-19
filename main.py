from flask import Flask, render_template,request,redirect,flash

from lib.isValidLength import isValidLength
from lib.isPresent import isPresent

app = Flask(__name__)
app.secret_key = "tomEggletonIsAChud"

@app.route("/")
def home():
    if request.method =="GET":
     return render_template("login.html")
    
    return "Logging in..."


@app.route("/signup", methods = ["POST","GET"])
def signup():

    if request.method == "GET":

        return render_template("signup.html")

    formdata = request.form
    username = formdata.get("username")
    password = formdata.get("password")
    repassword = formdata.get("repassword")

    success = True

    if not isPresent(username):
        success = False
        flash("No username provided")

    if not isValidLength(password,8,100):
        success = False
        flash("Password must be at least 8 characters")

    if not isValidLength(repassword,8,100):
        flash("Confirmed password must be at least 8 characters")
        success = False


    if password!= repassword:
        success = False
        flash("Passwords do not match")

    if not success:
        return redirect("/signup")

    return "signing up..."
app.run(debug=True)

