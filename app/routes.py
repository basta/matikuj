from app import app, db
from flask import render_template, redirect, request

from .forms import SampleForm
from .forms import SessionCreator, SimpleButton
from .models import Problem, Quiz
from .create_question import CreateQuestionForm
from .basta import *
from .create_question import CreateQuestionForm
from .solve_question import SolveQuestionForm

from typing import List, Dict


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/articles')
def articles():
    return render_template('articles.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/teacher')
def teacher():
    return render_template('teacher.html')


@app.route('/sample_problem')
def sample_problem():
    return render_template('sample_problem.html')


@app.route('/answer-question', methods=['GET', 'POST'])
def solve_question():
    form = SolveQuestionForm()
    if form.validate_on_submit():
            return redirect('index')
    print(request.form)
    return render_template('solve-question.html', form=form)


@app.route('/create-question', methods=['GET', 'POST'])
def create_question():
    form = CreateQuestionForm()

    # If form is upon submission and is validated success
    if request.method == "POST":
        #Defaults
        image64 = None
        options = None
        options_type = None


        data = request.form
        print(data)
        typ = data["typ"]
        body = data["body"]
        difficulty = data["difficulty"]
        tags = data["tags"]
        submitter = 1
        print("typ:",typ, type(typ))
        if typ == "field":
            result = data["result_field"]
        elif typ == "multiple":
            print("jsem tu")
            result = "0"
            if data["multiple_ans_type"] == "field":
                options = "|delim|".join(data.getlist("multiple_ans_field"))
                options_type = "field"
                print("Options:", options)
            elif data["multiple_ans_type"] == "graph":
                pass
            elif data["multiple_ans_type"] == "image":
                pass

        problem = Problem(
            typ = typ,
            body = body,
            difficulty = difficulty,
            tags = tags,
            result = result,
            options = options,
            options_type = options_type,
            image64 = data["image64"],
            submitter = 1)
        
        db.session.add(problem)
        db.session.commit()
        if form.validate_on_submit():
            return redirect('index')

    print(request.form)
    return render_template('create-question.html', form=form)


@app.route('/forms', methods=['GET', 'POST'])
def forms():
    form = SampleForm()

    data = request.database
    

    # If form is upon submission and is validated success
    if form.validate_on_submit():
        return redirect('index')

    return render_template('forms.html', form=form)


sessions: Dict[str, Session] = {}
@app.route("/session/", methods=["GET", "POST"])
def session_create():
    form = SessionCreator()
    print("session page")
    if request.method == "POST":
        #Join
        print(request.form)
        if "join" in request.form:
            sid = request.form["text"]
            if sid in sessions:
                member = Member(Member.random_id(), sid)
                sessions[sid].add_member(member)
            return redirect("/session/"+sid+"/user")
        #Create
        if "create" in request.form:
            sid = Session.random_id()
            sessions[sid] = Session(sid)
            return redirect("/session/"+sid+"/admin")
    else:
        return render_template("session_create.html", form=form)


@app.route("/session/<string:sid>/admin")
def session_admin(sid):
    if not sid in sessions:
        return "Neplatne ID"
    
    session = sessions[sid]
    print(session.members)
    return render_template("session_admin.html", session=session)


@app.route("/session/<string:sid>/user")
def session_user(sid):
    if not sid in sessions:
        return "Neplatne ID"
    
    session = sessions[sid]
    return render_template("session_user.html", session=session)

@app.route("/create-quiz", methods=["POST", "GET"])
def create_quiz():
    if request.method == "POST":
        data = request.data.decode("utf-8").split()
        data = [i.split("-")[1] for i in data]
        print(data)
        quiz = Quiz(typ="WIP",
                    name="WIP",
                    difficulty=0,
                    problems=" ".join(data),
                    submitter=0,
                    views=1
                    )

        db.session.add(quiz)
        db.session.commit()
        return redirect("/index")
    else:
        questions = Problem.query.all()
        print(questions)
        return render_template("create-quiz.html", questions = questions, form=SimpleButton())

