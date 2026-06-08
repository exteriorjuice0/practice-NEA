from flask import Blueprint, redirect, render_template, session

from lib.isAuthed import isAuthed



private = Blueprint("private",__name__)

@private.before_request
def privateGate():
    if not isAuthed():
        return redirect("/")

@private.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@private.route("/signout")
def signout():

    session.clear()

    return redirect("/")

@private.route("/settings")
def settings():
    return render_template("settings.html")