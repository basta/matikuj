from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField, FileField
from wtforms.validators import DataRequired


class SolveQuestionForm(FlaskForm):
    body = "Toto je dlouhý text se zadáním otázky. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nihil enim accusamus nam illum rerum odio rem aspernatur obcaecati facilis, ab reiciendis aut molestiae doloribus, officia incidunt necessitatibus amet praesentium tenetur."
    typ = "multiple"
    options = RadioField("Možnosti odpovědi", choices=["Možnost "+str(i) for i in range(4)])
    submit = SubmitField('Submit')
