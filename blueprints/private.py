from flask import Blueprint, flash, redirect, render_template, request, session

from database import DatabaseHandler
from lib.isAuthed import isAuthed
from lib.isValidLength import isValidLength



private = Blueprint("private",__name__)
db = DatabaseHandler()

@private.before_request
def privateGate():
    if not isAuthed():
        return redirect("/")

@private.route("/dashboard")
def dashboard():
    username = session.get("currentUser")
    success,tasks = db.readAllTasks(username)

    if not success:
        flash("Failed to fetch tasks")
        return redirect("/dashboard")
    
    return render_template("dashboard.html", tasks = tasks)

@private.route("/signout")
def signout():

    session.clear()

    return redirect("/")

@private.route("/settings")
def settings():
    return render_template("settings.html")

@private.route("/addtask", methods = ["POST","GET"])
def addTask():
    if request.method == "POST":
        formData = request.form
        description = formData.get("description")
        username = session.get("currentUser")
        
        if username == None:
            flash("No user found")
            return redirect("/addtask")

        if not isValidLength(description, 2, 500):
            flash("Invalid Description")
            return redirect("/addtask")
        success,message = db.createTask(description, username)

        if not success:
            flash(message)
            return redirect("/addtask")
        
        flash(message)
        return redirect("/dashboard")
        

    return render_template("addtask.html")