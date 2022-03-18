
from flask import Flask, render_template, redirect, request
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.user import User

@app.route('/') 
def index():
    mysql = connectToMySQL("users_schema")
    users = mysql.query_db("SELECT * FROM users;")
    print(users)
    return render_template("read.html", all_users = users)      

# new page for the data- just the display of new user
@app.route ('/user/new')
def new_user():
    return render_template("create.html")

#show
@app.route ('/users/<int:id>')
def show_user(id):
    data = {"id": id}
    user = User.get_one(data)
    return render_template ("show_user.html", user=user)

# edit
@app.route("/users/edit/<int:id>")
def edit_user(id):
    user = User.get_one({"id":id})
    return render_template("edit_user.html", user=user)


# action routes!!!!-----------------------------------------------------
# what we are doing on the templates (new user) action routes!
@app.route ('/user/create', methods=["POST"])
def create_user():
    User.make_user(request.form)
    return redirect('/')

@app.route('/users/update/<int:id>', methods=["POST"])
def update_the_user(id):
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id": id
    }
    User.update_user(data)
    return redirect('/')


@app.route("/users/<int:id>/delete")
def delete_user(id):
    data = {
    "id": id
    }
    User.delete_user(data) 
    return redirect('/')