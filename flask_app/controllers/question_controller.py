from flask_app import app
from flask import render_template, session, redirect, request, jsonify
from flask_app.models.question_model import State, Trigger

@app.route("/add")
def add_questions():
    return render_template("add_questions.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/dashboard")
def dashboard():
    if 'state'not in session:
        session['state'] = State.QUESTION_1.value
        session['answers'] = []
    return render_template("new_dashboard.html")

@app.route("/loading")
def loading():
    return render_template("loading_page.html")

@app.post('/process_answer')
def process_answer():
    session['state'] = request.form['next_state']
    session['answers'].append(request.form['answer'])
    print(session['answers'])
    return redirect('/dashboard')    

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/dashboard')
