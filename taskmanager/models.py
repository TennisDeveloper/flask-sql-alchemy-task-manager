#Since we will be defining the database, we obviously need to import db from the main taskmanager package.
from taskmanager import db

#we will be creating two separate tables, which will be represented by class-based models using SQLAlchemy's ORM.
# The first table will be for various categories, so let's call this class 'Category', which
# will use the declarative base from SQLAlchemy's model.
#If you recall from the last few lessons, we had to specifically import each column type at the top of the file.
# However, with Flask-SQLAlchemy, the 'db' variable contains each of those already, and we can
# simply use dot-notation to specify the data-type for our columns.
#By the way, you can see a full list of column and data types from the SQLAlchemy docs, which
# include Integer, Float, Text, String, Date, Boolean, etc.

class Category(db.Model):
    #schema for the Category model
    id= db.Column(db.Integer,primary_key=True)
    category_name= db.Column(db.String(25), unique = True, nullable = False)
    # this creates relationship, backref= category which is as many to one itself relationship. 
    # Also, it needs to have the 'cascade' parameter set to 'all, delete' which means it will find 
    # all related tasks and delete them. The last parameter here is lazy=True, which means that when 
    # we query the database for categories, it can simultaneously identify any task linked to the categories.
    tasks= db.relationship("Task", backref= "category", cascade= "all,delete", lazy= True) 

    def __repr__(self):
        #For each model, we also need to create a function called __repr__ that takes itself as the argument,
        # similar to the 'this' keyword in JavaScript.
        # This is a standard Python function meaning "represent", which means to represent the class objects as a string.
        return self.category_name


class Task(db.Model):
    #schema for the Task model
    id= db.Column(db.Integer,primary_key=True)
    task_name= db.Column(db.String(50), unique = True, nullable = False)
    task_description = db.Column(db.Text, nullable = False) #this allows longer strings to be used similar as text area
    is_urgent= db.Column(db.Boolean, default=False, nullable=False)
    due_date= db.Column(db.Date, nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False) #use lower case to refer to Cateogory class, once a category is deleted, it will perform a cascading effect and also delete any task linked to it.


    def __repr__(self):
        return"#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )