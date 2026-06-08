from flask import Flask, render_template,request,redirect,flash,session
from blueprints.private import private
from lib.isValidLength import isValidLength
from database import DatabaseHandler
from lib.isPresent import isPresent
from werkzeug.security import check_password_hash, generate_password_hash
from blueprints.public import public

app = Flask(__name__)
app.secret_key = "tomEggletonIsAChud"

db = DatabaseHandler()
db.createTables()

app.register_blueprint(public)
app.register_blueprint(private)



app.run(debug=True)

