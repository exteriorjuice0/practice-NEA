from flask import Flask
from blueprints.private import private
from database import DatabaseHandler
from blueprints.public import public

app = Flask(__name__)
app.secret_key = "tomEggletonIsAChud"

db = DatabaseHandler()
db.createTables()

app.register_blueprint(public)
app.register_blueprint(private)



app.run(debug=True)

