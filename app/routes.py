from app import app
from flask import render_template, redirect, request

from .forms import SampleForm
from .models import Problem


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/articles')
def articles():
    return render_template('articles.html')


@app.route('/create-question', methods=['GET', 'POST'])
def create_question():
    form = CreateQuestionForm()

    # If form is upon submission and is validated success
    data = request.form
    problem = Problem(
        typ = data["typ"],
        body = data["body"],
        difficulty = data["difficulty"],
        tags = data["tags"],
        result = data["result"],
        image64 = data["image64"],
        submitter = data["submitter"])
    
    db.session.add(problem)
    db.session.commit()
    if form.validate_on_submit():
        return redirect('index')
<<<<<<< HEAD

    print(request.form)
=======
>>>>>>> 705a81486a4cb34a7e470719cda298e2da160c8c
    return render_template('create-question.html', form=form)


@app.route('/forms', methods=['GET', 'POST'])
def forms():
    form = SampleForm()

    data = request.database
    

    # If form is upon submission and is validated success
    if form.validate_on_submit():
        return redirect('index')

    return render_template('forms.html', form=form)
