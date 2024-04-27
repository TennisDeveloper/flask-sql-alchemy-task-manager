from flask import render_template
from taskmanager import app, db 


#For simplicity to get the app running, we'll create a basic app route using the root-level directory of slash.
#This will be used to target a function called 'home', which will just return the rendered_template
#of "base.html" that we will create shortly.
@app.route("/")
def home():
    return render_template("base.html")
    