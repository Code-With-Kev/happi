from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user_model import User

#display route
@app.route("/")
def index():
        return render_template("login_page.html")



#action route
@app.route("/user/add", methods=['POST'])
def add_user ():
        
        if not User.validate_user(request.form):
                return redirect('/')

        user_id = User.create_user(request.form)

        session['user_id'] = user_id

        print(session['user_id'])
        return redirect("/profile")

@app.route("/user/login", methods=['POST'])
def login():
        user_status = User.login_user(request.form)
        if not user_status:
                return redirect('/')

        session['user_id'] = user_status.id
        return redirect('/profile')   

@app.route("/user/logout")
def logout():
        session.clear()
        return redirect("/")