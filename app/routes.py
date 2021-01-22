from app import app
from flask import render_template, redirect

from .forms import SampleForm
from .create_question import CreateQuestionForm


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
    if form.validate_on_submit():
        return redirect('index')

    return render_template('create-question.html', form=form)


@app.route('/forms', methods=['GET', 'POST'])
def forms():
    form = SampleForm()

    # If form is upon submission and is validated success
    if form.validate_on_submit():
        return redirect('index')

    return render_template('forms.html', form=form)
