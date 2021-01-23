from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField, FileField
from wtforms.validators import DataRequired


class SolveQuestionForm(FlaskForm):
    body = r"Kolik je \(\sqrt{\left(\frac{-42}{42}\right)^2}\)?"
    typ = "multiple"
    options = RadioField("Možnosti odpovědi", choices=[r"\(\frac{1}{42}\)", r"\(\pm i\)", "Whizzmot", r"\(\mathrm\LaTeX\)"])
    submit = SubmitField('Submit')
