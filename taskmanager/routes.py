from flask import render_template
from taskmanager import app, db 
from taskmanager.models import Category, Task


#For simplicity to get the app running, we'll create a basic app route using the root-level directory of slash.
#This will be used to target a function called 'home', which will just return the rendered_template
#of "base.html" that we will create shortly.
@app.route("/")
def home():
    return render_template("tasks.html") #this is now the home page, before it was base.html page as we didnt have before the other html file
    