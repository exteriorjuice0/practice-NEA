from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("signup.html")


@app.route("/signup", methods = ["POST"])
def signup():
    formdata = request.form
    username = formdata.get("username")
    password = formdata.get("password")
    repassword = formdata.get("repassword")

    
    print(username)

    return "signing up..."
app.run(debug=True)

