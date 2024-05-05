from flask import render_template, request, redirect, url_for #request is for the database to update data
from taskmanager import app, db 
from taskmanager.models import Category, Task


#For simplicity to get the app running, we'll create a basic app route using the root-level directory of slash.
#This will be used to target a function called 'home', which will just return the rendered_template
#of "base.html" that we will create shortly.
@app.route("/")
def home(): #this is the python function not the html site
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks= tasks) #this is now the home page, before it was base.html page as we didnt have before the other html file


@app.route("/categories") #html site
def categories(): #this is the python function not the html site
    categories = list(Category.query.order_by(Category.category_name).all()) # I am querying here all the categories and ordering the categories by name. .all() method is a cursor object, which is similar to an array or list of records. There is a simple method which converts the cursor object data into list.
    return render_template("categories.html", categories=categories) #categories as name of the html template = variable categories has to be passed to rendered object to display that to user

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

@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"]) #I need to add the integer of the category.id column which has variable defined as category_id on the categories.html file
def edit_category(category_id): #variable needs to be passed to the function as well
    category= Category.query.get_or_404(category_id) #What this does is query the database and attempts to find the specified record using the data provided, and if no match is found, it will trigger a 404 error page.
    if request.method == "POST":
        category.category_name= request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    
    return render_template("edit_category.html", category= category) #Now, we can pass that variable into the rendered template, which is expecting it to be called 'category', and that will be set to the defined 'category' variable above.

@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category= Category.query.get_or_404(category_id)
    db.session.delete(category) #here I need to delete the variable
    db.session.commit()
    return redirect(url_for("categories"))

#route decorator for adding the task.
#If you recall from the video where we designed our database schema, each task actually requires
# the user to select a category for that task.
# In order to do that, we first need to extract a list of all of the categories available from the database.

@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task = Task(
            task_name= request.form.get("task_name"),
            task_description= request.form.get("task_description"),
            is_urgent= bool(True if request.form.get("is_urgent") else False),
            due_date= request.form.get("due_date"),
            category_id= request.form.get("category_id")
        )
        #this is a new instance of the imported Category model
        db.session.add(task)  #Once we've grabbed the form data, we can then 'add' and 'commit' this information to the SQLAlchemy database variable of 'db' imported at the top of the file.
        db.session.commit()
        return redirect(url_for("home")) #After the form gets submitted, and we're adding and committing the new data to our database, we could redirect the user back to the 'home' page.
    return render_template("add_task.html", categories= categories) #this is like else block of the if statement, meaning GET statement: if user wants to get a new task he needs to be redirected to the add_task.html, which contains the form for adding the task
    #first categories is a variable name, second categories is the list of categories under the ad_task(): function, this retrieves the whole list

@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task= Task.query.get_or_404(task_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task.task_name= request.form.get("task_name")
        task.task_description= request.form.get("task_description")
        task.is_urgent= bool(True if request.form.get("is_urgent") else False)
        task.due_date= request.form.get("due_date")
        task.category_id= request.form.get("category_id")
        db.session.commit()
        return redirect(url_for("home")) #After the form gets submitted, and we're adding and committing the new data to our database, we could redirect the user back to the 'home' page.
    return render_template("edit_task.html", task=task , categories= categories) #this is like else block of the if statement, meaning GET statement: if user wants to get a task he needs to be redirected to the edit_task.html, which contains the form for editing the task
    

