from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField, FileField
from wtforms.validators import DataRequired


class SolveQuestionForm(FlaskForm):
    body = r"Kolik je \(\sqrt{\left(\frac{-42}{42}\right)^{-e^{\pi i}}}\)?"
    typ = "multiple"
    options = RadioField("Možnosti odpovědi", choices=[r"\(\frac{1}{42}\)", r"\(\pm i\)", "Whizzmot", r"\(\mathrm\LaTeX\)"])
    submit = SubmitField('Potvrdit')

class HardcodedGraphQuestion(FlaskForm):
    body = r"Který z těchto grafů ukazuje monotónní funkci?"
    typ = "multiple"
    options = RadioField("Možnosti odpovědi", choices=[r"x^2-x-2", r"exp(-x)", r"abs(x)-4", r"3*sin(x)"])
    submit = SubmitField('Potvrdit')
