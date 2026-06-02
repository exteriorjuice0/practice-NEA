from flask import Flask, render_template,request,redirect,flash
from lib.isValidLength import isValidLength
from database import DatabaseHandler
from lib.isPresent import isPresent
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "tomEggletonIsAChud"

db = DatabaseHandler()
db.createTables()

@app.route("/")
def home():
    if request.method =="GET":
     return render_template("login.html")

    
    if request.method == "POST":
        formData = request.form
        username = formData.get("username")
        password = formData.get("password")

        success, passwordHash = db.readUserPasswordHash(username)

        if not success or passwordHash == None:
            flash("an error occured")
            return redirect("/")

        if not check_password_hash(passwordHash[0], password):
            flash("invalid login details")
            return redirect("/")
        
        return redirect("/dashboard")


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
    
    hashedPassword = generate_password_hash(password)

    db_success, message = db.createUser(username,hashedPassword)

    if not db_success:
       flash(message)
       return redirect ("/signup")
    
    return redirect("/dashboard")
    
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

app.run(debug=True)

