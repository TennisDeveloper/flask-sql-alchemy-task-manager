from flask import render_template, request, redirect, url_for #request is for the database to update data
from taskmanager import app, db 
from taskmanager.models import Category, Task


#For simplicity to get the app running, we'll create a basic app route using the root-level directory of slash.
#This will be used to target a function called 'home', which will just return the rendered_template
#of "base.html" that we will create shortly.
@app.route("/")
def home(): #this is the python function not the html site
    return render_template("tasks.html") #this is now the home page, before it was base.html page as we didnt have before the other html file


@app.route("/categories") #html site
def categories(): #this is the python function not the html site
    return render_template("categories.html")

#The app route will be "/add_category", and this time we need to include a list of the
# two methods "GET" and "POST", since we will be submitting a form to the database.
# Our function name will match 'add_category', which, if you recall, is the same name we
# added to the link href to target this function that we're creating now.
# When a user clicks to add a new category, it should render the template that contains
# a form, and by displaying the form to users, this uses the "GET" method to 'get' the page.
# We can copy the render template line from one of the functions above, and just replace
# the template name with 'add_category.html'.
# However, when a user eventually submits this form, the form will attempt to 'post' the
# data into the database, and this is why we need to specify both methods in the app route.
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category= Category(category_name= request.form.get("category_name"))                #this is a new instance of the imported Category model
        db.session.add(category)  #Once we've grabbed the form data, we can then 'add' and 'commit' this information to the SQLAlchemy database variable of 'db' imported at the top of the file.
        db.session.commit()
        return redirect(url_for("categories")) #After the form gets submitted, and we're adding and committing the new data to our database, we could redirect the user back to the 'categories' page.
    return render_template("add_category.html") #this is like else block of the if statement. by default the normal method is GET

