from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SampleForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name')
    email = StringField('Email')
    submit = SubmitField('Submit')

class SessionCreator(FlaskForm):
    text = StringField('Name:', render_kw={"placeholder": "ID", "style" : "width:234px; font-size: 25px; text-align: center;"})
    join = SubmitField("Připojit", render_kw={"style" : "width:250px; font-size: 25px; margin-top: 10px"})
    create = SubmitField("Vytvořit", render_kw={"style" : "width:250px; font-size: 25px; margin-top: 10px"})

class SimpleButton(FlaskForm):
    submit = SubmitField("Vytvořit")